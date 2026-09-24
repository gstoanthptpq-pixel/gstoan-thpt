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
# 1. CẤU HÌNH GIAO DIỆN & STYLE SƯ PHẠM
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
# 2. HẠ TẦNG KẾT NỐI GEMINI API & GOOGLE SHEETS DỰ PHÒNG
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

# Hàm phát âm thanh bài giảng sư phạm tự động bằng gTTS
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
# 3. KHO HỌC LIỆU SỐ TOÀN DIỆN CHO CẢ 3 KHỐI 10, 11, 12 (KNTT)
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 10": {
        "Bài 1: Mệnh đề toán học và Tập hợp": {
            "chapter": "Chương I: Mệnh đề và Tập hợp",
            "video_title": "Bài giảng Vi mô: Bản chất Mệnh đề & Phủ định mệnh đề chứa lượng từ",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong bài học về Mệnh đề, em hãy ghi nhớ: Mệnh đề là một khẳng định có chân giá trị hoặc Đúng hoặc Sai, không thể vừa đúng vừa sai. Khi lấy phủ định của mệnh đề chứa lượng từ với mọi, ta chuyển thành tồn tại, và ngược lại. Đặc biệt lưu ý: phủ định của dấu lớn hơn là dấu nhỏ hơn hoặc bằng. Hãy luôn cẩn thận với dấu bằng khi phủ định bất đẳng thức nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Mệnh đề:** Khẳng định hoặc Đúng hoặc Sai. Câu cảm thán, câu hỏi không phải mệnh đề.
- **Phủ định:** Phủ định của $\forall x \in X, P(x)$ là $\exists x \in X, \overline{P(x)}$. Phủ định của $\exists x \in X, P(x)$ là $\forall x \in X, \overline{P(x)}$.
- **Phép toán tập hợp:** 
  + Giao: $A \cap B = \{x \mid x \in A \text{ và } x \in B\}$.
  + Hợp: $A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}$.
  + Hiệu: $A \setminus B = \{x \mid x \in A \text{ và } x \notin B\}$.
- ⚠️ *Bẫy sai lầm:* Phủ định của $>$ là $\le$ (không được quên dấu bằng).
            """,
            "exercise": {
                "id": "SGK_10_1.1",
                "title": "Bài tập 1.3 (Trang 11 - SGK Toán 10 KNTT)",
                "content": r"Cho mệnh đề $P$: '$\forall x \in \mathbb{R}, x^2 - 2x + 5 > 0$'. Hỏi mệnh đề phủ định $\overline{P}$ có dạng nào và nhận chân giá trị là Đúng hay Sai?",
                "question_type": "CHOICE",
                "options": [
                    "A. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 \\le 0$ (Chân giá trị: Sai)",
                    "B. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 < 0$ (Chân giá trị: Đúng)",
                    "C. $\\overline{P}: \\forall x \\in \\mathbb{R}, x^2 - 2x + 5 \\le 0$ (Chân giá trị: Sai)",
                    "D. $\\overline{P}: \\exists x \\in \\mathbb{R}, x^2 - 2x + 5 \\ge 0$ (Chân giá trị: Đúng)"
                ],
                "target_val": "A",
                "hint_1": "Quy tắc: $\\forall$ đổi thành $\\exists$, dấu $>$ đổi thành $\\le$.",
                "hint_2": "Biến đổi: $x^2 - 2x + 5 = (x-1)^2 + 4 \\ge 4 > 0, \\forall x$. Do đó $P$ luôn đúng.",
                "hint_3": "Vì $P$ đúng nên mệnh đề phủ định $\\overline{P}$ nhận chân giá trị Sai.",
                "solution_text": "Phủ định của 'với mọi' là 'tồn tại', phủ định của '>' là '<='. Do tam thức có biệt thức Delta < 0 và hệ số a > 0 nên luôn dương với mọi x, mệnh đề phủ định là Sai."
            }
        },
        "Bài 2: Hệ bất phương trình bậc nhất hai ẩn": {
            "chapter": "Chương II: Bất phương trình bậc nhất hai ẩn",
            "video_title": "Bài giảng Vi mô: Biểu diễn miền nghiệm & Bài toán tối ưu thực tế",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Khi giải hệ bất phương trình bậc nhất hai ẩn, quy trình gồm 3 bước: Bước một, vẽ các đường thẳng biên. Bước hai, chọn một điểm thử không thuộc đường thẳng, thường là gốc tọa độ O(0;0), để kiểm tra xem nửa mặt phẳng nào thỏa mãn. Bước ba, gạch bỏ miền không thỏa mãn. Trong bài toán tối ưu, giá trị lớn nhất hoặc nhỏ nhất luôn đạt tại các đỉnh của miền đa giác nghiệm!",
            "has_3d": False,
            "smart_notes": r"""
- Bất phương trình bậc nhất hai ẩn có dạng: $ax + by \le c$.
- **Xác định miền nghiệm:**
  1. Vẽ đường thẳng $d: ax + by = c$.
  2. Lấy điểm thử $O(0;0)$ (nếu $O \notin d$). Nếu $a(0) + b(0) \le c$ đúng, miền chứa $O$ là miền nghiệm.
