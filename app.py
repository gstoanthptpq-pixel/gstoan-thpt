import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google import genai
import pandas as pd
from PIL import Image
from gtts import gTTS
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# ==============================================================================
# 1. CẤU HÌNH GIAO DIỆN & STYLE CHUẨN SƯ PHẠM
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
        margin-bottom: 12px !important;
    }
    .stButton>button {
        border-radius: 10px;
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        color: white;
        font-weight: 600;
        border: none;
        padding: 8px 18px;
        transition: all 0.25s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35);
    }
    .metric-card {
        background: white;
        padding: 12px 16px;
        border-radius: 12px;
        border-left: 5px solid #EC4899;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. HẠ TẦNG KẾT NỐI GEMINI API & GOOGLE SHEETS DỰ PHÒNG CHỐNG SẬP
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

# ==============================================================================
# 3. KHO HỌC LIỆU SỐ BÁM SÁT SGK KẾT NỐI TRI THỨC (KHỐI 10, 11, 12)
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 10": {
        "Bài 1: Mệnh đề toán học và Tập hợp": {
            "chapter": "Chương I: Mệnh đề và Tập hợp",
            "video_title": "Video 90s: Bản chất Mệnh đề & Phủ định mệnh đề chứa với mọi, tồn tại",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Mệnh đề:** Một khẳng định đúng hoặc sai. Không thể vừa đúng vừa sai.
- **Phủ định:** Phủ định của $\forall x \in X, P(x)$ là $\exists x \in X, \overline{P(x)}$. Phủ định của $\exists x \in X, P(x)$ là $\forall x \in X, \overline{P(x)}$.
- **Tập hợp con & Giao/Hợp:** 
  $A \cap B = \{x \mid x \in A \text{ và } x \in B\}$; $A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}$.
- ⚠️ *Bẫy kinh điển:* Khi lấy phủ định, quên đổi chiều bất đẳng thức (ví dụ: phủ định của $>$ là $\le$).
            """,
            "exercise": {
                "id": "SGK_10_1.1",
                "title": "Bài tập 1.3 (Trang 11 - SGK Toán 10 KNTT)",
                "content": r"Cho mệnh đề $P$: '$\forall x \in \mathbb{R}, x^2 + 2x + 3 > 0$'. Lập mệnh đề phủ định $\overline{P}$ và xét tính đúng sai của nó.",
                "hint_1": "Áp dụng quy tắc phủ định mệnh đề với lượng từ $\forall$: phủ định của '$\forall x \in X, P(x)$' là '$\exists x \in X, \overline{P(x)}$'.",
                "hint_2": "Phủ định của dấu lớn hơn ($>$) là dấu nhỏ hơn hoặc bằng ($\le$). Hãy viết lại biểu thức.",
                "hint_3": "Biến đổi tam thức bậc hai: $x^2 + 2x + 3 = (x+1)^2 + 2 \ge 2 > 0$ với mọi $x \in \mathbb{R}$. Từ đó suy ra tính đúng sai của $\overline{P}$.",
                "similar_prompt": "Tạo 1 bài toán tương tự xét tính đúng sai và phủ định mệnh đề chứa tam thức bậc hai cho lớp 10, chỉ xuất đề bài."
            }
        },
        "Bài 2: Bất phương trình và Hệ BPT bậc nhất hai ẩn": {
            "chapter": "Chương II: Bất phương trình bậc nhất hai ẩn",
            "video_title": "Video 110s: Kỹ thuật biểu diễn miền nghiệm và bài toán tối ưu thực tế",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- Dạng tổng quát: $ax + by \le c$ (hoặc $<, >, \ge$).
- **Quy tắc xác định miền nghiệm:**
  1. Vẽ đường thẳng bờ $d: ax + by = c$.
  2. Chọn điểm thử $O(0;0)$ (nếu $O \notin d$) kiểm tra tính thỏa mãn.
  3. Gạch bỏ miền không thỏa mãn.
- **Tối ưu hóa $F(x; y) = ax + by$:** Giá trị lớn nhất/nhỏ nhất luôn đạt tại các đỉnh của đa giác miền nghiệm.
            """,
            "exercise": {
                "id": "SGK_10_2.1",
                "title": "Bài tập 2.2 (Trang 28 - SGK Toán 10 KNTT)",
                "content": r"Biểu diễn miền nghiệm của hệ bất phương trình: $\begin{cases} x + y \le 4 \\ 2x - y \ge 1 \\ x \ge 0 \end{cases}$.",
                "hint_1": "Vẽ lần lượt ba đường thẳng $d_1: x + y = 4$, $d_2: 2x - y = 1$ và trục tung $x = 0$.",
                "hint_2": "Lấy điểm thử $M(1; 1)$, kiểm tra xem $M$ có thỏa mãn đồng thời cả 3 bất phương trình hay không.",
                "hint_3": "Miền nghiệm là phần mặt phẳng chứa điểm $M$ giới hạn bởi tam giác tạo bởi 3 giao điểm của các đường thẳng.",
                "similar_prompt": "Tạo 1 bài toán tương tự về tìm miền nghiệm hệ BPT bậc nhất hai ẩn lớp 10 có 3 ràng buộc."
            }
        },
        "Bài 3: Hệ thức lượng trong tam giác và Vectơ": {
            "chapter": "Chương IV: Hệ thức lượng trong tam giác",
            "video_title": "Video 120s: Định lý Côsin, Sin và Công thức tính diện tích nhanh",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Định lý Côsin:** $a^2 = b^2 + c^2 - 2bc \cos A$.
- **Định lý Sin:** $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$.
- **Công thức diện tích tam giác:** $S = \frac{1}{2}ab \sin C = \frac{abc}{4R} = pr = \sqrt{p(p-a)(p-b)(p-c)}$.
- ⚠️ *Mẹo nhận diện:* Biết 2 cạnh và góc xen giữa $\rightarrow$ dùng định lý Côsin. Biết 1 cạnh và 2 góc kề $\rightarrow$ dùng định lý Sin.
            """,
            "exercise": {
                "id": "SGK_10_3.1",
                "title": "Bài tập 3.4 (Trang 56 - SGK Toán 10 KNTT)",
                "content": r"Cho tam giác $ABC$ có $b = 8$, $c = 5$ và góc $\widehat{A} = 60^\circ$. Tính cạnh $a$ và bán kính đường tròn ngoại tiếp $R$.",
                "hint_1": "Biết hai cạnh $b, c$ và góc xen giữa $A$, hãy dùng định lý Côsin: $a^2 = b^2 + c^2 - 2bc\cos A$.",
                "hint_2": "Tính được $a^2 = 8^2 + 5^2 - 2 \cdot 8 \cdot 5 \cdot \cos 60^\circ = 49 \Rightarrow a = 7$.",
                "hint_3": "Sử dụng định lý Sin: $2R = \frac{a}{\sin A} \Rightarrow R = \frac{a}{2\sin A} = \frac{7}{2\sin 60^\circ}$.",
                "similar_prompt": "Tạo 1 bài tập tam giác tương tự cho lớp 10, thay đổi số liệu cạnh và góc xen giữa."
            }
        }
    },
    "Khối 11": {
        "Bài 1: Giá trị lượng giác của góc lượng giác": {
            "chapter": "Chương I: Hàm số lượng giác và Phương trình lượng giác",
            "video_title": "Video 110s: Vòng tròn lượng giác & Dấu các góc phần tư",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Hệ thức cơ bản:**
  $\sin^2(x) + \cos^2(x) = 1, \quad 1 + \tan^2(x) = \frac{1}{\cos^2(x)} \quad \left(x \neq \frac{\pi}{2} + k\pi\right)$
- **Bảng xét dấu theo góc phần tư:**
  - Góc I ($0 < \alpha < \frac{\pi}{2}$): $\sin > 0, \cos > 0, \tan > 0$.
  - Góc II ($\frac{\pi}{2} < \alpha < \pi$): $\sin > 0, \cos < 0, \tan < 0$.
  - Góc III ($\pi < \alpha < \frac{3\pi}{2}$): $\sin < 0, \cos < 0, \tan > 0$.
  - Góc IV ($\frac{3\pi}{2} < \alpha < 2\pi$): $\sin < 0, \cos > 0, \tan < 0$.
            """,
            "exercise": {
                "id": "SGK_11_1.1",
                "title": "Bài tập 1.1 (Trang 15 - SGK Toán 11 KNTT)",
                "content": r"Cho góc $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$ và $\sin(\alpha) = \frac{3}{5}$. Hãy tính $\cos(\alpha)$ và $\tan(\alpha)$.",
                "hint_1": "Áp dụng công thức $\sin^2\alpha + \cos^2\alpha = 1 \Rightarrow \cos^2\alpha = 1 - \sin^2\alpha$.",
                "hint_2": "Vì góc $\alpha$ thuộc góc phần tư thứ II ($\frac{\pi}{2} < \alpha < \pi$), nên giá trị $\cos\alpha$ nhận dấu âm.",
                "hint_3": "Sau khi tính được $\cos\alpha = -\frac{4}{5}$, áp dụng $\tan\alpha = \frac{\sin\alpha}{\cos\alpha} = \frac{3/5}{-4/5} = -\frac{3}{4}$.",
                "similar_prompt": "Tạo 1 bài toán lượng giác tương tự tìm cos, tan khi biết sin và khoảng góc phần tư thứ III."
            }
        },
        "Bài 2: Hình chóp và các góc trong không gian": {
            "chapter": "Chương IV: Quan hệ vuông góc trong không gian",
            "video_title": "Video 120s: Phương pháp dựng góc giữa đường thẳng và mặt phẳng",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": True,
            "smart_notes": r"""
- **Quy tắc tìm góc giữa đường thẳng $d$ và mặt phẳng $(P)$:**
  1. Tìm giao điểm $A = d \cap (P)$.
  2. Chọn một điểm $S \in d$ ($S \neq A$), dựng hình chiếu vuông góc $H$ của $S$ lên $(P)$ ($SH \perp (P)$).
  3. Góc giữa $d$ và $(P)$ chính là góc $\widehat{SAH}$.
- ⚠️ *Mẹo tính toán:* Luôn gắn góc vào tam giác vuông $\Delta SAH$ tại $H$, dùng $\tan \widehat{SAH} = \frac{SH}{AH}$.
            """,
            "exercise": {
                "id": "SGK_11_2.1",
                "title": "Bài tập 2.5 (Trang 84 - SGK Toán 11 KNTT)",
                "content": r"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$, $AB = a$. Cạnh bên $SA \perp (ABC)$ và $SA = a\sqrt{3}$. Tính góc giữa cạnh bên $SC$ và mặt phẳng đáy $(ABC)$.",
                "hint_1": "Xác định hình chiếu của cạnh $SC$ lên mặt đáy $(ABC)$: $C$ là giao điểm, hình chiếu của $S$ là điểm $A$ (do $SA \perp (ABC)$).",
                "hint_2": "Hình chiếu của đoạn $SC$ lên đáy là đoạn $AC$. Vậy góc cần tìm là $\widehat{SCA}$.",
                "hint_3": "Tam giác $ABC$ vuông cân tại $B \Rightarrow AC = a\sqrt{2}$. Xét $\Delta SAC$ vuông tại $A$: $\tan \widehat{SCA} = \frac{SA}{AC} = \frac{a\sqrt{3}}{a\sqrt{2}} = \frac{\sqrt{6}}{2}$.",
                "similar_prompt": "Tạo 1 bài toán hình không gian lớp 11 tương tự tính góc giữa đường và mặt đáy cho hình chóp tam giác đều."
            }
        },
        "Bài 3: Cấp số cộng và Cấp số nhân": {
            "chapter": "Chương II: Dãy số. Cấp số cộng và Cấp số nhân",
            "video_title": "Video 95s: Công thức số hạng tổng quát & Tổng n số hạng đầu",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Cấp số cộng (CSC):** $u_n = u_1 + (n-1)d$; $S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n-1)d]}{2}$.
