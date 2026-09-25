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
# 1. CẤU HÌNH GIAO DIỆN & CSS THANH CUỘN CHUYÊN BIỆT
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
# 2. KHỞI TẠO HẠ TẦNG KẾT NỐI GEMINI API & GOOGLE SHEETS
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
# 3. KHO HỌC LIỆU SỐ TOÀN DIỆN: 27 BÀI (K10), 33 BÀI (K11), 19 BÀI (K12)
# ==============================================================================
RAW_LESSONS_10 = [
    ("Bài 1: Mệnh đề toán học", "Chương I: Mệnh đề và tập hợp",
     "Mệnh đề là khẳng định đúng hoặc khẳng định sai. Không thể vừa đúng vừa sai.",
     r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
     "Phủ định của dấu lớn hơn (>) là dấu nhỏ hơn hoặc bằng (<=), không được quên dấu bằng.",
     "Phủ định mệnh đề: Mọi số thực x đều có x^2 >= 0", "A", "CHOICE", ["A. Tồn tại x có x^2 < 0", "B. Tồn tại x có x^2 <= 0", "C. Mọi x có x^2 < 0"],
     "Lập mệnh đề phủ định của P: 'Số 15 chia hết cho 2'.", "Mệnh đề phủ định là: 'Số 15 không chia hết cho 2'. Mệnh đề này là mệnh đề Đúng."),

    ("Bài 2: Tập hợp và các phép toán trên tập hợp", "Chương I: Mệnh đề và tập hợp",
     "Giao lấy phần chung, hợp lấy tất cả, hiệu A trừ B lấy thuộc A nhưng không thuộc B.",
     r"A \cap B = \{x \mid x \in A \text{ và } x \in B\}; \quad A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}",
     "Phân biệt khoảng (a; b) và đoạn [a; b] trên trục số thực.",
     "Cho A = [1; 5] và B = (3; 7). Số phần tử nguyên thuộc A giao B là:", "2", "NUMERIC", [],
     "Cho A = {1; 2; 3; 4} và B = {3; 4; 5}. Tìm A giao B.", "Giao của hai tập hợp là phần tử chung của cả hai tập: A giao B = {3; 4}."),

    ("Bài 3: Bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn",
     "Dạng ax + by <= c. Đường thẳng bờ ax + by = c chia mặt phẳng làm hai nửa.",
     r"ax + by \le c \quad (a^2 + b^2 \neq 0)",
     "Chọn điểm thử O(0;0) nếu O không thuộc đường thẳng bờ để xác định nửa mặt phẳng nghiệm.",
     "Điểm O(0;0) có thuộc miền nghiệm của 2x + y <= 3 không? (1: Có, 0: Không)", "1", "NUMERIC", [],
     "Xác định miền nghiệm của x - y > 0.", "Vẽ đường thẳng x - y = 0. Chọn điểm (1; 0) thay vào: 1 - 0 = 1 > 0 (thỏa mãn). Miền nghiệm là nửa mặt phẳng chứa điểm (1; 0) không kể bờ."),

    ("Bài 4: Hệ bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn",
     "Miền nghiệm của hệ là phần giao của các miền nghiệm của từng bất phương trình.",
     r"F(x; y) = ax + by \quad \text{đạt GTLN/GTNN tại một trong các đỉnh của miền đa giác}",
     "Giá trị lớn nhất và nhỏ nhất luôn đạt tại một trong các đỉnh của miền đa giác nghiệm.",
     "Cho hệ x + y <= 4, x >= 0, y >= 0. GTLN của F(x;y) = 3x + 2y bằng:", "12", "NUMERIC", [],
     "Tìm các đỉnh của miền nghiệm hệ: x + y <= 4, x >= 0, y >= 0.", "Miền nghiệm là tam giác OAB với O(0;0), A(4;0), B(0;4)."),

    ("Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ", "Chương III: Hệ thức lượng trong tam giác",
     "Điểm M trên nửa đường tròn đơn vị: tung độ là sin, hoành độ là cos.",
     r"\sin^2\alpha + \cos^2\alpha = 1; \quad \tan\alpha = \frac{\sin\alpha}{\cos\alpha} \ (\alpha \neq 90^\circ)",
     "Khi góc alpha tù thì cos alpha âm, tan alpha âm, còn sin alpha luôn dương.",
     "Tính sin(30 độ) + cos(60 độ) (dạng số thập phân):", "1", "NUMERIC", [],
     "Tính giá trị của cos(120 độ).", "Ta có: cos(120°) = cos(180° - 60°) = -cos(60°) = -1/2 = -0.5."),

    ("Bài 6: Hệ thức lượng trong tam giác", "Chương III: Hệ thức lượng trong tam giác",
     "Định lý Côsin tính cạnh thứ ba; định lý Sin tính cạnh và bán kính đường tròn ngoại tiếp R.",
     r"a^2 = b^2 + c^2 - 2bc \cos A; \quad \frac{a}{\sin A} = 2R; \quad S = \frac{1}{2}bc\sin A",
     "Nếu cos A < 0 thì góc A là góc tù trong tam giác.",
     "Tam giác có b=8, c=5, góc A=60 độ. Cạnh a bằng:", "7", "NUMERIC", [],
     "Cho tam giác ABC có b=6, c=8, góc A=90 độ. Tính bán kính R.", "Tam giác vuông tại A nên cạnh huyền a = căn(6^2 + 8^2) = 10. Bán kính R = a / 2 = 5."),

    ("Bài 7: Các khái niệm mở đầu về vectơ", "Chương IV: Vectơ",
     "Vectơ là đoạn thẳng có hướng. Hai vectơ cùng phương khi giá song song hoặc trùng nhau.",
     r"\vec{a} = \vec{b} \iff |\vec{a}| = |\vec{b}| \text{ và cùng hướng}",
     "Vectơ không cùng phương và cùng hướng với mọi vectơ.",
     "Hai vectơ cùng độ dài thì chắc chắn bằng nhau? (1: Đúng, 0: Sai)", "0", "NUMERIC", [],
     "Cho hình vuông ABCD. So sánh độ dài hai vectơ AB và BC.", "Vì ABCD là hình vuông nên độ dài cạnh AB bằng BC, do đó độ dài hai vectơ AB và BC bằng nhau."),

    ("Bài 8: Tổng và hiệu của hai vectơ", "Chương IV: Vectơ",
     "Quy tắc 3 điểm: AB + BC = AC. Quy tắc hình bình hành: AB + AD = AC.",
     r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{AB} - \vec{AC} = \vec{CB}",
     "Quy tắc trừ chung gốc: AB trừ AC bằng CB, không phải BC.",
     "Cho tam giác đều ABC cạnh 2. Độ dài vectơ AB + BC bằng:", "2", "NUMERIC", [],
     "Rút gọn biểu thức vectơ: AB + BC + CD.", "Áp dụng quy tắc 3 điểm liên tiếp: (AB + BC) + CD = AC + CD = AD."),

    ("Bài 9: Tích của một vectơ với một số", "Chương IV: Vectơ",
     "Tích k*a cùng hướng với a khi k > 0, ngược hướng khi k < 0. Độ dài bằng |k|*|a|.",
     r"k\vec{a}; \quad I \text{ là trung điểm } AB \iff \vec{IA} + \vec{IB} = \vec{0}",
     "Điều kiện để hai vectơ cùng phương: tồn tại số k sao cho a = k*b.",
     "Gọi G là trọng tâm tam giác ABC. Độ dài vectơ GA + GB + GC bằng:", "0", "NUMERIC", [],
     "Cho I là trung điểm AB. Biểu diễn vectơ MI qua MA và MB.", "Theo tính chất trung điểm: MA + MB = 2*MI => MI = (1/2)*MA + (1/2)*MB."),

    ("Bài 10: Vectơ trong mặt phẳng tọa độ", "Chương IV: Vectơ",
     "Tọa độ vectơ bằng tọa độ điểm cuối trừ điểm đầu. Tọa độ trung điểm bằng trung bình cộng.",
     r"\vec{u} = (x; y) \iff \vec{u} = x\vec{i} + y\vec{j}; \quad x_I = \frac{x_A + x_B}{2}",
     "Tọa độ trọng tâm tam giác: xG = (xA + xB + xC) / 3.",
     "Cho A(1; 3), B(5; 7). Hoành độ trung điểm I của AB bằng:", "3", "NUMERIC", [],
     "Cho A(2; 1) và B(4; 5). Tìm tọa độ vectơ AB.", "Tọa độ vectơ AB = (xB - xA; yB - yA) = (4 - 2; 5 - 1) = (2; 4)."),

    ("Bài 11: Tích vô hướng của hai vectơ", "Chương IV: Vectơ",
     "Tích vô hướng bằng tích độ dài nhân cosin góc giữa chúng: x1x2 + y1y2.",
     r"\vec{u} \cdot \vec{v} = |\vec{u}||\vec{v}|\cos(\vec{u}, \vec{v}) = x_1x_2 + y_1y_2; \quad \vec{u} \perp \vec{v} \iff x_1x_2 + y_1y_2 = 0",
     "Hai vectơ vuông góc với nhau khi và chỉ khi tích vô hướng bằng 0.",
     "Cho u = (2; -3) và v = (3; 2). Tích vô hướng u.v bằng:", "0", "NUMERIC", [],
     "Tính độ dài vectơ u = (3; 4).", "Độ dài vectơ u = căn(3^2 + 4^2) = căn(25) = 5."),

    ("Bài 12: Số gần đúng và sai số", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Sai số tuyệt đối đo khoảng cách giữa giá trị gần đúng và số đúng.",
     r"\Delta_a = |a - \overline{a}| \le d",
     "Quy tròn số: chữ số sau hàng quy tròn >= 5 thì tăng 1, < 5 giữ nguyên.",
     "Quy tròn số 12.3456 đến hàng phần trăm:", "12.35", "NUMERIC", [],
     "Xác định chữ số chắc của số gần đúng a = 12.34 với sai số d = 0.02.", "Chữ số hàng phần mười (3) và các hàng trước nó (1, 2) là chữ số chắc."),

    ("Bài 13: Các số đặc trưng đo xu thế trung tâm", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Số trung bình phản ánh giá trị trung tâm. Trung vị chia mẫu số liệu thành hai nửa.",
     r"\overline{x} = \frac{\sum x_i}{n}; \quad M_e = x_{\frac{n+1}{2}}",
     "Khi có số liệu đột biến (quá lớn/quá nhỏ), trung vị đại diện tốt hơn số trung bình.",
     "Trung vị của dãy điểm: 3, 5, 7, 8, 9 bằng:", "7", "NUMERIC", [],
     "Tìm mốt của mẫu số liệu: 5, 6, 7, 7, 8, 9.", "Số 7 xuất hiện nhiều nhất (2 lần) nên mốt Mo = 7."),

    ("Bài 14: Các số đặc trưng đo độ phân tán", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Khoảng biến thiên R = max - min. Khoảng tứ phân vị delta Q = Q3 - Q1.",
     r"R = x_{\max} - x_{\min}; \quad \Delta_Q = Q_3 - Q_1; \quad s = \sqrt{s^2}",
     "Độ lệch chuẩn s luôn cùng đơn vị với số liệu gốc.",
     "Mẫu số liệu có min = 10, max = 35. Khoảng biến thiên R bằng:", "25", "NUMERIC", [],
     "Tính khoảng biến thiên của mẫu: 2, 8, 12, 20.", "Giá trị lớn nhất là 20, nhỏ nhất là 2. Khoảng biến thiên R = 20 - 2 = 18."),

    ("Bài 15: Hàm số và đồ thị", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Hàm đồng biến khi x tăng y tăng; nghịch biến khi x tăng y giảm.",
     r"x_1 < x_2 \Rightarrow f(x_1) < f(x_2) \ (\text{Đồng biến})",
     "Điều kiện xác định: mẫu khác 0, biểu thức dưới căn bậc hai không âm.",
     "Hàm số y = (m - 2)x + 3 đồng biến trên R khi m > ?", "2", "NUMERIC", [],
     "Tìm tập xác định của hàm số y = 1 / (x - 3).", "Hàm số xác định khi mẫu số khác 0: x - 3 khác 0 <=> x khác 3. Tập xác định D = R \\ {3}."),

    ("Bài 16: Hàm số bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Đồ thị parabol có trục đối xứng x = -b/(2a), đỉnh I(-b/(2a); -Delta/(4a)).",
     r"y = ax^2 + bx + c; \quad I\left(-\frac{b}{2a}; -\frac{\Delta}{4a}\right)",
     "a > 0 bề lõm quay lên, a < 0 bề lõm quay xuống.",
     "Hoành độ đỉnh parabol y = x^2 - 6x + 5 bằng:", "3", "NUMERIC", [],
     "Xác định tọa độ đỉnh của parabol y = x^2 - 4x + 3.", "Hoành độ x = -b/(2a) = 4/2 = 2. Tung độ y = 2^2 - 4(2) + 3 = -1. Đỉnh I(2; -1)."),

    ("Bài 17: Dấu của tam thức bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Delta < 0 tam thức cùng dấu hệ số a. Delta > 0 trong trái ngoài cùng.",
     r"\Delta < 0 \Rightarrow a \cdot f(x) > 0, \ \forall x \in \mathbb{R}",
     "Khẩu quyết 'Trong trái ngoài cùng' chỉ áp dụng khi có 2 nghiệm phân biệt.",
     "Bất phương trình x^2 - 4x + 3 < 0 có nghiệm khoảng (1; b). b bằng:", "3", "NUMERIC", [],
     "Xét dấu của tam thức bậc hai f(x) = x^2 - 5x + 6.", "Phương trình có 2 nghiệm x=2, x=3. Hệ số a=1>0. Trong khoảng (2; 3) f(x) < 0; ngoài khoảng (-vô cực; 2) và (3; +vô cực) f(x) > 0."),

    ("Bài 18: Phương trình quy về phương trình bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Dạng căn f(x) = g(x) giải bằng cách đặt điều kiện g(x) >= 0 rồi bình phương.",
     r"\sqrt{f(x)} = g(x) \iff \begin{cases} g(x) \ge 0 \\ f(x) = [g(x)]^2 \end{cases}",
     "Bắt buộc đối chiếu điều kiện g(x) >= 0 để loại nghiệm ngoại lai.",
     "Số nghiệm thực của căn(2x - 3) = x - 3 là:", "1", "NUMERIC", [],
     "Giải phương trình căn(x - 1) = 2.", "Bình phương hai vế: x - 1 = 4 <=> x = 5 (thỏa mãn điều kiện x >= 1)."),

    ("Bài 19: Phương trình đường thẳng", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Đường thẳng qua M(x0; y0) có VTPT n(A; B) có dạng A(x - x0) + B(y - y0) = 0.",
     r"Ax + By + C = 0; \quad \vec{n} = (A; B) \perp \vec{u} = (-B; A)",
     "VTPT n(A; B) đổi thành VTCP u(-B; A).",
     "Đường thẳng 3x - 4y + 5 = 0 có một VTPT n = (3; b). b bằng:", "-4", "NUMERIC", [],
     "Viết phương trình đường thẳng qua M(1; 2) có VTPT n = (2; 1).", "Phương trình: 2(x - 1) + 1(y - 2) = 0 <=> 2x + y - 4 = 0."),

    ("Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Khoảng cách từ điểm M(x0; y0) đến đường thẳng Delta: Ax + By + C = 0.",
     r"d(M, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
     "Góc giữa hai đường thẳng không vượt quá 90 độ, tử số có giá trị tuyệt đối.",
     "Khoảng cách từ O(0; 0) đến 3x - 4y + 10 = 0 bằng:", "2", "NUMERIC", [],
     "Tính khoảng cách từ điểm A(1; 1) đến đường thẳng 3x + 4y - 2 = 0.", "d = |3(1) + 4(1) - 2| / căn(3^2 + 4^2) = |5| / 5 = 1."),

    ("Bài 21: Đường tròn trong mặt phẳng tọa độ", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Phương trình chính tắc (x - a)^2 + (y - b)^2 = R^2 tâm I(a; b) bán kính R.",
     r"(x - a)^2 + (y - b)^2 = R^2; \quad R = \sqrt{a^2 + b^2 - c}",
     "Chia hệ số của x và y cho -2 để tìm tọa độ tâm I.",
     "Bán kính đường tròn (x - 1)^2 + (y + 3)^2 = 25 bằng:", "5", "NUMERIC", [],
     "Tìm tâm và bán kính của đường tròn (x - 2)^2 + (y - 3)^2 = 16.", "Tâm I(2; 3), bán kính R = căn(16) = 4."),

    ("Bài 22: Ba đường conic", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Elip x^2/a^2 + y^2/b^2 = 1 (a^2 = b^2 + c^2). Hypebol x^2/a^2 - y^2/b^2 = 1.",
     r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1; \quad 2a: \text{Trục lớn}; \quad 2b: \text{Trục bé}",
     "Trong Elip, độ dài trục lớn là 2a, tiêu cự là 2c.",
     "Độ dài trục lớn của Elip x^2/25 + y^2/9 = 1 bằng:", "10", "NUMERIC", [],
     "Xác định độ dài trục bé của Elip x^2/25 + y^2/16 = 1.", "Ta có b^2 = 16 => b = 4. Độ dài trục bé 2b = 8."),

    ("Bài 23: Quy tắc đếm", "Chương VIII: Đại số tổ hợp",
     "Quy tắc cộng dùng cho phương án độc lập. Quy tắc nhân dùng cho công đoạn nối tiếp.",
     r"\text{Cộng: } N = m + n; \quad \text{Nhân: } N = m \times n",
     "Xong bước 1 xong luôn việc thì cộng; phải làm tiếp bước 2 mới xong thì nhân.",
     "Có 4 khai vị và 5 món chính. Số cách chọn 1 bữa ăn gồm 2 món là:", "20", "NUMERIC", [],
     "Một lớp có 15 bạn nam và 20 bạn nữ. Có bao nhiêu cách chọn 1 bạn làm lớp trưởng?", "Áp dụng quy tắc cộng: 15 + 20 = 35 cách."),

    ("Bài 24: Hoán vị, chỉnh hợp và tổ hợp", "Chương VIII: Đại số tổ hợp",
     "Hoán vị Pn = n!. Chỉnh hợp chọn có thứ tự. Tổ hợp chọn không thứ tự.",
     r"P_n = n!; \quad A_n^k = \frac{n!}{(n-k)!}; \quad C_n^k = \frac{n!}{k!(n-k)!}",
     "Đổi thứ tự tạo kết quả mới thì dùng Chỉnh hợp, không đổi thứ tự thì dùng Tổ hợp.",
     "Số cách chọn 2 bạn từ 5 bạn đi lao động là:", "10", "NUMERIC", [],
     "Có bao nhiêu cách xếp 3 bạn học sinh ngồi vào 3 chiếc ghế?", "Số cách là số hoán vị của 3 phần tử: P3 = 3! = 6 cách."),

    ("Bài 25: Nhị thức Newton", "Chương VIII: Đại số tổ hợp",
     "Khai triển (a + b)^4 và (a + b)^5 với hệ số nhị thức đối xứng.",
     r"(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4",
     "Khi khai triển (a - b)^n dấu cộng trừ xen kẽ.",
     "Hệ số của x^3 trong (x + 1)^4 bằng:", "4", "NUMERIC", [],
     "Khai triển nhị thức (x + 2)^4.", "(x + 2)^4 = x^4 + 4*x^3*2 + 6*x^2*4 + 4*x*8 + 16 = x^4 + 8x^3 + 24x^2 + 32x + 16."),

    ("Bài 26: Biến cố và định nghĩa cổ điển của xác suất", "Chương IX: Tính xác suất theo định nghĩa cổ điển",
     "Xác suất P(A) = n(A) / n(Omega). Biến cố đối P(A ngang) = 1 - P(A).",
     r"P(A) = \frac{n(A)}{n(\Omega)}; \quad P(\overline{A}) = 1 - P(A)",
     "Xác suất chắc chắn bằng 1, không thể bằng 0.",
     "Gieo xúc xắc 6 mặt cân đối. Xác suất xuất hiện mặt chẵn là:", "0.5", "NUMERIC", [],
     "Gieo một đồng xu cân đối 2 lần. Tính xác suất để cả 2 lần đều xuất hiện mặt sấp.", "Không gian mẫu: {SS, SN, NS, NN} (4 phần tử). Biến cố cả hai sấp: {SS} (1 phần tử). Xác suất P = 1/4 = 0.25."),

    ("Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển", "Chương IX: Tính xác suất theo định nghĩa cổ điển",
     "Sử dụng công thức tổ hợp và phương pháp biến cố đối khi có từ 'ít nhất'.",
     r"n(\Omega) = C_n^k; \quad P(A) = 1 - P(\overline{A})",
     "Đề bài có 'ít nhất một...', hãy tính qua biến cố đối 'không có cái nào'.",
     "Hộp có 3 bi đỏ và 2 xanh. Lấy ngẫu nhiên 1 bi. Xác suất bi đỏ bằng:", "0.6", "NUMERIC", [],
     "Lấy ngẫu nhiên 2 viên bi từ hộp có 4 bi đỏ và 3 bi xanh. Tính số phần tử không gian mẫu.", "Số phần tử không gian mẫu là số cách chọn 2 viên bi từ 7 viên bi: n(Omega) = C(7, 2) = 21.")
]