- **Tối ưu hóa $F(x; y) = ax + by$:** Điểm tối ưu luôn nằm tại một trong các đỉnh của miền đa giác nghiệm.
            """,
            "exercise": {
                "id": "SGK_10_2.1",
                "title": "Bài tập 2.3 (Trang 29 - SGK Toán 10 KNTT)",
                "content": r"Cho hệ bất phương trình: $\begin{cases} x + y \le 4 \\ x \ge 0 \\ y \ge 0 \end{cases}$. Tìm giá trị lớn nhất $F_{\max}$ của biểu thức $F(x; y) = 3x + 2y$ trên miền nghiệm này.",
                "question_type": "NUMERIC",
                "target_val": "12",
                "hint_1": "Miền nghiệm là tam giác vuông giới hạn bởi ba đỉnh: $O(0;0)$, $A(4;0)$, $B(0;4)$.",
                "hint_2": "Tính giá trị của $F$ tại từng đỉnh: $F(0;0)$, $F(4;0)$, $F(0;4)$.",
                "hint_3": "Ta có: $F(0;0) = 0$, $F(0;4) = 8$, $F(4;0) = 3(4) + 2(0) = 12$.",
                "solution_text": "Miền nghiệm là tam giác OAB. So sánh giá trị F tại 3 đỉnh: F(0;0)=0, F(0;4)=8, F(4;0)=12. Vậy F_max = 12 đạt tại đỉnh A(4;0)."
            }
        },
        "Bài 3: Hệ thức lượng trong tam giác": {
            "chapter": "Chương IV: Hệ thức lượng trong tam giác",
            "video_title": "Bài giảng Vi mô: Định lý Côsin, Định lý Sin & Công thức diện tích",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong tam giác bất kỳ, hãy nhớ hai chìa khóa vạn năng: Nếu biết hai cạnh và góc xen giữa, ta dùng định lý Côsin để tìm cạnh còn lại. Nếu biết một cạnh và hai góc kề, ta dùng định lý Sin. Khi tính diện tích, công thức S bằng một nửa tích hai cạnh nhân sin góc xen giữa là công thức được dùng nhiều nhất!",
            "has_3d": False,
            "smart_notes": r"""
- **Định lý Côsin:** $a^2 = b^2 + c^2 - 2bc \cos A$.
- **Định lý Sin:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$.
- **Công thức diện tích tam giác:**
  $S = \frac{1}{2}ab \sin C = \frac{abc}{4R} = pr = \sqrt{p(p-a)(p-b)(p-c)}$.
            """,
            "exercise": {
                "id": "SGK_10_3.1",
                "title": "Bài tập 3.2 (Trang 55 - SGK Toán 10 KNTT)",
                "content": r"Cho tam giác $ABC$ có cạnh $b = 8$, cạnh $c = 5$ và góc xen giữa $\widehat{A} = 60^\circ$. Tính chính xác độ dài cạnh $a$.",
                "question_type": "NUMERIC",
                "target_val": "7",
                "hint_1": "Áp dụng định lý Côsin: $a^2 = b^2 + c^2 - 2bc\cos A$.",
                "hint_2": "Thay số: $a^2 = 8^2 + 5^2 - 2 \cdot 8 \cdot 5 \cdot \cos(60^\circ)$. Biết $\cos(60^\circ) = 0.5$.",
                "hint_3": "$a^2 = 64 + 25 - 40 = 49 \Rightarrow a = 7$.",
                "solution_text": "Theo định lý Côsin: a^2 = 8^2 + 5^2 - 2*8*5*cos(60°) = 64 + 25 - 40 = 49. Suy ra cạnh a = 7."
            }
        },
        "Bài 4: Đại số tổ hợp (Quy tắc đếm, Hoán vị, Chỉnh hợp, Tổ hợp)": {
            "chapter": "Chương VIII: Đại số tổ hợp",
            "video_title": "Bài giảng Vi mô: Phân biệt Hoán vị, Chỉnh hợp và Tổ hợp",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Điểm mấu chốt của Đại số tổ hợp là thứ tự: Nếu chọn ra k phần tử từ n phần tử mà có sắp xếp thứ tự thì dùng Chỉnh hợp A n chập k. Nếu chọn ra mà không quan tâm đến thứ tự thì dùng Tổ hợp C n chập k. Còn nếu sắp xếp toàn bộ n phần tử thì đó là Hoán vị n giai thừa!",
            "has_3d": False,
            "smart_notes": r"""