- **Cấp số nhân (CSN):** $u_n = u_1 \cdot q^{n-1}$; $S_n = u_1 \frac{1 - q^n}{1 - q}$ ($q \neq 1$).
- ⚠️ *Cảnh báo:* Chú ý $u_n$ bậc nhất theo $n$ là CSC, hàm mũ theo $n$ là CSN.
            """,
            "exercise": {
                "id": "SGK_11_3.1",
                "title": "Bài tập 2.12 (Trang 52 - SGK Toán 11 KNTT)",
                "content": r"Cho cấp số cộng $(u_n)$ thỏa mãn $u_1 = 3$ và công sai $d = 4$. Biết tổng $n$ số hạng đầu $S_n = 253$. Tìm số lượng số hạng $n$.",
                "hint_1": "Sử dụng công thức tổng $n$ số hạng: $S_n = \frac{n[2u_1 + (n-1)d]}{2}$.",
                "hint_2": "Thay số: $253 = \frac{n[2 \cdot 3 + (n-1) \cdot 4]}{2} \Leftrightarrow n(4n + 2)/2 = 253 \Leftrightarrow n(2n + 1) = 253$.",
                "hint_3": "Giải phương trình bậc hai $2n^2 + n - 253 = 0$. Vì $n \in \mathbb{N}^*$, ta chọn nghiệm nguyên dương $n = 11$.",
                "similar_prompt": "Tạo bài toán cấp số cộng tương tự tìm n khi biết u1, d và tổng Sn."
            }
        }
    },
    "Khối 12": {
        "Bài 1: Tính đơn điệu và Cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
            "video_title": "Video 120s: Bản đồ xét dấu đạo hàm $y'$ & Quy tắc cực trị chuẩn 2025+",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Tính đơn điệu:** Nếu $f'(x) \ge 0, \forall x \in K$ (bằng 0 tại hữu hạn điểm) thì hàm số đồng biến trên $K$.
- **Cực trị:** $x_0$ là điểm cực trị nếu $f'(x_0) = 0$ (hoặc không xác định) và $f'(x)$ đổi dấu khi qua $x_0$:
  - Đổi dấu từ $(+)$ sang $(-)$: Cực đại.
  - Đổi dấu từ $(-)$ sang $(+)$: Cực tiểu.
- ⚠️ *Lưu ý cấu trúc mới:* Phân biệt rõ "Điểm cực trị của hàm số" ($x$), "Giá trị cực trị" ($y$), và "Điểm cực trị của đồ thị" ($M(x; y)$).
            """,
            "exercise": {
                "id": "SGK_12_1.1",
                "title": "Bài tập 1.2 (Trang 14 - SGK Toán 12 KNTT)",
                "content": r"Tìm các khoảng đơn điệu và tọa độ điểm cực trị của đồ thị hàm số $y = x^3 - 3x^2 + 2$.",
                "hint_1": "Tính đạo hàm: $y' = 3x^2 - 6x = 3x(x - 2)$. Tìm nghiệm của $y' = 0$.",
                "hint_2": "Nghiệm là $x = 0$ và $x = 2$. Lập bảng xét dấu của tam thức bậc hai $y'$ (trong trái ngoài cùng).",
                "hint_3": "Hàm đồng biến trên $(-\infty; 0)$ và $(2; +\infty)$; nghịch biến trên $(0; 2)$. Điểm cực đại của đồ thị là $(0; 2)$, cực tiểu là $(2; -2)$.",
                "similar_prompt": "Tạo 1 bài toán khảo sát hàm bậc ba tương tự có tham số m để học sinh luyện tư duy phân loại."
            }
        },
        "Bài 2: Tọa độ vectơ và Hệ trục tọa độ Oxyz trong không gian": {
            "chapter": "Chương II: Vectơ và Hệ trục tọa độ trong không gian",
            "video_title": "Video 115s: Tích vô hướng, tích có hướng & Ứng dụng hình học không gian",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": True,
            "smart_notes": r"""
- **Tọa độ vectơ:** $\vec{u} = (x; y; z) \Leftrightarrow \vec{u} = x\vec{i} + y\vec{j} + z\vec{k}$.
- **Tích vô hướng:** $\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2 = |\vec{u}| |\vec{v}| \cos(\vec{u}, \vec{v})$.
- **Khoảng cách 2 điểm:** $AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.
- **Phương trình mặt cầu:** $(S): (x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$.
            """,
            "exercise": {
                "id": "SGK_12_2.1",
                "title": "Bài tập 2.8 (Trang 65 - SGK Toán 12 KNTT)",
                "content": r"Trong không gian $Oxyz$, cho $A(1; 2; -1)$, $B(3; 0; 1)$. Viết phương trình mặt cầu đường kính $AB$.",
                "hint_1": "Tâm $I$ của mặt cầu là trung điểm của đoạn thẳng $AB$. Sử dụng công thức tọa độ trung điểm: $x_I = \frac{x_A + x_B}{2}, \dots$",
                "hint_2": "Tính được $I(2; 1; 0)$. Bán kính $R = \frac{AB}{2} = \frac{\sqrt{(3-1)^2 + (0-2)^2 + (1 - (-1))^2}}{2}$.",
                "hint_3": "Ta có $AB = \sqrt{4 + 4 + 4} = 2\sqrt{3} \Rightarrow R = \sqrt{3}$. Vậy phương trình mặt cầu là: $(x-2)^2 + (y-1)^2 + z^2 = 3$.",
                "similar_prompt": "Tạo 1 bài toán Oxyz tương tự viết phương trình mặt phẳng trung trực của đoạn thẳng AB."
            }
        },
        "Bài 3: Nguyên hàm và Tích phân": {
            "chapter": "Chương IV: Nguyên hàm, Tích phân và Ứng dụng",
            "video_title": "Video 120s: Ứng dụng tích phân tính diện tích hình phẳng & Thể tích vật thể",
            "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "has_3d": False,
            "smart_notes": r"""
- **Định nghĩa tích phân:** $\int_a^b f(x)dx = F(b) - F(a)$.
- **Diện tích hình phẳng:** $S = \int_a^b |f(x) - g(x)| dx$.
- **Thể tích khối tròn xoay:** $V = \pi \int_a^b [f(x)]^2 dx$ (quay quanh trục $Ox$).
- ⚠️ *Mẹo bấm máy tính & tư duy:* Luôn tìm giao điểm trước để chia khoảng phá dấu trị tuyệt đối.
            """,
            "exercise": {
                "id": "SGK_12_3.1",
                "title": "Bài tập 4.6 (Trang 102 - SGK Toán 12 KNTT)",
                "content": r"Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = x^2 - 2x$ và trục hoành $Ox$.",
                "hint_1": "Phương trình hoành độ giao điểm với trục hoành ($y=0$): $x^2 - 2x = 0 \Leftrightarrow x = 0$ hoặc $x = 2$.",
                "hint_2": "Áp dụng công thức diện tích: $S = \int_0^2 |x^2 - 2x| dx$. Trên khoảng $(0; 2)$, biểu thức $x^2 - 2x \le 0$.",
                "hint_3": "Ta có $S = \int_0^2 (2x - x^2)dx = \left[x^2 - \frac{x^3}{3}\right]_0^2 = 4 - \frac{8}{3} = \frac{4}{3}$.",
                "similar_prompt": "Tạo bài toán tính diện tích hình phẳng giới hạn bởi parabol và đường thẳng y = x."
            }
        }
    }
}

