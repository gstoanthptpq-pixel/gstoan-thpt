# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 (PHẦN 1: BÀI 1 -> BÀI 16)
# Chuẩn hóa theo Vở tự học: Các chủ điểm là mục 1, 2, 3... thuộc PHẦN I
# ==============================================================================

GRADE_11_DATA = {}

GRADE_11_DATA.update({
    "Bài 1: Giá trị lượng giác của góc lượng giác": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Góc lượng giác và Đơn vị đo góc (Độ và Radian)": {
                "theory": "Tia Ou quay quanh O đến Ov tạo ra góc lượng giác (Ou, Ov). Chiều quay ngược chiều kim đồng hồ là chiều dương, cùng chiều là chiều âm. Mối liên hệ: $180^\\circ = \\pi \\text{ rad}$. Độ dài cung tròn bán kính R chắn góc $\\alpha$ rad là $l = \\alpha R$.",
                "formula": r"1^\circ = \frac{\pi}{180} \text{ rad}; \quad l = \alpha \cdot R \ (\alpha \text{ tính bằng rad})",
                "trap": "Khi tính độ dài cung tròn $l = \\alpha R$, góc $\\alpha$ bắt buộc phải đổi sang đơn vị radian. Dùng số đo độ sẽ cho kết quả sai.",
                "audio": "Góc lượng giác có chiều dương và chiều âm. Khi tính độ dài cung tròn, em bắt buộc phải đổi đơn vị góc sang radian trước.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đổi đơn vị góc",
                        "problem": "Đổi góc $135^\\circ$ sang đơn vị radian.",
                        "solution": "- Ta có $\\alpha = 135 \\cdot \\frac{\\pi}{180} = \\frac{3\\pi}{4}$ rad."
                    },
                    {
                        "title": "Ví dụ 2: Tính độ dài cung tròn",
                        "problem": "Tính độ dài cung tròn có bán kính $R = 8\\text{ cm}$ chắn góc có số đo $\\alpha = \\frac{\\pi}{4}\\text{ rad}$.",
                        "solution": "- Áp dụng công thức: $l = \\alpha R = \\frac{\\pi}{4} \\cdot 8 = 2\\pi \\approx 6.28\\text{ cm}$."
                    }
                ],
                "exercise": {"id": "11_1_1", "title": "Kiểm minh chứng", "content": "Góc 45 độ đổi sang radian có dạng pi/c. Giá trị của c bằng:", "type": "NUMERIC", "target": "4", "options": []}
            },
            "2. Giá trị lượng giác của góc lượng giác trên đường tròn": {
                "theory": "Trên đường tròn lượng giác gốc $A(1; 0)$, điểm $M(x; y)$ biểu diễn góc $\\alpha$: $\\sin\\alpha = y$ (tung độ), $\\cos\\alpha = x$ (hoành độ), $\\tan\\alpha = \\frac{y}{x}$ ($x \\neq 0$), $\\cot\\alpha = \\frac{x}{y}$ ($y \\neq 0$). Dấu các giá trị: Góc I (+; +), Góc II (-; +), Góc III (-; -), Góc IV (+; -).",
                "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha} \ (\alpha \neq \frac{\pi}{2} + k\pi)",
                "trap": "Khi khai căn $\\cos^2\\alpha = 1 - \\sin^2\\alpha$, phải đối chiếu góc $\\alpha$ nằm ở góc phần tư nào để lấy dấu (+) hoặc (-) chính xác.",
                "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Nhớ xét góc phần tư để chọn dấu âm hay dương cho chuẩn xác.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lượng giác",
                        "problem": "Cho $\\cos\\alpha = -\\frac{3}{5}$ với $\\pi < \\alpha < \\frac{3\\pi}{2}$. Tính $\\sin\\alpha$.",
                        "solution": "- $\\sin^2\\alpha = 1 - \\cos^2\\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$.\n- Vì $\\pi < \\alpha < \\frac{3\\pi}{2}$ (góc phần tư thứ III) nên $\\sin\\alpha < 0$.\n- Vậy $\\sin\\alpha = -\\frac{4}{5} = -0.8$."
                    }
                ],
                "exercise": {"id": "11_1_2", "title": "Kiểm minh chứng", "content": "Góc phần tư thứ II, sin = 0.8 thì cos bằng bao nhiêu?", "type": "NUMERIC", "target": "-0.6", "options": []}
            },
            "3. Giá trị lượng giác của các góc có liên quan đặc biệt": {
                "theory": "Hai góc đối nhau: $\\cos(-x) = \\cos x$ (các giá trị khác đối dấu). Hai góc bù nhau: $\\sin(\\pi - x) = \\sin x$. Hai góc phụ nhau: chéo nhau (sin thành cos). Hai góc hơn kém $\\pi$: tan và cot giữ nguyên.",
                "formula": r"\cos(-x) = \cos x; \quad \sin(\pi - x) = \sin x; \quad \tan(x + \pi) = \tan x",
                "trap": "Chỉ có $\\cos$ của hai góc đối nhau là bằng nhau. Sin, Tan, Cot của hai góc đối đều phải thêm dấu trừ đằng trước.",
                "audio": "Cos đối, sin bù, phụ chéo, hơn kém pi thì tan cot bằng nhau. Đó là thần chú để nhớ mọi công thức góc liên quan đặc biệt.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức lượng giác",
                        "problem": "Rút gọn biểu thức $A = \\sin(\\pi - x) + \\cos(-x) - \\cos(\\pi - x)$.",
                        "solution": "- $\\sin(\\pi - x) = \\sin x$.\n- $\\cos(-x) = \\cos x$.\n- $\\cos(\\pi - x) = -\\cos x$.\n- Vậy $A = \\sin x + \\cos x - (-\\cos x) = \\sin x + 2\\cos x$."
                    }
                ],
                "exercise": {"id": "11_1_3", "title": "Kiểm minh chứng", "content": "Giá trị của cos(-60 độ) bằng bao nhiêu?", "type": "NUMERIC", "target": "0.5", "options": []}
            }
        }
    },
    "Bài 2: Công thức lượng giác": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Công thức cộng": {
                "theory": "Khai triển lượng giác của tổng hoặc hiệu: $\\cos(a \\pm b) = \\cos a\\cos b \\mp \\sin a\\sin b$; $\\sin(a \\pm b) = \\sin a\\cos b \\pm \\cos a\\sin b$; $\\tan(a \\pm b) = \\frac{\\tan a \\pm \\tan b}{1 \\mp \\tan a\\tan b}$.",
                "formula": r"\cos(a + b) = \cos a\cos b - \sin a\sin b; \quad \sin(a + b) = \sin a\cos b + \cos a\sin b",
                "trap": "Công thức $\\cos(a + b)$ ở vế phải mang dấu TRỪ; còn $\\cos(a - b)$ vế phải mang dấu CỘNG. Rất dễ bị nhầm dấu.",
                "audio": "Cos thì cos cos sin sin đổi dấu, sin thì sin cos cos sin cùng dấu. Hãy nhớ kĩ quy tắc đổi dấu của hàm cosin nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lượng giác",
                        "problem": "Tính $\\sin 75^\\circ$ biết $75^\\circ = 45^\\circ + 30^\\circ$.",
                        "solution": "- $\\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ\\cos 30^\\circ + \\cos 45^\\circ\\sin 30^\\circ = \\frac{\\sqrt{2}}{2}\\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{2}}{2}\\frac{1}{2} = \\frac{\\sqrt{6} + \\sqrt{2}}{4}$."
                    }
                ],
                "exercise": {"id": "11_2_1", "title": "Kiểm minh chứng", "content": "Khai triển cos(a + b) bằng cos a.cos b - sin a.sin b. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Công thức nhân đôi và Hạ bậc": {
                "theory": "Công thức nhân đôi: $\\sin 2a = 2\\sin a\\cos a$; $\\cos 2a = \\cos^2 a - \\sin^2 a = 2\\cos^2 a - 1 = 1 - 2\\sin^2 a$. Công thức hạ bậc: $\\cos^2 a = \\frac{1 + \\cos 2a}{2}$; $\\sin^2 a = \\frac{1 - \\cos 2a}{2}$.",
                "formula": r"\sin 2a = 2\sin a\cos a; \quad \cos 2a = 2\cos^2 a - 1; \quad \cos^2 a = \frac{1 + \cos 2a}{2}",
                "trap": "Học sinh hay quên số 2 ở công thức $\\sin 2a = 2\\sin a\\cos a$. Quên chia 2 khi dùng công thức hạ bậc.",
                "audio": "Nhân đôi thì góc tăng gấp đôi số mũ giảm, hạ bậc thì giảm bậc hai xuống bậc một và góc tăng gấp đôi.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính theo góc nhân đôi",
                        "problem": "Cho $\\sin a = 0.6, \\cos a = 0.8$. Tính $\\sin 2a$.",
                        "solution": "- $\\sin 2a = 2\\sin a\\cos a = 2(0.6)(0.8) = 0.96$."
                    }
                ],
                "exercise": {"id": "11_2_2", "title": "Kiểm minh chứng", "content": "Biết sin a * cos a = 0.25. Giá trị của sin(2a) bằng:", "type": "NUMERIC", "target": "0.5", "options": []}
            },
            "3. Công thức biến đổi tích thành tổng và tổng thành tích": {
                "theory": "Biến đổi tổng thành tích: $\\cos a + \\cos b = 2\\cos\\frac{a+b}{2}\\cos\\frac{a-b}{2}$; $\\cos a - \\cos b = -2\\sin\\frac{a+b}{2}\\sin\\frac{a-b}{2}$; $\\sin a + \\sin b = 2\\sin\\frac{a+b}{2}\\cos\\frac{a-b}{2}$.",
                "formula": r"\cos a + \cos b = 2\cos\frac{a+b}{2}\cos\frac{a-b}{2}; \quad \cos a - \\cos b = -2\sin\frac{a+b}{2}\sin\frac{a-b}{2}",
                "trap": "Công thức $\\cos a - \\cos b$ có dấu TRỪ ở phía trước: $-2\\sin\\frac{a+b}{2}\\sin\\frac{a-b}{2}$.",
                "audio": "Cos cộng cos bằng hai cos cos, cos trừ cos bằng trừ hai sin sin. Chú ý dấu trừ ở hiệu hai cos nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức lượng giác",
                        "problem": "Rút gọn biểu thức $P = \\sin 4x + \\sin 2x$.",
                        "solution": "- $P = 2\\sin\\left(\\frac{4x+2x}{2}\\right)\\cos\\left(\\frac{4x-2x}{2}\\right) = 2\\sin 3x\\cos x$."
                    }
                ],
                "exercise": {"id": "11_2_3", "title": "Kiểm minh chứng", "content": "Rút gọn (sin 4x + sin 2x) / cos x được c.sin(3x). Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 3: Hàm số lượng giác": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Tập xác định của các hàm số lượng giác": {
                "theory": "Hàm số $y = \\sin x$ và $y = \\cos x$ có TXĐ $D = \\mathbb{R}$, tập giá trị $[-1; 1]$. Hàm số $y = \\tan x$ xác định khi $\\cos x \\neq 0 \\iff x \\neq \\frac{\\pi}{2} + k\\pi$. Hàm số $y = \\cot x$ xác định khi $\\sin x \\neq 0 \\iff x \\neq k\\pi$ ($k \\in \\mathbb{Z}$).",
                "formula": r"D_{\tan} = \mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi\right\}; \quad D_{\cot} = \mathbb{R} \setminus \{k\pi\}",
                "trap": "Điều kiện xác định của $\\tan x$ là $x \\neq \\frac{\\pi}{2} + k\\pi$ (đuôi $k\\pi$, học sinh hay ghi nhầm thành $k2\\pi$).",
                "audio": "Sin và Cos xác định trên toàn trục số thực. Tan không xác định tại các điểm pi trên 2 cộng k pi, Cot không xác định tại k pi.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định",
                        "problem": "Tìm tập xác định của hàm số $y = \\frac{1}{\\sin x}$.",
                        "solution": "- Điều kiện: $\\sin x \\neq 0 \\iff x \\neq k\\pi$ ($k \\in \\mathbb{Z}$).\n- Tập xác định $D = \\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$."
                    }
                ],
                "exercise": {"id": "11_3_1", "title": "Kiểm minh chứng", "content": "Tập giá trị của hàm số y = 3 sin(x) + 2 là [-1; c]. Giá trị c bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Tính tuần hoàn và Chu kỳ của hàm số lượng giác": {
                "theory": "Hàm $y = \\sin x, y = \\cos x$ tuần hoàn với chu kỳ $T = 2\\pi$. Hàm $y = \\tan x, y = \\cot x$ tuần hoàn với chu kỳ $T = \\pi$. Với hàm $y = \\sin(ax + b)$, chu kỳ là $T = \\frac{2\\pi}{|a|}$.",
                "formula": r"T = \frac{2\pi}{|a|} \ (\text{với } \sin, \cos); \quad T = \frac{\pi}{|a|} \ (\text{với } \tan, \cot)",
                "trap": "Khi tính chu kỳ của hàm số lượng giác mở rộng, học sinh hay quên chia cho giá trị tuyệt đối $|a|$ của hệ số đứng trước biến x.",
                "audio": "Chu kỳ là khoảng lặp lại của đồ thị. Hàm sin và cos tuần hoàn theo chu kỳ hai pi, còn tan và cot tuần hoàn theo một pi.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm chu kỳ hàm số",
                        "problem": "Tìm chu kỳ tuần hoàn của hàm số $y = \\cos(3x)$.",
                        "solution": "- Hệ số $a = 3$. Chu kỳ của hàm số là $T = \\frac{2\\pi}{|3|} = \\frac{2\\pi}{3}$."
                    }
                ],
                "exercise": {"id": "11_3_2", "title": "Kiểm minh chứng", "content": "Chu kỳ của hàm số y = tan(2x) có dạng pi/c. Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "3. Tính chẵn lẻ và Đồ thị của hàm số lượng giác": {
                "theory": "Hàm số $y = \\cos x$ là hàm số CHẴN (đồ thị đối xứng qua trục tung $Oy$). Ba hàm số $y = \\sin x, y = \\tan x, y = \\cot x$ là các hàm số LẺ (đồ thị đối xứng qua gốc tọa độ O).",
                "formula": r"\cos(-x) = \cos x \ (\text{Chẵn}); \quad \sin(-x) = -\sin x \ (\text{Lẻ})",
                "trap": "Học sinh thường nhầm hàm $y = \\sin x$ là hàm chẵn. Nhớ kĩ: Duy nhất hàm cosin là hàm chẵn.",
                "audio": "Duy nhất hàm cosin là hàm số chẵn có đồ thị đối xứng qua trục tung. Cả ba hàm còn lại đều là hàm số lẻ nhận gốc O làm tâm đối xứng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính chẵn lẻ",
                        "problem": "Xét tính chẵn lẻ của hàm số $f(x) = x \\cdot \\sin x$.",
                        "solution": "- $TXĐ: D = \\mathbb{R}$.\n- Ta có $f(-x) = (-x) \\cdot \\sin(-x) = (-x) \\cdot (-\\sin x) = x\\sin x = f(x)$.\n- Vậy $f(x)$ là hàm số chẵn."
                    }
                ],
                "exercise": {"id": "11_3_3", "title": "Kiểm minh chứng", "content": "Hàm số y = sin(x) là hàm số chẵn (1) hay hàm số lẻ (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 4: Phương trình lượng giác cơ bản": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phương trình sin x = m và cos x = m": {
                "theory": "Phương trình có nghiệm $\\iff |m| \\le 1$. Nếu $|m| > 1$, phương trình vô nghiệm. $\\sin x = \\sin\\alpha \\iff x = \\alpha + k2\\pi$ hoặc $x = \\pi - \\alpha + k2\\pi$. $\\cos x = \\cos\\alpha \\iff x = \\pm\\alpha + k2\\pi$ ($k \\in \\mathbb{Z}$).",
                "formula": r"\sin x = \sin\alpha \iff \left[\begin{matrix} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{matrix}\right.; \quad \cos x = \cos\alpha \iff x = \pm\alpha + k2\pi",
                "trap": "Học sinh giải phương trình $\\sin x = m$ rất hay quên họ nghiệm thứ hai là góc bù: $x = \\pi - \\alpha + k2\\pi$.",
                "audio": "Phương trình sin có hai họ nghiệm bù nhau đuôi k2pi. Phương trình cos có hai họ nghiệm đối nhau đuôi k2pi.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình sin cơ bản",
                        "problem": "Giải phương trình $\\sin x = \\frac{1}{2}$.",
                        "solution": "- Vì $\\frac{1}{2} = \\sin\\frac{\\pi}{6}$ nên ta có hai họ nghiệm:\n- $x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\pi - \\frac{\\pi}{6} + k2\\pi = \\frac{5\\pi}{6} + k2\\pi$ ($k \\in \\mathbb{Z}$)."
                    }
                ],
                "exercise": {"id": "11_4_1", "title": "Kiểm minh chứng", "content": "Phương trình cos(x) = 1 có một nghiệm thuộc [0; pi] là x bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Phương trình tan x = m và cot x = m": {
                "theory": "Phương trình $\\tan x = m$ và $\\cot x = m$ luôn có nghiệm với mọi $m \\in \\mathbb{R}$. Họ nghiệm có chu kỳ là $k\\pi$: $\\tan x = \\tan\\alpha \\iff x = \\alpha + k\\pi$; $\\cot x = \\cot\\alpha \\iff x = \\alpha + k\\pi$.",
                "formula": r"\tan x = \tan\alpha \iff x = \alpha + k\pi; \quad \cot x = \cot\alpha \iff x = \alpha + k\pi",
                "trap": "Quen tay ghi đuôi chu kỳ của tan và cot thành $+ k2\\pi$. Nhớ kỹ đuôi của tan và cot chỉ là $+ k\\pi$.",
                "audio": "Phương trình tan và cot luôn có nghiệm với mọi m. Đuôi chu kỳ cộng thêm chỉ là một k pi duy nhất.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình tan",
                        "problem": "Giải phương trình $\\tan x = 1$.",
                        "solution": "- Ta có $1 = \\tan\\frac{\\pi}{4}$.\n- Vậy $x = \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$)."
                    }
                ],
                "exercise": {"id": "11_4_2", "title": "Kiểm minh chứng", "content": "Số nghiệm của phương trình tan(x) = 1 trên khoảng (0; pi) là:", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 5: Dãy số": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khái niệm và Cách cho một dãy số": {
                "theory": "Dãy số là hàm số xác định trên tập số nguyên dương $\\mathbb{N}^*$. Dãy số vô hạn $(u_n) = u_1, u_2, \\dots, u_n, \\dots$ Dãy số có thể cho bằng: (1) Công thức số hạng tổng quát $u_n = f(n)$; (2) Hệ thức truy hồi; (3) Liệt kê.",
                "formula": r"u_n = f(n) \quad (n \in \mathbb{N}^*)",
                "trap": "Số hạng đầu tiên của dãy số luôn ứng với chỉ số $n = 1$, không bao giờ có số hạng ứng với $n = 0$.",
                "audio": "Dãy số là hàm số có tập xác định là các số tự nhiên bắt đầu từ 1. Muốn tìm số hạng thứ mấy thì em thay n bằng số đó.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng của dãy số",
                        "problem": "Cho dãy số $u_n = \\frac{2n - 1}{n + 1}$. Tính số hạng $u_3$.",
                        "solution": "- Thay $n = 3$: $u_3 = \\frac{2(3) - 1}{3 + 1} = \\frac{5}{4}$."
                    }
                ],
                "exercise": {"id": "11_5_1", "title": "Kiểm minh chứng", "content": "Cho dãy số u_n = 4n - 3. Số hạng u_4 bằng bao nhiêu?", "type": "NUMERIC", "target": "13", "options": []}
            },
            "2. Dãy số tăng, dãy số giảm": {
                "theory": "Dãy số $(u_n)$ là dãy tăng nếu $u_{n+1} > u_n, \\forall n \\ge 1$ (hiệu $u_{n+1} - u_n > 0$). Dãy số $(u_n)$ là dãy giảm nếu $u_{n+1} < u_n, \\forall n \\ge 1$ (hiệu $u_{n+1} - u_n < 0$).",
                "formula": r"u_{n+1} - u_n > 0 \implies \text{Dãy tăng}; \quad u_{n+1} - u_n < 0 \implies \text{Dãy giảm}",
                "trap": "Lập tỉ số $\\frac{u_{n+1}}{u_n}$ so sánh với 1 để xét tính tăng giảm chỉ được áp dụng khi tất cả các số hạng của dãy đều là số DƯƠNG.",
                "audio": "Muốn biết dãy số tăng hay giảm, em cứ lấy số hạng sau trừ đi số hạng liền trước. Nếu hiệu dương là dãy tăng, hiệu âm là dãy giảm.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính tăng giảm",
                        "problem": "Xét tính tăng, giảm của dãy số $u_n = 2n + 5$.",
                        "solution": "- Ta xét hiệu: $u_{n+1} - u_n = [2(n+1) + 5] - (2n + 5) = 2 > 0$.\n- Vì hiệu luôn dương nên $(u_n)$ là dãy số tăng."
                    }
                ],
                "exercise": {"id": "11_5_2", "title": "Kiểm minh chứng", "content": "Dãy số u_n = 5 - 2n là dãy số tăng (1) hay dãy số giảm (0)?", "type": "NUMERIC", "target": "0", "options": []}
            },
            "3. Dãy số bị chặn": {
                "theory": "Dãy $(u_n)$ bị chặn trên nếu tồn tại M sao cho $u_n \\le M, \\forall n$. Dãy bị chặn dưới nếu tồn tại m sao cho $u_n \\ge m, \\forall n$. Dãy số vừa bị chặn trên vừa bị chặn dưới thì gọi là dãy số bị chặn.",
                "formula": r"m \le u_n \le M, \forall n \in \mathbb{N}^* \implies (u_n) \text{ bị chặn}",
                "trap": "Kết luận dãy số bị chặn khi mới chỉ chỉ ra được nó bị chặn trên hoặc chặn dưới là sai. Bị chặn phải gồm cả hai đầu.",
                "audio": "Dãy số bị chặn là dãy số bị kẹp ở giữa hai con số cố định, không thể tăng lên vô cùng mà cũng không thể giảm xuống âm vô cùng.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh dãy số bị chặn",
                        "problem": "Dãy số $u_n = \\frac{1}{n}$ có bị chặn không?",
                        "solution": "- Với mọi $n \\ge 1$, ta luôn có $0 < \\frac{1}{n} \\le 1$.\n- Dãy số bị chặn dưới bởi 0 và bị chặn trên bởi 1, nên là dãy số bị chặn."
                    }
                ],
                "exercise": {"id": "11_5_3", "title": "Kiểm minh chứng", "content": "Giá trị lớn nhất của dãy số u_n = 1/n đạt được bằng:", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 6: Cấp số cộng": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Số hạng tổng quát của cấp số cộng": {
                "theory": "Cấp số cộng (CSC) là dãy số thỏa mãn $u_{n+1} = u_n + d$ (d là công sai không đổi). Số hạng tổng quát: $u_n = u_1 + (n - 1)d$. Tính chất các số hạng: $u_k = \\frac{u_{k-1} + u_{k+1}}{2}$.",
                "formula": r"u_n = u_1 + (n - 1)d; \quad u_{k-1} + u_{k+1} = 2u_k",
                "trap": "Học sinh thường nhầm số hạng tổng quát thành $u_n = u_1 + nd$ (nhớ là phải nhân với $n - 1$).",
                "audio": "Cấp số cộng có quy luật số sau bằng số trước cộng thêm công sai d. Số hạng thứ n bằng u1 cộng n trừ 1 nhân d.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng tổng quát",
                        "problem": "Cho cấp số cộng có $u_1 = 3, d = 4$. Tìm $u_6$.",
                        "solution": "- Áp dụng: $u_6 = u_1 + (6 - 1)d = 3 + 5(4) = 23$."
                    }
                ],
                "exercise": {"id": "11_6_1", "title": "Kiểm minh chứng", "content": "Cấp số cộng có u1 = 5, d = 2. Số hạng u4 bằng bao nhiêu?", "type": "NUMERIC", "target": "11", "options": []}
            },
            "2. Tổng n số hạng đầu tiên của cấp số cộng": {
                "theory": "Tổng của n số hạng đầu tiên $S_n = u_1 + u_2 + \\dots + u_n$ bằng số lượng số hạng nhân với trung bình cộng của số đầu và số cuối.",
                "formula": r"S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n - 1)d]}{2}",
                "trap": "Khi tính $S_n$ bằng công thức chứa công sai $d$, học sinh thường nhầm lẫn thành $nd$ thay vì $(n - 1)d$.",
                "audio": "Tổng cấp số cộng bằng số lượng số hạng nhân với tổng số đầu cộng số cuối rồi chia cho hai.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng cấp số cộng",
                        "problem": "Tính tổng 10 số hạng đầu của cấp số cộng có $u_1 = 2, d = 3$.",
                        "solution": "- $S_{10} = \\frac{10[2(2) + 9(3)]}{2} = 5(4 + 27) = 5 \\cdot 31 = 155$."
                    }
                ],
                "exercise": {"id": "11_6_2", "title": "Kiểm minh chứng", "content": "Tổng 5 số hạng đầu của CSC có u1 = 1, d = 2 bằng:", "type": "NUMERIC", "target": "25", "options": []}
            }
        }
    },
    "Bài 7: Cấp số nhân": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Số hạng tổng quát của cấp số nhân": {
                "theory": "Cấp số nhân (CSN) là dãy số thỏa mãn $u_{n+1} = u_n \\cdot q$ (q là công bội không đổi). Số hạng tổng quát: $u_n = u_1 \\cdot q^{n-1}$. Tính chất ba số hạng liên tiếp: $u_k^2 = u_{k-1} \\cdot u_{k+1}$.",
                "formula": r"u_n = u_1 \cdot q^{n-1}; \quad u_k^2 = u_{k-1} \cdot u_{k+1}",
                "trap": "Số mũ của công bội q trong công thức số hạng tổng quát là $n - 1$, học sinh rất hay ghi nhầm thành $q^n$.",
                "audio": "Cấp số nhân có số sau bằng số trước nhân công bội q. Số hạng thứ n bằng u1 nhân q mũ n trừ 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng của cấp số nhân",
                        "problem": "Cho cấp số nhân có $u_1 = 2, q = 3$. Tìm số hạng $u_4$.",
                        "solution": "- $u_4 = u_1 \\cdot q^{4-1} = 2 \\cdot 3^3 = 2 \\cdot 27 = 54$."
                    }
                ],
                "exercise": {"id": "11_7_1", "title": "Kiểm minh chứng", "content": "Cấp số nhân có u1 = 3, q = 2. Số hạng u3 bằng:", "type": "NUMERIC", "target": "12", "options": []}
            },
            "2. Tổng n số hạng đầu tiên của cấp số nhân": {
                "theory": "Tổng của n số hạng đầu tiên của cấp số nhân có công bội $q \\neq 1$: $S_n = u_1 \\frac{1 - q^n}{1 - q}$.",
                "formula": r"S_n = u_1 \frac{1 - q^n}{1 - q} \ (q \neq 1)",
                "trap": "Trong công thức tổng $S_n$, trên tử số là $q^n$ (mũ n nguyên vẹn), không phải $q^{n-1}$.",
                "audio": "Tính tổng cấp số nhân em lấy u1 nhân với phân thức 1 trừ q mũ n chia cho 1 trừ q.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng cấp số nhân",
                        "problem": "Tính tổng 4 số hạng đầu của cấp số nhân có $u_1 = 2, q = 3$.",
                        "solution": "- $S_4 = 2 \\cdot \\frac{1 - 3^4}{1 - 3} = 2 \\cdot \\frac{1 - 81}{-2} = 80$."
                    }
                ],
                "exercise": {"id": "11_7_2", "title": "Kiểm minh chứng", "content": "Tổng 3 số hạng đầu của CSN có u1 = 1, q = 2 bằng:", "type": "NUMERIC", "target": "7", "options": []}
            }
        }
    },
    "Bài 8: Mẫu số liệu ghép nhóm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Bảng số liệu ghép nhóm và Độ dài nhóm": {
                "theory": "Mẫu số liệu ghép nhóm được phân vào các nhóm nửa khoảng $[a_i; a_{i+1})$. Độ dài của mỗi nhóm là hiệu $h = a_{i+1} - a_i$. Tần số $n_i$ là số lượng quan sát thuộc vào nhóm đó.",
                "formula": r"h = a_{i+1} - a_i; \quad n = \sum_{i=1}^k n_i",
                "trap": "Nhóm số liệu $[a; b)$ bao gồm điểm đầu mút $a$ nhưng KHÔNG bao gồm điểm đầu mút $b$.",
                "audio": "Mẫu số liệu ghép nhóm chia dữ liệu thành các khoảng liền kề nhau. Độ dài nhóm bằng đầu mút phải trừ đầu mút trái.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài nhóm",
                        "problem": "Tính độ dài của nhóm số liệu $[20; 35)$.",
                        "solution": "- Độ dài nhóm: $h = 35 - 20 = 15$."
                    }
                ],
                "exercise": {"id": "11_8_1", "title": "Kiểm minh chứng", "content": "Độ dài của nhóm số liệu [10; 25) bằng bao nhiêu?", "type": "NUMERIC", "target": "15", "options": []}
            },
            "2. Tần số tích lũy và Giá trị đại diện của nhóm": {
                "theory": "Giá trị đại diện $c_i$ của nhóm $[a_i; a_{i+1})$ là trung bình cộng của hai đầu mút. Tần số tích lũy $C_k$ của nhóm k là tổng tần số của nhóm đó và tất cả các nhóm đứng trước nó.",
                "formula": r"c_i = \frac{a_i + a_{i+1}}{2}; \quad C_k = n_1 + n_2 + \dots + n_k",
                "trap": "Giá trị đại diện tính bằng phép CỘNG hai đầu mút rồi chia đôi, không phải phép trừ.",
                "audio": "Giá trị đại diện là số nằm chính giữa nhóm, em lấy hai đầu mút cộng lại chia đôi là xong.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giá trị đại diện",
                        "problem": "Tìm giá trị đại diện của nhóm số liệu $[40; 50)$.",
                        "solution": "- $c = \\frac{40 + 50}{2} = 45$."
                    }
                ],
                "exercise": {"id": "11_8_2", "title": "Kiểm minh chứng", "content": "Giá trị đại diện của nhóm [20; 30) bằng bao nhiêu?", "type": "NUMERIC", "target": "25", "options": []}
            }
        }
    },
    "Bài 9: Các số đặc trưng đo xu thế trung tâm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Số trung bình của mẫu số liệu ghép nhóm": {
                "theory": "Số trung bình bằng tổng các tích của tần số nhân với giá trị đại diện của nhóm tương ứng, chia cho tổng cỡ mẫu n.",
                "formula": r"\overline{x} = \frac{1}{n}\sum_{i=1}^k n_i c_i = \frac{n_1c_1 + n_2c_2 + \dots + n_kc_k}{n}",
                "trap": "Học sinh thường quên nhân tần số $n_i$ vào giá trị đại diện $c_i$, chỉ cộng các $c_i$ lại chia cho số nhóm là sai.",
                "audio": "Số trung bình tính bằng trung bình có trọng số. Mỗi giá trị đại diện phải nhân với tần số của nhóm nó rồi mới cộng lại chia cho tổng số.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính số trung bình ghép nhóm",
                        "problem": "Nhóm [0; 10) có tần số 3, nhóm [10; 20) có tần số 7. Tính số trung bình.",
                        "solution": "- Giá trị đại diện: $c_1 = 5, c_2 = 15$. Cỡ mẫu $n = 3 + 7 = 10$.\n- $\\overline{x} = \\frac{3(5) + 7(15)}{10} = \\frac{15 + 105}{10} = 12$."
                    }
                ],
                "exercise": {"id": "11_9_1", "title": "Kiểm minh chứng", "content": "Mẫu có [0; 10) tần số 5 và [10; 20) tần số 5. Số trung bình bằng:", "type": "NUMERIC", "target": "10", "options": []}
            },
            "2. Trung vị và Tứ phân vị của mẫu số liệu ghép nhóm": {
                "theory": "Trung vị $M_e = Q_2$ chia đôi mẫu số liệu. Nhóm chứa trung vị là nhóm đầu tiên có tần số tích lũy $\\ge n/2$. Công thức nội suy: $M_e = u_m + \\frac{\\frac{n}{2} - C}{n_m} \\cdot h$. Tương tự với $Q_1$ (vị trí $n/4$) và $Q_3$ (vị trí $3n/4$).",
                "formula": r"M_e = u_m + \frac{\frac{n}{2} - C}{n_m} \cdot h; \quad Q_1 = u_p + \frac{\frac{n}{4} - C_{p-1}}{n_p} \cdot h",
                "trap": "Đại lượng $C$ trong công thức là tần số tích lũy của nhóm ĐỨNG LIỀN TRƯỚC nhóm chứa trung vị, không bao gồm nhóm hiện tại.",
                "audio": "Trung vị chia đôi dữ liệu. Nhóm chứa trung vị là nhóm có tần số tích lũy vượt qua mốc n chia 2.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định nhóm chứa trung vị",
                        "problem": "Cỡ mẫu $n = 60$. Nhóm 1 tần số 20, nhóm 2 tần số 15. Nhóm nào chứa trung vị?",
                        "solution": "- Mốc $n/2 = 30$.\n- Tần số tích lũy nhóm 1 là 20 (< 30). Tần số tích lũy nhóm 2 là $20 + 15 = 35$ ($\\ge 30$).\n- Vậy trung vị nằm ở nhóm thứ 2."
                    }
                ],
                "exercise": {"id": "11_9_2", "title": "Kiểm minh chứng", "content": "Cỡ mẫu n = 80 thì mốc xác định nhóm chứa trung vị n/2 bằng bao nhiêu?", "type": "NUMERIC", "target": "40", "options": []}
            },
            "3. Mốt của mẫu số liệu ghép nhóm": {
                "theory": "Nhóm chứa mốt là nhóm có tần số lớn nhất $n_m$. Mốt $M_o$ được tính bằng công thức nội suy dựa trên tần số nhóm trước và nhóm sau.",
                "formula": r"M_o = u_m + \frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \cdot h",
                "trap": "Nhầm lẫn giữa tần số nhóm liền trước ($n_{m-1}$) và nhóm liền sau ($n_{m+1}$) trong công thức tính Mốt.",
                "audio": "Nhóm chứa mốt là nhóm đạt đỉnh tần số cao nhất. Từ nhóm đó ta áp dụng công thức nội suy để tìm ra giá trị mốt.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định nhóm chứa mốt",
                        "problem": "Cho 3 nhóm có tần số lần lượt là 12, 28, 15. Nhóm nào chứa mốt?",
                        "solution": "- Tần số lớn nhất là 28 thuộc nhóm thứ 2. Vậy nhóm 2 là nhóm chứa mốt."
                    }
                ],
                "exercise": {"id": "11_9_3", "title": "Kiểm minh chứng", "content": "Nếu 3 nhóm có tần số 5, 20, 10 thì tần số của nhóm chứa mốt n_m bằng:", "type": "NUMERIC", "target": "20", "options": []}
            }
        }
    },
    "Bài 10: Đường thẳng và mặt phẳng trong không gian": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Các khái niệm mở đầu và Tính chất thừa nhận": {
                "theory": "Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng. Nếu một đường thẳng có hai điểm phân biệt thuộc một mặt phẳng thì mọi điểm của đường thẳng đều thuộc mặt phẳng đó.",
                "formula": r"A, B, C \text{ không thẳng hàng} \implies \exists! (ABC)",
                "trap": "Ba điểm PHẢI KHÔNG THẲNG HÀNG thì mới xác định duy nhất một mặt phẳng. Nếu ba điểm thẳng hàng thì có vô số mặt phẳng đi qua chúng.",
                "audio": "Ba điểm không thẳng hàng tạo nên một mặt phẳng duy nhất vững chắc, giống như chiếc kiềng ba chân.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Điểm thuộc mặt phẳng",
                        "problem": "Cho tứ diện ABCD. Điểm A có thuộc mặt phẳng (BCD) không?",
                        "solution": "- Bốn đỉnh của tứ diện không đồng phẳng nên đỉnh A không thuộc mặt phẳng (BCD)."
                    }
                ],
                "exercise": {"id": "11_10_1", "title": "Kiểm minh chứng", "content": "Số mặt phẳng đi qua 3 điểm phân biệt không thẳng hàng là:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Cách xác định mặt phẳng và Giao tuyến": {
                "theory": "Có 3 cách xác định mặt phẳng: Qua 3 điểm không thẳng hàng; Qua 1 đường thẳng và 1 điểm ngoài đường; Qua 2 đường thẳng cắt nhau. Giao tuyến của hai mặt phẳng phân biệt là đường thẳng đi qua tất cả các điểm chung của chúng.",
                "formula": r"(P) \cap (Q) = d; \quad d \cap (P) = M",
                "trap": "Để tìm giao tuyến, cần tìm 2 điểm chung phân biệt. Điểm chung thứ hai thường là giao điểm của hai đường thẳng cắt nhau trong mặt phẳng đáy.",
                "audio": "Giao tuyến của hai mặt phẳng là đường thẳng nối các điểm chung giữa chúng, giống như gáy của một cuốn sách đang mở.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giao tuyến cơ bản",
                        "problem": "Cho hình chóp S.ABCD. Giao tuyến của mặt phẳng (SAB) và (SBC) là đường nào?",
                        "solution": "- Hai mặt phẳng có hai điểm chung là S và B.\n- Vậy giao tuyến là đường thẳng SB."
                    }
                ],
                "exercise": {"id": "11_10_2", "title": "Kiểm minh chứng", "content": "Giao tuyến của (SAC) và (SBD) trong hình chóp S.ABCD đi qua S và tâm đáy O. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 11: Hai đường thẳng song song": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Vị trí tương đối của hai đường thẳng trong không gian": {
                "theory": "Trong không gian, hai đường thẳng có 4 vị trí: Cắt nhau, Song song (cùng thuộc 1 mặt phẳng và không có điểm chung), Trùng nhau, và Chéo nhau (không cùng nằm trong bất kỳ mặt phẳng nào).",
                "formula": r"a \parallel b \iff a, b \subset (P) \text{ và } a \cap b = \emptyset; \quad a, b \text{ chéo nhau} \iff \text{Không đồng phẳng}",
                "trap": "Hai đường thẳng không có điểm chung CHƯA CHẮC đã song song, chúng có thể chéo nhau.",
                "audio": "Trong không gian, hai đường thẳng không cắt nhau có thể song song hoặc chéo nhau. Chéo nhau nghĩa là không có mặt phẳng nào chứa cả hai đường.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện đường chéo nhau",
                        "problem": "Cho tứ diện ABCD. Cạnh AB và CD có vị trí tương đối thế nào?",
                        "solution": "- Bốn điểm A, B, C, D không đồng phẳng nên AB và CD không thể cùng nằm trong một mặt phẳng.\n- Vậy AB và CD chéo nhau."
                    }
                ],
                "exercise": {"id": "11_11_1", "title": "Kiểm minh chứng", "content": "Hai đường thẳng không có điểm chung thì chắc chắn song song. Khẳng định này Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Tính chất hai đường thẳng song song và Định lí ba giao tuyến": {
                "theory": "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau. Định lí ba giao tuyến: Ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến đó hoặc đồng quy, hoặc đôi một song song.",
                "formula": r"a \parallel c, b \parallel c \implies a \parallel b; \quad \text{Định lí ba giao tuyến: Đồng quy hoặc đôi một song song}",
                "trap": "Nếu hai mặt phẳng lần lượt chứa hai đường thẳng song song thì giao tuyến của chúng (nếu có) phải song song với hai đường đó hoặc trùng một trong hai.",
                "audio": "Định lí ba giao tuyến khẳng định ba nếp gấp của ba mặt phẳng chỉ có thể cùng chụm vào một điểm hoặc song song thẳng hàng với nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giao tuyến song song",
                        "problem": "Hình chóp S.ABCD đáy hình bình hành. Giao tuyến của (SAB) và (SCD) đi qua S và song song với cạnh nào?",
                        "solution": "- Vì $AB \\parallel CD$ nên giao tuyến của (SAB) và (SCD) là đường thẳng qua S và song song với AB và CD."
                    }
                ],
                "exercise": {"id": "11_11_2", "title": "Kiểm minh chứng", "content": "Giao tuyến của (SAB) và (SCD) với đáy ABCD hình bình hành có song song với AB không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 12: Đường thẳng và mặt phẳng song song": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Điều kiện để đường thẳng song song với mặt phẳng": {
                "theory": "Đường thẳng $d$ song song với mặt phẳng $(P)$ nếu $d$ không nằm trong $(P)$ và $d$ song song với MỘT đường thẳng $a$ nằm trong $(P)$.",
                "formula": r"\begin{cases} d \not\subset (P) \\ a \subset (P) \\ d \parallel a \end{cases} \implies d \parallel (P)",
                "trap": "Bắt buộc phải có điều kiện $d$ KHÔNG NẰM TRONG mặt phẳng $(P)$. Nếu $d$ nằm trong $(P)$ thì không được kết luận song song.",
                "audio": "Muốn chứng minh một đường thẳng song song với mặt phẳng, em chỉ cần tìm một đường thẳng nằm trong mặt phẳng đó song song với đường thẳng đã cho.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường song song mặt",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành. Chứng minh AB song song với mặt phẳng (SCD).",
                        "solution": "- Ta có $AB \\parallel CD$ (tính chất hình bình hành).\n- Cạnh $CD \\subset (SCD)$ và $AB \\not\\subset (SCD)$.\n- Suy ra $AB \\parallel (SCD)$."
                    }
                ],
                "exercise": {"id": "11_12_1", "title": "Kiểm minh chứng", "content": "Đường thẳng d nằm hoàn toàn trong mặt phẳng (P). Hỏi d có song song với (P) không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Tính chất của đường thẳng song song mặt phẳng": {
                "theory": "Nếu đường thẳng $a$ song song với mặt phẳng $(P)$, thì bất kỳ mặt phẳng $(Q)$ nào chứa $a$ mà cắt $(P)$ theo giao tuyến $b$ thì $b$ phải song song với $a$.",
                "formula": r"\begin{cases} a \parallel (P) \\ a \subset (Q) \\ (P) \cap (Q) = b \end{cases} \implies b \parallel a",
                "trap": "Đường thẳng song song với mặt phẳng KHÔNG CÓ NGHĨA là nó song song với mọi đường thẳng trong mặt đó. Nó chỉ song song với các đường cùng phương.",
                "audio": "Đường thẳng song song với mặt phẳng thì sẽ song song với giao tuyến của mặt phẳng đó với bất kỳ mặt phẳng nào chứa nó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm thiết diện song song",
                        "problem": "Mặt phẳng đi qua điểm M và song song với đường thẳng d thì giao tuyến của nó với các mặt phẳng chứa d sẽ như thế nào?",
                        "solution": "- Giao tuyến sinh ra luôn song song với đường thẳng d."
                    }
                ],
                "exercise": {"id": "11_12_2", "title": "Kiểm minh chứng", "content": "Nếu a // (P) thì a không có điểm chung nào với (P). Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 13: Hai mặt phẳng song song": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Điều kiện để hai mặt phẳng song song": {
                "theory": "Mặt phẳng $(P)$ song song với mặt phẳng $(Q)$ nếu $(P)$ chứa HAI đường thẳng CẮT NHAU cùng song song với mặt phẳng $(Q)$.",
                "formula": r"\begin{cases} a, b \subset (P); \ a \cap b = I \\ a \parallel (Q); \ b \parallel (Q) \end{cases} \implies (P) \parallel (Q)",
                "trap": "Hai đường thẳng $a$ và $b$ nằm trong $(P)$ BẮT BUỘC phải cắt nhau. Nếu chúng song song với nhau thì chưa đủ điều kiện kết luận.",
                "audio": "Muốn chứng minh hai mặt phẳng song song, em cần tìm hai đường thẳng cắt nhau trong mặt phẳng này cùng song song với mặt phẳng kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng song song",
                        "problem": "Cho hình chóp S.ABC. M, N, P lần lượt là trung điểm SA, SB, SC. Chứng minh (MNP) // (ABC).",
                        "solution": "- Ta có $MN \\parallel AB$ và $NP \\parallel BC$ (đường trung bình).\n- MN và NP cắt nhau tại N nằm trong (MNP).\n- Suy ra $(MNP) \\parallel (ABC)$."
                    }
                ],
                "exercise": {"id": "11_13_1", "title": "Kiểm minh chứng", "content": "Để (P) // (Q) thì (P) cần chứa tối thiểu bao nhiêu đường thẳng cắt nhau cùng song song (Q)?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Tính chất hai mặt phẳng song song và Hình lăng trụ": {
                "theory": "Mặt phẳng thứ ba cắt hai mặt phẳng song song theo hai giao tuyến song song. Hai mặt phẳng song song chắn trên hai cát tuyến song song những đoạn thẳng bằng nhau. Hình lăng trụ có các cạnh bên song song và bằng nhau, hai đáy song song và là các đa giác bằng nhau.",
                "formula": r"(P) \parallel (Q); \ (R) \cap (P) = a; \ (R) \cap (Q) = b \implies a \parallel b",
                "trap": "Các đoạn thẳng chắn giữa hai mặt phẳng song song chỉ BẰNG NHAU khi hai đường thẳng đó song song với nhau.",
                "audio": "Mặt phẳng thứ ba cắt hai mặt phẳng song song sẽ tạo ra hai giao tuyến song song. Các cạnh bên của hình lăng trụ luôn song song và bằng nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính chất lăng trụ",
                        "problem": "Trong hình lăng trụ tam giác ABC.A'B'C', các mặt bên là hình gì?",
                        "solution": "- Các mặt bên có các cạnh đối song song và bằng nhau nên luôn là các hình bình hành."
                    }
                ],
                "exercise": {"id": "11_13_2", "title": "Kiểm minh chứng", "content": "Hai mặt phẳng phân biệt cùng song song với mặt phẳng thứ ba thì song song với nhau. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 14: Phép chiếu song song": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phép chiếu song song và Tính chất": {
                "theory": "Phép chiếu song song biến đường thẳng thành đường thẳng, biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau. Bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc nằm trên hai đường thẳng song song.",
                "formula": r"\text{Bảo toàn tính thẳng hàng, song song và tỉ số đoạn thẳng cùng phương}",
                "trap": "Phép chiếu song song KHÔNG bảo toàn độ lớn của góc và độ dài thực tế của đoạn thẳng.",
                "audio": "Phép chiếu song song giữ nguyên tính thẳng hàng và song song, nhưng không giữ nguyên số đo góc hay khoảng cách.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Hình biểu diễn của hình phẳng",
                        "problem": "Hình chiếu song song của một hình chữ nhật có thể là hình gì?",
                        "solution": "- Do bảo toàn tính song song của các cạnh đối diện nhưng không bảo toàn góc vuông, hình chiếu của hình chữ nhật là một hình bình hành."
                    }
                ],
                "exercise": {"id": "11_14_1", "title": "Kiểm minh chứng", "content": "Phép chiếu song song có luôn bảo toàn số đo góc vuông không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Hình biểu diễn của một hình không gian": {
                "theory": "Hình biểu diễn của đường tròn là hình elip. Hình biểu diễn của tam giác đều, tam giác cân thường là tam giác thường. Quy ước: Đường nhìn thấy vẽ nét liền, đường bị che khuất vẽ nét đứt.",
                "formula": r"\text{Đường tròn } \to \text{Hình Elip; } \text{Bị khuất } \to \text{Nét đứt}",
                "trap": "Vẽ hình học không gian tuyệt đối không được vẽ nét liền cho các đoạn thẳng bị khuất ở phía sau.",
                "audio": "Đường nhìn thấy vẽ nét liền, đường bị che khuất vẽ nét đứt. Tròn vẽ thành elip, vuông vẽ thành bình hành.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Biểu diễn hình học",
                        "problem": "Khi vẽ hình chóp đáy là hình vuông, ta vẽ đáy là hình gì?",
                        "solution": "- Đáy được vẽ biểu diễn bằng hình bình hành."
                    }
                ],
                "exercise": {"id": "11_14_2", "title": "Kiểm minh chứng", "content": "Hình biểu diễn của đường tròn trong phép chiếu song song thường là hình elip. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 15: Giới hạn của dãy số": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Giới hạn hữu hạn của dãy số": {
                "theory": "Các giới hạn cơ bản khi $n \\to +\\infty$: $\\lim \\frac{1}{n^k} = 0$ ($k > 0$); $\\lim q^n = 0$ ($|q| < 1$). Quy tắc tính giới hạn phân thức đại số: Chia cả tử và mẫu cho lũy thừa bậc cao nhất của n.",
                "formula": r"\lim_{n \to +\infty} \frac{1}{n} = 0; \quad \lim_{n \to +\infty} q^n = 0 \ (|q| < 1)",
                "trap": "Giới hạn $\\lim q^n = 0$ chỉ đúng khi $|q| < 1$. Nếu $q > 1$ thì giới hạn tiến ra $+\\infty$.",
                "audio": "Giới hạn phân thức chứa n tiến ra vô cực, em cứ chia cả tử và mẫu cho n với số mũ cao nhất là bài toán được giải quyết.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giới hạn phân thức",
                        "problem": "Tính giới hạn $\\lim \\frac{6n + 1}{2n - 3}$.",
                        "solution": "- Chia cả tử và mẫu cho $n$: $\\lim \\frac{6 + 1/n}{2 - 3/n} = \\frac{6 + 0}{2 - 0} = 3$."
                    }
                ],
                "exercise": {"id": "11_15_1", "title": "Kiểm minh chứng", "content": "Giới hạn lim (4n - 1)/(2n + 5) bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Tổng của cấp số nhân lùi vô hạn": {
                "theory": "Cấp số nhân có công bội thỏa mãn $|q| < 1$ gọi là lùi vô hạn. Tổng của vô hạn các số hạng của nó hội tụ về một số thực: $S = \\frac{u_1}{1 - q}$.",
                "formula": r"S = u_1 + u_1 q + u_1 q^2 + \dots = \frac{u_1}{1 - q} \ (|q| < 1)",
                "trap": "Không được dùng công thức này nếu $|q| \\ge 1$, vì khi đó tổng phân kỳ ra vô cực.",
                "audio": "Tổng cấp số nhân lùi vô hạn bằng số hạng đầu chia cho 1 trừ đi công bội q. Công thức ngắn gọn và rất hay xuất hiện trong đề thi.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng chuỗi số",
                        "problem": "Tính tổng $S = 1 + \\frac{1}{2} + \\frac{1}{4} + \\dots$",
                        "solution": "- Ta có $u_1 = 1, q = 1/2 < 1$.\n- Áp dụng: $S = \\frac{1}{1 - 1/2} = 2$."
                    }
                ],
                "exercise": {"id": "11_15_2", "title": "Kiểm minh chứng", "content": "Tổng vô hạn của cấp số nhân u1 = 3, q = 1/2 bằng:", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 16: Giới hạn của hàm số": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Giới hạn hữu hạn của hàm số tại một điểm (Dạng 0/0)": {
                "theory": "Khi thay $x = x_0$ vào hàm phân thức được dạng $\\frac{0}{0}$ (dạng vô định), ta khử dạng vô định bằng cách phân tích tử và mẫu thành nhân tử chứa $(x - x_0)$ rồi triệt tiêu, hoặc nhân lượng liên hợp nếu có căn thức.",
                "formula": r"\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{(x - x_0)P(x)}{(x - x_0)Q(x)} = \lim_{x \to x_0} \frac{P(x)}{Q(x)}",
                "trap": "Gặp dạng $\\frac{0}{0}$ vội kết luận giới hạn bằng 0 hoặc không tồn tại là sai. Phải phân tích nhân tử để khử dạng vô định trước.",
                "audio": "Gặp dạng không chia không, hãy dùng hằng đẳng thức hoặc nhân liên hợp để triệt tiêu nhân tử chung làm cho mẫu bằng không.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Khử dạng vô định 0/0",
                        "problem": "Tính $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2}$.",
                        "solution": "- Dạng 0/0 tại $x = 2$.\n- $\\lim_{x \\to 2} \\frac{(x - 2)(x + 2)}{x - 2} = \\lim_{x \\to 2} (x + 2) = 4$."
                    }
                ],
                "exercise": {"id": "11_16_1", "title": "Kiểm minh chứng", "content": "Tính giới hạn lim(x^2 - 1)/(x - 1) khi x tiến tới 1.", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Giới hạn một bên và Giới hạn tại vô cực": {
                "theory": "Giới hạn bên phải $\\lim_{x \\to x_0^+} f(x)$ và bên trái $\\lim_{x \\to x_0^-} f(x)$. Giới hạn $\\lim_{x \\to x_0} f(x) = L$ khi và chỉ khi giới hạn trái và phải cùng tồn tại và BẰNG NHAU. Giới hạn tại vô cực làm tương tự giới hạn của dãy số.",
                "formula": r"\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L",
                "trap": "Nếu giới hạn bên trái và bên phải ra hai kết quả khác nhau thì kết luận hàm số KHÔNG TỒN TẠI giới hạn tại điểm đó.",
                "audio": "Giới hạn bên trái và bên phải phải bằng nhau thì giới hạn chung tại điểm đó mới thực sự tồn tại.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giới hạn một bên",
                        "problem": "Tính $\\lim_{x \\to 1^+} \\frac{1}{x - 1}$.",
                        "solution": "- Khi $x \\to 1^+$, tử số bằng 1 (>0), mẫu số $x - 1 > 0$ và tiến dần về 0.\n- Kết quả giới hạn là $+\\infty$."
                    }
                ],
                "exercise": {"id": "11_16_2", "title": "Kiểm minh chứng", "content": "Nếu giới hạn trái bằng 4 và giới hạn phải bằng 4 thì giới hạn tại điểm đó bằng:", "type": "NUMERIC", "target": "4", "options": []}
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 (PHẦN 2: BÀI 17 -> BÀI 33)
# Chuẩn hóa theo Vở tự học: Các chủ điểm là mục 1, 2, 3... thuộc PHẦN I
# ==============================================================================

