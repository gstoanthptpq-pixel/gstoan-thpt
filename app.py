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
# 1. THIẾT LẬP CẤU HÌNH & GIAO DIỆN SƯ PHẠM
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
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
    .rule-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 10px 14px;
        border-radius: 8px;
        margin-bottom: 12px;
        font-size: 14px;
    }
    .audio-box {
        background: linear-gradient(135deg, #F0FDF4, #DCFCE7);
        border: 1px solid #86EFAC;
        padding: 12px;
        border-radius: 10px;
        margin-top: 10px;
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
# 3. KHO HỌC LIỆU SỐ CHÍNH THỨC TRÍCH XUẤT TỪ VỞ TỰ HỌC TOÁN 10, 11, 12
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 10": {
        "Bài 1: Mệnh đề toán học": {
            "chapter": "Chương I: Mệnh đề và Tập hợp",
            "video_title": "Bài giảng Vi mô: Bản chất Mệnh đề & Phủ định mệnh đề chứa lượng từ",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong Vở tự học Toán 10, em cần nắm vững: Mệnh đề toán học là một khẳng định đúng hoặc sai, tuyệt đối không thể vừa đúng vừa sai. Khi phủ định mệnh đề chứa lượng từ với mọi, ta đổi thành tồn tại, dấu lớn hơn đổi thành dấu nhỏ hơn hoặc bằng. Nhớ đừng bao giờ bỏ quên dấu bằng khi phủ định bất đẳng thức nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Mệnh đề:** Khẳng định có chân giá trị hoặc Đúng hoặc Sai.
- **Phủ định mệnh đề chứa lượng từ:**
  + Phủ định của $\forall x \in X, P(x)$ là $\exists x \in X, \overline{P(x)}$.
  + Phủ định của $\exists x \in X, P(x)$ là $\forall x \in X, \overline{P(x)}$.
- ⚠️ *Bẫy sai lầm:* Phủ định của $>$ là $\le$; phủ định của $\ge$ là $<$.
            """,
            "exercise": {
                "id": "VTH_10_B1",
                "title": "Bài tập 1 (Trích Vở tự học Toán 10 - Chương I)",
                "content": r"Cho mệnh đề $P$: '$\forall x \in \mathbb{R}, x^2 - 2x + 5 > 0$'. Hỏi mệnh đề phủ định $\overline{P}$ có dạng nào và nhận chân giá trị là Đúng hay Sai?",
                "question_type": "CHOICE",
                "options": [
                    "A. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 \\le 0$ (Chân giá trị: Sai)",
                    "B. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 < 0$ (Chân giá trị: Đúng)",
                    "C. $\\overline{P}: \\forall x \\in \\mathbb{R}, x^2 - 2x + 5 \\le 0$ (Chân giá trị: Sai)",
                    "D. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 \\ge 0$ (Chân giá trị: Đúng)"
                ],
                "target_val": "A",
                "hint_1": "Quy tắc: $\\forall$ chuyển thành $\\exists$, dấu $>$ chuyển thành $\\le$.",
                "hint_2": "Biến đổi tam thức: $x^2 - 2x + 5 = (x-1)^2 + 4 \\ge 4 > 0, \\forall x$. Mệnh đề $P$ luôn đúng.",
                "hint_3": "Do $P$ đúng nên mệnh đề phủ định $\\overline{P}$ nhận chân giá trị Sai.",
                "solution_text": "Phủ định của 'với mọi' là 'tồn tại', phủ định của '>' là '<='. Vì x^2 - 2x + 5 luôn dương với mọi x nên mệnh đề phủ định là Sai."
            }
        },
        "Bài 2: Hệ bất phương trình bậc nhất hai ẩn": {
            "chapter": "Chương II: Bất phương trình bậc nhất hai ẩn",
            "video_title": "Bài giảng Vi mô: Biểu diễn miền nghiệm & Bài toán quy hoạch tối ưu",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Để tìm miền nghiệm của hệ bất phương trình bậc nhất hai ẩn, ta vẽ từng đường thẳng biên và dùng điểm thử O(0;0) để xác định nửa mặt phẳng phù hợp. Với bài toán tối ưu thực tế, giá trị lớn nhất hoặc nhỏ nhất của hàm mục tiêu luôn luôn đạt tại một trong các đỉnh của miền đa giác nghiệm!",
            "has_3d": False,
            "smart_notes": r"""
- Bất phương trình bậc nhất hai ẩn: $ax + by \le c$.
- **Quy tắc miền nghiệm:** Điểm thử $O(0;0)$ thỏa mãn thì nửa mặt phẳng chứa $O$ là miền nghiệm.
- **Tối ưu hóa $F(x; y) = ax + by$:** Giá trị lớn nhất/nhỏ nhất luôn đạt tại một trong các đỉnh của miền đa giác nghiệm.
            """,
            "exercise": {
                "id": "VTH_10_B2",
                "title": "Bài tập 2 (Trích Vở tự học Toán 10 - Chương II)",
                "content": r"Cho hệ bất phương trình: $\begin{cases} x + y \le 4 \\ x \ge 0 \\ y \ge 0 \end{cases}$. Tìm giá trị lớn nhất $F_{\max}$ của biểu thức $F(x; y) = 3x + 2y$ trên miền nghiệm này.",
                "question_type": "NUMERIC",
                "target_val": "12",
                "hint_1": "Miền nghiệm là tam giác vuông OAB với $O(0;0), A(4;0), B(0;4)$.",
                "hint_2": "Tính giá trị của $F$ tại từng đỉnh: $F(0;0)=0, F(0;4)=8, F(4;0)=12$.",
                "hint_3": "So sánh 3 giá trị để xác định giá trị lớn nhất.",
                "solution_text": "F(4;0) = 3*(4) + 2*(0) = 12. Vậy giá trị lớn nhất F_max = 12 đạt tại đỉnh A(4;0)."
            }
        },
        "Bài 3: Hệ thức lượng trong tam giác": {
            "chapter": "Chương IV: Hệ thức lượng trong tam giác",
            "video_title": "Bài giảng Vi mô: Định lý Côsin, Định lý Sin & Công thức diện tích",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong tam giác bất kỳ, biết hai cạnh và góc xen giữa ta dùng định lý Côsin tính cạnh còn lại. Biết một cạnh và hai góc kề, ta dùng định lý Sin. Công thức tính diện tích nhanh nhất là lấy một nửa tích hai cạnh nhân sin góc xen giữa!",
            "has_3d": False,
            "smart_notes": r"""
- **Định lý Côsin:** $a^2 = b^2 + c^2 - 2bc \cos A$.
- **Định lý Sin:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$.
- **Diện tích:** $S = \frac{1}{2}ab \sin C = \frac{abc}{4R} = pr$.
            """,
            "exercise": {
                "id": "VTH_10_B3",
                "title": "Bài tập 3 (Trích Vở tự học Toán 10 - Chương IV)",
                "content": r"Cho tam giác $ABC$ có cạnh $b = 8$, cạnh $c = 5$ và góc xen giữa $\widehat{A} = 60^\circ$. Tính chính xác độ dài cạnh $a$.",
                "question_type": "NUMERIC",
                "target_val": "7",
                "hint_1": "Áp dụng định lý Côsin: $a^2 = b^2 + c^2 - 2bc\cos A$.",
                "hint_2": "Thay số: $a^2 = 8^2 + 5^2 - 2 \cdot 8 \cdot 5 \cdot \cos(60^\circ) = 64 + 25 - 40 = 49$.",
                "hint_3": "Khai căn: $a = \sqrt{49} = 7$.",
                "solution_text": "a^2 = 64 + 25 - 40 = 49 => a = 7."
            }
        }
    },
    "Khối 11": {
        "Bài 1: Giá trị lượng giác của góc lượng giác": {
            "chapter": "Chương I: Hàm số lượng giác và Phương trình lượng giác",
            "video_title": "Bài giảng Vi mô: Trục Sin/Cos trên đường tròn lượng giác & Dấu các góc phần tư",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong Vở tự học Toán 11, em hãy nhớ quy tắc xét dấu: Góc phần tư thứ nhất, tất cả đều dương. Góc phần tư thứ hai, chỉ có sin dương, còn cos và tan đều âm. Khi tính cos từ sin, em dùng hệ thức sin bình cộng cos bình bằng 1, và nhớ xét dấu âm cho cos ở góc phần tư thứ hai!",
            "has_3d": False,
            "smart_notes": r"""
- **Hệ thức cơ bản:** $\sin^2\alpha + \cos^2\alpha = 1$; $\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$; $1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}$.
- **Dấu theo góc phần tư:**
  + Góc I ($0 < \alpha < \frac{\pi}{2}$): $\sin > 0, \cos > 0, \tan > 0$.
  + Góc II ($\frac{\pi}{2} < \alpha < \pi$): $\sin > 0, \cos < 0, \tan < 0$.
  + Góc III ($\pi < \alpha < \frac{3\pi}{2}$): $\sin < 0, \cos < 0, \tan > 0$.
  + Góc IV ($\frac{3\pi}{2} < \alpha < 2\pi$): $\cos > 0, \sin < 0, \tan < 0$.
            """,
            "exercise": {
                "id": "VTH_11_B1",
                "title": "Bài tập 1 (Trích Vở tự học Toán 11 - Chương I)",
                "content": r"Cho góc lượng giác $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$ và $\sin\alpha = \frac{3}{5}$. Hãy tính giá trị của $\cos\alpha$ (điền số thập phân hoặc phân số, ví dụ: -0.8).",
                "question_type": "NUMERIC",
                "target_val": "-0.8",
                "alt_vals": ["-4/5", "-0,8"],
                "hint_1": "Áp dụng hệ thức $\cos^2\alpha = 1 - \sin^2\alpha = 1 - \frac{9}{25} = \frac{16}{25}$.",
                "hint_2": "Vì góc $\alpha$ thuộc góc phần tư thứ II nên $\cos\alpha < 0$.",
                "hint_3": "Do đó $\cos\alpha = -\sqrt{\frac{16}{25}} = -0.8$.",
                "solution_text": "cos^2(alpha) = 1 - 9/25 = 16/25. Do pi/2 < alpha < pi nên cos(alpha) < 0 => cos(alpha) = -4/5 = -0.8."
            }
        },
        "Bài 2: Ứng dụng lượng giác giải toán thực tế": {
            "chapter": "Chương I: Hàm số lượng giác và Phương trình lượng giác",
            "video_title": "Bài giảng Vi mô: Giải toán mô hình hóa chuyển động ném tạ & Dòng điện xoay chiều",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Vở tự học Toán 11 giới thiệu bài toán mô hình hóa thực tế rất hay: Tầm xa khi ném tạ được tính theo công thức L bằng v không bình phương nhân sin hai alpha chia g. Khi bài toán cho trước tầm xa, vận tốc ban đầu và gia tốc trọng trường, ta rút ra phương trình lượng giác để tìm góc ném tối ưu. Hãy biến đổi cẩn thận để tìm góc ném nhỏ nhất nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Tầm xa chuyển động ném xiên:** $L = \frac{v_0^2 \sin(2\alpha)}{g}$ với $0^\circ < \alpha < 90^\circ$.
- **Cường độ dòng điện xoay chiều:** $i(t) = a\sin(\omega t) + b\cos(\omega t)$ có giá trị cực đại là $I_{\max} = \sqrt{a^2 + b^2}$.
            """,
            "exercise": {
                "id": "VTH_11_B2_REAL",
                "title": "Bài toán thực tế Câu 9 (Trang 15 - Vở tự học Toán 11)",
                "content": r"Một vận động viên ném một quả tạ xiên từ mặt đất với vận tốc đầu $v_0 = 14\text{ m/s}$. Bỏ qua sức cản không khí, tầm xa của quả tạ là $L = \frac{v_0^2 \sin 2\alpha}{g}$ với $g = 9.8\text{ m/s}^2$. Để quả tạ rơi cách vị trí ném đúng $10\text{ m}$ thì góc ném $\alpha$ nhỏ nhất bằng bao nhiêu độ? (Làm tròn đến phần nguyên độ).",
                "question_type": "NUMERIC",
                "target_val": "15",
                "alt_vals": ["15 độ", "15°"],
                "hint_1": "Thay số: $10 = \frac{14^2 \sin 2\alpha}{9.8} = \frac{196 \sin 2\alpha}{9.8} = 20 \sin 2\alpha$.",
                "hint_2": "Suy ra $\sin 2\alpha = \frac{10}{20} = 0.5$.",
                "hint_3": "Do đó $2\alpha = 30^\circ \Rightarrow \alpha = 15^\circ$.",
                "solution_text": "Ta có 10 = (14^2 * sin(2*alpha)) / 9.8 <=> 10 = 20*sin(2*alpha) <=> sin(2*alpha) = 0.5 => 2*alpha = 30 độ => alpha = 15 độ."
            }
        },
        "Bài 3: Đường thẳng vuông góc với mặt phẳng": {
            "chapter": "Chương IV: Quan hệ vuông góc trong không gian",
            "video_title": "Bài giảng Vi mô: Phương pháp xác định góc giữa đường thẳng và mặt phẳng",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Để tìm góc giữa đường thẳng và mặt phẳng, ta tìm giao điểm trước, sau đó hạ hình chiếu vuông góc từ đỉnh còn lại xuống mặt đáy. Góc cần tìm chính là góc giữa đường thẳng ban đầu và hình chiếu của nó. Hãy sử dụng mô hình 3D tương tác bên dưới để quan sát rõ góc này trong không gian nhé!",
            "has_3d": True,
            "smart_notes": r"""
- **Quy tắc xác định góc:**
  1. Giao điểm $A = d \cap (P)$.
  2. Hình chiếu vuông góc $H$ của $S \in d$ lên $(P)$ ($SH \perp (P)$).
  3. Góc $\varphi = \widehat{(d, (P))} = \widehat{SAH}$.
            """,
            "exercise": {
                "id": "VTH_11_B3",
                "title": "Bài tập 3 (Trích Vở tự học Toán 11 - Chương IV)",
                "content": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$, $AB = a$. Cạnh bên $SA \perp (ABC)$ và $SA = a$. Tính góc giữa cạnh bên $SB$ và mặt phẳng đáy $(ABC)$ (nhập số độ, ví dụ: 45).",
                "question_type": "NUMERIC",
                "target_val": "45",
                "hint_1": "Giao điểm của $SB$ và đáy là $B$. Điểm $S$ có hình chiếu lên đáy là $A$.",
                "hint_2": "Hình chiếu của $SB$ lên đáy là $AB$. Góc cần tìm là $\widehat{SBA}$.",
                "hint_3": "Tam giác $SAB$ vuông tại $A$ có $SA = AB = a$ (vuông cân), suy ra $\widehat{SBA} = 45^\circ$.",
                "solution_text": "Hình chiếu của SB lên đáy là AB. Tam giác SAB vuông cân tại A nên góc SBA = 45 độ."
            }
        }
    },
    "Khối 12": {
        "Bài 1: Tính đơn điệu và Cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "video_title": "Bài giảng Vi mô: Bảng biến thiên, dấu đạo hàm y' và cực trị hàm số chuẩn 2025+",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Khảo sát hàm số trong Vở tự học Toán 12 yêu cầu phân biệt rõ: Điểm cực trị của hàm số là x, giá trị cực trị là y, và điểm cực trị của đồ thị là cặp điểm M(x; y). Đạo hàm y phẩy đổi dấu từ dương sang âm ta có cực đại, từ âm sang dương ta có cực tiểu!",
            "has_3d": False,
            "smart_notes": r"""
- **Cực trị:** $f'(x_0) = 0$ và đổi dấu qua $x_0$:
  + Đổi dấu $(+) \rightarrow (-)$: Điểm cực đại.
  + Đổi dấu $(-) \rightarrow (+)$: Điểm cực tiểu.
- ⚠️ *Phân biệt thuật ngữ:*
  + Điểm cực trị của hàm số: $x_0$.
  + Giá trị cực trị của hàm số: $y_0 = f(x_0)$.
  + Điểm cực trị của đồ thị: $M(x_0; y_0)$.
            """,
            "exercise": {
                "id": "VTH_12_B1",
                "title": "Bài tập 1 (Trang 18 - Vở tự học Toán 12)",
                "content": r"Cho hàm số $y = x^3 - 3x + 2$. Tìm giá trị cực tiểu ($y_{CT}$) của hàm số đã cho.",
                "question_type": "NUMERIC",
                "target_val": "0",
                "hint_1": "Tính đạo hàm: $y' = 3x^2 - 3 = 0 \Leftrightarrow x = 1$ hoặc $x = -1$.",
                "hint_2": "Lập bảng xét dấu: tại $x = 1$, đạo hàm đổi dấu từ âm sang dương nên $x = 1$ là điểm cực tiểu.",
                "hint_3": "Thay $x = 1$ vào hàm số ban đầu: $y_{CT} = 1^3 - 3(1) + 2 = 0$.",
                "solution_text": "y' = 3x^2 - 3 = 0 <=> x = +-1. Tại x = 1, y' đổi dấu từ âm sang dương nên hàm số đạt cực tiểu tại x = 1. Giá trị cực tiểu y_CT = 1 - 3 + 2 = 0."
            }
        },
        "Bài 2: Giá trị lớn nhất, nhỏ nhất & Tối ưu thực tiễn": {
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "video_title": "Bài giảng Vi mô: Giải toán tối ưu diện tích hộp và chi phí sản xuất trung bình",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong Trang 18 Vở tự học Toán 12 có bài toán kinh điển: Làm chiếc hộp không nắp đáy hình vuông có thể tích 32 dm khối. Khi đặt cạnh đáy là x thì chiều cao là 32 chia x bình phương. Biểu thức diện tích toàn phần là x bình cộng 128 chia x. Lấy đạo hàm và giải nghiệm bằng 0, ta tìm được cạnh đáy x bằng 4 và diện tích vật liệu nhỏ nhất bằng 48 dm vuông!",
            "has_3d": False,
            "smart_notes": r"""
- **Bài toán hộp không nắp đáy vuông:**
  + Thể tích: $V = x^2 h = 32 \Rightarrow h = \frac{32}{x^2}$.
  + Diện tích vật liệu: $S(x) = x^2 + 4xh = x^2 + \frac{128}{x}$.
  + Đạo hàm: $S'(x) = 2x - \frac{128}{x^2} = 0 \Leftrightarrow x^3 = 64 \Leftrightarrow x = 4$.
  + Diện tích nhỏ nhất: $S(4) = 4^2 + \frac{128}{4} = 16 + 32 = 48\text{ dm}^2$.
            """,
            "exercise": {
                "id": "VTH_12_P3_C1",
                "title": "Phần 3 - Câu 1 (Trang 18 - Vở tự học Toán 12)",
                "content": r"Người ta cần làm một chiếc hộp không nắp có đáy là hình vuông và thể tích bằng $32\text{ dm}^3$. Hỏi diện tích vật liệu cần dùng (tổng diện tích đáy và bốn mặt bên) nhỏ nhất bằng bao nhiêu $\text{dm}^2$?",
                "question_type": "NUMERIC",
                "target_val": "48",
                "alt_vals": ["48 dm2", "48dm2"],
                "hint_1": "Gọi cạnh đáy hình vuông là $x > 0$, chiều cao là $h > 0$. Ta có $V = x^2 h = 32 \Rightarrow h = \frac{32}{x^2}$.",
                "hint_2": "Diện tích vật liệu cần dùng là $S(x) = x^2 + 4xh = x^2 + \frac{128}{x}$.",
                "hint_3": "Tính đạo hàm: $S'(x) = 2x - \frac{128}{x^2} = 0 \Leftrightarrow x^3 = 64 \Leftrightarrow x = 4$. Thay $x = 4$ vào $S(x)$.",
                "solution_text": "S(x) = x^2 + 128/x. S'(x) = 2x - 128/x^2 = 0 <=> x = 4. Diện tích nhỏ nhất là S(4) = 16 + 32 = 48 dm2."
            }
        },
        "Bài 3: Đường tiệm cận của đồ thị hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "video_title": "Bài giảng Vi mô: Nhận diện nhanh tiệm cận đứng, ngang & Tiệm cận xiên",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Đường tiệm cận của đồ thị hàm số là một nội dung trọng tâm trong đề thi tốt nghiệp THPT. Tiệm cận đứng xuất hiện tại các điểm làm mẫu số triệt tiêu mà tử số khác không. Tiệm cận ngang xác định bởi giới hạn khi x tiến tới cộng hoặc trừ vô cùng. Nhớ chú ý hàm phân thức bậc hai trên bậc nhất sẽ có tiệm cận xiên em nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Tiệm cận đứng:** $x = x_0$ nếu ít nhất một trong các giới hạn $\lim_{x \to x_0^\pm} f(x) = \pm\infty$.