# ==============================================================================
# 4. KHO ĐỀ KHẢO THÍ CHUẨN HÓA (GK1, CK1, GK2, CK2, TỐT NGHIỆP THPT & ĐGNL)
# ==============================================================================
EXAM_BANK = {
    "Khối 10": {
        "Giữa học kỳ 1": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 1 - Toán 10 (Chuẩn KNTT)",
            "p1": [
                {"q": r"Mệnh đề nào sau đây là mệnh đề chứa biến?", "ops": [r"A. $2 + 3 = 5$", r"B. $x^2 > 0$", r"C. $\pi$ là số vô tỉ", r"D. Hà Nội là thủ đô của Việt Nam"], "ans": "B", "exp": "Chứa biến x chưa xác định chân giá trị."},
                {"q": r"Cho tập hợp $A = \{x \in \mathbb{N} \mid x \le 3\}$. Số phần tử của tập hợp $A$ là:", "ops": ["A. 3", "B. 4", "C. 5", "D. Vô số"], "ans": "B", "exp": "A = {0, 1, 2, 3} gồm 4 phần tử."}
            ],
            "p2": [
                {"q": r"Cho tam thức bậc hai $f(x) = x^2 - 4x + 3$. Xét tính Đúng/Sai của các mệnh đề sau:", "items": [
                    ("a) Phương trình f(x) = 0 có 2 nghiệm phân biệt là x = 1 và x = 3.", True),
                    ("b) f(x) > 0 với mọi x thuộc khoảng (1; 3).", False),
                    ("c) Đỉnh của parabol có tọa độ I(2; -1).", True),
                    ("d) Điểm cực tiểu của hàm số là y = -1.", True)
                ]}
            ],
            "p3": [
                {"q": r"Cho tam giác ABC có AB = 6, AC = 8, góc A = 60 độ. Tính độ dài cạnh BC (làm tròn đến hàng phần mười nếu là số thập phân).", "ans": "7.2", "exp": "BC^2 = 6^2 + 8^2 - 2*6*8*cos(60) = 52 => BC ≈ 7.21"}
            ]
        },
        "Cuối học kỳ 1": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 1 - Toán 10",
            "p1": [{"q": r"Cho hai vectơ $\vec{u}=(2; -1)$ và $\vec{v}=(3; 4)$. Tích vô hướng $\vec{u} \cdot \vec{v}$ bằng:", "ops": ["A. 2", "B. 10", "C. -2", "D. 14"], "ans": "A", "exp": "2*3 + (-1)*4 = 6 - 4 = 2."}],
            "p2": [{"q": r"Cho tam giác đều ABC cạnh bằng 2. Xét các khẳng định sau:", "items": [("a) Độ dài vectơ AB bằng 2.", True), ("b) Góc giữa vectơ AB và AC bằng 60 độ.", True), ("c) Tích vô hướng AB.AC bằng 2.", True), ("d) Vectơ AB cùng phương vectơ BC.", False)]}],
            "p3": [{"q": r"Một người kéo một vật với một lực F = 50 N hợp với phương ngang một góc 30 độ làm vật di chuyển 10 mét. Tính công sinh ra (kJ, làm tròn đến 2 chữ số thập phân).", "ans": "0.43", "exp": "A = F * s * cos(30) = 50 * 10 * sqrt(3)/2 ≈ 433 J = 0.43 kJ."}]
        },
        "Giữa học kỳ 2": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 2 - Toán 10",
            "p1": [{"q": r"Phương trình quy về bậc hai $\sqrt{2x^2 - 5x - 3} = x - 1$ có bao nhiêu nghiệm nguyên?", "ops": ["A. 0", "B. 1", "C. 2", "D. 3"], "ans": "B", "exp": "Bình phương hai vế với điều kiện x >= 1, giải ra 1 nghiệm thỏa mãn."}],
            "p2": [{"q": r"Cho đường thẳng d: 3x - 4y + 5 = 0. Xét tính Đúng/Sai:", "items": [("a) Vectơ chỉ phương của d là u = (4; 3).", True), ("b) Điểm M(1; 2) thuộc đường thẳng d.", True), ("c) Khoảng cách từ gốc O đến d bằng 1.", True), ("d) d vuông góc với đường thẳng 4x + 3y = 0.", False)]}],
            "p3": [{"q": r"Tính khoảng cách từ điểm A(1; 3) đến đường thẳng d: 3x - 4y + 4 = 0.", "ans": "1", "exp": "|3*1 - 4*3 + 4| / sqrt(3^2 + (-4)^2) = |-5| / 5 = 1."}]
        },
        "Cuối học kỳ 2": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 2 - Toán 10 Toàn Diện",
            "p1": [{"q": r"Có bao nhiêu cách chọn 3 học sinh từ một tổ gồm 10 học sinh?", "ops": ["A. 720", "B. 120", "C. 30", "D. 210"], "ans": "B", "exp": "C(10, 3) = 120."}],
            "p2": [{"q": r"Gieo một con xúc xắc cân đối 2 lần liên tiếp. Xét các biến cố:", "items": [("a) Không gian mẫu có 36 phần tử.", True), ("b) Biến cố tổng số chấm bằng 7 có xác suất là 1/6.", True), ("c) Xác suất để cả 2 lần đều xuất hiện mặt 6 chấm là 1/12.", False), ("d) Biến cố ít nhất một lần xuất hiện mặt chẵn có xác suất 3/4.", True)]}],
            "p3": [{"q": r"Tính số hoán vị của 5 chữ số phân biệt {1, 2, 3, 4, 5}.", "ans": "120", "exp": "5! = 120."}]
        }
    },
    "Khối 11": {
        "Giữa học kỳ 1": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 1 - Toán 11",
            "p1": [
                {"q": r"Phương trình $\sin(x) = 1$ có tập nghiệm là:", "ops": [r"A. $x = \frac{\pi}{2} + k2\pi$", r"B. $x = k\pi$", r"C. $x = \frac{\pi}{2} + k\pi$", r"D. $x = \pi + k2\pi$"], "ans": "A", "exp": "Nghiệm đặc biệt trên trục sin."},
                {"q": r"Cho cấp số cộng $(u_n)$ có $u_1 = 2, d = 3$. Tìm $u_5$.", "ops": ["A. 14", "B. 11", "C. 17", "D. 15"], "ans": "A", "exp": "u_5 = 2 + 4*3 = 14."}
            ],
            "p2": [
                {"q": r"Cho hàm số $y = \cos(2x)$. Xét các khẳng định sau:", "items": [
                    ("a) Chu kỳ tuần hoàn của hàm số là T = pi.", True),
                    ("b) Tập giá trị của hàm số là [-1; 1].", True),
                    ("c) Hàm số đồng biến trên khoảng (0; pi/2).", False),
                    ("d) Đồ thị hàm số nhận trục Oy làm trục đối xứng.", True)
                ]}
            ],
            "p3": [
                {"q": r"Một rạp chiếu phim có 15 hàng ghế. Hàng đầu tiên có 20 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Tính tổng số ghế trong rạp.", "ans": "510", "exp": "CSC: u1=20, d=2, n=15 => S_15 = 15*(2*20 + 14*2)/2 = 510 ghế."}
            ]
        },
        "Cuối học kỳ 1": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 1 - Toán 11",
            "p1": [{"q": r"Giới hạn $\lim_{n \to \infty} \frac{2n + 1}{n - 3}$ bằng:", "ops": ["A. 2", "B. -1/3", "C. vô cùng", "D. 0"], "ans": "A", "exp": "Chia cả tử và mẫu cho n."}],
            "p2": [{"q": r"Cho tứ diện ABCD. Gọi M, N lần lượt là trung điểm của AB, CD:", "items": [("a) MN và BC chéo nhau.", True), ("b) Giao tuyến của (ABN) và (ABC) là AB.", True), ("c) Bốn điểm A, B, C, D đồng phẳng.", False), ("d) MN cắt đường thẳng BD.", False)]}],
            "p3": [{"q": r"Tính giới hạn: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$.", "ans": "4", "exp": "x^2 - 4 = (x-2)(x+2) => lim = 2 + 2 = 4."}]
        },
        "Giữa học kỳ 2": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 2 - Toán 11",
            "p1": [{"q": r"Đạo hàm của hàm số $y = x^3 - 2x$ tại điểm $x = 1$ bằng:", "ops": ["A. 1", "B. 3", "C. -1", "D. 0"], "ans": "A", "exp": "y' = 3x^2 - 2 => y'(1) = 3(1) - 2 = 1."}],
            "p2": [{"q": r"Cho hình lập phương ABCD.A'B'C'D'. Xét tính Đúng/Sai:", "items": [("a) Đường thẳng AA' vuông góc với mặt phẳng (ABCD).", True), ("b) Góc giữa A'C' và BD bằng 90 độ.", True), ("c) Khoảng cách giữa AB và C'D' bằng độ dài cạnh hình lập phương.", True), ("d) Mặt phẳng (A'BD) song song với (B'CD').", False)]}],
            "p3": [{"q": r"Một chất điểm chuyển động với phương trình $s(t) = 2t^3 - t^2 + 5$ (mét). Vận tốc tức thời của chất điểm tại thời điểm $t = 3$ giây là bao nhiêu (m/s)?", "ans": "48", "exp": "v(t) = s'(t) = 6t^2 - 2t => v(3) = 6*9 - 6 = 48 m/s."}]
        },
        "Cuối học kỳ 2": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 2 - Toán 11 Toàn Diện",
            "p1": [{"q": r"Cho hai biến cố độc lập A và B có P(A) = 0.4; P(B) = 0.5. Tính xác suất P(A giao B):", "ops": ["A. 0.2", "B. 0.9", "C. 0.1", "D. 0.45"], "ans": "A", "exp": "P(AB) = P(A)*P(B) = 0.4 * 0.5 = 0.2."}],
            "p2": [{"q": r"Cho hình chóp S.ABCD có đáy ABCD là hình vuông cạnh a, SA vuông góc đáy và SA = a:", "items": [("a) Tam giác SBC vuông tại B.", True), ("b) Góc giữa SC và đáy (ABCD) bằng 45 độ.", False), ("c) Thể tích khối chóp bằng a^3 / 3.", True), ("d) Khoảng cách từ S đến mặt phẳng (ABCD) bằng a.", True)]}],
            "p3": [{"q": r"Hộp thứ nhất có 3 bi trắng 2 bi đỏ. Hộp thứ hai có 4 bi trắng 1 bi đỏ. Lấy ngẫu nhiên mỗi hộp 1 bi. Tính xác suất để lấy được 2 bi trắng (dưới dạng số thập phân).", "ans": "0.48", "exp": "P = (3/5) * (4/5) = 12/25 = 0.48."}]
        }
    },
    "Khối 12": {
        "Giữa học kỳ 1": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 1 - Toán 12",
            "p1": [{"q": r"Điểm cực đại của đồ thị hàm số $y = -x^3 + 3x - 1$ là:", "ops": [r"A. $M(1; 1)$", r"B. $M(-1; -3)$", r"C. $x = 1$", r"D. $y = 1$"], "ans": "A", "exp": "y' = -3x^2 + 3 = 0 <=> x = +-1. x=1 là điểm cực đại, y(1) = 1 => M(1; 1)."}],
            "p2": [{"q": r"Cho hàm số $y = \frac{2x - 1}{x + 1}$. Xét các khẳng định sau:", "items": [("a) Tiệm cận đứng của đồ thị là x = -1.", True), ("b) Tiệm cận ngang của đồ thị là y = 2.", True), ("c) Hàm số đồng biến trên toàn trục số thực R.", False), ("d) Đồ thị cắt trục tung tại điểm có tung độ y = -1.", True)]}],
            "p3": [{"q": r"Tìm giá trị lớn nhất của hàm số $f(x) = x^3 - 3x + 5$ trên đoạn $[0; 2]$.", "ans": "7", "exp": "f'(x) = 3x^2 - 3 = 0 => x = 1. f(0) = 5, f(1) = 3, f(2) = 7 => Max = 7."}]
        },
        "Cuối học kỳ 1": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 1 - Toán 12",
            "p1": [{"q": r"Trong không gian Oxyz, cho mặt cầu $(S): (x-1)^2 + (y+2)^2 + (z-3)^2 = 16$. Bán kính của mặt cầu bằng:", "ops": ["A. 4", "B. 16", "C. 8", "D. 2"], "ans": "A", "exp": "R = sqrt(16) = 4."}],
            "p2": [{"q": r"Trong không gian Oxyz, cho A(1; 0; 0), B(0; 2; 0), C(0; 0; 3):", "items": [("a) Phương trình mặt phẳng (ABC) là x/1 + y/2 + z/3 = 1.", True), ("b) Vectơ pháp tuyến của (ABC) cùng phương với (6; 3; 2).", True), ("c) Gốc tọa độ O nằm trên mặt phẳng (ABC).", False), ("d) Thể tích tứ diện OABC bằng 1.", True)]}],
            "p3": [{"q": r"Tính khoảng cách từ gốc tọa độ O đến mặt phẳng (P): 2x - 2y + z - 9 = 0.", "ans": "3", "exp": "|-9| / sqrt(2^2 + (-2)^2 + 1^2) = 9 / 3 = 3."}]
        },
        "Giữa học kỳ 2": {
            "title": "Đề Khảo Thí Giữa Học Kỳ 2 - Toán 12",
            "p1": [{"q": r"Họ nguyên hàm của hàm số $f(x) = e^{2x} + \cos(x)$ là:", "ops": [r"A. $\frac{1}{2}e^{2x} + \sin(x) + C$", r"B. $2e^{2x} - \sin(x) + C$", r"C. $e^{2x} + \sin(x) + C$", r"D. $\frac{1}{2}e^{2x} - \sin(x) + C$"], "ans": "A", "exp": "Nguyên hàm cơ bản."}],
            "p2": [{"q": r"Cho tích phân $I = \int_0^1 (2x + 1)e^x dx$:", "items": [("a) Có thể tính tích phân I bằng phương pháp từng phần.", True), ("b) Đặt u = 2x + 1 thì du = 2dx.", True), ("c) Giá trị của I là một số nguyên.", False), ("d) Kết quả I = e + 1.", True)]}],
            "p3": [{"q": r"Tính diện tích hình phẳng giới hạn bởi đường cong $y = x^3$, trục hoành $Ox$, và hai đường thẳng $x = 0, x = 2$.", "ans": "4", "exp": "Tích phân từ 0 đến 2 của x^3 dx = [x^4 / 4]_0^2 = 16 / 4 = 4."}]
        },
        "Cuối học kỳ 2": {
            "title": "Đề Kiểm Tra Cuối Học Kỳ 2 - Toán 12",
            "p1": [{"q": r"Phương sai của mẫu số liệu ghép nhóm đo lường điều gì?", "ops": ["A. Độ phân tán của số liệu quanh số trung bình", "B. Giá trị trung bình", "C. Giá trị xuất hiện nhiều nhất", "D. Khoảng biến thiên"], "ans": "A", "exp": "Khái niệm thống kê chuẩn."}],
            "p2": [{"q": r"Xét các khẳng định về xác suất có điều kiện P(A|B):", "items": [("a) P(A|B) = P(AB) / P(B) với P(B) > 0.", True), ("b) Nếu A và B độc lập thì P(A|B) = P(A).", True), ("c) P(A|B) luôn bằng P(B|A).", False), ("d) 0 <= P(A|B) <= 1.", True)]}],
            "p3": [{"q": r"Một cuộc thi có 100 thí sinh. Điểm trung bình là 7.0, độ lệch chuẩn s = 1.5. Tính phương sai của mẫu số liệu.", "ans": "2.25", "exp": "Phương sai s^2 = 1.5^2 = 2.25."}]
        },
        "🏛️ Ôn thi Tốt nghiệp THPT (Cấu trúc 2025+)": {
            "title": "ĐỀ KHẢO THÍ CHUẨN ĐỊNH DẠNG TỐT NGHIỆP THPT (BỘ GD&ĐT MỚI)",
            "p1": [
                {"q": r"Cho hàm số $y = f(x)$ có đạo hàm $f'(x) = x(x-1)^2 (x+2)^3$. Số điểm cực trị của hàm số đã cho là:", "ops": ["A. 2", "B. 3", "C. 1", "D. 0"], "ans": "A", "exp": "f'(x) đổi dấu khi qua nghiệm bội lẻ x = 0 và x = -2 (bội 3). Nghiệm x = 1 là bội chẵn (bội 2) nên không đổi dấu. Vậy có đúng 2 cực trị."}
            ],
            "p2": [
                {"q": r"Cho hình chóp tam giác đều $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$. Cạnh bên tạo với mặt phẳng đáy một góc $60^\circ$. Xét tính Đúng/Sai của các mệnh đề sau:", "items": [
                    ("a) Hình chiếu vuông góc của đỉnh S lên mặt phẳng (ABC) trùng với trọng tâm tam giác ABC.", True),
                    ("b) Độ dài đường cao của hình chóp bằng a.", True),
                    ("c) Thể tích của khối chóp S.ABC bằng a^3 / 4.", False),
                    ("d) Bán kính mặt cầu ngoại tiếp hình chóp bằng 2a/3.", True)
                ]}
            ],
            "p3": [
                {"q": r"Một doanh nghiệp sản xuất một loại sản phẩm với hàm tổng chi phí $C(x) = x^3 - 30x^2 + 500x + 1000$ (nghìn đồng), trong đó $x$ là số sản phẩm ($1 \le x \le 30$). Biết giá bán mỗi sản phẩm trên thị trường là 800 nghìn đồng. Hãy xác định số sản phẩm $x$ cần sản xuất để lợi nhuận của doanh nghiệp đạt giá trị lớn nhất.", "ans": "20", "exp": "Lợi nhuận L(x) = Doanh thu - Chi phí = 800x - C(x) = -x^3 + 30x^2 + 300x - 1000. L'(x) = -3x^2 + 60x + 300 = 0 <=> x = 10 + 10*sqrt(2) hoặc giải thực tế x = 20."}
            ]
        },
        "🚀 Ôn thi Đánh giá năng lực (ĐGNL)": {
            "title": "BỘ ĐỀ ĐÁNH GIÁ NĂNG LỰC TOÁN HỌC & TƯ DUY LOGIC (ĐHQG / ĐHBK)",
            "p1": [
                {"q": r"Một hồ chứa nước sinh hoạt đang chứa $1000 \text{ m}^3$ nước và bị nhiễm vi khuẩn. Người ta tiến hành sục hóa chất diệt khuẩn. Tốc độ thay đổi lượng vi khuẩn sau $t$ giờ được mô hình bởi hàm số $N'(t) = -\frac{200}{(t+1)^2}$ (đơn vị khuẩn/giờ). Biết ban đầu $N(0) = 500$ đơn vị. Sau bao nhiêu giờ thì lượng vi khuẩn giảm xuống còn 350 đơn vị?", "ops": ["A. 3 giờ", "B. 4 giờ", "C. 2 giờ", "D. 5 giờ"], "ans": "A", "exp": "N(t) = nguyên hàm N'(t) = 200/(t+1) + C. N(0) = 200 + C = 500 => C = 300. N(t) = 200/(t+1) + 300 = 350 => 200/(t+1) = 50 => t + 1 = 4 => t = 3 giờ."}
            ],
            "p2": [
                {"q": r"Trong một phòng thí nghiệm hóa sinh, một mẫu chất phóng xạ phân rã theo hàm số mũ $M(t) = M_0 \cdot e^{-0.05t}$ (với $t$ tính bằng năm). Xét các khẳng định sau:", "items": [
                    ("a) Ban đầu tại thời điểm t = 0, khối lượng chất phóng xạ là M0.", True),
                    ("b) Khối lượng chất phóng xạ tăng dần theo thời gian.", False),
                    ("c) Chu kỳ bán rã (thời gian để khối lượng giảm đi một nửa) xấp xỉ 13.86 năm.", True),
                    ("d) Sau 40 năm, khối lượng còn lại nhỏ hơn 15% khối lượng ban đầu.", True)
                ]}
            ],
            "p3": [
                {"q": r"Một người gửi tiết kiệm ngân hàng 200 triệu đồng với lãi suất kép 6.5%/năm. Hỏi sau tối thiểu bao nhiêu năm thì số tiền người đó nhận được cả gốc lẫn lãi vượt quá 350 triệu đồng? (Điền số nguyên năm tối thiểu).", "ans": "9", "exp": "200 * (1 + 0.065)^n > 350 <=> (1.065)^n > 1.75 <=> n > ln(1.75) / ln(1.065) ≈ 8.87 => Tối thiểu 9 năm."}
            ]
        }
    }
}

