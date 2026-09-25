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
# 1. CẤU HÌNH GIAO DIỆN & STYLE THANH CUỘN / TƯƠNG TÁC BƯỚC
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Thanh cuộn chuyên biệt cho Dropdown danh sách bài học */
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
    .step-box-active {
        background-color: #FFFFFF !important;
        border: 2px solid #2563EB !important;
        border-radius: 12px !important;
        padding: 14px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.08) !important;
    }
    .step-box-done {
        background-color: #F8FAFC !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 12px !important;
        padding: 14px !important;
        margin-bottom: 12px !important;
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
# 3. KHO HỌC LIỆU SỐ TOÀN DIỆN: ĐỦ 27 BÀI (K10), 33 BÀI (K11), 19 BÀI (K12)
# ==============================================================================
RAW_DATA_10 = [
    ("Bài 1: Mệnh đề toán học", "Chương I: Mệnh đề và tập hợp",
     "Mệnh đề là khẳng định đúng hoặc sai. Một mệnh đề không thể vừa đúng vừa sai.",
     r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)} \quad \text{và} \quad \overline{\exists x \in X, P(x)} \iff \forall x \in X, \overline{P(x)}",
     "Phủ định của dấu lớn hơn (>) là dấu nhỏ hơn hoặc bằng (<=), không được bỏ quên dấu bằng.",
     "Cho mệnh đề P: 'Mọi số thực x đều có x^2 >= 0'. Phủ định của P là mệnh đề nào?", "A", "CHOICE", ["A. Tồn tại x sao cho x^2 < 0", "B. Tồn tại x sao cho x^2 <= 0", "C. Mọi x có x^2 < 0"], "A"),
     
    ("Bài 2: Tập hợp và các phép toán trên tập hợp", "Chương I: Mệnh đề và tập hợp",
     "Giao của hai tập hợp lấy phần tử chung. Hợp lấy tất cả phần tử thuộc ít nhất một trong hai tập hợp. Hiệu A trừ B lấy phần tử thuộc A nhưng không thuộc B.",
     r"A \cap B = \{x \mid x \in A \text{ và } x \in B\}; \quad A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}",
     "Lưu ý các tập con của tập số thực R: khoảng (a; b), đoạn [a; b], nửa khoảng [a; b). Tránh nhầm lẫn ngoặc đơn và ngoặc vuông.",
     "Cho A = [1; 5] và B = (3; 7). Số nguyên thuộc tập hợp A giao B gồm bao nhiêu số?", "2", "NUMERIC", [], "2"),

    ("Bài 3: Bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn",
     "Bất phương trình bậc nhất hai ẩn x, y có dạng tổng quát là ax + by <= c. Đường thẳng bờ d: ax + by = c chia mặt phẳng làm hai nửa.",
     r"ax + by \le c \quad (a^2 + b^2 \neq 0)",
     "Để xác định miền nghiệm, chọn điểm thử O(0;0) nếu O không nằm trên đường thẳng bờ. Thay tọa độ vào, nếu thỏa mãn thì miền chứa O là miền nghiệm.",
     "Điểm M(1; 2) có thuộc miền nghiệm của bất phương trình 2x - y + 1 > 0 không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),

    ("Bài 4: Hệ bất phương trình bậc nhất hai ẩn", "Chương II: Bất phương trình bậc nhất hai ẩn",
     "Miền nghiệm của hệ là phần giao của các miền nghiệm của từng bất phương trình trong hệ. Miền nghiệm thường là một miền đa giác lồi.",
     r"F(x; y) = ax + by \quad \text{đạt GTLN/GTNN tại một trong các đỉnh của miền đa giác nghiệm}",
     "Trong bài toán thực tế tối ưu hóa lợi nhuận F(x;y), luôn tính giá trị F tại tất cả các đỉnh của miền đa giác rồi so sánh.",
     "Cho hệ x + y <= 4, x >= 0, y >= 0. Giá trị lớn nhất của F(x;y) = 3x + 2y trên miền nghiệm bằng bao nhiêu?", "12", "NUMERIC", [], "12"),

    ("Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ", "Chương III: Hệ thức lượng trong tam giác",
     "Với mỗi góc alpha (0 đến 180 độ), điểm M(x; y) trên nửa đường tròn đơn vị có tung độ y = sin alpha, hoành độ x = cos alpha.",
     r"\sin^2\alpha + \cos^2\alpha = 1; \quad \tan\alpha = \frac{\sin\alpha}{\cos\alpha} \ (\alpha \neq 90^\circ); \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
     "Khi góc alpha tù (90 đến 180 độ), hoành độ âm nên cos alpha < 0 và tan alpha < 0, nhưng tung độ sin alpha luôn dương.",
     "Tính giá trị của biểu thức P = sin(30 độ) + cos(60 độ) (dưới dạng số thập phân):", "1", "NUMERIC", [], "1"),

    ("Bài 6: Hệ thức lượng trong tam giác", "Chương III: Hệ thức lượng trong tam giác",
     "Định lý Côsin áp dụng khi biết 2 cạnh và góc xen giữa. Định lý Sin áp dụng khi biết 1 cạnh và 2 góc kề, hoặc bán kính R đường tròn ngoại tiếp.",
     r"a^2 = b^2 + c^2 - 2bc \cos A; \quad \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R; \quad S = \frac{1}{2}bc\sin A = \frac{abc}{4R} = pr",
     "Khi áp dụng định lý Côsin tính góc A, dùng công thức hệ quả: cos A = (b^2 + c^2 - a^2) / (2bc). Nếu cos A < 0 thì góc A là góc tù.",
     "Tam giác ABC có b = 8, c = 5, góc A = 60 độ. Độ dài cạnh a bằng bao nhiêu?", "7", "NUMERIC", [], "7"),

    ("Bài 7: Các khái niệm mở đầu về vectơ", "Chương IV: Vectơ",
     "Vectơ là một đoạn thẳng có hướng. Hai vectơ cùng phương khi giá của chúng song song hoặc trùng nhau.",
     r"\vec{a} = \vec{b} \iff |\vec{a}| = |\vec{b}| \quad \text{và} \quad \vec{a}, \vec{b} \text{ cùng hướng}",
     "Vectơ không có độ dài bằng 0 và cùng phương, cùng hướng với mọi vectơ.",
     "Hai vectơ có cùng độ dài thì chắc chắn bằng nhau. Khẳng định này Đúng hay Sai? (1: Đúng, 0: Sai)", "0", "NUMERIC", [], "0"),

    ("Bài 8: Tổng và hiệu của hai vectơ", "Chương IV: Vectơ",
     "Quy tắc 3 điểm nối đuôi: AB cộng BC bằng AC. Quy tắc hình bình hành với hai vectơ chung gốc: AB cộng AD bằng AC.",
     r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{AB} + \vec{AD} = \vec{AC} \ (\text{ABCD là hình bình hành}); \quad \vec{AB} - \vec{AC} = \vec{CB}",
     "Quy tắc trừ chung gốc: AB trừ AC bằng CB, không phải BC.",
     "Cho tam giác đều ABC cạnh 2. Độ dài của vectơ AB + BC bằng bao nhiêu?", "2", "NUMERIC", [], "2"),

    ("Bài 9: Tích của một vectơ với một số", "Chương IV: Vectơ",
     "Tích của số k khác 0 với vectơ a là vectơ cùng hướng khi k > 0, ngược hướng khi k < 0. Độ dài bằng |k| lần độ dài vectơ a.",
     r"k\vec{a}; \quad I \text{ là trung điểm } AB \iff \vec{IA} + \vec{IB} = \vec{0}; \quad G \text{ là trọng tâm } \Delta ABC \iff \vec{GA} + \vec{GB} + \vec{GC} = \vec{0}",
     "Điều kiện để hai vectơ cùng phương: Có số k sao cho vectơ a bằng k lần vectơ b.",
     "Gọi G là trọng tâm tam giác ABC. Độ dài vectơ GA + GB + GC bằng bao nhiêu?", "0", "NUMERIC", [], "0"),

    ("Bài 10: Vectơ trong mặt phẳng tọa độ", "Chương IV: Vectơ",
     "Mỗi vectơ u phân tích qua hai vectơ đơn vị i và j. Tọa độ của vectơ bằng tọa độ điểm cuối trừ điểm đầu.",
     r"\vec{u} = (x; y) \iff \vec{u} = x\vec{i} + y\vec{j}; \quad \vec{AB} = (x_B - x_A; y_B - y_A); \quad x_I = \frac{x_A + x_B}{2}, \ y_I = \frac{y_A + y_B}{2}",
     "Tọa độ trọng tâm G bằng trung bình cộng tọa độ ba đỉnh: xG = (xA + xB + xC)/3.",
     "Cho A(1; 3) và B(5; 7). Tọa độ trung điểm I của đoạn thẳng AB có hoành độ xI bằng bao nhiêu?", "3", "NUMERIC", [], "3"),

    ("Bài 11: Tích vô hướng của hai vectơ", "Chương IV: Vectơ",
     "Tích vô hướng bằng tích độ dài nhân cosin góc giữa chúng. Trong hệ tọa độ, tích vô hướng bằng tổng tích các tọa độ tương ứng.",
     r"\vec{u} \cdot \vec{v} = |\vec{u}| |\vec{v}| \cos(\vec{u}, \vec{v}) = x_1 x_2 + y_1 y_2; \quad \vec{u} \perp \vec{v} \iff x_1 x_2 + y_1 y_2 = 0",
     "Hai vectơ vuông góc với nhau khi và chỉ khi tích vô hướng bằng 0.",
     "Cho u = (2; -3) và v = (3; 2). Tích vô hướng u.v bằng bao nhiêu?", "0", "NUMERIC", [], "0"),

    ("Bài 12: Số gần đúng và sai số", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Sai số tuyệt đối đo khoảng cách giữa giá trị gần đúng và số đúng. Quy tròn số theo hàng quy chuẩn.",
     r"\Delta_a = |a - \overline{a}| \le d; \quad \delta_a = \frac{\Delta_a}{|a|} \le \frac{d}{|a|}",
     "Nhìn chữ số ngay sau hàng quy tròn: nếu >= 5 tăng 1 đơn vị, nếu < 5 giữ nguyên.",
     "Quy tròn số 12.3456 đến hàng phần trăm (chữ số thập phân thứ hai) được kết quả là:", "12.35", "NUMERIC", [], "12.35"),

    ("Bài 13: Các số đặc trưng đo xu thế trung tâm", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Số trung bình cộng phản ánh giá trị trung tâm. Trung vị chia mẫu số liệu thành hai nửa bằng nhau. Mốt là giá trị xuất hiện nhiều nhất.",
     r"\overline{x} = \frac{\sum x_i}{n}; \quad M_e = x_{\frac{n+1}{2}} \text{ (n lẻ)}; \quad M_e = \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} \text{ (n chẵn)}",
     "Khi mẫu có số liệu bất thường, trung vị đại diện tốt hơn số trung bình.",
     "Cho dãy điểm số: 3, 5, 7, 8, 9. Số trung vị của mẫu số liệu trên bằng bao nhiêu?", "7", "NUMERIC", [], "7"),

    ("Bài 14: Các số đặc trưng đo độ phân tán", "Chương V: Số đặc trưng đo xu thế trung tâm",
     "Khoảng biến thiên R bằng max trừ min. Khoảng tứ phân vị delta Q bằng Q3 trừ Q1. Phương sai s^2 và độ lệch chuẩn s đo độ phân tán.",
     r"R = x_{\max} - x_{\min}; \quad \Delta_Q = Q_3 - Q_1; \quad s = \sqrt{s^2}",
     "Độ lệch chuẩn s luôn cùng đơn vị với số liệu gốc.",
     "Mẫu số liệu có giá trị nhỏ nhất là 10 và giá trị lớn nhất là 35. Khoảng biến thiên R bằng:", "25", "NUMERIC", [], "25"),

    ("Bài 15: Hàm số và đồ thị", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Hàm số y = f(x). Hàm đồng biến khi x tăng y tăng; hàm nghịch biến khi x tăng y giảm.",
     r"x_1 < x_2 \Rightarrow f(x_1) < f(x_2) \ (\text{Đồng biến}); \quad x_1 < x_2 \Rightarrow f(x_1) > f(x_2) \ (\text{Nghịch biến})",
     "Mẫu số phải khác 0; biểu thức dưới căn bậc hai phải lớn hơn hoặc bằng 0.",
     "Tìm giá trị của m để hàm số y = (m - 2)x + 3 đồng biến trên R. Điều kiện của m là m > ?", "2", "NUMERIC", [], "2"),

    ("Bài 16: Hàm số bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Đồ thị parabol có trục đối xứng x = -b/(2a) và tọa độ đỉnh I(-b/(2a); -Delta/(4a)).",
     r"y = ax^2 + bx + c; \quad I\left(-\frac{b}{2a}; -\frac{\Delta}{4a}\right); \quad x = -\frac{b}{2a}",
     "Nếu a > 0 parabol quay bề lõm lên trên, nếu a < 0 quay bề lõm xuống dưới.",
     "Hoành độ đỉnh của parabol y = x^2 - 6x + 5 bằng bao nhiêu?", "3", "NUMERIC", [], "3"),

    ("Bài 17: Dấu của tam thức bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Tam thức f(x) = ax^2 + bx + c. Khi Delta < 0 thì tam thức cùng dấu với a với mọi x. Khi Delta > 0, trong khoảng hai nghiệm trái dấu với a.",
     r"\Delta < 0 \Rightarrow a \cdot f(x) > 0, \ \forall x \in \mathbb{R}; \quad \Delta > 0: \text{Trong trái - Ngoài cùng}",
     "Khẩu quyết 'Trong trái ngoài cùng' chỉ áp dụng khi tam thức có 2 nghiệm phân biệt.",
     "Bất phương trình x^2 - 4x + 3 < 0 có tập nghiệm là khoảng (1; b). Giá trị của b bằng:", "3", "NUMERIC", [], "3"),

    ("Bài 18: Phương trình quy về phương trình bậc hai", "Chương VI: Hàm số, đồ thị và ứng dụng",
     "Phương trình chứa căn bậc hai căn f(x) = g(x) giải bằng cách đặt điều kiện g(x) >= 0 rồi bình phương hai vế.",
     r"\sqrt{f(x)} = g(x) \iff \begin{cases} g(x) \ge 0 \\ f(x) = [g(x)]^2 \end{cases}",
     "Bắt buộc đối chiếu điều kiện g(x) >= 0 để loại nghiệm ngoại lai.",
     "Phương trình căn(2x - 3) = x - 3 có bao nhiêu nghiệm thực thỏa mãn?", "1", "NUMERIC", [], "1"),

    ("Bài 19: Phương trình đường thẳng", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Đường thẳng qua M(x0; y0) có VTPT n(A; B) có phương trình tổng quát A(x - x0) + B(y - y0) = 0.",
     r"Ax + By + C = 0; \quad \begin{cases} x = x_0 + at \\ y = y_0 + bt \end{cases}; \quad \vec{n} = (A; B) \perp \vec{u} = (-B; A)",
     "Chuyển đổi giữa VTPT n(A; B) và VTCP u(-B; A).",
     "Đường thẳng 3x - 4y + 5 = 0 có một vectơ pháp tuyến là n = (3; b). Giá trị của b là:", "-4", "NUMERIC", [], "-4"),

    ("Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Công thức tính khoảng cách từ điểm M(x0; y0) đến đường thẳng Delta và góc giữa hai đường thẳng.",
     r"d(M, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}; \quad \cos(\Delta_1, \Delta_2) = \frac{|A_1 A_2 + B_1 B_2|}{\sqrt{A_1^2 + B_1^2}\sqrt{A_2^2 + B_2^2}}",
     "Góc giữa hai đường thẳng không vượt quá 90 độ, tử số công thức cosin luôn có giá trị tuyệt đối.",
     "Khoảng cách từ gốc tọa độ O(0; 0) đến đường thẳng 3x - 4y + 10 = 0 bằng bao nhiêu?", "2", "NUMERIC", [], "2"),

    ("Bài 21: Đường tròn trong mặt phẳng tọa độ", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Phương trình đường tròn tâm I(a; b) bán kính R là (x - a)^2 + (y - b)^2 = R^2.",
     r"(x - a)^2 + (y - b)^2 = R^2; \quad R = \sqrt{a^2 + b^2 - c} \ (a^2 + b^2 - c > 0)",
     "Chia hệ số của x và y cho -2 để tìm tọa độ tâm I(a; b).",
     "Bán kính của đường tròn (x - 1)^2 + (y + 3)^2 = 25 bằng bao nhiêu?", "5", "NUMERIC", [], "5"),

    ("Bài 22: Ba đường conic", "Chương VII: Phương pháp tọa độ trong mặt phẳng",
     "Elip x^2/a^2 + y^2/b^2 = 1 (a^2 = b^2 + c^2). Hypebol có dấu trừ ở giữa. Parabol y^2 = 2px.",
     r"\text{Elip: } \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1; \quad \text{Hypebol: } \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1; \quad \text{Parabol: } y^2 = 2px",
     "Trong Elip, độ dài trục lớn là 2a, trục bé là 2b, tiêu cự là 2c.",
     "Độ dài trục lớn của Elip x^2/25 + y^2/9 = 1 bằng bao nhiêu?", "10", "NUMERIC", [], "10"),

    ("Bài 23: Quy tắc đếm", "Chương VIII: Đại số tổ hợp",
     "Quy tắc cộng dùng cho các phương án độc lập. Quy tắc nhân dùng cho các công đoạn liên tiếp nối nhau.",
     r"\text{Quy tắc cộng: } N = m + n; \quad \text{Quy tắc nhân: } N = m \times n",
     "Nếu xong bước 1 mà xong luôn việc thì dùng cộng; nếu phải làm tiếp mới xong thì dùng nhân.",
     "Một quán ăn có 4 món khai vị và 5 món chính. Có bao nhiêu cách chọn 1 món khai vị và 1 món chính?", "20", "NUMERIC", [], "20"),

    ("Bài 24: Hoán vị, chỉnh hợp và tổ hợp", "Chương VIII: Đại số tổ hợp",
     "Hoán vị Pn = n!. Chỉnh hợp chọn và xếp thứ tự. Tổ hợp chọn mà không xếp thứ tự.",
     r"P_n = n!; \quad A_n^k = \frac{n!}{(n-k)!}; \quad C_n^k = \frac{n!}{k!(n-k)!}",
     "Đổi thứ tự tạo kết quả mới thì dùng Chỉnh hợp, không đổi thì dùng Tổ hợp.",
     "Có bao nhiêu cách chọn ra 2 học sinh từ một nhóm gồm 5 học sinh đi lao động?", "10", "NUMERIC", [], "10"),

    ("Bài 25: Nhị thức Newton", "Chương VIII: Đại số tổ hợp",
     "Công thức khai triển (a + b)^4 và (a + b)^5 với các hệ số nhị thức đối xứng.",
     r"(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4; \quad (a + b)^5 = a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5",
     "Khi khai triển (a - b)^n, các dấu cộng trừ xen kẽ bắt đầu bằng dấu cộng.",
     "Hệ số của x^3 trong khai triển của (x + 1)^4 bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 26: Biến cố và định nghĩa cổ điển của xác suất", "Chương IX: Tính xác suất theo định nghĩa cổ điển",
     "Xác suất biến cố A bằng tỉ số giữa số kết quả thuận lợi n(A) và số phần tử không gian mẫu n(Omega).",
     r"P(A) = \frac{n(A)}{n(\Omega)}; \quad 0 \le P(A) \le 1; \quad P(\overline{A}) = 1 - P(A)",
     "Xác suất chắc chắn bằng 1, biến cố không thể bằng 0.",
     "Gieo một con xúc xắc cân đối 6 mặt. Xác suất để xuất hiện mặt chấm chẵn là bao nhiêu?", "0.5", "NUMERIC", [], "0.5"),

    ("Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển", "Chương IX: Tính xác suất theo định nghĩa cổ điển",
     "Sử dụng công thức tổ hợp và phương pháp biến cố đối khi bài toán có cụm từ 'ít nhất'.",
     r"n(\Omega) = C_n^k; \quad P(A) = \frac{n(A)}{n(\Omega)} = 1 - P(\overline{A})",
     "Đề bài có cụm từ 'ít nhất một...', hãy tính qua biến cố đối 'không có cái nào'.",
     "Một hộp có 3 bi đỏ và 2 bi xanh. Lấy ngẫu nhiên 1 viên bi. Xác suất lấy được viên bi đỏ bằng:", "0.6", "NUMERIC", [], "0.6")
]