- **Tiệm cận ngang:** $y = y_0$ nếu $\lim_{x \to +\infty} f(x) = y_0$ hoặc $\lim_{x \to -\infty} f(x) = y_0$.
- **Hàm nhất biến:** $y = \frac{ax+b}{cx+d}$ có TCĐ $x = -\frac{d}{c}$, TCN $y = \frac{a}{c}$.
            """,
            "exercise": {
                "id": "VTH_12_B3_TC",
                "title": "Phần 2 - Câu 1 (Trang 25 - Vở tự học Toán 12)",
                "content": r"Cho hàm số $f(x) = \frac{2x - 3}{x + 1}$. Tọa độ giao điểm của tiệm cận đứng và tiệm cận ngang của đồ thị hàm số là điểm nào?",
                "question_type": "CHOICE",
                "options": [
                    "A. $I(-1; 2)$",
                    "B. $I(1; 2)$",
                    "C. $I(-1; -3)$",
                    "D. $I(2; -1)$"
                ],
                "target_val": "A",
                "hint_1": "Tìm phương trình tiệm cận đứng: nghiệm của mẫu $x + 1 = 0 \Rightarrow x = -1$.",
                "hint_2": "Tìm phương trình tiệm cận ngang: bậc tử bằng bậc mẫu nên $y = \frac{2}{1} = 2$.",
                "hint_3": "Giao điểm của hai đường thẳng $x = -1$ và $y = 2$ là điểm $I(-1; 2)$.",
                "solution_text": "Tiệm cận đứng x = -1, tiệm cận ngang y = 2. Giao điểm là I(-1; 2)."
            }
        },
        "Bài 4: Tọa độ và Mô hình hóa Vectơ Oxyz trong không gian": {
            "chapter": "Chương II: Vectơ và Hệ trục tọa độ trong không gian",
            "video_title": "Bài giảng Vi mô: Mô hình hóa tọa độ Radar quét máy bay & Vận tốc chuyển động",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong Trang 132 Vở tự học Toán 12, chúng ta có bài toán mô hình hóa thực tế rất hay về radar: Một trạm radar đặt tại gốc tọa độ phát hiện các vật thể trong bán kính 10 km. Biên vùng quét chính là phương trình mặt cầu x bình cộng y bình cộng z bình bằng 100. Muốn kiểm tra máy bay có nằm trong vùng quét hay không, em tính khoảng cách từ điểm đến gốc tọa độ rồi so sánh với bán kính 10 km!",
            "has_3d": True,
            "smart_notes": r"""