# ==============================================================================
# 5. DỮ LIỆU TÀI KHOẢN MẪU VÀ QUẢN LÝ SESSION STATE
# ==============================================================================
DEFAULT_STUDENTS = [
    {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "current_level": "Khá", "weak_spots": "Dấu lượng giác, Hình không gian", "flowers": 30, "hints_avg": 1.5, "total_solved": 8, "last_active": "2026-09-24"},
    {"student_id": "HS10_01", "password": "123", "full_name": "Lê Bảo Ngọc", "grade": 10, "current_level": "Giỏi", "weak_spots": "Phủ định mệnh đề", "flowers": 35, "hints_avg": 0.5, "total_solved": 14, "last_active": "2026-09-24"},
    {"student_id": "HS12_01", "password": "123", "full_name": "Nguyễn Hoàng Nam", "grade": 12, "current_level": "Trung bình", "weak_spots": "Tọa độ Oxyz, Đạo hàm tham số", "flowers": 28, "hints_avg": 2.2, "total_solved": 6, "last_active": "2026-09-24"}
]

if "auth_user" not in st.session_state:
    st.session_state["auth_user"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None
if "students_db" not in st.session_state:
    st.session_state["students_db"] = DEFAULT_STUDENTS
if "inbox_db" not in st.session_state:
    st.session_state["inbox_db"] = []
if "curr_grade" not in st.session_state:
    st.session_state["curr_grade"] = "Khối 11"

# ĐỒNG BỘ DỮ LIỆU TỪ GOOGLE SHEETS
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

def save_new_student(new_student):
    st.session_state["students_db"].append(new_student)
    if conn is not None:
        try:
            df = pd.DataFrame(st.session_state["students_db"])
            conn.write(worksheet="STUDENT_PROFILES", data=df)
        except Exception:
            pass

def log_activity_to_db(student_id, lesson_id, exercise_id, action_type, hint_lvl, is_corr, tag):
    new_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "student_id": student_id,
        "lesson_id": lesson_id,
        "exercise_id": exercise_id,
        "action_type": action_type,
        "hint_level": hint_lvl,
        "is_correct": is_corr,
        "error_tag": tag
    }
    if conn is not None:
        try:
            df_new = pd.DataFrame([new_row])
            conn.write(worksheet="ACTIVITY_LOGS", data=df_new)
        except Exception:
            pass

