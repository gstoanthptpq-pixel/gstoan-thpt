import streamlit as st
import streamlit.components.v1 as components
from streamlit_gsheets import GSheetsConnection
from google import genai
import pandas as pd
from PIL import Image
from gtts import gTTS
import os
import hashlib
import json
import io
import time
import re
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ==============================================================================
# 1. CẤU HÌNH GIAO DIỆN & TÙY BIẾN GIAO DIỆN SÁNG / TỐI (THEME)
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "theme_mode" not in st.session_state:
    st.session_state["theme_mode"] = "Sáng"

is_dark = st.session_state["theme_mode"] == "Tối"

bg_color = "#0F172A" if is_dark else "#F8FAFC"
card_bg = "#1E293B" if is_dark else "#FFFFFF"
text_color = "#F1F5F9" if is_dark else "#0F172A"
border_color = "#334155" if is_dark else "#E2E8F0"
subtext_color = "#94A3B8" if is_dark else "#475569"

st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    div[data-baseweb="popover"] ul, div[role="listbox"] {{
        max-height: 320px !important;
        overflow-y: auto !important;
    }}
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        border-radius: 14px !important;
        background-color: {card_bg} !important;
        border: 1px solid {border_color} !important;
        padding: 16px !important;
        margin-bottom: 14px !important;
    }}
    .stButton>button {{
        border-radius: 10px;
        background: linear-gradient(90deg, #1E3A8A, #2563EB);
        color: white;
        font-weight: 600;
        border: none;
        padding: 8px 18px;
        transition: all 0.25s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}
    .audio-box {{
        background: {("#1E3A5F" if is_dark else "linear-gradient(135deg, #F0FDF4, #DCFCE7)")};
        border: 1px solid {("#2563EB" if is_dark else "#86EFAC")};
        color: {text_color};
        padding: 12px;
        border-radius: 10px;
        margin-top: 12px;
    }}
    .topic-card {{
        background-color: {card_bg};
        color: {text_color};
        border-left: 5px solid #2563EB;
        padding: 10px 14px;
        border-radius: 6px;
        margin-top: 14px;
        margin-bottom: 8px;
    }}
    .adv-box {{
        background: {("#312E81" if is_dark else "linear-gradient(135deg, #EEF2FF, #E0E7FF)")};
        border: 1px solid #6366F1;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 16px;
    }}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. KHỞI TẠO GEMINI API, CƠ CHẾ TỰ ĐỘNG DÒ MODEL VÀ MULTI-FALLBACK TRIỆT ĐỂ
# ==============================================================================
client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"].strip())
    except Exception:
        pass

conn = None
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    pass

def get_available_models():
    """Tự động quét danh mục model khả dụng từ Google API trên tài khoản hiện hành."""
    if not client:
        return []
    
    # Thứ tự các model ưu tiên thử nghiệm
    preferred_order = [
        'gemini-3.8-flash',
        'gemini-2.5-flash',
        'gemini-2.0-flash',
        'gemini-flash-latest',
        'gemini-2.5-pro',
        'gemini-1.5-flash',
        'gemini-1.5-pro'
    ]
    
    discovered = []
    try:
        for m in client.models.list():
            name = m.name.replace('models/', '')
            if hasattr(m, 'supported_generation_methods') and 'generateContent' in m.supported_generation_methods:
                discovered.append(name)
            elif not hasattr(m, 'supported_generation_methods'):
                discovered.append(name)
    except Exception:
        pass
    
    final_models = []
    # 1. Thêm theo độ ưu tiên đã tìm thấy
    for pref in preferred_order:
        for d in discovered:
            if pref in d and d not in final_models:
                final_models.append(d)
                
    # 2. Bổ sung các model khác tìm thấy có flash hoặc pro
    for d in discovered:
        if ('flash' in d or 'pro' in d) and d not in final_models:
            final_models.append(d)
            
    # 3. Dự phòng danh sách cứng nếu không truy vấn được list
    if not final_models:
        final_models = ['gemini-3.8-flash', 'gemini-flash-latest', 'gemini-2.5-flash', 'gemini-2.0-flash']
        
    return final_models

def call_gemini_safe(contents_payload):
    """Cơ chế xoay vòng tự động qua các model để xử lý dứt điểm lỗi 503 và 404."""
    if not client:
        raise Exception("Chưa cấu hình GEMINI_API_KEY trong Streamlit Secrets!")
    
    candidate_models = get_available_models()
    last_err = ""
    
    for m in candidate_models:
        try:
            res = client.models.generate_content(
                model=m,
                contents=contents_payload
            )
            if res and res.text:
                return res.text
        except Exception as e:
            err_str = str(e)
            last_err = err_str
            # Nếu gặp 503 (quá tải), 404 (model cũ đổi tên), 429, tự động bỏ qua sang model tiếp theo
            if any(code in err_str for code in ["503", "404", "429", "NOT_FOUND", "UNAVAILABLE"]):
                time.sleep(1)
                continue
            else:
                time.sleep(1)
                continue
                
    raise Exception(f"Tất cả các cụm máy chủ AI đang phản hồi: {last_err}")

def get_lecture_audio(text_script, audio_id):
    filename = f"lecture_{audio_id}.mp3"
    if not os.path.exists(filename):
        try:
            tts = gTTS(text=text_script, lang='vi', slow=False)
            tts.save(filename)
        except Exception:
            return None
    return filename

# ==============================================================================
# 3. HÌNH ẢNH VECTOR SVG CHUẨN XÁC (KHÔNG ĐÈ CHỮ)
# ==============================================================================
PRESET_SVGS = {
    "DON_DIEU": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="90" y1="20" x2="90" y2="200" stroke="#475569" stroke-width="2"/>
        <line x1="20" y1="65" x2="500" y2="65" stroke="#475569" stroke-width="2"/>
        <line x1="20" y1="110" x2="500" y2="110" stroke="#475569" stroke-width="2"/>
        <text x="50" y="48" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">x</text>
        <text x="50" y="95" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">y'</text>
        <text x="50" y="160" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">y</text>
        <text x="120" y="48" font-family="sans-serif" font-size="14" fill="#64748B">-∞</text>
        <text x="230" y="48" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0F172A">x₁</text>
        <text x="360" y="48" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0F172A">x₂</text>
        <text x="460" y="48" font-family="sans-serif" font-size="14" fill="#64748B">+∞</text>
        <text x="233" y="95" font-family="sans-serif" font-size="16" fill="#334155">0</text>
        <text x="363" y="95" font-family="sans-serif" font-size="16" fill="#334155">0</text>
        <text x="165" y="95" font-family="sans-serif" font-size="20" font-weight="bold" fill="#16A34A">+</text>
        <text x="295" y="95" font-family="sans-serif" font-size="22" font-weight="bold" fill="#DC2626">-</text>
        <text x="420" y="95" font-family="sans-serif" font-size="20" font-weight="bold" fill="#16A34A">+</text>
        <defs><marker id="arr_bbt" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#2563EB"/></marker></defs>
        <line x1="120" y1="185" x2="220" y2="130" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arr_bbt)"/>
        <line x1="245" y1="130" x2="345" y2="185" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arr_bbt)"/>
        <line x1="370" y1="185" x2="470" y2="130" stroke="#2563EB" stroke-width="2.5" marker-end="url(#arr_bbt)"/>
    </svg>""",

    "CUC_TRI": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="40" y1="185" x2="480" y2="185" stroke="#94A3B8" stroke-width="1.5"/>
        <line x1="70" y1="205" x2="70" y2="25" stroke="#94A3B8" stroke-width="1.5"/>
        <text x="485" y="190" font-family="sans-serif" font-size="14" font-weight="bold" fill="#64748B">x</text>
        <text x="65" y="20" font-family="sans-serif" font-size="14" font-weight="bold" fill="#64748B">y</text>
        <path d="M 85 175 C 115 70, 130 50, 150 50 C 185 50, 290 150, 330 150 C 365 150, 395 70, 440 30" fill="none" stroke="#2563EB" stroke-width="3"/>
        <circle cx="150" cy="50" r="5.5" fill="#15803D"/>
        <line x1="150" y1="50" x2="150" y2="185" stroke="#86EFAC" stroke-dasharray="4"/>
        <text x="100" y="32" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803D">Cực Đại (y' = 0)</text>
        <circle cx="330" cy="150" r="5.5" fill="#DC2626"/>
        <line x1="330" y1="150" x2="330" y2="185" stroke="#FCA5A5" stroke-dasharray="4"/>
        <text x="310" y="172" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DC2626">Cực Tiểu (y' = 0)</text>
    </svg>""",

    "TIEM_CAN": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="30" y1="135" x2="490" y2="135" stroke="#94A3B8" stroke-width="1.5"/>
        <line x1="160" y1="200" x2="160" y2="15" stroke="#94A3B8" stroke-width="1.5"/>
        <line x1="240" y1="15" x2="240" y2="205" stroke="#DC2626" stroke-width="2" stroke-dasharray="5"/>
        <text x="246" y="35" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DC2626">TCĐ: x = x₀</text>
        <line x1="20" y1="70" x2="500" y2="70" stroke="#2563EB" stroke-width="2" stroke-dasharray="5"/>
        <text x="390" y="62" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563EB">TCN: y = y₀</text>
        <path d="M 50 63 Q 200 60 230 18" fill="none" stroke="#0F172A" stroke-width="2.5"/>
        <path d="M 252 200 Q 275 78 470 76" fill="none" stroke="#0F172A" stroke-width="2.5"/>
    </svg>""",

    "GTLN_GTNN": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="30" y1="190" x2="480" y2="190" stroke="#94A3B8" stroke-width="1.5"/>
        <line x1="120" y1="190" x2="120" y2="20" stroke="#CBD5E1" stroke-dasharray="4"/>
        <line x1="410" y1="190" x2="410" y2="20" stroke="#CBD5E1" stroke-dasharray="4"/>
        <text x="115" y="208" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1E293B">a</text>
        <text x="405" y="208" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1E293B">b</text>
        <path d="M 120 155 Q 210 35 270 70 T 410 135" fill="none" stroke="#2563EB" stroke-width="3"/>
        <circle cx="210" cy="48" r="5" fill="#15803D"/>
        <text x="220" y="42" font-family="sans-serif" font-size="13" font-weight="bold" fill="#15803D">max f(x) trên [a; b]</text>
        <circle cx="120" cy="155" r="5" fill="#DC2626"/>
        <text x="130" y="165" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DC2626">min f(x)</text>
    </svg>""",

    "TAP_HOP": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <circle cx="215" cy="110" r="75" fill="#93C5FD" fill-opacity="0.45" stroke="#2563EB" stroke-width="2"/>
        <circle cx="305" cy="110" r="75" fill="#FCA5A5" fill-opacity="0.45" stroke="#DC2626" stroke-width="2"/>
        <text x="160" y="115" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E40AF">Tập A</text>
        <text x="335" y="115" font-family="sans-serif" font-size="16" font-weight="bold" fill="#991B1B">Tập B</text>
        <text x="240" y="115" font-family="sans-serif" font-size="15" font-weight="bold" fill="#047857">A ∩ B</text>
    </svg>""",

    "VECTOR": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <defs><marker id="arr_vec" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#2563EB"/></marker></defs>
        <line x1="90" y1="160" x2="410" y2="55" stroke="#2563EB" stroke-width="3.5" marker-end="url(#arr_vec)"/>
        <circle cx="90" cy="160" r="5" fill="#DC2626"/>
        <text x="70" y="180" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">A (Gốc)</text>
        <text x="420" y="55" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">B (Ngọn)</text>
        <text x="230" y="95" font-family="sans-serif" font-size="17" font-weight="bold" fill="#2563EB">Vectơ u = AB</text>
    </svg>""",

    "LUONG_GIAC": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="130" y1="110" x2="390" y2="110" stroke="#475569" stroke-width="1.8"/>
        <line x1="260" y1="205" x2="260" y2="15" stroke="#475569" stroke-width="1.8"/>
        <circle cx="260" cy="110" r="80" fill="none" stroke="#0284C7" stroke-width="2"/>
        <text x="398" y="115" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563EB">Trục Cos</text>
        <text x="268" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Trục Sin</text>
        <line x1="260" y1="110" x2="316" y2="54" stroke="#D97706" stroke-width="2.5"/>
        <circle cx="316" cy="54" r="5" fill="#D97706"/>
        <text x="325" y="52" font-family="sans-serif" font-size="13" font-weight="bold" fill="#B45309">M(cosα; sinα)</text>
    </svg>""",

    "HINH_KHONG_GIAN": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <polygon points="160,170 370,170 300,115" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
        <line x1="260" y1="25" x2="260" y2="140" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4"/>
        <line x1="260" y1="25" x2="160" y2="170" stroke="#1E293B" stroke-width="2"/>
        <line x1="260" y1="25" x2="370" y2="170" stroke="#1E293B" stroke-width="2"/>
        <line x1="260" y1="25" x2="300" y2="115" stroke="#1E293B" stroke-width="2" stroke-dasharray="3"/>
        <text x="255" y="18" font-family="sans-serif" font-size="15" font-weight="bold" fill="#DC2626">S</text>
        <text x="145" y="180" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1E293B">A</text>
        <text x="380" y="180" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1E293B">B</text>
        <text x="305" y="110" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1E293B">C</text>
        <text x="268" y="152" font-family="sans-serif" font-size="12" font-weight="bold" fill="#DC2626">H</text>
    </svg>""",

    "OXYZ": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="250" y1="125" x2="250" y2="20" stroke="#0284C7" stroke-width="2.5"/>
        <line x1="250" y1="125" x2="440" y2="125" stroke="#16A34A" stroke-width="2.5"/>
        <line x1="250" y1="125" x2="120" y2="200" stroke="#DC2626" stroke-width="2.5"/>
        <text x="256" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0284C7">Oz (Cao độ)</text>
        <text x="445" y="130" font-family="sans-serif" font-size="14" font-weight="bold" fill="#16A34A">Oy (Tung độ)</text>
        <text x="100" y="205" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Ox (Hoành độ)</text>
        <circle cx="325" cy="75" r="5" fill="#D97706"/>
        <text x="335" y="75" font-family="sans-serif" font-size="14" font-weight="bold" fill="#B45309">M(x; y; z)</text>
    </svg>""",

    "TICH_PHAN": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="40" y1="170" x2="480" y2="170" stroke="#64748B" stroke-width="1.5"/>
        <line x1="80" y1="195" x2="80" y2="25" stroke="#64748B" stroke-width="1.5"/>
        <path d="M 120 170 Q 230 40 360 170 Z" fill="#93C5FD" fill-opacity="0.6" stroke="#2563EB" stroke-width="2.5"/>
        <text x="115" y="190" font-family="sans-serif" font-size="14" font-weight="bold">a</text>
        <text x="355" y="190" font-family="sans-serif" font-size="14" font-weight="bold">b</text>
        <text x="220" y="135" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1E40AF">S = ∫ f(x)dx</text>
    </svg>""",

    "MAT_PHANG": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <polygon points="100,170 380,170 440,75 160,75" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.5"/>
        <circle cx="280" cy="122" r="5" fill="#1E293B"/>
        <text x="290" y="132" font-family="sans-serif" font-size="14" font-weight="bold">M₀(x₀; y₀; z₀)</text>
        <line x1="280" y1="122" x2="280" y2="30" stroke="#DC2626" stroke-width="3"/>
        <polygon points="280,22 274,36 286,36" fill="#DC2626"/>
        <text x="292" y="42" font-family="sans-serif" font-size="15" font-weight="bold" fill="#DC2626">n⃗ = (A; B; C) ⊥ (P)</text>
    </svg>""",

    "MAT_CAU": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <circle cx="260" cy="110" r="85" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
        <ellipse cx="260" cy="110" rx="85" ry="25" fill="none" stroke="#0284C7" stroke-width="2" stroke-dasharray="5"/>
        <circle cx="260" cy="110" r="4.5" fill="#DC2626"/>
        <text x="245" y="100" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">I(a; b; c)</text>
        <line x1="260" y1="110" x2="330" y2="60" stroke="#16A34A" stroke-width="3"/>
        <text x="295" y="80" font-family="sans-serif" font-size="16" font-weight="bold" fill="#15803D">R</text>
    </svg>""",

    "DUONG_THANG_OXYZ": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <line x1="90" y1="170" x2="430" y2="45" stroke="#0284C7" stroke-width="3"/>
        <text x="100" y="155" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0284C7">d</text>
        <circle cx="210" cy="126" r="5" fill="#DC2626"/>
        <text x="220" y="138" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">M₀(x₀; y₀; z₀)</text>
        <line x1="290" y1="96" x2="380" y2="63" stroke="#16A34A" stroke-width="3"/>
        <polygon points="390,60 377,68 381,58" fill="#16A34A"/>
        <text x="300" y="82" font-family="sans-serif" font-size="15" font-weight="bold" fill="#16A34A">u⃗ = (a; b; c)</text>
    </svg>""",

    "XAC_SUAT": """<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <rect width="520" height="220" fill="#FFFFFF" rx="10" stroke="#CBD5E1" stroke-width="2"/>
        <rect x="150" y="85" width="45" height="100" fill="#3B82F6"/>
        <rect x="235" y="45" width="45" height="140" fill="#10B981"/>
        <rect x="320" y="115" width="45" height="70" fill="#F59E0B"/>
        <line x1="90" y1="185" x2="430" y2="185" stroke="#334155" stroke-width="2"/>
        <line x1="90" y1="185" x2="90" y2="25" stroke="#334155" stroke-width="2"/>
        <text x="180" y="35" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">Xác suất & Thống kê</text>
    </svg>"""
}

def render_dynamic_svg(svg_data):
    svg_code = ""
    if isinstance(svg_data, str) and svg_data.strip().startswith("<svg"):
        svg_code = svg_data.strip()
    else:
        svg_code = PRESET_SVGS.get(svg_data, PRESET_SVGS["DON_DIEU"])

    html_payload = f"""
    <div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%; background: #FFFFFF; border-radius: 10px;">
        {svg_code}
    </div>
    """
    components.html(html_payload, height=230)

# ==============================================================================
# 4. TỰ ĐỘNG NẠP HỌC LIỆU TỪ CÁC MODULE CHUYÊN BIỆT
# ==============================================================================
CURRICULUM_DATA = {"Khối 10": {}, "Khối 11": {}, "Khối 12": {}}

try:
    from data_grade12 import GRADE_12_DATA
    CURRICULUM_DATA["Khối 12"] = GRADE_12_DATA
except Exception:
    pass

try:
    from data_grade11 import GRADE_11_DATA
    CURRICULUM_DATA["Khối 11"] = GRADE_11_DATA
except Exception:
    pass

try:
    from data_grade10 import GRADE_10_DATA
    CURRICULUM_DATA["Khối 10"] = GRADE_10_DATA
except Exception:
    pass

# ==============================================================================
# 5. QUẢN LÝ TÀI KHOẢN VÀ ĐỒNG BỘ GOOGLE SHEETS
# ==============================================================================
if "auth_user" not in st.session_state:
    st.session_state["auth_user"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None
if "students_db" not in st.session_state:
    st.session_state["students_db"] = [
        {"student_id": "HS12_01", "password": "123", "full_name": "Nguyễn Nam", "grade": 12, "flowers": 30},
        {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "flowers": 30},
        {"student_id": "HS10_01", "password": "123", "full_name": "Lê Ngọc", "grade": 10, "flowers": 35}
    ]

if "dynamic_similar_exercises" not in st.session_state:
    st.session_state["dynamic_similar_exercises"] = {}

if "advanced_exercise_data" not in st.session_state:
    st.session_state["advanced_exercise_data"] = {}

if "generated_exam" not in st.session_state:
    st.session_state["generated_exam"] = None
if "current_exam_idx" not in st.session_state:
    st.session_state["current_exam_idx"] = 0
if "user_exam_answers" not in st.session_state:
    st.session_state["user_exam_answers"] = {}
if "exam_submitted_result" not in st.session_state:
    st.session_state["exam_submitted_result"] = None

def sync_flower_to_sheets(student_id, student_name, earned, total_flowers, reason):
    if conn:
        try:
            log_data = pd.DataFrame([{
                "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Mã HS": student_id,
                "Họ và Tên": student_name,
                "Số hoa nhận": earned,
                "Tổng hoa hiện tại": total_flowers,
                "Lí do tích lũy": reason
            }])
            existing_df = conn.read(worksheet="FlowerLogs", ttl=0)
            updated_df = pd.concat([existing_df, log_data], ignore_index=True)
            conn.update(worksheet="FlowerLogs", data=updated_df)
        except Exception:
            pass

def reward_student_flower(student_id, earned, reason):
    for s in st.session_state["students_db"]:
        if s["student_id"] == student_id:
            s["flowers"] = int(s.get("flowers", 30)) + earned
            st.toast(f"🌸 Tuyệt vời! Em nhận được +{earned} Bông hoa vì: {reason}!")
            if st.session_state["auth_user"] and st.session_state["auth_user"]["student_id"] == student_id:
                st.session_state["auth_user"]["flowers"] = s["flowers"]
            sync_flower_to_sheets(student_id, s.get("full_name", ""), earned, s["flowers"], reason)
            break

# ==============================================================================
# HÀM AI SINH ĐỀ TƯƠNG TỰ, ĐỀ NÂNG CAO VÀ ĐỀ THI MA TRẬN TÙY CHỈNH
# ==============================================================================
def generate_similar_exercise_ai(base_problem):
    prompt = (
        f"Dựa vào bài toán gốc sau: '{base_problem}'.\n"
        "Hãy phát sinh 1 bài toán TƯƠNG TỰ CÙNG DẠNG, chỉ thay đổi số liệu hoặc ngữ cảnh đơn giản, "
        "sao cho đáp số cuối cùng là MỘT CON SỐ cụ thể (hoặc số nguyên, hoặc số thập phân đơn giản).\n"
        "Trả về kết quả duy nhất ở định dạng JSON chuẩn (không dùng markdown):\n"
        "{\n"
        '  "problem": "Nội dung đề bài mới",\n'
        '  "answer": "đáp số cuối cùng (chỉ ghi số)",\n'
        '  "hint": "Gợi ý hoặc tóm tắt cách giải ngắn gọn"\n'
        "}"
    )
    try:
        raw_text = call_gemini_safe([prompt])
        t = raw_text.strip()
        if t.startswith("```json"):
            t = t[7:]
        if t.endswith("```"):
            t = t[:-3]
        return json.loads(t.strip())
    except Exception:
        return None

def generate_advanced_exercise_ai(lesson_title):
    prompt = (
        f"Bạn là chuyên gia ra đề thi Toán THPT chương trình GDPT 2018 bộ Kết nối tri thức.\n"
        f"Thuộc bài học: '{lesson_title}'.\n"
        "Hãy sáng tạo 1 bài toán ở mức độ VẬN DỤNG, VẬN DỤNG CAO hoặc MÔ HÌNH HÓA TOÁN HỌC THỰC TẾ "
        "(bài toán tối ưu, lợi nhuận, chuyển động thực tế, xác suất, hình học thực tế...).\n"
        "Yêu cầu: Kết quả làm tròn đến 1 chữ số thập phân hoặc là số nguyên.\n"
        "Trả về duy nhất định dạng JSON chuẩn:\n"
        "{\n"
        '  "problem": "Nội dung đề bài mô hình hóa/vận dụng cao",\n'
        '  "answer": "đáp số số học (chỉ ghi số)",\n'
        '  "guide": "Lời giải chi tiết từng bước chuẩn mực sư phạm"\n'
        "}"
    )
    try:
        raw_text = call_gemini_safe([prompt])
        t = raw_text.strip()
        if t.startswith("```json"):
            t = t[7:]
        if t.endswith("```"):
            t = t[:-3]
        return json.loads(t.strip())
    except Exception:
        return None

def generate_matrix_custom_exam(grade, term, p1_nb, p1_th, p1_vd, p2_nb, p2_th, p2_vd, p3_th, p3_vd, p3_vdc, p3_mod):
    """Sinh đề thi theo chi tiết số lượng câu của từng mức độ nhận thức bám sát GDPT 2018."""
    total_p1 = p1_nb + p1_th + p1_vd
    total_p2 = p2_nb + p2_th + p2_vd
    total_p3 = p3_th + p3_vd + p3_vdc
    
    prompt = f"""
Bạn là chuyên gia Khảo thí môn Toán THPT Chương trình GDPT 2018 bộ Kết nối tri thức.
Hãy tạo 1 đề kiểm tra trắc nghiệm hoàn chỉnh cho: {grade.upper()} - Kỳ thi: {term.upper()}.

YÊU CẦU BẮT BUỘC VỀ SỐ LƯỢNG CÂU HỎI (PHẢI TẠO ĐỦ CHÍNH XÁC):
1. PHẦN I (Trắc nghiệm 4 lựa chọn A, B, C, D): BẮT BUỘC TẠO ĐỦ {total_p1} CÂU.
   - Gồm {p1_nb} câu Nhận biết, {p1_th} câu Thông hiểu, {p1_vd} câu Vận dụng.
   - Mỗi câu có đúng 4 phương án A, B, C, D và chỉ 1 đáp án đúng ("correct": "A" hoặc "B", "C", "D").

2. PHẦN II (Trắc nghiệm Đúng/Sai): BẮT BUỘC TẠO ĐỦ {total_p2} CÂU.
   - Gồm {p2_nb} câu Nhận biết, {p2_th} câu Thông hiểu, {p2_vd} câu Vận dụng.
   - Mỗi câu gồm đề bài và đúng 4 ý a, b, c, d với trường "correct" là true hoặc false.

3. PHẦN III (Trả lời ngắn): BẮT BUỘC TẠO ĐỦ {total_p3} CÂU.
   - Gồm {p3_th} câu Thông hiểu, {p3_vd} câu Vận dụng, {p3_vdc} câu Vận dụng cao.
   - Có đúng {p3_mod} câu là bài toán mô hình hóa thực tế ("is_modeled": true).
   - Đáp án ("correct_num") chỉ ghi một con số thực cụ thể (số nguyên hoặc làm tròn 1 chữ số thập phân).

LƯU Ý: Công thức toán viết dạng LaTeX đơn giản trong dấu $. Nếu phần nào có số câu bằng 0 thì để mảng rỗng [].

TRẢ VỀ DUY NHẤT một chuỗi JSON hợp lệ (không kèm lời giải thích nào khác ngoài chuỗi JSON):
{{
  "exam_title": "ĐỀ THI {grade.upper()} - {term.upper()}",
  "part1": [
    {{"id": "P1_1", "question": "Nội dung câu hỏi...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "correct": "A"}}
  ],
  "part2": [
    {{"id": "P2_1", "question": "Nội dung câu...", "sub_items": [{{"label": "a", "text": "...", "correct": true}}, {{"label": "b", "text": "...", "correct": false}}, {{"label": "c", "text": "...", "correct": true}}, {{"label": "d", "text": "...", "correct": false}}]}}
  ],
  "part3": [
    {{"id": "P3_1", "question": "Nội dung câu...", "correct_num": "4.5", "is_modeled": true}}
  ]
}}
"""
    raw = call_gemini_safe([prompt])
    if not raw:
        raise Exception("Không nhận được phản hồi từ AI.")
        
    t = raw.strip()
    if t.startswith("```json"):
        t = t[7:]
    elif t.startswith("```"):
        t = t[3:]
    if t.endswith("```"):
        t = t[:-3]
    t = t.strip()
    
    try:
        exam_json = json.loads(t)
    except Exception as parse_err:
        raise Exception(f"Lỗi đọc định dạng JSON từ AI: {parse_err}. Nội dung nhận được: {t[:300]}...")

    return exam_json

# ==============================================================================
# BỘ CHUYỂN ĐỔI LATEX SANG UNICODE TOÁN HỌC & XUẤT FILE WORD IN ĐƯỢC
# ==============================================================================
def clean_latex_to_text(text: str) -> str:
    """Chuyển đổi các cú pháp LaTeX thông dụng sang ký tự Unicode toán học để in ngay trên Word."""
    if not text:
        return ""
    s = str(text)

    # 1. Bỏ dấu đóng/mở khối công thức $ hoặc $$
    s = re.sub(r'\$\$?', '', s)

    # 2. Chuyển đổi các ký hiệu đặc biệt
    replacements = [
        (r'\\pm', '±'),
        (r'\\times', '×'),
        (r'\\div', '÷'),
        (r'\\approx', '≈'),
        (r'\\ne', '≠'),
        (r'\\le', '≤'),
        (r'\\ge', '≥'),
        (r'\\in', '∈'),
        (r'\\notin', '∉'),
        (r'\\subset', '⊂'),
        (r'\\cap', '∩'),
        (r'\\cup', '∪'),
        (r'\\emptyset', '∅'),
        (r'\\infty', '∞'),
        (r'\\forall', '∀'),
        (r'\\exists', '∃'),
        (r'\\implies', '⇒'),
        (r'\\iff', '⇔'),
        (r'\\perp', '⊥'),
        (r'\\parallel', '∥'),
        (r'\\alpha', 'α'),
        (r'\\beta', 'β'),
        (r'\\pi', 'π'),
        (r'\\Delta', 'Δ'),
        (r'\\int', '∫'),
        (r'\\mathbb\{R\}', 'ℝ'),
        (r'\\mathbb\{N\}', 'ℕ'),
        (r'\\mathbb\{Z\}', 'ℤ'),
        (r'\\mathbb\{Q\}', 'ℚ'),
    ]
    for pattern, repl in replacements:
        s = re.sub(pattern, repl, s)

    # 3. Chuyển đổi phân số: \frac{a}{b} -> (a)/(b)
    s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', s)

    # 4. Chuyển đổi căn thức: \sqrt{a} -> √(a)
    s = re.sub(r'\\sqrt\{([^{}]+)\}', r'√(\1)', s)
    s = re.sub(r'\\sqrt\s*([a-zA-Z0-9])', r'√\1', s)

    # 5. Chuyển đổi vectơ: \vec{AB} -> vectơ AB
    s = re.sub(r'\\vec\{([^{}]+)\}', r'vectơ \1', s)

    # 6. Chuyển đổi số mũ cơ bản sang Unicode superscript
    superscript_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '+': '⁺', '-': '⁻'}
    def replace_pow(match):
        p = match.group(1)
        return ''.join(superscript_map.get(c, c) for c in p)
    s = re.sub(r'\^\{([0-9+-]+)\}', replace_pow, s)
    s = re.sub(r'\^([0-9])', lambda m: superscript_map.get(m.group(1), m.group(1)), s)

    # 7. Chuyển đổi chỉ số dưới: x_1 -> x₁, x_0 -> x₀
    subscript_map = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'}
    s = re.sub(r'\_\{([0-9]+)\}', lambda m: ''.join(subscript_map.get(c, c) for c in m.group(1)), s)
    s = re.sub(r'\_([0-9])', lambda m: subscript_map.get(m.group(1), m.group(1)), s)

    # 8. Dọn dẹp khoảng trắng thừa và dấu ngoặc nhọn
    s = s.replace('{', '').replace('}', '')
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def export_exam_to_docx(exam_data):
    """Xuất đề thi ra file Word (.docx) chuẩn format in ấn, sạch mã LaTeX."""
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    table_header = doc.add_table(rows=1, cols=2)
    table_header.autofit = False
    
    cell_left = table_header.cell(0, 0)
    p_left = cell_left.paragraphs[0]
    p_left.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_left.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\n").bold = True
    p_left.add_run("TRƯỜNG THPT CHUYÊN / CHUẨN\n").bold = True
    p_left.add_run("ĐỀ THI CHÍNH THỨC").italic = True

    cell_right = table_header.cell(0, 1)
    p_right = cell_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_text = clean_latex_to_text(exam_data.get("exam_title", "ĐỀ KIỂM TRA MÔN TOÁN")).upper()
    run_t = p_right.add_run(f"{title_text}\n")
    run_t.bold = True
    run_t.font.size = Pt(12)
    p_right.add_run("Thời gian làm bài: 90 phút (Không kể thời gian phát đề)\n").italic = True
    p_right.add_run("Mã đề thi: 101").bold = True

    doc.add_paragraph("─" * 58).alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_info = doc.add_paragraph()
    p_info.add_run("Họ và tên thí sinh: ............................................................................   Số báo danh: .....................\n")

    p1 = exam_data.get("part1", [])
    if p1:
        h1 = doc.add_paragraph()
        r1 = h1.add_run("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn.")
        r1.bold = True
        r1.font.size = Pt(11)
        doc.add_paragraph("Thí sinh trả lời từ câu 1 đến câu " + str(len(p1)) + ". Mỗi câu hỏi thí sinh chỉ chọn một phương án.")

        for idx, q in enumerate(p1):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.add_run(f"Câu {idx + 1}: ").bold = True
            p.add_run(clean_latex_to_text(q.get("question", "")))
            
            opts = q.get("options", [])
            for opt in opts:
                p_opt = doc.add_paragraph()
                p_opt.paragraph_format.left_indent = Inches(0.25)
                p_opt.paragraph_format.space_before = Pt(0)
                p_opt.paragraph_format.space_after = Pt(2)
                p_opt.add_run(clean_latex_to_text(opt))

    p2 = exam_data.get("part2", [])
    if p2:
        h2 = doc.add_paragraph()
        h2.paragraph_format.space_before = Pt(10)
        r2 = h2.add_run("PHẦN II. Câu trắc nghiệm đúng sai.")
        r2.bold = True
        r2.font.size = Pt(11)
        doc.add_paragraph("Thí sinh trả lời từ câu 1 đến câu " + str(len(p2)) + ". Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.")

        for idx, q in enumerate(p2):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.add_run(f"Câu {idx + 1}: ").bold = True
            p.add_run(clean_latex_to_text(q.get("question", "")))

            for sub in q.get("sub_items", []):
                p_sub = doc.add_paragraph()
                p_sub.paragraph_format.left_indent = Inches(0.25)
                p_sub.paragraph_format.space_before = Pt(0)
                p_sub.paragraph_format.space_after = Pt(2)
                p_sub.add_run(f"{sub.get('label')}) ").bold = True
                p_sub.add_run(clean_latex_to_text(sub.get("text", "")))

    p3 = exam_data.get("part3", [])
    if p3:
        h3 = doc.add_paragraph()
        h3.paragraph_format.space_before = Pt(10)
        r3 = h3.add_run("PHẦN III. Câu trắc nghiệm trả lời ngắn.")
        r3.bold = True
        r3.font.size = Pt(11)
        doc.add_paragraph("Thí sinh trả lời từ câu 1 đến câu " + str(len(p3)) + ". Viết kết quả dưới dạng số (làm tròn đến 1 chữ số thập phân nếu cần).")

        for idx, q in enumerate(p3):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.add_run(f"Câu {idx + 1}: ").bold = True
            p.add_run(clean_latex_to_text(q.get("question", "")))
            
            p_ans = doc.add_paragraph()
            p_ans.paragraph_format.left_indent = Inches(0.25)
            p_ans.add_run("Đáp số: .....................................................").italic = True

    p_end = doc.add_paragraph()
    p_end.paragraph_format.space_before = Pt(14)
    p_end.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_end.add_run("────────── HẾT ──────────\n").bold = True
    p_end.add_run("Cán bộ coi thi không giải thích gì thêm.").italic = True

    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

# ==============================================================================
# 6. MÀN HÌNH ĐĂNG NHẬP
# ==============================================================================
if st.session_state["auth_user"] is None:
    st.markdown(f"<h2 style='text-align: center; color: #2563EB;'>📐 HỆ SINH THÁI TỰ HỌC TOÁN THPT 'GSTOÁN'</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: {subtext_color};'>Chuẩn hóa 100% Chủ điểm SGK & Vở tự học Kết nối tri thức (Khối 10, 11, 12)</p>", unsafe_allow_html=True)
    
    col_l1, col_box, col_l2 = st.columns([1, 1.2, 1])
    with col_box:
        with st.container(border=True):
            st.markdown("### 🔐 Cổng Đăng Nhập")
            login_role = st.radio("Vai trò:", ["👨‍🎓 Học sinh", "👩‍‍🏫 Giáo viên (Admin)"], horizontal=True)
            user_input = st.text_input("Tài khoản / Mã học sinh:", value="HS11_01")
            pass_input = st.text_input("Mật khẩu:", type="password", value="123")

            if st.button("Đăng Nhập Ngay", use_container_width=True):
                if login_role == "👩‍🏫 Giáo viên (Admin)":
                    if user_input.strip().lower() == "admin" and pass_input in ["gstoan2026", "123"]:
                        st.session_state["auth_user"] = {"full_name": "Thầy/Cô Bộ Môn Toán", "role": "teacher"}
                        st.session_state["role"] = "teacher"
                        st.rerun()
                    else:
                        st.error("Sai tài khoản Giáo viên!")
                else:
                    found = next((s for s in st.session_state["students_db"] if s["student_id"].upper() == user_input.strip().upper()), None)
                    if found and str(found.get("password", "123")) == pass_input.strip():
                        st.session_state["auth_user"] = found
                        st.session_state["role"] = "student"
                        st.rerun()
                    else:
                        st.error("Sai mã học sinh hoặc mật khẩu!")
            st.caption("💡 Mẫu: `HS10_01`, `HS11_01`, `HS12_01` (Pass: `123`). Admin: `admin` / `123`.")
    st.stop()

# ==============================================================================
# 7. THANH ĐIỀU HƯỚNG BÊN (SIDEBAR) & CHUYỂN GIAO DIỆN SÁNG / TỐI
# ==============================================================================
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state['auth_user']['full_name']}")
    
    theme_choice = st.radio("🎨 Chế độ hiển thị:", ["Sáng ☀️", "Tối 🌙"], index=(1 if is_dark else 0))
    selected_mode = "Tối" if "Tối" in theme_choice else "Sáng"
    if selected_mode != st.session_state["theme_mode"]:
        st.session_state["theme_mode"] = selected_mode
        st.rerun()

    if st.session_state["role"] == "student":
        st.caption(f"Mã định danh: **{st.session_state['auth_user']['student_id']}**")
        flowers = st.session_state['auth_user'].get('flowers', 30)
        with st.container(border=True):
            st.markdown("<h5 style='text-align: center; color: #DB2777; margin:0;'>🌸 Vườn hoa Tri thức</h5>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #BE185D; margin:4px 0;'>{flowers} 🌸</h2>", unsafe_allow_html=True)
            st.caption("Giải đúng BT +2 hoa. Nghe giảng +1 hoa. Khảo thí +3 hoa!")
            
    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.session_state["role"] = None
        st.rerun()

if st.session_state["role"] == "teacher":
    st.title("👩‍🏫 Bảng Điều Khiển Giáo Viên (Dashboard Quản Lý)")
    st.info("Chào mừng Thầy/Cô! Dưới đây là bảng theo dõi tiến độ tự học của học sinh.")
    
    df_students = pd.DataFrame(st.session_state["students_db"])
    st.dataframe(df_students[["student_id", "full_name", "grade", "flowers"]], use_container_width=True)
    
    if conn:
        try:
            logs = conn.read(worksheet="FlowerLogs", ttl=0)
            st.markdown("#### 📜 Nhật Ký Hoạt Động Tự Học Trực Tuyến")
            st.dataframe(logs, use_container_width=True)
        except Exception:
            st.caption("Chưa có kết nối bảng ghi nhật ký Google Sheets.")
    st.stop()

# ==============================================================================
# 8. ĐỒNG BỘ 100% CÙNG FORM "CHỦ ĐIỂM 1, CHỦ ĐIỂM 2,..." CHO CẢ 3 KHỐI
# ==============================================================================
student_info = st.session_state["auth_user"]

search_kw = st.text_input("🔍 Tìm kiếm nhanh bài học, chủ điểm (Ví dụ: 'Simpson', 'Đạo hàm', 'Tọa độ'):", "")

if "selected_grade" not in st.session_state:
    st.session_state["selected_grade"] = "Khối 12" if student_info.get("grade") == 12 else ("Khối 10" if student_info.get("grade") == 10 else "Khối 11")

def on_grade_change():
    st.session_state.pop("selected_lesson", None)
    st.session_state.pop("selected_topic_display", None)

c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])

with c_gr:
    grade_list = ["Khối 10", "Khối 11", "Khối 12"]
    curr_gr_idx = grade_list.index(st.session_state["selected_grade"]) if st.session_state["selected_grade"] in grade_list else 2
    sel_grade = st.selectbox("📚 Khối Lớp:", grade_list, index=curr_gr_idx, key="selected_grade", on_change=on_grade_change)

grade_dict = CURRICULUM_DATA.get(sel_grade, {})
if not grade_dict:
    st.warning(f"Dữ liệu của {sel_grade} đang được đồng bộ hóa. Vui lòng kiểm tra lại file data tương ứng!")
    st.stop()

all_lessons = list(grade_dict.keys())
if search_kw.strip():
    kw_lower = search_kw.strip().lower()
    filtered_lessons = [
        l_name for l_name, l_data in grade_dict.items()
        if kw_lower in l_name.lower() or any(kw_lower in t.lower() for t in l_data.get("topics", {}).keys())
    ]
    lesson_list = filtered_lessons if filtered_lessons else all_lessons
else:
    lesson_list = all_lessons

def on_lesson_change():
    st.session_state.pop("selected_topic_display", None)

with c_les:
    if "selected_lesson" not in st.session_state or st.session_state["selected_lesson"] not in lesson_list:
        st.session_state["selected_lesson"] = lesson_list[0]
    sel_lesson = st.selectbox(f"📖 Bài học ({len(lesson_list)} bài):", lesson_list, key="selected_lesson", on_change=on_lesson_change)

cur_lesson_obj = grade_dict[sel_lesson]
raw_topic_list = list(cur_lesson_obj.get("topics", {}).keys())

if not raw_topic_list:
    st.warning("Bài học này đang được chuẩn hóa chủ điểm.")
    st.stop()

# ĐỒNG BỘ 100% CÙNG MỘT FORM "Chủ điểm 1: ...", "Chủ điểm 2: ..." CHO CẢ 3 KHỐI
formatted_topic_map = {}
for idx, t_raw in enumerate(raw_topic_list):
    clean_t = t_raw.strip()
    if clean_t.startswith("Chủ điểm"):
        display_name = clean_t
    else:
        parts = clean_t.split(".", 1)
        if len(parts) > 1 and parts[0].strip().isdigit():
            clean_title = parts[1].strip()
        else:
            clean_title = clean_t
        display_name = f"Chủ điểm {idx+1}: {clean_title}"
        
    formatted_topic_map[display_name] = t_raw

display_topic_list = list(formatted_topic_map.keys())

with c_top:
    if "selected_topic_display" not in st.session_state or st.session_state["selected_topic_display"] not in display_topic_list:
        st.session_state["selected_topic_display"] = display_topic_list[0]
    sel_topic_display = st.selectbox("🎯 Danh sách Chủ điểm (Vở tự học):", display_topic_list, key="selected_topic_display")

real_topic_key = formatted_topic_map[sel_topic_display]
cur_topic_data = cur_lesson_obj["topics"][real_topic_key]

# 5 TABS CHÍNH
tab1, tab_ex, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Hình Ảnh & Audio)",
    "💡 Ví Dụ Minh Họa (Toàn Bộ Chủ Điểm)",
    "📝 Học Sinh Tự Giải (Luyện Tập & Đề Tương Tự)",
    "📸 Trợ Lý AI: Soi Vở & Lời Khuyên",
    "🎯 Phòng Khảo Thí Khách Quan"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {cur_lesson_obj.get('chapter', 'Kiến thức trọng tâm')}")
    st.markdown(f"#### {sel_lesson} — *{sel_topic_display}*")

    col_img, col_n = st.columns([1.2, 1.1])
    
    with col_img:
        with st.container(border=True):
            st.markdown("🖼 **Hình ảnh minh họa kiến thức (Vẽ chính xác bằng vector, không đè chữ):**")
            render_dynamic_svg(cur_topic_data.get("svg", "DON_DIEU"))
            
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Chủ Điểm (Trích Vở tự học):</b><br>
                <small>Nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5((sel_lesson + real_topic_key).encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_topic_data.get("audio", "Bài giảng vi mô."), audio_hash)
            if lecture_audio_file:
                st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã nghe xong bài giảng vi mô (+1 hoa)", key=f"btn_audio_{real_topic_key}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ nghe bài giảng vi mô")
                
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes)**")
            st.markdown(f"#### 1. Khái niệm & Định lý cốt lõi\n{cur_topic_data.get('theory', '')}")
            st.markdown("#### 2. Công thức Toán học trọng tâm")
            formula_text = cur_topic_data.get('formula', '')
            if formula_text.startswith("$$"):
                st.markdown(formula_text)
            else:
                st.markdown(f"$${formula_text}$$")
            st.markdown(f"#### 3. Cảnh báo bẫy đề thi\n- ⚠️ **Lưu ý:** {cur_topic_data.get('trap', '')}")

# ------------------------------------------------------------------------------
# TAB 2: VÍ DỤ MINH HỌA (LOAD TOÀN BỘ CHỦ ĐIỂM CỦA BÀI ĐANG CHỌN)
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Toàn Bộ Ví Dụ Minh Họa Chuẩn Mực — {sel_lesson}")
    st.caption("Hệ thống tự động tải toàn bộ ví dụ minh họa của TỪNG CHỦ ĐIỂM trong bài học. Bấm vào từng đề bài để xem lời giải chi tiết chuẩn mực sư phạm.")

    all_topics_in_lesson = cur_lesson_obj.get("topics", {})
    for t_idx, (t_name, t_content) in enumerate(all_topics_in_lesson.items()):
        clean_name = t_name.strip()
        if clean_name.startswith("Chủ điểm"):
            card_title = clean_name
        else:
            parts = clean_name.split(".", 1)
            clean_title = parts[1].strip() if len(parts) > 1 and parts[0].strip().isdigit() else clean_name
            card_title = f"Chủ điểm {t_idx+1}: {clean_title}"

        with st.container(border=True):
            st.markdown(f"<div class='topic-card'><b>🎯 {card_title}</b></div>", unsafe_allow_html=True)
            topic_examples = t_content.get("examples", [])
            if not topic_examples:
                st.info("Chủ điểm này đang được đồng bộ hóa ví dụ.")
            else:
                for idx, ex_item in enumerate(topic_examples):
                    is_default_open = (t_name == real_topic_key and idx == 0)
                    with st.expander(f"📌 {ex_item['title']}", expanded=is_default_open):
                        st.markdown(f"**Đề bài yêu cầu:**\n\n{ex_item['problem']}")
                        st.markdown("---")
                        st.markdown("**✍️ Lời giải chi tiết chuẩn mực sư phạm:**")
                        st.markdown(ex_item["solution"])

# ------------------------------------------------------------------------------
# TAB 3: HỌC SINH TỰ GIẢI (TỰ SINH ĐỀ TƯƠNG TỰ & ĐỀ NÂNG CAO MÔ HÌNH HÓA)
# ------------------------------------------------------------------------------
with tab2:
    st.subheader(f"📝 Không Gian Tự Luyện Toán Học — {sel_lesson}")
    st.caption("Hệ thống phát sinh bài tập rèn luyện tương tự cho TẤT CẢ ví dụ minh họa. Em hãy tự giải ra nháp, nhập đáp số và nộp bài để nhận phản hồi tức thì.")

    col_adv_btn, col_adv_space = st.columns([1.5, 2.5])
    with col_adv_btn:
        if st.button("🚀 Thử Sức: Tạo Đề Nâng Cao (Vận Dụng / Mô Hình Hóa)", use_container_width=True):
            with st.spinner("AI đang sáng tạo bài toán mô hình hóa thực tế cho bài học này..."):
                adv_res = generate_advanced_exercise_ai(sel_lesson)
                if adv_res:
                    st.session_state["advanced_exercise_data"][sel_lesson] = adv_res
                    st.rerun()
                else:
                    st.error("Không thể tạo đề nâng cao lúc này. Vui lòng thử lại sau.")

    if sel_lesson in st.session_state["advanced_exercise_data"]:
        adv_obj = st.session_state["advanced_exercise_data"][sel_lesson]
        with st.container(border=True):
            st.markdown("#### 🔥 Bài Toán Thực Tế / Vận Dụng Cao (Mô Hình Hóa)")
            st.markdown(f"**Đề bài:**\n\n{adv_obj.get('problem')}")
            
            c_adv_in, c_adv_sub = st.columns([2, 1])
            with c_adv_in:
                user_adv_ans = st.text_input("Nhập đáp số bài nâng cao của em:", key=f"ans_adv_{sel_lesson}")
            with c_adv_sub:
                st.write("")
                st.write("")
                btn_chk_adv = st.button("Nộp Bài Nâng Cao", key=f"btn_adv_{sel_lesson}", use_container_width=True)
                
            if btn_chk_adv:
                target_adv = str(adv_obj.get("answer", "")).strip().lower()
                u_ans = user_adv_ans.strip().lower()
                is_adv_correct = False
                if u_ans == target_adv:
                    is_adv_correct = True
                else:
                    try:
                        if abs(float(u_ans) - float(target_adv)) < 0.1:
                            is_adv_correct = True
                    except Exception:
                        pass

                if is_adv_correct:
                    st.balloons()
                    st.success("🎉 XUẤT SẮC! Em đã giải chính xác bài toán vận dụng cao và nhận được +3 Bông hoa Tri thức!")
                    reward_student_flower(student_info["student_id"], 3, "xuất sắc giải đúng bài toán nâng cao mô hình hóa")
                else:
                    st.error("❌ Kết quả chưa chính xác! Em hãy xem hướng dẫn chi tiết bên dưới.")
                
                with st.expander("📖 Xem Hướng Dẫn Chi Tiết Bài Nâng Cao"):
                    st.markdown(adv_obj.get("guide", "Đang cập nhật hướng dẫn."))

        st.markdown("---")

    all_topics_in_lesson = cur_lesson_obj.get("topics", {})
    exercise_counter = 1

    for t_idx, (t_name, t_content) in enumerate(all_topics_in_lesson.items()):
        clean_name = t_name.strip()
        if clean_name.startswith("Chủ điểm"):
            topic_label = clean_name
        else:
            parts = clean_name.split(".", 1)
            clean_title = parts[1].strip() if len(parts) > 1 and parts[0].strip().isdigit() else clean_name
            topic_label = f"Chủ điểm {t_idx+1}: {clean_title}"

        st.markdown(f"<div class='topic-card'><b>🎯 {topic_label} — Bài Tập Tự Luyện Tương Tự</b></div>", unsafe_allow_html=True)
        topic_examples = t_content.get("examples", [])
        
        if not topic_examples:
            def_ex = t_content.get("exercise", {})
            if def_ex:
                with st.container(border=True):
                    st.markdown(f"**Bài tập {exercise_counter}:** {def_ex.get('content')}")
                    ans_in = st.text_input("Nhập đáp số:", key=f"def_ex_{def_ex.get('id')}")
                    if st.button("Nộp Bài", key=f"btn_def_{def_ex.get('id')}"):
                        target = str(def_ex.get("target", "")).strip().lower()
                        if ans_in.strip().lower() == target:
                            st.balloons()
                            st.success("🎉 CHÍNH XÁC! +2 Bông hoa Tri thức!")
                            reward_student_flower(student_info["student_id"], 2, "giải đúng bài tập tự luyện")
                        else:
                            st.error("❌ Chưa đúng, em hãy thử lại nhé!")
                exercise_counter += 1
        else:
            for ex_idx, ex_item in enumerate(topic_examples):
                ex_key_id = f"{sel_lesson}_{t_name}_{ex_idx}"
                active_exercise = st.session_state["dynamic_similar_exercises"].get(ex_key_id)
                
                with st.container(border=True):
                    col_ex_title, col_ex_btn_regen = st.columns([3, 1])
                    with col_ex_title:
                        st.markdown(f"#### 📝 Bài tập tự luyện {exercise_counter} *(Tương tự: {ex_item['title']})*")
                    with col_ex_btn_regen:
                        if st.button("🔄 Tạo đề mới", key=f"regen_{ex_key_id}", help="Bấm để AI sinh một đề bài mới cùng dạng bài này"):
                            with st.spinner("Đang tạo đề tương tự mới..."):
                                new_sim = generate_similar_exercise_ai(ex_item["problem"])
                                if new_sim:
                                    st.session_state["dynamic_similar_exercises"][ex_key_id] = new_sim
                                    st.rerun()

                    if active_exercise:
                        st.info("✨ *Đề bài tương tự do AI phát sinh:*")
                        st.markdown(f"**Đề bài:**\n\n{active_exercise.get('problem')}")
                        target_ans_val = str(active_exercise.get("answer", "")).strip()
                        hint_val = active_exercise.get("hint", "")
                    else:
                        st.markdown(f"**Đề bài:**\n\n{ex_item['problem']}")
                        target_ans_val = ""
                        hint_val = ex_item["solution"]

                    col_ans_in, col_btn_sub = st.columns([2, 1])
                    with col_ans_in:
                        u_ans_input = st.text_input(f"Nhập kết quả Bài tập {exercise_counter}:", key=f"ans_in_{ex_key_id}")
                    with col_btn_sub:
                        st.write("")
                        st.write("")
                        btn_submit_ex = st.button("🚀 Nộp Bài", key=f"sub_btn_{ex_key_id}", use_container_width=True)

                    if btn_submit_ex:
                        if not u_ans_input.strip():
                            st.warning("Vui lòng điền đáp số trước khi nộp bài.")
                        else:
                            is_match = False
                            user_norm = u_ans_input.strip().lower()
                            
                            if target_ans_val:
                                if user_norm == target_ans_val.lower():
                                    is_match = True
                                else:
                                    try:
                                        if abs(float(user_norm) - float(target_ans_val)) < 0.05:
                                            is_match = True
                                    except Exception:
                                        pass
                            else:
                                if len(user_norm) >= 1 and user_norm in hint_val.lower():
                                    is_match = True

                            if is_match:
                                st.balloons()
                                st.success("🎉 HOÀN TOÀN CHÍNH XÁC! Em đã tự lực giải đúng bài tập và nhận +2 Bông hoa Tri thức!")
                                reward_student_flower(student_info["student_id"], 2, f"tự giải đúng bài tập tự luyện số {exercise_counter}")
                            else:
                                st.error("❌ Kết quả chưa chính xác! Em hãy xem lại phương pháp hoặc mở gợi ý giải.")

                    with st.expander("💡 Bấm để xem Gợi ý / Lời giải mẫu"):
                        st.markdown(hint_val)

                exercise_counter += 1

# ------------------------------------------------------------------------------
# TAB 4: TRỢ LÝ AI SOI VỞ VIẾT TAY
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("💬 Gia Sư AI: Soi Bài Viết Tay & Lời Khuyên Sư Phạm")
    st.caption("Chụp ảnh, tải file hoặc dán ảnh bài giải viết tay để Thầy/Cô AI chỉ rõ từng bước sai sót mà không giải hộ.")

    inp_mode = st.radio(
        "Chọn phương thức nạp bài làm:",
        [
            "📸 Chụp trực tiếp qua Camera", 
            "📁 Tải hoặc Dán ảnh bài làm (Upload / Paste Clipboard)", 
            "✍️ Chỉ gửi câu hỏi chữ"
        ],
        horizontal=True
    )

    image_to_process = None

    if inp_mode == "📸 Chụp trực tiếp qua Camera":
        cam_image = st.camera_input("Chụp ảnh trang vở nháp của em:")
        if cam_image:
            image_to_process = Image.open(cam_image)

    elif inp_mode == "📁 Tải hoặc Dán ảnh bài làm (Upload / Paste Clipboard)":
        st.markdown("""
        <div style="background-color: #F1F5F9; border: 2px dashed #94A3B8; border-radius: 10px; padding: 12px; text-align: center; margin-bottom: 8px;">
            <p style="margin: 0; color: #334155; font-size: 14px;">
                📎 <b>Hỗ trợ đa năng:</b> Em có thể bấm chọn file từ máy, kéo thả ảnh vào, hoặc bấm phím <code>Ctrl + V</code> (ảnh chụp màn hình) vào khung bên dưới.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_or_pasted_file = st.file_uploader(
            "Tải file hoặc dán ảnh bài làm vào đây (PNG, JPG, JPEG, WEBP):", 
            type=["png", "jpg", "jpeg", "webp"],
            help="Hỗ trợ ảnh chụp điện thoại hoặc dán trực tiếp từ bộ nhớ tạm clipboard"
        )
        if uploaded_or_pasted_file:
            image_to_process = Image.open(uploaded_or_pasted_file)
            st.image(image_to_process, caption="Ảnh bài làm đã tiếp nhận", use_container_width=True)

    user_q = st.text_area(
        "Ghi chú thêm câu hỏi hoặc thắc mắc của em:", 
        placeholder="Ví dụ: Thầy/cô xem giúp em bị sai từ dòng nào trong bước đặt ẩn phụ/tính đạo hàm này ạ..."
    )

    if st.button("🚀 Gửi Bài Nhờ Gia Sư AI Soi Bài", use_container_width=True):
        if client:
            try:
                with st.spinner("Thầy/Cô AI đang đọc bài làm và phân tích từng bước giải của em..."):
                    system_vision_prompt = (
                        f"Bạn là Thầy/Cô giáo dạy Toán cấp THPT với phương pháp sư phạm mẫu mực. "
                        f"Học sinh đang tự học bài: '{sel_lesson}', chủ điểm: '{sel_topic_display}'.\n\n"
                        "NHIỆM VỤ SƯ PHẠM KHI SOI BÀI VIẾT TAY:\n"
                        "1. Đọc và phiên dịch cẩn thận các dòng viết tay hoặc phương trình toán học trong ảnh.\n"
                        "2. Kiểm tra tính đúng đắn theo từng bước logic, biến đổi công thức và tính toán số học.\n"
                        "3. NẾU CÓ LỖI SAI: Hãy CHỈ RÕ CHÍNH XÁC học sinh bị sai từ dòng thứ mấy, phân tích nguyên nhân sai "
                        "(sai dấu, áp dụng sai công thức, quên điều kiện xác định hay nhầm lẫn số học).\n"
                        "4. GỢI Ý HƯỚNG GIẢI TIẾP THEO để học sinh tự làm lại. TUYỆT ĐỐI KHÔNG giải thay toàn bộ bài hay viết sẵn đáp số cuối cùng.\n"
                        "5. NẾU BÀI LÀM ĐÃ ĐÚNG: Hãy khen ngợi tinh thần tự học của học sinh và khuyến khích em thử sức với các bài tập nâng cao.\n"
                        "6. Luôn trình bày các biểu thức toán học bằng định dạng LaTeX chuẩn mực ($...$ hoặc $$...$$)."
                    )

                    contents = [system_vision_prompt]
                    if image_to_process:
                        contents.append(image_to_process)
                    if user_q.strip():
                        contents.append(f"Ghi chú thắc mắc của học sinh: {user_q}")
                    elif not image_to_process:
                        contents.append("Học sinh chưa cung cấp ảnh bài làm hoặc câu hỏi, hãy nhắc nhở em gửi ảnh hoặc nội dung cần giải đáp.")

                    ai_reply = call_gemini_safe(contents)
                    st.success("### ✍️ Lời Khuyên & Nhận Xét Từ Thầy/Cô AI:")
                    st.markdown(ai_reply)
                    reward_student_flower(student_info["student_id"], 1, "tích cực chụp bài hỏi Thầy/Cô AI")
            except Exception as e:
                st.error(f"Chi tiết lỗi kết nối AI: {e}")
        else:
            st.info("Trợ lý AI đang sẵn sàng hỗ trợ nội dung bài học này (yêu cầu cấu hình Gemini API Key hợp lệ trong mục Secrets).")

# ------------------------------------------------------------------------------
# TAB 5: PHÒNG KHẢO THÍ (TÙY CHỌN CHI TIẾT TỪNG MỨC ĐỘ, CHO PHÉP VỀ 0)
# ------------------------------------------------------------------------------
with tab4:
    st.subheader("🎯 Phòng Khảo Thí & Luyện Đề Chuẩn Hóa GDPT 2018")
    st.caption("Cấu trúc đề thi mới nhất bám sát khung năng lực của Bộ Giáo dục và Đào tạo. Tùy chọn số câu cho từng mức độ nhận thức (cho phép về 0), tương tác làm bài và xuất file Word.")

    with st.expander("⚙ BẢNG TÙY CHỌN MA TRẬN ĐỀ THI CHI TIẾT", expanded=(st.session_state["generated_exam"] is None)):
        c1, c2 = st.columns(2)
        with c1:
            exam_grade = st.selectbox("1. Khối lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=(2 if sel_grade=="Khối 12" else (0 if sel_grade=="Khối 10" else 1)))
        with c2:
            exam_term = st.selectbox("2. Kỳ kiểm tra:", ["Giữa kỳ 1", "Cuối kỳ 1", "Giữa kỳ 2", "Cuối kỳ 2"])
            
        st.markdown("---")
        
        # PHẦN I
        st.markdown("##### 3. PHẦN I: Trắc nghiệm 1 lựa chọn (A, B, C, D) — Mỗi câu 0.25 điểm")
        col_p1_nb, col_p1_th, col_p1_vd = st.columns(3)
        with col_p1_nb:
            p1_nb = st.number_input("Số câu Nhận biết (NB):", min_value=0, max_value=20, value=6, key="p1_nb")
        with col_p1_th:
            p1_th = st.number_input("Số câu Thông hiểu (TH):", min_value=0, max_value=20, value=5, key="p1_th")
        with col_p1_vd:
            p1_vd = st.number_input("Số câu Vận dụng (VD):", min_value=0, max_value=20, value=1, key="p1_vd")
        
        total_p1_calc = p1_nb + p1_th + p1_vd
        score_p1_calc = round(total_p1_calc * 0.25, 2)
        st.caption(f"👉 **Tổng Phần I:** **{total_p1_calc} câu** | Tổng điểm dự kiến: **{score_p1_calc} đ**")

        st.markdown("---")

        # PHẦN II
        st.markdown("##### 4. PHẦN II: Trắc nghiệm Đúng / Sai (Mỗi câu 4 ý a, b, c, d) — Mỗi câu tối đa 1.0 điểm")
        st.caption("Quy chuẩn điểm Bộ GD&ĐT: Đúng 1 ý: 0.1đ | Đúng 2 ý: 0.25đ | Đúng 3 ý: 0.5đ | Đúng 4 ý: 1.0đ.")
        col_p2_nb, col_p2_th, col_p2_vd = st.columns(3)
        with col_p2_nb:
            p2_nb = st.number_input("Số câu Nhận biết (NB):", min_value=0, max_value=10, value=2, key="p2_nb")
        with col_p2_th:
            p2_th = st.number_input("Số câu Thông hiểu (TH):", min_value=0, max_value=10, value=1, key="p2_th")
        with col_p2_vd:
            p2_vd = st.number_input("Số câu Vận dụng (VD):", min_value=0, max_value=10, value=1, key="p2_vd")
            
        total_p2_calc = p2_nb + p2_th + p2_vd
        score_p2_calc = round(total_p2_calc * 1.0, 2)
        st.caption(f"👉 **Tổng Phần II:** **{total_p2_calc} câu** | Tổng điểm dự kiến: **{score_p2_calc} đ**")

        st.markdown("---")

        # PHẦN III
        st.markdown("##### 5. PHẦN III: Trắc nghiệm trả lời ngắn — Mỗi câu 0.5 điểm")
        st.caption("Đáp số là số thực (làm tròn 1 chữ số thập phân).")
        col_p3_th, col_p3_vd, col_p3_vdc = st.columns(3)
        with col_p3_th:
            p3_th = st.number_input("Số câu Thông hiểu (TH):", min_value=0, max_value=10, value=3, key="p3_th")
        with col_p3_vd:
            p3_vd = st.number_input("Số câu Vận dụng (VD):", min_value=0, max_value=10, value=2, key="p3_vd")
        with col_p3_vdc:
            p3_vdc = st.number_input("Số câu Vận dụng cao (VDC):", min_value=0, max_value=10, value=1, key="p3_vdc")

        total_p3_calc = p3_th + p3_vd + p3_vdc
        col_p3_mod, col_p3_info = st.columns([1, 2])
        with col_p3_mod:
            p3_mod = st.number_input("Số câu mô hình hóa thực tế:", min_value=0, max_value=max(1, total_p3_calc), value=min(3, total_p3_calc), key="p3_mod")
        with col_p3_info:
            score_p3_calc = round(total_p3_calc * 0.5, 2)
            st.write("")
            st.caption(f"👉 **Tổng Phần III:** **{total_p3_calc} câu** (Trong đó {p3_mod} câu mô hình hóa) | Tổng điểm: **{score_p3_calc} đ**")

        total_exam_questions = total_p1_calc + total_p2_calc + total_p3_calc
        total_exam_score = round(score_p1_calc + score_p2_calc + score_p3_calc, 2)
        
        st.markdown(f"### 📊 Tổng quan đề: **{total_exam_questions} câu hỏi** — Tổng thang điểm: **{total_exam_score} điểm**")

        if st.button("🚀 BẮT ĐẦU TẠO ĐỀ THI THEO MA TRẬN NÀY", use_container_width=True):
            if total_exam_questions == 0:
                st.error("Tổng số câu hỏi của đề thi không được bằng 0! Vui lòng chọn ít nhất 1 câu.")
            else:
                with st.spinner("AI đang thiết kế toàn bộ câu hỏi theo đúng ma trận yêu cầu (có thể mất 15-30 giây)..."):
                    try:
                        new_exam = generate_matrix_custom_exam(
                            exam_grade, exam_term,
                            p1_nb, p1_th, p1_vd,
                            p2_nb, p2_th, p2_vd,
                            p3_th, p3_vd, p3_vdc, p3_mod
                        )
                        if new_exam:
                            st.session_state["generated_exam"] = new_exam
                            st.session_state["current_exam_idx"] = 0
                            st.session_state["user_exam_answers"] = {}
                            st.session_state["exam_submitted_result"] = None
                            st.rerun()
                    except Exception as e:
                        st.error(f"⚠️ Không thể tạo đề từ AI: {e}")

    # Giao diện làm bài thi khi đã tạo đề
    exam = st.session_state["generated_exam"]
    if exam:
        st.markdown(f"### 📋 {exam.get('exam_title', 'ĐỀ THI KHẢO THÍ')}")
        
        all_q_flat = []
        for idx, q in enumerate(exam.get("part1", [])):
            all_q_flat.append({"part": 1, "idx_part": idx, "label": f"I.{idx+1}", "data": q})
        for idx, q in enumerate(exam.get("part2", [])):
            all_q_flat.append({"part": 2, "idx_part": idx, "label": f"II.{idx+1}", "data": q})
        for idx, q in enumerate(exam.get("part3", [])):
            all_q_flat.append({"part": 3, "idx_part": idx, "label": f"III.{idx+1}", "data": q})

        total_questions = len(all_q_flat)
        
        if total_questions == 0:
            st.info("Đề thi chưa có câu hỏi nào.")
        else:
            if st.session_state["current_exam_idx"] >= total_questions:
                st.session_state["current_exam_idx"] = 0

            curr_i = st.session_state["current_exam_idx"]
            curr_q = all_q_flat[curr_i]

            col_down, col_info = st.columns([1.5, 2.5])
            with col_down:
                docx_file = export_exam_to_docx(exam)
                st.download_button(
                    label="📥 LƯU ĐỀ THÀNH FILE WORD (.DOCX)",
                    data=docx_file,
                    file_name=f"De_Thi_{exam_grade}_{exam_term}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )

            # Bảng câu hỏi tương tác (Navigation Bar)
            st.markdown("##### 🧭 Bảng câu hỏi (Bấm vào số câu để chuyển nhanh):")
            cols_nav = st.columns(min(12, total_questions))
            for i_btn, q_item in enumerate(all_q_flat):
                col_target = cols_nav[i_btn % len(cols_nav)]
                is_answered = q_item["label"] in st.session_state["user_exam_answers"]
                btn_label = f"✓ {q_item['label']}" if is_answered else q_item['label']
                
                with col_target:
                    if st.button(btn_label, key=f"nav_{i_btn}", use_container_width=True):
                        st.session_state["current_exam_idx"] = i_btn
                        st.rerun()

            # Hiển thị câu hỏi đang chọn
            with st.container(border=True):
                st.markdown(f"#### 📌 Câu hỏi {curr_q['label']} (Câu {curr_i + 1}/{total_questions})")
                
                # PHẦN I
                if curr_q["part"] == 1:
                    q_data = curr_q["data"]
                    st.markdown(f"**{q_data.get('question')}**")
                    saved_ans = st.session_state["user_exam_answers"].get(curr_q["label"], None)
                    opts = q_data.get("options", ["A", "B", "C", "D"])
                    
                    selected_opt = st.radio(
                        "Chọn đáp án của em:",
                        opts,
                        index=(["A", "B", "C", "D"].index(saved_ans) if saved_ans in ["A", "B", "C", "D"] else None),
                        key=f"radio_{curr_q['label']}"
                    )
                    if st.button("Lưu đáp án câu này", key=f"save_p1_{curr_q['label']}"):
                        if selected_opt:
                            opt_letter = selected_opt[0].upper()
                            st.session_state["user_exam_answers"][curr_q["label"]] = opt_letter
                            st.toast(f"Đã lưu đáp án {opt_letter} cho câu {curr_q['label']}!")
                            st.rerun()

                # PHẦN II
                elif curr_q["part"] == 2:
                    q_data = curr_q["data"]
                    st.markdown(f"**{q_data.get('question')}**")
                    saved_sub = st.session_state["user_exam_answers"].get(curr_q["label"], {})
                    cur_answers_p2 = {}
                    
                    for sub in q_data.get("sub_items", []):
                        lbl = sub.get("label")
                        st.write(f"**{lbl})** {sub.get('text')}")
                        prev_val = saved_sub.get(lbl, None)
                        choice = st.radio(
                            f"Ý {lbl}:",
                            ["Đúng", "Sai"],
                            index=(0 if prev_val is True else (1 if prev_val is False else None)),
                            horizontal=True,
                            key=f"sub_p2_{curr_q['label']}_{lbl}"
                        )
                        cur_answers_p2[lbl] = (choice == "Đúng") if choice else None

                    if st.button("Lưu câu Đúng/Sai này", key=f"save_p2_{curr_q['label']}"):
                        st.session_state["user_exam_answers"][curr_q["label"]] = cur_answers_p2
                        st.toast(f"Đã lưu các ý cho câu {curr_q['label']}!")
                        st.rerun()

                # PHẦN III
                elif curr_q["part"] == 3:
                    q_data = curr_q["data"]
                    if q_data.get("is_modeled"):
                        st.info("💡 *Đây là câu hỏi bài toán thực tế mô hình hóa.*")
                    st.markdown(f"**{q_data.get('question')}**")
                    prev_text = st.session_state["user_exam_answers"].get(curr_q["label"], "")
                    in_val = st.text_input("Nhập kết quả số học (làm tròn 1 chữ số thập phân):", value=prev_text, key=f"txt_p3_{curr_q['label']}")
                    if st.button("Lưu câu trả lời ngắn này", key=f"save_p3_{curr_q['label']}"):
                        if in_val.strip():
                            st.session_state["user_exam_answers"][curr_q["label"]] = in_val.strip()
                            st.toast(f"Đã lưu kết quả câu {curr_q['label']}!")
                            st.rerun()

            # NÚT NỘP TOÀN BÀI & XÁC NHẬN CHẤM ĐIỂM
            st.markdown("---")
            col_sub_all, col_res = st.columns([1.5, 2.5])
            with col_sub_all:
                with st.popover("📤 NỘP TOÀN BÀI THI", use_container_width=True):
                    st.markdown("⚠️ **XÁC NHẬN NỘP BÀI?**")
                    answered_count = len(st.session_state["user_exam_answers"])
                    st.write(f"Em đã hoàn thành: **{answered_count}/{total_questions}** câu hỏi.")
                    st.caption("Sau khi xác nhận, bài làm sẽ được gửi đi để chấm điểm ngay lập tức.")
                    
                    if st.button("Xác nhận nộp bài và chấm điểm", key="confirm_submit_exam"):
                        total_score = 0.0
                        user_ans = st.session_state["user_exam_answers"]
                        
                        # 1. Chấm phần I: Mỗi câu 0.25đ
                        p1_list = exam.get("part1", [])
                        for idx, q in enumerate(p1_list):
                            lbl = f"I.{idx+1}"
                            if user_ans.get(lbl) == q.get("correct"):
                                total_score += 0.25

                        # 2. Chấm phần II: Chuẩn Bộ GD&ĐT
                        for idx, q in enumerate(exam.get("part2", [])):
                            lbl = f"II.{idx+1}"
                            sub_dict = user_ans.get(lbl, {})
                            correct_count = 0
                            for sub in q.get("sub_items", []):
                                if sub_dict.get(sub.get("label")) == sub.get("correct"):
                                    correct_count += 1
                            if correct_count == 1:
                                total_score += 0.1
                            elif correct_count == 2:
                                total_score += 0.25
                            elif correct_count == 3:
                                total_score += 0.5
                            elif correct_count == 4:
                                total_score += 1.0

                        # 3. Chấm phần III: Mỗi câu 0.5đ
                        p3_list = exam.get("part3", [])
                        for idx, q in enumerate(p3_list):
                            lbl = f"III.{idx+1}"
                            u_v = str(user_ans.get(lbl, "")).strip().lower()
                            c_v = str(q.get("correct_num", "")).strip().lower()
                            if u_v == c_v:
                                total_score += 0.5
                            else:
                                try:
                                    if abs(float(u_v) - float(c_v)) < 0.15:
                                        total_score += 0.5
                                except Exception:
                                    pass

                        final_score = round(total_score, 2)
                        st.session_state["exam_submitted_result"] = final_score
                        reward_student_flower(student_info["student_id"], 3, f"hoàn thành bài khảo thí được {final_score} điểm")
                        st.rerun()

            # Hiển thị kết quả chấm bài
            if st.session_state["exam_submitted_result"] is not None:
                score = st.session_state["exam_submitted_result"]
                with st.container(border=True):
                    st.balloons()
                    st.markdown(f"## 🎉 KẾT QUẢ BÀI THI CỦA EM: **{score} / {total_exam_score} ĐIỂM**")
                    
                    if total_exam_score > 0 and (score / total_exam_score) >= 0.8:
                        comment = "🌟 Em học đỉnh chóp luôn á! Tư duy toán học siêu bén và tự giác vô cùng. Cố gắng giữ vững phong độ này nhé, tự hào về em quá chừng! 💖"
                    elif total_exam_score > 0 and (score / total_exam_score) >= 0.5:
                        comment = "🌸 Giỏi lắm nè! Em đã nắm rất chắc các dạng bài cơ bản rồi đó. Chỉ cần chú ý rèn thêm một chút cẩn thận ở phần tính toán là điểm cao trong tầm tay luôn nha! ✨"
                    else:
                        comment = "🌱 Đừng buồn nhé, em đã rất kiên trì hoàn thành bài thi! Mỗi lần thử là một lần mình hiểu sâu hơn. Xem lại gợi ý ở Tab 2 rồi thử sức lại nha, Thầy/Cô luôn đồng hành cùng em! 🥰"
                        
                    st.success(comment)