RAW_DATA_11 = [
    ("Bài 1: Giá trị lượng giác của góc lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Trục sin là trục đứng, trục cos là trục ngang. Góc phần tư thứ II có sin dương, cos âm.",
     r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}; \quad 1 + \cot^2\alpha = \frac{1}{\sin^2\alpha}",
     "Nhất cả (I: all > 0), Nhì sin (II: sin > 0), Tam tang (III: tan > 0), Tứ cos (IV: cos > 0).",
     "Cho góc alpha thuộc góc phần tư thứ II và sin alpha = 3/5. Giá trị của cos alpha bằng:", "-0.8", "NUMERIC", ["-4/5", "-0,8"], "-0.8"),

    ("Bài 2: Công thức lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Công thức cộng, công thức nhân đôi sin 2a = 2 sin a cos a, công thức hạ bậc.",
     r"\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b; \quad \sin 2a = 2\sin a \cos a; \quad \cos 2a = \cos^2 a - \sin^2 a",
     "Công thức nhân đôi cos 2a có 3 dạng biểu diễn khác nhau tùy bài toán.",
     "Nếu sin a * cos a = 0.25 thì giá trị của sin 2a bằng bao nhiêu?", "0.5", "NUMERIC", [], "0.5"),

    ("Bài 3: Hàm số lượng giác", "Chương I: Hàm số và phương trình lượng giác",
     "Hàm sin và cos tuần hoàn chu kỳ 2pi, tập giá trị [-1; 1]. Hàm tan tuần hoàn chu kỳ pi.",
     r"y = \sin x \ (T = 2\pi); \quad y = \cos x \ (T = 2\pi); \quad y = \tan x \ (T = \pi)",
     "y = sin x là hàm số lẻ, y = cos x là hàm số chẵn.",
     "Giá trị lớn nhất của hàm số y = 3sin x + 2 bằng bao nhiêu?", "5", "NUMERIC", [], "5"),

    ("Bài 4: Phương trình lượng giác cơ bản", "Chương I: Hàm số và phương trình lượng giác",
     "sin x = sin alpha có hai họ nghiệm alpha và pi - alpha cộng k2pi. cos x = cos alpha có nghiệm đối nhau.",
     r"\sin x = \sin\alpha \iff \left[\begin{array}{l} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{array}\right.; \quad \cos x = \cos\alpha \iff x = \pm\alpha + k2\pi",
     "Phương trình sin x = m có nghiệm khi và chỉ khi -1 <= m <= 1.",
     "Số nghiệm của phương trình sin x = 1 trên đoạn [0; 2pi] là:", "1", "NUMERIC", [], "1"),

    ("Bài 5: Dãy số", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Dãy số un là hàm số trên N*. Dãy tăng khi u(n+1) > un với mọi n. Dãy bị chặn khi bị chặn trên và dưới.",
     r"(u_n): u_{n+1} > u_n \ (\text{Dãy tăng}); \quad m \le u_n \le M \ (\text{Dãy bị chặn})",
     "Có thể xét hiệu u(n+1) - un hoặc tỉ số u(n+1)/un với 1 để xét tính tăng giảm.",
     "Cho dãy số un = 2n + 1. Số hạng thứ 3 (u3) của dãy số bằng bao nhiêu?", "7", "NUMERIC", [], "7"),

    ("Bài 6: Cấp số cộng", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Cấp số cộng có công sai d. Số hạng tổng quát un = u1 + (n - 1)d. Tổng Sn = n(u1 + un)/2.",
     r"u_n = u_1 + (n - 1)d; \quad S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n - 1)d]}{2}",
     "Ba số a, b, c lập thành cấp số cộng khi và chỉ khi a + c = 2b.",
     "Cho cấp số cộng có u1 = 3 và công sai d = 4. Số hạng thứ 5 bằng bao nhiêu?", "19", "NUMERIC", [], "19"),

    ("Bài 7: Cấp số nhân", "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
     "Cấp số nhân có công bội q. Số hạng tổng quát un = u1 * q^(n-1). Tổng n số hạng Sn.",
     r"u_n = u_1 \cdot q^{n-1}; \quad S_n = u_1 \frac{1 - q^n}{1 - q} \ (q \neq 1)",
     "Ba số a, b, c lập thành cấp số nhân khi và chỉ khi a * c = b^2.",
     "Cho cấp số nhân có u1 = 2 và công bội q = 3. Số hạng thứ 3 bằng bao nhiêu?", "18", "NUMERIC", [], "18"),

    ("Bài 8: Mẫu số liệu ghép nhóm", "Chương III: Các số đặc trưng đo xu thế trung tâm",
     "Mẫu ghép nhóm theo các nửa khoảng [a; b). Giá trị đại diện là trung điểm nửa khoảng đó.",
     r"c_i = \frac{a_i + a_{i+1}}{2}; \quad n = \sum n_i",
     "Độ dài của nhóm bằng đầu mút phải trừ đầu mút trái: b - a.",
     "Giá trị đại diện của nhóm số liệu [20; 30) bằng bao nhiêu?", "25", "NUMERIC", [], "25"),

    ("Bài 9: Các số đặc trưng đo xu thế trung tâm", "Chương III: Các số đặc trưng đo xu thế trung tâm",
     "Số trung bình, trung vị Me và mốt Mo của mẫu số liệu ghép nhóm.",
     r"\overline{x} = \frac{1}{n}\sum n_i c_i; \quad M_e = u_m + \frac{\frac{n}{2} - C}{n_m}(u_{m+1} - u_m)",
     "Nhóm chứa trung vị là nhóm đầu tiên có tần số tích lũy đạt tối thiểu n/2.",
     "Nếu mẫu ghép nhóm có cỡ mẫu n = 40, tần số tích lũy tối thiểu của nhóm chứa trung vị là:", "20", "NUMERIC", [], "20"),

    ("Bài 10: Đường thẳng và mặt phẳng trong không gian", "Chương IV: Quan hệ song song trong không gian",
     "Ba điểm không thẳng hàng xác định duy nhất một mặt phẳng. Tứ diện có 4 mặt là tam giác.",
     r"(ABC); \quad (d, A) \ (A \notin d); \quad (a, b) \ (a \cap b = I)",
     "Tứ diện đều có tất cả 6 cạnh đều bằng nhau.",
     "Có bao nhiêu mặt phẳng đi qua 3 điểm không thẳng hàng? Nhập số:", "1", "NUMERIC", [], "1"),

    ("Bài 11: Hai đường thẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "Hai đường thẳng song song cùng nằm trong một mặt phẳng và không có điểm chung. Chéo nhau khi không đồng phẳng.",
     r"a \parallel b \iff a, b \subset (P) \text{ và } a \cap b = \emptyset; \quad a, b \text{ chéo nhau } \iff \nexists (P) \supset a, b",
     "Ba mặt phẳng cắt nhau theo 3 giao tuyến thì 3 giao tuyến hoặc đồng quy hoặc đôi một song song.",
     "Hai đường thẳng không có điểm chung thì chắc chắn song song. Đúng hay Sai? (1: Đúng, 0: Sai)", "0", "NUMERIC", [], "0"),

    ("Bài 12: Đường thẳng và mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "Đường thẳng d song song (P) khi d không nằm trong (P) và d song song với một đường thẳng a trong (P).",
     r"\begin{cases} d \not\subset (P) \\ d \parallel a \subset (P) \end{cases} \Rightarrow d \parallel (P)",
     "Nếu d song song (P), mặt phẳng qua d cắt (P) theo giao tuyến d' thì d' song song d.",
     "Đường thẳng d nằm trong mặt phẳng (P) thì d có song song với (P) không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),

    ("Bài 13: Hai mặt phẳng song song", "Chương IV: Quan hệ song song trong không gian",
     "Mặt phẳng (P) chứa 2 đường thẳng cắt nhau cùng song song với (Q) thì (P) song song (Q).",
     r"\begin{cases} a, b \subset (P), \ a \cap b = I \\ a \parallel (Q), \ b \parallel (Q) \end{cases} \Rightarrow (P) \parallel (Q)",
     "Định lý Thales trong không gian bảo toàn tỉ số các đoạn thẳng chắn trên cát tuyến.",
     "Hai mặt phẳng phân biệt cùng song song mặt phẳng thứ ba thì song song nhau. (1: Đúng, 0: Sai)", "1", "NUMERIC", [], "1"),

    ("Bài 14: Phép chiếu song song", "Chương IV: Quan hệ song song trong không gian",
     "Chiếu song song bảo toàn tính song song, tỉ số độ dài đoạn thẳng cùng phương.",
     r"\text{Chiếu song song: Biến đoạn thẳng thành đoạn thẳng, bảo toàn tính song song}",
     "Hình chiếu song song của hình tròn là một hình elip hoặc một đoạn thẳng.",
     "Phép chiếu song song có luôn luôn bảo toàn độ lớn của góc không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),

    ("Bài 15: Giới hạn của dãy số", "Chương V: Giới hạn. Hàm số liên tục",
     "Giới hạn 1/n^k = 0 khi n tiến ra vô cực. Tổng cấp số nhân lùi vô hạn S = u1 / (1 - q).",
     r"\lim_{n \to \infty} \frac{1}{n^k} = 0; \quad \lim q^n = 0 \ (|q| < 1); \quad S = \frac{u_1}{1 - q}",
     "Chia cả tử và mẫu cho lũy thừa bậc cao nhất của n.",
     "Tính giới hạn của dãy số lim (4n + 3)/(2n - 1) khi n tiến ra dương vô cùng:", "2", "NUMERIC", [], "2"),

    ("Bài 16: Giới hạn của hàm số", "Chương V: Giới hạn. Hàm số liên tục",
     "Khử dạng vô định 0/0 bằng phân tích nhân tử chung (x - x0) hoặc nhân lượng liên hợp.",
     r"\lim_{x \to x_0} \frac{f(x)}{g(x)} \ (\text{Dạng } \frac{0}{0}) \Rightarrow \text{Khử nhân tử } (x - x_0)",
     "Lượng liên hợp bậc hai: căn A - B = (A - B^2) / (căn A + B).",
     "Tính giới hạn: lim (x^2 - 1)/(x - 1) khi x tiến tới 1:", "2", "NUMERIC", [], "2"),

    ("Bài 17: Hàm số liên tục", "Chương V: Giới hạn. Hàm số liên tục",
     "Hàm số liên tục tại x0 khi giới hạn tại x0 bằng f(x0). Hàm số f(a)*f(b) < 0 có nghiệm trên (a; b).",
     r"\lim_{x \to x_0} f(x) = f(x_0); \quad f(a) \cdot f(b) < 0 \Rightarrow \exists c \in (a; b): f(c) = 0",
     "Hàm đa thức liên tục trên toàn bộ trục số R.",
     "Hàm số y = 1/(x - 2) có liên tục tại điểm x = 2 không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),

    ("Bài 18: Lũy thừa với số mũ thực", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Tính chất lũy thừa nhân, chia cùng cơ số. Lũy thừa số mũ không nguyên yêu cầu cơ số dương.",
     r"a^\alpha \cdot a^\beta = a^{\alpha + \beta}; \quad \frac{a^\alpha}{a^\beta} = a^{\alpha - \beta}; \quad a^{\frac{m}{n}} = \sqrt[n]{a^m} \ (a > 0)",
     "Cơ số a phải dương khi xét lũy thừa với số mũ hữu tỉ hoặc vô tỉ.",
     "Giá trị của biểu thức 2^3 * 2^2 bằng bao nhiêu?", "32", "NUMERIC", [], "32"),

    ("Bài 19: Lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Lôgarit cơ số a của b bằng alpha khi a mũ alpha bằng b. Công thức cộng logarit cùng cơ số.",
     r"\log_a b = \alpha \iff a^\alpha = b; \quad \log_a(xy) = \log_a x + \log_a y; \quad \log_a(x^\alpha) = \alpha \log_a x",
     "Điều kiện: Cơ số a dương khác 1, biểu thức trong logarit b > 0.",
     "Giá trị của log_2(16) bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 20: Hàm số mũ và hàm số lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Hàm mũ y = a^x và logarit y = log_a x đồng biến khi a > 1, nghịch biến khi 0 < a < 1.",
     r"y = a^x; \quad y = \log_a x; \quad a > 1: \text{Đồng biến}; \quad 0 < a < 1: \text{Nghịch biến}",
     "Đồ thị hàm mũ tiệm cận ngang Ox; đồ thị hàm logarit tiệm cận đứng Oy.",
     "Hàm số y = (0.5)^x đồng biến hay nghịch biến trên R? (1: Nghịch biến, 0: Đồng biến)", "1", "NUMERIC", [], "1"),

    ("Bài 21: Phương trình, bất phương trình mũ và lôgarit", "Chương VI: Hàm số mũ và hàm số lôgarit",
     "Phương pháp đưa về cùng cơ số. Đổi chiều bất phương trình khi cơ số 0 < a < 1.",
     r"a^{f(x)} = a^{g(x)} \iff f(x) = g(x); \quad \log_a f(x) < \log_a g(x) \iff f(x) < g(x) \ (a > 1)",
     "Luôn đặt điều kiện xác định f(x) > 0 trước khi giải bất phương trình logarit.",
     "Nghiệm của phương trình 2^(x - 1) = 8 là x bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 22: Hai đường thẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian",
     "Góc giữa hai đường thẳng từ 0 đến 90 độ. Vuông góc khi góc bằng 90 độ.",
     r"0^\circ \le \widehat{(a, b)} \le 90^\circ; \quad a \perp b \iff \vec{u}_a \cdot \vec{u}_b = 0",
     "Hai đường thẳng chéo nhau vẫn có thể vuông góc nhau.",
     "Góc giữa hai đường thẳng trong không gian có thể bằng 120 độ không? (1: Có, 0: Không)", "0", "NUMERIC", [], "0"),

    ("Bài 23: Đường thẳng vuông góc với mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian",
     "d vuông góc (P) khi d vuông góc 2 đường thẳng cắt nhau trong (P). Khi đó d vuông góc mọi đường trong (P).",
     r"\begin{cases} d \perp a, \ d \perp b \subset (P) \\ a \cap b = I \end{cases} \Rightarrow d \perp (P); \quad d \perp (P) \Rightarrow d \perp c, \ \forall c \subset (P)",
     "Định lý ba đường vuông góc liên hệ giữa đường thẳng, đường xiên và hình chiếu.",
     "SA vuông góc mặt đáy (ABC). Đường thẳng SA có vuông góc với cạnh BC không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),

    ("Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng", "Chương VII: Quan hệ vuông góc trong không gian",
     "Góc giữa đường thẳng d và mặt phẳng (P) là góc giữa d và hình chiếu d' của nó.",
     r"\varphi = \widehat{(d, (P))} = \widehat{(d, d')}; \quad \tan\varphi = \frac{SH}{AH}",
     "Tìm chân đường vuông góc H hạ từ đỉnh S xuống mặt phẳng.",
     "Cho hình chóp S.ABC có SA vuông góc đáy và SA = AB = a. Góc giữa SB và đáy bằng bao nhiêu độ?", "45", "NUMERIC", [], "45"),

    ("Bài 25: Hai mặt phẳng vuông góc", "Chương VII: Quan hệ vuông góc trong không gian",
     "Hai mặt phẳng vuông góc khi mặt này chứa đường thẳng vuông góc mặt kia.",
     r"d \perp (Q), \ d \subset (P) \Rightarrow (P) \perp (Q); \quad (P) \perp (Q) \Rightarrow a \perp (Q) \ (a \subset (P), a \perp \Delta)",
     "Đường thẳng trong mặt này vuông góc giao tuyến thì vuông góc mặt kia.",
     "Hình chóp có SA vuông góc đáy thì mặt phẳng (SAB) có vuông góc đáy không? (1: Có, 0: Không)", "1", "NUMERIC", [], "1"),

    ("Bài 26: Khoảng cách trong không gian", "Chương VII: Quan hệ vuông góc trong không gian",
     "Khoảng cách từ điểm đến mặt phẳng, khoảng cách giữa hai đường thẳng chéo nhau.",
     r"d(M, (P)) = MH \ (MH \perp (P)); \quad d(a, b) = d(a, (P)) \ (b \subset (P), a \parallel (P))",
     "Kỹ thuật đổi điểm: Chuyển khoảng cách từ điểm M về chân đường cao A để tính.",
     "Hình chóp S.ABC có SA vuông góc đáy và SA = 5. Khoảng cách từ đỉnh S đến đáy bằng:", "5", "NUMERIC", [], "5"),

    ("Bài 27: Thể tích", "Chương VII: Quan hệ vuông góc trong không gian",
     "Thể tích lăng trụ V = B*h. Thể tích chóp V = (1/3)*B*h. Tỉ số thể tích Simson cho chóp tam giác.",
     r"V_{\text{lăng trụ}} = S_{\text{đáy}} \cdot h; \quad V_{\text{chóp}} = \frac{1}{3} S_{\text{đáy}} \cdot h",
     "Công thức tỉ số thể tích Simson chỉ áp dụng duy nhất cho hình chóp tam giác.",
     "Khối chóp có diện tích đáy bằng 9 và chiều cao bằng 4. Thể tích khối chóp bằng:", "12", "NUMERIC", [], "12"),

    ("Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất",
     "Biến cố hợp xảy ra khi ít nhất 1 biến cố xảy ra. Biến cố giao xảy ra khi cả 2 cùng xảy ra. Độc lập khi xác suất không ảnh hưởng nhau.",
     r"A \cup B; \quad A \cap B = AB; \quad P(AB) = P(A) \cdot P(B) \ (\text{Độc lập})",
     "Phân biệt độc lập và xung khắc (xung khắc thì giao bằng rỗng, P(AB) = 0).",
     "Hai biến cố A và B xung khắc thì xác suất biến cố giao P(AB) bằng bao nhiêu?", "0", "NUMERIC", [], "0"),

    ("Bài 29: Công thức cộng xác suất", "Chương VIII: Các quy tắc tính xác suất",
     "Công thức cộng cho hai biến cố bất kỳ P(A hợp B) = P(A) + P(B) - P(AB). Khi xung khắc trừ 0.",
     r"P(A \cup B) = P(A) + P(B) - P(AB); \quad A, B \text{ xung khắc} \Rightarrow P(A \cup B) = P(A) + P(B)",
     "Nhớ trừ phần giao P(AB) nếu hai biến cố không xung khắc.",
     "Cho hai biến cố xung khắc A và B có P(A) = 0.3 và P(B) = 0.4. Xác suất P(A hợp B) bằng:", "0.7", "NUMERIC", [], "0.7"),

    ("Bài 30: Công thức nhân xác suất cho hai biến cố độc lập", "Chương VIII: Các quy tắc tính xác suất",
     "Xác suất của biến cố giao của 2 biến cố độc lập bằng tích xác suất từng biến cố.",
     r"P(AB) = P(A) \cdot P(B); \quad P(A \overline{B}) = P(A) \cdot [1 - P(B)]",
     "Xác suất ít nhất một người bắn trúng P = 1 - P(cả hai cùng trượt).",
     "Hai xạ thủ bắn độc lập với xác suất trúng là 0.6 và 0.7. Xác suất cả hai cùng trúng bằng:", "0.42", "NUMERIC", [], "0.42"),

    ("Bài 31: Định nghĩa và ý nghĩa của đạo hàm", "Chương IX: Đạo hàm",
     "Đạo hàm là giới hạn của tỉ số số gia hàm số trên số gia đối số. Hệ số góc tiếp tuyến k = f'(x0).",
     r"f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}; \quad y - y_0 = f'(x_0)(x - x_0)",
     "Phương trình tiếp tuyến tại M(x0; y0): y = f'(x0)(x - x0) + y0.",
     "Tiếp tuyến của hàm số y = x^2 tại điểm x0 = 2 có hệ số góc k bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 32: Các quy tắc tính đạo hàm", "Chương IX: Đạo hàm",
     "Đạo hàm tổng, hiệu, tích, thương và đạo hàm hàm hợp [f(u)]' = f'(u) * u'.",
     r"(uv)' = u'v + uv'; \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}; \quad [f(u)]' = f'(u) \cdot u'",
     "Luôn nhân thêm u' ở cuối khi tính đạo hàm hàm hợp.",
     "Tính giá trị đạo hàm của hàm số f(x) = x^3 - 3x tại điểm x = 2:", "9", "NUMERIC", [], "9"),

    ("Bài 33: Đạo hàm cấp hai", "Chương IX: Đạo hàm",
     "Đạo hàm cấp hai y'' = (y')'. Ý nghĩa cơ học: Gia tốc tức thời a(t) = s''(t).",
     r"y'' = (y')'; \quad v(t) = s'(t); \quad a(t) = v'(t) = s''(t)",
     "Đạo hàm cấp hai còn dùng để tìm điểm uốn và xét tính lồi lõm của đồ thị.",
     "Vật chuyển động theo s(t) = t^3 (mét). Gia tốc tức thời a(t) tại t = 2 giây bằng bao nhiêu m/s^2?", "12", "NUMERIC", [], "12")
]

RAW_DATA_12 = [
    ("Bài 1: Tính đơn điệu và cực trị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Đồng biến khi f'(x) >= 0; nghịch biến khi f'(x) <= 0. Điểm cực đại đổi dấu từ dương sang âm, cực tiểu từ âm sang dương.",
     r"f'(x) \ge 0, \ \forall x \in K \ (\text{Đồng biến}); \quad f'(x_0) = 0 \text{ đổi dấu } (+) \to (-) \ (\text{Cực đại}); \quad (-) \to (+) \ (\text{Cực tiểu})",
     "Phân biệt 'Điểm cực trị của hàm số' là x0 và 'Giá trị cực trị' là y0 = f(x0).",
     "Cho hàm số y = x^3 - 3x + 2. Giá trị cực tiểu (yCT) của hàm số bằng bao nhiêu?", "0", "NUMERIC", [], "0"),

    ("Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Tìm GTLN, GTNN trên đoạn [a; b] bằng cách so sánh giá trị tại hai đầu mút và các điểm làm f'(x) = 0.",
     r"\max_{[a; b]} f(x) = \max\{f(a), f(b), f(x_i)\}; \quad \min_{[a; b]} f(x) = \min\{f(a), f(b), f(x_i)\}",
     "Nếu khảo sát trên khoảng, bắt buộc phải lập bảng biến thiên hoàn chỉnh.",
     "Giá trị lớn nhất của hàm số f(x) = x^3 - 3x + 1 trên đoạn [0; 2] bằng bao nhiêu?", "3", "NUMERIC", [], "3"),

    ("Bài 3: Đường tiệm cận của đồ thị hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Tiệm cận đứng x = x0 (mẫu triệt tiêu, tử khác 0). Tiệm cận ngang y = y0 khi x dần tới vô cực.",
     r"\lim_{x \to x_0^+} f(x) = \pm\infty \Rightarrow x = x_0 \ (\text{TCĐ}); \quad \lim_{x \to \pm\infty} f(x) = y_0 \Rightarrow y = y_0 \ (\text{TCN}); \quad y = \frac{ax+b}{cx+d} \Rightarrow y = \frac{a}{c}, \ x = -\frac{d}{c}",
     "Giao điểm hai đường tiệm cận là tâm đối xứng của đồ thị hàm nhất biến.",
     "Đường tiệm cận ngang của đồ thị hàm số y = (2x - 3)/(x + 1) có phương trình y bằng:", "2", "NUMERIC", [], "2"),

    ("Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Quy trình khảo sát: TXĐ -> Chiều biến thiên, cực trị, tiệm cận -> Bảng biến thiên -> Vẽ đồ thị.",
     r"y = ax^3 + bx^2 + cx + d; \quad y = \frac{ax+b}{cx+d}; \quad y = \frac{ax^2+bx+c}{px+q} \ (\text{Tiệm cận xiên})",
     "Đồ thị hàm bậc ba nhận điểm uốn I (nghiệm y'' = 0) làm tâm đối xứng.",
     "Đồ thị hàm số y = (2x - 3)/(x + 1) có tâm đối xứng I. Hoành độ xI bằng bao nhiêu?", "-1", "NUMERIC", [], "-1"),

    ("Bài 5: Ứng dụng đạo hàm giải quyết bài toán thực tiễn", "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
     "Lập hàm số mục tiêu theo một biến x. Tìm cực trị thực tế bằng cách giải phương trình đạo hàm f'(x) = 0.",
     r"V(x) \to \max \iff V'(x) = 0; \quad C(x) \to \min \iff C'(x) = 0; \quad S(x) = x^2 + \frac{128}{x}",
     "Đối chiếu nghiệm với điều kiện độ dài, số lượng sản phẩm phải dương.",
     "Người ta làm chiếc hộp không nắp đáy vuông thể tích 32 dm^3. Diện tích vật liệu nhỏ nhất bằng (dm^2):", "48", "NUMERIC", [], "48"),

    ("Bài 6: Vectơ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Quy tắc hình hộp: AC' = AB + AD + AA'. Định lý ba vectơ đồng phẳng.",
     r"\vec{AC'} = \vec{AB} + \vec{AD} + \vec{AA'}; \quad \vec{c} = m\vec{a} + n\vec{b} \iff \vec{a}, \vec{b}, \vec{c} \text{ đồng phẳng}",
     "Tích vô hướng trong không gian bằng tích độ dài nhân cosin góc xen giữa.",
     "Cho hình hộp ABCD.A'B'C'D'. Vectơ AB + AD + AA' bằng vectơ nào? (A: AC', B: BD')", "A", "CHOICE", ["A. Vectơ AC'", "B. Vectơ BD'"], "A"),

    ("Bài 7: Hệ trục tọa độ trong không gian", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Hệ trục Oxyz gồm 3 trục Ox, Oy, Oz vuông góc. Tọa độ điểm M(x; y; z) và hình chiếu vuông góc.",
     r"\vec{OM} = x\vec{i} + y\vec{j} + z\vec{k} \iff M(x; y; z); \quad \vec{i}^2 = \vec{j}^2 = \vec{k}^2 = 1; \quad \vec{i}\cdot\vec{j} = \vec{j}\cdot\vec{k} = \vec{k}\cdot\vec{i} = 0",
     "Hình chiếu vuông góc của M(x; y; z) lên trục Oz giữ nguyên z và cho x = y = 0.",
     "Hình chiếu vuông góc của điểm M(2; -3; 4) lên trục Oz có cao độ z bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 8: Biểu thức tọa độ của các phép toán vectơ", "Chương II: Vectơ và hệ tọa độ trong không gian",
     "Tích vô hướng x1x2 + y1y2 + z1z2. Độ dài vectơ bằng căn bậc hai tổng bình phương các tọa độ.",
     r"\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2; \quad |\vec{u}| = \sqrt{x^2 + y^2 + z^2}; \quad AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}",
     "Hai vectơ vuông góc khi và chỉ khi tích vô hướng bằng 0.",
     "Độ dài của vectơ a = (2; -3; 6) bằng bao nhiêu?", "7", "NUMERIC", [], "7"),

    ("Bài 9: Khoảng biến thiên và khoảng tứ phân vị", "Chương III: Các số đặc trưng đo mức độ phân tán",
     "Khoảng biến thiên R bằng đầu mút phải nhóm cuối trừ đầu mút trái nhóm đầu. Khoảng tứ phân vị delta Q = Q3 - Q1.",
     r"R = a_{k+1} - a_1; \quad \Delta_Q = Q_3 - Q_1; \quad Q_r = u_m + \frac{\frac{r \cdot n}{4} - C}{n_m}(u_{m+1} - u_m)",
     "Khoảng tứ phân vị ít bị ảnh hưởng bởi giá trị bất thường hơn khoảng biến thiên.",
     "Nếu mẫu ghép nhóm có Q1 = 12 và Q3 = 15.5 thì khoảng tứ phân vị delta Q bằng:", "3.5", "NUMERIC", [], "3.5"),

    ("Bài 10: Phương sai và độ lệch chuẩn", "Chương III: Các số đặc trưng đo mức độ phân tán",
     "Phương sai s^2 đo độ phân tán quanh số trung bình. Độ lệch chuẩn s bằng căn bậc hai của phương sai.",
     r"s^2 = \frac{1}{n} \sum n_i c_i^2 - (\overline{x})^2; \quad s = \sqrt{s^2}",
     "Độ lệch chuẩn càng nhỏ chứng tỏ số liệu càng tập trung đều quanh số trung bình.",
     "Nếu phương sai của mẫu số liệu ghép nhóm bằng 16 thì độ lệch chuẩn s bằng bao nhiêu?", "4", "NUMERIC", [], "4"),

    ("Bài 11: Nguyên hàm", "Chương IV: Nguyên hàm và tích phân",
     "Hàm F(x) là nguyên hàm của f(x) khi F'(x) = f(x). Bảng nguyên hàm cơ bản.",
     r"\int x^\alpha dx = \frac{x^{\alpha+1}}{\alpha+1} + C \ (\alpha \neq -1); \quad \int \frac{1}{x} dx = \ln|x| + C; \quad \int e^x dx = e^x + C; \quad \int \cos x dx = \sin x + C",
     "Không được quên hằng số tích phân C và dấu giá trị tuyệt đối của ln|x|.",
     "Một nguyên hàm của f(x) = 2x là F(x) = x^2. Tính hiệu số F(2) - F(0):", "4", "NUMERIC", [], "4"),

    ("Bài 12: Tích phân", "Chương IV: Nguyên hàm và tích phân",
     "Định lý Newton-Leibniz: Tích phân từ a đến b của f(x)dx bằng F(b) - F(a). Tích phân từng phần.",
     r"\int_a^b f(x)dx = F(b) - F(a) = F(x)\Big|_a^b; \quad \int_a^b u \, dv = uv\Big|_a^b - \int_a^b v \, du",
     "Thứ tự ưu tiên đặt u trong từng phần: Nhất lô, nhì đa, tam lượng, tứ mũ.",
     "Tính tích phân I = tích phân từ 0 đến 2 của (2x + 1)dx:", "6", "NUMERIC", [], "6"),

    ("Bài 13: Ứng dụng hình học của tích phân", "Chương IV: Nguyên hàm và tích phân",
     "Diện tích hình phẳng giới hạn bởi đồ thị và trục hoành. Thể tích khối tròn xoay quanh trục Ox.",
     r"S = \int_a^b |f(x)| dx; \quad S = \int_a^b |f(x) - g(x)| dx; \quad V_x = \pi \int_a^b [f(x)]^2 dx",
     "Công thức thể tích tròn xoay luôn có nhân tử số pi ở phía trước tích phân.",
     "Diện tích hình phẳng giới hạn bởi y = x^2 - 4x và trục Ox bằng bao nhiêu? (Dạng a/b):", "32/3", "NUMERIC", ["10.67", "32/3"], "32/3"),

    ("Bài 14: Phương trình mặt phẳng", "Chương V: Phương pháp tọa độ trong không gian",
     "Mặt phẳng qua M(x0; y0; z0) có VTPT n(A; B; C) có phương trình A(x - x0) + B(y - y0) + C(z - z0) = 0.",
     r"Ax + By + Cz + D = 0 \ (A^2 + B^2 + C^2 > 0); \quad d(M, (P)) = \frac{|Ax_M + By_M + Cz_M + D|}{\sqrt{A^2 + B^2 + C^2}}",
     "Vectơ pháp tuyến n của mặt phẳng qua 2 vectơ u, v là tích có hướng n = [u, v].",
     "Tính khoảng cách từ gốc tọa độ O(0; 0; 0) đến mặt phẳng 2x - 2y + z - 9 = 0:", "3", "NUMERIC", [], "3"),

    ("Bài 15: Phương trình đường thẳng trong không gian", "Chương V: Phương pháp tọa độ trong không gian",
     "Đường thẳng qua M(x0; y0; z0) có VTCP u(a; b; c) có phương trình tham số và chính tắc.",
     r"\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}; \quad \frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}",
     "Để chuyển sang chính tắc, rút tham số t từ từng phương trình tọa độ rồi cho bằng nhau.",
     "Đường thẳng (x - 1)/2 = (y + 2)/(-1) = (z - 3)/1 đi qua điểm M(1; -2; z0). z0 bằng:", "3", "NUMERIC", [], "3"),

    ("Bài 16: Công thức tính góc trong không gian", "Chương V: Phương pháp tọa độ trong không gian",
     "Cosin góc giữa hai mặt phẳng (qua 2 VTPT). Sin góc giữa đường thẳng và mặt phẳng (qua VTCP và VTPT).",
     r"\cos((P), (Q)) = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}; \quad \sin(d, (P)) = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}||\vec{n}|}",
     "Góc giữa đường thẳng và mặt phẳng dùng hàm sin, góc giữa hai mặt phẳng dùng hàm cosin.",
     "Hai mặt phẳng có VTPT n1 = (1; 0; 0) và n2 = (0; 1; 0) tạo với nhau một góc bằng (độ):", "90", "NUMERIC", [], "90"),

    ("Bài 17: Phương trình mặt cầu", "Chương V: Phương pháp tọa độ trong không gian",
     "Mặt cầu tâm I(a; b; c) bán kính R có phương trình chính tắc (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2.",
     r"(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2; \quad R = \sqrt{a^2 + b^2 + c^2 - d}",
     "Nếu khoảng cách từ tâm I đến mặt phẳng (P) bằng R thì mặt phẳng tiếp xúc mặt cầu.",
     "Bán kính của mặt cầu (x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 25 bằng bao nhiêu?", "5", "NUMERIC", [], "5"),

    ("Bài 18: Xác suất có điều kiện", "Chương VI: Xác suất có điều kiện",
     "Xác suất của biến cố A khi biết biến cố B đã xảy ra P(A|B) = P(AB) / P(B).",
     r"P(A|B) = \frac{P(AB)}{P(B)}; \quad P(AB) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)",
     "A và B độc lập khi và chỉ khi P(A|B) = P(A).",
     "Cho P(AB) = 0.2 và P(B) = 0.5. Tính xác suất có điều kiện P(A|B):", "0.4", "NUMERIC", [], "0.4"),

    ("Bài 19: Công thức xác suất toàn phần và công thức Bayes", "Chương VI: Xác suất có điều kiện",
     "Hệ biến cố đầy đủ. Công thức xác suất toàn phần và công thức Bayes tính xác suất hậu nghiệm.",
     r"P(A) = \sum_{i=1}^n P(B_i)P(A|B_i); \quad P(B_k|A) = \frac{P(B_k)P(A|B_k)}{P(A)} = \frac{P(B_k)P(A|B_k)}{\sum P(B_i)P(A|B_i)}",
     "Công thức Bayes dùng để cập nhật xác suất của nguyên nhân Bk khi biến cố A đã xảy ra.",
     "Cho hệ đầy đủ B1, B2 có P(B1) = 0.4, P(B2) = 0.6; P(A|B1) = 0.5, P(A|B2) = 0.2. Tính P(A):", "0.32", "NUMERIC", [], "0.32")
]

def build_curriculum_dict(raw_list):
    res = {}
    for idx, item in enumerate(raw_list):
        title, chap, concept, formula, trap, content, target, ans_type, opts, def_ans = item
        
        # Ghi chú nhanh với công thức LaTeX chuẩn $$...$$
        smart_notes_md = f"""
#### 1. Định nghĩa & Khái niệm cốt lõi
{concept}

#### 2. Công thức Toán học trọng tâm
$${formula}$$

#### 3. Phương pháp tư duy & Cảnh báo bẫy sai lầm
- ⚠️ **Lưu ý bẫy đề thi:** {trap}
"""

        # Cấu trúc các bước minh họa tương tác từng bước
        example_data = {
            "title": f"Ví dụ minh họa mẫu: {title}",
            "problem": f"**Bài toán mẫu (Trích Vở tự học):** Vận dụng kiến thức cốt lõi của *{title}* để giải quyết trọn vẹn yêu cầu toán học sau:\n\n> {content}",
            "steps": [
                {
                    "name": "Bước 1: Phân tích giả thiết & Xác định công thức / định lý áp dụng",
                    "content": f"""
- Đọc kỹ dữ kiện đề bài, xác định rõ đại lượng đã biết và đại lượng cần tìm.
- Nhắc lại định lý / công thức toán học nền tảng:
$${formula}$$
- *Ý nghĩa sư phạm:* Nhận diện đúng dạng bài giúp học sinh định hình con đường giải ngắn nhất, tránh sa đà vào các phép tính không cần thiết.
"""
                },
                {
                    "name": "Bước 2: Thiết lập phương trình & Biến đổi đại số / hình học trung gian",
                    "content": f"""
- Thay thế các số liệu đề bài vào hệ thức lý thuyết.
- Thực hiện các bước biến đổi trung gian tường minh:
$${formula}$$
- Trình bày mạch lạc từng dòng, giải thích rõ căn cứ suy luận để rèn luyện phương pháp viết bài thi chuẩn mực.
"""
                },
                {
                    "name": "Bước 3: Rà soát điều kiện xác định, kiểm tra bẫy sai lầm & Kết luận",
                    "content": f"""
- ⚠️ **Cảnh báo bẫy sai lầm thường gặp:** {trap}
- So sánh kết quả trung gian với điều kiện xác định của bài toán.
- **Đáp số chính xác cuối cùng:**
$$\\mathbf{{{target}}}$$
- Ghi câu kết luận hoàn chỉnh, nêu đúng đơn vị toán học.
"""
                }
            ]
        }

        res[title] = {
            "chapter": chap,
            "video_title": f"Bài giảng vi mô: {title}",
            "video_url": "https://www.youtube.com/watch?v=kYJ_t120-Jk",
            "audio_script": f"Chào em! Trong bài học {title}, em hãy lưu ý: {concept}. {trap}",
            "has_3d": True if ("không gian" in title or "Oxyz" in title or "Vectơ" in title or "mặt phẳng" in title or "mặt cầu" in title) else False,
            "smart_notes": smart_notes_md,
            "example": example_data,
            "exercise": {
                "id": f"EX_{idx+1}",
                "title": f"Bài tập tự luyện kiểm minh chứng - {title}",
                "content": content,
                "question_type": ans_type,
                "options": opts,
                "target_val": target,
                "hint_1": f"Áp dụng định lý: {concept}",
                "hint_2": f"Công thức then chốt: $${formula}$$",
                "hint_3": f"Đáp số chính xác cần đạt là: {target}",
                "solution_text": f"Dựa trên kiến thức: {concept}. Áp dụng công thức suy ra kết quả chính xác: {target}."
            }
        }
    return res

CURRICULUM_DATA = {
    "Khối 10": build_curriculum_dict(RAW_DATA_10),
    "Khối 11": build_curriculum_dict(RAW_DATA_11),
    "Khối 12": build_curriculum_dict(RAW_DATA_12)
}

# ==============================================================================
# 4. KHO ĐỀ KHẢO THÍ CHUẨN MA TRẬN MỚI CỦA BỘ GD&ĐT
# ==============================================================================
EXAM_BANK = {
    "Khối 10": {
        "Giữa học kỳ 1": {
            "title": "ĐỀ KHẢO THÍ GIỮA HỌC KỲ 1 - TOÁN 10",
            "p1": [{"q": r"Mệnh đề nào sau đây là mệnh đề toán học?", "ops": ["A. $2 + 3 = 6$", "B. Thời tiết hôm nay mát quá!", "C. Bạn học bài chưa?", "D. Hãy giải phương trình."], "ans": "A", "exp": "A là khẳng định sai, là mệnh đề toán học."}],
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
# 9. PHÂN HỆ HỌC SINH (5 TABS TOÀN DIỆN VỚI TAB VÍ DỤ MINH HỌA MỚI)
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

# KHỞI TẠO 5 TABS THEO ĐÚNG TIẾN TRÌNH SƯ PHẠM
tab1, tab_ex, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Video, Thuyết Minh & 3D)",
    "💡 Ví Dụ Minh Họa (Từng Bước Tương Tác)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC
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

    col_v, col_n = st.columns([1.1, 1.2])
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
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes)**")
            st.markdown(cur_data["smart_notes"])

# ------------------------------------------------------------------------------
# TAB 2: VÍ DỤ MINH HỌA (TỪNG BƯỚC TƯƠNG TÁC THEO NHẤP CHUỘT / PHÍM TỚI)
# ------------------------------------------------------------------------------
with tab_ex:
    ex_model = cur_data["example"]
    st.subheader(f"💡 {ex_model['title']}")
    st.caption("Quan sát cách trình bày bài giải mẫu chuẩn mực từng bước trước khi bắt tay làm bài tập tự luyện.")

    with st.container(border=True):
        st.markdown(ex_model["problem"])

    # Quản lý số bước đã hiển thị thông qua session_state
    lesson_hash_ex = hashlib.md5(sel_lesson.encode('utf-8')).hexdigest()[:8]
    step_key = f"step_ex_{lesson_hash_ex}"
    total_steps = len(ex_model["steps"])
    
    if step_key not in st.session_state:
        st.session_state[step_key] = 1

    # Thanh điều khiển bước tương tác
    c_btn1, c_slider, c_btn2, c_btn3 = st.columns([1, 2.2, 1, 1])
    with c_btn1:
        if st.button("⬅️ Bước trước", key=f"prev_{step_key}", use_container_width=True):
            st.session_state[step_key] = max(1, st.session_state[step_key] - 1)
            st.rerun()

    with c_slider:
        # Thanh trượt cho phép học sinh nhấn phím mũi tên Trái/Phải để chuyển bước
        current_step_val = st.select_slider(
            "Tiến trình các bước (bấm mũi tên phím để tới/lùi):",
            options=list(range(1, total_steps + 1)),
            value=st.session_state[step_key],
            key=f"slider_{step_key}"
        )
        if current_step_val != st.session_state[step_key]:
            st.session_state[step_key] = current_step_val
            st.rerun()

    with c_btn2:
        if st.button("Bước tiếp theo ➡️", key=f"next_{step_key}", use_container_width=True):
            st.session_state[step_key] = min(total_steps, st.session_state[step_key] + 1)
            st.rerun()

    with c_btn3:
        if st.button("🔄 Xem lại từ đầu", key=f"reset_{step_key}", use_container_width=True):
            st.session_state[step_key] = 1
            st.rerun()

    st.progress(st.session_state[step_key] / total_steps)
    st.markdown(f"**Đang hiển thị:** *Bước {st.session_state[step_key]} / {total_steps}*")

    # Hiển thị từng bước tích lũy từ bước 1 đến bước hiện tại
    for i in range(st.session_state[step_key]):
        step_obj = ex_model["steps"][i]
        is_latest = (i == st.session_state[step_key] - 1)
        
        box_class = "step-box-active" if is_latest else "step-box-done"
        badge = "📍 Đang giải thích" if is_latest else "✅ Đã tìm hiểu"
        
        with st.container(border=True):
            st.markdown(f"##### {step_obj['name']} `({badge})`")
            st.markdown(step_obj["content"])

    if st.session_state[step_key] == total_steps:
        st.success("🎉 **Tuyệt vời! Em đã hoàn thành việc quan sát và phân tích toàn bộ ví dụ mẫu.** Hãy chuyển sang tab **'📝 Học Sinh Tự Giải'** ngay bên cạnh để vận dụng phương pháp này nhé!")

# ------------------------------------------------------------------------------
# TAB 3: HỌC SINH TỰ GIẢI - KIỂM MINH CHỨNG MỚI ĐƯỢC THƯỞNG HOA
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
# TAB 4: TRỢ LÝ AI: SOI BÀI VỞ & TỐI ƯU ÂM THANH MIC/LOA
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