def send_question_inbox(student_id, sname, lesson_id, ex_id, note):
    item = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "student_id": student_id,
        "student_name": sname,
        "lesson_id": lesson_id,
        "exercise_id": ex_id,
        "student_note": note,
        "status": "Chưa giải đáp"
    }
    st.session_state["inbox_db"].append(item)
    if conn is not None:
        try:
            df_inbox = pd.DataFrame([item])
            conn.write(worksheet="TEACHER_INBOX", data=df_inbox)
        except Exception:
            pass

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
# 6. DỰNG MÔ HÌNH HÌNH HỌC KHÔNG GIAN 3D ZERO-INSTALL (WEBGL PLOTLY)
# ==============================================================================
def render_3d_geometry_view(topic_type="SHAPE_3D"):
    if topic_type == "OXYZ":
        fig = go.Figure()
        fig.add_trace(go.Scatter3d(
            x=[0, 3, 0, 0], y=[0, 0, 3, 0], z=[0, 0, 0, 3],
            mode='lines+text',
            text=['O', 'Ox', 'Oy', 'Oz'],
            line=dict(color='#0284C7', width=6)
        ))
        u, v = [0, 2], [0, 3]
        fig.add_trace(go.Scatter3d(
            x=[1, 3], y=[2, 0], z=[-1, 1],
            mode='markers+text',
            marker=dict(size=8, color=['#DC2626', '#16A34A']),
            text=['A(1;2;-1)', 'B(3;0;1)'],
            textposition='top right'
        ))
        fig.add_trace(go.Scatter3d(
            x=[1, 3], y=[2, 0], z=[-1, 1],
            mode='lines',
            line=dict(color='#F59E0B', width=4, dash='dash')
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
# 7. PHÂN HỆ ĐĂNG NHẬP & PHÂN QUYỀN (AUTH & ACCOUNT LOGIC)
# ==============================================================================
if st.session_state["auth_user"] is None:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📐 HỆ SINH THÁI TỰ HỌC TOÁN THPT 'GSTOÁN'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>Bám sát chuẩn SGK Kết nối tri thức với cuộc sống (Khối 10, 11, 12)</p>", unsafe_allow_html=True)
    
    col_l1, col_box, col_l2 = st.columns([1, 1.3, 1])
    with col_box:
        with st.container(border=True):
            st.markdown("### 🔐 Cổng Đăng Nhập")
            login_role = st.radio("Đăng nhập với vai trò:", ["👨‍🎓 Học sinh", "👩‍🏫 Giáo viên (Admin)"], horizontal=True)
            user_input = st.text_input("Tên đăng nhập / Mã học sinh:", placeholder="Ví dụ: HS11_01 hoặc admin")
            pass_input = st.text_input("Mật khẩu:", type="password", placeholder="Nhập mật khẩu...")
            
            if st.button("Đăng nhập vào GSToán", use_container_width=True):
                if login_role == "👩‍🏫 Giáo viên (Admin)":
                    if user_input.strip().lower() == "admin" and (pass_input == "gstoan2026" or pass_input == "123"):
                        st.session_state["auth_user"] = {"full_name": "Thầy/Cô Quản Trị Môn Toán", "role": "teacher"}
                        st.session_state["role"] = "teacher"
                        st.success("Đăng nhập Giáo viên thành công!")
                        st.rerun()
                    else:
                        st.error("Sai tài khoản hoặc mật khẩu Giáo viên! (Mặc định: admin / gstoan2026 hoặc 123)")
                else:
                    all_st = load_all_students()
                    found = next((s for s in all_st if s["student_id"].upper() == user_input.strip().upper()), None)
                    if found:
                        if str(found.get("password", "123")) == pass_input.strip():
                            st.session_state["auth_user"] = found
                            st.session_state["role"] = "student"
                            st.session_state["curr_grade"] = f"Khối {found.get('grade', 11)}"
                            st.success(f"Chào mừng em {found['full_name']}!")
                            st.rerun()
                        else:
                            st.error("Mật khẩu không chính xác. Hãy liên hệ Thầy/Cô để được cấp lại.")
                    else:
                        st.error("Không tìm thấy mã học sinh này trong danh sách lớp!")
            
            st.markdown("---")
            st.caption("💡 *Tài khoản học sinh trải nghiệm:* `HS11_01` (Pass: `123`), `HS12_01` (Pass: `123`), `HS10_01` (Pass: `123`). Admin: `admin` / `gstoan2026`.")
    st.stop()

# ==============================================================================
# 8. THANH ĐIỀU HƯỚNG BÊN HÔNG (SIDEBAR) & ĐĂNG XUẤT
# ==============================================================================
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state['auth_user']['full_name']}")
    if st.session_state["role"] == "student":
        st.caption(f"Mã: **{st.session_state['auth_user']['student_id']}** | Lớp: **{st.session_state['curr_grade']}**")
        
        # HIỂN THỊ VƯỜN HOA TRI THỨC CỦA HỌC SINH
        flowers = st.session_state['auth_user'].get('flowers', 30)
        with st.container(border=True):
            st.markdown("<h5 style='text-align: center; color: #DB2777; margin:0;'>🌸 Vườn hoa Tri thức</h5>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #BE185D; margin:4px 0;'>{flowers} 🌸</h2>", unsafe_allow_html=True)
            st.caption("Chăm chỉ tự giải bài, xem video và luyện đề để tích hoa nhận Học bổng vinh danh cuối kỳ!")
    else:
        st.info("Quyền hạn: **Cố vấn Sư phạm & Quản trị Hệ thống**")

    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.session_state["role"] = None
        st.rerun()

    st.markdown("---")

# ==============================================================================
# 9. PHÂN HỆ GIÁO VIÊN (ADMIN PANEL & QUẢN LÝ ACCOUNT)
# ==============================================================================
if st.session_state["role"] == "teacher":
    st.title("👩‍🏫 Trung Tâm Quản Trị Sư Phạm & Điều Hành GSToán")
    st.caption("Phân hệ dành riêng cho Giáo viên: Tạo tài khoản, chẩn đoán năng lực học sinh và xử lý thắc mắc.")

    t_tab1, t_tab2, t_tab3 = st.tabs([
        "👥 Quản lý & Cấp Tài khoản Học sinh", 
        "📬 Hộp thư Cứu trợ Sư phạm (Thắc mắc)", 
        "📊 Chẩn đoán Năng lực & Khuyến nghị AI"
    ])

    # --------------------------------------------------------------------------
    # TAB GIAO VIEN 1: TẠO VÀ CẤP TÀI KHOẢN HỌC SINH
    # --------------------------------------------------------------------------
    with t_tab1:
        st.subheader("📋 Danh sách Tài khoản Học sinh Hiện tại")
        all_st = load_all_students()
        df_students = pd.DataFrame(all_st)
        st.dataframe(df_students[["student_id", "full_name", "grade", "current_level", "flowers", "weak_spots", "password"]], use_container_width=True)

        with st.container(border=True):
            st.markdown("#### ➕ Tạo và Cấp Tài Khoản Mới Cho Học Sinh")
            with st.form("form_create_student"):
                c_c1, c_c2 = st.columns(2)
                with c_c1:
                    new_id = st.text_input("Mã học sinh mới (Ví dụ: HS11_05):")
                    new_name = st.text_input("Họ và tên học sinh:")
                    new_grade = st.selectbox("Khối lớp:", [10, 11, 12], index=1)
                with c_c2:
                    new_pass = st.text_input("Mật khẩu cấp phát:", value="123")
                    new_lvl = st.selectbox("Học lực khởi điểm:", ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Cần cố gắng"], index=2)
                    new_weak = st.text_input("Lỗ hổng kiến thức ghi nhận trước (nếu có):", value="Cần rèn thêm kỹ năng giải toán SGK")

                submit_create = st.form_submit_button("Xác nhận Cấp Tài Khoản")
                if submit_create:
                    if not new_id.strip() or not new_name.strip():
                        st.error("Vui lòng điền đầy đủ Mã học sinh và Họ tên!")
                    elif any(s["student_id"].upper() == new_id.strip().upper() for s in all_st):
                        st.error("Mã học sinh này đã tồn tại trên hệ thống!")
                    else:
                        new_acc = {
                            "student_id": new_id.strip().upper(),
                            "password": new_pass.strip(),
                            "full_name": new_name.strip(),
                            "grade": int(new_grade),
                            "current_level": new_lvl,
                            "weak_spots": new_weak.strip(),
                            "flowers": 30,
                            "hints_avg": 0.0,
                            "total_solved": 0,
                            "last_active": datetime.now().strftime("%Y-%m-%d")
                        }
                        save_new_student(new_acc)
                        st.success(f"✅ Đã tạo thành công tài khoản `{new_acc['student_id']}` cho học sinh **{new_acc['full_name']}** với 30 hoa khởi điểm!")
                        st.rerun()

        with st.container(border=True):
            st.markdown("#### 🌸 Vinh Danh & Thưởng Hoa Đột Xuất Cho Học Sinh")
            col_rw1, col_rw2, col_rw3 = st.columns([1.5, 1, 1])
            with col_rw1:
                st_target = st.selectbox("Chọn học sinh cần thưởng:", [f"{s['student_id']} - {s['full_name']}" for s in all_st])
            with col_rw2:
                flower_add = st.number_input("Số hoa thưởng thêm:", min_value=1, max_value=20, value=2)
            with col_rw3:
                reason_add = st.text_input("Lý do vinh danh:", value="Phát biểu tích cực trên lớp")
            if st.button("Tặng Hoa Vinh Danh"):
                target_id = st_target.split(" - ")[0]
                reward_student_flower(target_id, flower_add, reason_add)
                st.success(f"Đã cộng +{flower_add} bông hoa cho học sinh {st_target}!")

    # --------------------------------------------------------------------------
    # TAB GIAO VIEN 2: HỘP THƯ SƯ PHẠM
    # --------------------------------------------------------------------------
    with t_tab2:
        st.subheader("📬 Hộp Thư Cứu Trợ Sư Phạm (Học sinh gửi điểm bế tắc)")
        st.caption("Các câu hỏi học sinh đã xem gợi ý nhưng vẫn chưa thông suốt, chuyển tiếp lên lớp nhờ Thầy/Cô gỡ điểm nghẽn.")
        if st.session_state["inbox_db"]:
            df_in = pd.DataFrame(st.session_state["inbox_db"])
            st.dataframe(df_in, use_container_width=True)
        else:
            st.success("Hiện tại không có câu hỏi tồn đọng nào từ học sinh!")

    # --------------------------------------------------------------------------
    # TAB GIAO VIEN 3: CHẨN ĐOÁN VÀ DỰ BÁO NĂNG LỰC
    # --------------------------------------------------------------------------
    with t_tab3:
        st.subheader("🔮 Chẩn Đoán Sư Phạm Chuyên Sâu Từng Học Sinh")
        all_st = load_all_students()
        selected_st_str = st.selectbox("Chọn học sinh cần chẩn đoán:", [f"{s['student_id']} - {s['full_name']}" for s in all_st])
        curr_s_id = selected_st_str.split(" - ")[0]
        s_data = next((s for s in all_st if s["student_id"] == curr_s_id), None)

        if s_data and st.button("Chạy Mô Hình Dự Báo & Khuyến Nghị"):
            with st.spinner("AI đang phân tích chuỗi dữ liệu tự học..."):
                prompt_diag = f"""
                Bạn là Cố vấn Sư phạm Toán THPT bám sát chương trình GDPT và SGK Kết nối tri thức.
                Dữ liệu học sinh:
                - Họ tên: {s_data['full_name']} (Lớp {s_data.get('grade', 11)})
                - Cấp độ: {s_data.get('current_level')}
                - Lỗ hổng: {s_data.get('weak_spots')}
                - Số bài giải hoàn thành: {s_data.get('total_solved')}
                - Số hoa tích lũy: {s_data.get('flowers')}

                YÊU CẦU BÁO CÁO CHO GIÁO VIÊN:
                1. DỰ BÁO: Khoảng điểm bài thi khảo thí sắp tới (thang điểm 10) và mức độ rủi ro (Đỏ / Vàng / Xanh).
                2. NGUYÊN NHÂN SÂU XA: Phân tích vì sao học sinh gặp khó khăn ở các dạng toán trên.
                3. HÀNH ĐỘNG SƯ PHẠM: 2 việc giáo viên nên làm trực tiếp trên lớp và 1 bài tập giao bổ trợ trên Web App.
                """
                if client:
                    try:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_diag)
                        advice_txt = res.text
                    except Exception:
                        advice_txt = "Hệ thống AI đang bận. Dữ liệu ghi nhận: Học sinh cần chú trọng làm bài tập củng cố nấc 1 trên lớp."
                else:
                    advice_txt = "Dự báo: 7.0 - 7.5 điểm. Cần lưu ý luyện kỹ bài tập hình học không gian và kỹ năng xét dấu tam thức."

                with st.container(border=True):
                    st.markdown(advice_txt)
    st.stop()

# ==============================================================================
# 10. PHÂN HỆ HỌC SINH (TOÀN VẸN NỘI HÀM & TƯƠNG TÁC ĐỘNG)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN KHỐI LỚP VÀ BÀI HỌC TOÀN NĂNG (CONTEXT SWITCHER)
c_sel1, c_sel2 = st.columns([1, 2.5])
with c_sel1:
    selected_grade = st.selectbox(
        "📚 Chọn Khối Lớp:",
        ["Khối 10", "Khối 11", "Khối 12"],
        index=0 if student_info.get("grade") == 10 else (2 if student_info.get("grade") == 12 else 1)
    )
with c_sel2:
    available_lessons = list(CURRICULUM_DATA[selected_grade].keys())
    selected_lesson_name = st.selectbox("📖 Chọn Bài Học SGK (Kết Nối Tri Thức):", available_lessons)

lesson_obj = CURRICULUM_DATA[selected_grade][selected_lesson_name]

# 4 TABS HỌC TẬP TOÀN DIỆN CHO MỖI BÀI HỌC
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Video, Ghi Chú & 3D)",
    "📝 Đồng Hành Bài Tập SGK & Gợi Ý Phân Tầng",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí & Luyện Đề Chuẩn Hóa"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC THEO BÀI HỌC
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {lesson_obj['chapter']}")
    st.markdown(f"#### {selected_lesson_name}")

    if lesson_obj.get("has_3d", False):
        with st.container(border=True):
            st.markdown("🌐 **Mô Hình Không Gian 3D Tương Tác Trực Tiếp (Zero-Install)**")
            st.caption("Dùng chuột hoặc ngón tay để xoay lật 360 độ, quan sát thiết diện và trực quan hóa góc trong không gian:")
            topic_3d = "OXYZ" if "Oxyz" in selected_lesson_name else "SHAPE_3D"
            render_3d_geometry_view(topic_3d)

    col_v, col_n = st.columns([1.1, 1])
    with col_v:
        with st.container(border=True):
            st.markdown(f"🎬 **{lesson_obj['video_title']}**")
            st.caption("Cô đọng lý thuyết trọng tâm + quét nhanh ví dụ bẫy sai lầm")
            st.video(lesson_obj["video_url"])
            if st.button("🌸 Đã xem kỹ video bài giảng (+1 hoa)", key=f"btn_v_{selected_lesson_name}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ xem bài giảng vi mô")
                log_activity_to_db(student_info["student_id"], selected_lesson_name, "VIDEO_TAB", "WATCH_VIDEO", 0, "TRUE", "Xem video bài học")
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes $\LaTeX$)**")
            st.markdown(lesson_obj["smart_notes"])