- **Quy tắc cộng:** Các phương án độc lập nhau (hoặc phương án này hoặc phương án kia).
- **Quy tắc nhân:** Các công đoạn nối tiếp nhau để hoàn thành công việc.
- **Hoán vị:** $P_n = n!$.
- **Chỉnh hợp (Có thứ tự):** $A_n^k = \frac{n!}{(n-k)!}$.
- **Tổ hợp (Không quan tâm thứ tự):** $C_n^k = \frac{n!}{k!(n-k)!}$.
            """,
            "exercise": {
                "id": "SGK_10_4.1",
                "title": "Bài tập 8.4 (Trang 68 - SGK Toán 10 KNTT)",
                "content": r"Có bao nhiêu cách chọn một ban chấp hành gồm 3 học sinh từ một lớp học có 30 học sinh (gồm 1 Bí thư, 1 Lớp phó và 1 Thủ quỹ - mỗi bạn giữ 1 chức vụ)?",
                "question_type": "NUMERIC",
                "target_val": "24360",
                "hint_1": "Mỗi học sinh được chọn giữ một chức vụ cụ thể, tức là thứ tự sắp xếp có ý nghĩa.",
                "hint_2": "Sử dụng công thức Chỉnh hợp chập 3 của 30 phần tử: $A_{30}^3$.",
                "hint_3": "Tính toán: $A_{30}^3 = 30 \times 29 \times 28 = 24360$.",
                "solution_text": "Do 3 vị trí chức vụ phân biệt nên đây là bài toán chỉnh hợp: A(30, 3) = 30 * 29 * 28 = 24360 cách."
            }
        }
    },
    "Khối 11": {
        "Bài 1: Giá trị lượng giác của góc lượng giác": {
            "chapter": "Chương I: Hàm số lượng giác và Phương trình lượng giác",
            "video_title": "Bài giảng Vi mô: Vòng tròn lượng giác & Quy tắc xét dấu các góc phần tư",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trên đường tròn lượng giác, trục sin là trục tung thẳng đứng, trục cos là trục hoành nằm ngang. Hãy nhớ quy tắc khẩu quyết: Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Khi giải bài tập, luôn kiểm tra khoảng của góc để lấy dấu căn bậc hai chính xác nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Hệ thức cơ bản:** $\sin^2\alpha + \cos^2\alpha = 1$; $\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$; $1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}$.
- **Dấu theo góc phần tư:**
  - Góc I ($0 < \alpha < \frac{\pi}{2}$): $\sin > 0, \cos > 0, \tan > 0$.
  - Góc II ($\frac{\pi}{2} < \alpha < \pi$): $\sin > 0, \cos < 0, \tan < 0$.
  - Góc III ($\pi < \alpha < \frac{3\pi}{2}$): $\sin < 0, \cos < 0, \tan > 0$.
  - Góc IV ($\frac{3\pi}{2} < \alpha < 2\pi$): $\cos > 0, \sin < 0, \tan < 0$.
            """,
            "exercise": {
                "id": "SGK_11_1.1",
                "title": "Bài tập 1.1 (Trang 15 - SGK Toán 11 KNTT)",
                "content": r"Cho góc lượng giác $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$ và $\sin\alpha = \frac{3}{5}$. Hãy tính giá trị của $\cos\alpha$ (điền số thập phân hoặc phân số, ví dụ: -0.8).",
                "question_type": "NUMERIC",
                "target_val": "-0.8",
                "alt_vals": ["-4/5", "-0,8"],
                "hint_1": "Áp dụng $\cos^2\alpha = 1 - \sin^2\alpha = 1 - \frac{9}{25} = \frac{16}{25}$.",
                "hint_2": "Vì góc $\alpha$ thuộc góc phần tư thứ II nên $\cos\alpha < 0$.",
                "hint_3": "Khai căn có dấu trừ: $\cos\alpha = -\sqrt{\frac{16}{25}} = -0.8$.",
                "solution_text": "cos^2(alpha) = 1 - (3/5)^2 = 16/25. Do pi/2 < alpha < pi nên cos(alpha) < 0 => cos(alpha) = -4/5 = -0.8."
            }
        },
        "Bài 2: Cấp số cộng và Cấp số nhân": {
            "chapter": "Chương II: Dãy số. Cấp số cộng và Cấp số nhân",
            "video_title": "Bài giảng Vi mô: Số hạng tổng quát & Tổng n số hạng đầu",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Cấp số cộng là dãy số mà mỗi số hạng sau bằng số hạng trước cộng thêm công sai d. Số hạng tổng quát u n bằng u 1 cộng n trừ 1 nhân d. Cấp số nhân là dãy số mà số hạng sau bằng số hạng trước nhân công bội q. Số hạng tổng quát u n bằng u 1 nhân q mũ n trừ 1. Hãy nhớ phân biệt công thức tổng của hai cấp số này nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Cấp số cộng (CSC):** $u_n = u_1 + (n-1)d$; $S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n-1)d]}{2}$.
- **Cấp số nhân (CSN):** $u_n = u_1 \cdot q^{n-1}$; $S_n = u_1 \frac{1 - q^n}{1 - q}$ ($q \neq 1$).
            """,
            "exercise": {
                "id": "SGK_11_2.1",
                "title": "Bài tập 2.10 (Trang 52 - SGK Toán 11 KNTT)",
                "content": r"Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 3$ và công sai $d = 5$. Tìm giá trị của số hạng thứ 10 ($u_{10}$).",
                "question_type": "NUMERIC",
                "target_val": "48",
                "hint_1": "Sử dụng công thức số hạng tổng quát: $u_n = u_1 + (n-1)d$.",
                "hint_2": "Thay số: $n = 10, u_1 = 3, d = 5$.",
                "hint_3": "$u_{10} = 3 + (10 - 1) \cdot 5 = 3 + 45 = 48$.",
                "solution_text": "u_10 = u_1 + 9*d = 3 + 9*5 = 48."
            }
        },
        "Bài 3: Đường thẳng và Mặt phẳng vuông góc trong không gian": {
            "chapter": "Chương IV: Quan hệ vuông góc trong không gian",
            "video_title": "Bài giảng Vi mô: Phương pháp xác định góc giữa đường thẳng và mặt phẳng",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Để tìm góc giữa đường thẳng d và mặt phẳng P, ta thực hiện 3 bước: Bước 1, tìm giao điểm A giữa đường thẳng và mặt phẳng. Bước 2, từ một điểm S trên đường thẳng, hạ hình chiếu vuông góc H lên mặt phẳng P. Bước 3, góc cần tìm chính là góc giữa SA và AH, tức là góc SAH. Luôn gắn góc này vào tam giác vuông SAH tại H nhé!",
            "has_3d": True,
            "smart_notes": r"""