- **Tọa độ điểm & vectơ:** $\vec{u} = (x; y; z) \Leftrightarrow \vec{u} = x\vec{i} + y\vec{j} + z\vec{k}$.
- **Mặt cầu:** $(S): (x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$.
- **Bài toán Radar:** Biên vùng quét đặt tại gốc $O(0;0;0)$ bán kính $R = 10\text{ km}$ là $x^2 + y^2 + z^2 \le 100$.
            """,
            "exercise": {
                "id": "VTH_12_P2_RADAR",
                "title": "Phần 2 - Câu 2 (Trang 132 - Vở tự học Toán 12)",
                "content": r"Một trạm radar đặt tại gốc tọa độ $O$ phát hiện các vật thể trong bán kính $10\text{ km}$ (mặt phẳng $Oxy$ là mặt đất). Một máy bay ở vị trí $B(7; 6; 5)$. Khoảng cách từ máy bay $B$ đến trạm radar bằng bao nhiêu (km, làm tròn 2 chữ số thập phân)? Máy bay có nằm trong vùng quét không?",
                "question_type": "NUMERIC",
                "target_val": "10.49",
                "alt_vals": ["10.5", "10,49"],
                "hint_1": "Khoảng cách từ gốc $O(0;0;0)$ đến $B(7;6;5)$ là $OB = \sqrt{7^2 + 6^2 + 5^2}$.",
                "hint_2": "Tính toán: $OB = \sqrt{49 + 36 + 25} = \sqrt{110} \approx 10.49\text{ km}$.",
                "hint_3": "Do $10.49 > 10$ nên máy bay nằm ngoài vùng quét radar.",
                "solution_text": "OB = sqrt(7^2 + 6^2 + 5^2) = sqrt(110) ≈ 10.49 km. Do 10.49 > 10 km nên máy bay không nằm trong vùng quét."
            }
        },
        "Bài 5: Ứng dụng hình học của Tích phân": {
            "chapter": "Chương IV: Nguyên hàm và Tích phân",
            "video_title": "Bài giảng Vi mô: Tính diện tích hình phẳng giới hạn bởi Parabol & Trục hoành",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong Trang 103 Vở tự học Toán 12, để tính diện tích hình phẳng giới hạn bởi parabol và trục hoành, bước đầu tiên là em giải phương trình hoành độ giao điểm để tìm hai cận tích phân. Sau đó lấy tích phân giá trị tuyệt đối. Hãy tính cẩn thận bài tập 4 trang 103 bên dưới để rèn luyện nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Diện tích hình phẳng giới hạn bởi đồ thị $y = f(x)$ và trục $Ox$:**
  $S = \int_a^b |f(x)| dx$.
- Với parabol $y = x^2 - 4x$, giao điểm với $Ox$ là $x = 0$ và $x = 4$.
- $S = \int_0^4 |x^2 - 4x| dx = \int_0^4 (4x - x^2) dx = \left[ 2x^2 - \frac{x^3}{3} \right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3}$.
            """,
            "exercise": {
                "id": "VTH_12_P1_C4_T103",
                "title": "Phần 1 - Câu 4 (Trang 103 - Vở tự học Toán 12)",
                "content": r"Diện tích hình phẳng giới hạn bởi parabol $y = x^2 - 4x$ và trục hoành $Ox$ bằng bao nhiêu? (Nhập phân số dạng a/b hoặc số thập phân làm tròn 2 chữ số, ví dụ: 32/3 hoặc 10.67).",
                "question_type": "NUMERIC",
                "target_val": "32/3",
                "alt_vals": ["10.67", "10,67"],
                "hint_1": "Phương trình hoành độ giao điểm: $x^2 - 4x = 0 \Leftrightarrow x = 0$ hoặc $x = 4$.",
                "hint_2": "Diện tích: $S = \int_0^4 |x^2 - 4x| dx = \int_0^4 (4x - x^2) dx$.",
                "hint_3": "Tính tích phân: $\left[2x^2 - \frac{x^3}{3}\right]_0^4 = 32 - \frac{64}{3} = \frac{32}{3}$.",
                "solution_text": "Phương trình hoành độ giao điểm có nghiệm 0 và 4. S = tích phân từ 0 đến 4 của (4x - x^2)dx = [2x^2 - x^3/3]_0^4 = 32/3 ≈ 10.67."
            }
        }
    }
}