RAW_LESSONS_11 = [
    ("Bài 1: Giá trị lượng giác của góc lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Trục sin đứng, trục cos nằm. Góc phần tư thứ II có sin dương, cos âm.",
     r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
     "Nhất cả (I: all > 0), Nhì sin (II: sin > 0), Tam tang (III: tan > 0), Tứ cos (IV: cos > 0).",
     "Góc alpha thuộc góc II và sin alpha = 3/5. Giá trị cos alpha bằng:", "-0.8", "NUMERIC", ["-4/5", "-0,8"],
     "Cho cos alpha = 4/5 với 0 < alpha < pi/2. Tính sin alpha.", "Vì 0 < alpha < pi/2 nên sin alpha > 0. Suy ra sin alpha = căn(1 - (4/5)^2) = 3/5 = 0.6."),

    ("Bài 2: Công thức lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Công thức cộng, công thức nhân đôi sin 2a = 2 sin a cos a.",
     r"\cos(a \pm b) = \cos a\cos b \mp \sin a\sin b; \quad \sin 2a = 2\sin a\cos a",
     "Công thức nhân đôi cos 2a có 3 dạng biểu diễn khác nhau.",
     "Nếu sin a * cos a = 0.25 thì sin 2a bằng:", "0.5", "NUMERIC", [],
     "Tính giá trị của sin(75 độ) theo công thức cộng.", "sin(75°) = sin(45° + 30°) = sin(45°)cos(30°) + cos(45°)sin(30°) = (căn 6 + căn 2) / 4."),

    ("Bài 3: Hàm số lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Hàm sin và cos tuần hoàn chu kỳ 2pi, tập giá trị [-1; 1].",
     r"y = \sin x \ (T = 2\pi); \quad y = \cos x \ (T = 2\pi)",
     "y = sin x là hàm lẻ, y = cos x là hàm chẵn.",
     "Giá trị lớn nhất của hàm số y = 3sin x + 2 bằng:", "5", "NUMERIC", [],
     "Tìm tập xác định của hàm số y = tan x.", "Hàm số tan x = sin x / cos x xác định khi cos x khác 0 <=> x khác pi/2 + k*pi."),

    ("Bài 4: Phương trình lượng giác cơ bản", "Chương I: Hàm số và phương trình lượng giác",
     "sin x = sin alpha có nghiệm alpha và pi - alpha cộng k2pi.",
     r"\sin x = \sin\alpha \iff \left[\begin{array}{l} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{array}\right.",
     "Phương trình sin x = m có nghiệm khi -1 <= m <= 1.",
     "Số nghiệm của sin x = 1 trên đoạn [0; 2pi] là:", "1", "NUMERIC", [],
     "Giải phương trình cos x = 1/2.", "cos x = cos(pi/3) <=> x = pi/3 + k2pi hoặc x = -pi/3 + k2pi (k thuộc Z)."),

    ("Bài 5: Dãy số", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Dãy số un là hàm số trên N*. Dãy tăng khi u(n+1) > un với mọi n.",
     r"(u_n): u_{n+1} > u_n \ (\text{Dãy tăng})",
     "Có thể xét hiệu u(n+1) - un để kết luận tính tăng giảm.",
     "Cho dãy số un = 2n + 1. Số hạng thứ 3 (u3) bằng:", "7", "NUMERIC", [],
     "Viết 3 số hạng đầu tiên của dãy số un = 1 / n.", "Với n = 1: u1 = 1; n = 2: u2 = 1/2; n = 3: u3 = 1/3."),

    ("Bài 6: Cấp số cộng", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Số hạng tổng quát un = u1 + (n - 1)d. Tổng Sn = n(u1 + un)/2.",
     r"u_n = u_1 + (n - 1)d; \quad S_n = \frac{n(u_1 + u_n)}{2}",
     "Ba số a, b, c lập thành cấp số cộng khi a + c = 2b.",
     "Cấp số cộng có u1 = 3, d = 4. Số hạng thứ 5 bằng:", "19", "NUMERIC", [],
     "Cho cấp số cộng có u1 = 2 và công sai d = 5. Tính tổng 10 số hạng đầu.", "S10 = 10 * [2*2 + 9*5] / 2 = 5 * [4 + 45] = 5 * 49 = 245."),

    ("Bài 7: Cấp số nhân", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Số hạng tổng quát un = u1 * q^(n-1). Tổng Sn = u1*(1 - q^n)/(1 - q).",
     r"u_n = u_1 \cdot q^{n-1}; \quad S_n = u_1 \frac{1 - q^n}{1 - q}",
     "Ba số a, b, c lập thành cấp số nhân khi a * c = b^2.",
     "Cấp số nhân có u1 = 2, q = 3. Số hạng thứ 3 bằng:", "18", "NUMERIC", [],
     "Tìm công bội q của cấp số nhân có u1 = 3 và u2 = 6.", "Công bội q = u2 / u1 = 6 / 3 = 2."),

    ("Bài 8: Mẫu số liệu ghép nhóm", "Chương III: Các số đặc trưng đo xu thế trung tâm",
     "Mẫu ghép nhóm theo nửa khoảng [a; b). Giá trị đại diện là trung điểm.",
     r"c_i = \frac{a_i + a_{i+1}}{2}; \quad n = \sum n_i",
     "Độ dài của nhóm bằng b - a.",
     "Giá trị đại diện của nhóm [20; 30) bằng:", "25", "NUMERIC", [],
     "Một nhóm có khoảng [150; 160) với tần số 12. Xác định giá trị đại diện.", "Giá trị đại diện ci = (150 + 160) / 2 = 155."),

    ("Bài 9: Các số đặc trưng đo xu thế trung tâm", "Chương III: Các số đặc trưng đo xu thế trung tâm",
     "Trung vị Me chia mẫu số liệu ghép nhóm thành hai phần bằng nhau.",
     r"M_e = u_m + \frac{\frac{n}{2} - C}{n_m}(u_{m+1} - u_m)",
     "Nhóm chứa trung vị có tần số tích lũy tối thiểu bằng n/2.",
     "Mẫu có cỡ mẫu n = 40. Tần số tích lũy nhóm trung vị tối thiểu là:", "20", "NUMERIC", [],
     "Nêu ý nghĩa của mốt trong mẫu số liệu ghép nhóm.", "Mốt là giá trị phản ánh nhóm có mật độ xuất hiện thường xuyên nhất trong tập dữ liệu."),

    ("Bài 10: Đường thẳng và mặt phẳng trong không gian", "Chương IV: Quan hệ song song trong không gian",
     "Ba điểm không thẳng hàng xác định duy nhất 1 mặt phẳng.",
     r"(ABC); \quad (d, A) \ (A \notin d)",
     "Tứ diện đều có tất cả 6 cạnh bằng nhau.",
     "Số mặt phẳng đi qua 3 điểm không thẳng hàng là:", "1", "NUMERIC", [],
     "Hình chóp tứ giác có bao nhiêu mặt bên?", "Hình chóp tứ giác có đáy là tứ giác nên có đúng 4 mặt bên là các tam giác."),

    ("Bài 11: Hai đường thẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "Hai đường thẳng song song cùng nằm trong 1 mặt phẳng và không có điểm chung.",
     r"a \parallel b \iff a, b \subset (P) \text{ và } a \cap b = \emptyset",
     "Hai đường chéo nhau không cùng nằm trong bất kỳ mặt phẳng nào.",
     "Hai đường thẳng không điểm chung thì chắc chắn song song? (1: Đúng, 0: Sai)", "0", "NUMERIC", [],
     "Cho tứ diện ABCD. Hai đường thẳng AB và CD có vị trí tương đối gì?", "AB và CD không cùng thuộc mặt phẳng nào nên AB và CD chéo nhau."),

    ("Bài 12: Đường thẳng và mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "d song song (P) khi d không nằm trong (P) và d song song với 1 đường trong (P).",
     r"\begin{cases} d \not\subset (P) \\ d \parallel a \subset (P) \end{cases} \Rightarrow d \parallel (P)",
     "Mặt phẳng qua d cắt (P) theo giao tuyến song song d.",
     "d nằm trong (P) thì d có song song (P) không? (1: Có, 0: Không)", "0", "NUMERIC", [],
     "Cho hình chóp S.ABCD đáy ABCD là hình bình hành. Chứng minh AB song song (SCD).", "Ta có AB // CD mà CD nằm trong (SCD), AB không nằm trong (SCD) nên AB // (SCD)."),

    ("Bài 13: Hai mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "(P) chứa 2 đường cắt nhau cùng song song với (Q) thì (P) song song (Q).",
     r"\begin{cases} a, b \subset (P), \ a \cap b = I \\ a \parallel (Q), \ b \parallel (Q) \end{cases} \Rightarrow (P) \parallel (Q)",
     "Định lý Thales bảo toàn tỉ số đoạn thẳng chắn trên cát tuyến.",
     "Hai mặt phẳng cùng song song mặt phẳng thứ ba thì song song nhau? (1: Đúng, 0: Sai)", "1", "NUMERIC", [],
     "Mặt phẳng (P) song song (Q). Một đường thẳng a nằm trong (P) có song song (Q) không?", "Có, đường thẳng a song song với toàn bộ mặt phẳng (Q)."),

    ("Bài 14: Phép chiếu song song", "Chương IV: Quan hệ song song trong không gian",
     "Phép chiếu song song bảo toàn tính song song và tỉ số đoạn thẳng.",
     r"\text{Chiếu song song: Biến đoạn thẳng thành đoạn thẳng}",
     "Hình chiếu của hình tròn là hình elip hoặc đoạn thẳng.",
     "Phép chiếu song song luôn bảo toàn độ lớn góc? (1: Có, 0: Không)", "0", "NUMERIC", [],
     "Hình chiếu song song của hình bình hành có thể là hình gì?", "Có thể là một hình bình hành hoặc một đoạn thẳng (khi mặt phẳng chứa hình song song phương chiếu)."),

    ("Bài 15: Giới hạn của dãy số", "Chương V: Giới hạn. Hàm số liên tục",
     "Giới hạn 1/n^k = 0. Tổng cấp số nhân lùi vô hạn S = u1/(1 - q).",
     r"\lim_{n \to \infty} \frac{1}{n^k} = 0; \quad S = \frac{u_1}{1 - q}",
     "Chia cả tử và mẫu cho lũy thừa cao nhất của n.",
     "Giới hạn lim (4n + 3)/(2n - 1) bằng:", "2", "NUMERIC", [],
     "Tính tổng cấp số nhân lùi vô hạn có u1 = 1, công bội q = 1/2.", "Áp dụng công thức S = u1 / (1 - q) = 1 / (1 - 1/2) = 2."),

    ("Bài 16: Giới hạn của hàm số", "Chương V: Giới hạn. Hàm số liên tục",
     "Khử dạng 0/0 bằng phân tích nhân tử (x - x0) hoặc nhân liên hợp.",
     r"\lim_{x \to x_0} \frac{f(x)}{g(x)} \ (\text{Dạng } \frac{0}{0})",
     "Lượng liên hợp: căn A - B = (A - B^2) / (căn A + B).",
     "Giới hạn lim (x^2 - 1)/(x - 1) khi x tiến tới 1 bằng:", "2", "NUMERIC", [],
     "Tính giới hạn lim (x + 2) khi x tiến tới 3.", "Thay trực tiếp: lim (x + 2) = 3 + 2 = 5."),

    ("Bài 17: Hàm số liên tục", "Chương V: Giới hạn. Hàm số liên tục",
     "Hàm liên tục tại x0 khi giới hạn tại x0 bằng f(x0).",
     r"\lim_{x \to x_0} f(x) = f(x_0); \quad f(a)f(b) < 0 \Rightarrow \exists c: f(c) = 0",
     "Hàm đa thức liên tục trên toàn R.",
     "Hàm số y = 1/(x - 2) liên tục tại x = 2 không? (1: Có, 0: Không)", "0", "NUMERIC", [],
     "Chứng minh phương trình x^3 + x - 1 = 0 có nghiệm trên khoảng (0; 1).", "Hàm số f(x) = x^3 + x - 1 liên tục trên [0; 1]. Ta có f(0) = -1 < 0 và f(1) = 1 > 0. Vì f(0)*f(1) < 0 nên phương trình có ít nhất 1 nghiệm thuộc (0; 1)."),

    ("Bài 18: Lũy thừa với số mũ thực", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Lũy thừa số mũ hữu tỉ yêu cầu cơ số dương a > 0.",
     r"a^\alpha \cdot a^\beta = a^{\alpha + \beta}; \quad a^{\frac{m}{n}} = \sqrt[n]{a^m}",
     "Cơ số phải dương khi xét số mũ hữu tỉ.",
     "Giá trị của 2^3 * 2^2 bằng:", "32", "NUMERIC", [],
     "Rút gọn biểu thức: a^(1/2) * a^(3/2) (với a > 0).", "Ta có: a^(1/2 + 3/2) = a^(4/2) = a^2."),

    ("Bài 19: Lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "log_a b = alpha khi a^alpha = b. Điều kiện a > 0, a khác 1, b > 0.",
     r"\log_a b = \alpha \iff a^\alpha = b; \quad \log_a(xy) = \log_a x + \log_a y",
     "Biểu thức dưới dấu logarit bắt buộc phải dương.",
     "Giá trị của log_2(16) bằng:", "4", "NUMERIC", [],
     "Tính giá trị của log_3(9) + log_3(1).", "log_3(9) = 2, log_3(1) = 0. Tổng bằng 2 + 0 = 2."),

    ("Bài 20: Hàm số mũ và hàm số lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Hàm mũ y = a^x và logarit y = log_a x đồng biến khi a > 1, nghịch biến khi 0 < a < 1.",
     r"y = a^x; \quad y = \log_a x; \quad a > 1: \text{Đồng biến}",
     "Đồ thị hàm mũ tiệm cận ngang Ox; hàm logarit tiệm cận đứng Oy.",
     "Hàm số y = (0.5)^x đồng biến hay nghịch biến? (1: Nghịch biến, 0: Đồng biến)", "1", "NUMERIC", [],
     "Tìm tập xác định của hàm số y = log_2(x - 3).", "Điều kiện x - 3 > 0 <=> x > 3. Tập xác định D = (3; +vô cực)."),

    ("Bài 21: Phương trình, bất phương trình mũ và lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Đưa về cùng cơ số. Đổi chiều khi cơ số 0 < a < 1.",
     r"a^{f(x)} = a^{g(x)} \iff f(x) = g(x)",
     "Luôn đặt điều kiện xác định trước khi giải bất phương trình logarit.",
     "Nghiệm phương trình 2^(x - 1) = 8 là x bằng:", "4", "NUMERIC", [],
     "Giải phương trình log_2(x) = 3.", "Điều kiện x > 0. Phương trình <=> x = 2^3 = 8 (thỏa mãn)."),

    ("Bài 22: Hai đường thẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian",
     "Góc giữa 2 đường thẳng từ 0 đến 90 độ. Vuông góc khi góc bằng 90 độ.",
     r"0^\circ \le \widehat{(a, b)} \le 90^\circ; \quad a \perp b \iff \vec{u}_a \cdot \vec{u}_b = 0",
     "Hai đường chéo nhau vẫn có thể vuông góc nhau.",
     "Góc giữa 2 đường thẳng có thể bằng 120 độ? (1: Có, 0: Không)", "0", "NUMERIC", [],
     "Cho hình lập phương ABCD.A'B'C'D'. Tính góc giữa AB và B'C'.", "Do B'C' // AD nên góc giữa AB và B'C' bằng góc giữa AB và AD = 90 độ."),

    ("Bài 23: Đường thẳng vuông góc với mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian",
     "d vuông góc (P) khi d vuông góc 2 đường cắt nhau trong (P).",
     r"\begin{cases} d \perp a, \ d \perp b \subset (P) \\ a \cap b = I \end{cases} \Rightarrow d \perp (P)",
     "Khi d vuông góc (P) thì d vuông góc với mọi đường trong (P).",
     "SA vuông góc đáy (ABC). SA có vuông góc BC không? (1: Có, 0: Không)", "1", "NUMERIC", [],
     "Cho hình chóp S.ABC có SA vuông góc đáy, tam giác ABC vuông tại B. Chứng minh BC vuông góc (SAB).", "BC vuông góc AB (tam giác vuông) và BC vuông góc SA (do SA vuông góc đáy). Vậy BC vuông góc (SAB)."),

    ("Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian",
     "Góc giữa đường thẳng d và mặt phẳng (P) là góc giữa d và hình chiếu d'.",
     r"\varphi = \widehat{(d, (P))} = \widehat{(d, d')}; \quad \tan\varphi = \frac{SH}{AH}",
     "Tìm chân đường vuông góc H hạ từ đỉnh S xuống mặt phẳng.",
     "SA vuông góc đáy và SA = AB = a. Góc giữa SB và đáy bằng:", "45", "NUMERIC", [],
     "Cho chóp S.ABC có SA vuông góc (ABC). Hình chiếu của SB lên đáy là đoạn nào?", "Hình chiếu của S là A, hình chiếu của B là B. Vậy hình chiếu của SB lên (ABC) là đoạn AB."),

    ("Bài 25: Hai mặt phẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian",
     "(P) chứa đường vuông góc với (Q) thì (P) vuông góc (Q).",
     r"d \perp (Q), \ d \subset (P) \Rightarrow (P) \perp (Q)",
     "Đường trong mặt này vuông góc giao tuyến thì vuông góc mặt kia.",
     "SA vuông góc đáy thì (SAB) có vuông góc đáy không? (1: Có, 0: Không)", "1", "NUMERIC", [],
     "Cho hình chóp S.ABCD có đáy là hình vuông, SA vuông góc đáy. Chứng minh (SAB) vuông góc (SBC).", "Do BC vuông góc (SAB) mà BC nằm trong (SBC) nên (SBC) vuông góc (SAB)."),

    ("Bài 26: Khoảng cách trong không gian", "Chương VII: Quan hệ vuông góc trong không gian",
     "Khoảng cách từ điểm đến mặt phẳng, khoảng cách 2 đường chéo nhau.",
     r"d(M, (P)) = MH \ (MH \perp (P))",
     "Kỹ thuật đổi điểm: Chuyển khoảng cách về chân đường cao.",
     "SA vuông góc đáy, SA = 5. Khoảng cách từ S đến đáy bằng:", "5", "NUMERIC", [],
     "Cho hình chóp S.ABC có SA vuông góc đáy, SA = 4. Khoảng cách từ S đến mặt phẳng (ABC) bằng bao nhiêu?", "Khoảng cách chính bằng độ dài đoạn SA = 4."),

    ("Bài 27: Thể tích", "Chương VII: Quan hệ vuông góc trong không gian",
     "Thể tích lăng trụ V = B*h. Thể tích chóp V = (1/3)*B*h.",
     r"V_{\text{lăng trụ}} = S_{\text{đáy}} \cdot h; \quad V_{\text{chóp}} = \frac{1}{3} S_{\text{đáy}} \cdot h",
     "Công thức Simson chỉ áp dụng cho hình chóp tam giác.",
     "Khối chóp có đáy bằng 9, chiều cao bằng 4. Thể tích bằng:", "12", "NUMERIC", [],
     "Tính thể tích khối lăng trụ có diện tích đáy bằng 10 và chiều cao bằng 6.", "V = B * h = 10 * 6 = 60."),

    ("Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất",
     "Biến cố giao cùng xảy ra. Độc lập khi xác suất không ảnh hưởng nhau.",
     r"P(AB) = P(A) \cdot P(B) \ (\text{Độc lập})",
     "Xung khắc thì giao bằng rỗng P(AB) = 0.",
     "A và B xung khắc thì P(AB) bằng:", "0", "NUMERIC", [],
     "Gieo 1 đồng xu và 1 con xúc xắc. Hai biến cố này có độc lập không?", "Có, kết quả gieo đồng xu không làm thay đổi xác suất xuất hiện số chấm của con xúc xắc."),

    ("Bài 29: Công thức cộng xác suất", "Chương VIII: Các quy tắc tính xác suất",
     "P(A hợp B) = P(A) + P(B) - P(AB). Khi xung khắc trừ 0.",
     r"P(A \cup B) = P(A) + P(B) \ (A, B \text{ xung khắc})",
     "Trừ phần giao nếu hai biến cố không xung khắc.",
     "A và B xung khắc, P(A)=0.3, P(B)=0.4. P(A hợp B) bằng:", "0.7", "NUMERIC", [],
     "Cho P(A) = 0.5, P(B) = 0.3, P(AB) = 0.1. Tính P(A hợp B).", "P(A hợp B) = P(A) + P(B) - P(AB) = 0.5 + 0.3 - 0.1 = 0.7."),

    ("Bài 30: Công thức nhân xác suất cho hai biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất",
     "A và B độc lập: P(AB) = P(A) * P(B).",
     r"P(AB) = P(A) \cdot P(B)",
     "Xác suất ít nhất một người trúng = 1 - P(cả hai cùng trượt).",
     "Hai xạ thủ bắn độc lập, xác suất trúng 0.6 và 0.7. Cả hai cùng trúng bằng:", "0.42", "NUMERIC", [],
     "Xác suất bắn trượt của 2 xạ thủ lần lượt là 0.4 và 0.3. Tính xác suất cả hai cùng trượt.", "P = 0.4 * 0.3 = 0.12."),

    ("Bài 31: Định nghĩa và ý nghĩa của đạo hàm", "Chương IX: Đạo hàm",
     "Hệ số góc tiếp tuyến k = f'(x0). Tiếp tuyến: y = f'(x0)(x - x0) + y0.",
     r"f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}",
     "Hệ số góc của tiếp tuyến tại tiếp điểm x0 chính là f'(x0).",
     "Tiếp tuyến của y = x^2 tại x0 = 2 có hệ số góc bằng:", "4", "NUMERIC", [],
     "Viết phương trình tiếp tuyến của đồ thị hàm số y = x^2 tại điểm có hoành độ x = 1.", "y' = 2x => y'(1) = 2. Tại x = 1 thì y = 1. Phương trình tiếp tuyến: y - 1 = 2(x - 1) <=> y = 2x - 1."),

    ("Bài 32: Các quy tắc tính đạo hàm", "Chương IX: Đạo hàm",
     "Đạo hàm tổng, hiệu, tích, thương và đạo hàm hàm hợp [f(u)]' = f'(u)*u'.",
     r"(uv)' = u'v + uv'; \quad [f(u)]' = f'(u) \cdot u'",
     "Luôn nhân thêm u' ở cuối khi tính đạo hàm hàm hợp.",
     "Đạo hàm của f(x) = x^3 - 3x tại x = 2 bằng:", "9", "NUMERIC", [],
     "Tính đạo hàm của hàm số y = (2x + 1)^3.", "Áp dụng công thức đạo hàm hàm hợp: y' = 3*(2x + 1)^2 * (2x + 1)' = 6*(2x + 1)^2."),

    ("Bài 33: Đạo hàm cấp hai", "Chương IX: Đạo hàm",
     "Đạo hàm cấp hai y'' = (y')'. Gia tốc tức thời a(t) = s''(t).",
     r"y'' = (y')'; \quad a(t) = s''(t)",
     "Đạo hàm cấp hai dùng tìm điểm uốn và xét tính lồi lõm.",
     "Vật chuyển động theo s(t) = t^3. Gia tốc tại t = 2 giây bằng:", "12", "NUMERIC", [],
     "Tìm đạo hàm cấp hai của hàm số y = x^4.", "Đạo hàm cấp một: y' = 4x^3. Đạo hàm cấp hai: y'' = 12x^2.")
]

