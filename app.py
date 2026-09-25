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
        margin-top: 10px;
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
# 3. KHO HỌC LIỆU SỐ TOÀN DIỆN BÁM SÁT VỞ TỰ HỌC: ĐỦ CHỦ ĐIỂM & 3-4 VÍ DỤ CƠ BẢN
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 12": {
        "Bài 1: Tính đơn điệu và cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị của hàm số",
            "topics": {
                "Chủ điểm 1: Tính đơn điệu của hàm số": {
                    "theory": """
- Cho hàm số $y = f(x)$ xác định và có đạo hàm trên khoảng $K$:
  + Nếu $f'(x) > 0, \forall x \in K$ thì hàm số **đồng biến** trên $K$.
  + Nếu $f'(x) < 0, \forall x \in K$ thì hàm số **nghịch biến** trên $K$.
  + Nếu $f'(x) \ge 0$ (hoặc $f'(x) \le 0$), $\forall x \in K$ và $f'(x) = 0$ chỉ tại hữu hạn điểm thì hàm số đồng biến (hoặc nghịch biến) trên $K$.
- **Quy trình xét tính đơn điệu:**
  1. Tìm tập xác định $D$.
  2. Tính đạo hàm $y' = f'(x)$. Tìm các điểm mà tại đó đạo hàm bằng $0$ hoặc không xác định.
  3. Lập bảng xét dấu $y'$ và kết luận từng khoảng đồng biến, nghịch biến.
""",
                    "formula": r"f'(x) \ge 0, \forall x \in K \iff \text{Hàm số đồng biến trên } K; \quad f'(x) \le 0, \forall x \in K \iff \text{Hàm số nghịch biến trên } K",
                    "trap": "Kết luận khoảng đồng biến, nghịch biến phải dùng từ 'và' hoặc dấu phẩy, tuyệt đối không dùng ký hiệu hợp (U) hay phép trừ tập hợp (\\).",
                    "audio": "Hàm số đồng biến khi đạo hàm lớn hơn hoặc bằng không, nghịch biến khi đạo hàm nhỏ hơn hoặc bằng không. Luôn kết luận trên từng khoảng riêng biệt.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm khoảng đơn điệu của hàm số bậc ba",
                            "problem": "Xét tính đơn điệu và tìm các khoảng đồng biến, nghịch biến của hàm số: $$y = x^3 - 3x^2 + 2$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R}$.
- **Bước 2: Đạo hàm:**
  $$y' = 3x^2 - 6x = 3x(x - 2)$$
  Cho $y' = 0 \\iff 3x(x - 2) = 0 \\iff x = 0$ hoặc $x = 2$.
- **Bước 3: Bảng xét dấu đạo hàm:**
  + Khoảng $(-\\infty; 0)$: $y' > 0$ $\\Rightarrow$ Hàm số đồng biến.
  + Khoảng $(0; 2)$: $y' < 0$ $\\Rightarrow$ Hàm số nghịch biến.
  + Khoảng $(2; +\\infty)$: $y' > 0$ $\\Rightarrow$ Hàm số đồng biến.
- **Kết luận:** Hàm số đồng biến trên các khoảng $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên khoảng $(0; 2)$.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm khoảng đơn điệu của hàm phân thức bậc nhất trên bậc nhất",
                            "problem": "Tìm các khoảng đồng biến và nghịch biến của hàm số: $$y = \\frac{2x - 1}{x + 1}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R} \\setminus \\{-1\\}$.
- **Bước 2: Tính đạo hàm theo công thức nhanh $\\left(\\frac{ax+b}{cx+d}\\right)' = \\frac{ad - bc}{(cx+d)^2}$:**
  $$y' = \\frac{2 \\cdot 1 - (-1) \\cdot 1}{(x + 1)^2} = \\frac{3}{(x + 1)^2}$$
- **Bước 3: Xét dấu đạo hàm:**
  Vì $3 > 0$ và $(x + 1)^2 > 0$ với mọi $x \\neq -1$ nên:
  $$y' > 0, \\quad \\forall x \\neq -1$$
- **Kết luận:** Hàm số đồng biến trên từng khoảng xác định $(-\\infty; -1)$ và $(-1; +\\infty)$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm khoảng đơn điệu của hàm phân thức bậc hai trên bậc nhất",
                            "problem": "Tìm các khoảng đơn điệu của hàm số: $$y = \\frac{x^2 - 2x + 2}{x - 1}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R} \\setminus \\{1\\}$.
- **Bước 2: Đạo hàm thương $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$:**
  $$y' = \\frac{(2x - 2)(x - 1) - (x^2 - 2x + 2) \\cdot 1}{(x - 1)^2} = \\frac{x^2 - 2x}{(x - 1)^2}$$
  Cho $y' = 0 \\iff x^2 - 2x = 0 \\iff x = 0$ hoặc $x = 2$ (cả hai đều thỏa mãn $x \\neq 1$).
- **Bước 3: Bảng xét dấu đạo hàm:**
  + $y' > 0$ trên $(-\\infty; 0)$ và $(2; +\\infty)$.
  + $y' < 0$ trên $(0; 1)$ và $(1; 2)$.
- **Kết luận:** Hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên $(0; 1)$ và $(1; 2)$.
"""
                        },
                        {
                            "title": "Ví dụ 4: Đọc khoảng đơn điệu từ bảng biến thiên",
                            "problem": "Cho hàm số $y = f(x)$ xác định trên $\\mathbb{R}$ có bảng biến thiên: $f'(x) > 0$ trên $(-\\infty; -1)$ và $(3; +\\infty)$; $f'(x) < 0$ trên $(-1; 3)$. Khẳng định nào đúng về khoảng nghịch biến?",
                            "solution": """
- **Phương pháp đọc bảng biến thiên:** Khoảng nghịch biến của hàm số là khoảng của biến số $x$ mà tại đó mũi tên đi xuống hoặc đạo hàm mang dấu âm.
- Nhìn vào dòng $f'(x)$, ta thấy dấu $(-)$ xuất hiện trên khoảng $(-1; 3)$.
- **Kết luận:** Hàm số nghịch biến trên khoảng $(-1; 3)$.
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
- **Định nghĩa:** Cho hàm số $y = f(x)$ xác định trên tập $D$ và $x_0 \in D$.
  + Nếu tồn tại khoảng $(a; b) \subset D$ chứa $x_0$ sao cho $f(x) < f(x_0), \forall x \in (a; b) \setminus \{x_0\}$ thì $x_0$ là **điểm cực đại**. Khi đó $f(x_0)$ là **giá trị cực đại**.
  + Nếu $f(x) > f(x_0), \forall x \in (a; b) \setminus \{x_0\}$ thì $x_0$ là **điểm cực tiểu**. Khi đó $f(x_0)$ là **giá trị cực tiểu**.
- **Dấu hiệu 1 (Đổi dấu đạo hàm cấp 1):**
  + Qua điểm $x_0$, nếu $f'(x)$ đổi dấu từ $(+)$ sang $(-)$ thì $x_0$ là điểm cực đại.
  + Qua điểm $x_0$, nếu $f'(x)$ đổi dấu từ $(-)$ sang $(+)$ thì $x_0$ là điểm cực tiểu.
""",
                    "formula": r"f'(x_0) = 0 \text{ hoặc không xác định}; \quad (+) \xrightarrow{x_0} (-) \implies \text{Cực đại}; \quad (-) \xrightarrow{x_0} (+) \implies \text{Cực tiểu}",
                    "trap": "Phân biệt rõ: 'Điểm cực trị của hàm số' là hoành độ x0. 'Giá trị cực trị' là tung độ y0 = f(x0). 'Điểm cực trị của đồ thị' là cặp tọa độ M(x0; y0).",
                    "audio": "Điểm cực trị là giá trị x0, giá trị cực trị là tung độ y0, còn điểm cực trị của đồ thị là cặp tọa độ M(x0; y0). Nhớ phân biệt kỹ câu hỏi.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm cực trị của hàm số bậc ba",
                            "problem": "Tìm các điểm cực trị và giá trị cực trị của hàm số: $$y = x^3 - 3x^2 + 2$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R}$.
- **Bước 2: Đạo hàm:**
  $$y' = 3x^2 - 6x = 3x(x - 2)$$
  Cho $y' = 0 \\iff x = 0$ hoặc $x = 2$.
- **Bước 3: Xét dấu $y'$ qua các điểm nghiệm:**
  + Khi $x$ qua điểm $0$, đạo hàm $y'$ đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow x = 0$ là điểm cực đại. Giá trị cực đại là $y_{CĐ} = f(0) = 2$.
  + Khi $x$ qua điểm $2$, đạo hàm $y'$ đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow x = 2$ là điểm cực tiểu. Giá trị cực tiểu là $y_{CT} = f(2) = 2^3 - 3(2^2) + 2 = -2$.
- **Kết luận:** Hàm số đạt cực đại tại $x = 0$ với $y_{CĐ} = 2$; đạt cực tiểu tại $x = 2$ với $y_{CT} = -2$.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm tọa độ điểm cực trị của đồ thị hàm số",
                            "problem": "Tìm tọa độ các điểm cực trị của đồ thị hàm số: $$y = -x^4 + 2x^2 + 3$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R}$.
- **Bước 2: Đạo hàm:**
  $$y' = -4x^3 + 4x = -4x(x^2 - 1)$$
  Cho $y' = 0 \\iff x = 0$ hoặc $x = 1$ hoặc $x = -1$.
- **Bước 3: Tính giá trị tương ứng:**
  + Tại $x = 0$: $y(0) = 3$. Đạo hàm đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow (0; 3)$ là điểm cực tiểu của đồ thị.
  + Tại $x = 1$: $y(1) = 4$. Đạo hàm đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow (1; 4)$ là điểm cực đại của đồ thị.
  + Tại $x = -1$: $y(-1) = 4$. Đạo hàm đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow (-1; 4)$ là điểm cực đại của đồ thị.
- **Kết luận:** Đồ thị hàm số có hai điểm cực đại là $A(1; 4), B(-1; 4)$ và một điểm cực tiểu là $C(0; 3)$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm cực trị của hàm phân thức bậc hai trên bậc nhất",
                            "problem": "Tìm các điểm cực trị của hàm số: $$y = \\frac{x^2 + 3}{x - 1}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $D = \\mathbb{R} \\setminus \\{1\\}$.
- **Bước 2: Đạo hàm:**
  $$y' = \\frac{2x(x - 1) - (x^2 + 3) \\cdot 1}{(x - 1)^2} = \\frac{x^2 - 2x - 3}{(x - 1)^2}$$
  Cho $y' = 0 \\iff x^2 - 2x - 3 = 0 \\iff x = -1$ hoặc $x = 3$.
- **Bước 3: Đổi dấu đạo hàm:**
  + Qua $x = -1$, $y'$ đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow x = -1$ là điểm cực đại; $y_{CĐ} = \\frac{(-1)^2 + 3}{-1 - 1} = -2$.
  + Qua $x = 3$, $y'$ đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow x = 3$ là điểm cực tiểu; $y_{CT} = \\frac{3^2 + 3}{3 - 1} = 6$.
- **Kết luận:** Hàm số đạt cực đại tại $x = -1$ với $y_{CĐ} = -2$; đạt cực tiểu tại $x = 3$ với $y_{CT} = 6$.
"""
                        },
                        {
                            "title": "Ví dụ 4: Nhận biết cực trị qua đạo hàm không xác định",
                            "problem": "Cho hàm số $y = f(x)$ liên tục trên $\\mathbb{R}$, có đạo hàm $f'(x) = \\frac{x-1}{\\sqrt[3]{x^2}}$. Hỏi hàm số có bao nhiêu điểm cực trị?",
                            "solution": """
- Hàm số liên tục trên toàn $\\mathbb{R}$.
- Đạo hàm $f'(x) = 0 \\iff x = 1$. Tại $x = 0$, đạo hàm không xác định nhưng hàm số vẫn liên tục.
- **Xét sự đổi dấu của $f'(x)$:**
  + Khi $x$ qua điểm $0$: mẫu số $\\sqrt[3]{x^2} > 0, \\forall x \\neq 0$ và tử số $x - 1 < 0$ khi $x < 1$. Do đó qua $x = 0$, $f'(x)$ KHÔNG đổi dấu (vẫn âm). Vậy $x = 0$ không phải cực trị.
  + Khi $x$ qua điểm $1$: tử số $x - 1$ đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow x = 1$ là điểm cực tiểu.
- **Kết luận:** Hàm số có đúng $1$ điểm cực trị là điểm cực tiểu $x = 1$.
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
                "Chủ điểm 1: Tìm GTLN và GTNN của hàm số trên một đoạn [a; b]": {
                    "theory": """
- **Định lý:** Mọi hàm số liên tục trên một đoạn $[a; b]$ đều có giá trị lớn nhất và giá trị nhỏ nhất trên đoạn đó.
- **Quy trình tìm GTLN, GTNN trên đoạn $[a; b]$ không cần lập bảng biến thiên:**
  1. Tính đạo hàm $f'(x)$.
  2. Tìm các nghiệm $x_1, x_2, \dots \in (a; b)$ của phương trình $f'(x) = 0$ (loại bỏ các nghiệm nằm ngoài đoạn).
  3. Tính các giá trị $f(a), f(b), f(x_1), f(x_2), \dots$.
  4. Số lớn nhất trong các giá trị vừa tính là $\\max_{[a; b]} f(x)$, số nhỏ nhất là $\\min_{[a; b]} f(x)$.
""",
                    "formula": r"\max_{[a; b]} f(x) = \max\{f(a), f(b), f(x_i)\}; \quad \min_{[a; b]} f(x) = \min\{f(a), f(b), f(x_i)\}",
                    "trap": "Chỉ lấy các nghiệm đạo hàm NẰM TRONG khoảng (a; b). Nghiệm nằm ngoài đoạn bắt buộc phải loại bỏ trước khi tính giá trị.",
                    "audio": "Trên một đoạn số thực, ta tính giá trị tại hai đầu mút và tại các điểm đạo hàm bằng không thuộc khoảng đó rồi so sánh.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm GTLN, GTNN của hàm đa thức bậc ba trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số: $$f(x) = x^3 - 3x + 1 \\quad \\text{trên đoạn } [0; 2]$$",
                            "solution": """
- **Bước 1:** Hàm số liên tục trên $[0; 2]$.
- **Bước 2: Đạo hàm:**
  $$f'(x) = 3x^2 - 3 = 0 \\iff x = 1 \\in (0; 2) \\quad \\text{hoặc } x = -1 \\notin (0; 2) \\text{ (loại)}$$
- **Bước 3: Tính các giá trị:**
  + $f(0) = 1$
  + $f(1) = 1^3 - 3(1) + 1 = -1$
  + $f(2) = 2^3 - 3(2) + 1 = 3$
- **Bước 4: So sánh và kết luận:**
  $$\\max_{[0; 2]} f(x) = f(2) = 3; \\quad \\min_{[0; 2]} f(x) = f(1) = -1$$
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm GTLN, GTNN của hàm phân thức trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và nhỏ nhất của hàm số: $$y = \\frac{x - 2}{x + 1} \\quad \\text{trên đoạn } [0; 3]$$",
                            "solution": """
- **Bước 1:** Hàm số xác định và liên tục trên $[0; 3]$ (vì điểm gián đoạn $x = -1 \\notin [0; 3]$).
- **Bước 2: Đạo hàm:**
  $$y' = \\frac{1 \\cdot 1 - (-2) \\cdot 1}{(x + 1)^2} = \\frac{3}{(x + 1)^2} > 0, \\quad \\forall x \\in [0; 3]$$
- Do $y' > 0$ nên hàm số đồng biến liên tục trên đoạn $[0; 3]$.
- **Bước 3: Kết luận:**
  + $\\min_{[0; 3]} y = y(0) = \\frac{0 - 2}{0 + 1} = -2$.
  + $\\max_{[0; 3]} y = y(3) = \\frac{3 - 2}{3 + 1} = \\frac{1}{4}$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm GTLN, GTNN của hàm chứa căn thức trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số: $$y = x + \\sqrt{4 - x^2}$$",
                            "solution": """
- **Bước 1: Tập xác định:** $4 - x^2 \\ge 0 \\iff x \\in [-2; 2]$. Ta xét trên đoạn $[-2; 2]$.
- **Bước 2: Đạo hàm trên $(-2; 2)$:**
  $$y' = 1 - \\frac{x}{\\sqrt{4 - x^2}}$$
  Cho $y' = 0 \\iff \\sqrt{4 - x^2} = x \\iff \\begin{cases} x > 0 \\\\ 4 - x^2 = x^2 \\end{cases} \\iff 2x^2 = 4 \\iff x = \\sqrt{2} \\in (-2; 2)$.
- **Bước 3: Tính các giá trị:**
  + $y(-2) = -2 + 0 = -2$.
  + $y(2) = 2 + 0 = 2$.
  + $y(\\sqrt{2}) = \\sqrt{2} + \\sqrt{4 - 2} = 2\\sqrt{2}$.
- **Bước 4: Kết luận:** $\\max_{[-2; 2]} y = 2\\sqrt{2}$ (đạt tại $x = \\sqrt{2}$); $\\min_{[-2; 2]} y = -2$ (đạt tại $x = -2$).
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
- **Tiệm cận đứng:** Đường thẳng $x = x_0$ là tiệm cận đứng của đồ thị hàm số $y = f(x)$ nếu có ít nhất một trong các điều kiện sau thỏa mãn:
  $$\\lim_{x \\to x_0^+} f(x) = +\\infty; \\quad \\lim_{x \\to x_0^+} f(x) = -\\infty; \\quad \\lim_{x \\to x_0^-} f(x) = +\\infty; \\quad \\lim_{x \\to x_0^-} f(x) = -\\infty$$
- **Tiệm cận ngang:** Đường thẳng $y = y_0$ là tiệm cận ngang của đồ thị hàm số $y = f(x)$ nếu:
  $$\\lim_{x \\to +\\infty} f(x) = y_0 \\quad \\text{hoặc} \\quad \\lim_{x \\to -\\infty} f(x) = y_0$$
- **Hàm số nhất biến $y = \\frac{ax + b}{cx + d}$ ($c \\neq 0, ad - bc \\neq 0$):**
  + Tiệm cận đứng: $x = -\\frac{d}{c}$.
  + Tiệm cận ngang: $y = \\frac{a}{c}$.
""",
                    "formula": r"\lim_{x \to x_0} y = \pm\infty \implies x = x_0 \ (\text{TCĐ}); \quad \lim_{x \to \pm\infty} y = y_0 \implies y = y_0 \ (\text{TCN})",
                    "trap": "Tránh nhầm lẫn biến: Tiệm cận đứng là phương trình dạng x = số, tiệm cận ngang là phương trình dạng y = số.",
                    "audio": "Mẫu số triệt tiêu mà tử số khác không cho ta tiệm cận đứng x = x0. Giới hạn tại vô cực cho ta tiệm cận ngang y = y0.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm tiệm cận của hàm phân thức bậc nhất trên bậc nhất",
                            "problem": "Xác định các đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số: $$y = \\frac{2x - 3}{x + 1}$$",
                            "solution": """
- **Tiệm cận đứng:**
  Mẫu số triệt tiêu khi $x + 1 = 0 \\iff x = -1$.
  Ta có $\\lim_{x \\to -1^+} \\frac{2x - 3}{x + 1} = -\\infty$ (do tử số tiến tới $-5 < 0$, mẫu số tiến tới $0^+$).
  $\\Rightarrow$ Đường thẳng $x = -1$ là tiệm cận đứng.
- **Tiệm cận ngang:**
  Ta có $\\lim_{x \\to +\\infty} \\frac{2x - 3}{x + 1} = \\lim_{x \\to +\\infty} \\frac{2 - \\frac{3}{x}}{1 + \\frac{1}{x}} = 2$.
  Tương tự $\\lim_{x \\to -\\infty} y = 2$.
  $\\Rightarrow$ Đường thẳng $y = 2$ là tiệm cận ngang.
"""
                        },
                        {
                            "title": "Ví dụ 2: Tìm tiệm cận của đồ thị hàm số có nghiệm của mẫu triệt tiêu tử",
                            "problem": "Tìm số đường tiệm cận đứng của đồ thị hàm số: $$y = \\frac{x - 1}{x^2 - 1}$$",
                            "solution": """
- Mẫu số $x^2 - 1 = 0 \\iff x = 1$ hoặc $x = -1$.
- Xét tại $x = 1$:
  $$\\lim_{x \\to 1} \\frac{x - 1}{(x - 1)(x + 1)} = \\lim_{x \\to 1} \\frac{1}{x + 1} = \\frac{1}{2} \\neq \\pm\\infty$$
  Do đó đường thẳng $x = 1$ KHÔNG phải là tiệm cận đứng.
- Xét tại $x = -1$:
  $$\\lim_{x \\to -1^+} \\frac{1}{x + 1} = +\\infty$$
  Do đó đường thẳng $x = -1$ là tiệm cận đứng duy nhất.
- **Kết luận:** Đồ thị hàm số chỉ có đúng $1$ đường tiệm cận đứng là $x = -1$.
"""
                        },
                        {
                            "title": "Ví dụ 3: Tìm tiệm cận ngang của hàm chứa căn thức",
                            "problem": "Tìm các đường tiệm cận ngang của đồ thị hàm số: $$y = \\frac{\\sqrt{x^2 + 1}}{x - 1}$$",
                            "solution": """
- Khi $x \\to +\\infty$: $\\sqrt{x^2 + 1} = x\\sqrt{1 + \\frac{1}{x^2}}$.
  $$\\lim_{x \\to +\\infty} \\frac{x\\sqrt{1 + \\frac{1}{x^2}}}{x(1 - \\frac{1}{x})} = 1 \\implies y = 1 \\text{ là một TCN.}$$
- Khi $x \\to -\\infty$: $\\sqrt{x^2 + 1} = -x\\sqrt{1 + \\frac{1}{x^2}}$ (vì $x < 0$).
  $$\\lim_{x \\to -\\infty} \\frac{-x\\sqrt{1 + \\frac{1}{x^2}}}{x(1 - \\frac{1}{x})} = -1 \\implies y = -1 \\text{ là một TCN.}$$
- **Kết luận:** Đồ thị hàm số có 2 đường tiệm cận ngang là $y = 1$ và $y = -1$.
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
                "Chủ điểm 1: Khái niệm mệnh đề và Mệnh đề chứa biến": {
                    "theory": "Mệnh đề toán học là một câu khẳng định có chân giá trị Đúng hoặc Sai, không thể vừa đúng vừa sai. Câu cảm thán, câu hỏi không phải là mệnh đề.",
                    "formula": r"P \in \{\text{Đúng}, \text{Sai}\}",
                    "trap": "Mệnh đề chứa biến chưa gán giá trị cụ thể thì chưa thể xác định tính đúng sai.",
                    "audio": "Mệnh đề toán học là một câu khẳng định chỉ nhận một trong hai chân giá trị: Đúng hoặc Sai.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Nhận diện câu là mệnh đề toán học",
                            "problem": "Trong các câu sau, câu nào là mệnh đề toán học: a) 15 là số nguyên tố; b) Số 0 là số tự nhiên nhỏ nhất?",
                            "solution": "Cả hai câu a và b đều là khẳng định: câu a là mệnh đề toán học Sai, câu b là mệnh đề toán học Đúng."
                        },
                        {
                            "title": "Ví dụ 2: Mệnh đề chứa biến",
                            "problem": "Cho mệnh đề chứa biến $P(n)$: '$n$ chia hết cho 3'. Tìm một giá trị của $n$ để được mệnh đề đúng và một giá trị để được mệnh đề sai.",
                            "solution": "- Với $n = 6$: $P(6)$ là mệnh đề đúng vì 6 chia hết cho 3.\n- Với $n = 5$: $P(5)$ là mệnh đề sai vì 5 không chia hết cho 3."
                        },
                        {
                            "title": "Ví dụ 3: Xác định tính đúng sai của mệnh đề",
                            "problem": "Xét tính đúng sai của mệnh đề: 'Tổng ba góc trong một tam giác bằng 180 độ'.",
                            "solution": "Đây là khẳng định toán học chính xác theo tiên đề Euclid. Mệnh đề này nhận chân giá trị Đúng."
                        }
                    ],
                    "exercise": {
                        "id": "10_B1_CD1",
                        "title": "Bài tập kiểm minh chứng: Mệnh đề toán học",
                        "content": "Trong các câu: (1) 2 + 3 = 5; (2) Số pi là số hữu tỉ; (3) Bạn học bài chưa? Có bao nhiêu câu là mệnh đề toán học?",
                        "type": "NUMERIC", "target": "2", "options": []
                    }
                },
                "Chủ điểm 2: Mệnh đề phủ định và Mệnh đề chứa lượng từ": {
                    "theory": "Phủ định của mệnh đề P là mệnh đề P ngang. Phủ định của 'với mọi' là 'tồn tại', phủ định của '>' là '<='.",
                    "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
                    "trap": "Không được bỏ quên dấu bằng khi phủ định các bất đẳng thức lớn hơn hoặc nhỏ hơn.",
                    "audio": "Phủ định của với mọi là tồn tại, phủ định của lớn hơn là nhỏ hơn hoặc bằng.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Phủ định mệnh đề có lượng từ với mọi",
                            "problem": "Lập mệnh đề phủ định của $P$: '$\\forall x \\in \\mathbb{R}, x^2 + 1 > 0$'.",
                            "solution": "Phủ định của $\\forall$ là $\\exists$, phủ định của $>$ là $\\le$.\nVậy $\\overline{P}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$'. Mệnh đề phủ định này Sai."
                        },
                        {
                            "title": "Ví dụ 2: Phủ định mệnh đề có lượng từ tồn tại",
                            "problem": "Lập mệnh đề phủ định của $Q$: '$\\exists n \\in \\mathbb{N}, n^2 = n$'.",
                            "solution": "Phủ định của $\\exists$ là $\\forall$, phủ định của $=$ là $\\neq$.\nVậy $\\overline{Q}$: '$\\forall n \\in \\mathbb{N}, n^2 \\neq n$'."
                        },
                        {
                            "title": "Ví dụ 3: Xét tính đúng sai của mệnh đề chứa lượng từ",
                            "problem": "Xét tính đúng sai của mệnh đề: '$\\exists x \\in \\mathbb{R}, x^2 - 4 = 0$'.",
                            "solution": "Phương trình $x^2 - 4 = 0$ có nghiệm $x = 2 \\in \\mathbb{R}$. Vì tồn tại ít nhất một giá trị thỏa mãn nên mệnh đề này Đúng."
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
                    "trap": "Khai căn để tìm cos từ sin bắt buộc phải dựa vào góc phần tư để chọn dấu âm hoặc dương.",
                    "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Luôn kiểm tra kỹ góc phần tư khi khai căn.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính cos khi biết sin ở góc phần tư thứ II",
                            "problem": "Cho góc $\\alpha$ thỏa mãn $\\frac{\\pi}{2} < \\alpha < \\pi$ và $\\sin\\alpha = \\frac{3}{5}$. Hãy tính $\\cos\\alpha$ và $\\tan\\alpha$.",
                            "solution": "Ta có $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$.\nVì $\\frac{\\pi}{2} < \\alpha < \\pi$ (góc II) nên $\\cos\\alpha < 0$.\nVậy $\\cos\\alpha = -\\frac{4}{5} = -0.8$ và $\\tan\\alpha = \\frac{3/5}{-4/5} = -0.75$."
                        },
                        {
                            "title": "Ví dụ 2: Tính sin khi biết cos ở góc phần tư thứ IV",
                            "problem": "Cho $\\cos\\alpha = \\frac{5}{13}$ với $\\frac{3\\pi}{2} < \\alpha < 2\\pi$. Tính $\\sin\\alpha$.",
                            "solution": "Ta có $\\sin^2\\alpha = 1 - \\cos^2\\alpha = 1 - \\frac{25}{169} = \\frac{144}{169}$.\nVì $\\alpha$ thuộc góc IV nên $\\sin\\alpha < 0$. Do đó $\\sin\\alpha = -\\frac{12}{13}$."
                        },
                        {
                            "title": "Ví dụ 3: Rút gọn biểu thức lượng giác cơ bản",
                            "problem": "Rút gọn biểu thức: $A = (1 - \\sin^2\\alpha)\\tan^2\\alpha + (1 - \\cos^2\\alpha)$.",
                            "solution": "Thay $1 - \\sin^2\\alpha = \\cos^2\\alpha$ và $1 - \\cos^2\\alpha = \\sin^2\\alpha$:\n$$A = \\cos^2\\alpha \\cdot \\frac{\\sin^2\\alpha}{\\cos^2\\alpha} + \\sin^2\\alpha = \\sin^2\\alpha + \\sin^2\\alpha = 2\\sin^2\\alpha$$."
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
# 4. KHO ĐỀ KHẢO THÍ CHUẨN ĐỊNH DẠNG MỚI CỦA BỘ GD&ĐT
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
# 5. DỮ LIỆU TÀI KHOẢN & GAMIFICATION
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

def render_3d_geometry_view(topic_type="SHAPE_3D"):
    x = [0, 0, 3, 1.5, 0]
    y = [0, 0, 0, 2.5, 0]
    z = [3, 0, 0, 0, 3]
    fig = go.Figure(data=[
        go.Scatter3d(
            x=x, y=y, z=z, mode='lines+markers+text',
            text=['S', 'A', 'B', 'C', 'S'],
            textposition='top center',
            line=dict(color='#2563EB', width=5),
            marker=dict(size=5, color='#E11D48')
        ),
        go.Mesh3d(
            x=[0, 3, 1.5], y=[0, 0, 2.5], z=[0, 0, 0],
            color='#67E8F9', opacity=0.35
        )
    ])
    fig.update_layout(
        scene=dict(
            xaxis=dict(showbackground=False, showticklabels=False, title=''),
            yaxis=dict(showbackground=False, showticklabels=False, title=''),
            zaxis=dict(showbackground=False, showticklabels=False, title='')
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=360
    )
    st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 6. MÀN HÌNH ĐĂNG NHẬP & PHÂN QUYỀN
# ==============================================================================
if st.session_state["auth_user"] is None:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📐 HỆ SINH THÁI TỰ HỌC TOÁN THPT 'GSTOÁN'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>Chuẩn hóa từng Chủ điểm bám sát Vở tự học Kết nối tri thức</p>", unsafe_allow_html=True)

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
            st.caption("💡 Tài khoản học sinh: `HS12_01`, `HS11_01`, `HS10_01` (Pass: `123`). Admin: `admin` / `gstoan2026`.")
    st.stop()

# ==============================================================================
# 7. THANH ĐIỀU HƯỚNG BÊN HÔNG (SIDEBAR)
# ==============================================================================
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state['auth_user']['full_name']}")
    if st.session_state["role"] == "student":
        st.caption(f"Mã định danh: **{st.session_state['auth_user']['student_id']}**")
        flowers = st.session_state['auth_user'].get('flowers', 30)
        with st.container(border=True):
            st.markdown("<h5 style='text-align: center; color: #DB2777; margin:0;'>🌸 Vườn hoa Tri thức</h5>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #BE185D; margin:4px 0;'>{flowers} 🌸</h2>", unsafe_allow_html=True)
            st.caption("Giải đúng bài tập nhận +2 hoa. Xem video +1 hoa. Khảo thí nhận tới +3 hoa!")
    else:
        st.info("Vai trò: **Cố Vấn Sư Phạm & Quản Trị**")

    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.session_state["role"] = None
        st.rerun()
    st.markdown("---")

# ==============================================================================
# 8. PHÂN HỆ GIÁO VIÊN
# ==============================================================================
if st.session_state["role"] == "teacher":
    st.title("👩‍🏫 Bảng Điều Khiển Giáo Viên: Quản Trị & Cố Vấn Sư Phạm")
    gt1, gt2 = st.tabs(["👥 Quản lý & Cấp Tài Khoản", "📬 Hộp Thư Cứu Trợ Sư Phạm"])

    with gt1:
        st.subheader("📋 Danh sách Học sinh Trên Hệ Thống")
        all_st = load_all_students()
        st.dataframe(pd.DataFrame(all_st)[["student_id", "full_name", "grade", "current_level", "flowers", "weak_spots"]], use_container_width=True)

        with st.container(border=True):
            st.markdown("#### ➕ Cấp Tài Khoản Học Sinh Mới")
            with st.form("form_add_s"):
                c1, c2 = st.columns(2)
                with c1:
                    nid = st.text_input("Mã học sinh mới (Ví dụ: HS12_02):")
                    nname = st.text_input("Họ và tên học sinh:")
                    ngrade = st.selectbox("Khối lớp:", [10, 11, 12], index=2)
                with c2:
                    npass = st.text_input("Mật khẩu cấp ban đầu:", value="123")
                    nlvl = st.selectbox("Học lực khởi điểm:", ["Giỏi", "Khá", "Trung bình", "Cần hỗ trợ"], index=1)
                    nweak = st.text_input("Lỗ hổng kiến thức:", value="Cần rèn luyện thêm bài tập SGK")
                if st.form_submit_button("Lưu & Cấp Tài Khoản"):
                    if nid and nname:
                        new_item = {"student_id": nid.strip().upper(), "password": npass, "full_name": nname.strip(), "grade": ngrade, "current_level": nlvl, "weak_spots": nweak, "flowers": 30, "total_solved": 0}
                        st.session_state["students_db"].append(new_item)
                        st.success(f"Đã cấp tài khoản thành công cho học sinh {nname}!")
                        st.rerun()

    with gt2:
        st.subheader("📬 Hộp Thư Nhận Câu Hỏi Bế Tắc Của Học Sinh")
        if st.session_state["inbox_db"]:
            st.dataframe(pd.DataFrame(st.session_state["inbox_db"]), use_container_width=True)
        else:
            st.info("Hiện không có câu hỏi bế tắc nào tồn đọng từ học sinh.")
    st.stop()

# ==============================================================================
# 9. PHÂN HỆ HỌC SINH (BỘ CHỌN 3 BẬC: KHỐI -> BÀI HỌC -> CHỦ ĐIỂM KIẾN THỨC)
# ==============================================================================
student_info = st.session_state["auth_user"]

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
    "📖 Cốt Lõi Kiến Thức (Video, Thuyết Minh & 3D)",
    "💡 Ví Dụ Minh Họa (Bấm Xem Lời Giải)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {cur_lesson_obj['chapter']}")
    st.markdown(f"#### {sel_lesson} — *{sel_topic}*")

    if "không gian" in sel_lesson or "Oxyz" in sel_lesson or "Vectơ" in sel_lesson:
        with st.container(border=True):
            st.markdown("🌐 **Mô Hình Không Gian 3D Tương Tác Trực Tiếp (Zero-Install)**")
            st.caption("Dùng chuột hoặc ngón tay chạm/vuốt để xoay 360 độ, quan sát hình chiếu:")
            render_3d_geometry_view()

    col_v, col_n = st.columns([1.1, 1.2])
    with col_v:
        with st.container(border=True):
            st.markdown(f"🎬 **Video bài giảng vi mô: {sel_topic}**")
            st.caption("Video tóm tắt lý thuyết trọng tâm + phương pháp giải toán then chốt")
            st.video("https://www.youtube.com/watch?v=kYJ_t120-Jk")
            
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Chủ Điểm (Trích Vở tự học):</b><br>
                <small>Bật nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5((sel_lesson + sel_topic).encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_topic_data["audio"], audio_hash)
            if lecture_audio_file:
                st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã xem và nghe xong bài giảng vi mô (+1 hoa)", key=f"vid_{sel_topic}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ xem và nghe bài giảng vi mô")
                
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes)**")
            st.markdown(f"#### 1. Định nghĩa & Khái niệm cốt lõi\n{cur_topic_data['theory']}")
            st.markdown("#### 2. Công thức Toán học trọng tâm")
            st.markdown(f"$${cur_topic_data['formula']}$$")
            st.markdown(f"#### 3. Phương pháp tư duy & Cảnh báo bẫy sai lầm\n- ⚠️ **Lưu ý bẫy đề thi:** {cur_topic_data['trap']}")

# ------------------------------------------------------------------------------
# TAB 2: VÍ DỤ MINH HỌA (TRÌNH BÀY ĐỀ BÀI -> BẤM VÀO ĐỂ HIỆN LỜI GIẢI CHI TIẾT)
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Ví Dụ Minh Họa Chuẩn Mực: {sel_topic}")
    st.caption("Danh sách 3 đến 4 ví dụ trọng tâm bám sát Vở tự học (loại bỏ bài chứa tham số m và bài vận dụng cao). Bấm vào từng đề bài để xem lời giải chi tiết và học cách trình bày.")

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