# ------------------------------------------------------------------------------
# TAB 2: ĐỒNG HÀNH BÀI TẬP SGK & NÚT CỨU TRỢ SƯ PHẠM
# ------------------------------------------------------------------------------
with tab2:
    ex_data = lesson_obj["exercise"]
    with st.container(border=True):
        st.subheader(f"📝 {ex_data['title']}")
        st.markdown(ex_data["content"])

        c_h1, c_h2, c_h3 = st.columns(3)
        with c_h1:
            if st.button("💡 Mở Gợi Ý Nấc 1", key=f"h1_{ex_data['id']}", use_container_width=True):
                st.info(f"**Gợi ý nấc 1 (Định hướng định lý/công thức):**\n\n{ex_data['hint_1']}")
                log_activity_to_db(student_info["student_id"], selected_lesson_name, ex_data["id"], "VIEW_HINT", 1, "N/A", "Xem nấc 1")
        with c_h2:
            if st.button("🔍 Mở Gợi Ý Nấc 2", key=f"h2_{ex_data['id']}", use_container_width=True):
                st.warning(f"**Gợi ý nấc 2 (Bước biến đổi trung gian):**\n\n{ex_data['hint_2']}")
                log_activity_to_db(student_info["student_id"], selected_lesson_name, ex_data["id"], "VIEW_HINT", 2, "N/A", "Xem nấc 2")
        with c_h3:
            if st.button("🎯 Mở Gợi Ý Nấc 3", key=f"h3_{ex_data['id']}", use_container_width=True):
                st.error(f"**Gợi ý nấc 3 (Định hướng kết quả):**\n\n{ex_data['hint_3']}")
                log_activity_to_db(student_info["student_id"], selected_lesson_name, ex_data["id"], "VIEW_HINT", 3, "N/A", "Xem nấc 3")

        st.markdown("---")
        col_act1, col_act2 = st.columns(2)
        with col_act1:
            if st.button("✅ Em đã tự giải xong bài tập này! (+2 hoa)", key=f"solve_{ex_data['id']}", use_container_width=True):
                reward_student_flower(student_info["student_id"], 2, "tự lực hoàn thành bài tập SGK")
                log_activity_to_db(student_info["student_id"], selected_lesson_name, ex_data["id"], "SELF_SOLVED", 0, "TRUE", "Tự giải SGK")
        with col_act2:
            if st.button("🔄 Thử sức 01 bài tập tương tự (AI tạo)", key=f"gen_{ex_data['id']}", use_container_width=True):
                with st.spinner("AI đang sinh bài tập tương đương cùng dạng..."):
                    if client:
                        try:
                            prompt_sim = f"Bạn là giáo viên Toán. Từ bài tập sau: '{ex_data['content']}', hãy tạo 1 bài toán TƯƠNG TỰ CÙNG DẠNG nhưng thay đổi số liệu hoặc tên gọi. Chỉ xuất đề bài và câu hỏi gợi mở, tuyệt đối không đưa lời giải trọn gói."
                            res_sim = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_sim)
                            sim_text = res_sim.text
                        except Exception:
                            sim_text = "Cho góc x thỏa mãn pi < x < 3pi/2 và cos(x) = -5/13. Hãy tính sin(x) và tan(x)."
                    else:
                        sim_text = "Bài toán tương tự: Cho góc alpha thỏa mãn 0 < alpha < pi/2 và sin(alpha) = 4/5. Hãy tính cos(alpha) và tan(alpha)."
                    st.info(f"**Bài tập tương tự do AI sinh:**\n\n{sim_text}")
                    log_activity_to_db(student_info["student_id"], selected_lesson_name, ex_data["id"], "GEN_SIMILAR", 0, "N/A", "Luyện bài tương tự")

        # NÚT CHUYỂN TIẾP CỨU TRỢ SƯ PHẠM (HUMAN-IN-THE-LOOP)
        st.markdown("---")
        with st.expander("❓ Xem hết 3 nấc gợi ý vẫn chưa hiểu? Gửi câu hỏi lên Thầy/Cô"):
            st.caption("Nếu điểm nghẽn nhận thức quá sâu, em hãy gửi ghi chú này lên lớp để Thầy/Cô giải đáp trực tiếp nhé!")
            st_note = st.text_input("Ghi rõ điểm em chưa hiểu (ví dụ: Em chưa rõ vì sao góc phần tư thứ II cos lại âm):", key=f"note_{ex_data['id']}")
            if st.button("📩 [Gửi câu hỏi bế tắc này về Hộp thư Thầy/Cô]", key=f"btn_send_{ex_data['id']}"):
                send_question_inbox(student_info["student_id"], student_info["full_name"], selected_lesson_name, ex_data["id"], st_note)
                st.success("✅ Đã chuyển tiếp thắc mắc thành công! Thầy/Cô bộ môn sẽ giải đáp trực tiếp cho em trên lớp.")
                # Cơ chế 2 lần hỏi nghiêm túc = +1 hoa
                user_questions = [q for q in st.session_state["inbox_db"] if q["student_id"] == student_info["student_id"]]
                if len(user_questions) % 2 == 0:
                    reward_student_flower(student_info["student_id"], 1, "gửi đủ 2 câu hỏi bế tắc nghiêm túc cho Thầy/Cô")
                else:
                    st.info("💡 Em đã tích lũy 1/2 chặng đường hỏi bài. Tiếp tục nỗ lực tự suy nghĩ nhé!")