RAW_LESSONS_12 = [
    ("Bài 1: Tính đơn điệu và cực trị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Đồng biến khi f'(x) >= 0; nghịch biến khi f'(x) <= 0. Cực đại đổi từ + sang -, cực tiểu từ - sang +.",
     r"f'(x) \ge 0 \ (\text{Đồng biến}); \quad f'(x_0) = 0 \text{ đổi } (+) \to (-) \ (\text{Cực đại})",
     "Phân biệt điểm cực trị của hàm số (x0) và giá trị cực trị (y0).",
     "Giá trị cực tiểu của y = x^3 - 3x + 2 bằng:", "0", "NUMERIC", [],
     "Tìm các khoảng đơn điệu của hàm số y = x^3 - 3x.", "y' = 3x^2 - 3 = 0 <=> x = 1 hoặc x = -1. Hàm số đồng biến trên (-vô cực; -1) và (1; +vô cực); nghịch biến trên (-1; 1)."),

    ("Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Tìm GTLN, GTNN trên đoạn [a; b] qua giá trị 2 đầu mút và nghiệm f'(x) = 0.",
     r"\max_{[a; b]} f(x); \quad \min_{[a; b]} f(x)",
     "Chỉ lấy các nghiệm xi nằm trong khoảng (a; b).",
     "GTLN của f(x) = x^3 - 3x + 1 trên [0; 2] bằng:", "3", "NUMERIC", [],
     "Tìm giá trị nhỏ nhất của hàm số y = x^2 - 4x + 5 trên đoạn [0; 3].", "y' = 2x - 4 = 0 <=> x = 2 (thuộc [0; 3]). Tính y(0) = 5, y(2) = 1, y(3) = 2. Vậy GTNN bằng 1."),

    ("Bài 3: Đường tiệm cận của đồ thị hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Tiệm cận đứng x = x0 (mẫu triệt tiêu, tử khác 0). Tiệm cận ngang y = y0 khi x ra vô cực.",
     r"\lim_{x \to x_0} y = \infty \Rightarrow x = x_0; \quad \lim_{x \to \infty} y = y_0 \Rightarrow y = y_0",
     "Hàm nhất biến y = (ax+b)/(cx+d) có TCĐ x = -d/c và TCN y = a/c.",
     "Tiệm cận ngang của y = (2x - 3)/(x + 1) là y bằng:", "2", "NUMERIC", [],
     "Tìm tiệm cận đứng của đồ thị hàm số y = 1 / (x - 2).", "Mẫu số triệt tiêu tại x = 2 và tử số khác 0 nên đường thẳng x = 2 là tiệm cận đứng."),

    ("Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Quy trình khảo sát hàm số: TXĐ, đạo hàm, cực trị, tiệm cận, bảng biến thiên, đồ thị.",
     r"y = ax^3 + bx^2 + cx + d; \quad y = \frac{ax+b}{cx+d}",
     "Đồ thị hàm bậc ba nhận điểm uốn làm tâm đối xứng.",
     "Tâm đối xứng của y = (2x - 3)/(x + 1) có hoành độ bằng:", "-1", "NUMERIC", [],
     "Tìm tọa độ giao điểm của đồ thị hàm số y = x^3 - 3x + 2 với trục tung Oy.", "Cho x = 0 => y = 2. Giao điểm là M(0; 2)."),

    ("Bài 5: Ứng dụng đạo hàm giải quyết bài toán thực tiễn", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Lập hàm số mục tiêu theo 1 biến x rồi tìm giá trị tối ưu bằng đạo hàm f'(x) = 0.",
     r"V'(x) = 0; \quad S(x) = x^2 + \frac{128}{x}",
     "Đối chiếu nghiệm với điều kiện độ dài thực tế phải dương.",
     "Hộp không nắp đáy vuông V = 32 dm^3. Diện tích vật liệu nhỏ nhất bằng:", "48", "NUMERIC", [],
     "Một mảnh vườn hình chữ nhật có chu vi 40m. Tìm diện tích lớn nhất.", "Nửa chu vi là 20m. Gọi chiều rộng là x (0 < x < 20), chiều dài là 20 - x. Diện tích S(x) = x(20 - x) = -x^2 + 20x đạt GTLN tại x = 10, S_max = 100 m^2."),

    ("Bài 6: Vectơ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Quy tắc hình hộp AC' = AB + AD + AA'. Định lý đồng phẳng 3 vectơ.",
     r"\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}",
     "Tích vô hướng trong không gian bằng tích độ dài nhân cos góc xen giữa.",
     "Cho hình hộp ABCD.A'B'C'D'. AB + AD + AA' bằng: (A: AC', B: BD')", "A", "CHOICE", ["A. Vectơ AC'", "B. Vectơ BD'"],
     "Trong không gian, cho tứ diện ABCD. Rút gọn biểu thức vectơ AB + BC + CD.", "Theo quy tắc cộng 3 điểm: AB + BC + CD = AC + CD = AD."),

    ("Bài 7: Hệ trục tọa độ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Hệ trục Oxyz gồm 3 trục vuông góc. Tọa độ điểm M(x; y; z).",
     r"\vec{OM} = x\vec{i} + y\vec{j} + z\vec{k} \iff M(x; y; z)",
     "Chiếu vuông góc lên trục Oz thì x = y = 0, giữ nguyên z.",
     "Chiếu điểm M(2; -3; 4) lên trục Oz có cao độ z bằng:", "4", "NUMERIC", [],
     "Tìm tọa độ trung điểm I của đoạn thẳng AB với A(1; 2; 3) và B(3; 0; 1).", "xI = (1+3)/2 = 2, yI = (2+0)/2 = 1, zI = (3+1)/2 = 2. Tọa độ I(2; 1; 2)."),

    ("Bài 8: Biểu thức tọa độ của các phép toán vectơ", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Tích vô hướng x1x2 + y1y2 + z1z2. Độ dài vectơ căn tổng bình phương tọa độ.",
     r"\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2; \quad |\vec{u}| = \sqrt{x^2 + y^2 + z^2}",
     "Hai vectơ vuông góc khi tích vô hướng bằng 0.",
     "Độ dài của vectơ a = (2; -3; 6) bằng:", "7", "NUMERIC", [],
     "Cho hai vectơ u = (1; 2; -1) và v = (2; -1; 3). Tính tích vô hướng u.v.", "u.v = 1*2 + 2*(-1) + (-1)*3 = 2 - 2 - 3 = -3."),

    ("Bài 9: Khoảng biến thiên và khoảng tứ phân vị", "Chương III: Các số đặc trưng đo mức độ phân tán",
     "Khoảng biến thiên R = max - min. Khoảng tứ phân vị delta Q = Q3 - Q1.",
     r"R = a_{k+1} - a_1; \quad \Delta_Q = Q_3 - Q_1",
     "Khoảng tứ phân vị ít bị ảnh hưởng bởi giá trị bất thường.",
     "Mẫu có Q1 = 12 và Q3 = 15.5 thì khoảng tứ phân vị bằng:", "3.5", "NUMERIC", [],
     "Nêu công thức tính khoảng biến thiên của mẫu số liệu ghép nhóm.", "Khoảng biến thiên R bằng đầu mút phải của nhóm cuối trừ đầu mút trái của nhóm đầu."),

    ("Bài 10: Phương sai và độ lệch chuẩn", "Chương III: Các số đặc trưng đo mức độ phân tán",
     "Phương sai s^2 đo độ phân tán quanh số trung bình. Độ lệch chuẩn s = căn(s^2).",
     r"s^2 = \frac{1}{n} \sum n_i c_i^2 - (\overline{x})^2; \quad s = \sqrt{s^2}",
     "Độ lệch chuẩn càng nhỏ số liệu càng tập trung đều quanh số trung bình.",
     "Phương sai mẫu bằng 16 thì độ lệch chuẩn s bằng:", "4", "NUMERIC", [],
     "Tính độ lệch chuẩn nếu biết phương sai của mẫu ghép nhóm bằng 25.", "Độ lệch chuẩn s = căn(25) = 5."),

    ("Bài 11: Nguyên hàm", "Chương IV: Nguyên hàm và tích phân",
     "Hàm F(x) là nguyên hàm khi F'(x) = f(x). Nguyên hàm x^n bằng x^(n+1)/(n+1).",
     r"\int x^\alpha dx = \frac{x^{\alpha+1}}{\alpha+1} + C; \quad \int \frac{1}{x} dx = \ln|x| + C",
     "Không được quên hằng số C và dấu giá trị tuyệt đối của ln|x|.",
     "F(x) là nguyên hàm của f(x) = 2x. Hiệu số F(2) - F(0) bằng:", "4", "NUMERIC", [],
     "Tìm một nguyên hàm của hàm số f(x) = 3x^2.", "Nguyên hàm của 3x^2 là F(x) = x^3 + C. Một nguyên hàm là F(x) = x^3."),

    ("Bài 12: Tích phân", "Chương IV: Nguyên hàm và tích phân",
     "Định lý Newton-Leibniz: Tích phân từ a đến b bằng F(b) - F(a).",
     r"\int_a^b f(x)dx = F(b) - F(a); \quad \int_a^b u \, dv = uv\Big|_a^b - \int_a^b v \, du",
     "Thứ tự đặt u trong từng phần: Nhất lô, nhì đa, tam lượng, tứ mũ.",
     "Tích phân từ 0 đến 2 của (2x + 1)dx bằng:", "6", "NUMERIC", [],
     "Tính tích phân từ 1 đến 2 của 2x dx.", "Nguyên hàm của 2x là x^2. Tích phân = x^2 | cận 1 đến 2 = 2^2 - 1^2 = 4 - 1 = 3."),

    ("Bài 13: Ứng dụng hình học của tích phân", "Chương IV: Nguyên hàm và tích phân",
     "Diện tích hình phẳng giới hạn bởi đồ thị và trục Ox: tích phân trị tuyệt đối.",
     r"S = \int_a^b |f(x)| dx; \quad V_x = \pi \int_a^b [f(x)]^2 dx",
     "Thể tích tròn xoay quanh Ox luôn có nhân tử pi ở phía trước.",
     "Diện tích giới hạn bởi y = x^2 - 4x và Ox bằng: (Nhập a/b)", "32/3", "NUMERIC", ["10.67", "32/3"],
     "Tính diện tích hình phẳng giới hạn bởi đường cong y = x^2, trục hoành và hai đường thẳng x = 0, x = 1.", "S = tích phân từ 0 đến 1 của x^2 dx = [x^3 / 3] | cận 0 đến 1 = 1/3."),

    ("Bài 14: Phương trình mặt phẳng", "Chương V: Phương pháp tọa độ trong không gian",
     "Mặt phẳng qua M(x0; y0; z0) có VTPT n(A; B; C): A(x-x0) + B(y-y0) + C(z-z0) = 0.",
     r"Ax + By + Cz + D = 0; \quad d(M, (P)) = \frac{|Ax_M + By_M + Cz_M + D|}{\sqrt{A^2 + B^2 + C^2}}",
     "VTPT vuông góc với 2 vectơ chỉ phương: n = [u, v].",
     "Khoảng cách từ O(0; 0; 0) đến 2x - 2y + z - 9 = 0 bằng:", "3", "NUMERIC", [],
     "Mặt phẳng 2x - 3y + z - 5 = 0 có một vectơ pháp tuyến là gì?", "Tọa độ vectơ pháp tuyến là hệ số trước x, y, z: n = (2; -3; 1)."),

    ("Bài 15: Phương trình đường thẳng trong không gian", "Chương V: Phương pháp tọa độ trong không gian",
     "Đường thẳng qua M(x0; y0; z0) có VTCP u(a; b; c): dạng tham số và chính tắc.",
     r"\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}; \quad \frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}",
     "Để chuyển sang chính tắc rút tham số t cho bằng nhau.",
     "Đường thẳng (x - 1)/2 = (y + 2)/-1 = (z - 3)/1 đi qua M(1; -2; z0). z0 bằng:", "3", "NUMERIC", [],
     "Tìm một vectơ chỉ phương của đường thẳng (x - 1)/3 = (y + 2)/-2 = z/5.", "Vectơ chỉ phương lấy từ các mẫu số: u = (3; -2; 5)."),

    ("Bài 16: Công thức tính góc trong không gian", "Chương V: Phương pháp tọa độ trong không gian",
     "Cosin góc 2 mặt phẳng qua 2 VTPT. Sin góc đường thẳng và mặt phẳng.",
     r"\cos((P), (Q)) = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}; \quad \sin(d, (P)) = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}||\vec{n}|}",
     "Góc đường và mặt dùng sin, góc 2 mặt phẳng dùng cosin.",
     "Hai mặt phẳng có n1=(1;0;0) và n2=(0;1;0) tạo góc bằng (độ):", "90", "NUMERIC", [],
     "Hai mặt phẳng vuông góc với nhau khi tích vô hướng của hai vectơ pháp tuyến bằng bao nhiêu?", "Bằng 0: n1 . n2 = 0."),

    ("Bài 17: Phương trình mặt cầu", "Chương V: Phương pháp tọa độ trong không gian",
     "Mặt cầu tâm I(a; b; c) bán kính R: (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2.",
     r"(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2; \quad R = \sqrt{a^2 + b^2 + c^2 - d}",
     "Mặt phẳng tiếp xúc mặt cầu khi khoảng cách từ tâm đến mặt bằng R.",
     "Bán kính của (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 25 bằng:", "5", "NUMERIC", [],
     "Tìm tâm và bán kính của mặt cầu (x - 1)^2 + y^2 + (z + 2)^2 = 9.", "Tâm I(1; 0; -2) và bán kính R = căn(9) = 3."),

    ("Bài 18: Xác suất có điều kiện", "Chương VI: Xác suất có điều kiện",
     "Xác suất của A khi biết B đã xảy ra: P(A|B) = P(AB) / P(B).",
     r"P(A|B) = \frac{P(AB)}{P(B)}; \quad P(AB) = P(B) \cdot P(A|B)",
     "A và B độc lập khi và chỉ khi P(A|B) = P(A).",
     "P(AB) = 0.2 và P(B) = 0.5. Xác suất P(A|B) bằng:", "0.4", "NUMERIC", [],
     "Cho P(A) = 0.4, P(B) = 0.5, P(AB) = 0.2. A và B có độc lập không?", "Ta có P(A)*P(B) = 0.4 * 0.5 = 0.2 = P(AB) nên A và B độc lập."),

    ("Bài 19: Công thức xác suất toàn phần và công thức Bayes", "Chương VI: Xác suất có điều kiện",
     "Xác suất toàn phần qua hệ đầy đủ. Công thức Bayes tính xác suất hậu nghiệm.",
     r"P(A) = \sum_{i=1}^n P(B_i)P(A|B_i); \quad P(B_k|A) = \frac{P(B_k)P(A|B_k)}{P(A)}",
     "Công thức Bayes dùng cập nhật xác suất khi đã biết biến cố A xảy ra.",
     "Hệ đầy đủ B1, B2: P(B1)=0.4, P(B2)=0.6; P(A|B1)=0.5, P(A|B2)=0.2. P(A) bằng:", "0.32", "NUMERIC", [],
     "Nêu ý nghĩa của công thức xác suất toàn phần.", "Cho phép tính xác suất của biến cố A thông qua các trường hợp phân hoạch rời nhau của không gian mẫu.")
]

