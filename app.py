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
from datetime import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# ==============================================================================
# 1. CẤU HÌNH GIAO DIỆN & TÙY BIẾN CHẾ ĐỘ SÁNG / TỐI (LIGHT / DARK THEME)
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
# 2. KHỞI TẠO KẾT NỐI GEMINI API, GSHEETS & HÀM GỌI AI FALLBACK CHỐNG LỖI 503/404
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

def call_gemini_safe(contents_payload):
    """
    Cơ chế Fallback thông minh: Thử lần lượt các cụm model.
    Nếu cụm 3.8 quá tải (503), tự động chuyển sang 2.5-flash hoặc 2.0-flash.
    """
    if not client:
        return None
    
    candidate_models = ['gemini-3.8-flash', 'gemini-2.5-flash', 'gemini-2.0-flash']
    last_err = ""
    
    for m in candidate_models:
        for attempt in range(2):
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
                if "503" in err_str or "429" in err_str:
                    time.sleep(2)
                    break
                time.sleep(1)
                continue
                
    raise Exception(f"Máy chủ AI đang phản hồi: {last_err}")

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
# 3. ENGINE RENDER HÌNH ẢNH SVG ĐỘC LẬP (CÔ LẬP TRONG IFRAME)
# ==============================================================================
PRESET_SVGS = {
    "DON_DIEU": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="80" y1="15" x2="80" y2="185" stroke="#475569" stroke-width="2"/><line x1="20" y1="55" x2="480" y2="55" stroke="#475569" stroke-width="2"/><line x1="20" y1="95" x2="480" y2="95" stroke="#475569" stroke-width="2"/><text x="45" y="42" font-family="sans-serif" font-size="16" font-weight="bold">x</text><text x="45" y="82" font-family="sans-serif" font-size="16" font-weight="bold">y'</text><text x="45" y="145" font-family="sans-serif" font-size="16" font-weight="bold">y</text><text x="210" y="42" font-family="sans-serif" font-size="15" font-weight="bold">x₁</text><text x="330" y="42" font-family="sans-serif" font-size="15" font-weight="bold">x₂</text><text x="215" y="82" font-family="sans-serif" font-size="16">0</text><text x="335" y="82" font-family="sans-serif" font-size="16">0</text><text x="150" y="82" font-family="sans-serif" font-size="18" font-weight="bold" fill="#16A34A">+</text><text x="270" y="82" font-family="sans-serif" font-size="20" font-weight="bold" fill="#DC2626">-</text><text x="390" y="82" font-family="sans-serif" font-size="18" font-weight="bold" fill="#16A34A">+</text><line x1="110" y1="165" x2="200" y2="115" stroke="#2563EB" stroke-width="3"/><line x1="230" y1="115" x2="320" y2="165" stroke="#DC2626" stroke-width="3"/><line x1="350" y1="165" x2="440" y2="115" stroke="#2563EB" stroke-width="3"/></svg>""",
    "TAP_HOP": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><circle cx="210" cy="100" r="70" fill="#93C5FD" fill-opacity="0.5" stroke="#2563EB" stroke-width="2"/><circle cx="290" cy="100" r="70" fill="#FCA5A5" fill-opacity="0.5" stroke="#DC2626" stroke-width="2"/><text x="165" y="105" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E40AF">Tập A</text><text x="315" y="105" font-family="sans-serif" font-size="16" font-weight="bold" fill="#991B1B">Tập B</text><text x="235" y="105" font-family="sans-serif" font-size="15" font-weight="bold" fill="#047857">A ∩ B</text></svg>""",
    "VECTOR": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#2563EB"/></marker></defs><line x1="100" y1="150" x2="380" y2="50" stroke="#2563EB" stroke-width="4" marker-end="url(#arrow)"/><circle cx="100" cy="150" r="5" fill="#DC2626"/><text x="80" y="170" font-family="sans-serif" font-size="16" font-weight="bold">A</text><text x="400" y="45" font-family="sans-serif" font-size="16" font-weight="bold">B</text><text x="220" y="90" font-family="sans-serif" font-size="18" font-weight="bold" fill="#2563EB">Vectơ u = AB</text></svg>""",
    "LUONG_GIAC": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="140" y1="100" x2="360" y2="100" stroke="#334155" stroke-width="2"/><line x1="250" y1="190" x2="250" y2="10" stroke="#334155" stroke-width="2"/><circle cx="250" cy="100" r="75" fill="none" stroke="#0284C7" stroke-width="2"/><text x="365" y="105" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563EB">Cos (+)</text><text x="255" y="23" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Sin (+)</text><line x1="250" y1="100" x2="303" y2="47" stroke="#D97706" stroke-width="2.5"/><circle cx="303" cy="47" r="4.5" fill="#D97706"/><text x="312" y="47" font-family="sans-serif" font-size="13" font-weight="bold" fill="#B45309">M(cosα; sinα)</text></svg>""",
    "DAY_SO": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><defs><marker id="arr_ds" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#DC2626"/></marker></defs><line x1="50" y1="120" x2="450" y2="120" stroke="#475569" stroke-width="3"/><circle cx="100" cy="120" r="6" fill="#2563EB"/><text x="90" y="150" font-family="sans-serif" font-size="16" font-weight="bold">u₁</text><circle cx="200" cy="120" r="6" fill="#2563EB"/><text x="190" y="150" font-family="sans-serif" font-size="16" font-weight="bold">u₂</text><circle cx="300" cy="120" r="6" fill="#2563EB"/><text x="290" y="150" font-family="sans-serif" font-size="16" font-weight="bold">u₃</text><circle cx="400" cy="120" r="6" fill="#2563EB"/><text x="390" y="150" font-family="sans-serif" font-size="16" font-weight="bold">u₄</text><path d="M 100 105 Q 150 50 195 105" fill="none" stroke="#DC2626" stroke-width="2" stroke-dasharray="4" marker-end="url(#arr_ds)"/><path d="M 200 105 Q 250 50 295 105" fill="none" stroke="#DC2626" stroke-width="2" stroke-dasharray="4" marker-end="url(#arr_ds)"/><text x="235" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">+ d (CSC) / × q (CSN)</text></svg>""",
    "HINH_KHONG_GIAN": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><polygon points="170,160 350,160 290,110" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/><line x1="250" y1="25" x2="250" y2="135" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="4"/><line x1="250" y1="25" x2="170" y2="160" stroke="#1E293B" stroke-width="2"/><line x1="250" y1="25" x2="350" y2="160" stroke="#1E293B" stroke-width="2"/><line x1="250" y1="25" x2="290" y2="110" stroke="#1E293B" stroke-width="2" stroke-dasharray="3"/><text x="245" y="18" font-family="sans-serif" font-size="15" font-weight="bold" fill="#DC2626">S</text><text x="155" y="170" font-family="sans-serif" font-size="14" font-weight="bold">A</text><text x="360" y="170" font-family="sans-serif" font-size="14" font-weight="bold">B</text><text x="295" y="100" font-family="sans-serif" font-size="14" font-weight="bold">C</text><text x="255" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#DC2626">H</text></svg>""",
    "OXYZ": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="240" y1="120" x2="240" y2="20" stroke="#0284C7" stroke-width="2.5"/><line x1="240" y1="120" x2="420" y2="120" stroke="#16A34A" stroke-width="2.5"/><line x1="240" y1="120" x2="120" y2="190" stroke="#DC2626" stroke-width="2.5"/><text x="245" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0284C7">Oz (Cao độ)</text><text x="425" y="125" font-family="sans-serif" font-size="14" font-weight="bold" fill="#16A34A">Oy (Tung độ)</text><text x="105" y="195" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Ox (Hoành độ)</text><circle cx="310" cy="70" r="5" fill="#D97706"/><text x="320" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#B45309">M(x; y; z)</text></svg>""",
    "CUC_TRI": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="40" y1="175" x2="460" y2="175" stroke="#64748B" stroke-width="1.5"/><line x1="70" y1="190" x2="70" y2="15" stroke="#64748B" stroke-width="1.5"/><path d="M 90 160 C 140 15, 200 25, 250 95 C 300 165, 360 175, 420 15" fill="none" stroke="#2563EB" stroke-width="3"/><circle cx="170" cy="40" r="5" fill="#16A34A"/><text x="135" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#15803D">Cực Đại (y' = 0)</text><circle cx="330" cy="150" r="5" fill="#DC2626"/><text x="295" y="180" font-family="sans-serif" font-size="14" font-weight="bold" fill="#B91C1C">Cực Tiểu (y' = 0)</text></svg>""",
    "TIEM_CAN": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="30" y1="130" x2="470" y2="130" stroke="#94A3B8" stroke-width="1.5"/><line x1="160" y1="190" x2="160" y2="10" stroke="#94A3B8" stroke-width="1.5"/><line x1="230" y1="10" x2="230" y2="190" stroke="#DC2626" stroke-width="2" stroke-dasharray="6"/><text x="235" y="28" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DC2626">TCĐ: x = x₀</text><line x1="20" y1="65" x2="480" y2="65" stroke="#2563EB" stroke-width="2" stroke-dasharray="6"/><text x="380" y="58" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563EB">TCN: y = y₀</text><path d="M 50 58 Q 180 56 215 15" fill="none" stroke="#0F172A" stroke-width="2.5"/><path d="M 245 185 Q 270 75 450 73" fill="none" stroke="#0F172A" stroke-width="2.5"/></svg>""",
    "GTLN_GTNN": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><path d="M 130 140 Q 220 20 280 60 T 390 120" fill="none" stroke="#2563EB" stroke-width="3"/><line x1="130" y1="190" x2="130" y2="10" stroke="#94A3B8" stroke-dasharray="4"/><line x1="390" y1="190" x2="390" y2="10" stroke="#94A3B8" stroke-dasharray="4"/><text x="125" y="195" font-family="sans-serif" font-weight="bold">a</text><text x="385" y="195" font-family="sans-serif" font-weight="bold">b</text><circle cx="215" cy="40" r="5" fill="#16A34A"/><text x="225" y="35" font-family="sans-serif" font-weight="bold" fill="#15803D">max f(x)</text><circle cx="130" cy="140" r="5" fill="#DC2626"/><text x="140" y="150" font-family="sans-serif" font-weight="bold" fill="#B91C1C">min f(x)</text></svg>""",
    "TICH_PHAN": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="40" y1="160" x2="460" y2="160" stroke="#64748B" stroke-width="1.5"/><line x1="80" y1="190" x2="80" y2="20" stroke="#64748B" stroke-width="1.5"/><path d="M 120 160 Q 220 40 340 160 Z" fill="#93C5FD" fill-opacity="0.6" stroke="#2563EB" stroke-width="2.5"/><text x="115" y="180" font-family="sans-serif" font-size="14" font-weight="bold">a</text><text x="335" y="180" font-family="sans-serif" font-size="14" font-weight="bold">b</text><text x="210" y="125" font-family="sans-serif" font-size="15" font-weight="bold" fill="#1E40AF">S = ∫ f(x)dx</text></svg>""",
    "XAC_SUAT": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><rect x="150" y="80" width="40" height="100" fill="#3B82F6"/><rect x="230" y="40" width="40" height="140" fill="#10B981"/><rect x="310" y="110" width="40" height="70" fill="#F59E0B"/><line x1="100" y1="180" x2="400" y2="180" stroke="#334155" stroke-width="2"/><line x1="100" y1="180" x2="100" y2="20" stroke="#334155" stroke-width="2"/><text x="190" y="30" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">Xác suất & Thống kê</text></svg>""",
    "MAT_PHANG": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><polygon points="100,160 360,160 420,70 160,70" fill="#E0F2FE" stroke="#0284C7" stroke-width="2.5"/><circle cx="260" cy="115" r="5" fill="#1E293B"/><text x="270" y="125" font-family="sans-serif" font-size="14" font-weight="bold">M₀(x₀; y₀; z₀)</text><line x1="260" y1="115" x2="260" y2="25" stroke="#DC2626" stroke-width="3"/><polygon points="260,18 254,32 266,32" fill="#DC2626"/><text x="272" y="35" font-family="sans-serif" font-size="15" font-weight="bold" fill="#DC2626">n⃗ = (A; B; C) ⊥ (P)</text></svg>""",
    "MAT_CAU": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><circle cx="250" cy="100" r="80" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/><ellipse cx="250" cy="100" rx="80" ry="25" fill="none" stroke="#0284C7" stroke-width="2" stroke-dasharray="5"/><circle cx="250" cy="100" r="4" fill="#DC2626"/><text x="235" y="90" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">I(a; b; c)</text><line x1="250" y1="100" x2="315" y2="55" stroke="#16A34A" stroke-width="3"/><text x="280" y="70" font-family="sans-serif" font-size="16" font-weight="bold" fill="#15803D">R</text></svg>""",
    "DUONG_THANG_OXYZ": """<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg"><rect width="500" height="200" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/><line x1="80" y1="160" x2="420" y2="40" stroke="#0284C7" stroke-width="3"/><text x="90" y="145" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0284C7">d</text><circle cx="200" cy="117.6" r="5" fill="#DC2626"/><text x="210" y="130" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">M₀(x₀; y₀; z₀)</text><line x1="280" y1="89.4" x2="365" y2="59.4" stroke="#16A34A" stroke-width="3"/><polygon points="375,56 362,64 366,54" fill="#16A34A"/><text x="290" y="75" font-family="sans-serif" font-size="15" font-weight="bold" fill="#16A34A">u⃗ = (a; b; c)</text></svg>"""
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
    components.html(html_payload, height=210)

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

# Session lưu trữ trạng thái khảo thí Tab 5
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
# HÀM AI SINH ĐỀ TƯƠNG TỰ, ĐỀ NÂNG CAO VÀ ĐỀ THI ĐỊNH KỲ (FALLBACK SAFE)
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

def generate_custom_full_exam(grade, term, n_p1, n_p2, n_p3, n_mod):
    """Sinh đề thi qua AI; nếu Google quá tải 503, tự động kích hoạt đề thi mẫu chuẩn ma trận."""
    prompt = (
        f"Bạn là chuyên gia khảo thí môn Toán THPT Chương trình GDPT 2018 (Bộ sách Kết nối tri thức).\n"
        f"Hãy tạo 1 đề thi môn Toán dành cho {grade}, kỳ thi: {term}.\n"
        f"Cấu trúc: {n_p1} câu phần I (trắc nghiệm 4 lựa chọn), {n_p2} câu phần II (Đúng/Sai 4 ý a,b,c,d), "
        f"{n_p3} câu phần III (trả lời ngắn, có {n_mod} câu mô hình hóa). "
        "Trả về DUY NHẤT một chuỗi JSON hợp lệ không có markdown bọc ngoài:\n"
        "{\n"
        '  "exam_title": "ĐỀ KIỂM TRA ' + f'{grade.upper()} - {term.upper()}' + '",\n'
        '  "part1": [{"id": "P1_1", "question": "Nội dung...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "correct": "A"}],\n'
        '  "part2": [{"id": "P2_1", "question": "Nội dung...", "sub_items": [{"label": "a", "text": "...", "correct": true}]}],\n'
        '  "part3": [{"id": "P3_1", "question": "Nội dung...", "correct_num": "5", "is_modeled": true}]\n'
        "}"
    )
    try:
        raw = call_gemini_safe([prompt])
        t = raw.strip()
        if t.startswith("```json"):
            t = t[7:]
        if t.endswith("```"):
            t = t[:-3]
        return json.loads(t.strip())
    except Exception:
        # Tự động nạp đề chuẩn bị sẵn nếu AI bị quá tải 503 để học sinh không bị gián đoạn
        return {
            "exam_title": f"ĐỀ THI KHẢO THÍ CHUẨN HÓA {grade.upper()} - {term.upper()}",
            "part1": [
                {"id": "P1_1", "question": f"Cho hàm số bậc ba $y = f(x)$ có bảng biến thiên chuẩn. Điểm cực đại của hàm số đã cho là:", "options": ["A. x = 1", "B. x = -1", "C. y = 2", "D. x = 3"], "correct": "A"},
                {"id": "P1_2", "question": "Tập nghiệm của bất phương trình $\\log_2(x - 1) < 3$ là:", "options": ["A. (1; 9)", "B. (-vô cực; 9)", "C. (1; 8)", "D. (0; 9)"], "correct": "A"},
                {"id": "P1_3", "question": "Trong không gian Oxyz, vectơ nào sau đây là một vectơ pháp tuyến của mặt phẳng (P): $2x - y + 3z - 1 = 0$?", "options": ["A. (2; -1; 3)", "B. (2; 1; 3)", "C. (-2; -1; 3)", "D. (2; -1; -1)"], "correct": "A"}
            ],
            "part2": [
                {
                    "id": "P2_1",
                    "question": "Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a, $SA \\perp (ABCD)$ và $SA = a\\sqrt{2}$. Xét tính đúng sai của các khẳng định sau:",
                    "sub_items": [
                        {"label": "a", "text": "Đường thẳng SA vuông góc với mặt phẳng (ABCD).", "correct": True},
                        {"label": "b", "text": "Tam giác SBC là tam giác vuông tại B.", "correct": True},
                        {"label": "c", "text": "Góc giữa đường thẳng SC và mặt phẳng (ABCD) bằng 60 độ.", "correct": False},
                        {"label": "d", "text": "Thể tích khối chóp S.ABCD bằng a^3 căn 2 chia 3.", "correct": True}
                    ]
                }
            ],
            "part3": [
                {"id": "P3_1", "question": "Một xưởng sản xuất muốn tối ưu hóa chi phí làm hộp chứa hàng dạng hình hộp chữ nhật không nắp có thể tích 500 m^3. Chiều dài đáy gấp đôi chiều rộng. Tính chiều rộng của đáy (mét) để diện tích vật liệu làm hộp nhỏ nhất (làm tròn 1 chữ số thập phân).", "correct_num": "6.1", "is_modeled": True},
                {"id": "P3_2", "question": "Tính đạo hàm cấp hai của hàm số $y = x^4 - 2x^2$ tại điểm $x = 2$.", "correct_num": "44", "is_modeled": False}
            ]
        }

def export_exam_to_docx(exam_data):
    """Xuất đề thi ra file Word (.docx) chuẩn format có thể in trực tiếp."""
    doc = Document()
    
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = title_p.add_run(exam_data.get("exam_title", "ĐỀ THI MÔN TOÁN THPT").upper() + "\n")
    run_t.bold = True
    run_t.font.size = Pt(14)
    run_sub = title_p.add_run("Thời gian làm bài: 90 phút (Không kể thời gian phát đề)\n-----------------------")
    run_sub.font.italic = True
    
    doc.add_heading("PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Thí sinh chọn 1 đáp án)", level=2)
    for idx, q in enumerate(exam_data.get("part1", [])):
        p = doc.add_paragraph()
        p.add_run(f"Câu {idx + 1}: ").bold = True
        p.add_run(q.get("question", ""))
        for opt in q.get("options", []):
            doc.add_paragraph(f"    {opt}")

    doc.add_heading("PHẦN II. Câu trắc nghiệm Đúng/Sai (Mỗi câu thí sinh trả lời đúng/sai cho các ý a, b, c, d)", level=2)
    for idx, q in enumerate(exam_data.get("part2", [])):
        p = doc.add_paragraph()
        p.add_run(f"Câu {idx + 1}: ").bold = True
        p.add_run(q.get("question", ""))
        for sub in q.get("sub_items", []):
            doc.add_paragraph(f"    {sub.get('label')}) {sub.get('text')}")

    doc.add_heading("PHẦN III. Câu trắc nghiệm trả lời ngắn (Thí sinh điền kết quả vào ô trả lời)", level=2)
    for idx, q in enumerate(exam_data.get("part3", [])):
        p = doc.add_paragraph()
        p.add_run(f"Câu {idx + 1}: ").bold = True
        p.add_run(q.get("question", ""))
        doc.add_paragraph("    Đáp số: .....................................................")

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
            login_role = st.radio("Vai trò:", ["👨‍🎓 Học sinh", "👩‍🏫 Giáo viên (Admin)"], horizontal=True)
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
# 8. PHÂN HỆ HỌC SINH (5 TABS & TÌM KIẾM NHANH)
# ==============================================================================
student_info = st.session_state["auth_user"]

search_kw = st.text_input("🔍 Tìm kiếm nhanh bài học, chủ điểm (Ví dụ: 'Simpson', 'Đạo hàm', 'Tọa độ'):", "")

c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])
with c_gr:
    user_grade_default = 2 if student_info.get("grade") == 12 else (0 if student_info.get("grade") == 10 else 1)
    sel_grade = st.selectbox("📚 Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

grade_dict = CURRICULUM_DATA.get(sel_grade, {})
if not grade_dict:
    st.warning(f"Dữ liệu của {sel_grade} đang được đồng bộ hóa. Vui lòng kiểm tra lại file data tương ứng!")
    st.stop()

all_lessons = list(grade_dict.keys())
if search_kw.strip():
    filtered_lessons = []
    kw_lower = search_kw.strip().lower()
    for l_name, l_data in grade_dict.items():
        if kw_lower in l_name.lower() or any(kw_lower in t.lower() for t in l_data.get("topics", {}).keys()):
            filtered_lessons.append(l_name)
    lesson_list = filtered_lessons if filtered_lessons else all_lessons
    if not filtered_lessons:
        st.info("Không tìm thấy bài học trùng khớp, hiển thị danh mục mặc định.")
else:
    lesson_list = all_lessons

with c_les:
    sel_lesson = st.selectbox(f"📖 Bài học ({len(lesson_list)} bài):", lesson_list)

cur_lesson_obj = grade_dict[sel_lesson]

with c_top:
    topic_list = list(cur_lesson_obj["topics"].keys())
    sel_topic = st.selectbox("🎯 Danh sách Chủ điểm (Vở tự học):", topic_list)

cur_topic_data = cur_lesson_obj["topics"][sel_topic]

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
    st.markdown(f"#### {sel_lesson} — *{sel_topic}*")

    col_img, col_n = st.columns([1.2, 1.1])
    
    with col_img:
        with st.container(border=True):
            st.markdown("🖼️ **Hình ảnh minh họa kiến thức (Tạo riêng cho chủ điểm):**")
            render_dynamic_svg(cur_topic_data.get("svg", "DON_DIEU"))
            
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Chủ Điểm (Trích Vở tự học):</b><br>
                <small>Nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5((sel_lesson + sel_topic).encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_topic_data.get("audio", "Bài giảng vi mô."), audio_hash)
            if lecture_audio_file:
                st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã nghe xong bài giảng vi mô (+1 hoa)", key=f"btn_audio_{sel_topic}"):
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
# TAB 2: VÍ DỤ MINH HỌA
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Toàn Bộ Ví Dụ Minh Họa Chuẩn Mực — {sel_lesson}")
    st.caption("Hệ thống tự động tải toàn bộ ví dụ minh họa của TỪNG CHỦ ĐIỂM trong bài học. Bấm vào từng đề bài để xem lời giải chi tiết chuẩn mực sư phạm.")

    all_topics_in_lesson = cur_lesson_obj.get("topics", {})
    for t_name, t_content in all_topics_in_lesson.items():
        with st.container(border=True):
            st.markdown(f"<div class='topic-card'><b>🎯 {t_name}</b></div>", unsafe_allow_html=True)
            topic_examples = t_content.get("examples", [])
            if not topic_examples:
                st.info("Chủ điểm này đang được đồng bộ hóa ví dụ.")
            else:
                for idx, ex_item in enumerate(topic_examples):
                    is_default_open = (t_name == sel_topic and idx == 0)
                    with st.expander(f"📌 {ex_item['title']}", expanded=is_default_open):
                        st.markdown(f"**Đề bài yêu cầu:**\n\n{ex_item['problem']}")
                        st.markdown("---")
                        st.markdown("**✍️ Lời giải chi tiết chuẩn mực sư phạm:**")
                        st.markdown(ex_item["solution"])

# ------------------------------------------------------------------------------
# TAB 3: HỌC SINH TỰ GIẢI
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

    for t_name, t_content in all_topics_in_lesson.items():
        st.markdown(f"<div class='topic-card'><b>🎯 {t_name} — Bài Tập Tự Luyện Tương Tự</b></div>", unsafe_allow_html=True)
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
                        f"Học sinh đang tự học bài: '{sel_lesson}', chủ điểm: '{sel_topic}'.\n\n"
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
# TAB 5: PHÒNG KHẢO THÍ CHUẨN MA TRẬN GDPT 2018 (TƯƠNG TÁC TỪNG CÂU & XUẤT DOCX)
# ------------------------------------------------------------------------------
with tab4:
    st.subheader("🎯 Phòng Khảo Thí & Luyện Đề Chuẩn Hóa GDPT 2018")
    st.caption("Cấu trúc đề thi mới nhất bám sát khung năng lực của Bộ Giáo dục và Đào tạo. Tùy chọn ma trận, tương tác làm từng câu và lưu đề file Word.")

    with st.expander("⚙️ BẢNG TÙY CHỌN MA TRẬN ĐỀ THI", expanded=(st.session_state["generated_exam"] is None)):
        c1, c2 = st.columns(2)
        with c1:
            exam_grade = st.selectbox("1. Khối lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=(2 if sel_grade=="Khối 12" else (0 if sel_grade=="Khối 10" else 1)))
        with c2:
            exam_term = st.selectbox("2. Kỳ kiểm tra:", ["Giữa kỳ 1", "Cuối kỳ 1", "Giữa kỳ 2", "Cuối kỳ 2"])
            
        st.markdown("---")
        st.markdown("##### 3. PHẦN I: Trắc nghiệm 1 lựa chọn (A, B, C, D) — Mặc định 3.0 điểm")
        col_p1_1, col_p1_2 = st.columns([1, 2])
        with col_p1_1:
            p1_count = st.number_input("Số câu phần I:", min_value=1, max_value=20, value=12)
        with col_p1_2:
            st.caption("Cấu hình mức độ mặc định: **6 Nhận biết (NB), 5 Thông hiểu (TH), 1 Vận dụng (VD)**.")

        st.markdown("##### 4. PHẦN II: Trắc nghiệm Đúng / Sai (Mỗi câu 4 ý a, b, c, d) — Mặc định 4.0 điểm")
        col_p2_1, col_p2_2 = st.columns([1, 2])
        with col_p2_1:
            p2_count = st.number_input("Số câu phần II:", min_value=1, max_value=10, value=4)
        with col_p2_2:
            st.caption("Quy chuẩn điểm Bộ GD&ĐT: Đúng 1 ý: 0.1đ | Đúng 2 ý: 0.25đ | Đúng 3 ý: 0.5đ | Đúng 4 ý: 1.0đ. Mức độ: [NB, NB, TH, VD].")

        st.markdown("##### 5. PHẦN III: Trắc nghiệm trả lời ngắn — Mặc định 3.0 điểm (Mỗi câu 0.5đ)")
        col_p3_1, col_p3_2, col_p3_3 = st.columns([1, 1, 1])
        with col_p3_1:
            p3_count = st.number_input("Số câu phần III:", min_value=1, max_value=10, value=6)
        with col_p3_2:
            p3_modeled = st.number_input("Số câu mô hình hóa thực tế:", min_value=0, max_value=p3_count, value=3)
        with col_p3_3:
            st.caption("Mức độ: 3 TH, 2 VD, 1 VDC. Đáp số là số thực (làm tròn 1 chữ số thập phân).")

        if st.button("🚀 BẮT ĐẦU TẠO ĐỀ THI", use_container_width=True):
            with st.spinner("AI đang thiết kế và chuẩn hóa đề thi theo đúng ma trận yêu cầu..."):
                try:
                    new_exam = generate_custom_full_exam(exam_grade, exam_term, p1_count, p2_count, p3_count, p3_modeled)
                    if new_exam:
                        st.session_state["generated_exam"] = new_exam
                        st.session_state["current_exam_idx"] = 0
                        st.session_state["user_exam_answers"] = {}
                        st.session_state["exam_submitted_result"] = None
                        st.rerun()
                    else:
                        st.error("Không thể tạo đề lúc này, vui lòng thử lại.")
                except Exception as e:
                    st.error(f"Lỗi tạo đề: {e}")

    # Giao diện làm bài thi khi đã tạo đề
    exam = st.session_state["generated_exam"]
    if exam:
        st.markdown(f"### 📋 {exam.get('exam_title', 'ĐỀ THI KHẢO THÍ')}")
        
        # Gom danh sách toàn bộ câu hỏi để điều hướng
        all_q_flat = []
        for idx, q in enumerate(exam.get("part1", [])):
            all_q_flat.append({"part": 1, "idx_part": idx, "label": f"I.{idx+1}", "data": q})
        for idx, q in enumerate(exam.get("part2", [])):
            all_q_flat.append({"part": 2, "idx_part": idx, "label": f"II.{idx+1}", "data": q})
        for idx, q in enumerate(exam.get("part3", [])):
            all_q_flat.append({"part": 3, "idx_part": idx, "label": f"III.{idx+1}", "data": q})

        total_questions = len(all_q_flat)
        curr_i = st.session_state["current_exam_idx"]
        curr_q = all_q_flat[curr_i]

        # Nút Lưu đề Word (.docx)
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

        # Hiển thị nội dung câu hỏi hiện tại
        with st.container(border=True):
            st.markdown(f"#### 📌 Câu hỏi {curr_q['label']} (Câu {curr_i + 1}/{total_questions})")
            
            # --- PHẦN I ---
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

            # --- PHẦN II ---
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

            # --- PHẦN III ---
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

        # NÚT NỘP TOÀN BÀI & CƠ CHẾ XÁC NHẬN CHẤM ĐIỂM
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
                    
                    # 1. Chấm phần I: 12 câu -> 3 điểm (mỗi câu 0.25đ)
                    p1_list = exam.get("part1", [])
                    p1_score_per_q = 3.0 / len(p1_list) if p1_list else 0.25
                    for idx, q in enumerate(p1_list):
                        lbl = f"I.{idx+1}"
                        if user_ans.get(lbl) == q.get("correct"):
                            total_score += p1_score_per_q

                    # 2. Chấm phần II: Chuẩn Bộ GD&ĐT (đúng 1 ý 0.1đ, đúng 2 ý 0.25đ, đúng 3 ý 0.5đ, đúng 4 ý 1.0đ)
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

                    # 3. Chấm phần III: 6 câu -> 3 điểm (mỗi câu 0.5đ)
                    p3_list = exam.get("part3", [])
                    p3_score_per_q = 3.0 / len(p3_list) if p3_list else 0.5
                    for idx, q in enumerate(p3_list):
                        lbl = f"III.{idx+1}"
                        u_v = str(user_ans.get(lbl, "")).strip().lower()
                        c_v = str(q.get("correct_num", "")).strip().lower()
                        if u_v == c_v:
                            total_score += p3_score_per_q
                        else:
                            try:
                                if abs(float(u_v) - float(c_v)) < 0.15:
                                    total_score += p3_score_per_q
                            except Exception:
                                pass

                    final_score = round(total_score, 2)
                    st.session_state["exam_submitted_result"] = final_score
                    reward_student_flower(student_info["student_id"], 3, f"hoàn thành bài khảo thí được {final_score} điểm")
                    st.rerun()

        # Hiển thị kết quả chấm bài và nhận xét động viên
        if st.session_state["exam_submitted_result"] is not None:
            score = st.session_state["exam_submitted_result"]
            with st.container(border=True):
                st.balloons()
                st.markdown(f"## 🎉 KẾT QUẢ BÀI THI CỦA EM: **{score} / 10.0 ĐIỂM**")
                
                if score >= 8.5:
                    comment = "🌟 Em học đỉnh chóp luôn á! Tư duy toán học siêu bén và tự giác vô cùng. Cố gắng giữ vững phong độ này nhé, tự hào về em quá chừng! 💖"
                elif score >= 6.5:
                    comment = "🌸 Giỏi lắm nè! Em đã nắm rất chắc các dạng bài cơ bản rồi đó. Chỉ cần chú ý rèn thêm một chút cẩn thận ở phần tính toán là điểm 9, 10 trong tầm tay luôn nha! ✨"
                else:
                    comment = "🌱 Đừng buồn nhé, em đã rất kiên trì hoàn thành cả bài thi dài rồi! Mỗi lần sai là một lần mình hiểu sâu hơn. Xem lại gợi ý ở Tab 2 rồi thử sức lại nha, Thầy/Cô luôn đồng hành cùng em! 🥰"
                    
                st.success(comment)