# ==============================================================================
# 4. KHO ĐỀ KHẢO THÍ CHUẨN MA TRẬN MỚI CỦA BỘ GD&ĐT
# ==============================================================================
EXAM_BANK = {
    "Khối 10": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 10",
            "p1": [
                {"q": r"Mệnh đề nào sau đây là mệnh đề toán học?", "ops": ["A. $2 + 3 = 6$", "B. Thời tiết hôm nay mát mẻ quá!", "C. Bạn có thích học Toán không?", "D. Hãy mở trang 10 sách giáo khoa."], "ans": "A", "exp": "A là câu khẳng định có chân giá trị sai, là mệnh đề toán học."}
            ],
            "p2": [
                {
                    "q": r"Cho tam thức bậc hai $f(x) = x^2 - 4x + 3$. Xét tính Đúng/Sai của các mệnh đề sau:",
                    "items": [
                        ("a) Phương trình f(x) = 0 có hai nghiệm phân biệt là x = 1 và x = 3.", True, "Delta' = 4 - 3 = 1 > 0, nghiệm là x = 1 và x = 3."),
                        ("b) f(x) < 0 với mọi x thuộc khoảng (1; 3).", True, "Trong khoảng hai nghiệm f(x) trái dấu với hệ số a = 1 > 0."),
                        ("c) Đỉnh của parabol đồ thị hàm số có tọa độ I(2; 1).", False, "Đỉnh parabol x = 2, y = f(2) = -1. Tọa độ đúng là I(2; -1)."),
                        ("d) f(0) = 3.", True, "Thay x = 0 được f(0) = 3.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Cho tam giác ABC có AB = 6, AC = 8 và góc A = 60 độ. Tính độ dài cạnh BC.", "ans": "7.21", "alt": ["7.2", "52^0.5"], "exp": "BC^2 = 6^2 + 8^2 - 2*6*8*cos(60°) = 52 => BC ≈ 7.21"}
            ]
        },
        "Cuối học kỳ 1": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 1 - TOÁN 10",
            "p1": [
                {"q": r"Cho hai vectơ $\vec{a} = (1; 2)$ và $\vec{b} = (-2; 3)$. Tích vô hướng $\vec{a} \cdot \vec{b}$ bằng:", "ops": ["A. 4", "B. -8", "C. 8", "D. 0"], "ans": "A", "exp": "1*(-2) + 2*3 = -2 + 6 = 4."}
            ],
            "p2": [
                {
                    "q": r"Cho hình vuông ABCD cạnh a. Xét tính Đúng/Sai của các khẳng định sau:",
                    "items": [
                        ("a) Độ dài vectơ AB bằng a.", True, "Độ dài vectơ cạnh hình vuông."),
                        ("b) Tích vô hướng của vectơ AB và AD bằng 0.", True, "Do AB vuông góc AD."),
                        ("c) Vectơ AC cùng hướng với vectơ BD.", False, "Hai đường chéo cắt nhau, không cùng hướng."),
                        ("d) Độ dài vectơ AC bằng a nhân căn 2.", True, "Đường chéo hình vuông cạnh a.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tính khoảng cách từ điểm M(1; 2) đến đường thẳng d: 3x - 4y + 15 = 0.", "ans": "2", "alt": ["2.0"], "exp": "d = |3(1) - 4(2) + 15| / sqrt(3^2 + 4^2) = 10 / 5 = 2."}
            ]
        },
        "Giữa học kỳ 2": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 2 - TOÁN 10",
            "p1": [
                {"q": r"Phương trình $\sqrt{x^2 - 3x + 2} = x - 1$ có bao nhiêu nghiệm thực?", "ops": ["A. 1", "B. 2", "C. 0", "D. Vô số"], "ans": "A", "exp": "Bình phương hai vế với x >= 1: x^2 - 3x + 2 = x^2 - 2x + 1 <=> x = 1 (thỏa mãn)."}
            ],
            "p2": [
                {
                    "q": r"Cho đường thẳng Delta: 3x - 4y + 1 = 0. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Vectơ pháp tuyến của đường thẳng là n = (3; -4).", True, "Tọa độ hệ số trước x, y."),
                        ("b) Vectơ chỉ phương của đường thẳng là u = (4; 3).", True, "Tích vô hướng với pháp tuyến bằng 0."),
                        ("c) Điểm A(1; 1) thuộc đường thẳng Delta.", True, "3(1) - 4(1) + 1 = 0 thỏa mãn."),
                        ("d) Đường thẳng Delta đi qua gốc tọa độ O(0;0).", False, "3(0) - 4(0) + 1 = 1 khác 0.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tính góc giữa hai đường thẳng d1: x + y = 0 và d2: x - y + 5 = 0 (nhập số độ).", "ans": "90", "alt": ["90 độ"], "exp": "Hai vectơ pháp tuyến vuông góc nên góc bằng 90 độ."}
            ]
        },
        "Cuối học kỳ 2": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 2 - TOÁN 10",
            "p1": [
                {"q": r"Có bao nhiêu cách xếp 5 bạn học sinh ngồi vào một hàng ngang 5 ghế?", "ops": ["A. 120", "B. 24", "C. 720", "D. 25"], "ans": "A", "exp": "Số hoán vị P_5 = 5! = 120."}
            ],
            "p2": [
                {
                    "q": r"Gieo một đồng xu cân đối 3 lần liên tiếp. Xét tính Đúng/Sai của các biến cố:",
                    "items": [
                        ("a) Không gian mẫu có 8 phần tử.", True, "2^3 = 8 phần tử."),
                        ("b) Xác suất để 3 lần đều xuất hiện mặt sấp là 1/8.", True, "Chỉ có 1 kết quả SSS trong 8 kết quả."),
                        ("c) Xác suất để có ít nhất một lần xuất hiện mặt ngửa là 7/8.", True, "Biến cố đối là 1 - 1/8 = 7/8."),
                        ("d) Biến cố 'xuất hiện 2 mặt ngửa' có xác suất 1/2.", False, "Có 3 kết quả nên xác suất là 3/8 khác 1/2.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tìm hệ số của x^3 trong khai triển nhị thức Newton của (x + 2)^4.", "ans": "8", "alt": ["8.0"], "exp": "Số hạng: C(4, 1)*x^3*2^1 = 8x^3. Hệ số là 8."}
            ]
        }
    },
    "Khối 11": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 11",
            "p1": [
                {"q": r"Tập xác định của hàm số $y = \tan(x)$ là:", "ops": [r"A. $D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\}$", r"B. $D = \mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$", r"C. $D = \mathbb{R}$", r"D. $D = [-1; 1]$"], "ans": "A", "exp": "Điều kiện cos(x) khác 0."}
            ],
            "p2": [
                {
                    "q": r"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 2$ và công sai $d = 3$. Xét tính Đúng/Sai của các mệnh đề:",
                    "items": [
                        ("a) Số hạng thứ hai u_2 = 5.", True, "u_2 = 2 + 3 = 5."),
                        ("b) Công thức số hạng tổng quát là u_n = 3n - 1.", True, "u_n = 2 + (n-1)*3 = 3n - 1."),
                        ("c) Số 20 là một số hạng của cấp số cộng trên.", True, "3n - 1 = 20 <=> n = 7 nguyên dương."),
                        ("d) Tổng 10 số hạng đầu tiên S_10 = 155.", True, "S_10 = 10*(2*2 + 9*3)/2 = 155.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một rạp hát có 12 hàng ghế. Hàng đầu có 15 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Tính tổng số ghế của rạp.", "ans": "312", "alt": ["312 ghế"], "exp": "S_12 = 12*(2*15 + 11*2)/2 = 312."}
            ]
        },
        "Cuối học kỳ 1": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 1 - TOÁN 11",
            "p1": [
                {"q": r"Giá trị của giới hạn $\lim_{n \to \infty} \frac{4n + 3}{2n - 1}$ bằng:", "ops": ["A. 2", "B. -3", "C. 4", "D. 0"], "ans": "A", "exp": "Chia cả tử và mẫu cho n được 4/2 = 2."}
            ],
            "p2": [
                {
                    "q": r"Cho hình chóp S.ABCD có đáy ABCD là hình bình hành tâm O. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Giao tuyến của hai mặt phẳng (SAC) và (SBD) là đường thẳng SO.", True, "S và O là hai điểm chung."),
                        ("b) Đường thẳng AB song song với mặt phẳng (SCD).", True, "AB song song CD thuộc (SCD)."),
                        ("c) Đường thẳng SO cắt đường thẳng AD.", False, "SO và AD chéo nhau."),
                        ("d) Thiết diện của hình chóp cắt bởi mặt phẳng qua O song song với (SAB) là hình thang.", True, "Mặt phẳng cắt song song mặt bên.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tính giới hạn: $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$.", "ans": "2", "alt": ["2.0"], "exp": "(x-1)(x+1)/(x-1) = x + 1. Thay x = 1 được 2."}
            ]
        },
        "Giữa học kỳ 2": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 2 - TOÁN 11",
            "p1": [
                {"q": r"Đạo hàm của hàm số $y = x^3 - 2x + 1$ là:", "ops": [r"A. $y' = 3x^2 - 2$", r"B. $y' = 3x^2 + 2$", r"C. $y' = x^2 - 2$", r"D. $y' = 3x - 2$"], "ans": "A", "exp": "Đạo hàm: (x^3)' = 3x^2, (-2x)' = -2, 1' = 0."}
            ],
            "p2": [
                {
                    "q": r"Cho hàm số $f(x) = \frac{2x - 1}{x + 1}$. Xét tính Đúng/Sai của các mệnh đề:",
                    "items": [
                        ("a) Tập xác định của hàm số là D = R \\ {-1}.", True, "Mẫu số khác 0 khi x khác -1."),
                        ("b) Đạo hàm f'(x) = 3 / (x+1)^2.", True, "ad - bc = 2*1 - (-1)*1 = 3."),
                        ("c) Hàm số luôn đồng biến trên từng khoảng xác định.", True, "f'(x) > 0 với mọi x khác -1."),
                        ("d) f'(0) = 1.", False, "f'(0) = 3 / 1^2 = 3 khác 1.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một chất điểm chuyển động theo phương trình $s(t) = t^3 - 3t^2 + 2$ (t tính bằng giây, s tính bằng mét). Tính vận tốc tức thời tại thời điểm t = 4 giây (m/s).", "ans": "24", "alt": ["24 m/s"], "exp": "v(t) = s'(t) = 3t^2 - 6t. Tại t = 4: v(4) = 3(16) - 6(4) = 24 m/s."}
            ]
        },
        "Cuối học kỳ 2": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 2 - TOÁN 11",
            "p1": [
                {"q": r"Cho hình lập phương ABCD.A'B'C'D'. Góc giữa hai đường thẳng A'B' và CD bằng:", "ops": ["A. 0 độ", "B. 90 độ", "C. 45 độ", "D. 60 độ"], "ans": "A", "exp": "A'B' song song CD nên góc bằng 0 độ."}
            ],
            "p2": [
                {
                    "q": r"Cho hình chóp S.ABC có SA vuông góc đáy, tam giác ABC vuông tại B. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) SA vuông góc với BC.", True, "SA vuông góc đáy nên vuông góc mọi đường trong đáy."),
                        ("b) BC vuông góc với mặt phẳng (SAB).", True, "BC vuông góc AB và SA."),
                        ("c) Tam giác SBC là tam giác vuông tại B.", True, "BC vuông góc SB."),
                        ("d) Khoảng cách từ S đến mặt phẳng (ABC) bằng độ dài cạnh SB.", False, "Khoảng cách bằng độ dài cạnh SA.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Cho hình chóp tam giác đều S.ABC có cạnh đáy bằng 3, đường cao SH = 4. Tính thể tích khối chóp S.ABC (làm tròn 2 chữ số thập phân).", "ans": "5.2", "alt": ["5.19", "5.20"], "exp": "V = (1/3)*(9*sqrt(3)/4)*4 = 3*sqrt(3) ≈ 5.20."}
            ]
        }
    },
    "Khối 12": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 12",
            "p1": [
                {"q": r"Cho hàm số $y = f(x)$ có bảng biến thiên... Khẳng định nào sau đây đúng về cực trị?", "ops": [r"A. Hàm số đạt cực đại tại $x = 1$", r"B. Hàm số đạt cực đại tại $x = -1$", r"C. Giá trị cực tiểu bằng $1$", r"D. Hàm số không có cực trị"], "ans": "A", "exp": "Đạo hàm đổi dấu từ dương sang âm tại x = 1."}
            ],
            "p2": [
                {
                    "q": r"Cho hàm số $f(x) = x^3 - 3x^2 + 2$. Xét tính Đúng/Sai của các mệnh đề sau:",
                    "items": [
                        ("a) Đạo hàm của hàm số là f'(x) = 3x^2 - 6x.", True, "Đạo hàm chuẩn xác."),
                        ("b) Hàm số đồng biến trên khoảng (0; 2).", False, "f'(x) < 0 trên khoảng (0; 2) nên nghịch biến."),
                        ("c) Điểm cực đại của đồ thị hàm số là điểm A(0; 2).", True, "f'(0) = 0, f(0) = 2, f' đổi dấu + sang -."),
                        ("d) Giá trị cực tiểu của hàm số bằng -2.", True, "Điểm cực tiểu x = 2, f(2) = -2.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tìm giá trị lớn nhất của hàm số $f(x) = x^3 - 3x + 1$ trên đoạn $[0; 2]$.", "ans": "3", "alt": ["3.0"], "exp": "f(0) = 1, f(1) = -1, f(2) = 3. Giá trị lớn nhất là 3."}
            ]
        },
        "Cuối học kỳ 1": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 1 - TOÁN 12",
            "p1": [
                {"q": r"Trong không gian Oxyz, tọa độ của vectơ $\vec{u} = 2\vec{i} - 3\vec{j} + \vec{k}$ là:", "ops": ["A. (2; -3; 1)", "B. (2; 3; 1)", "C. (-2; 3; -1)", "D. (1; -3; 2)"], "ans": "A", "exp": "Hệ số tương ứng trước i, j, k."}
            ],
            "p2": [
                {
                    "q": r"Trong không gian Oxyz, cho mặt cầu $(S): (x-1)^2 + (y+2)^2 + (z-3)^2 = 16$. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Tâm của mặt cầu là điểm I(1; -2; 3).", True, "Tâm đối dấu tọa độ."),
                        ("b) Bán kính của mặt cầu bằng 4.", True, "R = sqrt(16) = 4."),
                        ("c) Điểm O(0; 0; 0) nằm bên trong mặt cầu (S).", True, "(0-1)^2 + (0+2)^2 + (0-3)^2 = 14 < 16 nên nằm trong."),
                        ("d) Diện tích mặt cầu bằng 64pi.", True, "S = 4*pi*R^2 = 64pi.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Trong không gian Oxyz, tính khoảng cách từ điểm A(1; 2; 3) đến mặt phẳng (P): 2x - y + 2z + 1 = 0.", "ans": "3", "alt": ["3.0"], "exp": "d = |2(1) - 2 + 2(3) + 1| / sqrt(2^2 + (-1)^2 + 2^2) = 9 / 3 = 3."}
            ]
        },
        "Giữa học kỳ 2": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 2 - TOÁN 12",
            "p1": [
                {"q": r"Họ nguyên hàm của hàm số $f(x) = 3x^2 + \cos x$ là:", "ops": [r"A. $x^3 + \sin x + C$", r"B. $x^3 - \sin x + C$", r"C. $6x - \sin x + C$", r"D. $x^3 + \cos x + C$"], "ans": "A", "exp": "Nguyên hàm 3x^2 là x^3, nguyên hàm cos x là sin x."}
            ],
            "p2": [
                {
                    "q": r"Cho tích phân $I = \int_0^1 (2x + 1) e^x dx$. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Có thể dùng phương pháp tích phân từng phần để tính I.", True, "Dạng đa thức nhân hàm mũ."),
                        ("b) Đặt u = 2x + 1 thì du = 2dx.", True, "Đạo hàm u chuẩn xác."),
                        ("c) Đặt dv = e^x dx thì chọn v = e^x.", True, "Nguyên hàm e^x là e^x."),
                        ("d) Giá trị của I bằng e + 1.", True, "I = [(2x+1)e^x]_0^1 - 2\int e^x dx = e + 1.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tính diện tích hình phẳng giới hạn bởi parabol $y = x^2$ và đường thẳng $y = 2x$.", "ans": "1.33", "alt": ["4/3", "1.3"], "exp": "S = \int_0^2 (2x - x^2) dx = 4/3 ≈ 1.33."}
            ]
        },
        "Cuối học kỳ 2": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 2 - TOÁN 12",
            "p1": [
                {"q": r"Phương sai của mẫu số liệu ghép nhóm đo lường đặc trưng nào?", "ops": ["A. Độ phân tán của số liệu quanh số trung bình", "B. Giá trị trung tâm xuất hiện nhiều nhất", "C. Giá trị trung bình", "D. Khoảng biến thiên"], "ans": "A", "exp": "Đặc trưng độ phân tán."}
            ],
            "p2": [
                {
                    "q": r"Trong không gian Oxyz, cho đường thẳng d: (x-1)/2 = (y+2)/-1 = (z-3)/1. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Đường thẳng d đi qua điểm M(1; -2; 3).", True, "Tọa độ thỏa mãn phương trình chính tắc."),
                        ("b) Một vectơ chỉ phương của d là u = (2; -1; 1).", True, "Các hệ số dưới mẫu."),
                        ("c) Điểm A(3; -3; 4) thuộc đường thẳng d.", True, "Thay vào thỏa mãn dấu bằng."),
                        ("d) d vuông góc với mặt phẳng (P): 2x - y + z + 5 = 0.", True, "Vectơ chỉ phương của d cùng phương với pháp tuyến (P).")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một hộp chứa 5 viên bi đỏ và 4 viên bi xanh. Lấy ngẫu nhiên 3 viên bi. Tính xác suất để lấy được đúng 2 viên bi đỏ (làm tròn 2 chữ số thập phân).", "ans": "0.48", "alt": ["10/21", "0.476"], "exp": "C(5, 2)*C(4, 1) / C(9, 3) = 40/84 = 10/21 ≈ 0.48."}
            ]
        },
        "🏛️ Ôn thi Tốt nghiệp THPT (Cấu trúc mới)": {
            "title": "ĐỀ KHẢO THÍ CHUẨN ĐỊNH DẠNG TỐT NGHIỆP THPT (BỘ GD&ĐT MỚI)",
            "p1": [
                {"q": r"Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x-1)^2 (x+2)^3$. Số điểm cực trị của hàm số đã cho là:", "ops": ["A. 2", "B. 3", "C. 1", "D. 0"], "ans": "A", "exp": "f'(x) đổi dấu khi qua nghiệm bội lẻ x = 0 và x = -2 (bội 3). Nghiệm x = 1 là bội chẵn không đổi dấu. Vậy có đúng 2 điểm cực trị."}
            ],
            "p2": [
                {
                    "q": r"Cho hình chóp tam giác đều $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. Cạnh bên tạo với mặt đáy góc $60^\circ$. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Hình chiếu vuông góc của S lên (ABC) trùng với trọng tâm tam giác ABC.", True, "Tính chất hình chóp đều."),
                        ("b) Độ dài đường cao hình chóp bằng a.", True, "h = (a*sqrt(3)/3)*tan(60°) = a."),
                        ("c) Thể tích khối chóp S.ABC bằng a^3 / 4.", False, "V = a^3*sqrt(3)/12 khác a^3/4."),
                        ("d) Bán kính mặt cầu ngoại tiếp bằng 2a/3.", True, "R = SA^2 / (2h) = 2a/3.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một doanh nghiệp sản xuất một loại sản phẩm với hàm chi phí $C(x) = x^3 - 30x^2 + 500x + 1000$ (nghìn đồng) với $1 \le x \le 30$. Giá bán mỗi sản phẩm là 800 nghìn đồng. Xác định số sản phẩm x để lợi nhuận lớn nhất.", "ans": "20", "alt": ["20 sản phẩm"], "exp": "Lợi nhuận L(x) = 800x - C(x). L'(x) = -3x^2 + 60x + 300 = 0 giải ra nghiệm cực đại x = 20."}
            ]
        },
        "🚀 Ôn thi Đánh giá năng lực (ĐGNL)": {
            "title": "BỘ ĐỀ ĐÁNH GIÁ NĂNG LỰC TOÁN HỌC & MÔ HÌNH HÓA THỰC TẾ (ĐHQG/ĐHBK)",
            "p1": [
                {"q": r"Một hồ nước sinh hoạt bị nhiễm vi khuẩn. Tốc độ thay đổi vi khuẩn sau $t$ giờ là $N'(t) = -\frac{200}{(t+1)^2}$ (khuẩn/giờ). Ban đầu $N(0) = 500$ đơn vị. Sau bao nhiêu giờ thì lượng vi khuẩn giảm còn 350 đơn vị?", "ops": ["A. 3 giờ", "B. 4 giờ", "C. 2 giờ", "D. 5 giờ"], "ans": "A", "exp": "N(t) = 200/(t+1) + 300 = 350 <=> 200/(t+1) = 50 <=> t + 1 = 4 => t = 3 giờ."}
            ],
            "p2": [
                {
                    "q": r"Một công ty sản xuất bóng chuyền có chi phí sản xuất mỗi quả là $C(x) = 50 + \frac{200}{x}$ (nghìn đồng/quả) với $x \ge 10$. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) Khi số lượng sản xuất x càng tăng thì chi phí trung bình trên mỗi quả bóng càng giảm.", True, "Hàm C(x) nghịch biến theo x."),
                        ("b) Nếu sản xuất 100 quả bóng thì chi phí mỗi quả là 52 nghìn đồng.", True, "C(100) = 50 + 200/100 = 52."),
                        ("c) Chi phí trên mỗi quả bóng có thể hạ xuống dưới mức 50 nghìn đồng nếu x đủ lớn.", False, "Tiệm cận ngang là 50, hàm luôn lớn hơn 50."),
                        ("d) Đạo hàm C'(x) mang dấu âm với mọi x >= 10.", True, "C'(x) = -200 / x^2 < 0.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một bể chứa nước hình trụ có thể tích V = 54pi (m3). Bác thợ muốn làm bể tốn ít tôn nhất (diện tích toàn phần nhỏ nhất). Bán kính đáy R của bể cần bằng bao nhiêu mét?", "ans": "3", "alt": ["3m", "3.0"], "exp": "V = pi*R^2*h = 54pi => h = 54/R^2. S_tp = 2pi(R^2 + 54/R). f'(R) = 2R - 54/R^2 = 0 <=> R = 3m."}
            ]
        }
    }
}