def build_data_map(raw_list):
    res = {}
    for item in raw_list:
        title, chap, concept, formula, trap, content, target, ans_type, opts, ex_prob, ex_sol = item
        
        # Tạo 2 chủ điểm cho mỗi bài học
        res[title] = {
            "chapter": chap,
            "topics": {
                "Chủ điểm 1: Lý thuyết trọng tâm & Phương pháp giải toán": {
                    "theory": concept,
                    "formula": formula,
                    "trap": trap,
                    "audio": f"Chào em! Trong chủ điểm lý thuyết này, em hãy ghi nhớ: {concept}. {trap}",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Bài toán cơ bản áp dụng định lý",
                            "problem": ex_prob,
                            "solution": ex_sol
                        }
                    ],
                    "exercise": {
                        "id": f"EX1_{hashlib.md5(title.encode()).hexdigest()[:6]}",
                        "title": f"Bài tập tự luyện: {title}",
                        "content": content,
                        "type": ans_type,
                        "target": target,
                        "options": opts
                    }
                },
                "Chủ điểm 2: Phân tích dạng bài & Rèn luyện kỹ năng": {
                    "theory": f"Rèn luyện kỹ năng tư duy và nhận diện dạng toán cho {title}. Bám sát đề cương SGK và Vở tự học.",
                    "formula": formula,
                    "trap": f"Lưu ý đối chiếu điều kiện bài toán: {trap}",
                    "audio": f"Trong chủ điểm kỹ năng, các em cần chú ý cách trình bày từng bước chặt chẽ, tránh lỗi suy luận.",
                    "examples": [
                        {
                            "title": "Ví dụ 2: Bài toán củng cố phương pháp giải chuẩn mực",
                            "problem": f"Vận dụng kiến thức bài học để giải quyết bài toán: {content}",
                            "solution": f"Áp dụng công thức lý thuyết: $${formula}$$. Thay số và biến đổi từng bước để thu được đáp số chính xác: $${target}$$."
                        }
                    ],
                    "exercise": {
                        "id": f"EX2_{hashlib.md5(title.encode()).hexdigest()[:6]}",
                        "title": f"Bài tập kiểm minh chứng: {title}",
                        "content": content,
                        "type": ans_type,
                        "target": target,
                        "options": opts
                    }
                }
            }
        }
    return res