GRADE_11_DATA.update({
    "Bài 17: Hàm số liên tục": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Hàm số liên tục tại một điểm": {
                "theory": "Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa $x_0$. Hàm số được gọi là liên tục tại điểm $x_0$ nếu giới hạn của hàm số khi $x$ dần tới $x_0$ bằng giá trị của hàm số tại $x_0$. Nếu điều kiện này không thỏa mãn thì hàm số bị gián đoạn tại $x_0$.",
                "formula": r"\lim_{x \to x_0} f(x) = f(x_0)",
                "trap": "Học sinh thường chỉ tính $\\lim_{x \\to x_0} f(x)$ mà quên tính $f(x_0)$. Để hàm số liên tục, hai giá trị này bắt buộc phải cùng tồn tại và bằng nhau.",
                "audio": "Hàm số liên tục tại một điểm khi giới hạn tại điểm đó bằng đúng giá trị của hàm số. Đồ thị của nó là một đường liền nét không bị ngắt quãng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính liên tục tại một điểm",
                        "problem": "Xét tính liên tục của hàm số $f(x) = x^2 + 2x$ tại điểm $x_0 = 1$.",
                        "solution": "- Tập xác định: $D = \\mathbb{R}$, chứa $x_0 = 1$.\n- Tính giá trị: $f(1) = 1^2 + 2(1) = 3$.\n- Tính giới hạn: $\\lim_{x \\to 1} (x^2 + 2x) = 1^2 + 2(1) = 3$.\n- Vì $\\lim_{x \\to 1} f(x) = f(1) = 3$, nên hàm số liên tục tại $x_0 = 1$."
                    }
                ],
                "exercise": {"id": "11_17_1", "title": "Kiểm minh chứng", "content": "Để hàm số f(x) = 3x khi x khác 0 và f(x) = m khi x = 0 liên tục tại x = 0 thì m bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Hàm số liên tục trên khoảng và Định lí giá trị trung gian": {
                "theory": "Hàm số đa thức, phân thức hữu tỉ, lượng giác liên tục trên từng khoảng xác định của chúng. Định lí giá trị trung gian: Nếu $f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \\cdot f(b) < 0$ thì phương trình $f(x) = 0$ có ít nhất một nghiệm thuộc khoảng $(a; b)$.",
                "formula": r"f(a) \cdot f(b) < 0 \implies \exists c \in (a; b): f(c) = 0",
                "trap": "Khi áp dụng định lí chứng minh phương trình có nghiệm, học sinh hay quên nêu điều kiện 'Hàm số $f(x)$ liên tục trên đoạn $[a; b]$'.",
                "audio": "Nếu hàm số đi liền nét từ giá trị âm sang giá trị dương trên một đoạn, chắc chắn đồ thị phải cắt trục hoành ít nhất một lần.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh phương trình có nghiệm",
                        "problem": "Chứng minh phương trình $x^3 + 2x - 1 = 0$ có ít nhất một nghiệm trong khoảng $(0; 1)$.",
                        "solution": "- Hàm số $f(x) = x^3 + 2x - 1$ là hàm đa thức nên liên tục trên $[0; 1]$.\n- Ta có $f(0) = -1 < 0$ và $f(1) = 2 > 0$.\n- Vì $f(0) \\cdot f(1) = -2 < 0$, nên phương trình có ít nhất một nghiệm thuộc khoảng $(0; 1)$."
                    }
                ],
                "exercise": {"id": "11_17_2", "title": "Kiểm minh chứng", "content": "Hàm số f(x) = x^3 - 3 liên tục trên [1; 2]. Giá trị f(1).f(2) bằng:", "type": "NUMERIC", "target": "-10", "options": []}
            }
        }
    },
    "Bài 18: Lũy thừa với số mũ thực": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Lũy thừa với số mũ nguyên và số mũ hữu tỉ": {
                "theory": "Với số nguyên dương $n$: $a^n = a \\cdot a \\dots a$. Với $a \\neq 0$: $a^0 = 1, a^{-n} = \\frac{1}{a^n}$. Căn bậc $n$ của số $a > 0$ lũy thừa $m$ được viết dưới dạng số mũ hữu tỉ: $a^{\\frac{m}{n}} = \\sqrt[n]{a^m}$.",
                "formula": r"a^{\frac{m}{n}} = \sqrt[n]{a^m} \ (a > 0); \quad a^{-n} = \frac{1}{a^n} \ (a \neq 0)",
                "trap": "Lũy thừa với số mũ hữu tỉ $a^{\\frac{m}{n}}$ chỉ xác định khi cơ số $a > 0$. Số âm không có lũy thừa số mũ không nguyên.",
                "audio": "Nhân hai lũy thừa cùng cơ số thì cộng số mũ, chia thì trừ số mũ. Chú ý điều kiện cơ số phải dương khi chuyển từ căn sang số mũ hữu tỉ.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chuyển căn sang số mũ hữu tỉ",
                        "problem": "Rút gọn biểu thức $P = x \\cdot \\sqrt[3]{x}$ với $x > 0$.",
                        "solution": "- Ta viết lại căn: $\\sqrt[3]{x} = x^{\\frac{1}{3}}$.\n- $P = x^1 \\cdot x^{\\frac{1}{3}} = x^{1 + \\frac{1}{3}} = x^{\\frac{4}{3}}$."
                    }
                ],
                "exercise": {"id": "11_18_1", "title": "Kiểm minh chứng", "content": "Rút gọn x^2 * x^(1/3) được x^(c/3). Giá trị c bằng:", "type": "NUMERIC", "target": "7", "options": []}
            },
            "2. Lũy thừa với số mũ thực và Các tính chất": {
                "theory": "Với $a, b > 0$ và $\\alpha, \\beta \\in \\mathbb{R}$: $a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}$; $\\frac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}$; $(a^\\alpha)^\\beta = a^{\\alpha\\beta}$; $(ab)^\\alpha = a^\\alpha b^\\alpha$. So sánh: Với $a > 1$, $a^\\alpha > a^\\beta \\iff \\alpha > \\beta$. Với $0 < a < 1$, $a^\\alpha > a^\\beta \\iff \\alpha < \\beta$.",
                "formula": r"(a^\alpha)^\beta = a^{\alpha\beta}; \quad a > 1 \implies (a^\alpha > a^\beta \iff \alpha > \beta)",
                "trap": "Học sinh hay nhầm lẫn $(a^\\alpha)^\\beta = a^{\\alpha + \\beta}$. Lũy thừa của lũy thừa phải NHÂN hai số mũ, không phải cộng.",
                "audio": "Lũy thừa của lũy thừa thì nhân hai số mũ lại với nhau. Khi so sánh hai lũy thừa cùng cơ số nhỏ hơn một, nhớ đảo chiều bất đẳng thức.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính toán lũy thừa số mũ thực",
                        "problem": "Tính giá trị của biểu thức $A = (2^{\\sqrt{3}})^{\\sqrt{3}}$.",
                        "solution": "- Áp dụng tính chất nhân số mũ: $A = 2^{\\sqrt{3} \\cdot \\sqrt{3}} = 2^3 = 8$."
                    }
                ],
                "exercise": {"id": "11_18_2", "title": "Kiểm minh chứng", "content": "Giá trị của (3^(căn 2))^(căn 2) bằng bao nhiêu?", "type": "NUMERIC", "target": "9", "options": []}
            }
        }
    },
    "Bài 19: Lôgarit": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khái niệm và Tính chất cơ bản của lôgarit": {
                "theory": "Cho $0 < a \\neq 1, b > 0$. Số $\\alpha$ thỏa mãn $a^\\alpha = b$ được gọi là lôgarit cơ số $a$ của $b$, kí hiệu $\\log_a b$. Các hệ thức cơ bản: $\\log_a 1 = 0$, $\\log_a a = 1$, $a^{\\log_a b} = b$, $\\log_a(a^\\alpha) = \\alpha$.",
                "formula": r"\log_a b = \alpha \iff a^\alpha = b \quad (0 < a \neq 1, b > 0)",
                "trap": "Biểu thức dưới dấu lôgarit bắt buộc phải DƯƠNG nghiêm ngặt ($b > 0$). Không tồn tại lôgarit của số âm hoặc số 0.",
                "audio": "Lôgarit cơ số a của b chính là số mũ để khi lấy a nâng lên lũy thừa đó thì ra b. Cơ số phải dương khác một và biểu thức trong log phải dương.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính lôgarit theo định nghĩa",
                        "problem": "Tính giá trị của biểu thức $\\log_2 32$.",
                        "solution": "- Ta có $32 = 2^5$. Do đó $\\log_2 32 = \\log_2(2^5) = 5$."
                    }
                ],
                "exercise": {"id": "11_19_1", "title": "Kiểm minh chứng", "content": "Giá trị của log_5(125) bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            },
            "2. Các quy tắc tính và Công thức đổi cơ số": {
                "theory": "Quy tắc: $\\log_a(xy) = \\log_a x + \\log_a y$; $\\log_a(x/y) = \\log_a x - \\log_a y$; $\\log_a(x^\\alpha) = \\alpha\\log_a x$. Đổi cơ số: $\\log_a b = \\frac{\\log_c b}{\\log_c a}$; $\\log_{a^\\beta} b = \\frac{1}{\\beta}\\log_a b$; $\\log_a b = \\frac{1}{\\log_b a}$.",
                "formula": r"\log_a(xy) = \log_a x + \log_a y; \quad \log_a b = \frac{\log_c b}{\log_c a}; \quad \log_{a^\beta} b = \frac{1}{\beta}\log_a b",
                "trap": "Lôgarit của một tổng KHÔNG BẰNG tổng các lôgarit. Tức là $\\log_a(x + y) \\neq \\log_a x + \\log_a y$.",
                "audio": "Log của một tích bằng tổng hai log, log của một thương bằng hiệu hai log. Số mũ ở cơ số đưa ra ngoài nhớ nghịch đảo thành một phần beta.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc tính lôgarit",
                        "problem": "Tính giá trị của $P = \\log_2 6 - \\log_2 3$.",
                        "solution": "- Áp dụng log của thương: $P = \\log_2\\left(\\frac{6}{3}\\right) = \\log_2 2 = 1$."
                    }
                ],
                "exercise": {"id": "11_19_2", "title": "Kiểm minh chứng", "content": "Giá trị của biểu thức log_3(2) * log_2(9) bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 20: Hàm số mũ và hàm số lôgarit": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Hàm số mũ": {
                "theory": "Hàm số mũ $y = a^x$ ($0 < a \\neq 1$) có TXĐ $D = \\mathbb{R}$, tập giá trị $(0; +\\infty)$. Đạo hàm: $(a^x)' = a^x \\ln a$, $(e^x)' = e^x$. Chiều biến thiên: Nếu $a > 1$, hàm số đồng biến trên $\\mathbb{R}$; nếu $0 < a < 1$, hàm số nghịch biến trên $\\mathbb{R}$. Đồ thị đi qua điểm $(0; 1)$ và nhận trục hoành làm tiệm cận ngang.",
                "formula": r"y = a^x > 0, \forall x \in \mathbb{R}; \quad (a^x)' = a^x \ln a",
                "trap": "Hàm số mũ luôn nhận giá trị dương. Khi đặt ẩn phụ $t = a^x$, học sinh thường quên đặt điều kiện $t > 0$.",
                "audio": "Hàm số mũ luôn dương và đồ thị luôn nằm phía trên trục hoành. Cơ số lớn hơn một hàm đồng biến, nhỏ hơn một hàm nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đơn điệu hàm số mũ",
                        "problem": "Hàm số $y = (0.2)^x$ đồng biến hay nghịch biến trên $\\mathbb{R}$?",
                        "solution": "- Cơ số $a = 0.2 \\in (0; 1)$ nên hàm số nghịch biến trên $\\mathbb{R}$."
                    }
                ],
                "exercise": {"id": "11_20_1", "title": "Kiểm minh chứng", "content": "Đồ thị hàm số y = 4^x đi qua điểm (0; c). Giá trị c bằng:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Hàm số lôgarit": {
                "theory": "Hàm số lôgarit $y = \\log_a x$ ($0 < a \\neq 1$) có TXĐ $D = (0; +\\infty)$, tập giá trị $\\mathbb{R}$. Đạo hàm: $(\\log_a x)' = \\frac{1}{x\\ln a}$, $(\\ln x)' = \\frac{1}{x}$. Chiều biến thiên: Nếu $a > 1$, đồng biến trên $(0; +\\infty)$; nếu $0 < a < 1$, nghịch biến trên $(0; +\\infty)$. Đồ thị đi qua điểm $(1; 0)$ và nhận trục tung làm tiệm cận đứng.",
                "formula": r"y = \log_a x \implies \text{TXĐ: } x > 0; \quad (\ln x)' = \frac{1}{x}",
                "trap": "Học sinh hay quên điều kiện biểu thức trong logarit phải lớn hơn 0 khi tìm tập xác định của hàm số lôgarit dạng hợp.",
                "audio": "Hàm số lôgarit chỉ xác định cho biến số dương. Đồ thị đi qua điểm một không trên trục hoành và nhận trục tung làm tiệm cận đứng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định của hàm lôgarit",
                        "problem": "Tìm tập xác định của hàm số $y = \\log_3(x - 2)$.",
                        "solution": "- Điều kiện xác định: $x - 2 > 0 \\iff x > 2$.\n- Vậy tập xác định là $D = (2; +\\infty)$."
                    }
                ],
                "exercise": {"id": "11_20_2", "title": "Kiểm minh chứng", "content": "Tập xác định của y = ln(x - 4) có dạng (c; +vô cực). Giá trị c bằng:", "type": "NUMERIC", "target": "4", "options": []}
            }
        }
    },
    "Bài 21: Phương trình, bất phương trình mũ và lôgarit": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phương trình mũ và Phương trình lôgarit cơ bản": {
                "theory": "Phương trình $a^x = b$: Nếu $b > 0 \\implies x = \\log_a b$; nếu $b \\le 0 \\implies$ Vô nghiệm. Phương trình $\\log_a x = b \\iff x = a^b$. Phương trình cùng cơ số: $\\log_a f(x) = \\log_a g(x) \\iff \\begin{cases} f(x) > 0 \\\\ f(x) = g(x) \\end{cases}$.",
                "formula": r"a^{f(x)} = a^{g(x)} \iff f(x) = g(x); \quad \log_a f(x) = b \iff f(x) = a^b",
                "trap": "Giải phương trình lôgarit bắt buộc phải đặt điều kiện biểu thức trong dấu logarit dương trước khi biến đổi giải phương trình.",
                "audio": "Giải phương trình mũ bằng cách đưa về cùng cơ số hoặc lấy logarit. Phương trình lôgarit thì bước đầu tiên luôn là đặt điều kiện xác định.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình logarit cơ bản",
                        "problem": "Giải phương trình $\\log_2(2x - 1) = 3$.",
                        "solution": "- Điều kiện: $2x - 1 > 0 \\iff x > 1/2$.\n- Đội mũ hai vế: $2x - 1 = 2^3 = 8 \\iff 2x = 9 \\iff x = 4.5$ (thỏa mãn)."
                    }
                ],
                "exercise": {"id": "11_21_1", "title": "Kiểm minh chứng", "content": "Nghiệm của phương trình 3^(x - 2) = 9 là x bằng:", "type": "NUMERIC", "target": "4", "options": []}
            },
            "2. Bất phương trình mũ và Bất phương trình lôgarit cơ bản": {
                "theory": "Quy tắc so sánh: Khi cơ số $a > 1$, GIỮ NGUYÊN chiều BPT. Khi cơ số $0 < a < 1$, ĐỔI CHIỀU BPT. Chú ý với logarit: $\\log_a f(x) > b$: Nếu $0 < a < 1 \\implies 0 < f(x) < a^b$ (phải chặn lớn hơn 0).",
                "formula": r"a > 1: a^{f(x)} > a^{g(x)} \iff f(x) > g(x); \quad 0 < a < 1: a^{f(x)} > a^{g(x)} \iff f(x) < g(x)",
                "trap": "Quên đổi chiều BPT khi cơ số $a < 1$. Quên đặt điều kiện $f(x) > 0$ khi giải BPT lôgarit dạng $\\log_a f(x) < b$.",
                "audio": "Nhìn cơ số trước khi phá mũ hay logarit. Cơ số lớn hơn một giữ nguyên chiều, nhỏ hơn một nhớ quay ngược chiều lại.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bất phương trình cơ số nhỏ hơn 1",
                        "problem": "Giải bất phương trình $(0.5)^x < 0.25$.",
                        "solution": "- Viết lại: $(0.5)^x < (0.5)^2$.\n- Vì cơ số $0.5 < 1$, đổi chiều bất phương trình: $x > 2$."
                    }
                ],
                "exercise": {"id": "11_21_2", "title": "Kiểm minh chứng", "content": "Tập nghiệm của (1/2)^x < 1/8 là x > c. Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 22: Hai đường thẳng vuông góc": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Góc giữa hai đường thẳng trong không gian": {
                "theory": "Góc giữa hai đường thẳng $a$ và $b$ là góc giữa hai đường thẳng $a', b'$ cùng đi qua một điểm và lần lượt song song với $a, b$. Số đo góc luôn thuộc đoạn $[0^\\circ; 90^\\circ]$. Công thức cosin qua vectơ chỉ phương: $\\cos\\varphi = \\frac{|\\vec{u} \\cdot \\vec{v}|}{|\\vec{u}| \\cdot |\\vec{v}|}$.",
                "formula": r"0^\circ \le \widehat{(a, b)} \le 90^\circ; \quad \cos\widehat{(a, b)} = \frac{|\vec{u_a} \cdot \vec{u_b}|}{|\vec{u_a}| \cdot |\vec{u_b}|}",
                "trap": "Góc giữa 2 vectơ chỉ phương có thể là góc tù, nhưng góc giữa 2 đường thẳng KHÔNG BAO GIỜ là góc tù. Tử số bắt buộc có trị tuyệt đối.",
                "audio": "Góc giữa hai đường thẳng trong không gian luôn là góc nhọn hoặc góc vuông, tối đa chỉ bằng chín mươi độ.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa hai đường thẳng chéo nhau",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D'. Tính góc giữa AB và B'C'.",
                        "solution": "- Vì $B'C' \\parallel BC$ nên góc giữa AB và B'C' chính là góc giữa AB và BC.\n- ABCD là hình vuông nên $\\widehat{ABC} = 90^\\circ$."
                    }
                ],
                "exercise": {"id": "11_22_1", "title": "Kiểm minh chứng", "content": "Hình lập phương ABCD.A'B'C'D'. Góc giữa A'B' và AD bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "2. Hai đường thẳng vuông góc trong không gian": {
                "theory": "Hai đường thẳng $a$ và $b$ gọi là vuông góc với nhau nếu góc giữa chúng bằng $90^\\circ$, kí hiệu $a \\perp b$. Điều kiện: Tích vô hướng của hai vectơ chỉ phương bằng 0. Trong không gian, hai đường thẳng vuông góc có thể cắt nhau hoặc chéo nhau.",
                "formula": r"a \perp b \iff \vec{u_a} \cdot \vec{u_b} = 0",
                "trap": "Học sinh thường ngộ nhận hai đường thẳng vuông góc thì phải CẮT NHAU. Trong không gian chúng hoàn toàn có thể chéo nhau.",
                "audio": "Hai đường thẳng vuông góc khi tích vô hướng của hai vectơ chỉ phương bằng không. Chúng có thể cắt nhau hoặc chéo nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận định vuông góc",
                        "problem": "Cho tứ diện ABCD có $AB \\perp CD$. Tích vô hướng $\\vec{AB} \\cdot \\vec{CD}$ bằng bao nhiêu?",
                        "solution": "- Do hai đường thẳng vuông góc nên $\\vec{AB} \\cdot \\vec{CD} = 0$."
                    }
                ],
                "exercise": {"id": "11_22_2", "title": "Kiểm minh chứng", "content": "Nếu u . v = 0 thì góc giữa hai đường thẳng tương ứng bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 23: Đường thẳng vuông góc với mặt phẳng": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Điều kiện để đường thẳng vuông góc với mặt phẳng": {
                "theory": "Đường thẳng $d$ vuông góc với mặt phẳng $(P)$ nếu $d$ vuông góc với HAI đường thẳng CẮT NHAU nằm trong $(P)$. Khi đó, $d$ vuông góc với MỌI đường thẳng nằm trong mặt phẳng $(P)$.",
                "formula": r"\begin{cases} d \perp a, d \perp b \\ a \cap b = I; \ a, b \subset (P) \end{cases} \implies d \perp (P)",
                "trap": "Chỉ chỉ ra được $d$ vuông góc với hai đường thẳng SONG SONG trong $(P)$ thì chưa đủ điều kiện kết luận vuông góc với mặt phẳng.",
                "audio": "Muốn chứng minh đường vuông góc với mặt, em phải chỉ ra nó vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng đó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường vuông góc mặt",
                        "problem": "Cho chóp S.ABC có $SA \\perp (ABC)$, đáy ABC vuông tại B. Chứng minh $BC \\perp (SAB)$.",
                        "solution": "- Ta có $BC \\perp AB$ (do đáy vuông tại B).\n- Lại có $BC \\perp SA$ (do $SA \\perp (ABC)$).\n- Vì AB và SA cắt nhau tại A trong $(SAB)$, nên $BC \\perp (SAB)$."
                    }
                ],
                "exercise": {"id": "11_23_1", "title": "Kiểm minh chứng", "content": "Để d vuông góc (P) thì d cần vuông góc với tối thiểu mấy đường thẳng cắt nhau trong (P)?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Mối liên hệ giữa quan hệ song song và quan hệ vuông góc": {
                "theory": "Tính chất: (1) Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song với nhau; (2) Mặt phẳng nào vuông góc với một trong hai đường thẳng song song thì vuông góc với đường còn lại; (3) Hai mặt phẳng phân biệt cùng vuông góc với một đường thẳng thì song song với nhau.",
                "formula": r"a \perp (P), b \perp (P) \implies a \parallel b; \quad a \parallel b, (P) \perp a \implies (P) \perp b",
                "trap": "Nhầm lẫn: Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì song song (sai trong không gian).",
                "audio": "Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song với nhau. Hai mặt phẳng cùng vuông góc với một đường thẳng cũng song song với nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện quan hệ",
                        "problem": "Cho đường thẳng $a \\perp (P)$ và đường thẳng $b \\parallel a$. Hỏi $b$ có vuông góc với $(P)$ không?",
                        "solution": "- Theo tính chất: Đường thẳng $b$ cũng vuông góc với $(P)$."
                    }
                ],
                "exercise": {"id": "11_23_2", "title": "Kiểm minh chứng", "content": "Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phép chiếu vuông góc và Định lí ba đường vuông góc": {
                "theory": "Phép chiếu song song có phương chiếu vuông góc với mặt phẳng chiếu gọi là phép chiếu vuông góc. Định lí ba đường vuông góc: Cho đường thẳng $a$ nằm trong $(P)$ và đường xiên $d$. Khi đó $a \\perp d \\iff a \\perp d'$ (với $d'$ là hình chiếu vuông góc của $d$ trên $(P)$).",
                "formula": r"a \subset (P) \implies (a \perp d \iff a \perp d')",
                "trap": "Đường thẳng $a$ bắt buộc phải NẰM TRONG mặt phẳng chiếu $(P)$ thì định lí ba đường vuông góc mới áp dụng được.",
                "audio": "Định lí ba đường vuông góc cho phép thay việc chứng minh vuông góc với đường xiên bằng chứng minh vuông góc với hình chiếu của nó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm hình chiếu vuông góc",
                        "problem": "Cho hình chóp S.ABC có $SA \\perp (ABC)$. Hình chiếu vuông góc của đoạn thẳng SB lên mặt phẳng (ABC) là đoạn nào?",
                        "solution": "- Hình chiếu của S lên (ABC) là A.\n- Hình chiếu của B lên (ABC) là B.\n- Vậy hình chiếu của đoạn thẳng SB là đoạn thẳng AB."
                    }
                ],
                "exercise": {"id": "11_24_1", "title": "Kiểm minh chứng", "content": "Cho chóp S.ABC có SA vuông góc đáy. Hình chiếu của SC lên (ABC) là cạnh nào? (Nhập tên cạnh)", "type": "STRING", "target": "AC", "options": []}
            },
            "2. Góc giữa đường thẳng và mặt phẳng": {
                "theory": "Nếu $d \\perp (P)$ thì góc bằng $90^\\circ$. Nếu $d$ không vuông góc $(P)$, góc giữa $d$ và $(P)$ là góc giữa $d$ và hình chiếu vuông góc $d'$ của nó trên $(P)$. Số đo góc thuộc đoạn $[0^\\circ; 90^\\circ]$.",
                "formula": r"\widehat{(d, (P))} = \widehat{(d, d')} \quad (0^\circ \le \varphi \le 90^\circ)",
                "trap": "Xác định sai chân đường vuông góc hạ từ đỉnh xuống mặt phẳng sẽ dẫn đến kẻ sai đường hình chiếu $d'$.",
                "audio": "Góc giữa đường thẳng và mặt phẳng là góc tạo bởi đường thẳng đó và chiếc bóng hình chiếu vuông góc của nó trên mặt phẳng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa đường và mặt",
                        "problem": "Cho chóp S.ABC có $SA \\perp (ABC)$, $\\Delta SAB$ vuông cân tại A. Tính góc giữa SB và (ABC).",
                        "solution": "- Hình chiếu của SB lên (ABC) là AB.\n- Góc giữa SB và (ABC) là góc $\\widehat{SBA}$.\n- Vì $\\Delta SAB$ vuông cân tại A nên $\\widehat{SBA} = 45^\\circ$."
                    }
                ],
                "exercise": {"id": "11_24_2", "title": "Kiểm minh chứng", "content": "Đường thẳng vuông góc với mặt phẳng thì góc giữa chúng bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 25: Hai mặt phẳng vuông góc": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Điều kiện để hai mặt phẳng vuông góc": {
                "theory": "Hai mặt phẳng vuông góc nếu góc giữa chúng bằng $90^\\circ$. Điều kiện: Mặt phẳng $(P)$ vuông góc với $(Q)$ nếu $(P)$ chứa MỘT đường thẳng vuông góc với $(Q)$.",
                "formula": r"\begin{cases} a \subset (P) \\ a \perp (Q) \end{cases} \implies (P) \perp (Q)",
                "trap": "Học sinh hay nhầm lẫn: Chỉ cần tìm được một đường thẳng nằm trong mặt này vuông góc với mặt kia là đủ, không cần tìm hai đường.",
                "audio": "Muốn chứng minh hai mặt phẳng vuông góc, em chỉ cần tìm trong mặt phẳng này một đường thẳng đâm thẳng góc xuống mặt phẳng kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng vuông góc",
                        "problem": "Cho chóp S.ABCD có $SA \\perp (ABCD)$. Chứng minh $(SAB) \\perp (ABCD)$.",
                        "solution": "- Mặt phẳng $(SAB)$ chứa đường thẳng $SA$.\n- Mà $SA \\perp (ABCD)$ theo giả thiết.\n- Suy ra $(SAB) \\perp (ABCD)$."
                    }
                ],
                "exercise": {"id": "11_25_1", "title": "Kiểm minh chứng", "content": "Hình hộp chữ nhật có các mặt bên vuông góc với mặt đáy. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Tính chất của hai mặt phẳng vuông góc": {
                "theory": "Nếu hai mặt phẳng vuông góc thì bất kỳ đường thẳng nào nằm trong mặt này mà VUÔNG GÓC VỚI GIAO TUYẾN thì sẽ vuông góc với mặt phẳng kia. Nếu hai mặt phẳng cắt nhau cùng vuông góc với mặt thứ ba thì giao tuyến của chúng vuông góc với mặt thứ ba.",
                "formula": r"\begin{cases} (P) \perp (Q); \ (P) \cap (Q) = d \\ a \subset (P); \ a \perp d \end{cases} \implies a \perp (Q)",
                "trap": "Đường thẳng nằm trong mặt thứ nhất bắt buộc phải vuông góc với GIAO TUYẾN thì mới vuông góc với mặt phẳng thứ hai.",
                "audio": "Hai mặt phẳng vuông góc thì đường thẳng nào nằm trong mặt này mà vuông góc với giao tuyến sẽ vuông góc với toàn bộ mặt phẳng kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng tính chất giao tuyến",
                        "problem": "Cho $(SAB) \\perp (ABC)$ theo giao tuyến AB. Kẻ $SH \\perp AB$ ($H \\in AB$). Kết luận gì về SH?",
                        "solution": "- Vì $SH \\subset (SAB)$ và $SH \\perp AB$ (giao tuyến) nên $SH \\perp (ABC)$."
                    }
                ],
                "exercise": {"id": "11_25_2", "title": "Kiểm minh chứng", "content": "Hai mặt phẳng vuông góc tạo với nhau một góc bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 26: Khoảng cách trong không gian": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khoảng cách từ một điểm đến mặt phẳng": {
                "theory": "Khoảng cách từ $M$ đến mặt phẳng $(P)$ là độ dài đoạn vuông góc $MH$ ($H \\in (P)$). Phương pháp dời điểm: Nếu đường thẳng $AB$ cắt $(P)$ tại $I$ thì $\\frac{d(A, (P))}{d(B, (P))} = \\frac{IA}{IB}$. Nếu $AB \\parallel (P)$ thì khoảng cách từ A và B đến $(P)$ bằng nhau.",
                "formula": r"\frac{d(A, (P))}{d(B, (P))} = \frac{IA}{IB} \quad (AB \cap (P) = I); \quad d(A, (P)) = d(B, (P)) \quad (AB \parallel (P))",
                "trap": "Kẻ bừa một đường xiên rồi ngộ nhận đó là khoảng cách. Phải dựng chân đường vuông góc chuẩn xác.",
                "audio": "Khoảng cách từ điểm đến mặt là đoạn vuông góc ngắn nhất. Em nên dời điểm cần tính về chân đường cao để tính bằng hệ thức lượng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách từ chân đường cao",
                        "problem": "Cho chóp S.ABC có $SA \\perp (ABC)$, $SA = 3$, $\\Delta ABC$ vuông tại B có $AB = 4$. Tính $d(A, (SBC))$.",
                        "solution": "- Kẻ $AH \\perp SB$. Do $BC \\perp (SAB) \\implies BC \\perp AH$. Suy ra $AH \\perp (SBC)$.\n- $\\frac{1}{AH^2} = \\frac{1}{SA^2} + \\frac{1}{AB^2} = \\frac{1}{9} + \\frac{1}{16} = \\frac{25}{144} \\implies AH = 2.4$."
                    }
                ],
                "exercise": {"id": "11_26_1", "title": "Kiểm minh chứng", "content": "Đoạn thẳng AB song song với mặt phẳng (P). Tỉ số d(A, (P)) / d(B, (P)) bằng:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Khoảng cách giữa hai đường thẳng chéo nhau": {
                "theory": "Khoảng cách giữa hai đường thẳng chéo nhau $a$ và $b$ bằng độ dài đoạn vuông góc chung của chúng, hoặc bằng khoảng cách từ đường thẳng $a$ đến mặt phẳng $(P)$ chứa $b$ và song song với $a$.",
                "formula": r"d(a, b) = d(a, (P)) \quad (b \subset (P), a \parallel (P))",
                "trap": "Đoạn vuông góc chung phải đồng thời cắt và vuông góc với CẢ HAI đường thẳng chéo nhau.",
                "audio": "Tính khoảng cách giữa hai đường chéo nhau bằng cách dựng mặt phẳng chứa đường này và song song với đường kia rồi quy về khoảng cách từ điểm.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đoạn vuông góc chung",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D' cạnh bằng 2. Khoảng cách giữa AA' và BC bằng bao nhiêu?",
                        "solution": "- Ta có $AB \\perp AA'$ và $AB \\perp BC$. Do đó AB là đoạn vuông góc chung.\n- Khoảng cách bằng độ dài $AB = 2$."
                    }
                ],
                "exercise": {"id": "11_26_2", "title": "Kiểm minh chứng", "content": "Đoạn vuông góc chung của 2 đường thẳng chéo nhau tạo với mỗi đường góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 27: Thể tích": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Thể tích khối lăng trụ và Khối chóp": {
                "theory": "Thể tích khối lăng trụ: $V = S_{\\text{đáy}} \\cdot h$. Thể tích khối chóp: $V = \\frac{1}{3} S_{\\text{đáy}} \\cdot h$. Thể tích khối chóp cụt: $V = \\frac{1}{3} h (B + B' + \\sqrt{BB'})$.",
                "formula": r"V_{\text{lăng trụ}} = S \cdot h; \quad V_{\text{chóp}} = \frac{1}{3} S \cdot h",
                "trap": "Học sinh rất hay quên nhân hệ số $\\frac{1}{3}$ khi tính thể tích của khối chóp.",
                "audio": "Khối chóp nhọn đầu thì có một phần ba diện tích đáy nhân chiều cao. Khối lăng trụ hai đáy bằng nhau thì chỉ cần lấy đáy nhân cao.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính thể tích khối chóp",
                        "problem": "Khối chóp có diện tích đáy bằng $18\\text{ cm}^2$, chiều cao bằng $5\\text{ cm}$. Tính thể tích.",
                        "solution": "- $V = \\frac{1}{3} S \\cdot h = \\frac{1}{3} \\cdot 18 \\cdot 5 = 30\\text{ cm}^3$."
                    }
                ],
                "exercise": {"id": "11_27_1", "title": "Kiểm minh chứng", "content": "Khối chóp có diện tích đáy bằng 12, chiều cao bằng 4. Thể tích bằng bao nhiêu?", "type": "NUMERIC", "target": "16", "options": []}
            },
            "2. Tỉ số thể tích khối chóp tam giác (Định lí Simpson)": {
                "theory": "Cho hình chóp tam giác $S.ABC$. Lấy $A' \\in SA, B' \\in SB, C' \\in SC$. Khi đó: $\\frac{V_{S.A'B'C'}}{V_{S.ABC}} = \\frac{SA'}{SA} \\cdot \\frac{SB'}{SB} \\cdot \\frac{SC'}{SC}$.",
                "formula": r"\frac{V_{S.A'B'C'}}{V_{S.ABC}} = \frac{SA'}{SA} \cdot \frac{SB'}{SB} \cdot \frac{SC'}{SC}",
                "trap": "Định lí Simpson CHỈ ÁP DỤNG cho khối chóp có đáy là TAM GIÁC. Tuyệt đối không dùng trực tiếp cho đáy tứ giác.",
                "audio": "Tỉ số thể tích Simpson chỉ áp dụng cho chóp tam giác, bằng tích ba tỉ lệ cạnh bên nhân lại với nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng tỉ số Simpson",
                        "problem": "Cho chóp S.ABC có thể tích $V = 24$. M, N, P lần lượt là trung điểm của SA, SB, SC. Tính thể tích S.MNP.",
                        "solution": "- $\\frac{V_{S.MNP}}{V_{S.ABC}} = \\frac{1}{2} \\cdot \\frac{1}{2} \\cdot \\frac{1}{2} = \\frac{1}{8}$.\n- $V_{S.MNP} = 24 \\cdot \\frac{1}{8} = 3$."
                    }
                ],
                "exercise": {"id": "11_27_2", "title": "Kiểm minh chứng", "content": "Nếu M, N là trung điểm SA, SB; P trùng C thì tỉ số thể tích V(S.MNP)/V(S.ABC) bằng 1/c. c bằng:", "type": "NUMERIC", "target": "4", "options": []}
            }
        }
    },
    "Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Biến cố hợp và Biến cố giao": {
                "theory": "Biến cố hợp $A \\cup B$ xảy ra khi có ÍT NHẤT một trong hai biến cố A hoặc B xảy ra (hoặc A, hoặc B). Biến cố giao $AB$ (hay $A \\cap B$) xảy ra khi CẢ HAI biến cố A và B ĐỒNG THỜI xảy ra.",
                "formula": r"A \cup B \iff \text{A hoặc B xảy ra}; \quad AB \iff \text{Cả A và B cùng xảy ra}",
                "trap": "Nhầm lẫn giữa từ 'hoặc' (hợp) và từ 'và' (giao).",
                "audio": "Hợp là phép gộp, chỉ cần một biến cố xảy ra là được. Giao là phần chung, bắt buộc cả hai cùng phải xảy ra đồng thời.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định biến cố giao",
                        "problem": "Gieo một con xúc xắc. A: 'Số chấm chẵn', B: 'Số chấm chia hết cho 3'. Xác định biến cố AB.",
                        "solution": "- $A = \\{2; 4; 6\\}, B = \\{3; 6\\}$.\n- Biến cố giao $AB = A \\cap B = \\{6\\}$."
                    }
                ],
                "exercise": {"id": "11_28_1", "title": "Kiểm minh chứng", "content": "Hai biến cố xung khắc thì số phần tử của biến cố giao bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Biến cố độc lập": {
                "theory": "Hai biến cố A và B được gọi là độc lập nếu việc xảy ra (hay không xảy ra) của biến cố này không làm ảnh hưởng đến xác suất xảy ra của biến cố kia.",
                "formula": r"A, B \text{ độc lập} \implies P(AB) = P(A) \cdot P(B)",
                "trap": "Nhầm lẫn giữa 'độc lập' và 'xung khắc'. Xung khắc là không thể cùng xảy ra, độc lập là việc của ai người nấy làm không ảnh hưởng nhau.",
                "audio": "Hai biến cố độc lập khi việc biến cố này xảy ra hay không chẳng liên quan gì đến xác suất của biến cố kia.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất hai biến cố độc lập",
                        "problem": "Hai bạn An và Bình bắn súng độc lập. $P(An) = 0.8$, $P(Binh) = 0.7$. Tính xác suất cả hai bạn cùng bắn trúng.",
                        "solution": "- Do hai biến cố độc lập nên $P = P(An) \\cdot P(Binh) = 0.8 \\cdot 0.7 = 0.56$."
                    }
                ],
                "exercise": {"id": "11_28_2", "title": "Kiểm minh chứng", "content": "P(A) = 0.5, P(B) = 0.6 độc lập. Xác suất P(AB) bằng:", "type": "NUMERIC", "target": "0.3", "options": []}
            }
        }
    },
    "Bài 29: Công thức cộng xác suất": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Công thức cộng xác suất cho hai biến cố bất kì": {
                "theory": "Với hai biến cố A và B bất kì: $P(A \\cup B) = P(A) + P(B) - P(AB)$. Phải trừ đi phần giao $P(AB)$ để không bị tính lặp lại hai lần.",
                "formula": r"P(A \cup B) = P(A) + P(B) - P(AB)",
                "trap": "Học sinh thường quên trừ phần giao $P(AB)$, dẫn đến tính xác suất của biến cố hợp đôi khi vượt quá 1 (vô lý).",
                "audio": "Tính xác suất của biến cố hợp, em lấy xác suất của từng cái cộng lại rồi nhớ trừ đi phần giao chung.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất hợp",
                        "problem": "Cho $P(A) = 0.4, P(B) = 0.5, P(AB) = 0.1$. Tính $P(A \\cup B)$.",
                        "solution": "- $P(A \\cup B) = P(A) + P(B) - P(AB) = 0.4 + 0.5 - 0.1 = 0.8$."
                    }
                ],
                "exercise": {"id": "11_29_1", "title": "Kiểm minh chứng", "content": "P(A) = 0.6, P(B) = 0.3, P(AB) = 0.1. P(A hợp B) bằng bao nhiêu?", "type": "NUMERIC", "target": "0.8", "options": []}
            },
            "2. Công thức cộng cho hai biến cố xung khắc": {
                "theory": "Nếu hai biến cố A và B xung khắc (không thể cùng xảy ra, $AB = \\emptyset$) thì $P(AB) = 0$. Khi đó công thức cộng rút gọn thành: $P(A \\cup B) = P(A) + P(B)$.",
                "formula": r"A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B)",
                "trap": "Chỉ được cộng trực tiếp $P(A) + P(B)$ khi biết chắc chắn hai biến cố đó xung khắc nhau.",
                "audio": "Khi hai biến cố đã xung khắc sống chết có nhau thì phần giao bằng không, xác suất hợp chỉ bằng tổng hai xác suất.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Biến cố xung khắc",
                        "problem": "Rút một lá bài từ bộ 52 lá. A: 'Rút được lá Át', B: 'Rút được lá K'. Tính $P(A \\cup B)$.",
                        "solution": "- Rút 1 lá không thể vừa là Át vừa là K $\\implies A, B$ xung khắc.\n- $P(A \\cup B) = \\frac{4}{52} + \\frac{4}{52} = \\frac{8}{52} = \\frac{2}{13}$."
                    }
                ],
                "exercise": {"id": "11_29_2", "title": "Kiểm minh chứng", "content": "P(A) = 0.3, P(B) = 0.4. Biết A và B xung khắc. P(A hợp B) bằng:", "type": "NUMERIC", "target": "0.7", "options": []}
            }
        }
    },
    "Bài 30: Công thức nhân xác suất cho hai biến cố độc lập": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Công thức nhân xác suất": {
                "theory": "Hai biến cố A và B độc lập khi và chỉ khi xác suất của biến cố giao bằng tích xác suất của hai biến cố thành phần: $P(AB) = P(A) \\cdot P(B)$.",
                "formula": r"P(AB) = P(A) \cdot P(B)",
                "trap": "Công thức nhân $P(AB) = P(A) \\cdot P(B)$ CHỈ ĐƯỢC DÙNG khi hai biến cố độc lập với nhau.",
                "audio": "Công thức nhân xác suất áp dụng cho các biến cố độc lập: Xác suất đồng thời xảy ra bằng tích hai xác suất riêng biệt.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất đồng thời",
                        "problem": "Xác suất An thi đỗ là 0.9, Bình thi đỗ là 0.8 (độc lập). Tính xác suất cả hai bạn cùng đỗ.",
                        "solution": "- $P = P(An) \\cdot P(Binh) = 0.9 \\cdot 0.8 = 0.72$."
                    }
                ],
                "exercise": {"id": "11_30_1", "title": "Kiểm minh chứng", "content": "P(A) = 0.4, P(B) = 0.5 độc lập. Xác suất P(AB) bằng:", "type": "NUMERIC", "target": "0.2", "options": []}
            },
            "2. Biến cố đối và Xác suất có ít nhất một biến cố xảy ra": {
                "theory": "Nếu A và B độc lập thì $\\overline{A}$ và $\\overline{B}$ cũng độc lập. Để tính xác suất 'Có ít nhất một trong hai biến cố xảy ra', ta dùng biến cố đối: $P(A \\cup B) = 1 - P(\\overline{A}) \\cdot P(\\overline{B})$.",
                "formula": r"P(\text{Ít nhất một}) = 1 - P(\overline{A}) \cdot P(\overline{B})",
                "trap": "Bài toán có cụm từ 'ít nhất một' nếu tính trực tiếp phải chia nhiều trường hợp, dùng biến cố đối lấy 1 trừ đi sẽ nhanh và chính xác nhất.",
                "audio": "Gặp câu hỏi có ít nhất một biến cố xảy ra, em tính xác suất cả hai cùng không xảy ra rồi lấy một trừ đi.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bài toán ít nhất một người trúng",
                        "problem": "Hai xạ thủ bắn bia độc lập với xác suất trúng là 0.7 và 0.8. Tính xác suất có ít nhất một người bắn trúng.",
                        "solution": "- Xác suất cả hai cùng trượt: $P(\\text{cùng trượt}) = (1 - 0.7)(1 - 0.8) = 0.3 \\cdot 0.2 = 0.06$.\n- Xác suất ít nhất một người trúng: $P = 1 - 0.06 = 0.94$."
                    }
                ],
                "exercise": {"id": "11_30_2", "title": "Kiểm minh chứng", "content": "P(A) = 0.5, P(B) = 0.4 độc lập. Xác suất cả hai cùng không xảy ra bằng:", "type": "NUMERIC", "target": "0.3", "options": []}
            }
        }
    },
    "Bài 31: Định nghĩa và ý nghĩa của đạo hàm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa đạo hàm tại một điểm": {
                "theory": "Cho $y = f(x)$ xác định trên $(a; b)$ chứa $x_0$. Đạo hàm tại $x_0$ là giới hạn: $f'(x_0) = \\lim_{x \\to x_0} \\frac{f(x) - f(x_0)}{x - x_0} = \\lim_{\\Delta x \\to 0} \\frac{\\Delta y}{\\Delta x}$.",
                "formula": r"f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}",
                "trap": "Hàm số có đạo hàm tại $x_0$ thì liên tục tại $x_0$. Nhưng hàm số liên tục tại $x_0$ CHƯA CHẮC đã có đạo hàm tại điểm đó.",
                "audio": "Đạo hàm là tốc độ biến thiên tức thời của hàm số tại một điểm, được tính bằng giới hạn của tỉ số số gia.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính đạo hàm bằng định nghĩa",
                        "problem": "Tính đạo hàm của $f(x) = x^2$ tại $x_0 = 2$.",
                        "solution": "- $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} (x + 2) = 4$. Vậy $f'(2) = 4$."
                    }
                ],
                "exercise": {"id": "11_31_1", "title": "Kiểm minh chứng", "content": "Đạo hàm của hàm số f(x) = 3x tại điểm x_0 = 5 bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            },
            "2. Ý nghĩa hình học và Phương trình tiếp tuyến": {
                "theory": "Đạo hàm $f'(x_0)$ là hệ số góc của tiếp tuyến của đồ thị $(C): y = f(x)$ tại tiếp điểm $M_0(x_0; y_0)$. Phương trình tiếp tuyến: $y - y_0 = f'(x_0)(x - x_0)$.",
                "formula": r"y - y_0 = f'(x_0)(x - x_0); \quad k = f'(x_0)",
                "trap": "Nhầm lẫn giữa tiếp tuyến TẠI tiếp điểm $M_0(x_0; y_0) \\in (C)$ và tiếp tuyến ĐI QUA một điểm bên ngoài đồ thị.",
                "audio": "Hệ số góc của tiếp tuyến tại một điểm chính là giá trị của đạo hàm tại điểm đó. Nhớ công thức y trừ y không bằng k nhân x trừ x không.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết phương trình tiếp tuyến",
                        "problem": "Viết phương trình tiếp tuyến của $(C): y = x^2$ tại điểm $M(1; 1)$.",
                        "solution": "- Đạo hàm: $y' = 2x \\implies k = y'(1) = 2$.\n- Phương trình tiếp tuyến: $y - 1 = 2(x - 1) \\iff y = 2x - 1$."
                    }
                ],
                "exercise": {"id": "11_31_2", "title": "Kiểm minh chứng", "content": "Hệ số góc tiếp tuyến của y = x^3 tại điểm có hoành độ x_0 = 1 bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "3. Ý nghĩa vật lý của đạo hàm": {
                "theory": "Vận tốc tức thời của chuyển động thẳng bằng đạo hàm của phương trình quãng đường: $v(t) = s'(t)$.",
                "formula": r"v(t) = s'(t)",
                "trap": "Nhầm lẫn giữa vận tốc trung bình trên khoảng thời gian và vận tốc tức thời tại một thời điểm.",
                "audio": "Trong vật lý, đạo hàm của quãng đường theo thời gian chính là vận tốc tức thời của chuyển động.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính vận tốc tức thời",
                        "problem": "Một vật chuyển động có phương trình $s(t) = 3t^2 + 2t$ (m). Tính vận tốc tại thời điểm $t = 2$ s.",
                        "solution": "- Phương trình vận tốc: $v(t) = s'(t) = 6t + 2$.\n- Tại $t = 2$: $v(2) = 6(2) + 2 = 14\\text{ m/s}$."
                    }
                ],
                "exercise": {"id": "11_31_3", "title": "Kiểm minh chứng", "content": "Cho s(t) = 2t^2. Vận tốc tức thời tại thời điểm t = 3 bằng bao nhiêu?", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 32: Các quy tắc tính đạo hàm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Đạo hàm của tổng, hiệu, tích, thương": {
                "theory": "Quy tắc: $(u \\pm v)' = u' \\pm v'$; $(uv)' = u'v + uv'$; $(ku)' = ku'$; $\\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2}$ ($v \\neq 0$). Đạo hàm cơ bản: $(x^n)' = n x^{n-1}$; $(\\sqrt{x})' = \\frac{1}{2\\sqrt{x}}$.",
                "formula": r"(uv)' = u'v + uv'; \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}",
                "trap": "Đạo hàm của thương có dấu TRỪ ở tử số ($u'v - uv'$), học sinh rất hay ghi nhầm thành dấu cộng.",
                "audio": "Đạo hàm của tích bằng u phẩy v cộng u v phẩy. Đạo hàm của thương nhớ có dấu trừ ở tử số và mẫu số bình phương.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm hàm đa thức",
                        "problem": "Tính đạo hàm của hàm số $y = 2x^3 - 3x^2 + 5$.",
                        "solution": "- $y' = 2(3x^2) - 3(2x) + 0 = 6x^2 - 6x$."
                    }
                ],
                "exercise": {"id": "11_32_1", "title": "Kiểm minh chứng", "content": "Đạo hàm của y = x^2 - 4x tại điểm x = 3 bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Đạo hàm của hàm hợp và Hàm số lượng giác": {
                "theory": "Hàm hợp: $y'_x = y'_u \\cdot u'_x$. Cụ thể: $(u^n)' = n u^{n-1} u'$; $(\\sqrt{u})' = \\frac{u'}{2\\sqrt{u}}$. Đạo hàm lượng giác: $(\\sin x)' = \\cos x$; $(\\cos x)' = -\\sin x$; $(\\tan x)' = \\frac{1}{\\cos^2 x}$; $(\\cot x)' = -\\frac{1}{\\sin^2 x}$.",
                "formula": r"(\sin u)' = u' \cdot \cos u; \quad (\cos u)' = -u' \cdot \sin u; \quad (u^n)' = n u^{n-1} u'",
                "trap": "Khi tính đạo hàm của hàm hợp, học sinh rất hay quên nhân thêm đại lượng $u'$ ở cuối.",
                "audio": "Đạo hàm hàm hợp em tính như hàm cơ bản nhưng nhớ nhân thêm u phẩy. Đạo hàm của cos nhớ có dấu trừ nhé.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm hàm hợp lũy thừa",
                        "problem": "Tính đạo hàm của $y = (3x - 1)^4$.",
                        "solution": "- Áp dụng $(u^4)' = 4u^3 \\cdot u'$ với $u = 3x - 1$.\n- $y' = 4(3x - 1)^3 \\cdot (3x - 1)' = 4(3x - 1)^3 \\cdot 3 = 12(3x - 1)^3$."
                    }
                ],
                "exercise": {"id": "11_32_2", "title": "Kiểm minh chứng", "content": "Giá trị đạo hàm của y = sin(2x) tại x = 0 bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 33: Đạo hàm cấp hai": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Cách tính đạo hàm cấp hai": {
                "theory": "Đạo hàm cấp hai của hàm số $y = f(x)$ là đạo hàm của đạo hàm cấp một, kí hiệu là $f''(x)$ hoặc $y''$. Quy trình tính: Lấy đạo hàm lần thứ nhất tìm $y'$, sau đó lấy đạo hàm tiếp trên $y'$ để tìm $y''$.",
                "formula": r"f''(x) = [f'(x)]'",
                "trap": "Tính sai đạo hàm cấp một dẫn đến đạo hàm cấp hai sai dây chuyền.",
                "audio": "Đạo hàm cấp hai đơn giản là lấy đạo hàm thêm một lần nữa. Tính đạo hàm cấp một xong lấy kết quả đó đạo hàm tiếp.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính đạo hàm cấp hai",
                        "problem": "Tính đạo hàm cấp hai của hàm số $y = x^4 - 2x^3 + 5x$.",
                        "solution": "- Đạo hàm cấp một: $y' = 4x^3 - 6x^2 + 5$.\n- Đạo hàm cấp hai: $y'' = (4x^3 - 6x^2 + 5)' = 12x^2 - 12x$."
                    }
                ],
                "exercise": {"id": "11_33_1", "title": "Kiểm minh chứng", "content": "Cho y = x^3. Đạo hàm cấp hai y'' tại điểm x = 2 bằng bao nhiêu?", "type": "NUMERIC", "target": "12", "options": []}
            },
            "2. Ý nghĩa cơ học của đạo hàm cấp hai": {
                "theory": "Trong chuyển động thẳng, gia tốc tức thời $a(t)$ tại thời điểm $t$ chính là đạo hàm cấp hai của phương trình quãng đường $s(t)$, hoặc là đạo hàm cấp một của hàm vận tốc $v(t)$.",
                "formula": r"a(t) = v'(t) = s''(t)",
                "trap": "Học sinh thường nhầm gia tốc là đạo hàm cấp một của quãng đường (đạo hàm cấp một chỉ là vận tốc).",
                "audio": "Trong cơ học, đạo hàm của quãng đường ra vận tốc, và đạo hàm của vận tốc sẽ cho ta gia tốc tức thời của chuyển động.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính gia tốc chuyển động",
                        "problem": "Một vật chuyển động có phương trình $s(t) = 2t^3 - 4t + 1$. Tính gia tốc tại thời điểm $t = 3$.",
                        "solution": "- Vận tốc: $v(t) = s'(t) = 6t^2 - 4$.\n- Gia tốc: $a(t) = s''(t) = 12t$.\n- Tại $t = 3$: $a(3) = 12(3) = 36\\text{ m/s}^2$."
                    }
                ],
                "exercise": {"id": "11_33_2", "title": "Kiểm minh chứng", "content": "Cho s(t) = t^3. Gia tốc tức thời a(t) tại thời điểm t = 1 bằng:", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    }
})