# ==============================================================================
# 5. DỮ LIỆU TÀI KHOẢN & TRẠNG THÁI HỆ THỐNG
# ==============================================================================
DEFAULT_STUDENTS = [
    {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "current_level": "Khá", "weak_spots": "Dấu góc lượng giác, Hình không gian", "flowers": 30, "total_solved": 5},
    {"student_id": "HS10_01", "password": "123", "full_name": "Lê Bảo Ngọc", "grade": 10, "current_level": "Giỏi", "weak_spots": "Phủ định mệnh đề", "flowers": 35, "total_solved": 8},
    {"student_id": "HS12_01", "password": "123", "full_name": "Nguyễn Hoàng Nam", "grade": 12, "current_level": "Trung bình", "weak_spots": "Tọa độ Oxyz, Đạo hàm cực trị", "flowers": 28, "total_solved": 4}
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
    if topic_type == "OXYZ":
        fig = go.Figure()
        fig.add_trace(go.Scatter3d(
            x=[0, 3, 0, 0], y=[0, 0, 3, 0], z=[0, 0, 0, 3],
            mode='lines+text',
            text=['O', 'Ox', 'Oy', 'Oz'],
            line=dict(color='#0284C7', width=6)
        ))
        fig.add_trace(go.Scatter3d(
            x=[7], y=[6], z=[5],
            mode='markers+text',
            marker=dict(size=8, color='#DC2626'),
            text=['B(7;6;5) Máy bay'],
            textposition='top right'
        ))
    else:
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
    st.markdown("<p style='text-align: center; color: #475569;'>Chuẩn hóa Sách giáo khoa & Vở tự học Kết nối tri thức - Đầy đủ 3 Khối 10, 11, 12</p>", unsafe_allow_html=True)

    col_l1, col_box, col_l2 = st.columns([1, 1.2, 1])
    with col_box:
        with st.container(border=True):
            st.markdown("### 🔐 Cổng Đăng Nhập")
            login_role = st.radio("Vai trò của bạn:", ["👨‍🎓 Học sinh", "👩‍🏫 Giáo viên (Admin)"], horizontal=True)
            user_input = st.text_input("Tài khoản / Mã học sinh:", placeholder="Ví dụ: HS11_01 hoặc admin")
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
            st.caption("💡 Tài khoản học sinh: `HS11_01`, `HS10_01`, `HS12_01` (Pass: `123`). Admin: `admin` / `gstoan2026`.")
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
            st.caption("Giải đúng bài tập SGK/Vở tự học nhận +2 hoa. Đạt điểm cao khảo thí nhận tới +3 hoa!")
    else:
        st.info("Vai trò: **Cố Vấn Sư Phạm & Quản Trị**")

    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.session_state["role"] = None
        st.rerun()
    st.markdown("---")

# ==============================================================================
# 8. PHÂN HỆ GIÁO VIÊN (DASHBOARD & CẤP TÀI KHOẢN)
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
                    nid = st.text_input("Mã học sinh mới (Ví dụ: HS11_02):")
                    nname = st.text_input("Họ và tên học sinh:")
                    ngrade = st.selectbox("Khối lớp:", [10, 11, 12], index=1)
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
# 9. PHÂN HỆ HỌC SINH (HỌC LIỆU TOÀN DIỆN, THUYẾT MINH ÂM THANH, KIỂM MINH CHỨNG)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN KHỐI LỚP VÀ BÀI HỌC
c_gr, c_les = st.columns([1, 2.5])
with c_gr:
    user_grade_default = 0 if student_info.get("grade") == 10 else (2 if student_info.get("grade") == 12 else 1)
    sel_grade = st.selectbox("📚 Chọn Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)
with c_les:
    lesson_list = list(CURRICULUM_DATA[sel_grade].keys())
    sel_lesson = st.selectbox("📖 Chọn Bài Học (Trích Vở Tự Học KNTT):", lesson_list)

cur_data = CURRICULUM_DATA[sel_grade][sel_lesson]

# 4 TAB HỌC TẬP TƯƠNG TÁC
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Video, Thuyết Minh & 3D)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC KÈM ÂM THANH THUYẾT MINH CHUẨN
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {cur_data['chapter']}")
    st.markdown(f"#### {sel_lesson}")

    if cur_data.get("has_3d", False):
        with st.container(border=True):
            st.markdown("🌐 **Mô Hình Không Gian 3D Tương Tác Trực Tiếp (Zero-Install)**")
            st.caption("Dùng chuột hoặc ngón tay chạm/vuốt để xoay 360 độ, quan sát thiết diện và hình chiếu:")
            tp_3d = "OXYZ" if "Oxyz" in sel_lesson or "Vectơ" in sel_lesson else "SHAPE_3D"
            render_3d_geometry_view(tp_3d)

    col_v, col_n = st.columns([1.1, 1])
    with col_v:
        with st.container(border=True):
            st.markdown(f"🎬 **{cur_data['video_title']}**")
            st.caption("Video tóm tắt lý thuyết trọng tâm + phương pháp giải toán then chốt")
            st.video(cur_data["video_url"])
            
            # TRÌNH PHÁT ÂM THANH BÀI GIẢNG SƯ PHẠM ĐỒNG BỘ
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Bài Giảng Vi Mô (Trích Vở tự học):</b><br>
                <small>Bật nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5(sel_lesson.encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_data["audio_script"], audio_hash)
            if lecture_audio_file:
                st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã xem và nghe xong bài giảng vi mô (+1 hoa)", key=f"vid_{sel_lesson}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ xem và nghe bài giảng vi mô")
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes $\LaTeX$)**")
            st.markdown(cur_data["smart_notes"])