- **Đường thẳng vuông góc mặt phẳng:** $d \perp (P) \Leftrightarrow d \perp a$ và $d \perp b$ (với $a, b \subset (P)$ cắt nhau).
- **Góc giữa đường thẳng $d$ và mặt phẳng $(P)$:**
  + Nếu $d \perp (P)$ thì góc bằng $90^\circ$.
  + Nếu $d$ cắt $(P)$ tại $A$ và $H$ là hình chiếu của $S \in d$ lên $(P)$, thì $\widehat{(d, (P))} = \widehat{SAH}$.
            """,
            "exercise": {
                "id": "SGK_11_3.1",
                "title": "Bài tập 4.5 (Trang 84 - SGK Toán 11 KNTT)",
                "content": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$, $AB = a$. Cạnh bên $SA \perp (ABC)$ và $SA = a$. Tính góc giữa cạnh bên $SB$ và mặt phẳng đáy $(ABC)$ (nhập giá trị độ, ví dụ: 45).",
                "question_type": "NUMERIC",
                "target_val": "45",
                "hint_1": "Giao điểm của $SB$ và đáy là $B$. Điểm $S$ có hình chiếu lên đáy là $A$ (do $SA \perp (ABC)$).",
                "hint_2": "Hình chiếu của đoạn thẳng $SB$ lên mặt đáy là đoạn $AB$. Góc cần tìm là $\widehat{SBA}$.",
                "hint_3": "Tam giác $SAB$ vuông tại $A$ và có $SA = AB = a$ (vuông cân), do đó góc $\widehat{SBA} = 45^\circ$.",
                "solution_text": "Hình chiếu của SB lên đáy (ABC) là AB. Tam giác SAB vuông cân tại A vì SA = AB = a, do đó góc giữa SB và đáy là góc SBA = 45 độ."
            }
        },
        "Bài 4: Đạo hàm và Quy tắc tính đạo hàm": {
            "chapter": "Chương IX: Đạo hàm",
            "video_title": "Bài giảng Vi mô: Bảng đạo hàm cơ bản & Đạo hàm hàm hợp",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Đạo hàm biểu diễn tốc độ thay đổi tức thời của hàm số. Hãy nhớ các quy tắc cơ bản: đạo hàm của x mũ n bằng n nhân x mũ n trừ 1. Đạo hàm của u nhân v bằng u phẩy v cộng u v phẩy. Và đặc biệt với hàm hợp, nhớ luôn nhân thêm u phẩy ở cuối nhé!",
            "has_3d": False,
            "smart_notes": r"""
- **Bảng đạo hàm:**
  $(x^n)' = n x^{n-1}$; $(\sin x)' = \cos x$; $(\cos x)' = -\sin x$; $(e^x)' = e^x$; $(\ln x)' = \frac{1}{x}$.
- **Quy tắc:**
  $(u \pm v)' = u' \pm v'$; $(uv)' = u'v + uv'$; $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.
- **Đạo hàm hàm hợp:** $[f(u)]' = f'(u) \cdot u'$.
            """,
            "exercise": {
                "id": "SGK_11_4.1",
                "title": "Bài tập 9.2 (Trang 105 - SGK Toán 11 KNTT)",
                "content": r"Tính giá trị đạo hàm của hàm số $f(x) = x^3 - 3x^2 + 5$ tại điểm $x = 2$.",
                "question_type": "NUMERIC",
                "target_val": "0",
                "hint_1": "Tìm đạo hàm tổng quát: $f'(x) = (x^3)' - (3x^2)' + (5)'$.",
                "hint_2": "Ta có $f'(x) = 3x^2 - 6x$.",
                "hint_3": "Thay $x = 2$ vào: $f'(2) = 3(2^2) - 6(2) = 12 - 12 = 0$.",
                "solution_text": "f'(x) = 3x^2 - 6x. Tại x = 2, f'(2) = 3*(4) - 6*(2) = 0."
            }
        }
    },
    "Khối 12": {
        "Bài 1: Tính đơn điệu và Cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "video_title": "Bài giảng Vi mô: Bảng biến thiên, dấu đạo hàm y' và phân biệt cực trị chuẩn 2025+",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Trong chương trình lớp 12, khảo sát hàm số là trọng tâm số một. Hãy nhớ: Hàm số đồng biến khi y phẩy lớn hơn hoặc bằng không, nghịch biến khi y phẩy nhỏ hơn hoặc bằng không. Khi y phẩy đổi dấu từ dương sang âm, ta có điểm cực đại; đổi dấu từ âm sang dương, ta có điểm cực tiểu. Cực kỳ lưu ý: Điểm cực trị của hàm số là x, giá trị cực trị là y, còn điểm cực trị của đồ thị là cặp tọa độ x, y!",
            "has_3d": False,
            "smart_notes": r"""
