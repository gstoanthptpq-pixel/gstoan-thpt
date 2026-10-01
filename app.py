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
# 2. KHỞI TẠO KẾT NỐI GEMINI API, GSHEETS & HÀM GỌI FALLBACK AN TOÀN
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
    """Fallback tự động qua các cụm model để triệt tiêu lỗi 503 và 404."""
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
# 3. RÀ SOÁT & TỐI ƯU HÌNH ẢNH VECTOR SVG (CHỐNG ĐÈ CHỮ, CHUẨN ĐIỂM CỰC TRỊ)
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
    """Sinh đề thi theo chi tiết số lượng câu của từng mức độ nhận thức."""
    total_p1 = p1_nb + p1_th + p1_vd
    total_p2 = p2_nb + p2_th + p2_vd
    total_p3 = p3_th + p3_vd + p3_vdc
    
    prompt = (
        f"Bạn là chuyên gia khảo thí môn Toán THPT Chương trình GDPT 2018 (Bộ sách Kết nối tri thức).\n"
        f"Hãy tạo 1 đề thi môn Toán dành cho {grade}, kỳ thi: {term}.\n"
        f"MA TRẬN CẤU TRÚC CHI TIẾT:\n"
        f"- PHẦN I (Trắc nghiệm 4 lựa chọn, chọn 1): Tổng {total_p1} câu. Trong đó: {p1_nb} câu Nhận biết, {p1_th} câu Thông hiểu, {p1_vd} câu Vận dụng.\n"
        f"- PHẦN II (Trắc nghiệm Đúng/Sai, mỗi câu 4 ý a,b,c,d): Tổng {total_p2} câu. Trong đó có {p2_nb} câu Nhận biết, {p2_th} câu Thông hiểu, {p2_vd} câu Vận dụng.\n"
        f"- PHẦN III (Trắc nghiệm trả lời ngắn): Tổng {total_p3} câu. Trong đó: {p3_th} câu Thông hiểu, {p3_vd} câu Vận dụng, {p3_vdc} câu Vận dụng cao. Có {p3_mod} câu bài toán thực tế mô hình hóa. Đáp án bắt buộc là số thực.\n"
        "Nếu phần nào có số câu là 0 thì trả về mảng rỗng [] cho phần đó.\n"
        "Trả về DUY NHẤT một chuỗi JSON hợp lệ không có markdown bọc ngoài:\n"
        "{\n"
        '  "exam_title": "ĐỀ THI ' + f'{grade.upper()} - {term.upper()}' + '",\n'
        '  "part1": [\n'
        '    {"id": "P1_1", "question": "Nội dung...", "options": ["A. ...", "B. ...", "C. ...", "D. ..."], "correct": "A"}\n'
        '  ],\n'
        '  "part2": [\n'
        '    {"id": "P2_1", "question": "Nội dung...", "sub_items": [{"label": "a", "text": "...", "correct": true}, {"label": "b", "text": "...", "correct": false}, {"label": "c", "text": "...", "correct": true}, {"label": "d", "text": "...", "correct": false}]}\n'
        '  ],\n'
        '  "part3": [\n'
        '    {"id": "P3_1", "question": "Nội dung...", "correct_num": "4.5", "is_modeled": true}\n'
        '  ]\n'
        "}"
    )
    try:
        raw = call_gemini_safe([prompt])
        t = raw.strip()
        if t.startswith("```json"):
            t = t[7:]
        if t.endswith("