# ------------------------------------------------------------------------------
# TAB 2: HỌC SINH TỰ GIẢI - KIỂM MINH CHỨNG MỚI ĐƯỢC THƯỞNG HOA
# ------------------------------------------------------------------------------
with tab2:
    ex = cur_data["exercise"]
    with st.container(border=True):
        st.subheader(f"📝 {ex['title']}")
        st.markdown(f"**Đề bài:** {ex['content']}")

        # Khung phân tầng gợi ý
        c_h1, c_h2, c_h3 = st.columns(3)
        with c_h1:
            if st.button("💡 Gợi ý nấc 1 (Định hướng)", key=f"h1_{ex['id']}", use_container_width=True):
                st.info(f"**Nấc 1:** {ex['hint_1']}")
        with c_h2:
            if st.button("🔍 Gợi ý nấc 2 (Biến đổi)", key=f"h2_{ex['id']}", use_container_width=True):
                st.warning(f"**Nấc 2:** {ex['hint_2']}")
        with c_h3:
            if st.button("🎯 Gợi ý nấc 3 (Kết luận)", key=f"h3_{ex['id']}", use_container_width=True):
                st.error(f"**Nấc 3:** {ex['hint_3']}")

        st.markdown("---")
        st.markdown("#### ✍️ Kiểm Minh Chứng: Em hãy tự làm ra nháp và điền kết quả")
        st.caption("Hệ thống chỉ thưởng +2 🌸 Bông hoa Tri thức khi em thực sự giải chính xác!")

        user_submitted_ans = None
        if ex.get("question_type") == "CHOICE":
            user_submitted_ans = st.radio("Chọn phương án đúng của em:", ex["options"], key=f"choice_ex_{ex['id']}")
        else:
            user_submitted_ans = st.text_input("Nhập kết quả/đáp số của em (ví dụ: 48 hoặc -0.8 hoặc 32/3):", key=f"num_ex_{ex['id']}")

        c_chk, c_sim = st.columns([1, 1.2])
        with c_chk:
            if st.button("🚀 Nộp Bài Giải Để Kiểm Tra Minh Chứng", key=f"btn_check_{ex['id']}", use_container_width=True):
                is_correct = False
                if ex.get("question_type") == "CHOICE":
                    if user_submitted_ans.startswith(ex["target_val"]):
                        is_correct = True
                else:
                    clean_u = user_submitted_ans.strip().replace(",", ".")
                    clean_t = ex["target_val"].strip().replace(",", ".")
                    alt_list = [a.replace(",", ".") for a in ex.get("alt_vals", [])]
                    if clean_u == clean_t or clean_u in alt_list:
                        is_correct = True
                    else:
                        try:
                            # Hỗ trợ phân số như 32/3
                            if "/" in clean_u:
                                num, den = clean_u.split("/")
                                float_u = float(num) / float(den)
                            else:
                                float_u = float(clean_u)
                            
                            if "/" in clean_t:
                                num_t, den_t = clean_t.split("/")
                                float_t = float(num_t) / float(den_t)
                            else:
                                float_t = float(clean_t)
                                
                            if abs(float_u - float_t) < 0.05:
                                is_correct = True
                        except Exception:
                            pass

                if is_correct:
                    st.balloons()
                    st.success("🎉 CHÍNH XÁC 100%! Em đã tự giải đúng bài tập và xứng đáng nhận thưởng!")
                    reward_student_flower(student_info["student_id"], 2, "tự lực giải đúng bài tập Vở tự học có minh chứng")
                    with st.expander("📖 Xem Lời Giải Chi Tiết Hoàn Chỉnh"):
                        st.markdown(ex["solution_text"])
                else:
                    st.error("❌ Kết quả chưa chính xác! Em hãy xem lại các nấc gợi ý và thử giải lại ra nháp nhé. Hệ thống không cộng hoa cho kết quả sai.")

        with c_sim:
            if st.button("🔄 AI Tạo 01 Bài Tương Tự Để Luyện Thêm", key=f"btn_sim_{ex['id']}", use_container_width=True):
                with st.spinner("AI đang tạo bài tương tự cùng dạng..."):
                    if client:
                        try:
                            prompt_sim = f"Bạn là giáo viên Toán. Từ bài tập: '{ex['content']}', hãy tạo 1 bài toán TƯƠNG TỰ CÙNG DẠNG (đổi số liệu). Chỉ đưa đề bài và đáp số cuối cùng trong dấu ngoặc vuông để học sinh tự kiểm chứng."
                            res_sim = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_sim)
                            sim_t = res_sim.text
                        except Exception:
                            sim_t = "Người ta cần làm một chiếc hộp không nắp có đáy hình vuông và thể tích 108 dm3. Tìm diện tích vật liệu nhỏ nhất. [Đáp số: 108 dm2]"
                    else:
                        sim_t = "Bài toán tương tự: Cho góc alpha thỏa mãn 0 < alpha < pi/2 và sin(alpha) = 4/5. Hãy tính cos(alpha). [Đáp số: 3/5 = 0.6]"
                    st.info(f"**Bài toán tương tự rèn luyện:**\n\n{sim_t}")

        # NÚT CHUYỂN TIẾP SƯ PHẠM (HUMAN-IN-THE-LOOP)
        st.markdown("---")
        with st.expander("❓ Vẫn chưa hiểu bài sau khi giải và xem gợi ý? Gửi câu hỏi lên Thầy/Cô"):
            st.caption("Nếu gặp điểm nghẽn nhận thức quá khó, em gửi câu hỏi lên lớp để Thầy/Cô giải đáp trực tiếp:")
            s_note = st.text_input("Ghi rõ vị trí em bị nghẽn:", key=f"note_inbox_{ex['id']}")
            if st.button("📩 [Gửi câu hỏi bế tắc này về Thầy/Cô]", key=f"btn_send_{ex['id']}"):
                item_inbox = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "student_id": student_info["student_id"],
                    "student_name": student_info["full_name"],
                    "lesson_id": sel_lesson,
                    "exercise_id": ex["id"],
                    "student_note": s_note
                }
                st.session_state["inbox_db"].append(item_inbox)
                st.success("✅ Đã gửi câu hỏi về Hộp thư Giáo viên! Thầy/Cô sẽ hỗ trợ giải đáp trực tiếp cho em trên lớp.")
                total_q = len([q for q in st.session_state["inbox_db"] if q["student_id"] == student_info["student_id"]])
                if total_q % 2 == 0:
                    reward_student_flower(student_info["student_id"], 1, "gửi đủ 2 câu hỏi bế tắc nghiêm túc cho Thầy/Cô")

