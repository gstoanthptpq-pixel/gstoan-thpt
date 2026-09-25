import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google import genai
import pandas as pd
from PIL import Image
from gtts import gTTS
import plotly.graph_objects as go
from datetime import datetime
import os
import hashlib

# ==============================================================================
# 1. CẤU HÌNH GIAO DIỆN & THANH CUỘN CHO BÀI HỌC VÀ CHỦ ĐIỂM
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Thanh cuộn chuyên biệt cho Dropdown danh sách bài học và chủ điểm */
    div[data-baseweb="popover"] ul, div[role="listbox"] {
        max-height: 320px !important;
        overflow-y: auto !important;
        scrollbar-width: thin;
        scrollbar-color: #3B82F6 #F1F5F9;
    }
    div[data-baseweb="popover"] ul::-webkit-scrollbar, div[role="listbox"]::-webkit-scrollbar {
        width: 8px;
    }
    div[data-baseweb="popover"] ul::-webkit-scrollbar-thumb, div[role="listbox"]::-webkit-scrollbar-thumb {
        background-color: #3B82F6;
        border-radius: 4px;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px !important;
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        padding: 16px !important;
        margin-bottom: 14px !important;
    }
    .stButton>button {
        border-radius: 10px;
        background: linear-gradient(90deg, #1E3A8A, #2563EB);
        color: white;
        font-weight: 600;
        border: none;
        padding: 8px 18px;
        transition: all 0.25s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }
    .audio-box {
        background: linear-gradient(135deg, #F0FDF4, #DCFCE7);
        border: 1px solid #86EFAC;
        padding: 12px;
        border-radius: 10px;
        margin-top: 12px;
    }
    .img-box {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .rule-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. KHỞI TẠO KẾT NỐI GEMINI API & GOOGLE SHEETS
# ==============================================================================
client = None
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    except Exception:
        pass

conn = None
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    pass

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
# 3. TRÌNH TẠO HÌNH ẢNH MINH HỌA VECTOR CHUẨN SGK & VỞ TỰ HỌC
# ==============================================================================
def render_sgk_illustration_svg(topic_name, lesson_name):
    """Tạo sơ đồ hình ảnh đồ họa chuẩn mực thay thế video, mô phỏng các hình vẽ SGK."""
    t_low = (topic_name + " " + lesson_name).lower()
    
    # 1. Hình ảnh: Bảng biến thiên (Đơn điệu)
    if "đơn điệu" in t_low or "đồng biến" in t_low:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/>
            <line x1="80" y1="20" x2="80" y2="200" stroke="#475569" stroke-width="2"/>
            <line x1="20" y1="60" x2="480" y2="60" stroke="#475569" stroke-width="2"/>
            <line x1="20" y1="100" x2="480" y2="100" stroke="#475569" stroke-width="2"/>
            <text x="45" y="45" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">x</text>
            <text x="45" y="85" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">y'</text>
            <text x="45" y="160" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E293B">y</text>
            <text x="100" y="45" font-family="sans-serif" font-size="15" fill="#475569">-∞</text>
            <text x="210" y="45" font-family="sans-serif" font-size="15" fill="#1E293B" font-weight="bold">x₁</text>
            <text x="330" y="45" font-family="sans-serif" font-size="15" fill="#1E293B" font-weight="bold">x₂</text>
            <text x="440" y="45" font-family="sans-serif" font-size="15" fill="#475569">+∞</text>
            <text x="215" y="85" font-family="sans-serif" font-size="16" fill="#1E293B">0</text>
            <text x="335" y="85" font-family="sans-serif" font-size="16" fill="#1E293B">0</text>
            <text x="150" y="85" font-family="sans-serif" font-size="18" font-weight="bold" fill="#16A34A">+</text>
            <text x="270" y="85" font-family="sans-serif" font-size="20" font-weight="bold" fill="#DC2626">-</text>
            <text x="390" y="85" font-family="sans-serif" font-size="18" font-weight="bold" fill="#16A34A">+</text>
            <!-- Mũi tên đồng biến nghịch biến -->
            <line x1="110" y1="180" x2="200" y2="120" stroke="#2563EB" stroke-width="3" marker-end="url(#arrow)"/>
            <line x1="230" y1="120" x2="320" y2="180" stroke="#DC2626" stroke-width="3" marker-end="url(#arrow)"/>
            <line x1="350" y1="180" x2="440" y2="120" stroke="#2563EB" stroke-width="3" marker-end="url(#arrow)"/>
            <text x="205" y="115" font-family="sans-serif" font-size="14" fill="#1E3A8A" font-weight="bold">Cực đại</text>
            <text x="325" y="195" font-family="sans-serif" font-size="14" fill="#991B1B" font-weight="bold">Cực tiểu</text>
        </svg>
        """
    # 2. Hình ảnh: Cực trị hàm số (Đồ thị lồi lõm)
    elif "cực trị" in t_low:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/>
            <!-- Hệ trục Oxy -->
            <line x1="40" y1="190" x2="460" y2="190" stroke="#64748B" stroke-width="2"/>
            <line x1="70" y1="210" x2="70" y2="20" stroke="#64748B" stroke-width="2"/>
            <text x="465" y="195" font-family="sans-serif" font-size="14" fill="#334155">x</text>
            <text x="65" y="15" font-family="sans-serif" font-size="14" fill="#334155">y</text>
            <!-- Đồ thị hàm bậc 3 -->
            <path d="M 90 180 C 140 30, 200 40, 250 110 C 300 180, 360 190, 420 30" fill="none" stroke="#2563EB" stroke-width="3.5"/>
            <!-- Điểm cực đại -->
            <circle cx="170" cy="55" r="6" fill="#16A34A"/>
            <line x1="120" y1="55" x2="220" y2="55" stroke="#16A34A" stroke-width="2" stroke-dasharray="4"/>
            <text x="140" y="40" font-family="sans-serif" font-size="14" font-weight="bold" fill="#15803D">Điểm Cực Đại</text>
            <!-- Điểm cực tiểu -->
            <circle cx="330" cy="165" r="6" fill="#DC2626"/>
            <line x1="280" y1="165" x2="380" y2="165" stroke="#DC2626" stroke-width="2" stroke-dasharray="4"/>
            <text x="300" y="195" font-family="sans-serif" font-size="14" font-weight="bold" fill="#B91C1C">Điểm Cực Tiểu</text>
        </svg>
        """
    # 3. Hình ảnh: Đường tiệm cận
    elif "tiệm cận" in t_low:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/>
            <!-- Hệ trục -->
            <line x1="30" y1="150" x2="470" y2="150" stroke="#94A3B8" stroke-width="1.5"/>
            <line x1="160" y1="210" x2="160" y2="15" stroke="#94A3B8" stroke-width="1.5"/>
            <!-- Tiệm cận đứng x = x0 (đỏ) -->
            <line x1="230" y1="10" x2="230" y2="210" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="6"/>
            <text x="235" y="30" font-family="sans-serif" font-size="13" font-weight="bold" fill="#DC2626">TCĐ: x = x₀</text>
            <!-- Tiệm cận ngang y = y0 (xanh) -->
            <line x1="20" y1="80" x2="480" y2="80" stroke="#2563EB" stroke-width="2.5" stroke-dasharray="6"/>
            <text x="380" y="72" font-family="sans-serif" font-size="13" font-weight="bold" fill="#2563EB">TCN: y = y₀</text>
            <!-- 2 nhánh Hypebol -->
            <path d="M 50 72 Q 180 70 215 15" fill="none" stroke="#0F172A" stroke-width="3"/>
            <path d="M 245 205 Q 270 90 450 88" fill="none" stroke="#0F172A" stroke-width="3"/>
        </svg>
        """
    # 4. Hình ảnh: Đường tròn lượng giác (Khối 11)
    elif "lượng giác" in t_low or "sin" in t_low or "cos" in t_low:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/>
            <!-- Trục Cos ngang, Sin đứng -->
            <line x1="130" y1="110" x2="370" y2="110" stroke="#334155" stroke-width="2"/>
            <line x1="250" y1="210" x2="250" y2="10" stroke="#334155" stroke-width="2"/>
            <text x="375" y="115" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563EB">Trục Cos (+)</text>
            <text x="255" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#DC2626">Trục Sin (+)</text>
            <!-- Đường tròn đơn vị -->
            <circle cx="250" cy="110" r="80" fill="none" stroke="#0284C7" stroke-width="2.5"/>
            <!-- Góc alpha và điểm M -->
            <line x1="250" y1="110" x2="306" y2="54" stroke="#D97706" stroke-width="2.5"/>
            <circle cx="306" cy="54" r="5" fill="#D97706"/>
            <text x="315" y="55" font-family="sans-serif" font-size="13" font-weight="bold" fill="#B45309">M(cosα; sinα)</text>
            <!-- Nhãn 4 góc phần tư -->
            <text x="290" y="90" font-family="sans-serif" font-size="13" fill="#16A34A" font-weight="bold">Góc I (+,+)</text>
            <text x="160" y="90" font-family="sans-serif" font-size="13" fill="#64748B" font-weight="bold">Góc II (+,-)</text>
            <text x="160" y="145" font-family="sans-serif" font-size="13" fill="#64748B" font-weight="bold">Góc III (-,-)</text>
            <text x="290" y="145" font-family="sans-serif" font-size="13" fill="#64748B" font-weight="bold">Góc IV (-,+)</text>
        </svg>
        """
    # 5. Hình ảnh: Mệnh đề & Tập hợp (Biểu đồ Ven - Khối 10)
    elif "tập hợp" in t_low or "mệnh đề" in t_low:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#E2E8F0" stroke-width="2"/>
            <!-- Hai vòng tròn Ven -->
            <circle cx="200" cy="110" r="75" fill="#93C5FD" fill-opacity="0.5" stroke="#2563EB" stroke-width="2"/>
            <circle cx="300" cy="110" r="75" fill="#FCA5A5" fill-opacity="0.5" stroke="#DC2626" stroke-width="2"/>
            <text x="150" y="115" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1E40AF">Tập A</text>
            <text x="330" y="115" font-family="sans-serif" font-size="16" font-weight="bold" fill="#991B1B">Tập B</text>
            <text x="235" y="115" font-family="sans-serif" font-size="15" font-weight="bold" fill="#047857">A ∩ B</text>
            <text x="170" y="200" font-family="sans-serif" font-size="14" fill="#334155">Phần giao: phần tử thuộc cả A và B</text>
        </svg>
        """
    # 6. Mặc định: Hình minh họa bảng lý thuyết toán học tổng quát
    else:
        svg = """
        <svg viewBox="0 0 500 220" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
            <rect width="500" height="220" fill="#FFFFFF" rx="8" stroke="#CBD5E1" stroke-width="2"/>
            <rect x="25" y="25" width="450" height="170" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.5"/>
            <circle cx="80" cy="80" r="30" fill="#BFDBFE" stroke="#3B82F6" stroke-width="2"/>
            <line x1="80" y1="80" x2="160" y2="130" stroke="#3B82F6" stroke-width="3"/>
            <circle cx="160" cy="130" r="25" fill="#BBF7D0" stroke="#22C55E" stroke-width="2"/>
            <text x="230" y="85" font-family="sans-serif" font-size="17" font-weight="bold" fill="#1E293B">SƠ ĐỒ KIẾN THỨC CỐT LÕI</text>
            <text x="230" y="115" font-family="sans-serif" font-size="14" fill="#475569">Mô hình hóa trực quan phương pháp giải</text>
            <text x="230" y="145" font-family="sans-serif" font-size="14" font-weight="bold" fill="#2563EB">Bám sát cấu trúc SGK & Vở tự học</text>
        </svg>
        """
    st.markdown(f'<div class="img-box">{svg}</div>', unsafe_allow_html=True)

# ==============================================================================
# 4. KHO HỌC LIỆU SỐ BÁM SÁT VỞ TỰ HỌC: ĐỦ CHỦ ĐIỂM & VÍ DỤ MINH HỌA
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 12": {
        "Bài 1: Tính đơn điệu và cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị của hàm số",
            "topics": {
                "Chủ điểm 1: Tính đơn điệu của hàm số": {
                    "theory": """
- Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $K$:
  + Nếu $f'(x) > 0, \forall x \in K$ thì hàm số **đồng biến** trên $K$.
  + Nếu $f'(x) < 0, \forall x \in K$ thì hàm số **nghịch biến** trên $K$.
  + Nếu $f'(x) \ge 0$ (hoặc $\le 0$) trên $K$ và bằng $0$ tại hữu hạn điểm thì hàm số đồng biến (hoặc nghịch biến) trên $K$.
- **Quy trình xét tính đơn điệu:**
  1. Tìm tập xác định $D$.
  2. Tính đạo hàm $y' = f'(x)$, giải phương trình $y' = 0$ và tìm điểm $y'$ không xác định.
  3. Lập bảng xét dấu đạo hàm và kết luận các khoảng đơn điệu.
""",
                    "formula": r"f'(x) \ge 0, \forall x \in K \iff \text{Hàm số đồng biến trên } K; \quad f'(x) \le 0, \forall x \in K \iff \text{Hàm số nghịch biến trên } K",
                    "trap": "Khoảng đồng biến/nghịch biến phải viết rời nhau dùng từ 'và' hoặc dấu phẩy, tuyệt đối không dùng ký hiệu hợp (U).",
                    "audio": "Hàm số đồng biến khi đạo hàm lớn hơn hoặc bằng không, nghịch biến khi đạo hàm nhỏ hơn hoặc bằng không. Luôn kết luận trên từng khoảng riêng biệt.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm khoảng đơn điệu của hàm số bậc ba cơ bản",
                            "problem": "Xét tính đơn điệu và tìm các khoảng đồng biến, nghịch biến của hàm số: $$y = x^3 - 3x^2 + 2$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R}$.
- **Bước 2: Tính đạo hàm:**
  $$y' = 3x^2 - 6x = 3x(x - 2)$$
  Cho $y' = 0 \\iff 3x(x - 2) = 0 \\iff x = 0$ hoặc $x = 2$.
- **Bước 3: Xét dấu $y'$:**
  + Khoảng $(-\\infty; 0)$ và $(2; +\\infty)$: $y' > 0$ $\\Rightarrow$ Hàm số đồng biến.
  + Khoảng $(0; 2)$: $y' < 0$ $\\Rightarrow$ Hàm số nghịch biến.
- **Kết luận:** Hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên khoảng $(0; 2)$.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm khoảng đơn điệu của hàm phân thức bậc nhất trên bậc nhất",
                            "problem": "Tìm các khoảng đồng biến và nghịch biến của hàm số: $$y = \\frac{2x - 1}{x + 1}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R} \\setminus \\{-1\\}$.
- **Bước 2: Tính đạo hàm theo công thức nhanh $\\left(\\frac{ax+b}{cx+d}\\right)' = \\frac{ad - bc}{(cx+d)^2}$:**
  $$y' = \\frac{2 \\cdot 1 - (-1) \\cdot 1}{(x + 1)^2} = \\frac{3}{(x + 1)^2}$$
- **Bước 3: Kết luận:**
  Do $(x + 1)^2 > 0$ với mọi $x \\neq -1$ nên $y' > 0, \\forall x \\neq -1$.
  Vậy hàm số đồng biến trên từng khoảng xác định $(-\\infty; -1)$ và $(-1; +\\infty)$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm khoảng đơn điệu của hàm phân thức bậc hai trên bậc nhất",
                            "problem": "Tìm các khoảng đơn điệu của hàm số: $$y = \\frac{x^2 - 2x + 2}{x - 1}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R} \\setminus \\{1\\}$.
- **Bước 2: Tính đạo hàm:**
  $$y' = \\frac{(2x - 2)(x - 1) - (x^2 - 2x + 2) \\cdot 1}{(x - 1)^2} = \\frac{x^2 - 2x}{(x - 1)^2}$$
  Cho $y' = 0 \\iff x^2 - 2x = 0 \\iff x = 0$ hoặc $x = 2$ (thỏa mãn $x \\neq 1$).
- **Bước 3: Kết luận:**
  Hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên các khoảng $(0; 1)$ và $(1; 2)$.
"""
                        }
                    ],
                    "exercise": {
                        "id": "12_B1_CD1",
                        "title": "Bài tập kiểm minh chứng: Đơn điệu hàm số",
                        "content": "Hàm số y = x^3 - 3x nghịch biến trên khoảng (-1; b). Giá trị của b bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "1", "options": []
                    }
                },
                "Chủ điểm 2: Cực trị của hàm số": {
                    "theory": """
- **Định nghĩa:** $x_0$ là điểm cực đại nếu $f(x) < f(x_0)$ với mọi $x$ lân cận khác $x_0$. $x_0$ là điểm cực tiểu nếu $f(x) > f(x_0)$.
- **Dấu hiệu 1:** Qua điểm $x_0$:
  + Đạo hàm $f'(x)$ đổi dấu từ $(+)$ sang $(-)$ thì $x_0$ là **điểm cực đại**.
  + Đạo hàm $f'(x)$ đổi dấu từ $(-)$ sang $(+)$ thì $x_0$ là **điểm cực tiểu**.
- **Quy tắc phân biệt:**
  + *Điểm cực trị của hàm số:* $x_0$.
  + *Giá trị cực trị:* $y_0 = f(x_0)$.
  + *Điểm cực trị của đồ thị:* Cặp tọa độ $M(x_0; y_0)$.
""",
                    "formula": r"f'(x_0) = 0 \text{ hoặc không xác định}; \quad (+) \xrightarrow{x_0} (-) \implies \text{Cực đại}; \quad (-) \xrightarrow{x_0} (+) \implies \text{Cực tiểu}",
                    "trap": "Học sinh thường nhầm lẫn giữa hoành độ x (điểm cực trị của hàm số) và tung độ y (giá trị cực trị).",
                    "audio": "Điểm cực trị là giá trị x0, giá trị cực trị là tung độ y0, còn điểm cực trị của đồ thị là cặp tọa độ M(x0; y0). Nhớ đọc kỹ câu hỏi đề bài.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm cực trị của hàm số bậc ba",
                            "problem": "Tìm các điểm cực trị và giá trị cực trị tương ứng của hàm số: $$y = x^3 - 3x^2 + 2$$",
                            "solution": """
- **Bước 1: Đạo hàm:** $y' = 3x^2 - 6x = 3x(x - 2) = 0 \\iff x = 0$ hoặc $x = 2$.
- **Bước 2: Xét dấu đạo hàm:**
  + Qua $x = 0$, $y'$ đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow x = 0$ là điểm cực đại; giá trị cực đại $y_{CĐ} = f(0) = 2$.
  + Qua $x = 2$, $y'$ đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow x = 2$ là điểm cực tiểu; giá trị cực tiểu $y_{CT} = f(2) = -2$.
- **Kết luận:** Hàm số đạt cực đại tại $x = 0$ với $y_{CĐ} = 2$; đạt cực tiểu tại $x = 2$ với $y_{CT} = -2$.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm tọa độ điểm cực trị của đồ thị hàm trùng phương",
                            "problem": "Tìm tọa độ các điểm cực trị của đồ thị hàm số: $$y = -x^4 + 2x^2 + 3$$",
                            "solution": """
- **Bước 1: Đạo hàm:**
  $$y' = -4x^3 + 4x = -4x(x^2 - 1) = 0 \\iff x = 0, x = 1, x = -1$$
- **Bước 2: Tính giá trị tung độ tương ứng:**
  + Tại $x = 0$: $y = 3$. Đạo hàm đổi dấu $(-)$ sang $(+)$ $\\Rightarrow (0; 3)$ là điểm cực tiểu của đồ thị.
  + Tại $x = 1$: $y = 4$. Đạo hàm đổi dấu $(+)$ sang $(-)$ $\\Rightarrow (1; 4)$ là điểm cực đại của đồ thị.
  + Tại $x = -1$: $y = 4$. Đạo hàm đổi dấu $(+)$ sang $(-)$ $\\Rightarrow (-1; 4)$ là điểm cực đại của đồ thị.
- **Kết luận:** Đồ thị có hai điểm cực đại là $A(1; 4), B(-1; 4)$ và một điểm cực tiểu là $C(0; 3)$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm cực trị của hàm phân thức bậc hai trên bậc nhất",
                            "problem": "Tìm các điểm cực trị của hàm số: $$y = \\frac{x^2 + 3}{x - 1}$$",
                            "solution": """
- **Bước 1:** Tập xác định $D = \\mathbb{R} \\setminus \\{1\\}$.
- **Bước 2: Đạo hàm:**
  $$y' = \\frac{2x(x - 1) - (x^2 + 3)}{(x - 1)^2} = \\frac{x^2 - 2x - 3}{(x - 1)^2}$$
  Cho $y' = 0 \\iff x^2 - 2x - 3 = 0 \\iff x = -1$ hoặc $x = 3$.
- **Bước 3: Kết luận:**
  + Điểm cực đại là $x = -1$ với giá trị cực đại $y_{CĐ} = -2$.
  + Điểm cực tiểu là $x = 3$ với giá trị cực tiểu $y_{CT} = 6$.
"""
                        }
                    ],
                    "exercise": {
                        "id": "12_B1_CD2",
                        "title": "Bài tập kiểm minh chứng: Giá trị cực tiểu",
                        "content": "Giá trị cực tiểu (yCT) của hàm số y = x^3 - 3x + 2 bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "0", "options": []
                    }
                }
            }
        },
        "Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị của hàm số",
            "topics": {
                "Chủ điểm 1: Tìm GTLN và GTNN trên đoạn [a; b]": {
                    "theory": """
- Mọi hàm số liên tục trên đoạn $[a; b]$ đều có giá trị lớn nhất và giá trị nhỏ nhất trên đoạn đó.
- **Quy trình tính nhanh không cần lập bảng biến thiên:**
  1. Tính đạo hàm $f'(x)$.
  2. Tìm các nghiệm $x_i \in (a; b)$ của phương trình $f'(x) = 0$ (loại các nghiệm nằm ngoài khoảng).
  3. Tính $f(a), f(b), f(x_i)$.
  4. Số lớn nhất trong các giá trị tính được là GTLN, số nhỏ nhất là GTNN.
""",
                    "formula": r"\max_{[a; b]} f(x) = \max\{f(a), f(b), f(x_i)\}; \quad \min_{[a; b]} f(x) = \min\{f(a), f(b), f(x_i)\}",
                    "trap": "Chỉ lấy các nghiệm nằm hẳn BÊN TRONG khoảng (a; b). Nghiệm nằm ngoài đoạn bắt buộc phải loại bỏ.",
                    "audio": "Trên một đoạn số thực, tính giá trị tại hai đầu mút và tại các điểm đạo hàm bằng không thuộc khoảng rồi so sánh.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm GTLN, GTNN của hàm bậc ba trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số: $$f(x) = x^3 - 3x + 1 \\quad \\text{trên đoạn } [0; 2]$$",
                            "solution": """
- **Bước 1: Đạo hàm:** $f'(x) = 3x^2 - 3 = 0 \\iff x = 1 \\in (0; 2)$ hoặc $x = -1 \\notin (0; 2)$ (loại).
- **Bước 2: Tính giá trị:** $f(0) = 1$; $f(1) = -1$; $f(2) = 3$.
- **Kết luận:** $\\max_{[0; 2]} f(x) = f(2) = 3$ và $\\min_{[0; 2]} f(x) = f(1) = -1$.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm GTLN, GTNN của hàm phân thức trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và nhỏ nhất của hàm số: $$y = \\frac{x - 2}{x + 1} \\quad \\text{trên đoạn } [0; 3]$$",
                            "solution": """
- Hàm số xác định trên $[0; 3]$. Đạo hàm $y' = \\frac{3}{(x + 1)^2} > 0, \\forall x \\in [0; 3]$.
- Hàm số đồng biến liên tục trên $[0; 3]$.
- Kết luận: $\\min_{[0; 3]} y = y(0) = -2$; $\\max_{[0; 3]} y = y(3) = \\frac{1}{4}$.
"""
                        }
                    ],
                    "exercise": {
                        "id": "12_B2_CD1",
                        "title": "Bài tập kiểm minh chứng: GTLN trên đoạn",
                        "content": "Giá trị lớn nhất của hàm số f(x) = x^3 - 3x + 1 trên đoạn [0; 2] bằng:",
                        "type": "NUMERIC", "target": "3", "options": []
                    }
                }
            }
        },
        "Bài 3: Đường tiệm cận của đồ thị hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị của hàm số",
            "topics": {
                "Chủ điểm 1: Tiệm cận đứng và Tiệm cận ngang": {
                    "theory": """
- **Tiệm cận đứng:** $x = x_0$ nếu ít nhất một trong các giới hạn một bên khi $x \to x_0$ bằng $\pm\infty$.
- **Tiệm cận ngang:** $y = y_0$ nếu $\lim_{x \to +\infty} y = y_0$ hoặc $\lim_{x \to -\infty} y = y_0$.
- **Hàm nhất biến $y = \frac{ax+b}{cx+d}$:** Có TCĐ $x = -\frac{d}{c}$ và TCN $y = \frac{a}{c}$.
""",
                    "formula": r"\lim_{x \to x_0} y = \pm\infty \implies x = x_0 \ (\text{TCĐ}); \quad \lim_{x \to \pm\infty} y = y_0 \implies y = y_0 \ (\text{TCN})",
                    "trap": "Tránh nhầm lẫn biến: Tiệm cận đứng là x = số, tiệm cận ngang là y = số.",
                    "audio": "Mẫu số triệt tiêu mà tử số khác không cho ta tiệm cận đứng x. Giới hạn tại vô cực cho ta tiệm cận ngang y.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm tiệm cận của hàm nhất biến cơ bản",
                            "problem": "Tìm các đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số: $$y = \\frac{2x - 3}{x + 1}$$",
                            "solution": """
- Mẫu số $x + 1 = 0 \\iff x = -1$. Ta có $\\lim_{x \\to -1^+} y = -\\infty \\implies x = -1$ là tiệm cận đứng.
- Ta có $\\lim_{x \\to \\pm\\infty} y = 2 \\implies y = 2$ là tiệm cận ngang.
"""
                        },
                        {
                            "title": "Ví dụ 2: Nhận biết đường tiệm cận khi mẫu có nghiệm triệt tiêu tử",
                            "problem": "Tìm số đường tiệm cận đứng của đồ thị hàm số: $$y = \\frac{x - 1}{x^2 - 1}$$",
                            "solution": """
- Rút gọn với $x \\neq 1$: $y = \\frac{1}{x + 1}$.
- Tại $x = 1$: $\\lim_{x \\to 1} y = \\frac{1}{2}$ (hữu hạn nên $x = 1$ không phải TCĐ).
- Tại $x = -1$: $\\lim_{x \\to -1^+} y = +\\infty \\implies x = -1$ là tiệm cận đứng duy nhất.
"""
                        }
                    ],
                    "exercise": {
                        "id": "12_B3_CD1",
                        "title": "Bài tập kiểm minh chứng: Tiệm cận ngang",
                        "content": "Đường tiệm cận ngang của đồ thị hàm số y = (2x - 3)/(x + 1) có phương trình y bằng:",
                        "type": "NUMERIC", "target": "2", "options": []
                    }
                }
            }
        }
    },
    "Khối 10": {
        "Bài 1: Mệnh đề toán học": {
            "chapter": "Chương I: Mệnh đề và tập hợp",
            "topics": {
                "Chủ điểm 1: Khái niệm mệnh đề và mệnh đề chứa biến": {
                    "theory": "Mệnh đề toán học là khẳng định đúng hoặc sai, không thể vừa đúng vừa sai. Câu cảm thán, câu hỏi không phải mệnh đề.",
                    "formula": r"P \in \{\text{Đúng}, \text{Sai}\}",
                    "trap": "Mệnh đề chứa biến chưa gán giá trị cụ thể thì chưa xác định tính đúng sai.",
                    "audio": "Mệnh đề toán học là câu khẳng định chỉ nhận một trong hai chân giá trị: Đúng hoặc Sai.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Nhận diện mệnh đề toán học",
                            "problem": "Trong các câu sau, câu nào là mệnh đề toán học: a) 15 là số nguyên tố; b) Số 0 là số tự nhiên nhỏ nhất?",
                            "solution": "Cả hai câu a và b đều là khẳng định: câu a là mệnh đề toán học Sai, câu b là mệnh đề toán học Đúng."
                        },
                        {
                            "title": "Ví dụ 2: Mệnh đề chứa biến",
                            "problem": "Cho mệnh đề chứa biến P(n): 'n chia hết cho 3'. Tìm giá trị n để được mệnh đề đúng và sai.",
                            "solution": "Với n = 6: P(6) là mệnh đề đúng. Với n = 5: P(5) là mệnh đề sai."
                        }
                    ],
                    "exercise": {
                        "id": "10_B1_CD1",
                        "title": "Bài tập kiểm minh chứng: Mệnh đề toán học",
                        "content": "Trong các câu: (1) 2 + 3 = 5; (2) Số pi là số hữu tỉ; (3) Bạn học bài chưa? Có bao nhiêu câu là mệnh đề toán học?",
                        "type": "NUMERIC", "target": "2", "options": []
                    }
                },
                "Chủ điểm 2: Mệnh đề phủ định và Lượng từ với mọi, tồn tại": {
                    "theory": "Phủ định của mệnh đề chứa lượng từ 'với mọi' là 'tồn tại'. Phủ định của dấu lớn hơn (>) là dấu nhỏ hơn hoặc bằng (<=).",
                    "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
                    "trap": "Không được bỏ quên dấu bằng khi phủ định bất đẳng thức.",
                    "audio": "Phủ định của với mọi là tồn tại, phủ định của lớn hơn là nhỏ hơn hoặc bằng.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Phủ định mệnh đề lượng từ với mọi",
                            "problem": "Lập mệnh đề phủ định của P: 'Mọi số thực x đều có x^2 + 1 > 0'.",
                            "solution": "Phủ định của 'với mọi' là 'tồn tại', phủ định của '>' là '<='. Vậy P ngang: 'Tồn tại số thực x sao cho x^2 + 1 <= 0'."
                        }
                    ],
                    "exercise": {
                        "id": "10_B1_CD2",
                        "title": "Bài tập kiểm minh chứng: Phủ định lượng từ",
                        "content": "Phủ định của mệnh đề 'Mọi số nguyên x đều có x^2 >= 0' là: A. Tồn tại x có x^2 < 0; B. Tồn tại x có x^2 <= 0; C. Mọi x có x^2 < 0.",
                        "type": "CHOICE", "target": "A", "options": ["A. Tồn tại x có x^2 < 0", "B. Tồn tại x có x^2 <= 0", "C. Mọi x có x^2 < 0"]
                    }
                }
            }
        }
    },
    "Khối 11": {
        "Bài 1: Giá trị lượng giác của góc lượng giác": {
            "chapter": "Chương I: Hàm số và phương trình lượng giác",
            "topics": {
                "Chủ điểm 1: Dấu của các giá trị lượng giác theo góc phần tư": {
                    "theory": "Trục tung là sin, trục hoành là cos. Góc phần tư thứ II có sin > 0, cos < 0, tan < 0.",
                    "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
                    "trap": "Khai căn tìm cos từ sin bắt buộc phải dựa vào góc phần tư để chọn dấu âm hoặc dương.",
                    "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Luôn kiểm tra kỹ góc phần tư khi khai căn.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính cos khi biết sin ở góc phần tư thứ II",
                            "problem": "Cho góc alpha thỏa mãn pi/2 < alpha < pi và sin alpha = 3/5. Hãy tính cos alpha.",
                            "solution": "Ta có cos^2 alpha = 1 - sin^2 alpha = 1 - 9/25 = 16/25. Vì góc alpha thuộc góc phần tư thứ II nên cos alpha < 0. Do đó cos alpha = -4/5 = -0.8."
                        }
                    ],
                    "exercise": {
                        "id": "11_B1_CD1",
                        "title": "Bài tập kiểm minh chứng: Giá trị cos",
                        "content": "Cho góc alpha thuộc góc phần tư thứ II và sin alpha = 3/5. Giá trị của cos alpha bằng bao nhiêu (điền số thập phân)?",
                        "type": "NUMERIC", "target": "-0.8", "options": []
                    }
                }
            }
        }
    }
}

# ==============================================================================
# 5. KHO ĐỀ KHẢO THÍ CHUẨN MA TRẬN MỚI CỦA BỘ GD&ĐT
# ==============================================================================
EXAM_BANK = {
    "Khối 10": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 10",
            "p1": [{"q": r"Mệnh đề nào sau đây là mệnh đề toán học?", "ops": ["A. $2 + 3 = 6$", "B. Thời tiết hôm nay mát quá!", "C. Bạn học bài chưa?", "D. Hãy giải phương trình."], "ans": "A", "exp": "A là khẳng định sai, là mệnh đề toán học."}],
            "p2": [{"q": r"Cho tam thức $f(x) = x^2 - 4x + 3$. Xét tính Đúng/Sai:", "items": [("a) Phương trình có 2 nghiệm phân biệt x=1 và x=3.", True, "Delta'>0."), ("b) f(x) < 0 với x thuộc (1; 3).", True, "Trong trái ngoài cùng."), ("c) Đỉnh parabol là I(2; 1).", False, "Đỉnh đúng là I(2; -1)."), ("d) f(0) = 3.", True, "Thay x=0.")]}],
            "p3": [{"q": r"Cho tam giác ABC có b=8, c=5, góc A=60 độ. Cạnh a bằng bao nhiêu?", "ans": "7", "alt": ["7.0"], "exp": "a^2 = 64 + 25 - 40 = 49 => a = 7."}]
        }
    },
    "Khối 11": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 11",
            "p1": [{"q": r"Tập xác định của hàm số $y = \tan x$ là:", "ops": [r"A. $D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi\}$", r"B. $D = \mathbb{R} \setminus \{k\pi\}$", r"C. $D = \mathbb{R}$", r"D. $D = [-1; 1]$"], "ans": "A", "exp": "cos x khác 0."}],
            "p2": [{"q": r"Cho cấp số cộng (un) có u1 = 2, d = 3. Xét tính Đúng/Sai:", "items": [("a) u2 = 5.", True, "2+3=5."), ("b) Số hạng tổng quát un = 3n - 1.", True, "2 + 3(n-1)."), ("c) Số 20 là một số hạng của dãy.", True, "3n-1=20 => n=7."), ("d) Tổng 10 số hạng đầu S10 = 155.", True, "10*(4+27)/2 = 155.")]}],
            "p3": [{"q": r"Rạp hát có 12 hàng ghế. Hàng 1 có 15 ghế, mỗi hàng sau hơn 2 ghế. Tổng số ghế:", "ans": "312", "alt": ["312 ghế"], "exp": "S_12 = 12*(30 + 22)/2 = 312."}]
        }
    },
    "Khối 12": {
        "🏛️ Ôn thi Tốt nghiệp THPT (Cấu trúc mới)": {
            "title": "ĐỀ THI TỐT NGHIỆP THPT CHUẨN MA TRẬN KHẢO THÍ MỚI",
            "p1": [{"q": r"Cho hàm số có đạo hàm $f'(x) = x(x-1)^2 (x+2)^3$. Số điểm cực trị là:", "ops": ["A. 2", "B. 3", "C. 1", "D. 0"], "ans": "A", "exp": "Nghiệm bội lẻ x = 0 và x = -2."}],
            "p2": [{"q": r"Cho hình chóp đều S.ABC có đáy cạnh a, cạnh bên tạo đáy góc 60 độ. Xét tính Đúng/Sai:", "items": [("a) Hình chiếu của S là trọng tâm đáy.", True, "Chóp đều."), ("b) Độ dài đường cao bằng a.", True, "h = (a căn 3 / 3)*tan 60 = a."), ("c) Thể tích bằng a^3 / 4.", False, "a^3 căn 3 / 12."), ("d) Bán kính mặt cầu ngoại tiếp bằng 2a/3.", True, "R = 2a/3.")]}],
            "p3": [{"q": r"Làm hộp không nắp đáy vuông thể tích 32 dm3. Diện tích vật liệu nhỏ nhất (dm2):", "ans": "48", "alt": ["48 dm2"], "exp": "S(x) = x^2 + 128/x. Min tại x=4, S=48."}]
        }
    }
}

# ==============================================================================
# 6. QUẢN LÝ TÀI KHOẢN & GAMIFICATION
# ==============================================================================
DEFAULT_STUDENTS = [
    {"student_id": "HS12_01", "password": "123", "full_name": "Nguyễn Hoàng Nam", "grade": 12, "current_level": "Khá", "weak_spots": "Dấu đạo hàm, Tọa độ Oxyz", "flowers": 30, "total_solved": 6},
    {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "current_level": "Khá", "weak_spots": "Dấu lượng giác, Hình không gian", "flowers": 30, "total_solved": 5},
    {"student_id": "HS10_01", "password": "123", "full_name": "Lê Bảo Ngọc", "grade": 10, "current_level": "Giỏi", "weak_spots": "Phủ định mệnh đề", "flowers": 35, "total_solved": 8}
]

if "auth_user" not in st.session_state:
    st.session_state["auth_user"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None
if "students_db" not in st.session_state:
    st.session_state["students_db"] = DEFAULT_STUDENTS
if "inbox_db" not in st.session_state:
    st.session_state["inbox_db"] = []

def load_all_students():
    if conn is not None:
        try:
            df = conn.read(worksheet="STUDENT_PROFILES")
            if not df.empty and "student_id" in df.columns:
                records = df.to_dict(orient="records")
                for r in records:
                    if "password" not in r or str(r["password"]) == "nan":
                        r["password"] = "123"
                st.session_state["students_db"] = records
                return records
        except Exception:
            pass
    return st.session_state["students_db"]

def reward_student_flower(student_id, earned, reason):
    for s in st.session_state["students_db"]:
        if s["student_id"] == student_id:
            s["flowers"] = int(s.get("flowers", 30)) + earned
            st.toast(f"🌸 Tuyệt vời! Em nhận được +{earned} Bông hoa vì: {reason}!")
            if st.session_state["auth_user"] and st.session_state["auth_user"]["student_id"] == student_id:
                st.session_state["auth_user"]["flowers"] = s["flowers"]
            if conn is not None:
                try:
                    df = pd.DataFrame(st.session_state["students_db"])
                    conn.write(worksheet="STUDENT_PROFILES", data=df)
                except Exception:
                    pass
            break

# ==============================================================================
# 7. MÀN HÌNH ĐĂNG NHẬP & PHÂN QUYỀN
# ==============================================================================
if st.session_state["auth_user"] is None:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📐 HỆ SINH THÁI TỰ HỌC TOÁN THPT 'GSTOÁN'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>Chuẩn hóa từng Chủ điểm bám sát Vở tự học Kết nối tri thức (Khối 10, 11, 12)</p>", unsafe_allow_html=True)

    col_l1, col_box, col_l2 = st.columns([1, 1.2, 1])
    with col_box:
        with st.container(border=True):
            st.markdown("### 🔐 Cổng Đăng Nhập")
            login_role = st.radio("Vai trò của bạn:", ["👨‍🎓 Học sinh", "👩‍🏫 Giáo viên (Admin)"], horizontal=True)
            user_input = st.text_input("Tài khoản / Mã học sinh:", placeholder="Ví dụ: HS12_01 hoặc admin")
            pass_input = st.text_input("Mật khẩu:", type="password", placeholder="Nhập mật khẩu...")

            if st.button("Đăng Nhập Ngay", use_container_width=True):
                if login_role == "👩‍🏫 Giáo viên (Admin)":
                    if user_input.strip().lower() == "admin" and (pass_input == "gstoan2026" or pass_input == "123"):
                        st.session_state["auth_user"] = {"full_name": "Thầy/Cô Bộ Môn Toán", "role": "teacher"}
                        st.session_state["role"] = "teacher"
                        st.success("Đăng nhập Giáo viên thành công!")
                        st.rerun()
                    else:
                        st.error("Sai thông tin đăng nhập! Mặc định: `admin` / `gstoan2026` hoặc `123`")
                else:
                    all_st = load_all_students()
                    found = next((s for s in all_st if s["student_id"].upper() == user_input.strip().upper()), None)
                    if found:
                        if str(found.get("password", "123")) == pass_input.strip():
                            st.session_state["auth_user"] = found
                            st.session_state["role"] = "student"
                            st.success(f"Chào mừng em {found['full_name']}!")
                            st.rerun()
                        else:
                            st.error("Mật khẩu chưa chính xác!")
                    else:
                        st.error("Không tìm thấy mã học sinh này trong danh sách!")
            st.caption("💡 Tài khoản: `HS12_01`, `HS11_01`, `HS10_01` (Pass: `123`). Admin: `admin` / `gstoan2026`.")
    st.stop()

# ==============================================================================
# 8. THANH ĐIỀU HƯỚNG BÊN HÔNG (SIDEBAR)
# ==============================================================================
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state['auth_user']['full_name']}")
    if st.session_state["role"] == "student":
        st.caption(f"Mã định danh: **{st.session_state['auth_user']['student_id']}**")
        flowers = st.session_state['auth_user'].get('flowers', 30)
        with st.container(border=True):
            st.markdown("<h5 style='text-align: center; color: #DB2777; margin:0;'>🌸 Vườn hoa Tri thức</h5>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #BE185D; margin:4px 0;'>{flowers} 🌸</h2>", unsafe_allow_html=True)
            st.caption("Giải đúng bài tập nhận +2 hoa. Nghe bài giảng +1 hoa. Khảo thí nhận tới +3 hoa!")
    else:
        st.info("Vai trò: **Cố Vấn Sư Phạm & Quản Trị**")

    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.session_state["role"] = None
        st.rerun()
    st.markdown("---")

# ==============================================================================
# 9. PHÂN HỆ HỌC SINH (5 TABS: HÌNH ẢNH SGK THAY THẾ VIDEO)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN 3 BẬC: KHỐI -> BÀI HỌC -> CHỦ ĐIỂM KIẾN THỨC
c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])
with c_gr:
    user_grade_default = 2 if student_info.get("grade") == 12 else (0 if student_info.get("grade") == 10 else 1)
    sel_grade = st.selectbox("📚 Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

with c_les:
    lesson_list = list(CURRICULUM_DATA[sel_grade].keys())
    sel_lesson = st.selectbox("📖 Bài học SGK:", lesson_list)

cur_lesson_obj = CURRICULUM_DATA[sel_grade][sel_lesson]

with c_top:
    topic_list = list(cur_lesson_obj["topics"].keys())
    sel_topic = st.selectbox("🎯 Danh sách Chủ điểm (Vở tự học):", topic_list)

cur_topic_data = cur_lesson_obj["topics"][sel_topic]

# 5 TABS TOÀN DIỆN
tab1, tab_ex, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Hình Ảnh SGK & Audio)",
    "💡 Ví Dụ Minh Họa (Bấm Xem Lời Giải)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC (HÌNH ẢNH MINH HỌA SGK + AUDIO PHÍA DƯỚI)
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {cur_lesson_obj['chapter']}")
    st.markdown(f"#### {sel_lesson} — *{sel_topic}*")

    col_img, col_n = st.columns([1.2, 1.1])
    
    with col_img:
        with st.container(border=True):
            st.markdown(f"🖼️ **Hình ảnh minh họa kiến thức (Trích SGK & Vở tự học):**")
            # Hiển thị hình ảnh minh họa vector chuẩn SGK thay thế video
            render_sgk_illustration_svg(sel_topic, sel_lesson)
            
            # TRÌNH PHÁT ÂM THANH BÀI GIẢNG ĐẶT NGAY DƯỚI HÌNH ẢNH
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Bài Giảng Vi Mô (Trích Vở tự học):</b><br>
                <small>Nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5((sel_lesson + sel_topic).encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_topic_data["audio"], audio_hash)
            if lecture_audio_file:
                st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã nghe xong bài giảng vi mô (+1 hoa)", key=f"btn_audio_{sel_topic}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ nghe bài giảng vi mô")
                
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes)**")
            st.markdown(f"#### 1. Khái niệm & Định lý cốt lõi\n{cur_topic_data['theory']}")
            st.markdown("#### 2. Công thức Toán học trọng tâm")
            st.markdown(f"$${cur_topic_data['formula']}$$")
            st.markdown(f"#### 3. Cảnh báo bẫy đề thi\n- ⚠️ **Lưu ý:** {cur_topic_data['trap']}")

# ------------------------------------------------------------------------------
# TAB 2: VÍ DỤ MINH HỌA (TRÌNH BÀY ĐỀ BÀI -> BẤM XEM LỜI GIẢI CHI TIẾT)
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Ví Dụ Minh Họa Chuẩn Mực: {sel_topic}")
    st.caption("Các ví dụ cơ bản/trọng tâm từ Vở tự học (đã loại bỏ bài chứa tham số m và vận dụng cao). Bấm vào từng đề bài để xem lời giải chi tiết và học cách trình bày.")

    examples_list = cur_topic_data.get("examples", [])
    if not examples_list:
        st.info("Chủ điểm này đang được cập nhật thêm các ví dụ tiếp theo.")
    else:
        for idx, ex_item in enumerate(examples_list):
            with st.expander(f"📌 {ex_item['title']}", expanded=(idx == 0)):
                st.markdown(f"**Đề bài yêu cầu:**\n\n{ex_item['problem']}")
                st.markdown("---")
                st.markdown("**✍️ Lời giải chi tiết chuẩn mực sư phạm:**")
                st.markdown(ex_item["solution"])

# ------------------------------------------------------------------------------
# TAB 3: HỌC SINH TỰ GIẢI - KIỂM MINH CHỨNG MỚI ĐƯỢC THƯỞNG HOA
# ------------------------------------------------------------------------------
with tab2:
    ex = cur_topic_data["exercise"]
    with st.container(border=True):
        st.subheader(f"📝 {ex['title']}")
        st.markdown(f"**Đề bài:** {ex['content']}")

        st.markdown("---")
        st.markdown("#### ✍️ Kiểm Minh Chứng: Em hãy tự làm ra nháp và điền kết quả")
        st.caption("Hệ thống chỉ thưởng +2 🌸 Bông hoa Tri thức khi em thực sự giải chính xác!")

        user_submitted_ans = None
        if ex.get("type") == "CHOICE":
            user_submitted_ans = st.radio("Chọn phương án đúng của em:", ex["options"], key=f"choice_ex_{ex['id']}")
        else:
            user_submitted_ans = st.text_input("Nhập kết quả/đáp số của em (ví dụ: 1 hoặc 0 hoặc -0.8):", key=f"num_ex_{ex['id']}")

        c_chk, c_sim = st.columns([1, 1.2])
        with c_chk:
            if st.button("🚀 Nộp Bài Giải Để Kiểm Tra Minh Chứng", key=f"btn_check_{ex['id']}", use_container_width=True):
                is_correct = False
                if ex.get("type") == "CHOICE":
                    if user_submitted_ans.startswith(ex["target"]):
                        is_correct = True
                else:
                    clean_u = user_submitted_ans.strip().replace(",", ".")
                    clean_t = ex["target"].strip().replace(",", ".")
                    if clean_u == clean_t:
                        is_correct = True
                    else:
                        try:
                            val_u = float(clean_u.split("/")[0]) / float(clean_u.split("/")[1]) if "/" in clean_u else float(clean_u)
                            val_t = float(clean_t.split("/")[0]) / float(clean_t.split("/")[1]) if "/" in clean_t else float(clean_t)
                            if abs(val_u - val_t) < 0.05:
                                is_correct = True
                        except Exception:
                            pass

                if is_correct:
                    st.balloons()
                    st.success("🎉 CHÍNH XÁC 100%! Em đã tự giải đúng bài tập và xứng đáng nhận thưởng +2 Bông hoa Tri thức!")
                    reward_student_flower(student_info["student_id"], 2, "tự lực giải đúng bài tập Vở tự học có minh chứng")
                else:
                    st.error("❌ Kết quả chưa chính xác! Em hãy xem lại Ví dụ minh họa và thử giải lại ra nháp nhé. Hệ thống không cộng hoa cho kết quả sai.")

        with c_sim:
            if st.button("🔄 AI Tạo 01 Bài Tương Tự Để Luyện Thêm", key=f"btn_sim_{ex['id']}", use_container_width=True):
                with st.spinner("AI đang tạo bài tương tự cùng dạng..."):
                    if client:
                        try:
                            prompt_sim = f"Bạn là giáo viên Toán. Từ bài tập: '{ex['content']}', hãy tạo 1 bài toán TƯƠNG TỰ CÙNG DẠNG (đổi số liệu, tuyệt đối không chứa tham số m, không vận dụng cao). Chỉ đưa đề bài và đáp số cuối cùng trong dấu ngoặc vuông."
                            res_sim = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_sim)
                            sim_t = res_sim.text
                        except Exception:
                            sim_t = "Bài toán tương tự cùng dạng bám sát Vở tự học."
                    else:
                        sim_t = "Bài toán tương tự cùng dạng bám sát Vở tự học Kết nối tri thức."
                    st.info(f"**Bài toán tương tự rèn luyện:**\n\n{sim_t}")

        st.markdown("---")
        with st.expander("❓ Vẫn chưa hiểu bài sau khi giải và xem gợi ý? Gửi câu hỏi lên Thầy/Cô"):
            st.caption("Nếu gặp điểm nghẽn nhận thức, em gửi câu hỏi lên lớp để Thầy/Cô giải đáp trực tiếp:")
            s_note = st.text_input("Ghi rõ vị trí em bị nghẽn:", key=f"note_inbox_{ex['id']}")
            if st.button("📩 [Gửi câu hỏi bế tắc này về Thầy/Cô]", key=f"btn_send_{ex['id']}"):
                item_inbox = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "student_id": student_info["student_id"],
                    "student_name": student_info["full_name"],
                    "lesson_id": f"{sel_lesson} - {sel_topic}",
                    "exercise_id": ex["id"],
                    "student_note": s_note
                }
                st.session_state["inbox_db"].append(item_inbox)
                st.success("✅ Đã gửi câu hỏi về Hộp thư Giáo viên! Thầy/Cô sẽ hỗ trợ giải đáp trực tiếp cho em trên lớp.")
                total_q = len([q for q in st.session_state["inbox_db"] if q["student_id"] == student_info["student_id"]])
                if total_q % 2 == 0:
                    reward_student_flower(student_info["student_id"], 1, "gửi đủ 2 câu hỏi bế tắc nghiêm túc cho Thầy/Cô")

# ------------------------------------------------------------------------------
# TAB 4: TRỢ LÝ AI: SOI BÀI VỞ & TỐI ƯU ÂM THANH MIC/LOA
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("💬 Gia Sư AI: Soi Bài Viết Tay & Lời Khuyên Giọng Nói")
    st.caption(f"Trợ lý AI đang sẵn sàng hỗ trợ nội dung: {sel_topic}")

    inp_mode = st.radio("Phương thức hỏi:", ["📸 Chụp vở nháp qua Camera", "🎙️ Hỏi qua Mic", "✍️ Nhập văn bản"], horizontal=True)

    img_cam = None
    aud_mic = None
    txt_q = ""

    if inp_mode == "📸 Chụp vở nháp qua Camera":
        cam_in = st.camera_input("Chụp trang vở nháp bài làm của em:")
        if cam_in:
            img_cam = Image.open(cam_in)
            img_cam.thumbnail((1024, 1024))
    elif inp_mode == "🎙️ Hỏi qua Mic":
        aud_in = st.audio_input("Nói trực tiếp thắc mắc của em:")
        if aud_in:
            aud_mic = aud_in.read()
    else:
        txt_q = st.text_area("Nhập thắc mắc của em:")

    if st.button("🚀 Gửi Bài Nhờ Gia Sư AI Kiểm Tra", key="btn_ask_ai"):
        with st.spinner("AI đang phân tích và tìm điểm nghẽn..."):
            prompt_pedagogy = f"""
            Bạn là Gia sư dạy Toán THPT bám sát Vở tự học Kết nối tri thức.
            Bài học: {sel_lesson} | Chủ điểm: {sel_topic} ({sel_grade}).
            Học sinh: {student_info['full_name']} (Lỗ hổng: {student_info.get('weak_spots')}).

            QUY TẮC PHẢN HỒI BẮT BUỘC:
            1. KHÔNG giải hộ trọn gói. Chỉ ra bước làm đúng, khoanh vùng vị trí sai lầm và đặt câu hỏi gợi mở để học sinh tự chỉnh sửa.
            2. PHẢI CHIA RÕ 2 PHẦN THEO ĐÚNG CẤU TRÚC SAU:
            ---PHẦN HIỂN THỊ MÀN HÌNH---
            (Trình bày chi tiết, chuẩn sư phạm, công thức viết trong dấu $).
            ---PHẦN LỜI THOẠI PHÁT LOA---
            (Chỉ viết 2 đến 3 câu ngắn gọn, ấm áp, định hướng tư duy. TUYỆT ĐỐI KHÔNG CHỨA CÔNG THỨC TOÁN, KHÔNG CHỨA KÝ HIỆU LATEX để giọng đọc tự nhiên).
            """
            raw_reply = ""
            if client:
                try:
                    if img_cam:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt_pedagogy, img_cam])
                        reward_student_flower(student_info["student_id"], 1, "chụp ảnh vở nháp hỏi bài học tập")
                    elif aud_mic:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt_pedagogy, {"mime_type": "audio/wav", "data": aud_mic}])
                    else:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[prompt_pedagogy, f"Câu hỏi của học sinh: {txt_q}"])
                    raw_reply = res.text
                except Exception:
                    raw_reply = "---PHẦN HIỂN THỊ MÀN HÌNH---\nEm đã thực hiện đúng bước đại số cơ bản. Hãy kiểm tra kỹ lại dấu của góc lượng giác trong góc phần tư tương ứng nhé!\n---PHẦN LỜI THOẠI PHÁT LOA---\nThầy cô đã nhận bài làm của em. Các bước biến đổi rất tốt, em hãy quan sát kỹ lưu ý về dấu trên màn hình nhé!"
            else:
                raw_reply = "---PHẦN HIỂN THỊ MÀN HÌNH---\nEm đã thực hiện đúng bước biến đổi đầu tiên. Hãy chú ý điều kiện của góc để chọn dấu chính xác.\n---PHẦN LỜI THOẠI PHÁT LOA---\nCác bước làm rất tốt, em hãy kiểm tra lại dấu như hướng dẫn trên màn hình nhé!"

            disp_p = raw_reply
            voice_p = "Thầy cô đã xem bài của em, hãy xem kỹ hướng dẫn trên màn hình nhé!"
            if "---PHẦN HIỂN THỊ MÀN HÌNH---" in raw_reply and "---PHẦN LỜI THOẠI PHÁT LOA---" in raw_reply:
                parts = raw_reply.split("---PHẦN LỜI THOẠI PHÁT LOA---")
                disp_p = parts[0].replace("---PHẦN HIỂN THỊ MÀN HÌNH---", "").strip()
                voice_p = parts[1].strip()

            with st.container(border=True):
                st.markdown(disp_p)

            try:
                tts = gTTS(text=voice_p, lang='vi', slow=False)
                tts.save("voice_reply.mp3")
                st.markdown("🔊 **Lời Nhắn Nhủ Bằng Giọng Nói Từ Gia Sư AI:**")
                st.audio("voice_reply.mp3", format="audio/mp3")
            except Exception:
                pass

# ------------------------------------------------------------------------------
# TAB 5: PHÒNG KHẢO THÍ CHUẨN ĐỊNH DẠNG ĐÚNG/SAI & QUY CHẾ ĐIỂM BỘ GD&ĐT
# ------------------------------------------------------------------------------
with tab4:
    st.subheader(f"🎯 Phòng Khảo Thí & Luyện Đề Chuẩn Hóa ({sel_grade})")
    st.caption("Cấu trúc đề thi mới nhất: Trắc nghiệm 4 lựa chọn, Trắc nghiệm Đúng/Sai 4 ý, và Trả lời ngắn.")

    grade_exam_dict = EXAM_BANK.get(sel_grade, {})
    exam_k = list(grade_exam_dict.keys())
    sel_exam = st.selectbox("Chọn Kì Thi / Bài Khảo Thí:", exam_k)
    ex_pack = grade_exam_dict[sel_exam]

    with st.container(border=True):
        st.markdown(f"### 📋 {ex_pack['title']}")
        st.markdown("""
        <div class="rule-box">
            <b>⚖️ Quy chế tính điểm trắc nghiệm Đúng/Sai chính thức của Bộ GD&ĐT:</b><br>
            Mỗi câu gồm 4 ý a), b), c), d):<br>
            • Đúng <b>1 ý</b> được <b>0.1 điểm</b> | • Đúng <b>2 ý</b> được <b>0.25 điểm</b><br>
            • Đúng <b>3 ý</b> được <b>0.5 điểm</b> | • Đúng cả <b>4 ý</b> được <b>1.0 điểm trọn vẹn</b>.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### PHẦN I: Câu trắc nghiệm nhiều phương án lựa chọn (3.0 điểm)")
        user_p1 = {}
        for idx, item in enumerate(ex_pack.get("p1", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            user_p1[idx] = st.radio(f"Chọn phương án câu {idx + 1}:", item["ops"], key=f"ex_p1_{sel_exam}_{idx}")

        st.markdown("---")
        st.markdown("#### PHẦN II: Câu trắc nghiệm Đúng / Sai (4.0 điểm)")
        user_p2 = {}
        for idx, item in enumerate(ex_pack.get("p2", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            sub_choices = []
            for s_idx, (statement_text, _, _) in enumerate(item["items"]):
                c_lbl = f"{statement_text}"
                ans_val = st.radio(
                    label=c_lbl,
                    options=["Chưa chọn", "Đúng", "Sai"],
                    horizontal=True,
                    key=f"ex_p2_{sel_exam}_{idx}_{s_idx}"
                )
                sub_choices.append(ans_val)
            user_p2[idx] = sub_choices

        st.markdown("---")
        st.markdown("#### PHẦN III: Câu trắc nghiệm trả lời ngắn (3.0 điểm)")
        user_p3 = {}
        for idx, item in enumerate(ex_pack.get("p3", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            user_p3[idx] = st.text_input(f"Điền kết quả số câu {idx + 1}:", key=f"ex_p3_{sel_exam}_{idx}")

        st.markdown("---")
        if st.button("📤 Nộp Bài Khảo Thí & Chấm Điểm Chuẩn Quy Chế", use_container_width=True):
            score_p1 = 0.0
            score_p2 = 0.0
            score_p3 = 0.0

            p1_items = ex_pack.get("p1", [])
            p1_corr = sum(1 for idx, item in enumerate(p1_items) if user_p1[idx].startswith(item["ans"]))
            if p1_items:
                score_p1 = (p1_corr / len(p1_items)) * 3.0

            p2_questions = ex_pack.get("p2", [])
            for idx, item in enumerate(p2_questions):
                num_correct_in_q = 0
                for s_idx, (_, is_true, _) in enumerate(item["items"]):
                    u_c = user_p2[idx][s_idx]
                    if (u_c == "Đúng" and is_true) or (u_c == "Sai" and not is_true):
                        num_correct_in_q += 1

                if num_correct_in_q == 1:
                    score_p2 += 0.1
                elif num_correct_in_q == 2:
                    score_p2 += 0.25
                elif num_correct_in_q == 3:
                    score_p2 += 0.5
                elif num_correct_in_q == 4:
                    score_p2 += 1.0

            if p2_questions and len(p2_questions) != 4:
                score_p2 = (score_p2 / (len(p2_questions) * 1.0)) * 4.0

            p3_items = ex_pack.get("p3", [])
            p3_corr = 0
            for idx, item in enumerate(p3_items):
                clean_u = user_p3[idx].strip().replace(",", ".")
                clean_target = item["ans"].strip().replace(",", ".")
                alt_list = [a.replace(",", ".") for a in item.get("alt", [])]
                if clean_u == clean_target or clean_u in alt_list:
                    p3_corr += 1
                else:
                    try:
                        if abs(float(clean_u) - float(clean_target)) < 0.1:
                            p3_corr += 1
                    except Exception:
                        pass
            if p3_items:
                score_p3 = (p3_corr / len(p3_items)) * 3.0

            total_score = round(score_p1 + score_p2 + score_p3, 2)

            st.balloons()
            st.success(f"🎉 **KẾT QUẢ BÀI THI CỦA EM:** **{total_score} / 10.0 Điểm**")
            st.markdown(f"- Điểm Phần I: **{round(score_p1, 2)}** / 3.0 điểm.")
            st.markdown(f"- Điểm Phần II (Đúng/Sai bậc thang Bộ GD&ĐT): **{round(score_p2, 2)}** / 4.0 điểm.")
            st.markdown(f"- Điểm Phần III: **{round(score_p3, 2)}** / 3.0 điểm.")

            if total_score >= 10.0:
                reward_student_flower(student_info["student_id"], 3, f"đạt điểm tuyệt đối 10.0 ở {sel_exam}")
            elif total_score >= 9.0:
                reward_student_flower(student_info["student_id"], 2, f"đạt điểm xuất sắc {total_score} ở {sel_exam}")
            elif total_score >= 8.0:
                reward_student_flower(student_info["student_id"], 1, f"vượt ải thành công {total_score} điểm ở {sel_exam}")
            else:
                st.info("💡 Điểm số chưa đạt mốc 8.0 để nhận hoa thưởng. Hãy đối chiếu lời giải chi tiết bên dưới nhé!")

            with st.expander("📖 Xem Chi Tiết Đáp Án & Hướng Dẫn Giải Từng Câu"):
                st.markdown("#### Đáp án Phần I:")
                for idx, item in enumerate(p1_items):
                    st.markdown(f"- **Câu {idx+1}:** Đáp án đúng là **{item['ans']}**. {item['exp']}")

                st.markdown("#### Đáp án Phần II (Đúng / Sai):")
                for idx, item in enumerate(p2_questions):
                    st.markdown(f"**Câu {idx+1}:**")
                    for s_idx, (st_text, is_true, exp_txt) in enumerate(item["items"]):
                        txt_label = "ĐÚNG" if is_true else "SAI"
                        st.markdown(f"  + *Ý {chr(97+s_idx)})* : **{txt_label}** — {exp_txt}")

                st.markdown("#### Đáp án Phần III (Trả lời ngắn):")
                for idx, item in enumerate(p3_items):
                    st.markdown(f"- **Câu {idx+1}:** Đáp số là **{item['ans']}**. Hướng dẫn: {item['exp']}")
