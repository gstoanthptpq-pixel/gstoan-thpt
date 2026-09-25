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
# 1. CẤU HÌNH GIAO DIỆN & THANH CUỘN CHUYÊN DỤNG CHO CHỦ ĐIỂM
# ==============================================================================
st.set_page_config(
    page_title="GSToán - Hệ Sinh Thái Tự Học Toán THPT",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Thanh cuộn mượt cho Dropdown danh sách bài học và chủ điểm */
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
    .example-card {
        background-color: #FFFFFF;
        border-left: 4px solid #2563EB;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 10px;
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
# 3. KHO HỌC LIỆU SỐ BÁM SÁT VỞ TỰ HỌC: PHÂN TÁCH THEO CHỦ ĐIỂM KIẾN THỨC
# ==============================================================================
CURRICULUM_DATA = {
    "Khối 10": {
        "Bài 1: Mệnh đề toán học": {
            "chapter": "Chương I: Mệnh đề và tập hợp",
            "topics": {
                "Chủ điểm 1: Khái niệm mệnh đề và mệnh đề chứa biến": {
                    "theory": "Mệnh đề toán học là một câu khẳng định có chân giá trị hoặc Đúng hoặc Sai, không thể vừa đúng vừa sai. Mệnh đề chứa biến là câu khẳng định chứa biến số, chưa xác định đúng sai cho đến khi thay giá trị cụ thể.",
                    "formula": r"P \in \{\text{Đúng}, \text{Sai}\}; \quad P(x): \text{Mệnh đề chứa biến } x",
                    "trap": "Các câu hỏi, câu cảm thán hoặc mệnh đề chứa biến chưa gán giá trị thì không phải là mệnh đề toán học.",
                    "audio": "Mệnh đề toán học là một khẳng định chắc chắn đúng hoặc chắc chắn sai. Câu hỏi hay câu cảm thán không phải mệnh đề toán học.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Phân biệt câu là mệnh đề toán học",
                            "problem": "Trong các câu sau, câu nào là mệnh đề toán học? Xét tính đúng sai của nó: a) 15 là số nguyên tố; b) Hôm nay trời đẹp quá!",
                            "solution": "a) '15 là số nguyên tố' là mệnh đề toán học. Mệnh đề này Sai vì 15 chia hết cho 3 và 5.\nb) 'Hôm nay trời đẹp quá!' là câu cảm thán, không phải mệnh đề toán học."
                        },
                        {
                            "title": "Ví dụ 2: Xác định chân giá trị mệnh đề chứa biến",
                            "problem": "Cho mệnh đề chứa biến $P(n)$: '$n^2 - 1$ chia hết cho 4'. Xét tính đúng sai của $P(3)$ và $P(4)$.",
                            "solution": "- Với $n = 3$: $3^2 - 1 = 8$ chia hết cho 4, suy ra $P(3)$ là mệnh đề Đúng.\n- Với $n = 4$: $4^2 - 1 = 15$ không chia hết cho 4, suy ra $P(4)$ là mệnh đề Sai."
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
                    "theory": "Mệnh đề phủ định của P ký hiệu là P ngang, đúng khi P sai và sai khi P đúng. Phủ định của lượng từ 'với mọi' là 'tồn tại', phủ định của dấu '>' là '<='.",
                    "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}; \quad \overline{\exists x \in X, P(x)} \iff \forall x \in X, \overline{P(x)}",
                    "trap": "Phủ định của dấu lớn hơn (>) bắt buộc phải là dấu nhỏ hơn hoặc bằng (<=), không được bỏ quên dấu bằng.",
                    "audio": "Khi lấy phủ định của mệnh đề chứa lượng từ với mọi, ta đổi thành tồn tại. Nhớ rằng phủ định của dấu lớn hơn là nhỏ hơn hoặc bằng.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Lập mệnh đề phủ định thông thường",
                            "problem": "Lập mệnh đề phủ định của mệnh đề $P$: 'Số 12 chia hết cho 5' và xét tính đúng sai.",
                            "solution": "Mệnh đề phủ định là $\\overline{P}$: 'Số 12 không chia hết cho 5'. Vì $P$ sai nên $\\overline{P}$ là mệnh đề Đúng."
                        },
                        {
                            "title": "Ví dụ 2: Phủ định mệnh đề chứa lượng từ với mọi",
                            "problem": "Lập mệnh đề phủ định của $Q$: '$\\forall x \\in \\mathbb{R}, x^2 + 1 > 0$'.",
                            "solution": "Phủ định của lượng từ $\\forall$ là $\\exists$, phủ định của $>$ là $\\le$.\nVậy $\\overline{Q}$: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$'. Mệnh đề $\\overline{Q}$ nhận chân giá trị Sai vì $x^2 + 1 \\ge 1 > 0$ với mọi $x$."
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
        },
        "Bài 2: Tập hợp và các phép toán trên tập hợp": {
            "chapter": "Chương I: Mệnh đề và tập hợp",
            "topics": {
                "Chủ điểm 1: Các phép toán giao, hợp, hiệu của hai tập hợp": {
                    "theory": "Giao của hai tập hợp lấy phần tử chung. Hợp lấy tất cả phần tử thuộc ít nhất một trong hai tập hợp. Hiệu A trừ B lấy phần tử thuộc A nhưng không thuộc B.",
                    "formula": r"A \cap B = \{x \mid x \in A \text{ và } x \in B\}; \quad A \cup B = \{x \mid x \in A \text{ hoặc } x \in B\}; \quad A \setminus B = \{x \mid x \in A \text{ và } x \notin B\}",
                    "trap": "Phân biệt rõ ngoặc đơn (khoảng) và ngoặc vuông (đoạn) khi làm việc với các tập con của số thực.",
                    "audio": "Giao là lấy phần tử chung, hợp là gộp tất cả phần tử, hiệu A trừ B là thuộc A nhưng bỏ đi phần tử thuộc B.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm giao, hợp, hiệu của hai tập hợp rời rạc",
                            "problem": "Cho hai tập hợp $A = \\{1; 2; 3; 4\\}$ và $B = \\{3; 4; 5; 6\\}$. Hãy xác định $A \\cap B$, $A \\cup B$, và $A \\setminus B$.",
                            "solution": "- Giao: Các phần tử chung là 3 và 4 $\\Rightarrow A \\cap B = \\{3; 4\\}$.\n- Hợp: Gộp tất cả phần tử $\\Rightarrow A \\cup B = \\{1; 2; 3; 4; 5; 6\\}$.\n- Hiệu: Các phần tử thuộc $A$ nhưng không thuộc $B$ $\\Rightarrow A \\setminus B = \\{1; 2\\}$."
                        },
                        {
                            "title": "Ví dụ 2: Các phép toán trên khoảng và đoạn số thực",
                            "problem": "Cho $A = [-2; 3]$ và $B = (1; 5)$. Xác định tập hợp $A \\cap B$ và $A \\cup B$.",
                            "solution": "- Biểu diễn trên trục số:\n- Giao là phần chung: $A \\cap B = (1; 3]$.\n- Hợp là phần phủ toàn bộ: $A \\cup B = [-2; 5)$."
                        }
                    ],
                    "exercise": {
                        "id": "10_B2_CD1",
                        "title": "Bài tập kiểm minh chứng: Giao tập hợp",
                        "content": "Cho A = [1; 5] và B = (3; 7). Số nguyên thuộc tập hợp A giao B gồm bao nhiêu số?",
                        "type": "NUMERIC", "target": "2", "options": []
                    }
                }
            }
        },
        "Bài 3: Hệ thức lượng trong tam giác": {
            "chapter": "Chương III: Hệ thức lượng trong tam giác",
            "topics": {
                "Chủ điểm 1: Định lý Côsin và Định lý Sin": {
                    "theory": "Định lý Côsin dùng tính cạnh thứ ba khi biết 2 cạnh và góc xen giữa. Định lý Sin tính cạnh và bán kính R đường tròn ngoại tiếp khi biết 1 cạnh và góc đối.",
                    "formula": r"a^2 = b^2 + c^2 - 2bc \cos A; \quad \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R",
                    "trap": "Khi tính góc qua hệ quả định lý Côsin, nếu cos A < 0 thì góc A là góc tù (lớn hơn 90 độ).",
                    "audio": "Biết hai cạnh và góc xen giữa dùng định lý Côsin. Biết một cạnh và góc đối dùng định lý Sin.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính cạnh tam giác bằng định lý Côsin",
                            "problem": "Cho tam giác $ABC$ có $b = 8$, $c = 5$ và góc $\\widehat{A} = 60^\\circ$. Tính cạnh $a$.",
                            "solution": "Áp dụng định lý Côsin:\n$$a^2 = b^2 + c^2 - 2bc \\cos A = 8^2 + 5^2 - 2 \\cdot 8 \\cdot 5 \\cdot \\cos 60^\\circ$$\n$$a^2 = 64 + 25 - 40 = 49 \\Rightarrow a = 7$$."
                        },
                        {
                            "title": "Ví dụ 2: Tính bán kính đường tròn ngoại tiếp bằng định lý Sin",
                            "problem": "Cho tam giác $ABC$ có cạnh $a = 7$ và góc $\\widehat{A} = 60^\\circ$. Tính bán kính $R$ của đường tròn ngoại tiếp tam giác.",
                            "solution": "Áp dụng định lý Sin:\n$$\\frac{a}{\\sin A} = 2R \\Rightarrow R = \\frac{a}{2\\sin A} = \\frac{7}{2\\sin 60^\\circ} = \\frac{7}{2 \\cdot \\frac{\\sqrt{3}}{2}} = \\frac{7\\sqrt{3}}{3}$$."
                        }
                    ],
                    "exercise": {
                        "id": "10_B3_CD1",
                        "title": "Bài tập kiểm minh chứng: Định lý Côsin",
                        "content": "Cho tam giác ABC có b = 6, c = 4 và góc A = 60 độ. Cạnh a^2 bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "28", "options": []
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
                    "theory": "Trục tung là trục sin, trục hoành là trục cos. Khẩu quyết: Nhất cả (I: all > 0), Nhì sin (II: sin > 0, cos < 0), Tam tang (III: tan, cot > 0), Tứ cos (IV: cos > 0, sin < 0).",
                    "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad \tan\alpha = \frac{\sin\alpha}{\cos\alpha}; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
                    "trap": "Khi khai căn bậc hai để tìm cos từ sin, bắt buộc phải căn cứ vào góc phần tư để đặt dấu âm hay dương.",
                    "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Luôn kiểm tra kỹ góc phần tư để lấy dấu âm dương khi khai căn.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính giá trị lượng giác khi biết sin và góc phần tư thứ II",
                            "problem": "Cho góc $\\alpha$ thỏa mãn $\\frac{\\pi}{2} < \\alpha < \\pi$ và $\\sin\\alpha = \\frac{3}{5}$. Hãy tính $\\cos\\alpha$ và $\\tan\\alpha$.",
                            "solution": "Ta có:\n$$\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\left(\\frac{3}{5}\\right)^2 = \\frac{16}{25}$$\nVì $\\frac{\\pi}{2} < \\alpha < \\pi$ (góc phần tư thứ II) nên $\\cos\\alpha < 0$.\nDo đó: $\\cos\\alpha = -\\sqrt{\\frac{16}{25}} = -\\frac{4}{5} = -0.8$.\nSuy ra: $\\tan\\alpha = \\frac{\\sin\\alpha}{\\cos\\alpha} = \\frac{3/5}{-4/5} = -\\frac{3}{4} = -0.75$."
                        },
                        {
                            "title": "Ví dụ 2: Tính giá trị lượng giác khi biết cos ở góc phần tư thứ IV",
                            "problem": "Cho $\\cos\\alpha = \\frac{5}{13}$ với $\\frac{3\\pi}{2} < \\alpha < 2\\pi$. Tính giá trị của $\\sin\\alpha$.",
                            "solution": "Ta có $\\sin^2\\alpha = 1 - \\cos^2\\alpha = 1 - \\frac{25}{169} = \\frac{144}{169}$.\nVì $\\alpha$ thuộc góc phần tư thứ IV nên $\\sin\\alpha < 0$.\nVậy $\\sin\\alpha = -\\sqrt{\\frac{144}{169}} = -\\frac{12}{13}$."
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
        },
        "Bài 2: Cấp số cộng": {
            "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
            "topics": {
                "Chủ điểm 1: Số hạng tổng quát và Công sai của cấp số cộng": {
                    "theory": "Cấp số cộng là dãy số có số hạng sau bằng số hạng trước cộng công sai d không đổi. Số hạng tổng quát un bằng u1 cộng (n-1)d.",
                    "formula": r"u_n = u_1 + (n - 1)d; \quad S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n - 1)d]}{2}",
                    "trap": "Khi tính tổng Sn, chú ý công thức có chia 2 và nhân với số lượng phần tử n.",
                    "audio": "Số hạng thứ n bằng số hạng đầu cộng n trừ 1 nhân công sai d. Tổng n số hạng đầu bằng n nhân tổng số hạng đầu và số hạng cuối chia 2.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm số hạng và công sai của cấp số cộng",
                            "problem": "Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 3$ và công sai $d = 4$. Hãy tìm số hạng thứ 10 ($u_{10}$).",
                            "solution": "Áp dụng công thức số hạng tổng quát:\n$$u_{10} = u_1 + (10 - 1)d = 3 + 9 \\cdot 4 = 3 + 36 = 39$$."
                        },
                        {
                            "title": "Ví dụ 2: Tính tổng n số hạng đầu tiên",
                            "problem": "Tính tổng 20 số hạng đầu của cấp số cộng $(u_n)$ biết $u_1 = 2$ và công sai $d = 3$.",
                            "solution": "Áp dụng công thức tổng $S_n$:\n$$S_{20} = \\frac{20 \\cdot [2 \\cdot 2 + (20 - 1) \\cdot 3]}{2} = 10 \\cdot [4 + 57] = 10 \\cdot 61 = 610$$."
                        }
                    ],
                    "exercise": {
                        "id": "11_B2_CD1",
                        "title": "Bài tập kiểm minh chứng: Số hạng cấp số cộng",
                        "content": "Cho cấp số cộng có u1 = 3, d = 4. Số hạng thứ 5 (u5) bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "19", "options": []
                    }
                }
            }
        },
        "Bài 3: Đường thẳng vuông góc với mặt phẳng": {
            "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
            "topics": {
                "Chủ điểm 1: Chứng minh đường thẳng vuông góc mặt phẳng & Góc đường và mặt": {
                    "theory": "Đường thẳng vuông góc với mặt phẳng khi nó vuông góc với 2 đường thẳng cắt nhau trong mặt phẳng đó. Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng và hình chiếu vuông góc của nó.",
                    "formula": r"\begin{cases} d \perp a, \ d \perp b \subset (P) \\ a \cap b = I \end{cases} \Rightarrow d \perp (P); \quad \varphi = \widehat{(d, (P))} = \widehat{(d, d')}",
                    "trap": "Chỉ kết luận đường thẳng vuông góc mặt phẳng khi nó vuông góc với HAI ĐƯỜNG CẮT NHAU, không được là hai đường song song.",
                    "audio": "Muốn chứng minh đường thẳng vuông góc mặt phẳng, hãy chỉ ra nó vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng đó.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Chứng minh đường thẳng vuông góc mặt phẳng",
                            "problem": "Cho hình chóp $S.ABC$ có đáy $ABC$ vuông tại $B$, cạnh bên $SA \\perp (ABC)$. Chứng minh rằng $BC \\perp (SAB)$.",
                            "solution": "- Do tam giác $ABC$ vuông tại $B$ nên $BC \\perp AB$ (1).\n- Do $SA \\perp (ABC)$ mà $BC \\subset (ABC)$ nên $BC \\perp SA$ (2).\n- Từ (1) và (2), nhận thấy $BC$ vuông góc với hai đường thẳng cắt nhau $AB$ và $SA$ trong $(SAB)$.\nVậy $BC \\perp (SAB)$."
                        },
                        {
                            "title": "Ví dụ 2: Xác định góc giữa đường thẳng và mặt phẳng đáy",
                            "problem": "Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, đáy là tam giác vuông cân tại $B$ có $AB = a$. Biết $SA = a$. Tính góc giữa cạnh bên $SB$ và mặt phẳng đáy $(ABC)$.",
                            "solution": "- Hình chiếu vuông góc của điểm $S$ lên mặt đáy $(ABC)$ là điểm $A$ (do $SA \\perp (ABC)$).\n- Hình chiếu của điểm $B$ là chính nó.\n- Do đó, hình chiếu vuông góc của đường thẳng $SB$ lên mặt đáy $(ABC)$ là đoạn thẳng $AB$.\n- Góc cần tìm là $\\widehat{SBA}$.\n- Xét tam giác vuông $SAB$ vuông tại $A$: có $SA = AB = a$ (tam giác vuông cân), suy ra $\\widehat{SBA} = 45^\\circ$."
                        }
                    ],
                    "exercise": {
                        "id": "11_B3_CD1",
                        "title": "Bài tập kiểm minh chứng: Góc đường thẳng và mặt đáy",
                        "content": "Cho hình chóp S.ABC có SA vuông góc đáy, SA = a, AB = a. Góc giữa SB và đáy bằng bao nhiêu độ?",
                        "type": "NUMERIC", "target": "45", "options": []
                    }
                }
            }
        }
    },
    "Khối 12": {
        "Bài 1: Tính đơn điệu và cực trị của hàm số": {
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "topics": {
                "Chủ điểm 1: Xét tính đồng biến, nghịch biến của hàm số": {
                    "theory": "Hàm số f(x) đồng biến trên K khi đạo hàm f'(x) >= 0 với mọi x thuộc K; nghịch biến khi f'(x) <= 0. Đạo hàm bằng 0 tại hữu hạn điểm.",
                    "formula": r"f'(x) \ge 0, \ \forall x \in K \ (\text{Đồng biến}); \quad f'(x) \le 0, \ \forall x \in K \ (\text{Nghịch biến})",
                    "trap": "Dấu ngoặc kết luận khoảng đồng biến: dùng từ 'và' hoặc dấu phẩy, tuyệt đối không dùng ký hiệu hợp (U).",
                    "audio": "Hàm số đồng biến khi y phẩy lớn hơn hoặc bằng không, nghịch biến khi y phẩy nhỏ hơn hoặc bằng không. Luôn kết luận trên từng khoảng riêng biệt.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm các khoảng đơn điệu của hàm số bậc ba",
                            "problem": "Tìm các khoảng đồng biến và nghịch biến của hàm số $y = x^3 - 3x^2 + 2$.",
                            "solution": "1. Tập xác định: $D = \\mathbb{R}$.\n2. Tính đạo hàm: $y' = 3x^2 - 6x = 3x(x - 2)$.\n3. Cho $y' = 0 \\iff x = 0$ hoặc $x = 2$.\n4. Xét dấu $y'$: Trong khoảng $(0; 2)$ đạo hàm $y' < 0$; ngoài khoảng đạo hàm $y' > 0$.\nVậy hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên khoảng $(0; 2)$."
                        },
                        {
                            "title": "Ví dụ 2: Tìm các khoảng đơn điệu của hàm phân thức bậc nhất trên bậc nhất",
                            "problem": "Xét tính đơn điệu của hàm số $y = \\frac{2x - 1}{x + 1}$.",
                            "solution": "1. Tập xác định: $D = \\mathbb{R} \\setminus \\{-1\\}$.\n2. Tính đạo hàm:\n$$y' = \\frac{2 \\cdot 1 - (-1) \\cdot 1}{(x + 1)^2} = \\frac{3}{(x + 1)^2} > 0, \\quad \\forall x \\neq -1$$\n3. Kết luận: Hàm số đồng biến trên từng khoảng xác định $(-\\infty; -1)$ và $(-1; +\\infty)$."
                        }
                    ],
                    "exercise": {
                        "id": "12_B1_CD1",
                        "title": "Bài tập kiểm minh chứng: Đơn điệu hàm số",
                        "content": "Hàm số y = x^3 - 3x nghịch biến trên khoảng (a; 1). Giá trị của a bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "-1", "options": []
                    }
                },
                "Chủ điểm 2: Tìm cực trị của hàm số": {
                    "theory": "Điểm x0 là điểm cực đại nếu đạo hàm đổi dấu từ dương sang âm khi qua x0. Điểm x0 là điểm cực tiểu nếu đạo hàm đổi dấu từ âm sang dương.",
                    "formula": r"f'(x_0) = 0; \quad (+) \to (-) \ (\text{Cực đại}); \quad (-) \to (+) \ (\text{Cực tiểu})",
                    "trap": "Phân biệt rõ: 'Điểm cực trị của hàm số' là x0, còn 'Giá trị cực trị' là y0 = f(x0).",
                    "audio": "Điểm cực trị là hoành độ x không, giá trị cực trị là tung độ y không bằng f của x không. Hãy phân biệt rõ khi đọc yêu cầu đề thi.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm điểm cực trị và giá trị cực trị của hàm số",
                            "problem": "Tìm tọa độ các điểm cực trị của đồ thị hàm số $y = x^3 - 3x + 2$.",
                            "solution": "1. Tính đạo hàm: $y' = 3x^2 - 3 = 3(x^2 - 1) = 0 \\iff x = 1$ hoặc $x = -1$.\n2. Bảng xét dấu $y'$:\n- Qua $x = -1$, $y'$ đổi dấu từ $(+)$ sang $(-)$ $\\Rightarrow x = -1$ là điểm cực đại, giá trị $y_{CĐ} = (-1)^3 - 3(-1) + 2 = 4$.\n- Qua $x = 1$, $y'$ đổi dấu từ $(-)$ sang $(+)$ $\\Rightarrow x = 1$ là điểm cực tiểu, giá trị $y_{CT} = 1^3 - 3(1) + 2 = 0$.\nVậy điểm cực đại của đồ thị là $A(-1; 4)$, điểm cực tiểu của đồ thị là $B(1; 0)$."
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
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "topics": {
                "Chủ điểm 1: Tìm GTLN và GTNN của hàm số trên một đoạn [a; b]": {
                    "theory": "Tính đạo hàm f'(x), tìm các nghiệm xi thuộc khoảng (a; b). Tính giá trị f(a), f(b), f(xi). Số lớn nhất trong các giá trị đó là GTLN, số nhỏ nhất là GTNN.",
                    "formula": r"\max_{[a; b]} f(x) = \max\{f(a), f(b), f(x_i)\}; \quad \min_{[a; b]} f(x) = \min\{f(a), f(b), f(x_i)\}",
                    "trap": "Chỉ lấy các nghiệm xi NẰM TRONG khoảng (a; b). Nghiệm nằm ngoài đoạn bắt buộc phải loại bỏ.",
                    "audio": "Trên một đoạn, không cần lập bảng biến thiên, chỉ cần tính giá trị tại hai đầu mút và tại các điểm đạo hàm bằng không rồi so sánh.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm GTLN, GTNN trên đoạn",
                            "problem": "Tìm giá trị lớn nhất và nhỏ nhất của hàm số $f(x) = x^3 - 3x + 1$ trên đoạn $[0; 2]$.",
                            "solution": "1. Đạo hàm: $f'(x) = 3x^2 - 3 = 0 \\iff x = 1$ (nhận vì thuộc $(0; 2)$) hoặc $x = -1$ (loại vì không thuộc $(0; 2)$).\n2. Tính các giá trị:\n- $f(0) = 1$\n- $f(1) = 1^3 - 3(1) + 1 = -1$\n- $f(2) = 2^3 - 3(2) + 1 = 3$\n3. So sánh: $\\max_{[0; 2]} f(x) = f(2) = 3$ và $\\min_{[0; 2]} f(x) = f(1) = -1$."
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
            "chapter": "Chương I: Ứng dụng đạo hàm khảo sát hàm số",
            "topics": {
                "Chủ điểm 1: Tiệm cận đứng và Tiệm cận ngang": {
                    "theory": "Đường x = x0 là tiệm cận đứng nếu giới hạn của y khi x tiến tới x0 bằng vô cực. Đường y = y0 là tiệm cận ngang nếu giới hạn của y khi x tiến tới vô cực bằng y0.",
                    "formula": r"\lim_{x \to x_0^+} y = \pm\infty \Rightarrow x = x_0 \ (\text{TCĐ}); \quad \lim_{x \to \pm\infty} y = y_0 \Rightarrow y = y_0 \ (\text{TCN}); \quad y = \frac{ax+b}{cx+d} \Rightarrow y = \frac{a}{c}, \ x = -\frac{d}{c}",
                    "trap": "Hàm phân thức bậc nhất trên bậc nhất có tiệm cận đứng là x = -d/c và tiệm cận ngang là y = a/c. Tránh nhầm lẫn x và y.",
                    "audio": "Mẫu số triệt tiêu mà tử khác không cho ta tiệm cận đứng x bằng x không. Giới hạn tại vô cực cho ta tiệm cận ngang y bằng y không.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tìm tiệm cận của hàm phân thức bậc nhất trên bậc nhất",
                            "problem": "Tìm các đường tiệm cận đứng và tiệm cận ngang của đồ thị hàm số $y = \\frac{2x - 3}{x + 1}$.",
                            "solution": "1. Tiệm cận đứng:\nTa có $\\lim_{x \\to -1^+} \\frac{2x - 3}{x + 1} = -\\infty$ (do tử số tiến tới -5 < 0, mẫu số tiến tới 0+).\nSuy ra đường thẳng $x = -1$ là tiệm cận đứng.\n2. Tiệm cận ngang:\nTa có $\\lim_{x \\to \\pm\\infty} \\frac{2x - 3}{x + 1} = 2$.\nSuy ra đường thẳng $y = 2$ là tiệm cận ngang."
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
        },
        "Bài 4: Hệ trục tọa độ và Vectơ trong không gian": {
            "chapter": "Chương II: Vectơ và Hệ trục tọa độ trong không gian",
            "topics": {
                "Chủ điểm 1: Tọa độ vectơ, độ dài và tích vô hướng trong không gian": {
                    "theory": "Vectơ trong không gian phân tích qua 3 vectơ đơn vị i, j, k. Tích vô hướng bằng x1x2 + y1y2 + z1z2. Độ dài vectơ bằng căn bậc hai tổng bình phương các tọa độ.",
                    "formula": r"\vec{u} = (x; y; z) \iff \vec{u} = x\vec{i} + y\vec{j} + z\vec{k}; \quad |\vec{u}| = \sqrt{x^2 + y^2 + z^2}; \quad \vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2",
                    "trap": "Hai vectơ vuông góc khi và chỉ khi tích vô hướng bằng 0: x1x2 + y1y2 + z1z2 = 0.",
                    "audio": "Tọa độ vectơ trong không gian gồm hoành độ x, tung độ y và cao độ z. Tích vô hướng bằng tổng của ba tích tọa độ tương ứng.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính độ dài vectơ và tích vô hướng",
                            "problem": "Trong không gian $Oxyz$, cho hai vectơ $\\vec{u} = (2; -3; 6)$ và $\\vec{v} = (1; 2; 2)$. Tính độ dài $|\vec{u}|$ và tích vô hướng $\\vec{u} \\cdot \\vec{v}$.",
                            "solution": "- Độ dài vectơ $\\vec{u}$:\n$$|\\vec{u}| = \\sqrt{2^2 + (-3)^2 + 6^2} = \\sqrt{4 + 9 + 36} = \\sqrt{49} = 7$$.\n- Tích vô hướng:\n$$\\vec{u} \\cdot \\vec{v} = 2 \\cdot 1 + (-3) \\cdot 2 + 6 \\cdot 2 = 2 - 6 + 12 = 8$$."
                        }
                    ],
                    "exercise": {
                        "id": "12_B4_CD1",
                        "title": "Bài tập kiểm minh chứng: Độ dài vectơ Oxyz",
                        "content": "Trong không gian Oxyz, độ dài của vectơ a = (2; -3; 6) bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "7", "options": []
                    }
                }
            }
        },
        "Bài 5: Nguyên hàm và Tích phân": {
            "chapter": "Chương IV: Nguyên hàm và tích phân",
            "topics": {
                "Chủ điểm 1: Định nghĩa và tính chất của Tích phân": {
                    "theory": "Tích phân từ a đến b của f(x)dx bằng F(b) trừ F(a) theo định lý Newton - Leibniz. Tích phân không phụ thuộc vào ký hiệu biến số.",
                    "formula": r"\int_a^b f(x)dx = F(b) - F(a) = F(x)\Big|_a^b; \quad \int_a^b [f(x) \pm g(x)]dx = \int_a^b f(x)dx \pm \int_a^b g(x)dx",
                    "trap": "Cận tích phân đảo chiều thì đổi dấu: tích phân từ a đến b bằng trừ tích phân từ b đến a.",
                    "audio": "Tích phân từ a đến b của hàm số bằng F của b trừ F của a, trong đó F lớn là một nguyên hàm của hàm số đã cho.",
                    "examples": [
                        {
                            "title": "Ví dụ 1: Tính tích phân đa thức cơ bản",
                            "problem": "Tính tích phân $I = \\int_0^2 (2x + 1) dx$.",
                            "solution": "- Một nguyên hàm của hàm số $f(x) = 2x + 1$ là $F(x) = x^2 + x$.\n- Áp dụng công thức Newton - Leibniz:\n$$I = (x^2 + x)\\Big|_0^2 = (2^2 + 2) - (0^2 + 0) = (4 + 2) - 0 = 6$$."
                        }
                    ],
                    "exercise": {
                        "id": "12_B5_CD1",
                        "title": "Bài tập kiểm minh chứng: Tích phân",
                        "content": "Tích phân từ 0 đến 2 của (2x + 1)dx bằng bao nhiêu?",
                        "type": "NUMERIC", "target": "6", "options": []
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
            text=['B(7;6;5) Điểm'],
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
    st.markdown("<p style='text-align: center; color: #475569;'>Phân hóa kiến thức theo Chủ điểm bám sát Vở tự học (Khối 10, 11, 12)</p>", unsafe_allow_html=True)

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
# 9. PHÂN HỆ HỌC SINH (3 BẬC LỌC: KHỐI -> BÀI HỌC -> CHỦ ĐIỂM KIẾN THỨC)
# ==============================================================================
student_info = st.session_state["auth_user"]

# BỘ CHỌN KHỐI LỚP, BÀI HỌC VÀ CHỦ ĐIỂM
c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])
with c_gr:
    user_grade_default = 0 if student_info.get("grade") == 10 else (2 if student_info.get("grade") == 12 else 1)
    sel_grade = st.selectbox("📚 Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

with c_les:
    lesson_list = list(CURRICULUM_DATA[sel_grade].keys())
    sel_lesson = st.selectbox("📖 Bài học SGK:", lesson_list)

cur_lesson_obj = CURRICULUM_DATA[sel_grade][sel_lesson]

with c_top:
    topic_list = list(cur_lesson_obj["topics"].keys())
    sel_topic = st.selectbox("🎯 Chủ điểm kiến thức (Vở tự học):", topic_list)

cur_topic_data = cur_lesson_obj["topics"][sel_topic]

# 5 TABS HỌC TẬP TƯƠNG TÁC
tab1, tab_ex, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Video, Thuyết Minh & 3D)",
    "💡 Ví Dụ Minh Họa (Bấm Xem Lời Giải)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Tương Tác Giọng Nói",
    "🎯 Phòng Khảo Thí (Cấu Trúc Mới Đúng/Sai)"
])

# ------------------------------------------------------------------------------
# TAB 1: CỐT LÕI KIẾN THỨC (THEO CHỦ ĐIỂM ĐƯỢC CHỌN)
# ------------------------------------------------------------------------------
with tab1:
    st.subheader(f"📌 {cur_lesson_obj['chapter']}")
    st.markdown(f"#### {sel_lesson} — *{sel_topic}*")

    if "không gian" in sel_lesson or "Oxyz" in sel_lesson or "Vectơ" in sel_lesson:
        with st.container(border=True):
            st.markdown("🌐 **Mô Hình Không Gian 3D Tương Tác Trực Tiếp (Zero-Install)**")
            st.caption("Dùng chuột hoặc ngón tay chạm/vuốt để xoay 360 độ, quan sát hình chiếu:")
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
# TAB 2: VÍ DỤ MINH HỌA (TRÌNH BÀY ĐỀ BÀI -> BẤM ĐỂ XEM LỜI GIẢI CHI TIẾT)
# ------------------------------------------------------------------------------
with tab_ex:
    st.subheader(f"💡 Ví Dụ Minh Họa Chuẩn Mực: {sel_topic}")
    st.caption("Các ví dụ trọng tâm bám sát Vở tự học. Bấm vào từng Đề bài bên dưới để xem Lời giải chi tiết và học cách trình bày.")

    examples_list = cur_topic_data.get("examples", [])
    if not examples_list:
        st.info("Chủ điểm này đang được cập nhật thêm các ví dụ minh họa tiếp theo.")
    else:
        for idx, ex_item in enumerate(examples_list):
            with st.expander(f"📌 Đề bài {idx + 1}: {ex_item['title']}", expanded=(idx == 0)):
                st.markdown(f"**Đề bài yêu cầu:**\n\n{ex_item['problem']}")
                st.markdown("---")
                st.markdown("**✍️ Lời giải chi tiết chuẩn sư phạm:**")
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