- **Đồng biến / Nghịch biến:** Hàm đồng biến trên $K \Leftrightarrow f'(x) \ge 0, \forall x \in K$ (bằng 0 tại hữu hạn điểm).
- **Quy tắc cực trị:** $f'(x_0) = 0$ (hoặc không xác định) và đổi dấu qua $x_0$:
  + Đổi dấu $(+) \rightarrow (-)$: Điểm cực đại.
  + Đổi dấu $(-) \rightarrow (+)$: Điểm cực tiểu.
- ⚠️ *Phân biệt thuật ngữ:*
  + Điểm cực trị của hàm số: $x_0$.
  + Giá trị cực trị của hàm số: $y_0 = f(x_0)$.
  + Điểm cực trị của đồ thị: $M(x_0; y_0)$.
            """,
            "exercise": {
                "id": "SGK_12_1.1",
                "title": "Bài tập 1.4 (Trang 15 - SGK Toán 12 KNTT)",
                "content": r"Tìm giá trị cực tiểu ($y_{CT}$) của hàm số $y = x^3 - 3x + 2$.",
                "question_type": "NUMERIC",
                "target_val": "0",
                "hint_1": "Tính đạo hàm: $y' = 3x^2 - 3 = 0 \Leftrightarrow x = 1$ hoặc $x = -1$.",
                "hint_2": "Lập bảng xét dấu: tại $x = 1$, đạo hàm $y'$ đổi dấu từ âm sang dương nên $x = 1$ là điểm cực tiểu.",
                "hint_3": "Thay $x = 1$ vào hàm ban đầu: $y_{CT} = 1^3 - 3(1) + 2 = 0$.",
                "solution_text": "y' = 3x^2 - 3 = 0 <=> x = +-1. Tại x = 1, y' đổi dấu từ âm sang dương nên hàm đạt cực tiểu tại x = 1. Giá trị cực tiểu y_CT = 1 - 3 + 2 = 0."
            }
        },
        "Bài 2: Vectơ và Hệ tọa độ Oxyz trong không gian": {
            "chapter": "Chương II: Vectơ và Hệ tọa độ trong không gian",
            "video_title": "Bài giảng Vi mô: Tọa độ điểm, vectơ, tích có hướng & Mặt cầu Oxyz",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Hệ trục tọa độ Oxyz gồm ba trục đôi một vuông góc: Ox hoành độ, Oy tung độ và Oz cao độ. Vectơ u có tọa độ x, y, z tương ứng với các vectơ đơn vị i, j, k. Phương trình chính tắc của mặt cầu tâm I(a; b; c) bán kính R là x trừ a tất cả bình cộng y trừ b tất cả bình cộng z trừ c tất cả bình bằng R bình phương. Nhớ đừng nhầm tâm đổi dấu nhé!",
            "has_3d": True,
            "smart_notes": r"""