CURRICULUM_DATA = {
    "Khối 10": build_data_map(RAW_LESSONS_10),
    "Khối 11": build_data_map(RAW_LESSONS_11),
    "Khối 12": build_data_map(RAW_LESSONS_12)
}

# ==============================================================================
# 4. KHO ĐỀ KHẢO THÍ CHUẨN ĐỊNH DẠNG MỚI CỦA BỘ GD&ĐT
# ==============================================================================
EXAM_BANK = {
    "Khối 10": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 10",
            "p1": [{"q": r"Mệnh đề nào sau đây là mệnh đề toán học?", "ops": ["A. $2 + 3 = 6$", "B. Thời tiết hôm nay mát quá!", "C. Bạn học bài chưa?", "D. Hãy giải phương trình."], "ans": "A", "exp": "A là câu khẳng định sai, là mệnh đề toán học."}],
            "p2": [{"q": r"Cho tam thức $f(x) = x^2 - 4x + 3$. Xét tính Đúng/Sai:", "items": [("a) Phương trình có 2 nghiệm phân biệt x=1 và x=3.", True, "Delta'>0."), ("b) f(x) < 0 với x thuộc (1; 3).", True, "Trong trái ngoài cùng."), ("c) Đỉnh parabol là I(2; 1).", False, "Đỉnh đúng là I(2; -1)."), ("d) f(0) = 3.", True, "Thay x=0.")]}],
            "p3": [{"q": r"Cho tam giác ABC có b=8, c=5, góc A=60 độ. Cạnh a bằng bao nhiêu?", "ans": "7", "alt": ["7.0"], "exp": "a^2 = 64 + 25 - 40 = 49 => a = 7."}]
        },
        "Cuối học kỳ 1": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 1 - TOÁN 10",
            "p1": [{"q": r"Cho u=(1;2), v=(-2;3). Tích vô hướng u.v bằng:", "ops": ["A. 4", "B. -8", "C. 8", "D. 0"], "ans": "A", "exp": "1*(-2) + 2*3 = 4."}],
            "p2": [{"q": r"Cho hình vuông ABCD cạnh a. Xét tính Đúng/Sai:", "items": [("a) Độ dài vectơ AB bằng a.", True, "Cạnh hình vuông."), ("b) AB vuông góc AD.", True, "Góc vuông."), ("c) Vectơ AC cùng hướng BD.", False, "Cắt nhau."), ("d) Độ dài vectơ AC bằng a căn 2.", True, "Đường chéo.")]}],
            "p3": [{"q": r"Khoảng cách từ điểm M(1; 2) đến đường thẳng 3x - 4y + 15 = 0 bằng:", "ans": "2", "alt": ["2.0"], "exp": "d = |3 - 8 + 15| / 5 = 2."}]
        }
    },
    "Khối 11": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 11",
            "p1": [{"q": r"Tập xác định của hàm số $y = \tan x$ là:", "ops": [r"A. $D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi\}$", r"B. $D = \mathbb{R} \setminus \{k\pi\}$", r"C. $D = \mathbb{R}$", r"D. $D = [-1; 1]$"], "ans": "A", "exp": "cos x khác 0."}],
            "p2": [{"q": r"Cho cấp số cộng (un) có u1 = 2, d = 3. Xét tính Đúng/Sai:", "items": [("a) u2 = 5.", True, "2+3=5."), ("b) Số hạng tổng quát un = 3n - 1.", True, "2 + 3(n-1)."), ("c) Số 20 là một số hạng của dãy.", True, "3n-1=20 => n=7."), ("d) Tổng 10 số hạng đầu S10 = 155.", True, "10*(4+27)/2 = 155.")]}],
            "p3": [{"q": r"Rạp hát có 12 hàng ghế. Hàng 1 có 15 ghế, mỗi hàng sau hơn 2 ghế. Tổng số ghế:", "ans": "312", "alt": ["312 ghế"], "exp": "S_12 = 12*(30 + 22)/2 = 312."}]
        },
        "Cuối học kỳ 1": {
            "title": "ĐỀ KIỂM TRA CUỐI HỌC KỲ 1 - TOÁN 11",
            "p1": [{"q": r"Giới hạn lim (4n + 3)/(2n - 1) khi n ra vô cùng bằng:", "ops": ["A. 2", "B. -3", "C. 4", "D. 0"], "ans": "A", "exp": "4/2 = 2."}],
            "p2": [{"q": r"Cho hình chóp S.ABCD đáy hình bình hành tâm O. Xét tính Đúng/Sai:", "items": [("a) Giao tuyến (SAC) và (SBD) là SO.", True, "Chung S và O."), ("b) AB song song (SCD).", True, "AB song song CD."), ("c) SO cắt AD.", False, "Chéo nhau."), ("d) Thiết diện qua O song song (SAB) là hình thang.", True, "Song song.")]}],
            "p3": [{"q": r"Tính giới hạn: lim (x^2 - 1)/(x - 1) khi x tiến tới 1.", "ans": "2", "alt": ["2.0"], "exp": "x + 1 = 2."}]
        }
    },
    "Khối 12": {
        "🏛️ Ôn thi Tốt nghiệp THPT (Cấu trúc mới)": {
            "title": "ĐỀ THI TỐT NGHIỆP THPT CHUẨN MA TRẬN KHẢO THÍ MỚI",
            "p1": [{"q": r"Cho hàm số có đạo hàm $f'(x) = x(x-1)^2 (x+2)^3$. Số điểm cực trị là:", "ops": ["A. 2", "B. 3", "C. 1", "D. 0"], "ans": "A", "exp": "Nghiệm bội lẻ x = 0 và x = -2."}],
            "p2": [{"q": r"Cho hình chóp đều S.ABC có đáy cạnh a, cạnh bên tạo đáy góc 60 độ. Xét tính Đúng/Sai:", "items": [("a) Hình chiếu của S là trọng tâm đáy.", True, "Chóp đều."), ("b) Độ dài đường cao bằng a.", True, "h = (a căn 3 / 3)*tan 60 = a."), ("c) Thể tích bằng a^3 / 4.", False, "a^3 căn 3 / 12."), ("d) Bán kính mặt cầu ngoại tiếp bằng 2a/3.", True, "R = 2a/3.")]}],
            "p3": [{"q": r"Làm hộp không nắp đáy vuông thể tích 32 dm3. Diện tích vật liệu nhỏ nhất (dm2):", "ans": "48", "alt": ["48 dm2"], "exp": "S(x) = x^2 + 128/x. Min tại x=4, S=48."}]
        },
        "🚀 Ôn thi Đánh giá năng lực (ĐGNL)": {
            "title": "BỘ ĐỀ ĐÁNH GIÁ NĂNG LỰC TOÁN HỌC & MÔ HÌNH HÓA THỰC TẾ",
            "p1": [{"q": r"Tốc độ vi khuẩn $N'(t) = -200/(t+1)^2$. Ban đầu $N(0)=500$. Sau mấy giờ còn 350 khuẩn?", "ops": ["A. 3 giờ", "B. 4 giờ", "C. 2 giờ", "D. 5 giờ"], "ans": "A", "exp": "200/(t+1) + 300 = 350 => t = 3."}],
            "p2": [{"q": r"Chi phí sản xuất $C(x) = 50 + 200/x$ (nghìn đồng) với $x \ge 10$. Xét tính Đúng/Sai:", "items": [("a) Sản xuất càng nhiều chi phí trung bình càng giảm.", True, "Hàm nghịch biến."), ("b) x = 100 thì chi phí là 52 nghìn.", True, "50 + 2 = 52."), ("c) Chi phí có thể hạ dưới 50 nghìn.", False, "Luôn lớn hơn 50."), ("d) Đạo hàm C'(x) luôn âm.", True, "-200/x^2 < 0.")]}],
            "p3": [{"q": r"Trạm radar tại O phát hiện trong bán kính 10 km. Máy bay tại B(7; 6; 5). Khoảng cách OB (km, làm tròn 2 số):", "ans": "10.49", "alt": ["10.5"], "exp": "căn(49 + 36 + 25) = căn(110) ≈ 10.49."}]
        }
    }
}