# ------------------------------------------------------------------------------
# TAB 3: TRỢ LÝ AI: SOI BÀI VỞ & TỐI ƯU ÂM THANH MIC/LOA
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("💬 Gia Sư AI: Soi Bài Viết Tay & Lời Khuyên Giọng Nói")
    st.caption(f"Trợ lý AI đang sẵn sàng hỗ trợ nội dung: {sel_lesson}")

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
            Bài học: {sel_lesson} ({sel_grade}).
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
# TAB 4: PHÒNG KHẢO THÍ CHUẨN ĐỊNH DẠNG ĐÚNG/SAI & QUY CHẾ ĐIỂM BỘ GD&ĐT
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

        # PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN
        st.markdown("#### PHẦN I: Câu trắc nghiệm nhiều phương án lựa chọn (3.0 điểm)")
        user_p1 = {}
        for idx, item in enumerate(ex_pack.get("p1", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            user_p1[idx] = st.radio(f"Chọn phương án câu {idx + 1}:", item["ops"], key=f"ex_p1_{sel_exam}_{idx}")

        # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI 4 Ý THEO FORM CHUẨN
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

        # PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN
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

            # 1. Chấm Phần I (Tổng 3 điểm)
            p1_items = ex_pack.get("p1", [])
            p1_corr = 0
            for idx, item in enumerate(p1_items):
                if user_p1[idx].startswith(item["ans"]):
                    p1_corr += 1
            if p1_items:
                score_p1 = (p1_corr / len(p1_items)) * 3.0

            # 2. Chấm Phần II (Chuẩn bậc thang 0.1 - 0.25 - 0.5 - 1.0 theo Bộ GD&ĐT)
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

            # 3. Chấm Phần III (Tổng 3 điểm)
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
            st.markdown(f"- Điểm Phần I (Nhiều lựa chọn): **{round(score_p1, 2)}** / 3.0 điểm.")
            st.markdown(f"- Điểm Phần II (Đúng/Sai chuẩn Bộ GD&ĐT): **{round(score_p2, 2)}** / 4.0 điểm.")
            st.markdown(f"- Điểm Phần III (Trả lời ngắn): **{round(score_p3, 2)}** / 3.0 điểm.")

            if total_score >= 10.0:
                reward_student_flower(student_info["student_id"], 3, f"đạt điểm tuyệt đối 10.0 ở {sel_exam}")
            elif total_score >= 9.0:
                reward_student_flower(student_info["student_id"], 2, f"đạt điểm xuất sắc {total_score} ở {sel_exam}")
            elif total_score >= 8.0:
                reward_student_flower(student_info["student_id"], 1, f"vượt ải thành công {total_score} điểm ở {sel_exam}")
            else:
                st.info("💡 Điểm số chưa đạt mốc 8.0 để nhận hoa thưởng. Em hãy đối chiếu bảng giải thích bên dưới để rút kinh nghiệm nhé!")

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