- $\vec{u} = (x; y; z) \Leftrightarrow \vec{u} = x\vec{i} + y\vec{j} + z\vec{k}$.
- **Tích vô hướng:** $\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2 = |\vec{u}| |\vec{v}| \cos(\vec{u}, \vec{v})$.
- **Khoảng cách 2 điểm:** $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.
- **Mặt cầu:** $(S): (x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$ có tâm $I(a; b; c)$ và bán kính $R$.
            """,
            "exercise": {
                "id": "SGK_12_2.1",
                "title": "Bài tập 2.6 (Trang 64 - SGK Toán 12 KNTT)",
                "content": r"Trong không gian $Oxyz$, cho mặt cầu $(S): (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 25$. Tìm bán kính $R$ của mặt cầu $(S)$.",
                "question_type": "NUMERIC",
                "target_val": "5",
                "hint_1": "Đồng nhất phương trình đã cho với phương trình chính tắc: $(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$.",
                "hint_2": "Vế phải là $R^2 = 25$.",
                "hint_3": "Do bán kính là số dương nên $R = \sqrt{25} = 5$.",
                "solution_text": "Theo dạng chính tắc phương trình mặt cầu, vế phải R^2 = 25 => Bán kính R = 5."
            }
        },
        "Bài 3: Nguyên hàm và Tích phân": {
            "chapter": "Chương IV: Nguyên hàm và Tích phân",
            "video_title": "Bài giảng Vi mô: Ý nghĩa hình học của Tích phân & Tính diện tích hình phẳng",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Tích phân từ a đến b của f x d x bằng F b trừ F a theo định lý Newton - Leibniz. Ý nghĩa hình học quan trọng nhất của tích phân là diện tích hình phẳng giới hạn bởi đường cong và trục hoành. Khi làm bài, hãy luôn vẽ phác đồ thị hoặc giải phương trình hoành độ giao điểm để phá dấu giá trị tuyệt đối chính xác!",
            "has_3d": False,
            "smart_notes": r"""
- **Định nghĩa tích phân:** $\int_a^b f(x) dx = F(b) - F(a)$.
- **Tính chất:**
  $\int_a^b [f(x) \pm g(x)] dx = \int_a^b f(x)dx \pm \int_a^b g(x)dx$; $\int_a^b k f(x) dx = k \int_a^b f(x)dx$.
- **Diện tích hình phẳng:** $S = \int_a^b |f(x) - g(x)| dx$.
            """,
            "exercise": {
                "id": "SGK_12_3.1",
                "title": "Bài tập 4.5 (Trang 101 - SGK Toán 12 KNTT)",
                "content": r"Tính tích phân $I = \int_0^2 (2x + 1) dx$.",
                "question_type": "NUMERIC",
                "target_val": "6",
                "hint_1": "Nguyên hàm của $2x + 1$ là $F(x) = x^2 + x$.",
                "hint_2": "Áp dụng định lý Newton - Leibniz: $I = F(2) - F(0)$.",
                "hint_3": "$I = (2^2 + 2) - (0^2 + 0) = 4 + 2 = 6$.",
                "solution_text": "F(x) = x^2 + x. I = F(2) - F(0) = (4 + 2) - 0 = 6."
            }
        },
        "Bài 4: Phương pháp tọa độ trong không gian (Mặt phẳng)": {
            "chapter": "Chương V: Phương trình mặt phẳng và đường thẳng trong không gian",
            "video_title": "Bài giảng Vi mô: Vectơ pháp tuyến & Phương trình tổng quát của mặt phẳng",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": "Chào em! Mặt phẳng trong không gian được xác định khi biết một điểm đi qua và một vectơ pháp tuyến vuông góc với mặt phẳng đó. Phương trình tổng quát có dạng A x cộng B y cộng C z cộng D bằng không, trong đó vectơ n có tọa độ A, B, C. Muốn tính khoảng cách từ một điểm đến mặt phẳng, em lấy tọa độ điểm thay vào vế trái chia cho độ dài vectơ pháp tuyến!",
            "has_3d": True,
            "smart_notes": r"""
- Vectơ pháp tuyến $\vec{n} = (A; B; C) \neq \vec{0}$ vuông góc với mọi vectơ nằm trong $(P)$.
- Phương trình qua $M_0(x_0; y_0; z_0)$ có VTPT $\vec{n}$:
  $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0 \Leftrightarrow Ax + By + Cz + D = 0$.
- **Khoảng cách từ $M(x_M; y_M; z_M)$ đến $(P)$:**
  $d(M, (P)) = \frac{|Ax_M + By_M + Cz_M + D|}{\sqrt{A^2 + B^2 + C^2}}$.
            """,
            "exercise": {
                "id": "SGK_12_4.1",
                "title": "Bài tập 5.2 (Trang 120 - SGK Toán 12 KNTT)",
                "content": r"Tính khoảng cách từ gốc tọa độ $O(0;0;0)$ đến mặt phẳng $(P): 2x - 2y + z - 9 = 0$.",
                "question_type": "NUMERIC",
                "target_val": "3",
                "hint_1": "Áp dụng công thức khoảng cách: $d(O, (P)) = \frac{|2(0) - 2(0) + 1(0) - 9|}{\sqrt{2^2 + (-2)^2 + 1^2}}$.",
                "hint_2": "Tử số là $|-9| = 9$.",
                "hint_3": "Mẫu số là $\sqrt{4 + 4 + 1} = \sqrt{9} = 3$. Vậy $d = \frac{9}{3} = 3$.",
                "solution_text": "d(O, (P)) = |-9| / sqrt(2^2 + (-2)^2 + 1^2) = 9 / 3 = 3."
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
                {"q": r"Tính góc giữa hai đường thẳng d1: x + y = 0 và d2: x - y + 5 = 0 (nhập số độ).", "ans": "90", "alt": ["90 độ"], "exp": "n1 = (1; 1), n2 = (1; -1). Tích vô hướng 1*1 + 1*(-1) = 0 nên hai đường vuông góc, góc 90 độ."}
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
                        ("a) Không gian mẫu có 8 phần tử.", True, "2^3 = 8."),
                        ("b) Xác suất để 3 lần đều xuất hiện mặt sấp là 1/8.", True, "Chỉ có 1 kết quả SSS trong 8 kết quả."),
                        ("c) Xác suất để có ít nhất một lần xuất hiện mặt ngửa là 7/8.", True, "Biến cố đối của '3 lần đều sấp' là 1 - 1/8 = 7/8."),
                        ("d) Biến cố 'xuất hiện 2 mặt ngửa' có xác suất 1/2.", False, "Có 3 kết quả (NNS, NSN, SNN), xác suất 3/8 khác 1/2.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tìm hệ số của x^3 trong khai triển nhị thức Newton của (x + 2)^4.", "ans": "8", "alt": ["8.0"], "exp": "Số hạng tổng quát: C(4, 1)*x^3*2^1 = 4*2*x^3 = 8x^3. Hệ số là 8."}
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
                        ("c) Số 20 là một số hạng của cấp số cộng trên.", True, "3n - 1 = 20 <=> 3n = 21 <=> n = 7 (nguyên dương thỏa mãn)."),
                        ("d) Tổng 10 số hạng đầu tiên S_10 = 155.", True, "S_10 = 10*(2*2 + 9*3)/2 = 10*31/2 = 155.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một rạp hát có 12 hàng ghế. Hàng đầu có 15 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Tính tổng số ghế của rạp.", "ans": "312", "alt": ["312 ghế"], "exp": "CSC: u1=15, d=2, n=12. S_12 = 12*(2*15 + 11*2)/2 = 12*52/2 = 312."}
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
                        ("b) Đường thẳng AB song song với mặt phẳng (SCD).", True, "AB song song CD và CD thuộc (SCD)."),
                        ("c) Đường thẳng SO cắt đường thẳng AD.", False, "SO và AD chéo nhau."),
                        ("d) Thiết diện của hình chóp cắt bởi mặt phẳng qua O song song với (SAB) là hình thang.", True, "Mặt phẳng cắt tạo các đoạn song song.")
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
                {"q": r"Đạo hàm của hàm số $y = x^3 - 2x + 1$ là:", "ops": [r"A. $y' = 3x^2 - 2$", r"B. $y' = 3x^2 + 2$", r"C. $y' = x^2 - 2$", r"D. $y' = 3x - 2$"], "ans": "A", "exp": "Đạo hàm từng số hạng: (x^3)' = 3x^2, (-2x)' = -2, 1' = 0."}
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
                {"q": r"Một chất điểm chuyển động theo phương trình $s(t) = t^3 - 3t^2 + 2$ (t tính bằng giây, s tính bằng mét). Tính vận tốc tức thời tại thời điểm t = 4 giây (m/s).", "ans": "24", "alt": ["24 m/s"], "exp": "v(t) = s'(t) = 3t^2 - 6t. Tại t = 4: v(4) = 3(16) - 6(4) = 48 - 24 = 24 m/s."}
            ]
        },
        "Cuối học kỳ 2": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 2 - TOÁN 11",
            "p1": [
                {"q": r"Cho hình lập phương ABCD.A'B'C'D'. Góc giữa hai đường thẳng A'B' và CD bằng:", "ops": ["A. 0 độ", "B. 90 độ", "C. 45 độ", "D. 60 độ"], "ans": "A", "exp": "A'B' song song AB và AB song song CD nên A'B' song song CD, góc 0 độ."}
            ],
            "p2": [
                {
                    "q": r"Cho hình chóp S.ABC có SA vuông góc đáy, tam giác ABC vuông tại B. Xét tính Đúng/Sai:",
                    "items": [
                        ("a) SA vuông góc với BC.", True, "SA vuông góc mặt phẳng (ABC) nên vuông góc mọi đường trong đáy."),
                        ("b) BC vuông góc với mặt phẳng (SAB).", True, "BC vuông góc AB và BC vuông góc SA."),
                        ("c) Tam giác SBC là tam giác vuông tại B.", True, "BC vuông góc SB vì BC vuông góc (SAB)."),
                        ("d) Khoảng cách từ S đến mặt phẳng (ABC) bằng độ dài cạnh SB.", False, "Khoảng cách bằng độ dài cạnh SA.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Cho hình chóp tam giác đều S.ABC có cạnh đáy bằng 3, đường cao SH = 4. Tính thể tích khối chóp S.ABC (làm tròn 2 chữ số thập phân).", "ans": "5.2", "alt": ["5.19", "5.20"], "exp": "S_day = 3^2 * sqrt(3) / 4 = 9*sqrt(3)/4. V = (1/3)*S_day*h = (1/3)*(9*sqrt(3)/4)*4 = 3*sqrt(3) ≈ 5.20."}
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
                        ("a) Đạo hàm của hàm số là f'(x) = 3x^2 - 6x.", True, "Đạo hàm chính xác."),
                        ("b) Hàm số đồng biến trên khoảng (0; 2).", False, "f'(x) < 0 trên khoảng (0; 2) nên hàm số nghịch biến."),
                        ("c) Điểm cực đại của đồ thị hàm số là điểm A(0; 2).", True, "f'(0) = 0, f(0) = 2, f' đổi dấu + sang -."),
                        ("d) Giá trị cực tiểu của hàm số bằng -2.", True, "Điểm cực tiểu x = 2, f(2) = 8 - 12 + 2 = -2.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tìm giá trị lớn nhất của hàm số $f(x) = x^3 - 3x + 1$ trên đoạn $[0; 2]$.", "ans": "3", "alt": ["3.0"], "exp": "f'(x) = 3x^2 - 3 = 0 <=> x = 1. f(0) = 1, f(1) = -1, f(2) = 3. Giá trị lớn nhất là 3."}
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
                        ("c) Điểm O(0; 0; 0) nằm bên trong mặt cầu (S).", True, "(0-1)^2 + (0+2)^2 + (0-3)^2 = 1 + 4 + 9 = 14 < 16 nên nằm trong."),
                        ("d) Diện tích mặt cầu bằng 64pi.", True, "S = 4*pi*R^2 = 4*pi*16 = 64pi.")
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
                        ("d) Giá trị của I bằng e + 1.", True, "I = [(2x+1)e^x]_0^1 - 2\int e^x dx = 3e - 1 - 2(e - 1) = e + 1.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Tính diện tích hình phẳng giới hạn bởi parabol $y = x^2$ và đường thẳng $y = 2x$.", "ans": "1.33", "alt": ["4/3", "1.3"], "exp": "Giao điểm x = 0, x = 2. S = \int_0^2 (2x - x^2) dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = 4/3 ≈ 1.33."}
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
                        ("c) Điểm A(3; -3; 4) thuộc đường thẳng d.", True, "Thay vào: (3-1)/2 = 1, (-3+2)/-1 = 1, (4-3)/1 = 1 thỏa mãn."),
                        ("d) d vuông góc với mặt phẳng (P): 2x - y + z + 5 = 0.", True, "Vectơ chỉ phương của d cùng phương pháp tuyến của (P).")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một hộp chứa 5 viên bi đỏ và 4 viên bi xanh. Lấy ngẫu nhiên 3 viên bi. Tính xác suất để lấy được đúng 2 viên bi đỏ (làm tròn 2 chữ số thập phân).", "ans": "0.48", "alt": ["10/21", "0.476"], "exp": "C(5, 2)*C(4, 1) / C(9, 3) = (10*4) / 84 = 40/84 = 10/21 ≈ 0.48."}
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
                        ("c) Thể tích khối chóp S.ABC bằng a^3 / 4.", False, "V = (1/3)*(a^2*sqrt(3)/4)*a = a^3*sqrt(3)/12 khác a^3/4."),
                        ("d) Bán kính mặt cầu ngoại tiếp bằng 2a/3.", True, "R = SA^2 / (2h) = (2a/sqrt(3))^2 / (2a) = 2a/3.")
                    ]
                }
            ],
            "p3": [
                {"q": r"Một doanh nghiệp sản xuất một loại sản phẩm với hàm chi phí $C(x) = x^3 - 30x^2 + 500x + 1000$ (nghìn đồng) với $1 \le x \le 30$. Giá bán mỗi sản phẩm là 800 nghìn đồng. Xác định số sản phẩm x để lợi nhuận lớn nhất.", "ans": "20", "alt": ["20 sản phẩm"], "exp": "Lợi nhuận L(x) = 800x - C(x) = -x^3 + 30x^2 + 300x - 1000. L'(x) = -3x^2 + 60x + 300 = 0 giải ra nghiệm cực đại x = 20."}
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
                {"q": r"Một bể chứa nước hình trụ có thể tích V = 54pi (m3). Bác thợ muốn làm bể tốn ít tôn nhất (diện tích toàn phần nhỏ nhất). Bán kính đáy R của bể cần bằng bao nhiêu mét?", "ans": "3", "alt": ["3m", "3.0"], "exp": "V = pi*R^2*h = 54pi => h = 54/R^2. S_tp = 2*pi*R^2 + 2*pi*R*h = 2pi(R^2 + 54/R). f'(R) = 2R - 54/R^2 = 0 <=> 2R^3 = 54 <=> R = 3m."}
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
            x=[2], y=[-1], z=[3],
            mode='markers+text',
            marker=dict(size=8, color='#DC2626'),
            text=['I(2;-1;3)'],
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
    st.markdown("<p style='text-align: center; color: #475569;'>Chuẩn hóa Sách giáo khoa Kết nối tri thức - Đầy đủ 3 Khối 10, 11, 12</p>", unsafe_allow_html=True)

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
            st.caption("Giải đúng bài tập SGK nhận +2 hoa. Đạt điểm cao khảo thí nhận tới +3 hoa!")
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
    sel_lesson = st.selectbox("📖 Chọn Bài Học SGK (Kết Nối Tri Thức):", lesson_list)

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
            tp_3d = "OXYZ" if "Oxyz" in sel_lesson else "SHAPE_3D"
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
                <b>🎙️ Âm Thanh Thuyết Minh Bài Giảng Vi Mô (Chuẩn sư phạm):</b><br>
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
            user_submitted_ans = st.text_input("Nhập kết quả/đáp số của em (ví dụ: -0.8 hoặc 7):", key=f"num_ex_{ex['id']}")

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
                            if abs(float(clean_u) - float(clean_t)) < 0.05:
                                is_correct = True
                        except Exception:
                            pass

                if is_correct:
                    st.balloons()
                    st.success("🎉 CHÍNH XÁC 100%! Em đã tự giải đúng bài tập và xứng đáng nhận thưởng!")
                    reward_student_flower(student_info["student_id"], 2, "tự lực giải đúng bài tập SGK có minh chứng")
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
                            sim_t = "Cho góc x thỏa mãn pi/2 < x < pi và sin(x) = 5/13. Hãy tính cos(x). [Đáp số: cos(x) = -12/13]"
                    else:
                        sim_t = "Bài tương tự: Cho tam giác ABC có b = 6, c = 4 và góc A = 60 độ. Tính cạnh a. [Đáp số: a = 2*căn(7)]"
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
            Bạn là Gia sư dạy Toán THPT bám sát SGK Kết nối tri thức.
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

                # Áp dụng thang điểm chính thức
                if num_correct_in_q == 1:
                    score_p2 += 0.1
                elif num_correct_in_q == 2:
                    score_p2 += 0.25
                elif num_correct_in_q == 3:
                    score_p2 += 0.5
                elif num_correct_in_q == 4:
                    score_p2 += 1.0

            # Quy đổi thang 4.0 nếu số lượng câu khác 4
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

            # Quy chế thưởng hoa
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