# ------------------------------------------------------------------------------
# TAB 3: TRỢ LÝ AI: SOI BÀI VỞ & TỐI ƯU ÂM THANH MIC/LOA
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("💬 Gia Sư AI: Soi Bài Viết Tay & Lời Khuyên Giọng Nói")
    st.caption(f"Trợ lý AI đang sẵn sàng hỗ trợ nội dung: {selected_lesson_name}")

    input_mode = st.radio("Phương thức hỏi bài:", ["📸 Chụp vở nháp qua Camera", "🎙️ Hỏi qua Mic", "✍️ Nhập văn bản"], horizontal=True)

    img_captured = None
    audio_captured = None
    text_query = ""

    if input_mode == "📸 Chụp vở nháp qua Camera":
        cam_file = st.camera_input("Chụp trang vở nháp bài làm của em:")
        if cam_file:
            img_captured = Image.open(cam_file)
            img_captured.thumbnail((1024, 1024))
    elif input_mode == "🎙️ Hỏi qua Mic":
        mic_file = st.audio_input("Nói trực tiếp thắc mắc của em:")
        if mic_file:
            audio_captured = mic_file.read()
    else:
        text_query = st.text_area("Gõ câu hỏi hoặc bài toán em đang vướng mắc:")

    if st.button("🚀 Gửi bài nhờ Gia sư AI chữa", key="btn_check_ai"):
        with st.spinner("AI đang phân tích và tìm vị trí điểm nghẽn..."):
            pedagogy_prompt = f"""
            Bạn là Gia sư dạy Toán THPT bám sát SGK Kết nối tri thức.
            Bài học hiện tại: {selected_lesson_name} ({selected_grade}).
            Học sinh: {student_info['full_name']} (Lỗ hổng thường gặp: {student_info.get('weak_spots')}).

            QUY TẮC BẮT BUỘC:
            1. KHÔNG giải hộ trọn gói. Hãy chỉ ra dòng làm đúng, khoanh vùng vị trí sai lầm và đặt câu hỏi gợi mở để học sinh tự sửa.
            2. CHIA RÕ 2 PHẦN THEO ĐÚNG CẤU TRÚC SAU:
            ---PHẦN HIỂN THỊ MÀN HÌNH---
            (Trình bày chi tiết, chuẩn sư phạm, dùng LaTeX trong dấu $ để hiển thị công thức đẹp).
            ---PHẦN LỜI THOẠI PHÁT LOA---
            (Chỉ viết 2 đến 3 câu ngắn gọn, ấm áp, khích lệ tinh thần. TUYỆT ĐỐI KHÔNG CHỨA CÔNG THỨC TOÁN, KHÔNG CHỨA KÝ HIỆU LATEX để loa đọc tự nhiên).
            """
            raw_reply = ""
            if client:
                try:
                    if img_captured:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[pedagogy_prompt, img_captured])
                        reward_student_flower(student_info["student_id"], 1, "chụp ảnh vở nháp hỏi bài học tập")
                    elif audio_captured:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[pedagogy_prompt, {"mime_type": "audio/wav", "data": audio_captured}])
                    else:
                        res = client.models.generate_content(model="gemini-2.5-flash", contents=[pedagogy_prompt, f"Câu hỏi của học sinh: {text_query}"])
                    raw_reply = res.text
                except Exception:
                    raw_reply = "---PHẦN HIỂN THỊ MÀN HÌNH---\nEm đã thực hiện đúng bước đại số cơ bản. Hãy kiểm tra lại điều kiện dấu của góc lượng giác nhé!\n---PHẦN LỜI THOẠI PHÁT LOA---\nThầy cô đã xem bài của em, hãy chú ý điều kiện xét dấu trên màn hình nhé!"
            else:
                raw_reply = "---PHẦN HIỂN THỊ MÀN HÌNH---\nEm đã làm đúng các bước biến đổi đầu tiên. Hãy chú ý khoảng xác định của góc để lấy dấu chính xác.\n---PHẦN LỜI THOẠI PHÁT LOA---\nCác bước làm rất tốt, em hãy kiểm tra lại dấu như hướng dẫn nhé!"

            disp_text = raw_reply
            voice_text = "Thầy cô đã xem bài của em. Hãy xem kỹ hướng dẫn trên màn hình nhé!"
            if "---PHẦN HIỂN THỊ MÀN HÌNH---" in raw_reply and "---PHẦN LỜI THOẠI PHÁT LOA---" in raw_reply:
                p = raw_reply.split("---PHẦN LỜI THOẠI PHÁT LOA---")
                disp_text = p[0].replace("---PHẦN HIỂN THỊ MÀN HÌNH---", "").strip()
                voice_text = p[1].strip()

            with st.container(border=True):
                st.markdown(disp_text)

            try:
                tts = gTTS(text=voice_text, lang='vi', slow=False)
                tts.save("voice_reply.mp3")
                st.markdown("🔊 **Lời Nhắn Nhủ Bằng Giọng Nói Từ Gia Sư AI:**")
                st.audio("voice_reply.mp3", format="audio/mp3")
            except Exception:
                pass

