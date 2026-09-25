# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 1: BÀI 1 -> BÀI 16)
# ==============================================================================

GRADE_11_DATA = {}

GRADE_11_DATA.update({
    "Bài 1: Giá trị lượng giác của góc lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "I. Góc lượng giác và Đơn vị đo góc": {
                "theory": "Góc lượng giác hình thành khi tia $Ou$ quay quanh gốc $O$ đến tia $Ov$. Góc quay ngược chiều kim đồng hồ mang dấu dương, cùng chiều mang dấu âm. Mối liên hệ đơn vị: $180^\circ = \pi \\text{ rad}$. Độ dài cung tròn bán kính $R$ chắn góc $\\alpha$ rad là $l = \\alpha R$.",
                "formula": r"1^\circ = \frac{\pi}{180} \text{ rad}; \quad l = \alpha \cdot R \ (\alpha \text{ tính bằng rad})",
                "trap": "Học sinh thường quên đổi góc sang đơn vị radian trước khi áp dụng công thức tính độ dài cung tròn $l = \\alpha R$.",
                "audio": "Góc lượng giác có thể nhận số đo âm và lớn hơn 360 độ tùy thuộc vào chiều và số vòng quay. Muốn tính độ dài cung tròn, nhớ đổi góc sang radian trước nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đổi đơn vị góc",
                        "problem": "Đổi góc $150^\circ$ sang đơn vị radian.",
                        "solution": "- Áp dụng công thức đổi: $\\alpha = 150 \cdot \\frac{\\pi}{180} = \\frac{5\\pi}{6}$ rad."
                    },
                    {
                        "title": "Ví dụ 2: Tính độ dài cung tròn",
                        "problem": "Tính độ dài cung tròn có bán kính $R = 6$ cm chắn góc có số đo $\\alpha = \\frac{\\pi}{3}$.",
                        "solution": "- Độ dài cung: $l = \\alpha R = \\frac{\\pi}{3} \cdot 6 = 2\\pi \\approx 6.28$ cm."
                    }
                ],
                "exercise": {"id": "11_1_1", "title": "Kiểm minh chứng", "content": "Góc 60 độ đổi ra radian có dạng pi/c. c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "II. Giá trị lượng giác của góc lượng giác": {
                "theory": "Trên đường tròn lượng giác gốc $A(1; 0)$, điểm $M(x; y)$ biểu diễn góc $\\alpha$: Tung độ là $\\sin\\alpha$, hoành độ là $\\cos\\alpha$. Dấu của các giá trị lượng giác theo 4 góc phần tư: Góc I (+; +), Góc II (-; +), Góc III (-; -), Góc IV (+; -).",
                "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha} \ (\alpha \neq \frac{\pi}{2} + k\pi)",
                "trap": "Khai căn để tìm $\\cos\\alpha$ từ $\\sin\\alpha$ bắt buộc phải dựa vào góc phần tư của $\\alpha$ để lấy dấu âm hoặc dương chính xác.",
                "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Luôn đối chiếu góc phần tư để chọn dấu khi tính toán.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lượng giác còn lại",
                        "problem": "Cho $\\sin\\alpha = \\frac{3}{5}$ với $\\frac{\\pi}{2} < \\alpha < \\pi$. Tính $\\cos\\alpha$.",
                        "solution": "- $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$.\n- Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ (góc phần tư thứ II) nên $\\cos\\alpha < 0$.\n- Vậy $\\cos\\alpha = -\\frac{4}{5} = -0.8$."
                    }
                ],
                "exercise": {"id": "11_1_2", "title": "Kiểm minh chứng", "content": "Góc phần tư thứ II, sin = 0.6 thì cos bằng bao nhiêu?", "type": "NUMERIC", "target": "-0.8", "options": []}
            }
        }
    },
    "Bài 2: Công thức lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "I. Công thức cộng": {
                "theory": "Công thức cộng giúp khai triển giá trị lượng giác của tổng hoặc hiệu hai góc: $\\cos(a \\pm b) = \\cos a\\cos b \\mp \\sin a\\sin b$; $\\sin(a \\pm b) = \\sin a\\cos b \\pm \\cos a\\sin b$.",
                "formula": r"\cos(a + b) = \cos a\cos b - \sin a\sin b; \quad \sin(a + b) = \sin a\cos b + \cos a\sin b",
                "trap": "Học sinh hay sai dấu trong công thức $\\cos(a + b)$: Trong ngoặc là dấu CỘNG thì vế phải khai triển phải mang dấu TRỪ.",
                "audio": "Cos thì cos cos sin sin đổi dấu, sin thì sin cos cos sin cùng dấu. Ghi nhớ câu thần chú để không bao giờ nhầm lẫn dấu công thức cộng.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc không đặc biệt",
                        "problem": "Tính $\\cos 75^\circ$ bằng công thức cộng.",
                        "solution": "- Tách $75^\circ = 45^\circ + 30^\circ$.\n- $\\cos(45^\circ + 30^\circ) = \\cos 45^\circ\\cos 30^\circ - \\sin 45^\circ\\sin 30^\circ = \\frac{\\sqrt{2}}{2}\\frac{\\sqrt{3}}{2} - \\frac{\\sqrt{2}}{2}\\frac{1}{2} = \\frac{\\sqrt{6} - \\sqrt{2}}{4}$."
                    }
                ],
                "exercise": {"id": "11_2_1", "title": "Kiểm minh chứng", "content": "Khai triển sin(a + b) được: sin a . cos b + cos a . sin b. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Công thức nhân đôi và hạ bậc": {
                "theory": "Công thức nhân đôi: $\\sin 2a = 2\\sin a\\cos a$; $\\cos 2a = \\cos^2 a - \\sin^2 a = 2\\cos^2 a - 1 = 1 - 2\\sin^2 a$. Công thức hạ bậc dùng để chuyển bậc 2 về bậc 1: $\\cos^2 a = \\frac{1 + \\cos 2a}{2}$.",
                "formula": r"\sin 2a = 2\sin a\cos a; \quad \cos 2a = 2\cos^2 a - 1; \quad \cos^2 a = \frac{1 + \\cos 2a}{2}",
                "trap": "Học sinh thường quên số 2 ở trước biểu thức nhân đôi: $\\sin 2a = 2\\sin a\\cos a$, không phải $\\sin a\\cos a$.",
                "audio": "Công thức nhân đôi biến góc đôi thành góc đơn, công thức hạ bậc giảm bậc 2 xuống bậc 1 và tăng đôi góc.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị nhân đôi",
                        "problem": "Cho $\\sin a\\cos a = 0.3$. Tính $\\sin 2a$.",
                        "solution": "- $\\sin 2a = 2\\sin a\\cos a = 2(0.3) = 0.6$."
                    }
                ],
                "exercise": {"id": "11_2_2", "title": "Kiểm minh chứng", "content": "Biết sin a * cos a = 0.45. Giá trị của sin(2a) bằng:", "type": "NUMERIC", "target": "0.9", "options": []}
            },
            "III. Công thức biến đổi tích thành tổng và tổng thành tích": {
                "theory": "Biến đổi tổng thành tích giúp đưa phương trình lượng giác về phương trình tích: $\\cos a + \\cos b = 2\\cos\\frac{a+b}{2}\\cos\\frac{a-b}{2}$; $\\cos a - \\cos b = -2\\sin\\frac{a+b}{2}\\sin\\frac{a-b}{2}$.",
                "formula": r"\cos a + \cos b = 2\cos\frac{a+b}{2}\cos\frac{a-b}{2}; \quad \sin a + \sin b = 2\sin\frac{a+b}{2}\cos\frac{a-b}{2}",
                "trap": "Công thức $\\cos a - \\cos b$ có dấu TRỪ ở phía trước: $-2\\sin\\frac{a+b}{2}\\sin\\frac{a-b}{2}$. Rất nhiều học sinh bỏ sót dấu trừ này.",
                "audio": "Cos cộng cos bằng hai cos cos, cos trừ cos bằng trừ hai sin sin. Chú ý dấu trừ quan trọng ở hiệu hai cos nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức lượng giác",
                        "problem": "Rút gọn biểu thức $A = \\sin 3x + \\sin x$.",
                        "solution": "- $A = 2\\sin\\left(\\frac{3x+x}{2}\\right)\\cos\\left(\\frac{3x-x}{2}\\right) = 2\\sin 2x\\cos x$."
                    }
                ],
                "exercise": {"id": "11_2_3", "title": "Kiểm minh chứng", "content": "Biểu thức sin(5x) + sin(x) = c.sin(3x).cos(2x). Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 3: Hàm số lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "I. Các hàm số lượng giác cơ bản": {
                "theory": "Hàm $y = \\sin x$ và $y = \\cos x$ có tập xác định $D = \\mathbb{R}$, tập giá trị $[-1; 1]$. Hàm $y = \\tan x$ xác định khi $x \\neq \\frac{\\pi}{2} + k\\pi$. Hàm $y = \\cot x$ xác định khi $x \\neq k\\pi$. Về tính chẵn lẻ: Chỉ có hàm $y = \\cos x$ là hàm chẵn, 3 hàm còn lại là hàm lẻ.",
                "formula": r"-1 \le \sin x \le 1; \quad -1 \le \cos x \le 1; \quad \cos(-x) = \cos x \ (\text{chẵn})",
                "trap": "Học sinh thường nhầm hàm $y = \\sin x$ là hàm chẵn. Nhớ rằng $\\sin(-x) = -\\sin x$ nên nó là hàm số lẻ.",
                "audio": "Cos đối, sin bù, phụ chéo. Hàm cosin là hàm số chẵn duy nhất có đồ thị đối xứng qua trục tung Oy.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập giá trị",
                        "problem": "Tìm giá trị lớn nhất của hàm số $y = 3\\sin x - 2$.",
                        "solution": "- Vì $-1 \\le \\sin x \\le 1$ nên $y_{\\max} = 3(1) - 2 = 1$."
                    }
                ],
                "exercise": {"id": "11_3_1", "title": "Kiểm minh chứng", "content": "Giá trị lớn nhất của hàm số y = 4 cos(x) + 1 bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "II. Tính tuần hoàn và Đồ thị": {
                "theory": "Hàm $y = \\sin x$ và $y = \\cos x$ tuần hoàn với chu kỳ $T = 2\\pi$. Hàm $y = \\tan x$ và $y = \\cot x$ tuần hoàn với chu kỳ $T = \\pi$. Với hàm $y = \\sin(ax + b)$, chu kỳ là $T = \\frac{2\\pi}{|a|}$.",
                "formula": r"T = \frac{2\pi}{|a|} \text{ (với } \sin, \cos); \quad T = \frac{\pi}{|a|} \text{ (với } \tan, \cot)",
                "trap": "Khi tính chu kỳ của hàm số lượng giác chứa hệ số $a$, quên chia cho $|a|$.",
                "audio": "Chu kỳ là khoảng lặp lại của đồ thị. Sin và Cos tuần hoàn theo hai pi, còn Tan và Cot tuần hoàn theo một pi.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm chu kỳ hàm số",
                        "problem": "Tìm chu kỳ tuần hoàn của hàm số $y = \\cos(2x)$.",
                        "solution": "- Hệ số $a = 2$. Chu kỳ $T = \\frac{2\\pi}{|2|} = \\pi$."
                    }
                ],
                "exercise": {"id": "11_3_2", "title": "Kiểm minh chứng", "content": "Chu kỳ của hàm số y = sin(4x) có dạng pi/c. Giá trị của c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 4: Phương trình lượng giác cơ bản": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "I. Phương trình sin x = m và cos x = m": {
                "theory": "Phương trình có nghiệm khi và chỉ khi $|m| \\le 1$. Nếu $|m| > 1$, phương trình vô nghiệm. Họ nghiệm của sin gồm 2 cung bù nhau. Họ nghiệm của cos gồm 2 cung đối nhau.",
                "formula": r"\sin x = \sin\alpha \iff \left[\begin{matrix} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{matrix}\right.; \quad \cos x = \cos\alpha \iff x = \pm\alpha + k2\pi",
                "trap": "Giải phương trình $\\sin x = m$, học sinh thường quên họ nghiệm thứ hai là $x = \\pi - \\alpha + k2\\pi$.",
                "audio": "Phương trình sin có hai họ nghiệm bù nhau đuôi k2pi. Phương trình cos có hai họ nghiệm đối nhau đuôi k2pi.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình sin",
                        "problem": "Giải phương trình $\\sin x = \\frac{1}{2}$.",
                        "solution": "- $\\frac{1}{2} = \\sin\\frac{\\pi}{6} \\implies x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$ ($k \\in \\mathbb{Z}$)."
                    }
                ],
                "exercise": {"id": "11_4_1", "title": "Kiểm minh chứng", "content": "Phương trình cos(x) = 1 có một nghiệm thuộc [0; pi] là x bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Phương trình tan x = m và cot x = m": {
                "theory": "Phương trình $\\tan x = m$ và $\\cot x = m$ luôn có nghiệm với mọi $m \\in \\mathbb{R}$. Đuôi chu kỳ nghiệm là $k\\pi$ (không phải $k2\\pi$).",
                "formula": r"\tan x = \tan\alpha \iff x = \alpha + k\pi; \quad \cot x = \cot\alpha \iff x = \alpha + k\pi",
                "trap": "Học sinh quen tay ghi đuôi chu kỳ của tan và cot thành $+ k2\\pi$ (sai, phải là $+ k\\pi$).",
                "audio": "Phương trình tan và cot luôn có nghiệm với mọi giá trị của m. Đuôi chu kỳ cộng thêm chỉ là một k pi.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình tan",
                        "problem": "Giải phương trình $\\tan x = 1$.",
                        "solution": "- $1 = \\tan\\frac{\\pi}{4} \\implies x = \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$)."
                    }
                ],
                "exercise": {"id": "11_4_2", "title": "Kiểm minh chứng", "content": "Số nghiệm của phương trình tan(x) = 1 trên đoạn [0; pi] là:", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 5: Dãy số": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "I. Khái niệm dãy số": {
                "theory": "Dãy số là hàm số xác định trên tập số nguyên dương $\\mathbb{N}^*$. Dãy số có thể cho bằng công thức số hạng tổng quát $u_n = f(n)$ hoặc bằng hệ thức truy hồi.",
                "formula": r"u_n = f(n) \quad (n \in \mathbb{N}^*)",
                "trap": "Số hạng đầu tiên của dãy số luôn ứng với $n = 1$, không phải $n = 0$.",
                "audio": "Dãy số là một hàm số đặc biệt với biến số n là các số nguyên dương 1, 2, 3, 4 bắt đầu từ 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng của dãy",
                        "problem": "Cho dãy số $u_n = 2n + 1$. Tìm số hạng $u_4$.",
                        "solution": "- Thay $n = 4$: $u_4 = 2(4) + 1 = 9$."
                    }
                ],
                "exercise": {"id": "11_5_1", "title": "Kiểm minh chứng", "content": "Cho u_n = 3n - 1. Số hạng u_3 bằng bao nhiêu?", "type": "NUMERIC", "target": "8", "options": []}
            },
            "II. Dãy số tăng, dãy số giảm và dãy số bị chặn": {
                "theory": "Dãy $(u_n)$ là dãy tăng nếu $u_{n+1} > u_n, \\forall n$. Là dãy giảm nếu $u_{n+1} < u_n, \\forall n$. Dãy bị chặn khi tồn tại $m, M$ sao cho $m \\le u_n \\le M, \\forall n$.",
                "formula": r"u_{n+1} - u_n > 0 \implies \text{Dãy tăng}; \quad m \le u_n \le M \implies \text{Dãy bị chặn}",
                "trap": "Xét tính tăng giảm bằng cách lập tỉ số $\\frac{u_{n+1}}{u_n}$ chỉ áp dụng được khi tất cả các số hạng đều DƯƠNG.",
                "audio": "Lấy số hạng sau trừ số hạng trước, nếu hiệu dương là dãy tăng, nếu hiệu âm là dãy giảm.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính tăng giảm",
                        "problem": "Dãy số $u_n = \\frac{1}{n}$ tăng hay giảm?",
                        "solution": "- Hiệu: $u_{n+1} - u_n = \\frac{1}{n+1} - \\frac{1}{n} = \\frac{-1}{n(n+1)} < 0$.\n- Hiệu âm nên dãy số $(u_n)$ là dãy giảm."
                    }
                ],
                "exercise": {"id": "11_5_2", "title": "Kiểm minh chứng", "content": "Dãy số u_n = 1/n đạt giá trị lớn nhất bằng bao nhiêu?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 6: Cấp số cộng": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "I. Định nghĩa và Số hạng tổng quát": {
                "theory": "Cấp số cộng là dãy số mà mỗi số hạng (từ số thứ 2) bằng số hạng trước cộng thêm công sai $d$. Công thức số hạng tổng quát: $u_n = u_1 + (n - 1)d$.",
                "formula": r"u_n = u_1 + (n - 1)d; \quad u_k = \frac{u_{k-1} + u_{k+1}}{2}",
                "trap": "Học sinh thường nhầm số hạng tổng quát thành $u_n = u_1 + nd$ (quên trừ 1 ở chỉ số $n$).",
                "audio": "Số hạng sau bằng số trước cộng công sai d. Số hạng thứ n bằng u1 cộng n trừ 1 nhân d.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng tổng quát",
                        "problem": "Cho cấp số cộng có $u_1 = 3, d = 4$. Tìm $u_5$.",
                        "solution": "- $u_5 = u_1 + (5 - 1)d = 3 + 4(4) = 19$."
                    }
                ],
                "exercise": {"id": "11_6_1", "title": "Kiểm minh chứng", "content": "CSC có u1 = 2, d = 3. Số hạng u4 bằng bao nhiêu?", "type": "NUMERIC", "target": "11", "options": []}
            },
            "II. Tổng n số hạng đầu tiên": {
                "theory": "Tổng $n$ số hạng đầu tiên $S_n$ bằng số lượng phần tử nhân trung bình cộng của số đầu và số cuối.",
                "formula": r"S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n - 1)d]}{2}",
                "trap": "Bấm máy tính nhầm cụm $(n-1)d$ thành $nd$ khi tính tổng $S_n$.",
                "audio": "Tổng cấp số cộng bằng số lượng phần tử nhân với tổng số đầu cộng số cuối rồi chia cho 2.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng cấp số cộng",
                        "problem": "Tính tổng 10 số hạng đầu của cấp số cộng có $u_1 = 1, d = 2$.",
                        "solution": "- $S_{10} = \\frac{10[2(1) + 9(2)]}{2} = 5(2 + 18) = 100$."
                    }
                ],
                "exercise": {"id": "11_6_2", "title": "Kiểm minh chứng", "content": "Tổng 5 số hạng đầu của CSC có u1 = 2, d = 3 bằng:", "type": "NUMERIC", "target": "40", "options": []}
            }
        }
    },
    "Bài 7: Cấp số nhân": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "I. Định nghĩa và Số hạng tổng quát": {
                "theory": "Cấp số nhân là dãy số mà mỗi số hạng (từ số thứ 2) bằng số hạng trước nhân với công bội $q$. Số hạng tổng quát: $u_n = u_1 \cdot q^{n-1}$.",
                "formula": r"u_n = u_1 \cdot q^{n-1}; \quad u_k^2 = u_{k-1} \cdot u_{k+1}",
                "trap": "Học sinh hay ghi nhầm số mũ thành $q^n$ thay vì $q^{n-1}$.",
                "audio": "Cấp số nhân có quy luật số sau bằng số trước nhân công bội q. Số hạng thứ n bằng u1 nhân q mũ n trừ 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng tổng quát",
                        "problem": "Cho cấp số nhân có $u_1 = 2, q = 3$. Tìm $u_4$.",
                        "solution": "- $u_4 = u_1 \\cdot q^3 = 2 \\cdot 3^3 = 2 \\cdot 27 = 54$."
                    }
                ],
                "exercise": {"id": "11_7_1", "title": "Kiểm minh chứng", "content": "CSN có u1 = 3, q = 2. Số hạng u3 bằng:", "type": "NUMERIC", "target": "12", "options": []}
            },
            "II. Tổng n số hạng đầu tiên": {
                "theory": "Tổng $n$ số hạng đầu tiên của cấp số nhân có công bội $q \neq 1$: $S_n = u_1 \\frac{1 - q^n}{1 - q}$.",
                "formula": r"S_n = u_1 \frac{1 - q^n}{1 - q} \ (q \neq 1)",
                "trap": "Trong công thức tổng CSN, số mũ của q trên tử số là $q^n$, không phải $q^{n-1}$.",
                "audio": "Tổng cấp số nhân bằng u1 nhân với phân thức 1 trừ q mũ n chia cho 1 trừ q.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng cấp số nhân",
                        "problem": "Tính tổng 4 số hạng đầu của cấp số nhân có $u_1 = 1, q = 2$.",
                        "solution": "- $S_4 = 1 \\cdot \\frac{1 - 2^4}{1 - 2} = \\frac{1 - 16}{-1} = 15$."
                    }
                ],
                "exercise": {"id": "11_7_2", "title": "Kiểm minh chứng", "content": "Tổng 3 số hạng đầu của CSN có u1 = 2, q = 3 bằng:", "type": "NUMERIC", "target": "26", "options": []}
            }
        }
    },
    "Bài 8: Mẫu số liệu ghép nhóm": {
        "chapter": "Chương III: Các số đặc trưng đo xu thế trung tâm",
        "topics": {
            "I. Thu thập và Biểu diễn mẫu số liệu ghép nhóm": {
                "theory": "Số liệu ghép nhóm được phân vào các nhóm nửa khoảng $[a_i; a_{i+1})$. Độ dài mỗi nhóm là $h = a_{i+1} - a_i$. Tần số $n_i$ là số lượng giá trị rơi vào nhóm đó.",
                "formula": r"h = a_{i+1} - a_i; \quad n = \sum n_i",
                "trap": "Lấy nhầm đầu mút: Nhóm $[a; b)$ bao gồm giá trị $a$ nhưng KHÔNG bao gồm giá trị $b$.",
                "audio": "Mẫu số liệu ghép nhóm chia dữ liệu thành các khoảng liền kề, giúp xử lý các tập dữ liệu lớn một cách gọn gàng.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài nhóm",
                        "problem": "Tính độ dài của nhóm số liệu $[20; 30)$.",
                        "solution": "- Độ dài nhóm: $h = 30 - 20 = 10$."
                    }
                ],
                "exercise": {"id": "11_8_1", "title": "Kiểm minh chứng", "content": "Độ dài của nhóm số liệu [15; 25) bằng bao nhiêu?", "type": "NUMERIC", "target": "10", "options": []}
            },
            "II. Tần số tích lũy và Giá trị đại diện": {
                "theory": "Giá trị đại diện $c_i$ của nhóm $[a_i; a_{i+1})$ là trung bình cộng hai đầu mút. Tần số tích lũy $C_k$ là tổng tần số từ nhóm 1 đến nhóm $k$.",
                "formula": r"c_i = \frac{a_i + a_{i+1}}{2}; \quad C_k = n_1 + n_2 + \dots + n_k",
                "trap": "Giá trị đại diện tính bằng phép CỘNG chia đôi, không phải phép trừ.",
                "audio": "Giá trị đại diện là điểm chính giữa của nhóm, lấy hai đầu mút cộng lại chia đôi là xong.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị đại diện",
                        "problem": "Tìm giá trị đại diện của nhóm $[40; 50)$.",
                        "solution": "- $c = \\frac{40 + 50}{2} = 45$."
                    }
                ],
                "exercise": {"id": "11_8_2", "title": "Kiểm minh chứng", "content": "Giá trị đại diện của nhóm [10; 20) bằng:", "type": "NUMERIC", "target": "15", "options": []}
            }
        }
    },
    "Bài 9: Các số đặc trưng đo xu thế trung tâm": {
        "chapter": "Chương III: Các số đặc trưng đo xu thế trung tâm",
        "topics": {
            "I. Số trung bình và Mốt của mẫu ghép nhóm": {
                "theory": "Số trung bình bằng tổng các tích tần số nhân giá trị đại diện chia cho cỡ mẫu. Nhóm chứa mốt là nhóm có tần số lớn nhất.",
                "formula": r"\overline{x} = \frac{1}{n}\sum n_i c_i; \quad M_o = u_m + \frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \cdot h",
                "trap": "Nhầm lẫn giữa tần số nhóm trước ($n_{m-1}$) và nhóm sau ($n_{m+1}$) trong công thức tính Mốt.",
                "audio": "Số trung bình tính bằng trung bình có trọng số. Mốt được nội suy từ nhóm có tần số cao nhất.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính số trung bình",
                        "problem": "Cho nhóm [0; 10) có 2 bạn, [10; 20) có 8 bạn. Tính số trung bình.",
                        "solution": "- $c_1 = 5, c_2 = 15$. $\\overline{x} = \\frac{2(5) + 8(15)}{10} = \\frac{140}{10} = 14$."
                    }
                ],
                "exercise": {"id": "11_9_1", "title": "Kiểm minh chứng", "content": "Số trung bình của mẫu gồm [0; 10) tần số 5 và [10; 20) tần số 5 là:", "type": "NUMERIC", "target": "10", "options": []}
            },
            "II. Trung vị và Tứ phân vị": {
                "theory": "Trung vị $M_e = Q_2$ chia đôi mẫu số liệu. Nhóm chứa trung vị là nhóm đầu tiên có tần số tích lũy $\\ge n/2$.",
                "formula": r"M_e = u_m + \frac{\frac{n}{2} - C}{n_m} \cdot h",
                "trap": "$C$ là tần số tích lũy của nhóm NGAY TRƯỚC nhóm chứa trung vị, không bao gồm nhóm hiện tại.",
                "audio": "Trung vị là mốc 50% dữ liệu. Xác định nhóm chứa trung vị bằng cách dò tần số tích lũy vượt qua n chia 2.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định nhóm chứa trung vị",
                        "problem": "Cỡ mẫu $n = 40$. Nhóm 1 có tần số 15, nhóm 2 có tần số 10. Trung vị thuộc nhóm nào?",
                        "solution": "- $n/2 = 20$. Tần số tích lũy nhóm 1 là 15 (< 20). Nhóm 2 là $15 + 10 = 25$ ($\\ge 20$).\n- Vậy trung vị thuộc nhóm thứ 2."
                    }
                ],
                "exercise": {"id": "11_9_2", "title": "Kiểm minh chứng", "content": "Cỡ mẫu n = 100 thì vị trí xác định nhóm trung vị n/2 bằng bao nhiêu?", "type": "NUMERIC", "target": "50", "options": []}
            }
        }
    },
    "Bài 10: Đường thẳng và mặt phẳng trong không gian": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "I. Khái niệm mở đầu và Các tính chất thừa nhận": {
                "theory": "Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng. Nếu một đường thẳng có hai điểm phân biệt thuộc mặt phẳng thì mọi điểm của đường thẳng đều thuộc mặt phẳng đó.",
                "formula": r"A, B, C \text{ không thẳng hàng} \implies \exists! (ABC)",
                "trap": "Ba điểm PHẢI KHÔNG THẲNG HÀNG thì mới xác định duy nhất một mặt phẳng. Nếu thẳng hàng thì có vô số mặt phẳng.",
                "audio": "Chiếc kiềng ba chân luôn đứng vững trên mọi mặt đất vì qua ba điểm không thẳng hàng luôn xác định duy nhất một mặt phẳng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định mặt phẳng",
                        "problem": "Có bao nhiêu mặt phẳng đi qua 3 điểm phân biệt thẳng hàng?",
                        "solution": "- Có vô số mặt phẳng đi qua 3 điểm thẳng hàng (chúng tạo thành một chùm mặt phẳng xoay quanh đường thẳng chứa 3 điểm)."
                    }
                ],
                "exercise": {"id": "11_10_1", "title": "Kiểm minh chứng", "content": "Số mặt phẳng đi qua 3 điểm phân biệt không thẳng hàng là:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Cách xác định mặt phẳng và Giao tuyến": {
                "theory": "Có 3 cách xác định mặt phẳng: Qua 3 điểm không thẳng hàng; Qua 1 đường thẳng và 1 điểm ngoài đường thẳng; Qua 2 đường thẳng cắt nhau. Giao tuyến của 2 mặt phẳng phân biệt là đường thẳng đi qua các điểm chung của chúng.",
                "formula": r"(P) \cap (Q) = d",
                "trap": "Để tìm giao tuyến, cần tìm 2 điểm chung phân biệt. Điểm chung thứ hai thường là giao của 2 đường thẳng cùng nằm trong mặt phẳng đáy.",
                "audio": "Giao tuyến của hai mặt phẳng giống như nếp gấp của trang sách mở, luôn là một đường thẳng nối các điểm chung.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giao tuyến",
                        "problem": "Cho hình chóp S.ABCD. Giao tuyến của (SAB) và (SBC) là đường thẳng nào?",
                        "solution": "- Hai mặt phẳng cùng chứa đỉnh S và điểm B.\n- Giao tuyến là đường thẳng SB."
                    }
                ],
                "exercise": {"id": "11_10_2", "title": "Kiểm minh chứng", "content": "Giao tuyến của (SAC) và (SBD) đi qua đỉnh S và tâm đáy O. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 11: Hai đường thẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "I. Vị trí tương đối của hai đường thẳng trong không gian": {
                "theory": "Trong không gian, hai đường thẳng có 4 vị trí tương đối: Trùng nhau, Cắt nhau, Song song (cùng thuộc 1 mặt phẳng và không có điểm chung), và Chéo nhau (không cùng thuộc bất kỳ mặt phẳng nào).",
                "formula": r"a \parallel b \implies a, b \subset (P) \text{ và } a \cap b = \emptyset",
                "trap": "Hai đường thẳng không có điểm chung có thể SONG SONG hoặc CHÉO NHAU. Không được kết luận ngay là song song.",
                "audio": "Khác với hình học phẳng, trong không gian hai đường thẳng không cắt nhau có thể chéo nhau đấy nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện đường chéo nhau",
                        "problem": "Cho tứ diện ABCD. Cạnh AB và CD có vị trí tương đối như thế nào?",
                        "solution": "- Bốn điểm A, B, C, D không đồng phẳng nên AB và CD không cùng thuộc mặt phẳng nào.\n- Vậy AB và CD chéo nhau."
                    }
                ],
                "exercise": {"id": "11_11_1", "title": "Kiểm minh chứng", "content": "Hai đường thẳng không có điểm chung thì chắc chắn song song. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Tính chất hai đường thẳng song song": {
                "theory": "Định lý 3 giao tuyến: Nếu 3 mặt phẳng đôi một cắt nhau theo 3 giao tuyến phân biệt thì 3 giao tuyến đó hoặc đồng quy, hoặc đôi một song song.",
                "formula": r"\begin{cases} (P) \cap (Q) = a \\ (Q) \cap (R) = b \\ (R) \cap (P) = c \end{cases} \implies a, b, c \text{ đồng quy hoặc đôi một song song}",
                "trap": "Nếu hai mặt phẳng chứa 2 đường thẳng song song thì giao tuyến của chúng (nếu có) phải song song với 2 đường đó hoặc trùng một trong hai.",
                "audio": "Định lý ba giao tuyến là công cụ mạnh mẽ để chứng minh hai đường thẳng song song hoặc ba đường thẳng đồng quy.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giao tuyến song song",
                        "problem": "Cho hình chóp S.ABCD đáy ABCD là hình bình hành. Giao tuyến của (SAB) và (SCD) song song với đường nào?",
                        "solution": "- Hai mặt phẳng cùng chứa đỉnh S.\n- Lần lượt chứa $AB \\parallel CD$.\n- Vậy giao tuyến là đường thẳng đi qua S và song song với AB, CD."
                    }
                ],
                "exercise": {"id": "11_11_2", "title": "Kiểm minh chứng", "content": "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 12: Đường thẳng và mặt phẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "I. Điều kiện để đường thẳng song song với mặt phẳng": {
                "theory": "Đường thẳng $d$ song song với mặt phẳng $(\\alpha)$ nếu $d$ không nằm trong $(\\alpha)$ và $d$ song song với MỘT đường thẳng $a$ nằm trong $(\\alpha)$.",
                "formula": r"\begin{cases} d \not\subset (\alpha) \\ a \subset (\alpha) \\ d \parallel a \end{cases} \implies d \parallel (\alpha)",
                "trap": "Học sinh thường quên kiểm tra điều kiện $d$ KHÔNG NẰM TRONG mặt phẳng $(\\alpha)$. Nếu nó nằm trong thì không được gọi là song song.",
                "audio": "Muốn chứng minh đường song song với mặt, hãy tìm trong mặt phẳng một đường thẳng song song với đường đã cho.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường song song mặt",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành. Chứng minh AB song song với (SCD).",
                        "solution": "- Ta có $AB \\parallel CD$ (do ABCD là hình bình hành).\n- $CD \\subset (SCD)$ và $AB \\not\\subset (SCD)$.\n- Suy ra $AB \\parallel (SCD)$."
                    }
                ],
                "exercise": {"id": "11_12_1", "title": "Kiểm minh chứng", "content": "Đường thẳng d nằm hoàn toàn trong (P). Hỏi d có song song với (P) không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Tính chất của đường thẳng song song mặt phẳng": {
                "theory": "Nếu đường thẳng $a$ song song với mặt phẳng $(P)$, thì bất kỳ mặt phẳng $(Q)$ nào chứa $a$ mà cắt $(P)$ theo giao tuyến $b$ thì giao tuyến $b$ phải song song với $a$.",
                "formula": r"\begin{cases} a \parallel (P) \\ a \subset (Q) \\ (P) \cap (Q) = b \end{cases} \implies a \parallel b",
                "trap": "Đường thẳng song song với mặt phẳng KHÔNG CÓ NGHĨA là nó song song với mọi đường trong mặt phẳng đó. Nó có thể chéo nhau với các đường khác.",
                "audio": "Đường song song với mặt thì chỉ song song với các đường cùng phương trong mặt, còn lại là chéo nhau hết đấy nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận định quan hệ",
                        "problem": "Nếu $d \\parallel (P)$ và $a \\subset (P)$ thì $d$ và $a$ có thể cắt nhau không?",
                        "solution": "- Không bao giờ. Vì nếu cắt nhau thì $d$ và $(P)$ có điểm chung, mâu thuẫn với giả thiết song song."
                    }
                ],
                "exercise": {"id": "11_12_2", "title": "Kiểm minh chứng", "content": "Nếu d // (P) thì d không có điểm chung với (P). Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 13: Hai mặt phẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "I. Điều kiện để hai mặt phẳng song song": {
                "theory": "Mặt phẳng $(P)$ song song với mặt phẳng $(Q)$ nếu $(P)$ chứa HAI đường thẳng CẮT NHAU cùng song song với $(Q)$.",
                "formula": r"\begin{cases} a, b \subset (P); \ a \cap b = I \\ a \parallel (Q); \ b \parallel (Q) \end{cases} \implies (P) \parallel (Q)",
                "trap": "Hai đường thẳng $a$ và $b$ nằm trong mặt phẳng $(P)$ BẮT BUỘC phải cắt nhau. Nếu chúng song song thì không đủ điều kiện.",
                "audio": "Chỉ cần tìm hai đường thẳng cắt nhau trong mặt phẳng này cùng song song với mặt phẳng kia là chứng minh xong hai mặt phẳng song song.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng song song",
                        "problem": "Cho hình chóp S.ABCD. Gọi M, N, P lần lượt là trung điểm SA, SB, SC. Mặt phẳng (MNP) có song song đáy (ABC) không?",
                        "solution": "- $MN \\parallel AB$ và $NP \\parallel BC$ (đường trung bình).\n- MN và NP cắt nhau tại N thuộc (MNP).\n- Suy ra $(MNP) \\parallel (ABC)$."
                    }
                ],
                "exercise": {"id": "11_13_1", "title": "Kiểm minh chứng", "content": "Để (P) // (Q) thì (P) cần chứa tối thiểu bao nhiêu đường thẳng cắt nhau cùng song song (Q)?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Tính chất hai mặt phẳng song song": {
                "theory": "Hai mặt phẳng song song chắn trên hai cát tuyến bất kỳ những đoạn thẳng tương ứng tỉ lệ (Định lý Thales không gian). Mặt phẳng thứ ba cắt hai mặt phẳng song song theo hai giao tuyến song song.",
                "formula": r"(P) \parallel (Q); \ (R) \cap (P) = a; \ (R) \cap (Q) = b \implies a \parallel b",
                "trap": "Các đoạn thẳng chắn giữa hai mặt phẳng song song chỉ BẰNG NHAU khi hai cát tuyến đó song song với nhau.",
                "audio": "Mặt phẳng thứ ba cắt hai mặt phẳng song song sẽ tạo ra hai giao tuyến song song như hai mép của một bậc cầu thang.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giao tuyến của mặt phẳng cắt",
                        "problem": "Mặt phẳng $(\\alpha)$ cắt hai mặt phẳng song song $(P)$ và $(Q)$ theo hai giao tuyến $a$ và $b$. Vị trí của $a$ và $b$?",
                        "solution": "- Theo tính chất, $a$ và $b$ song song với nhau."
                    }
                ],
                "exercise": {"id": "11_13_2", "title": "Kiểm minh chứng", "content": "Hai mặt phẳng phân biệt cùng song song với mặt phẳng thứ ba thì song song với nhau. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 14: Phép chiếu song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "I. Phép chiếu song song và Tính chất": {
                "theory": "Phép chiếu song song biến đường thẳng thành đường thẳng, biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau. Bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng hoặc nằm trên hai đường thẳng song song.",
                "formula": r"\text{Bảo toàn tính thẳng hàng, song song và tỉ số đoạn thẳng cùng phương}",
                "trap": "Phép chiếu song song KHÔNG bảo toàn độ lớn của góc và khoảng cách (góc vuông có thể bị chiếu thành góc nhọn hoặc tù).",
                "audio": "Phép chiếu song song giữ nguyên tính thẳng hàng và song song, nhưng không giữ nguyên số đo góc hay độ dài đoạn thẳng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Hình biểu diễn",
                        "problem": "Hình chiếu song song của một hình chữ nhật có thể là hình gì?",
                        "solution": "- Bảo toàn tính song song của các cạnh đối, nhưng góc vuông không bảo toàn.\n- Hình chiếu là một hình bình hành."
                    }
                ],
                "exercise": {"id": "11_14_1", "title": "Kiểm minh chứng", "content": "Phép chiếu song song có luôn bảo toàn số đo góc vuông không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Hình biểu diễn của một hình không gian": {
                "theory": "Hình biểu diễn của hình tròn thường là hình elip. Hình biểu diễn của tam giác đều, tam giác vuông thường là tam giác thường. Đường nhìn thấy vẽ nét liền, đường bị che khuất vẽ nét đứt.",
                "formula": r"\text{Hình tròn } \to \text{Hình Elip; } \text{Bị che } \to \text{Nét đứt}",
                "trap": "Vẽ hình không gian tuyệt đối không được vẽ nét liền cho các cạnh bị che khuất bên trong.",
                "audio": "Đường nhìn thấy vẽ nét liền, đường khuất sau lưng vẽ nét đứt. Tròn vẽ thành elip, vuông vẽ thành bình hành.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Biểu diễn hình vuông",
                        "problem": "Trong hình học không gian, đáy là hình vuông được vẽ biểu diễn bằng hình gì?",
                        "solution": "- Hình bình hành."
                    }
                ],
                "exercise": {"id": "11_14_2", "title": "Kiểm minh chứng", "content": "Hình biểu diễn của đường tròn trong phép chiếu song song thường là hình elip. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 15: Giới hạn của dãy số": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "I. Giới hạn hữu hạn của dãy số": {
                "theory": "Dãy số $(u_n)$ có giới hạn là 0 khi $n \to +\infty$ nếu $|u_n|$ có thể nhỏ hơn một số dương bé tùy ý. Các giới hạn cơ bản: $\\lim \\frac{1}{n^k} = 0$ ($k > 0$); $\\lim q^n = 0$ ($|q| < 1$). Quy tắc tính: Chia cả tử và mẫu cho lũy thừa cao nhất của $n$.",
                "formula": r"\lim_{n \to +\infty} \frac{1}{n} = 0; \quad \lim_{n \to +\infty} q^n = 0 \ (|q| < 1)",
                "trap": "Học sinh hay nhầm $\\lim q^n = 0$ với mọi $q$. Điều kiện bắt buộc là $|q| < 1$. Nếu $q > 1$ thì giới hạn tiến ra $+\\infty$.",
                "audio": "Gặp giới hạn phân thức của n tiến ra vô cực, cứ chia cả tử và mẫu cho n bậc cao nhất là bài toán được giải quyết.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giới hạn phân thức",
                        "problem": "Tính $\\lim \\frac{2n + 1}{n - 3}$.",
                        "solution": "- Chia cả tử và mẫu cho $n$: $\\lim \\frac{2 + 1/n}{1 - 3/n} = \\frac{2 + 0}{1 - 0} = 2$."
                    }
                ],
                "exercise": {"id": "11_15_1", "title": "Kiểm minh chứng", "content": "Giới hạn lim (4n - 1)/(2n + 3) bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Tổng của cấp số nhân lùi vô hạn": {
                "theory": "Cấp số nhân có công bội $|q| < 1$ gọi là lùi vô hạn. Tổng của vô hạn các số hạng của nó hội tụ về một số thực xác định.",
                "formula": r"S = u_1 + u_1 q + u_1 q^2 + \dots = \frac{u_1}{1 - q} \ (|q| < 1)",
                "trap": "Không được áp dụng công thức này nếu $|q| \\ge 1$, vì khi đó tổng không hội tụ.",
                "audio": "Tổng cấp số nhân lùi vô hạn bằng số hạng đầu chia cho 1 trừ đi công bội q. Công thức ngắn gọn và rất hay thi.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng chuỗi lùi vô hạn",
                        "problem": "Tính tổng $S = 1 + \\frac{1}{2} + \\frac{1}{4} + \\dots$",
                        "solution": "- $u_1 = 1, q = 1/2 < 1$.\n- $S = \\frac{1}{1 - 1/2} = 2$."
                    }
                ],
                "exercise": {"id": "11_15_2", "title": "Kiểm minh chứng", "content": "Tổng vô hạn của cấp số nhân u1 = 3, q = 1/2 bằng:", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 16: Giới hạn của hàm số": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "I. Giới hạn hữu hạn của hàm số tại một điểm": {
                "theory": "Khi thay $x = x_0$ vào hàm số dạng phân thức được $\\frac{0}{0}$ (dạng vô định), ta cần khử dạng vô định bằng cách phân tích tử và mẫu thành nhân tử chứa $(x - x_0)$ rồi triệt tiêu, hoặc nhân lượng liên hợp nếu có căn thức.",
                "formula": r"\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{(x - x_0)P(x)}{(x - x_0)Q(x)} = \lim_{x \to x_0} \frac{P(x)}{Q(x)}",
                "trap": "Thấy dạng $0/0$ vội kết luận giới hạn bằng 0 hoặc không tồn tại. Phải phân tích nhân tử để khử dạng vô định trước.",
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
            "II. Giới hạn một bên và Giới hạn tại vô cực": {
                "theory": "Giới hạn bên phải $\\lim_{x \\to x_0^+} f(x)$ và giới hạn bên trái $\\lim_{x \\to x_0^-} f(x)$. Giới hạn $\\lim_{x \\to x_0} f(x) = L$ khi và chỉ khi giới hạn trái và giới hạn phải cùng tồn tại và BẰNG NHAU.",
                "formula": r"\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L",
                "trap": "Nếu giới hạn trái và giới hạn phải cho ra hai kết quả khác nhau thì giới hạn chung tại điểm đó KHÔNG TỒN TẠI.",
                "audio": "Giới hạn bên trái và bên phải phải gặp nhau tại cùng một giá trị L thì giới hạn tại điểm đó mới thực sự tồn tại.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giới hạn một bên",
                        "problem": "Tính $\\lim_{x \\to 1^+} \\frac{1}{x - 1}$.",
                        "solution": "- Khi $x \\to 1^+$, tử số bằng 1 (>0), mẫu số $x - 1 > 0$ và tiến dần về 0.\n- Kết quả là $+\\infty$."
                    }
                ],
                "exercise": {"id": "11_16_2", "title": "Kiểm minh chứng", "content": "Nếu giới hạn bên trái bằng 3 và giới hạn bên phải bằng 3 thì giới hạn tại điểm đó bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 2: BÀI 17 -> BÀI 33)
# ==============================================================================

GRADE_11_DATA.update({
    "Bài 17: Hàm số liên tục": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "I. Khái niệm hàm số liên tục tại một điểm": {
                "theory": "Hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa $x_0$ được gọi là liên tục tại $x_0$ nếu giới hạn của hàm số khi $x \to x_0$ bằng giá trị của hàm số tại $x_0$. Nếu không thỏa mãn điều này, hàm số bị gián đoạn tại $x_0$.",
                "formula": r"\lim_{x \to x_0} f(x) = f(x_0)",
                "trap": "Học sinh thường quên tính $f(x_0)$ mà chỉ tính giới hạn $\lim_{x \to x_0} f(x)$. Để liên tục, hai giá trị này bắt buộc phải bằng nhau.",
                "audio": "Hàm số liên tục tại một điểm khi giới hạn tại điểm đó bằng đúng giá trị của hàm số. Đồ thị của hàm số liên tục là một nét liền không bị đứt quãng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính liên tục tại một điểm",
                        "problem": "Xét tính liên tục của hàm số $f(x) = x^2 + 1$ tại điểm $x_0 = 2$.",
                        "solution": "- Tập xác định: $D = \mathbb{R}$, chứa $x_0 = 2$.\n- Ta có $f(2) = 2^2 + 1 = 5$.\n- Giới hạn: $\lim_{x \to 2} (x^2 + 1) = 2^2 + 1 = 5$.\n- Vì $\lim_{x \to 2} f(x) = f(2) = 5$, hàm số liên tục tại $x_0 = 2$."
                    }
                ],
                "exercise": {"id": "11_17_1", "title": "Kiểm minh chứng", "content": "Để hàm số f(x) = 2x khi x khác 1 và f(x) = m khi x = 1 liên tục tại x = 1 thì m bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Hàm số liên tục trên khoảng và Định lý giá trị trung gian": {
                "theory": "Hàm số liên tục trên từng khoảng xác định của nó (đa thức, phân thức, lượng giác). Định lý giá trị trung gian: Nếu $f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \cdot f(b) < 0$ thì phương trình $f(x) = 0$ có ít nhất một nghiệm thuộc khoảng $(a; b)$.",
                "formula": r"f(a) \cdot f(b) < 0 \implies \exists c \in (a; b): f(c) = 0",
                "trap": "Thiếu điều kiện 'hàm số liên tục trên đoạn $[a; b]$' khi áp dụng định lý chứng minh phương trình có nghiệm.",
                "audio": "Nếu hàm số đi liền nét từ giá trị âm sang giá trị dương trên một đoạn, chắc chắn đồ thị phải cắt trục hoành ít nhất một lần.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh phương trình có nghiệm",
                        "problem": "Chứng minh phương trình $x^3 + 3x - 1 = 0$ có ít nhất 1 nghiệm trên $(0; 1)$.",
                        "solution": "- Xét $f(x) = x^3 + 3x - 1$ liên tục trên $[0; 1]$.\n- $f(0) = -1 < 0$ và $f(1) = 3 > 0$.\n- Tích $f(0) \cdot f(1) = -3 < 0$, suy ra phương trình có ít nhất 1 nghiệm trong $(0; 1)$."
                    }
                ],
                "exercise": {"id": "11_17_2", "title": "Kiểm minh chứng", "content": "Hàm số f(x) = x^3 - 2 liên tục trên [1; 2]. Tích f(1).f(2) bằng bao nhiêu?", "type": "NUMERIC", "target": "-6", "options": []}
            }
        }
    },
    "Bài 18: Lũy thừa với số mũ thực": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "I. Khái niệm lũy thừa và Tính chất": {
                "theory": "Lũy thừa với số mũ hữu tỉ $a^{m/n} = \sqrt[n]{a^m}$ ($a > 0$). Với $a, b > 0$, các quy tắc tính toán: $a^\alpha \cdot a^\beta = a^{\alpha + \beta}$; $\frac{a^\alpha}{a^\beta} = a^{\alpha - \beta}$; $(a^\alpha)^\beta = a^{\alpha\beta}$; $(ab)^\alpha = a^\alpha b^\alpha$.",
                "formula": r"a^\alpha \cdot a^\beta = a^{\alpha + \beta}; \quad a^{\frac{m}{n}} = \sqrt[n]{a^m} \ (a > 0)",
                "trap": "Biểu thức $a^{m/n}$ chỉ có nghĩa khi cơ số $a > 0$. Số mũ không nguyên không xác định với cơ số âm.",
                "audio": "Nhân hai lũy thừa cùng cơ số thì cộng số mũ, chia thì trừ số mũ, lũy thừa của lũy thừa thì nhân hai số mũ lại với nhau.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức lũy thừa",
                        "problem": "Rút gọn biểu thức $P = a^{\frac{1}{3}} \cdot \sqrt{a}$ với $a > 0$.",
                        "solution": "- Viết lại căn dưới dạng số mũ: $\sqrt{a} = a^{\frac{1}{2}}$.\n- $P = a^{\frac{1}{3}} \cdot a^{\frac{1}{2}} = a^{\frac{1}{3} + \frac{1}{2}} = a^{\frac{5}{6}}$."
                    }
                ],
                "exercise": {"id": "11_18_1", "title": "Kiểm minh chứng", "content": "Rút gọn a^2 * a^(1/2) được a^(c/2). Giá trị c bằng:", "type": "NUMERIC", "target": "5", "options": []}
            }
        }
    },
    "Bài 19: Lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "I. Khái niệm và Tính chất của lôgarit": {
                "theory": "Cho $0 < a \neq 1, b > 0$. Số $\alpha$ thỏa mãn $a^\alpha = b$ được gọi là lôgarit cơ số $a$ của $b$, ký hiệu $\log_a b$. Tính chất: $\log_a 1 = 0; \log_a a = 1; a^{\log_a b} = b$.",
                "formula": r"\log_a b = \alpha \iff a^\alpha = b \quad (0 < a \neq 1, b > 0)",
                "trap": "Biểu thức dưới dấu lôgarit phải luôn mang dấu DƯƠNG ($b > 0$). Không tồn tại lôgarit của số 0 hoặc số âm.",
                "audio": "Lôgarit cơ số a của b chính là số mũ để khi lấy a nâng lên lũy thừa đó thì thu được b. Điều kiện là cơ số dương khác 1 và b dương.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lôgarit",
                        "problem": "Tính giá trị của $\log_2 16$.",
                        "solution": "- Vì $2^4 = 16$ nên $\log_2 16 = 4$."
                    }
                ],
                "exercise": {"id": "11_19_1", "title": "Kiểm minh chứng", "content": "Giá trị của log_3(27) bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            },
            "II. Các quy tắc tính và Công thức đổi cơ số": {
                "theory": "Quy tắc: $\log_a(xy) = \log_a x + \log_a y$; $\log_a(x/y) = \log_a x - \log_a y$; $\log_a x^\alpha = \alpha\log_a x$. Công thức đổi cơ số: $\log_a b = \frac{\log_c b}{\log_c a}$.",
                "formula": r"\log_a(xy) = \log_a x + \log_a y; \quad \log_a b = \frac{\log_c b}{\log_c a}",
                "trap": "Học sinh hay nhầm lẫn giữa lôgarit của một tổng với tổng các lôgarit. Công thức $\log(x + y)$ không thể tách thành tổng.",
                "audio": "Log của một tích bằng tổng hai log, log của một thương bằng hiệu hai log. Số mũ bên trong đưa ra ngoài làm hệ số nhân.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc cộng logarit",
                        "problem": "Rút gọn biểu thức $A = \log_6 2 + \log_6 3$.",
                        "solution": "- $A = \log_6(2 \cdot 3) = \log_6 6 = 1$."
                    }
                ],
                "exercise": {"id": "11_19_2", "title": "Kiểm minh chứng", "content": "Giá trị của biểu thức log_2(12) - log_2(3) bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 20: Hàm số mũ và hàm số lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "I. Hàm số mũ": {
                "theory": "Hàm số mũ $y = a^x$ ($0 < a \neq 1$) có TXĐ $D = \mathbb{R}$, tập giá trị $(0; +\infty)$. Nếu $a > 1$, hàm số đồng biến trên $\mathbb{R}$. Nếu $0 < a < 1$, hàm số nghịch biến trên $\mathbb{R}$. Đồ thị đi qua điểm $(0; 1)$ và nằm phía trên trục hoành.",
                "formula": r"y = a^x \implies \text{TGT: } (0; +\infty); \quad a > 1 \implies \text{Đồng biến}",
                "trap": "Hàm số mũ luôn nhận giá trị DƯƠNG. Khi đặt ẩn phụ $t = a^x$, điều kiện bắt buộc là $t > 0$.",
                "audio": "Đồ thị hàm số mũ luôn nằm phía trên trục hoành. Cơ số lớn hơn 1 thì hàm số đi lên, cơ số nhỏ hơn 1 thì hàm số đi xuống.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện chiều biến thiên",
                        "problem": "Hàm số $y = (0.5)^x$ đồng biến hay nghịch biến trên $\mathbb{R}$?",
                        "solution": "- Cơ số $a = 0.5 \in (0; 1)$ nên hàm số nghịch biến trên $\mathbb{R}$."
                    }
                ],
                "exercise": {"id": "11_20_1", "title": "Kiểm minh chứng", "content": "Đồ thị hàm số y = 3^x cắt trục tung tại điểm có tung độ bằng:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Hàm số lôgarit": {
                "theory": "Hàm số lôgarit $y = \log_a x$ ($0 < a \neq 1$) có TXĐ $D = (0; +\infty)$, tập giá trị $\mathbb{R}$. Đồng biến khi $a > 1$, nghịch biến khi $0 < a < 1$. Đồ thị đi qua điểm $(1; 0)$ và nhận trục tung làm tiệm cận đứng.",
                "formula": r"y = \log_a x \implies \text{TXĐ: } x > 0; \quad 0 < a < 1 \implies \text{Nghịch biến}",
                "trap": "Học sinh thường quên đặt điều kiện biểu thức trong dấu logarit lớn hơn 0 khi tìm tập xác định.",
                "audio": "Hàm lôgarit chỉ xác định cho x dương. Cơ số lớn hơn 1 hàm đồng biến, cơ số nhỏ hơn 1 hàm nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định của hàm logarit",
                        "problem": "Tìm tập xác định của $y = \log_2(x - 3)$.",
                        "solution": "- Điều kiện: $x - 3 > 0 \iff x > 3$.\n- Tập xác định $D = (3; +\infty)$."
                    }
                ],
                "exercise": {"id": "11_20_2", "title": "Kiểm minh chứng", "content": "Tập xác định của y = log_3(x - 5) là (c; +vô cực). Giá trị c bằng:", "type": "NUMERIC", "target": "5", "options": []}
            }
        }
    },
    "Bài 21: Phương trình, bất phương trình mũ và lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "I. Phương trình mũ và lôgarit cơ bản": {
                "theory": "Phương trình $a^x = b$: Nếu $b > 0 \implies x = \log_a b$; nếu $b \le 0$ thì vô nghiệm. Phương trình $\log_a x = b \iff x = a^b$.",
                "formula": r"a^x = b \iff x = \log_a b \ (b > 0); \quad \log_a x = b \iff x = a^b",
                "trap": "Giải phương trình logarit bắt buộc phải tìm điều kiện xác định trước để loại nghiệm không phù hợp.",
                "audio": "Phương trình mũ bằng một số dương thì giải bằng logarit. Phương trình logarit thì đội mũ cơ số lên để tìm ẩn x.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình logarit cơ bản",
                        "problem": "Giải phương trình $\log_3(2x - 1) = 2$.",
                        "solution": "- Điều kiện: $2x - 1 > 0 \iff x > 1/2$.\n- Đội mũ: $2x - 1 = 3^2 = 9 \iff 2x = 10 \iff x = 5$ (thỏa mãn)."
                    }
                ],
                "exercise": {"id": "11_21_1", "title": "Kiểm minh chứng", "content": "Nghiệm của phương trình 2^(x - 1) = 8 là x bằng:", "type": "NUMERIC", "target": "4", "options": []}
            },
            "II. Bất phương trình mũ và lôgarit": {
                "theory": "Bất phương trình $a^x > a^y$ hoặc $\log_a x > \log_a y$: Nếu $a > 1$, GIỮ NGUYÊN chiều bất phương trình. Nếu $0 < a < 1$, ĐỔI CHIỀU bất phương trình.",
                "formula": r"a > 1 \implies x > y; \quad 0 < a < 1 \implies x < y",
                "trap": "Quên đổi chiều bất phương trình khi cơ số thuộc khoảng $(0; 1)$. Với logarit phải luôn kẹp điều kiện biểu thức lớn hơn 0.",
                "audio": "Khi giải bất phương trình mũ và logarit, mắt phải nhìn cơ số trước tiên: lớn hơn 1 giữ nguyên chiều, nhỏ hơn 1 đổi ngược chiều.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải bất phương trình cơ số bé hơn 1",
                        "problem": "Giải bất phương trình $(0.5)^x < 0.25$.",
                        "solution": "- Ta có $(0.5)^x < (0.5)^2$.\n- Vì cơ số $0.5 < 1$, đổi chiều bất phương trình: $x > 2$."
                    }
                ],
                "exercise": {"id": "11_21_2", "title": "Kiểm minh chứng", "content": "Tập nghiệm của (1/3)^x < 1/9 là x > c. Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 22: Hai đường thẳng vuông góc": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Góc giữa hai đường thẳng trong không gian": {
                "theory": "Góc giữa hai đường thẳng $a, b$ là góc giữa hai đường thẳng $a', b'$ cùng đi qua một điểm và lần lượt song song với $a, b$. Góc giữa hai đường thẳng thuộc đoạn $[0^\circ; 90^\circ]$.",
                "formula": r"0^\circ \le \widehat{(a, b)} \le 90^\circ; \quad \cos\widehat{(a, b)} = \frac{|\vec{u_a} \cdot \vec{u_b}|}{|\vec{u_a}| \cdot |\vec{u_b}|}",
                "trap": "Học sinh tính góc giữa 2 vectơ chỉ phương ra góc tù (ví dụ $120^\circ$) rồi lấy luôn làm góc giữa 2 đường thẳng. Góc giữa 2 đường thẳng không được vượt quá $90^\circ$, phải lấy bù là $60^\circ$.",
                "audio": "Góc giữa hai đường thẳng trong không gian luôn là góc nhọn hoặc góc vuông, không bao giờ vượt quá chín mươi độ.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định góc giữa hai đường chéo nhau",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D'. Tính góc giữa AB và B'C'.",
                        "solution": "- Vì $B'C' \parallel BC$ nên góc giữa AB và B'C' chính là góc giữa AB và BC.\n- ABCD là hình vuông nên $\widehat{ABC} = 90^\circ$."
                    }
                ],
                "exercise": {"id": "11_22_1", "title": "Kiểm minh chứng", "content": "Hình lập phương ABCD.A'B'C'D'. Góc giữa AA' và CD bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "II. Hai đường thẳng vuông góc": {
                "theory": "Hai đường thẳng gọi là vuông góc với nhau nếu góc giữa chúng bằng $90^\circ$. Trong không gian, hai đường thẳng vuông góc có thể cắt nhau hoặc chéo nhau.",
                "formula": r"a \perp b \iff \vec{u_a} \cdot \vec{u_b} = 0",
                "trap": "Mặc định hai đường thẳng vuông góc thì phải cắt nhau. Trong không gian chúng hoàn toàn có thể chéo nhau.",
                "audio": "Trong không gian, hai đường thẳng vuông góc với nhau có thể cắt nhau hoặc chéo nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai đường vuông góc",
                        "problem": "Cho tứ diện ABCD có AB vuông góc CD. Tích vô hướng $\vec{AB} \cdot \vec{CD}$ bằng bao nhiêu?",
                        "solution": "- Vì $AB \perp CD$ nên tích vô hướng của hai vectơ chỉ phương bằng 0."
                    }
                ],
                "exercise": {"id": "11_22_2", "title": "Kiểm minh chứng", "content": "Nếu u . v = 0 thì góc giữa hai đường thẳng tương ứng bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 23: Đường thẳng vuông góc với mặt phẳng": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Định lý đường thẳng vuông góc với mặt phẳng": {
                "theory": "Đường thẳng $d$ vuông góc với mặt phẳng $(P)$ nếu $d$ vuông góc với HAI đường thẳng CẮT NHAU nằm trong $(P)$. Khi đó, $d$ vuông góc với MỌI đường thẳng nằm trong $(P)$.",
                "formula": r"\begin{cases} d \perp a, d \perp b \\ a \cap b = I; \ a, b \subset (P) \end{cases} \implies d \perp (P)",
                "trap": "Chỉ chứng minh được $d$ vuông góc với hai đường thẳng song song trong $(P)$ thì chưa đủ để kết luận vuông góc với mặt phẳng.",
                "audio": "Muốn chứng minh đường vuông góc với mặt, em cần chỉ ra nó vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng đó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường vuông góc mặt",
                        "problem": "Cho hình chóp S.ABC có $SA \perp (ABC)$, đáy ABC vuông tại B. Chứng minh $BC \perp (SAB)$.",
                        "solution": "- $BC \perp AB$ (do đáy vuông tại B).\n- $BC \perp SA$ (do $SA \perp (ABC)$).\n- $AB$ và $SA$ cắt nhau tại A trong $(SAB)$. Vậy $BC \perp (SAB)$."
                    }
                ],
                "exercise": {"id": "11_23_1", "title": "Kiểm minh chứng", "content": "Để d vuông góc (P) thì d cần vuông góc với tối thiểu mấy đường thẳng cắt nhau trong (P)?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Mối liên hệ giữa quan hệ song song và vuông góc": {
                "theory": "Nếu hai đường thẳng song song, mặt phẳng nào vuông góc với đường này thì cũng vuông góc với đường kia. Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song với nhau.",
                "formula": r"a \parallel b, (P) \perp a \implies (P) \perp b; \quad a \perp (P), b \perp (P) \implies a \parallel b",
                "trap": "Học sinh hay nhầm: Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì song song (sai trong không gian).",
                "audio": "Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì chúng chắc chắn song song với nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận định quan hệ",
                        "problem": "Cho $a \perp (P)$ và $b \parallel a$. Kết luận gì về vị trí của $b$ và $(P)$?",
                        "solution": "- Theo tính chất: $b \perp (P)$."
                    }
                ],
                "exercise": {"id": "11_23_2", "title": "Kiểm minh chứng", "content": "Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Phép chiếu vuông góc và Định lý ba đường vuông góc": {
                "theory": "Phép chiếu song song có phương chiếu vuông góc với mặt phẳng chiếu gọi là phép chiếu vuông góc. Định lý ba đường vuông góc: Đường thẳng $a$ trong $(P)$ vuông góc với đường xiên $d$ khi và chỉ khi nó vuông góc với hình chiếu $d'$ của $d$ trên $(P)$.",
                "formula": r"a \subset (P) \implies (a \perp d \iff a \perp d')",
                "trap": "Đường thẳng $a$ bắt buộc phải nằm hoàn toàn trong mặt phẳng chiếu $(P)$ thì định lý mới áp dụng được.",
                "audio": "Định lý ba đường vuông góc cho phép chuyển việc chứng minh vuông góc với đường xiên sang chứng minh vuông góc với hình chiếu của nó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm hình chiếu của đường xiên",
                        "problem": "Cho hình chóp S.ABC có $SA \perp (ABC)$. Hình chiếu của SB trên mặt phẳng (ABC) là đoạn nào?",
                        "solution": "- Hình chiếu của S là A, hình chiếu của B là B. Hình chiếu của SB là đoạn AB."
                    }
                ],
                "exercise": {"id": "11_24_1", "title": "Kiểm minh chứng", "content": "Cho chóp S.ABC có SA vuông góc đáy. Hình chiếu của SC lên (ABC) là cạnh nào? (Nhập tên cạnh)", "type": "STRING", "target": "AC", "options": []}
            },
            "II. Góc giữa đường thẳng và mặt phẳng": {
                "theory": "Góc giữa đường thẳng $d$ và mặt phẳng $(P)$ là góc giữa $d$ và hình chiếu vuông góc $d'$ của nó trên $(P)$. Số đo góc thuộc đoạn $[0^\circ; 90^\circ]$. Nếu $d \perp (P)$ thì góc bằng $90^\circ$.",
                "formula": r"\widehat{(d, (P))} = \widehat{(d, d')} \quad (0^\circ \le \varphi \le 90^\circ)",
                "trap": "Xác định sai chân đường cao hạ từ đỉnh xuống đáy dẫn đến xác định sai góc.",
                "audio": "Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng đó và cái bóng hình chiếu vuông góc của nó trên mặt đáy.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa đường và mặt",
                        "problem": "Cho chóp S.ABC có $SA \perp (ABC)$, $\Delta ABC$ vuông tại B, $SA = AB = a$. Tính góc giữa SB và (ABC).",
                        "solution": "- Hình chiếu của SB lên (ABC) là AB. Góc cần tìm là $\widehat{SBA}$.\n- Tam giác SAB vuông cân tại A nên $\widehat{SBA} = 45^\circ$."
                    }
                ],
                "exercise": {"id": "11_24_2", "title": "Kiểm minh chứng", "content": "Đường thẳng vuông góc với mặt phẳng thì góc giữa chúng bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 25: Hai mặt phẳng vuông góc": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Định lý và Tính chất hai mặt phẳng vuông góc": {
                "theory": "Mặt phẳng $(P)$ vuông góc với $(Q)$ nếu $(P)$ chứa một đường thẳng vuông góc với $(Q)$. Nếu hai mặt phẳng vuông góc thì bất kỳ đường thẳng nào nằm trong mặt này và vuông góc với GIAO TUYẾN thì sẽ vuông góc với mặt kia.",
                "formula": r"\begin{cases} (P) \supset a \\ a \perp (Q) \end{cases} \implies (P) \perp (Q); \quad \begin{cases} (P) \perp (Q), (P) \cap (Q) = d \\ a \subset (P), a \perp d \end{cases} \implies a \perp (Q)",
                "trap": "Đường thẳng nằm trong mặt phẳng thứ nhất phải vuông góc với GIAO TUYẾN thì mới vuông góc với mặt phẳng thứ hai.",
                "audio": "Hai mặt phẳng vuông góc thì mọi đường thẳng nằm trong mặt này mà vuông góc với giao tuyến sẽ đâm thẳng góc vào mặt kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng vuông góc",
                        "problem": "Cho chóp S.ABCD có $SA \perp (ABCD)$. Chứng minh $(SAC) \perp (ABCD)$.",
                        "solution": "- Mặt phẳng $(SAC)$ chứa đường thẳng $SA$.\n- Mà $SA \perp (ABCD)$ theo giả thiết.\n- Vậy $(SAC) \perp (ABCD)$."
                    }
                ],
                "exercise": {"id": "11_25_1", "title": "Kiểm minh chứng", "content": "Hình hộp chữ nhật có các mặt bên vuông góc với mặt đáy. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 26: Khoảng cách trong không gian": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Khoảng cách từ một điểm đến mặt phẳng": {
                "theory": "Khoảng cách từ $M$ đến mặt phẳng $(P)$ là độ dài đoạn vuông góc $MH$ ($H \in (P)$). Phương pháp dời điểm: Tỉ số khoảng cách bằng tỉ số đoạn thẳng nối từ điểm đến giao điểm của đường nối với mặt phẳng.",
                "formula": r"\frac{d(A, (P))}{d(B, (P))} = \frac{IA}{IB} \quad (AB \cap (P) = I)",
                "trap": "Học sinh thường kẻ bừa một đoạn thẳng rồi nhận nhầm là khoảng cách. Phải dựng chân đường vuông góc chuẩn xác.",
                "audio": "Khoảng cách từ điểm đến mặt là đoạn vuông góc ngắn nhất. Em nên dời điểm về chân đường cao để tính toán nhanh nhất.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách từ chân đường cao",
                        "problem": "Cho chóp S.ABC có $SA \perp (ABC)$, $SA = 3$, đáy là tam giác vuông tại B có $AB = 4$. Tính $d(A, (SBC))$.",
                        "solution": "- Kẻ $AH \perp SB$. Vì $BC \perp (SAB) \implies BC \perp AH$. Suy ra $AH \perp (SBC)$.\n- $\frac{1}{AH^2} = \frac{1}{SA^2} + \frac{1}{AB^2} = \frac{1}{9} + \frac{1}{16} = \frac{25}{144} \implies AH = \frac{12}{5} = 2.4$."
                    }
                ],
                "exercise": {"id": "11_26_1", "title": "Kiểm minh chứng", "content": "Đoạn thẳng MN song song với mặt phẳng (P). Tỉ số d(M, (P)) / d(N, (P)) bằng:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Khoảng cách giữa hai đường thẳng chéo nhau": {
                "theory": "Khoảng cách giữa hai đường thẳng chéo nhau $a$ và $b$ bằng độ dài đoạn vuông góc chung của chúng, hoặc bằng khoảng cách từ $a$ đến mặt phẳng $(P)$ chứa $b$ và song song với $a$.",
                "formula": r"d(a, b) = d(a, (P)) \quad (b \subset (P), a \parallel (P))",
                "trap": "Xác định đoạn vuông góc chung sai vì đoạn thẳng đó không đồng thời vuông góc với cả hai đường.",
                "audio": "Tính khoảng cách hai đường chéo nhau bằng cách dựng mặt phẳng chứa đường này và song song với đường kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện khoảng cách hai đường chéo nhau",
                        "problem": "Đoạn vuông góc chung của hai đường thẳng chéo nhau $a$ và $b$ cắt cả $a$ và $b$. Đúng hay sai?",
                        "solution": "- Đúng theo định nghĩa đoạn vuông góc chung."
                    }
                ],
                "exercise": {"id": "11_26_2", "title": "Kiểm minh chứng", "content": "Đoạn vuông góc chung của 2 đường thẳng chéo nhau tạo với mỗi đường góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 27: Thể tích": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "I. Thể tích khối lăng trụ và Khối chóp": {
                "theory": "Thể tích khối lăng trụ bằng diện tích đáy nhân chiều cao: $V = S \cdot h$. Thể tích khối chóp bằng một phần ba diện tích đáy nhân chiều cao: $V = \frac{1}{3} S \cdot h$.",
                "formula": r"V_{langtru} = S_{day} \cdot h; \quad V_{chop} = \frac{1}{3} S_{day} \cdot h",
                "trap": "Học sinh rất hay quên nhân $\frac{1}{3}$ khi tính thể tích của khối chóp.",
                "audio": "Khối chóp nhọn đầu thì có một phần ba diện tích đáy nhân chiều cao. Khối lăng trụ thì bằng diện tích đáy nhân chiều cao.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính thể tích khối chóp",
                        "problem": "Khối chóp có diện tích đáy bằng $12$, chiều cao bằng $5$. Tính thể tích.",
                        "solution": "- $V = \frac{1}{3} S \cdot h = \frac{1}{3} \cdot 12 \cdot 5 = 20$."
                    }
                ],
                "exercise": {"id": "11_27_1", "title": "Kiểm minh chứng", "content": "Khối chóp có diện tích đáy bằng 9, chiều cao bằng 4. Thể tích bằng:", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "I. Biến cố hợp và Biến cố giao": {
                "theory": "Biến cố hợp $A \cup B$ xảy ra khi có ÍT NHẤT một trong hai biến cố $A$ hoặc $B$ xảy ra. Biến cố giao $AB$ xảy ra khi CẢ HAI biến cố $A$ và $B$ đồng thời xảy ra.",
                "formula": r"A \cup B \iff \text{A hoặc B xảy ra}; \quad AB \iff \text{Cả A và B cùng xảy ra}",
                "trap": "Nhầm lẫn giữa từ 'hoặc' (hợp) và từ 'và' (giao).",
                "audio": "Hợp là phép cộng gộp, chỉ cần một biến cố xảy ra là được. Giao là phần chung, bắt buộc cả hai cùng phải xảy ra đồng thời.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện biến cố giao",
                        "problem": "Gieo con xúc xắc. A: 'Số chấm chẵn', B: 'Số chấm chia hết cho 3'. Xác định biến cố AB.",
                        "solution": "- $A = \{2; 4; 6\}$, $B = \{3; 6\}$.\n- Biến cố giao $AB = \{6\}$."
                    }
                ],
                "exercise": {"id": "11_28_1", "title": "Kiểm minh chứng", "content": "Hai biến cố xung khắc thì biến cố giao của chúng có số phần tử bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Biến cố độc lập": {
                "theory": "Hai biến cố $A$ và $B$ độc lập nếu việc xảy ra của biến cố này không làm ảnh hưởng đến xác suất xảy ra của biến cố kia.",
                "formula": r"A, B \text{ độc lập} \implies P(AB) = P(A) \cdot P(B)",
                "trap": "Nhầm lẫn giữa độc lập và xung khắc. Hai biến cố xung khắc thì không độc lập.",
                "audio": "Hai biến cố độc lập khi xác suất xảy ra của cái này không phụ thuộc vào việc cái kia có xảy ra hay không.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất hai biến cố độc lập",
                        "problem": "Biết $P(A) = 0.4, P(B) = 0.5$ và A, B độc lập. Tính $P(AB)$.",
                        "solution": "- $P(AB) = P(A) \cdot P(B) = 0.4 \cdot 0.5 = 0.2$."
                    }
                ],
                "exercise": {"id": "11_28_2", "title": "Kiểm minh chứng", "content": "P(A) = 0.6, P(B) = 0.5. A và B độc lập. P(AB) bằng:", "type": "NUMERIC", "target": "0.3", "options": []}
            }
        }
    },
    "Bài 29: Công thức cộng xác suất": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "I. Công thức cộng xác suất": {
                "theory": "Với hai biến cố bất kỳ: $P(A \cup B) = P(A) + P(B) - P(AB)$. Nếu $A$ và $B$ xung khắc ($AB = \emptyset$) thì $P(A \cup B) = P(A) + P(B)$.",
                "formula": r"P(A \cup B) = P(A) + P(B) - P(AB)",
                "trap": "Học sinh thường quên trừ phần giao $P(AB)$ khi hai biến cố không xung khắc.",
                "audio": "Khi tính xác suất của biến cố hợp, luôn lấy xác suất từng cái cộng lại rồi trừ đi phần giao chung.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất biến cố hợp",
                        "problem": "Cho $P(A) = 0.5, P(B) = 0.4, P(AB) = 0.1$. Tính $P(A \cup B)$.",
                        "solution": "- $P(A \cup B) = 0.5 + 0.4 - 0.1 = 0.8$."
                    }
                ],
                "exercise": {"id": "11_29_1", "title": "Kiểm minh chứng", "content": "P(A) = 0.4, P(B) = 0.3. A và B xung khắc. P(A hợp B) bằng:", "type": "NUMERIC", "target": "0.7", "options": []}
            }
        }
    },
    "Bài 30: Công thức nhân xác suất cho hai biến cố độc lập": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "I. Công thức nhân xác suất và Biến cố đối": {
                "theory": "Nếu $A$ và $B$ độc lập thì $P(AB) = P(A) \cdot P(B)$. Để tính xác suất có 'ít nhất một' biến cố xảy ra, ta dùng biến cố đối: $P(\text{ít nhất 1}) = 1 - P(\overline{A}) \cdot P(\overline{B})$.",
                "formula": r"P(AB) = P(A) \cdot P(B); \quad P(A \cup B) = 1 - P(\overline{A})P(\overline{B})",
                "trap": "Bài toán có từ 'ít nhất' nếu làm trực tiếp phải chia nhiều trường hợp, dùng biến cố đối sẽ nhanh và tránh thiếu sót.",
                "audio": "Gặp bài toán yêu cầu có ít nhất một người bắn trúng, hãy tính xác suất cả hai cùng trượt rồi lấy 1 trừ đi.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bài toán bắn bia",
                        "problem": "Hai xạ thủ bắn độc lập, xác suất trúng bia là $0.8$ và $0.7$. Tính xác suất cả hai cùng trúng.",
                        "solution": "- $P = 0.8 \cdot 0.7 = 0.56$."
                    }
                ],
                "exercise": {"id": "11_30_1", "title": "Kiểm minh chứng", "content": "P(A) = 0.5, P(B) = 0.4 độc lập. Xác suất cả hai cùng không xảy ra bằng:", "type": "NUMERIC", "target": "0.3", "options": []}
            }
        }
    },
    "Bài 31: Định nghĩa và ý nghĩa của đạo hàm": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "I. Định nghĩa đạo hàm tại một điểm": {
                "theory": "Đạo hàm của $y = f(x)$ tại $x_0$ là giới hạn tỉ số số gia: $f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$. Đạo hàm biểu thị tốc độ thay đổi tức thời của hàm số.",
                "formula": r"f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}",
                "trap": "Nếu giới hạn này không tồn tại hoặc ra vô cực thì hàm số không có đạo hàm tại điểm đó.",
                "audio": "Đạo hàm là tốc độ biến thiên tức thời của hàm số tại một điểm, tính bằng giới hạn của tỉ số số gia.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính đạo hàm bằng định nghĩa",
                        "problem": "Tính đạo hàm của $f(x) = x^2$ tại $x_0 = 3$.",
                        "solution": "- $f'(3) = \lim_{x \to 3} \frac{x^2 - 9}{x - 3} = \lim_{x \to 3} (x + 3) = 6$."
                    }
                ],
                "exercise": {"id": "11_31_1", "title": "Kiểm minh chứng", "content": "Đạo hàm của f(x) = 2x tại x_0 = 4 bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Ý nghĩa hình học và Phương trình tiếp tuyến": {
                "theory": "Hệ số góc của tiếp tuyến của đồ thị $(C)$ tại điểm $M_0(x_0; y_0)$ là $k = f'(x_0)$. Phương trình tiếp tuyến: $y - y_0 = f'(x_0)(x - x_0)$.",
                "formula": r"y - y_0 = f'(x_0)(x - x_0)",
                "trap": "Nhầm lẫn giữa tiếp tuyến TẠI điểm $M_0 \in (C)$ và tiếp tuyến ĐI QUA một điểm bên ngoài.",
                "audio": "Hệ số góc của tiếp tuyến tại một điểm chính là giá trị của đạo hàm tại điểm đó.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập phương trình tiếp tuyến",
                        "problem": "Lập PTTT của $(C): y = x^2$ tại điểm có hoành độ $x_0 = 1$.",
                        "solution": "- $y_0 = 1^2 = 1$.\n- Đạo hàm $y' = 2x \implies k = y'(1) = 2$.\n- Phương trình tiếp tuyến: $y - 1 = 2(x - 1) \iff y = 2x - 1$."
                    }
                ],
                "exercise": {"id": "11_31_2", "title": "Kiểm minh chứng", "content": "Hệ số góc tiếp tuyến của y = x^3 tại x_0 = 2 bằng:", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 32: Các quy tắc tính đạo hàm": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "I. Đạo hàm của tổng, hiệu, tích, thương": {
                "theory": "Các quy tắc: $(u \pm v)' = u' \pm v'$; $(uv)' = u'v + uv'$; $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$. Đạo hàm lượng giác: $(\sin x)' = \cos x$; $(\cos x)' = -\sin x$.",
                "formula": r"(uv)' = u'v + uv'; \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}",
                "trap": "Đạo hàm của thương có dấu TRỪ ở tử số ($u'v - uv'$), học sinh rất hay ghi nhầm thành dấu cộng.",
                "audio": "Đạo hàm của tích bằng u phẩy v cộng u v phẩy. Đạo hàm của thương nhớ có dấu trừ ở tử số và bình phương ở mẫu số.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm của tích",
                        "problem": "Tính đạo hàm của $y = x \cdot \sin x$.",
                        "solution": "- $y' = (x)' \cdot \sin x + x \cdot (\sin x)' = \sin x + x\cos x$."
                    }
                ],
                "exercise": {"id": "11_32_1", "title": "Kiểm minh chứng", "content": "Đạo hàm của y = x^3 - 3x tại x = 2 bằng bao nhiêu?", "type": "NUMERIC", "target": "9", "options": []}
            },
            "II. Đạo hàm của hàm hợp": {
                "theory": "Nếu $y = f(u)$ và $u = u(x)$ thì $y'_x = y'_u \cdot u'_x$. Ví dụ: $(u^n)' = n \cdot u^{n-1} \cdot u'$; $(\sin u)' = u' \cdot \cos u$.",
                "formula": r"y'_x = y'_u \cdot u'_x",
                "trap": "Quên nhân thêm đại lượng $u'$ khi tính đạo hàm hàm hợp.",
                "audio": "Tính đạo hàm hàm hợp giống như bóc vỏ kẹo, đạo hàm hàm ngoài xong phải nhân với đạo hàm của ruột bên trong.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm hàm hợp lũy thừa",
                        "problem": "Tính đạo hàm của $y = (2x + 1)^3$.",
                        "solution": "- $y' = 3(2x + 1)^2 \cdot (2x + 1)' = 3(2x + 1)^2 \cdot 2 = 6(2x + 1)^2$."
                    }
                ],
                "exercise": {"id": "11_32_2", "title": "Kiểm minh chứng", "content": "Đạo hàm của y = (3x - 1)^2 tại x = 1 bằng:", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 33: Đạo hàm cấp hai": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "I. Khái niệm và Ý nghĩa cơ học của đạo hàm cấp hai": {
                "theory": "Đạo hàm cấp hai $f''(x)$ là đạo hàm của đạo hàm cấp một: $f''(x) = [f'(x)]'$. Ý nghĩa vật lý: Gia tốc tức thời của chuyển động bằng đạo hàm cấp hai của phương trình quãng đường: $a(t) = s''(t)$.",
                "formula": r"f''(x) = (f'(x))'; \quad a(t) = s''(t)",
                "trap": "Học sinh thường nhầm gia tốc là đạo hàm cấp 1 (đạo hàm cấp 1 là vận tốc $v(t) = s'(t)$).",
                "audio": "Đạo hàm cấp hai đơn giản là lấy đạo hàm thêm một lần nữa. Trong vật lý, đạo hàm hai lần quãng đường sẽ cho ta gia tốc tức thời.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính gia tốc tức thời",
                        "problem": "Một vật chuyển động có phương trình $s(t) = t^3 - 3t^2 + 2t$. Tính gia tốc tại thời điểm $t = 2$.",
                        "solution": "- Vận tốc $v(t) = s'(t) = 3t^2 - 6t + 2$.\n- Gia tốc $a(t) = s''(t) = 6t - 6$.\n- Tại $t = 2 \implies a(2) = 6(2) - 6 = 6$."
                    }
                ],
                "exercise": {"id": "11_33_1", "title": "Kiểm minh chứng", "content": "Cho y = x^4. Đạo hàm cấp hai y'' tại x = 1 bằng bao nhiêu?", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    }
})
