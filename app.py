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
# 1. CẤU HÌNH GIAO DIỆN & CSS THANH CUỘN CHO DANH SÁCH BÀI HỌC
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Thanh cuộn chuyên biệt cho Dropdown Selectbox */
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
# 2. KHỞI TẠO KẾT NỐI GEMINI API & GOOGLE SHEETS DỰ PHÒNG
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
# 3. KHO HỌC LIỆU SỐ CHÍNH THỨC: ĐỦ 27 BÀI (K10), 33 BÀI (K11), 19 BÀI (K12)
# ==============================================================================
LESSONS_10 = [
    ("Bài 1: Mệnh đề toán học", "Chương I: Mệnh đề và tập hợp", "Phủ định của với mọi là tồn tại, dấu lớn đổi thành nhỏ hơn hoặc bằng. Nhớ đừng quên dấu bằng.", r"\forall x \in X, P(x) \leftrightarrow \exists x \in X, \overline{P(x)}", "NUMERIC", "x^2 - 2x + 5 > 0", "A", "CHOICE", ["A. Sai", "B. Đúng"], "A"),
    ("Bài 2: Tập hợp và các phép toán trên tập hợp", "Chương I: Mệnh đề và tập hợp", "Giao là phần chung, hợp là lấy tất cả, hiệu là thuộc A nhưng không thuộc B.", r"A \cap B, A \cup B, A \setminus B", "NUMERIC", "Cho A={1,2,3}, B={2,3,4}. Số phần tử của A giao B là:", "2", "NUMERIC", [], "2"),
    ("Bài 3: Bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn", "Vẽ đường thẳng biên, lấy gốc O(0;0) thử để xác định nửa mặt phẳng nghiệm.", r"ax + by \le c", "NUMERIC", "Điểm O(0;0) có thuộc miền nghiệm của x + y <= 4 không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),
    ("Bài 4: Hệ bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn", "Miền nghiệm là phần giao của các nửa mặt phẳng. Điểm tối ưu luôn đạt tại các đỉnh đa giác.", r"F(x;y) = ax + by", "NUMERIC", "F(x;y)=3x+2y với x+y<=4, x>=0, y>=0. F max bằng:", "12", "NUMERIC", [], "12"),
    ("Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ", "Chương III: Hệ thức lượng trong tam giác", "Góc tù thì cos âm, sin luôn dương trong khoảng 0 đến 180 độ.", r"\sin^2\alpha + \cos^2\alpha = 1", "NUMERIC", "Tính sin(30 độ) (dạng thập phân):", "0.5", "NUMERIC", [], "0.5"),
    ("Bài 6: Hệ thức lượng trong tam giác", "Chương III: Hệ thức lượng trong tam giác", "Biết 2 cạnh và góc xen giữa dùng định lý Côsin. Biết 1 cạnh 2 góc kề dùng định lý Sin.", r"a^2 = b^2 + c^2 - 2bc \cos A", "NUMERIC", "Tam giác có b=8, c=5, góc A=60 độ. Cạnh a bằng:", "7", "NUMERIC", [], "7"),
    ("Bài 7: Các khái niệm mở đầu về vectơ", "Chương IV: Vectơ", "Vectơ là đoạn thẳng có hướng. Hai vectơ cùng phương khi giá của chúng song song hoặc trùng nhau.", r"\vec{u} = \vec{v} \Leftrightarrow |\vec{u}|=|\vec{v}| \text{ và cùng hướng}", "NUMERIC", "Vectơ cùng hướng thì có cùng phương không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),
    ("Bài 8: Tổng và hiệu của hai vectơ", "Chương IV: Vectơ", "Quy tắc 3 điểm: AB cộng BC bằng AC. Quy tắc hình bình hành áp dụng cho hai vectơ chung gốc.", r"\vec{AB} + \vec{BC} = \vec{AC}", "NUMERIC", "Cho tam giác đều ABC cạnh 2. Độ dài vectơ AB + BC bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 9: Tích của một vectơ với một số", "Chương IV: Vectơ", "Tích k nhân vectơ a cùng hướng khi k dương, ngược hướng khi k âm. Độ dài gấp trị tuyệt đối của k lần.", r"k\vec{a}", "NUMERIC", "I là trung điểm AB thì vectơ IA + IB bằng vectơ không. Độ dài bằng:", "0", "NUMERIC", [], "0"),
    ("Bài 10: Vectơ trong mặt phẳng tọa độ", "Chương IV: Vectơ", "Tọa độ vectơ bằng tọa độ điểm cuối trừ điểm đầu. Cộng trừ vectơ theo từng tọa độ tương ứng.", r"\vec{u}=(x; y) = x\vec{i} + y\vec{j}", "NUMERIC", "Cho A(1;2), B(3;5). Tọa độ vectơ AB là (x; y). Tính x+y:", "5", "NUMERIC", [], "5"),
    ("Bài 11: Tích vô hướng của hai vectơ", "Chương IV: Vectơ", "Tích vô hướng bằng tích độ dài nhân cos góc xen giữa. Hai vectơ vuông góc khi tích vô hướng bằng 0.", r"\vec{u}\cdot\vec{v} = |\vec{u}||\vec{v}|\cos(\vec{u},\vec{v})", "NUMERIC", "Cho u=(1;2), v=(-2;1). Tích vô hướng u.v bằng:", "0", "NUMERIC", [], "0"),
    ("Bài 12: Số gần đúng và sai số", "Chương V: Số đặc trưng đo xu thế trung tâm", "Sai số tuyệt đối đo khoảng cách giữa giá trị gần đúng và số đúng. Độ chính xác d.", r"\Delta_a = |a - \overline{a}| \le d", "NUMERIC", "Quy tròn số 3.14159 đến hàng phần trăm được:", "3.14", "NUMERIC", [], "3.14"),
    ("Bài 13: Các số đặc trưng đo xu thế trung tâm", "Chương V: Số đặc trưng đo xu thế trung tâm", "Số trung bình, trung vị chia đôi mẫu số liệu, mốt là giá trị xuất hiện nhiều nhất.", r"\overline{x} = \frac{\sum x_i}{n}", "NUMERIC", "Trung vị của mẫu 2, 4, 6, 8, 10 là:", "6", "NUMERIC", [], "6"),
    ("Bài 14: Các số đặc trưng đo độ phân tán", "Chương V: Số đặc trưng đo xu thế trung tâm", "Khoảng biến thiên R bằng giá trị lớn nhất trừ nhỏ nhất. Phương sai đo độ lệch bình phương.", r"R = x_{\max} - x_{\min}, s^2", "NUMERIC", "Khoảng biến thiên của mẫu 3, 5, 9, 12 là:", "9", "NUMERIC", [], "9"),
    ("Bài 15: Hàm số và đồ thị", "Chương VI: Hàm số, đồ thị và ứng dụng", "Hàm số đồng biến khi x tăng y tăng. Điểm thuộc đồ thị thỏa mãn phương trình hàm số.", r"y = f(x)", "NUMERIC", "Cho y = 2x - 1. Điểm M(1; y0) thuộc đồ thị thì y0 bằng:", "1", "NUMERIC", [], "1"),
    ("Bài 16: Hàm số bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng", "Đồ thị là parabol có đỉnh I(-b/2a; -Delta/4a). Bề lõm quay lên khi a dương, quay xuống khi a âm.", r"y = ax^2 + bx + c", "NUMERIC", "Hoành độ đỉnh của parabol y = x^2 - 4x + 3 là:", "2", "NUMERIC", [], "2"),
    ("Bài 17: Dấu của tam thức bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng", "Trong trái ngoài cùng. Tam thức luôn cùng dấu với hệ số a khi biệt thức Delta âm.", r"f(x) = ax^2 + bx + c", "NUMERIC", "Nghiệm của bpt x^2 - 4x + 3 < 0 là khoảng (1; x2). x2 bằng:", "3", "NUMERIC", [], "3"),
    ("Bài 18: Phương trình quy về phương trình bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng", "Phương trình chứa căn bậc hai luôn phải đặt điều kiện hoặc bình phương rồi thử lại nghiệm.", r"\sqrt{f(x)} = \sqrt{g(x)}", "NUMERIC", "Số nghiệm của phương trình căn(x-1) = 2 là:", "1", "NUMERIC", [], "1"),
    ("Bài 19: Phương trình đường thẳng", "Chương VII: Phương pháp tọa độ trong mặt phẳng", "Đường thẳng qua 1 điểm và có vectơ pháp tuyến (A;B) có phương trình A(x-x0) + B(y-y0) = 0.", r"Ax + By + C = 0", "NUMERIC", "Đường thẳng 2x - 3y + 1 = 0 có một VTPT n = (2; y0). y0 bằng:", "-3", "NUMERIC", [], "-3"),
    ("Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách", "Chương VII: Phương pháp tọa độ trong mặt phẳng", "Hai đường thẳng vuông góc khi tích vô hướng hai VTPT bằng 0. Công thức tính khoảng cách điểm đến đường thẳng.", r"d(M, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}", "NUMERIC", "Khoảng cách từ O(0;0) đến 3x - 4y + 10 = 0 bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 21: Đường tròn trong mặt phẳng tọa độ", "Chương VII: Phương pháp tọa độ trong mặt phẳng", "Phương trình chính tắc tâm I(a;b) bán kính R là (x-a)^2 + (y-b)^2 = R^2.", r"(x-a)^2 + (y-b)^2 = R^2", "NUMERIC", "Bán kính của đường tròn (x-1)^2 + (y+2)^2 = 16 bằng:", "4", "NUMERIC", [], "4"),
    ("Bài 22: Ba đường conic", "Chương VII: Phương pháp tọa độ trong mặt phẳng", "Elip x bình chia a bình cộng y bình chia b bình bằng 1. Hypebol có dấu trừ ở giữa. Parabol y bình bằng 2px.", r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1", "NUMERIC", "Elip x^2/25 + y^2/9 = 1 có độ dài trục lớn 2a bằng:", "10", "NUMERIC", [], "10"),
    ("Bài 23: Quy tắc đếm", "Chương VIII: Đại số tổ hợp", "Quy tắc cộng áp dụng cho các phương án độc lập. Quy tắc nhân áp dụng cho các công đoạn liên tiếp.", r"N = n_1 + n_2 \text{ hoặc } n_1 \times n_2", "NUMERIC", "Có 3 áo và 4 quần. Số cách chọn 1 bộ quần áo là:", "12", "NUMERIC", [], "12"),
    ("Bài 24: Hoán vị, chỉnh hợp và tổ hợp", "Chương VIII: Đại số tổ hợp", "Chỉnh hợp có thứ tự vị trí, tổ hợp không quan tâm thứ tự sắp xếp.", r"A_n^k = \frac{n!}{(n-k)!}, C_n^k = \frac{n!}{k!(n-k)!}", "NUMERIC", "Giá trị của C(5, 2) bằng:", "10", "NUMERIC", [], "10"),
    ("Bài 25: Nhị thức Newton", "Chương VIII: Đại số tổ hợp", "Khai triển (a+b)^4 và (a+b)^5 áp dụng công thức tổ hợp. Hệ số đối xứng.", r"(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4", "NUMERIC", "Hệ số của x^3 trong (x+1)^4 là:", "4", "NUMERIC", [], "4"),
    ("Bài 26: Biến cố và định nghĩa cổ điển của xác suất", "Chương IX: Tính xác suất theo định nghĩa cổ điển", "Xác suất biến cố A bằng số kết quả thuận lợi n(A) chia số phần tử không gian mẫu n(Omega).", r"P(A) = \frac{n(A)}{n(\Omega)}", "NUMERIC", "Gieo đồng xu cân đối 1 lần. Xác suất xuất hiện mặt ngửa:", "0.5", "NUMERIC", [], "0.5"),
    ("Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển", "Chương IX: Tính xác suất theo định nghĩa cổ điển", "Sử dụng quy tắc đếm và tổ hợp để đếm không gian mẫu và biến cố.", r"P(A) = \frac{C_m^k}{C_n^k}", "NUMERIC", "Hộp có 3 đỏ 2 xanh. Lấy ngẫu nhiên 1 bi. Xác suất bi đỏ:", "0.6", "NUMERIC", [], "0.6")
]

LESSONS_11 = [
    ("Bài 1: Giá trị lượng giác của góc lượng giác", "Chương I: Hàm số và phương trình lượng giác", "Trục sin đứng, trục cos nằm. Góc phần tư thứ hai thì sin dương, cos âm.", r"\sin^2\alpha + \cos^2\alpha = 1", "NUMERIC", "Biết sin(a)=3/5 với pi/2 < a < pi. Giá trị cos(a) là:", "-0.8", "NUMERIC", [], "-0.8"),
    ("Bài 2: Công thức lượng giác", "Chương I: Hàm số và phương trình lượng giác", "Cos thì cos cos sin sin, sin thì sin cos cos sin. Công thức nhân đôi: sin 2a = 2 sin a cos a.", r"\sin(a+b) = \sin a\cos b + \cos a\sin b", "NUMERIC", "Nếu sin(a)*cos(a) = 0.25 thì sin(2a) bằng:", "0.5", "NUMERIC", [], "0.5"),
    ("Bài 3: Hàm số lượng giác", "Chương I: Hàm số và phương trình lượng giác", "Hàm sin và cos có chu kỳ 2pi, tập giá trị [-1; 1]. Hàm tan và cot có chu kỳ pi.", r"y = \sin x, y = \cos x", "NUMERIC", "Giá trị lớn nhất của hàm số y = 3sin(x) + 2 là:", "5", "NUMERIC", [], "5"),
    ("Bài 4: Phương trình lượng giác cơ bản", "Chương I: Hàm số và phương trình lượng giác", "sin x = sin alpha có 2 họ nghiệm: alpha và pi trừ alpha cộng k2pi.", r"\sin x = m \quad (|m| \le 1)", "NUMERIC", "Số nghiệm của sin(x) = 1 trên đoạn [0; 2pi] là:", "1", "NUMERIC", [], "1"),
    ("Bài 5: Dãy số", "Chương II: Dãy số. Cấp số cộng và cấp số nhân", "Dãy số là hàm số xác định trên tập số nguyên dương. Dãy tăng khi u(n+1) lớn hơn un.", r"(u_n): u_n = f(n)", "NUMERIC", "Cho un = 2n + 1. Số hạng thứ 3 (u3) bằng:", "7", "NUMERIC", [], "7"),
    ("Bài 6: Cấp số cộng", "Chương II: Dãy số. Cấp số cộng và cấp số nhân", "Số hạng tổng quát un bằng u1 cộng n trừ 1 nhân d. Tổng n số hạng là n(u1+un)/2.", r"u_n = u_1 + (n-1)d", "NUMERIC", "Cho CSC có u1 = 3, d = 4. Số hạng thứ 5 bằng:", "19", "NUMERIC", [], "19"),
    ("Bài 7: Cấp số nhân", "Chương II: Dãy số. Cấp số cộng và cấp số nhân", "Số hạng tổng quát un bằng u1 nhân q mũ n trừ 1.", r"u_n = u_1 \cdot q^{n-1}", "NUMERIC", "Cho CSN có u1 = 2, q = 3. Số hạng thứ 3 bằng:", "18", "NUMERIC", [], "18"),
    ("Bài 8: Mẫu số liệu ghép nhóm", "Chương III: Các số đặc trưng đo xu thế trung tâm", "Ghép nhóm các số liệu thành từng nửa khoảng. Giá trị đại diện là trung điểm của nhóm.", r"c_i = \frac{a_i + a_{i+1}}{2}", "NUMERIC", "Giá trị đại diện của nhóm [10; 20) là:", "15", "NUMERIC", [], "15"),
    ("Bài 9: Các số đặc trưng đo xu thế trung tâm", "Chương III: Các số đặc trưng đo xu thế trung tâm", "Xác định nhóm chứa trung vị và mốt theo công thức tần số tích lũy.", r"M_e = a_p + \frac{\frac{n}{2} - C}{n_p} h", "NUMERIC", "Nhóm [20; 30) có tần số 10 trong tổng n=40. Tần số tích lũy trước đó là 10. Trung vị Me bằng:", "30", "NUMERIC", [], "30"),
    ("Bài 10: Đường thẳng và mặt phẳng trong không gian", "Chương IV: Quan hệ song song trong không gian", "Qua 3 điểm không thẳng hàng xác định duy nhất 1 mặt phẳng.", r"(ABC)", "NUMERIC", "Có bao nhiêu mặt phẳng đi qua 3 điểm thẳng hàng? (0: Không có, -1: Vô số)", "-1", "NUMERIC", [], "-1"),
    ("Bài 11: Hai đường thẳng song song", "Chương IV: Quan hệ song song trong không gian", "Hai đường thẳng song song là hai đường thẳng cùng nằm trong 1 mặt phẳng và không có điểm chung.", r"a \parallel b", "NUMERIC", "Hai đường thẳng chéo nhau có điểm chung không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),
    ("Bài 12: Đường thẳng và mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian", "Đường thẳng d song song với (P) nếu d song song với 1 đường thẳng a nằm trong (P).", r"d \parallel a \subset (P) \Rightarrow d \parallel (P)", "NUMERIC", "Nếu d nằm trong (P) thì d có song song (P) không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),
    ("Bài 13: Hai mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian", "Mặt phẳng (P) chứa 2 đường thẳng cắt nhau cùng song song với (Q) thì (P) song song (Q).", r"(P) \parallel (Q)", "NUMERIC", "Hai mặt phẳng phân biệt cùng song song với mặt phẳng thứ 3 thì song song nhau? (1: Đúng, 0: Sai)", "1", "NUMERIC", [], "1"),
    ("Bài 14: Phép chiếu song song", "Chương IV: Quan hệ song song trong không gian", "Phép chiếu song song bảo toàn tính song song và tỉ số đoạn thẳng cùng phương.", r"\text{Chiếu song song}", "NUMERIC", "Hình chiếu song song của hình bình hành là hình gì? (1: Hình bình hành/đoạn thẳng, 0: Hình tròn)", "1", "NUMERIC", [], "1"),
    ("Bài 15: Giới hạn của dãy số", "Chương V: Giới hạn. Hàm số liên tục", "Giới hạn 1/n bằng 0 khi n tiến ra vô cùng. Chia cả tử và mẫu cho lũy thừa bậc cao nhất của n.", r"\lim_{n \to \infty} \frac{1}{n^k} = 0", "NUMERIC", "Giới hạn lim (2n+1)/(n-3) khi n ra vô cùng bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 16: Giới hạn của hàm số", "Chương V: Giới hạn. Hàm số liên tục", "Dạng vô định 0/0 khử bằng cách phân tích đa thức thành nhân tử hoặc nhân liên hợp.", r"\lim_{x \to x_0} f(x)", "NUMERIC", "Giới hạn lim (x^2 - 1)/(x - 1) khi x tiến tới 1 bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 17: Hàm số liên tục", "Chương V: Giới hạn. Hàm số liên tục", "Hàm số liên tục tại x0 khi giới hạn tại x0 bằng đúng giá trị hàm số f(x0).", r"\lim_{x \to x_0} f(x) = f(x_0)", "NUMERIC", "Hàm đa thức có liên tục trên toàn R không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),
    ("Bài 18: Lũy thừa với số mũ thực", "Chương VI: Hàm số mũ và hàm số lôgarit", "Lũy thừa với số mũ hữu tỉ và thực. Tính chất nhân chia cùng cơ số.", r"a^\alpha \cdot a^\beta = a^{\alpha+\beta}", "NUMERIC", "Giá trị 2^3 * 2^2 bằng:", "32", "NUMERIC", [], "32"),
    ("Bài 19: Lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit", "Lôgarit cơ số a của b là số alpha sao cho a mũ alpha bằng b. Đổi cơ số.", r"\log_a b = \alpha \Leftrightarrow a^\alpha = b", "NUMERIC", "Giá trị của log_2(8) bằng:", "3", "NUMERIC", [], "3"),
    ("Bài 20: Hàm số mũ và hàm số lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit", "Cơ số a lớn hơn 1 hàm đồng biến, cơ số a trong khoảng (0; 1) hàm nghịch biến.", r"y = a^x, y = \log_a x", "NUMERIC", "Hàm số y = (0.5)^x đồng biến hay nghịch biến? (1: Nghịch biến, 0: Đồng biến)", "1", "NUMERIC", [], "1"),
    ("Bài 21: Phương trình, bất phương trình mũ và lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit", "Đưa về cùng cơ số hoặc đặt ẩn phụ. Nhớ đặt điều kiện cho biểu thức dưới dấu lôgarit.", r"a^x = b \Leftrightarrow x = \log_a b", "NUMERIC", "Nghiệm của phương trình 2^x = 16 là:", "4", "NUMERIC", [], "4"),
    ("Bài 22: Hai đường thẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian", "Góc giữa 2 đường thẳng không vượt quá 90 độ. Hai đường vuông góc khi góc bằng 90 độ.", r"a \perp b \Leftrightarrow (\widehat{a, b}) = 90^\circ", "NUMERIC", "Góc giữa 2 đường thẳng có thể bằng 120 độ không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),
    ("Bài 23: Đường thẳng vuông góc với mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian", "Đường thẳng d vuông góc với (P) khi vuông góc với 2 đường thẳng cắt nhau trong (P).", r"d \perp a, d \perp b \Rightarrow d \perp (P)", "NUMERIC", "SA vuông góc đáy (ABC), AB vuông góc BC. Tam giác SBC vuông tại đâu? (Điền chữ B hoặc C):", "B", "NUMERIC", [], "B"),
    ("Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian", "Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng và hình chiếu của nó.", r"\varphi = \widehat{(d, d')}", "NUMERIC", "SA vuông góc (ABC) và SA=AB=a. Góc giữa SB và (ABC) bằng:", "45", "NUMERIC", [], "45"),
    ("Bài 25: Hai mặt phẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian", "Mặt phẳng (P) chứa đường thẳng vuông góc với (Q) thì (P) vuông góc (Q).", r"(P) \perp (Q)", "NUMERIC", "Hình chóp có SA vuông góc đáy thì (SAB) có vuông góc đáy không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),
    ("Bài 26: Khoảng cách trong không gian", "Chương VII: Quan hệ vuông góc trong không gian", "Khoảng cách từ điểm đến mặt phẳng là độ dài đoạn vuông góc hạ từ điểm xuống mặt phẳng.", r"d(M, (P)) = MH", "NUMERIC", "SA vuông góc đáy, SA=3. Khoảng cách từ S đến đáy bằng:", "3", "NUMERIC", [], "3"),
    ("Bài 27: Thể tích", "Chương VII: Quan hệ vuông góc trong không gian", "Thể tích chóp bằng 1/3 diện tích đáy nhân chiều cao. Lăng trụ bằng đáy nhân chiều cao.", r"V_{\text{chóp}} = \frac{1}{3} S_d h", "NUMERIC", "Chóp có đáy diện tích 6, chiều cao 4. Thể tích bằng:", "8", "NUMERIC", [], "8"),
    ("Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất", "Biến cố giao xảy ra khi cả 2 cùng xảy ra. Độc lập khi xác suất cái này không ảnh hưởng cái kia.", r"A \cap B, A \cup B", "NUMERIC", "Hai biến cố xung khắc thì giao của chúng là biến cố không thể? (1: Đúng, 0: Sai)", "1", "NUMERIC", [], "1"),
    ("Bài 29: Công thức cộng xác suất", "Chương VIII: Các quy tắc tính xác suất", "P(A hợp B) = P(A) + P(B) - P(A giao B). Nếu xung khắc thì P(A hợp B) = P(A) + P(B).", r"P(A \cup B) = P(A) + P(B)", "NUMERIC", "P(A)=0.3, P(B)=0.4, A và B xung khắc. P(A hợp B) bằng:", "0.7", "NUMERIC", [], "0.7"),
    ("Bài 30: Công thức nhân xác suất cho hai biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất", "Nếu A và B độc lập thì P(A giao B) bằng tích P(A) nhân P(B).", r"P(AB) = P(A) \cdot P(B)", "NUMERIC", "P(A)=0.5, P(B)=0.4 độc lập. P(AB) bằng:", "0.2", "NUMERIC", [], "0.2"),
    ("Bài 31: Định nghĩa và ý nghĩa của đạo hàm", "Chương IX: Đạo hàm", "Đạo hàm là giới hạn tỉ số delta y chia delta x khi delta x tiến về 0. Ý nghĩa hệ số góc tiếp tuyến.", r"f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}", "NUMERIC", "Hệ số góc của tiếp tuyến đồ thị hàm số tại x0 chính là f'(x0)? (1: Đúng, 0: Sai)", "1", "NUMERIC", [], "1"),
    ("Bài 32: Các quy tắc tính đạo hàm", "Chương IX: Đạo hàm", "Đạo hàm x mũ n bằng n nhân x mũ n-1. Đạo hàm u nhân v bằng u'v + uv'.", r"(u \cdot v)' = u'v + uv'", "NUMERIC", "Đạo hàm của y = x^2 tại x = 3 bằng:", "6", "NUMERIC", [], "6"),
    ("Bài 33: Đạo hàm cấp hai", "Chương IX: Đạo hàm", "Đạo hàm cấp hai là đạo hàm của đạo hàm cấp một. Biểu thị gia tốc trong chuyển động cơ học.", r"y'' = (y')'", "NUMERIC", "Đạo hàm cấp hai của y = x^3 là 6x. Tại x = 2 giá trị bằng:", "12", "NUMERIC", [], "12")
]

LESSONS_12 = [
    ("Bài 1: Tính đơn điệu và cực trị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số", "y phẩy đổi dấu từ dương sang âm là cực đại, từ âm sang dương là cực tiểu.", r"f'(x) = 0", "NUMERIC", "Giá trị cực tiểu của hàm số y = x^3 - 3x + 2 là:", "0", "NUMERIC", [], "0"),
    ("Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số", "Khảo sát trên đoạn bằng cách tính giá trị tại 2 đầu mút và các điểm đạo hàm triệt tiêu.", r"\max_{[a;b]} f(x)", "NUMERIC", "Giá trị lớn nhất của y = x^3 - 3x trên [0; 2] bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 3: Đường tiệm cận của đồ thị hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số", "Mẫu triệt tiêu tử khác 0 là tiệm cận đứng. Giới hạn khi x ra vô cùng là tiệm cận ngang.", r"x = x_0, y = y_0", "NUMERIC", "Tiệm cận ngang của y = (2x-3)/(x+1) là y bằng:", "2", "NUMERIC", [], "2"),
    ("Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số", "Các bước khảo sát hàm bậc ba, phân thức bậc nhất trên bậc nhất, bậc hai trên bậc nhất.", r"y = \frac{ax+b}{cx+d}", "NUMERIC", "Tâm đối xứng của đồ thị y = (2x-3)/(x+1) có hoành độ x bằng:", "-1", "NUMERIC", [], "-1"),
    ("Bài 5: Ứng dụng đạo hàm giải quyết bài toán thực tiễn", "Chương I: Ứng dụng đạo hàm khảo sát hàm số", "Mô hình hóa hàm số mục tiêu (chi phí, diện tích, thể tích) rồi tìm cực trị.", r"S'(x) = 0", "NUMERIC", "Hộp không nắp đáy vuông thể tích 32 dm3. Diện tích vật liệu nhỏ nhất (dm2):", "48", "NUMERIC", [], "48"),
    ("Bài 6: Vectơ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian", "Quy tắc hình hộp: AC' = AB + AD + AA'. Vectơ đối, tích vô hướng trong không gian.", r"\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}", "NUMERIC", "Cho tứ diện ABCD. Vectơ AB + BC bằng AC? (1: Đúng, 0: Sai)", "1", "NUMERIC", [], "1"),
    ("Bài 7: Hệ trục tọa độ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian", "Hệ trục Oxyz gồm 3 trục vuông góc. Tọa độ điểm M(x;y;z) và hình chiếu.", r"M(x; y; z)", "NUMERIC", "Hình chiếu của điểm M(2; -3; 4) lên trục Oz có cao độ z bằng:", "4", "NUMERIC", [], "4"),
    ("Bài 8: Biểu thức tọa độ của các phép toán vectơ", "Chương II: Vectơ và hệ tọa độ trong không gian", "Cộng trừ theo tọa độ. Tích vô hướng x1x2 + y1y2 + z1z2. Tích có hướng vuông góc với cả hai vectơ.", r"\vec{u}\cdot\vec{v} = x_1x_2 + y_1y_2 + z_1z_2", "NUMERIC", "Độ dài vectơ a = (2; -3; 6) bằng:", "7", "NUMERIC", [], "7"),
    ("Bài 9: Khoảng biến thiên và khoảng tứ phân vị", "Chương III: Các số đặc trưng đo mức độ phân tán", "Khoảng biến thiên R bằng đầu mút phải nhóm cuối trừ đầu mút trái nhóm đầu.", r"\Delta_Q = Q_3 - Q_1", "NUMERIC", "Nếu Q3 = 15.14 và Q1 = 12 thì khoảng tứ phân vị delta Q bằng:", "3.14", "NUMERIC", [], "3.14"),
    ("Bài 10: Phương sai và độ lệch chuẩn", "Chương III: Các số đặc trưng đo mức độ phân tán", "Phương sai là trung bình bình phương các độ lệch so với số trung bình. Độ lệch chuẩn bằng căn phương sai.", r"s = \sqrt{s^2}", "NUMERIC", "Nếu phương sai s^2 = 16 thì độ lệch chuẩn s bằng:", "4", "NUMERIC", [], "4"),
    ("Bài 11: Nguyên hàm", "Chương IV: Nguyên hàm và tích phân", "Nguyên hàm của x^n bằng x^(n+1)/(n+1). Nguyên hàm của e^x là e^x, của cos x là sin x.", r"\int f(x)dx = F(x) + C", "NUMERIC", "Nguyên hàm của f(x) = 2x là x^2 + C. F(2) - F(0) bằng:", "4", "NUMERIC", [], "4"),
    ("Bài 12: Tích phân", "Chương IV: Nguyên hàm và tích phân", "Định lý Newton - Leibniz: Tích phân từ a đến b của f(x)dx bằng F(b) trừ F(a).", r"\int_a^b f(x)dx = F(b) - F(a)", "NUMERIC", "Tích phân từ 0 đến 2 của (2x + 1)dx bằng:", "6", "NUMERIC", [], "6"),
    ("Bài 13: Ứng dụng hình học của tích phân", "Chương IV: Nguyên hàm và tích phân", "Diện tích hình phẳng giới hạn bởi đồ thị và trục hoành. Thể tích khối tròn xoay quanh Ox.", r"S = \int_a^b |f(x)|dx, V = \pi\int_a^b f^2(x)dx", "NUMERIC", "Diện tích giới hạn bởi y = x^2 - 4x và Ox (phân số dạng a/b):", "32/3", "NUMERIC", [], "32/3"),
    ("Bài 14: Phương trình mặt phẳng", "Chương V: Phương pháp tọa độ trong không gian", "Mặt phẳng có VTPT n=(A;B;C) qua M0: A(x-x0) + B(y-y0) + C(z-z0) = 0.", r"Ax + By + Cz + D = 0", "NUMERIC", "Khoảng cách từ O(0;0;0) đến 2x - 2y + z - 9 = 0 bằng:", "3", "NUMERIC", [], "3"),
    ("Bài 15: Phương trình đường thẳng trong không gian", "Chương V: Phương pháp tọa độ trong không gian", "Đường thẳng qua M0 và có VTCP u=(a;b;c). Dạng tham số và dạng chính tắc.", r"\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}", "NUMERIC", "Đường thẳng (x-1)/2 = (y+2)/-1 = (z-3)/1 đi qua điểm M(1; -2; z0). z0 bằng:", "3", "NUMERIC", [], "3"),
    ("Bài 16: Công thức tính góc trong không gian", "Chương V: Phương pháp tọa độ trong không gian", "Góc giữa 2 mặt phẳng qua cos tích vô hướng 2 VTPT. Góc giữa đường và mặt qua sin tích có hướng.", r"\cos\varphi = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}", "NUMERIC", "Hai mặt phẳng có VTPT n1=(1;0;0) và n2=(0;1;0) tạo với nhau góc (độ):", "90", "NUMERIC", [], "90"),
    ("Bài 17: Phương trình mặt cầu", "Chương V: Phương pháp tọa độ trong không gian", "Mặt cầu tâm I(a;b;c) bán kính R có dạng (x-a)^2 + (y-b)^2 + (z-c)^2 = R^2.", r"(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2", "NUMERIC", "Bán kính của mặt cầu (x-2)^2 + (y+1)^2 + (z-3)^2 = 25 bằng:", "5", "NUMERIC", [], "5"),
    ("Bài 18: Xác suất có điều kiện", "Chương VI: Xác suất có điều kiện", "Xác suất của A khi biết B đã xảy ra bằng P(AB) chia cho P(B).", r"P(A|B) = \frac{P(AB)}{P(B)}", "NUMERIC", "Cho P(AB) = 0.2 và P(B) = 0.5. Xác suất P(A|B) bằng:", "0.4", "NUMERIC", [], "0.4"),
    ("Bài 19: Công thức xác suất toàn phần và công thức Bayes", "Chương VI: Xác suất có điều kiện", "Xác suất toàn phần tính qua hệ biến cố đầy đủ. Công thức Bayes tính xác suất hậu nghiệm.", r"P(A) = \sum P(B_i)P(A|B_i)", "NUMERIC", "Nếu P(B1)=0.4, P(A|B1)=0.5, P(B2)=0.6, P(A|B2)=0.2 thì P(A) bằng:", "0.32", "NUMERIC", [], "0.32")
]

def build_curriculum_dict(raw_list):
    res = {}
    for idx, item in enumerate(raw_list):
        title, chap, script, math_note, qtype, content, target, ans_type, opts, def_ans = item
        res[title] = {
            "chapter": chap,
            "video_title": f"Bài giảng vi mô: {title}",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": f"Chào em! Trong bài học {title}, em hãy ghi nhớ: {script} Khi làm bài tập, hãy biến đổi cẩn thận và kiểm tra lại điều kiện nhé!",
            "has_3d": True if ("không gian" in title or "Oxyz" in title or "Vectơ" in title or "mặt phẳng" in title or "mặt cầu" in title) else False,
            "smart_notes": f"- **Khái niệm cốt lõi:**\n{math_note}\n\n- **Ghi chú phương pháp:**\n{script}",
            "exercise": {
                "id": f"EX_{idx+1}",
                "title": f"Bài tập tự luyện kiểm minh chứng - {title}",
                "content": content,
                "question_type": ans_type,
                "options": opts,
                "target_val": target,
                "hint_1": f"Định lý áp dụng: {math_note}",
                "hint_2": f"Bước giải mấu chốt: {script}",
                "hint_3": f"Kết quả chính xác cần đạt là: {target}",
                "solution_text": f"Áp dụng lý thuyết: {math_note}. Thực hiện biến đổi suy ra đáp số chính xác: {target}."
            }
        }
    return res

CURRICULUM_DATA = {
    "Khối 10": build_curriculum_dict(LESSONS_10),
    "Khối 11": build_curriculum_dict(LESSONS_11),
    "Khối 12": build_curriculum_dict(LESSONS_12)
}

# ==============================================================================
# 4. KHO ĐỀ KHẢO THÍ CHUẨN MA TRẬN MỚI CỦA BỘ GD&ĐT
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
    st.markdown("<p style='text-align: center; color: #475569;'>Học liệu đầy đủ: 27 bài Khối 10, 33 bài Khối 11, 19 bài Khối 12 (KNTT)</p>", unsafe_allow_html=True)

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
            st.caption("💡 Tài khoản: `HS11_01`, `HS10_01`, `HS12_01` (Pass: `123`). Admin: `admin` / `gstoan2026`.")
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
# 9. PHÂN HỆ HỌC SINH (DANH SÁCH BÀI HỌC CÓ THANH CUỘN & ĐẦY ĐỦ 3 KHỐI)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN KHỐI LỚP VÀ DANH SÁCH BÀI HỌC CÓ THANH CUỘN
c_gr, c_les = st.columns([1, 2.5])
with c_gr:
    user_grade_default = 0 if student_info.get("grade") == 10 else (2 if student_info.get("grade") == 12 else 1)
    sel_grade = st.selectbox("📚 Chọn Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

with c_les:
    lesson_list = list(CURRICULUM_DATA[sel_grade].keys())
    sel_lesson = st.selectbox(
        f"📖 Danh sách bài học ({len(lesson_list)} bài - Cuộn chuột để xem hết):",
        lesson_list,
        help="Danh mục bài học có thanh cuộn mượt mà hỗ trợ duyệt nhanh toàn bộ chương trình."
    )

cur_data = CURRICULUM_DATA[sel_grade][sel_lesson]

# 4 TAB HỌC TẬP TƯƠNG TÁC
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Video, Thuyết Minh & 3D)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC KÈM ÂM THANH THUYẾT MINH
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
            user_submitted_ans = st.text_input("Nhập kết quả/đáp số của em (ví dụ: 12 hoặc -0.8 hoặc 32/3):", key=f"num_ex_{ex['id']}")

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
                            sim_t = "Bài toán tương tự cùng dạng: Đổi số liệu tương đương để học sinh tự rèn luyện."
                    else:
                        sim_t = "Bài toán tương tự: Đổi số liệu tương đương bám sát SGK Kết nối tri thức."
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