# ==============================================================================
# 5. DỮ LIỆU TÀI KHOẢN & GAMIFICATION
# ==============================================================================
DEFAULT_STUDENTS = [
    {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "current_level": "Khá", "weak_spots": "Dấu lượng giác, Hình không gian", "flowers": 30, "total_solved": 5},
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
            text=['B(7;6;5) Vật thể'],
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
            st.caption("Giải đúng bài tập nhận +2 hoa. Xem video +1 hoa. Khảo thí nhận tới +3 hoa!")
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
# 9. PHÂN HỆ HỌC SINH (5 TABS TOÀN DIỆN VỚI TAB VÍ DỤ MINH HỌA)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN 3 BẬC: KHỐI -> BÀI HỌC (27/33/19) -> CHỦ ĐIỂM KIẾN THỨC
c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])
with c_gr:
    user_grade_default = 0 if student_info.get("grade") == 10 else (2 if student_info.get("grade") == 12 else 1)
    sel_grade = st.selectbox("📚 Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

with c_les:
    lesson_list = list(CURRICULUM_DATA[sel_grade].keys())
    sel_lesson = st.selectbox(
        f"📖 Bài học ({len(lesson_list)} bài):",
        lesson_list,
        help="Danh mục bài học bám sát toàn bộ chương trình Kết nối tri thức."
    )

cur_lesson_obj = CURRICULUM_DATA[sel_grade][sel_lesson]

with c_top:
    topic_list = list(cur_lesson_obj["topics"].keys())
    sel_topic = st.selectbox("🎯 Danh sách Chủ điểm:", topic_list)

cur_topic_data = cur_lesson_obj["topics"][sel_topic]

# KHỞI TẠO 5 TABS: TAB VÍ DỤ MINH HỌA ĐẶT NGAY SAU CỐT LÕI KIẾN THỨC
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
            st.caption("Dùng chuột hoặc ngón tay chạm/vuốt để xoay 360 độ, quan sát thiết diện và hình chiếu:")
            tp_3d = "OXYZ" if "Oxyz" in sel_lesson or "Vectơ" in sel_lesson else "SHAPE_3D"
            render_3d_geometry_view(tp_3d)

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
# TAB 2: VÍ DỤ MINH HỌA (TRÌNH BÀY DẠNG ĐỀ BÀI -> BẤM XEM LỜI GIẢI CHI TIẾT)
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Ví Dụ Minh Họa Chuẩn Mực: {sel_topic}")
    st.caption("Các ví dụ trọng tâm bám sát Vở tự học (đã loại bỏ bài chứa tham số m và bài vận dụng cao). Bấm vào từng đề bài để xem lời giải chi tiết và học cách trình bày.")

    examples_list = cur_topic_data.get("examples", [])
    if not examples_list:
        st.info("Chủ điểm này đang được cập nhật thêm các ví dụ tiếp theo.")
    else:
        for idx, ex_item in enumerate(examples_list):
            with st.expander(f"📌 Đề bài {idx + 1}: {ex_item['title']}", expanded=(idx == 0)):
                st.markdown(f"**Đề bài yêu cầu:**\n\n> {ex_item['problem']}")
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
            user_submitted_ans = st.text_input("Nhập kết quả/đáp số của em (ví dụ: -0.8 hoặc 7):", key=f"num_ex_{ex['id']}")

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