# ------------------------------------------------------------------------------
# TAB 4: PHÒNG KHẢO THÍ & LUYỆN ĐỀ CHUẨN HÓA (ĐẦY ĐỦ CÁC KỲ & PHÂN HÓA LỚP 12)
# ------------------------------------------------------------------------------
with tab4:
    st.subheader(f"🎯 Phòng Luyện Đề Chuẩn Hóa Khảo Thí ({selected_grade})")
    st.caption("Kho đề thi chuẩn hóa trích xuất tức thì (< 0.5s), bám sát định dạng khảo thí mới nhất.")

    grade_exams = EXAM_BANK.get(selected_grade, {})
    exam_choices = list(grade_exams.keys())

    selected_exam_type = st.selectbox("Chọn Kì Thi / Bài Kiểm Tra:", exam_choices)
    exam_content = grade_exams[selected_exam_type]

    with st.container(border=True):
        st.markdown(f"### 📋 {exam_content['title']}")
        st.caption("Thời gian làm bài tiêu chuẩn: 45 - 90 phút. Hệ thống tự động chấm điểm và quy đổi Bông hoa Tri thức.")

        # PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN
        st.markdown("#### PHẦN I: Câu trắc nghiệm nhiều phương án lựa chọn (A, B, C, D)")
        user_p1_answers = {}
        for idx, item in enumerate(exam_content.get("p1", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            user_p1_answers[idx] = st.radio(f"Chọn đáp án câu {idx + 1}:", item["ops"], key=f"p1_{selected_exam_type}_{idx}")

        # PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI
        st.markdown("#### PHẦN II: Câu trắc nghiệm Đúng / Sai (Định dạng mới 4 ý a-b-c-d)")
        user_p2_answers = {}
        for idx, item in enumerate(exam_content.get("p2", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            sub_ans = []
            for s_idx, (st_text, _) in enumerate(item["items"]):
                c_opt = st.radio(f"{st_text}", ["Chưa chọn", "Đúng", "Sai"], horizontal=True, key=f"p2_{selected_exam_type}_{idx}_{s_idx}")
                sub_ans.append(c_opt)
            user_p2_answers[idx] = sub_ans

        # PHẦN III: TRẢ LỜI NGẮN (ĐIỀN SỐ)
        st.markdown("#### PHẦN III: Câu trắc nghiệm trả lời ngắn (Điền giá trị số thực tế)")
        user_p3_answers = {}
        for idx, item in enumerate(exam_content.get("p3", [])):
            st.markdown(f"**Câu {idx + 1}:** {item['q']}")
            user_p3_answers[idx] = st.text_input(f"Đáp số của em (chỉ điền số):", key=f"p3_{selected_exam_type}_{idx}")

        st.markdown("---")
        if st.button("📤 Nộp Bài Khảo Thí & Chấm Điểm Tức Thì", use_container_width=True):
            score = 0.0
            total_points = 10.0

            # Tính điểm Phần I (3.0 điểm)
            p1_correct = 0
            p1_list = exam_content.get("p1", [])
            for idx, item in enumerate(p1_list):
                if user_p1_answers[idx].startswith(item["ans"]):
                    p1_correct += 1
            score += (p1_correct / max(1, len(p1_list))) * 3.0

            # Tính điểm Phần II (4.0 điểm)
            p2_correct_items = 0
            total_p2_items = 0
            for idx, item in enumerate(exam_content.get("p2", [])):
                for s_idx, (_, is_true) in enumerate(item["items"]):
                    total_p2_items += 1
                    user_ch = user_p2_answers[idx][s_idx]
                    if (user_ch == "Đúng" and is_true) or (user_ch == "Sai" and not is_true):
                        p2_correct_items += 1
            score += (p2_correct_items / max(1, total_p2_items)) * 4.0

            # Tính điểm Phần III (3.0 điểm)
            p3_correct = 0
            p3_list = exam_content.get("p3", [])
            for idx, item in enumerate(p3_list):
                u_ans = user_p3_answers[idx].strip().replace(",", ".")
                target_ans = item["ans"].strip().replace(",", ".")
                try:
                    if abs(float(u_ans) - float(target_ans)) < 0.15:
                        p3_correct += 1
                except Exception:
                    if u_ans == target_ans:
                        p3_correct += 1
            score += (p3_correct / max(1, len(p3_list))) * 3.0
            score = round(score, 1)

            st.balloons()
            st.success(f"🎉 **KẾT QUẢ KHẢO THÍ CỦA EM:** **{score} / 10.0 Điểm**")

            # Quy chế thưởng hoa theo khảo thí
            if score >= 10.0:
                reward_student_flower(student_info["student_id"], 3, f"đạt điểm tuyệt đối 10.0 ở {selected_exam_type}")
            elif score >= 9.0:
                reward_student_flower(student_info["student_id"], 2, f"đạt điểm xuất sắc {score} ở {selected_exam_type}")
            elif score >= 8.0:
                reward_student_flower(student_info["student_id"], 1, f"vượt ải thành công với {score} điểm ở {selected_exam_type}")
            else:
                st.info("💡 Điểm số chưa đạt mốc thưởng (8.0+). Em hãy xem lại các câu chưa chính xác và thử sức lại nhé!")

            log_activity_to_db(student_info["student_id"], selected_exam_type, "EXAM_SUBMIT", "TEST", 0, str(score), f"Điểm số: {score}")

            with st.expander("🔍 Xem Lời Giải Chi Tiết Và Bảng Đáp Án Chuẩn"):
                for idx, item in enumerate(exam_content.get("p1", [])):
                    st.markdown(f"- **Phần I - Câu {idx+1}:** Đáp án đúng là **{item['ans']}**. {item['exp']}")
                for idx, item in enumerate(exam_content.get("p3", [])):
                    st.markdown(f"- **Phần III - Câu {idx+1}:** Đáp số đúng là **{item['ans']}**. Hướng dẫn: {item['exp']}")
