# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 1: BÀI 1 -> BÀI 8)
# ==============================================================================

GRADE_11_DATA = {}

GRADE_11_DATA.update({
    "Bài 1: Giá trị lượng giác của góc lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "Chủ điểm 1: Đường tròn lượng giác và Dấu của các giá trị lượng giác": {
                "theory": "Đường tròn lượng giác có bán kính $R=1$. Tung độ của điểm $M$ là $\\sin\\alpha$, hoành độ là $\\cos\\alpha$. Dấu của giá trị lượng giác phụ thuộc vào 4 góc phần tư: Nhất cả (I: +,+), Nhì sin (II: sin+, cos-), Tam tang (III: tan+, cot+), Tứ cos (IV: cos+, sin-).",
                "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
                "trap": "Khi tính $\\cos\\alpha$ từ $\\sin\\alpha$ bằng công thức bình phương, học sinh rất hay quên xét điều kiện của góc phần tư để chọn dấu âm hoặc dương, dẫn đến lấy sai nghiệm.",
                "audio": "Nhất cả dương, nhì sin dương, tam tan dương, tứ cos dương. Luôn kiểm tra kỹ góc phần tư trước khi khai căn em nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lượng giác còn lại",
                        "problem": "Cho góc $\\alpha$ thỏa mãn $\\frac{\\pi}{2} < \\alpha < \\pi$ và $\\sin\\alpha = \\frac{3}{5}$. Hãy tính $\\cos\\alpha$.",
                        "solution": "- Ta có $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\left(\\frac{3}{5}\\right)^2 = \\frac{16}{25}$.\n- Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ (Góc phần tư thứ II) nên $\\cos\\alpha < 0$.\n- **Kết luận:** $\\cos\\alpha = -\\frac{4}{5} = -0.8$."
                    },
                    {
                        "title": "Ví dụ 2: Quy đổi độ và radian",
                        "problem": "Đổi góc $120^\\circ$ sang đơn vị radian.",
                        "solution": "- Áp dụng công thức đổi: $\\alpha \\text{ (rad)} = \\frac{a^\\circ \\cdot \\pi}{180^\\circ}$.\n- Thay số: $\\frac{120\\pi}{180} = \\frac{2\\pi}{3}$.\n- **Kết luận:** $120^\\circ = \\frac{2\\pi}{3}$ rad."
                    },
                    {
                        "title": "Ví dụ 3: Rút gọn biểu thức lượng giác",
                        "problem": "Rút gọn biểu thức $A = (1 - \\sin^2\\alpha)\\tan^2\\alpha + (1 - \\cos^2\\alpha)$.",
                        "solution": "- Thay $1 - \\sin^2\\alpha = \\cos^2\\alpha$ và $1 - \\cos^2\\alpha = \\sin^2\\alpha$.\n- $A = \\cos^2\\alpha \\cdot \\frac{\\sin^2\\alpha}{\\cos^2\\alpha} + \\sin^2\\alpha = \\sin^2\\alpha + \\sin^2\\alpha = 2\\sin^2\\alpha$."
                    }
                ],
                "exercise": {
                    "id": "11_1_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho góc alpha thuộc góc phần tư thứ II và sin alpha = 0.6. Giá trị của cos alpha bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "-0.8", 
                    "options": []
                }
            }
        }
    },
    "Bài 2: Công thức lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "Chủ điểm 1: Công thức cộng và Công thức nhân đôi": {
                "theory": "Công thức cộng giúp tính giá trị lượng giác của tổng hoặc hiệu hai góc. Công thức nhân đôi giúp hạ góc từ $2a$ xuống $a$.",
                "formula": r"\cos(a+b) = \cos a\cos b - \sin a\sin b; \quad \sin 2a = 2\sin a\cos a",
                "trap": "Cực kỳ chú ý dấu trong công thức $\\cos(a+b)$. Dấu cộng ở giữa góc thì công thức khai triển phải mang dấu trừ, và ngược lại.",
                "audio": "Cốt cốt sin sin dấu trừ. Sin cos cos sin giữ nguyên dấu. Hãy nhớ kỹ câu thần chú này để không sai công thức cộng nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng công thức cộng",
                        "problem": "Tính giá trị của $\\cos 75^\\circ$ mà không dùng máy tính.",
                        "solution": "- Tách $75^\\circ = 45^\\circ + 30^\\circ$.\n- $\\cos(45^\\circ + 30^\\circ) = \\cos 45^\\circ\\cos 30^\\circ - \\sin 45^\\circ\\sin 30^\\circ$.\n- Thay số: $\\frac{\\sqrt{2}}{2} \\cdot \\frac{\\sqrt{3}}{2} - \\frac{\\sqrt{2}}{2} \\cdot \\frac{1}{2} = \\frac{\\sqrt{6} - \\sqrt{2}}{4}$."
                    },
                    {
                        "title": "Ví dụ 2: Công thức nhân đôi",
                        "problem": "Biết $\\sin a \\cdot \\cos a = 0.25$. Tính giá trị của $\\sin 2a$.",
                        "solution": "- Áp dụng công thức nhân đôi: $\\sin 2a = 2\\sin a\\cos a$.\n- Thay số: $\\sin 2a = 2 \\cdot 0.25 = 0.5$."
                    },
                    {
                        "title": "Ví dụ 3: Hạ bậc tính giá trị",
                        "problem": "Tính giá trị của $\\cos^2 15^\\circ$.",
                        "solution": "- Áp dụng công thức hạ bậc: $\\cos^2 a = \\frac{1 + \\cos 2a}{2}$.\n- $\\cos^2 15^\\circ = \\frac{1 + \\cos 30^\\circ}{2} = \\frac{1 + \\frac{\\sqrt{3}}{2}}{2} = \\frac{2 + \\sqrt{3}}{4}$."
                    }
                ],
                "exercise": {
                    "id": "11_2_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Biết sin a * cos a = 0.4. Giá trị của sin(2a) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0.8", 
                    "options": []
                }
            },
            "Chủ điểm 2: Công thức biến đổi tổng thành tích": {
                "theory": "Dùng để chuyển tổng (hoặc hiệu) của hai hàm sin, cos thành dạng tích, rất hữu ích khi giải phương trình lượng giác đưa về dạng phương trình tích.",
                "formula": r"\cos a + \cos b = 2\cos\frac{a+b}{2}\cos\frac{a-b}{2}; \quad \cos a - \cos b = -2\sin\frac{a+b}{2}\sin\frac{a-b}{2}",
                "trap": "Học sinh thường quên dấu trừ ở đầu công thức biến đổi $\\cos a - \cos b$.",
                "audio": "Cos cộng cos bằng 2 cos cos. Cos trừ cos bằng TRỪ 2 sin sin. Nhớ kỹ dấu trừ ở công thức cos trừ cos nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Biến đổi tổng thành tích",
                        "problem": "Biến đổi thành tích biểu thức $A = \\sin 4x + \\sin 2x$.",
                        "solution": "- Áp dụng công thức $\\sin a + \\sin b = 2\\sin\\frac{a+b}{2}\\cos\\frac{a-b}{2}$.\n- $A = 2\\sin\\left(\\frac{4x+2x}{2}\\right)\\cos\\left(\\frac{4x-2x}{2}\\right) = 2\\sin 3x \\cos x$."
                    },
                    {
                        "title": "Ví dụ 2: Rút gọn phân thức lượng giác",
                        "problem": "Rút gọn biểu thức $B = \\frac{\\cos 3x + \\cos x}{\\sin 3x + \\sin x}$.",
                        "solution": "- Tử số: $\\cos 3x + \\cos x = 2\\cos 2x \\cos x$.\n- Mẫu số: $\\sin 3x + \\sin x = 2\\sin 2x \\cos x$.\n- Rút gọn: $B = \\frac{2\\cos 2x \\cos x}{2\\sin 2x \\cos x} = \\frac{\\cos 2x}{\\sin 2x} = \\cot 2x$."
                    },
                    {
                        "title": "Ví dụ 3: Tính giá trị biểu thức không dùng máy tính",
                        "problem": "Tính giá trị $C = \\cos 75^\\circ + \\cos 15^\\circ$.",
                        "solution": "- $C = 2\\cos\\left(\\frac{75+15}{2}\\right)\\cos\\left(\\frac{75-15}{2}\\right) = 2\\cos 45^\\circ \\cos 30^\\circ$.\n- Thay số: $2 \\cdot \\frac{\\sqrt{2}}{2} \\cdot \\frac{\\sqrt{3}}{2} = \\frac{\\sqrt{6}}{2}$."
                    }
                ],
                "exercise": {
                    "id": "11_2_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Rút gọn biểu thức (sin 4x + sin 2x) / cos x. Kết quả là c * sin(3x). Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 3: Hàm số lượng giác": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "Chủ điểm 1: Tập xác định và Tính chẵn lẻ": {
                "theory": "Hàm $\\sin x, \\cos x$ có tập xác định là $\\mathbb{R}$. Hàm $\\tan x = \\frac{\\sin x}{\\cos x}$ nên điều kiện là $\\cos x \\neq 0$. Trong 4 hàm cơ bản, chỉ có $y = \\cos x$ là hàm chẵn, 3 hàm còn lại là hàm lẻ.",
                "formula": r"\cos(-x) = \cos x \ (\text{Hàm chẵn}); \quad \sin(-x) = -\sin x \ (\text{Hàm lẻ})",
                "trap": "Tìm tập xác định của $\\tan x$ phải cho $\\cos x \\neq 0 \\implies x \\neq \\frac{\\pi}{2} + k\\pi$, học sinh hay ghi nhầm thành $k2\\pi$.",
                "audio": "Cos đối, sin bù, phụ chéo. Hàm cosin là hàm chẵn duy nhất, nên cos của trừ x vẫn bằng cos x.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định",
                        "problem": "Tìm tập xác định của hàm số $y = \\frac{1}{\\cos x}$.",
                        "solution": "- Điều kiện xác định: mẫu số khác $0 \\implies \\cos x \\neq 0$.\n- Giải điều kiện: $x \\neq \\frac{\\pi}{2} + k\\pi, \\ (k \\in \\mathbb{Z})$.\n- **Kết luận:** $D = \\mathbb{R} \\setminus \\left\\{ \\frac{\\pi}{2} + k\\pi \\right\\}$."
                    },
                    {
                        "title": "Ví dụ 2: Xét tính chẵn lẻ",
                        "problem": "Xét tính chẵn lẻ của hàm số $f(x) = x^2 \\sin x$.",
                        "solution": "- Tập xác định $D = \\mathbb{R}$ là tập đối xứng.\n- Ta có $f(-x) = (-x)^2 \\sin(-x) = x^2 (-\\sin x) = -x^2 \\sin x = -f(x)$.\n- **Kết luận:** Hàm số $f(x)$ là hàm số lẻ."
                    },
                    {
                        "title": "Ví dụ 3: Tìm Giá trị lớn nhất, nhỏ nhất",
                        "problem": "Tìm GTLN và GTNN của hàm số $y = 3\\sin x - 1$.",
                        "solution": "- Ta luôn có: $-1 \\le \\sin x \\le 1$.\n- Nhân 3: $-3 \\le 3\\sin x \\le 3$.\n- Trừ 1: $-4 \\le 3\\sin x - 1 \\le 2$.\n- **Kết luận:** GTLN bằng $2$, GTNN bằng $-4$."
                    }
                ],
                "exercise": {
                    "id": "11_3_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị lớn nhất của hàm số y = 4 cos(x) + 3 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "7", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tính tuần hoàn và Đồ thị": {
                "theory": "Hàm $\\sin x, \\cos x$ tuần hoàn với chu kỳ $T = 2\\pi$. Hàm $\\tan x, \\cot x$ tuần hoàn với chu kỳ $T = \\pi$. Đồ thị hàm $\\sin$ đi qua gốc tọa độ, đồ thị hàm $\\cos$ đi qua điểm $(0; 1)$.",
                "formula": r"T = \frac{2\pi}{|a|} \text{ (đối với } y = \sin(ax+b))",
                "trap": "Quên chia cho hệ số $a$ khi tìm chu kỳ của hàm $\\sin(ax)$ hoặc $\\cos(ax)$.",
                "audio": "Chu kỳ của hàm sin và cos là 2 pi, còn tan và cot là 1 pi. Nếu có hệ số a nhân với x, nhớ chia chu kỳ cho trị tuyệt đối của a nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm chu kỳ hàm số",
                        "problem": "Tìm chu kỳ tuần hoàn của hàm số $y = \\cos(2x + \\frac{\\pi}{4})$.",
                        "solution": "- Hàm số cơ bản $y = \\cos x$ có chu kỳ là $2\\pi$.\n- Hệ số của x là $a = 2$.\n- Chu kỳ của hàm số là $T = \\frac{2\\pi}{2} = \\pi$."
                    },
                    {
                        "title": "Ví dụ 2: Đọc đồ thị hàm số",
                        "problem": "Đồ thị hàm số $y = \\sin x$ cắt trục hoành tại các điểm có hoành độ bằng bao nhiêu?",
                        "solution": "- Cắt trục hoành khi $y = 0 \\implies \\sin x = 0$.\n- Giải phương trình: $x = k\\pi \\ (k \\in \\mathbb{Z})$."
                    },
                    {
                        "title": "Ví dụ 3: Chu kỳ hàm tan",
                        "problem": "Tìm chu kỳ của hàm số $y = \\tan(3x)$.",
                        "solution": "- Hàm $y = \\tan x$ có chu kỳ $\\pi$.\n- Hệ số của x là $3 \\implies$ Chu kỳ $T = \\frac{\\pi}{3}$."
                    }
                ],
                "exercise": {
                    "id": "11_3_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Chu kỳ của hàm số y = sin(4x) có dạng T = pi/c. Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 4: Phương trình lượng giác cơ bản": {
        "chapter": "Chương I: Hàm số lượng giác và phương trình lượng giác",
        "topics": {
            "Chủ điểm 1: Phương trình sin x và cos x": {
                "theory": "Phương trình $\\sin x = m$ và $\\cos x = m$ chỉ có nghiệm khi $m \in [-1; 1]$. Cung nghiệm của sin là góc $\\alpha$ và góc bù $(\\pi - \\alpha)$. Cung nghiệm của cos là góc $\\alpha$ và góc đối $(-\\alpha)$.",
                "formula": r"\sin x = \sin\alpha \iff \left[\begin{matrix} x = \alpha + k2\pi \\ x = \pi - \alpha + k2\pi \end{matrix}\right.; \quad \cos x = \cos\alpha \iff x = \pm\alpha + k2\pi",
                "trap": "Học sinh thường quên họ nghiệm thứ hai (góc bù $\\pi - \\alpha$) của phương trình $\\sin x = m$.",
                "audio": "Phương trình sin có hai họ nghiệm bù nhau, còn phương trình cos có hai họ nghiệm đối nhau. Nhớ cộng thêm đuôi k2pi nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình sin",
                        "problem": "Giải phương trình $\\sin x = \\frac{1}{2}$.",
                        "solution": "- Ta có $\\frac{1}{2} = \\sin\\frac{\\pi}{6}$.\n- Áp dụng công thức: $x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\pi - \\frac{\\pi}{6} + k2\\pi = \\frac{5\\pi}{6} + k2\\pi$ ($k \\in \\mathbb{Z}$)."
                    },
                    {
                        "title": "Ví dụ 2: Giải phương trình cos",
                        "problem": "Giải phương trình $\\cos x = 1$.",
                        "solution": "- Đây là trường hợp đặc biệt: $\\cos x = 1 \\iff x = k2\\pi$ ($k \\in \\mathbb{Z}$)."
                    },
                    {
                        "title": "Ví dụ 3: Phương trình vô nghiệm",
                        "problem": "Giải phương trình $\\sin x = 2$.",
                        "solution": "- Vì $-1 \\le \\sin x \\le 1$ với mọi x, nên $\\sin x = 2$ là phương trình vô nghiệm."
                    }
                ],
                "exercise": {
                    "id": "11_4_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Phương trình cos(x) = 1 có một nghiệm nằm trong đoạn [0; pi] là x bằng:", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            },
            "Chủ điểm 2: Phương trình tan x và cot x": {
                "theory": "Phương trình $\\tan x = m$ và $\\cot x = m$ luôn có nghiệm với mọi giá trị của số thực $m$. Chu kỳ tuần hoàn của họ nghiệm là $k\\pi$.",
                "formula": r"\tan x = \tan\alpha \iff x = \alpha + k\pi; \quad \cot x = \cot\alpha \iff x = \alpha + k\pi",
                "trap": "Do quen tay với sin và cos, học sinh thường ghi sai đuôi chu kỳ là $k2\\pi$ thay vì $k\\pi$ đối với phương trình tan và cot.",
                "audio": "Phương trình tan và cot luôn có nghiệm với mọi giá trị m. Đuôi chu kỳ cộng thêm chỉ là k pi, không có số 2 nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình tan",
                        "problem": "Giải phương trình $\\tan x = 1$.",
                        "solution": "- Ta có $1 = \\tan\\frac{\\pi}{4}$.\n- Áp dụng công thức: $x = \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$)."
                    },
                    {
                        "title": "Ví dụ 2: Giải phương trình cot",
                        "problem": "Giải phương trình $\\cot x = 0$.",
                        "solution": "- Ta có $0 = \\cot\\frac{\\pi}{2}$.\n- Áp dụng công thức: $x = \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$)."
                    },
                    {
                        "title": "Ví dụ 3: Tìm nghiệm trên một khoảng",
                        "problem": "Tìm số nghiệm của phương trình $\\tan x = 1$ trên khoảng $(0; \\pi)$.",
                        "solution": "- Họ nghiệm $x = \\frac{\\pi}{4} + k\\pi$.\n- Do $0 < x < \\pi \\implies 0 < \\frac{\\pi}{4} + k\\pi < \\pi \\implies -0.25 < k < 0.75$.\n- Vì $k \\in \\mathbb{Z}$ nên $k = 0$. Phương trình có 1 nghiệm $x = \\frac{\\pi}{4}$."
                    }
                ],
                "exercise": {
                    "id": "11_4_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Số nghiệm của phương trình tan(x) = 1 trên đoạn [0; pi] là bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 5: Dãy số": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "Chủ điểm 1: Khái niệm và Số hạng tổng quát": {
                "theory": "Dãy số là một hàm số xác định trên tập các số nguyên dương $\\mathbb{N}^*$. Dãy số có thể cho bằng liệt kê, bằng công thức số hạng tổng quát $u_n = f(n)$, hoặc bằng hệ thức truy hồi.",
                "formula": r"u_n = f(n) \quad (n \ge 1, n \in \mathbb{Z})",
                "trap": "Học sinh thường quên số hạng đầu tiên của dãy số bắt đầu từ $n=1$, không phải $n=0$.",
                "audio": "Dãy số chẳng qua là một hàm số mà tập xác định là các số tự nhiên lớn hơn 0. Số hạng đầu tiên luôn ứng với n bằng 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng từ công thức tổng quát",
                        "problem": "Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = \\frac{2n - 1}{n + 1}$. Tính $u_3$.",
                        "solution": "- Thay $n = 3$ vào công thức: $u_3 = \\frac{2(3) - 1}{3 + 1} = \\frac{5}{4}$."
                    },
                    {
                        "title": "Ví dụ 2: Dãy số cho bằng truy hồi",
                        "problem": "Cho dãy số $(u_n)$ xác định bởi $u_1 = 2$ và $u_n = u_{n-1} + 3$ với $n \\ge 2$. Tính $u_3$.",
                        "solution": "- Tính $u_2 = u_1 + 3 = 2 + 3 = 5$.\n- Tính $u_3 = u_2 + 3 = 5 + 3 = 8$.\n- **Kết luận:** $u_3 = 8$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định vị trí số hạng",
                        "problem": "Cho dãy số $u_n = 3n + 2$. Số $17$ là số hạng thứ mấy của dãy?",
                        "solution": "- Giải phương trình $u_n = 17 \\iff 3n + 2 = 17 \\iff 3n = 15 \\iff n = 5$.\n- Vậy $17$ là số hạng thứ 5."
                    }
                ],
                "exercise": {
                    "id": "11_5_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho dãy số u_n = 4n - 3. Số hạng u_4 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "13", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tính tăng, giảm và bị chặn của dãy số": {
                "theory": "Xét hiệu $H = u_{n+1} - u_n$. Nếu $H > 0$ thì dãy tăng, nếu $H < 0$ thì dãy nghịch biến. Dãy số bị chặn khi tồn tại 2 hằng số $m, M$ sao cho $m \\le u_n \\le M$ với mọi $n$.",
                "formula": r"u_{n+1} - u_n > 0 \implies \text{Dãy tăng}; \quad m \le u_n \le M \implies \text{Dãy bị chặn}",
                "trap": "Kết luận dãy bị chặn khi mới chỉ chỉ ra được nó bị chặn trên hoặc chặn dưới. Bị chặn phải gồm cả hai phía.",
                "audio": "Để xét tính tăng giảm, ta cứ lấy số hạng sau trừ số hạng trước. Nếu dương là dãy tăng, âm là dãy giảm.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính tăng giảm",
                        "problem": "Xét tính đơn điệu của dãy số $u_n = 2n + 5$.",
                        "solution": "- Xét hiệu $H = u_{n+1} - u_n = [2(n+1) + 5] - [2n + 5] = 2n + 7 - 2n - 5 = 2$.\n- Vì $H = 2 > 0$ với mọi $n \\ge 1$, nên $(u_n)$ là dãy số tăng."
                    },
                    {
                        "title": "Ví dụ 2: Dãy số bị chặn dưới",
                        "problem": "Chứng minh dãy số $u_n = n^2 + 1$ bị chặn dưới.",
                        "solution": "- Vì $n \\ge 1 \\implies n^2 \\ge 1 \\implies u_n = n^2 + 1 \\ge 2$.\n- Dãy số luôn lớn hơn hoặc bằng 2, vậy dãy bị chặn dưới bởi $m=2$."
                    },
                    {
                        "title": "Ví dụ 3: Xét tính bị chặn của dãy phân thức",
                        "problem": "Dãy số $u_n = \\frac{1}{n}$ có bị chặn không?",
                        "solution": "- Ta có $n \\ge 1 \\implies 0 < \\frac{1}{n} \\le 1$.\n- Dãy số thỏa mãn $0 < u_n \\le 1$ với mọi $n \\ge 1$, do đó dãy số bị chặn."
                    }
                ],
                "exercise": {
                    "id": "11_5_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Dãy số u_n = 1/n đạt giá trị lớn nhất bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 6: Cấp số cộng": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Số hạng tổng quát": {
                "theory": "Cấp số cộng (CSC) là dãy số có số hạng sau bằng số hạng ngay trước nó cộng với số không đổi $d$ (công sai). Số hạng tổng quát được tính theo $u_1$ và $d$.",
                "formula": r"u_n = u_{n-1} + d; \quad u_n = u_1 + (n-1)d; \quad u_{k-1} + u_{k+1} = 2u_k",
                "trap": "Học sinh rất hay nhầm công thức tổng quát thành $u_n = u_1 + nd$. Chữ số nhân với $d$ phải luôn là $n-1$.",
                "audio": "Cấp số cộng có quy luật cứ số sau bằng số trước cộng thêm công sai d. Nhớ công thức số hạng thứ n là u1 cộng n trừ 1 nhân d nhé.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng tổng quát",
                        "problem": "Cho cấp số cộng có $u_1 = 3$ và công sai $d = 5$. Tìm $u_6$.",
                        "solution": "- Áp dụng công thức $u_n = u_1 + (n-1)d$.\n- $u_6 = 3 + (6-1) \\cdot 5 = 3 + 25 = 28$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm công sai d",
                        "problem": "Một cấp số cộng có $u_1 = 2$ và $u_4 = 11$. Tìm công sai $d$.",
                        "solution": "- Ta có $u_4 = u_1 + 3d \\implies 11 = 2 + 3d$.\n- $3d = 9 \\implies d = 3$."
                    },
                    {
                        "title": "Ví dụ 3: Tính chất các số hạng liên tiếp",
                        "problem": "Cho 3 số $x, 5, 9$ lập thành một cấp số cộng. Tìm $x$.",
                        "solution": "- Áp dụng tính chất số trung bình cộng: $x + 9 = 2 \\cdot 5$.\n- $x + 9 = 10 \\implies x = 1$."
                    }
                ],
                "exercise": {
                    "id": "11_6_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cấp số cộng có u1 = 5, d = 2. Số hạng u4 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "11", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tổng n số hạng đầu tiên": {
                "theory": "Tổng của $n$ số hạng đầu tiên trong CSC bằng số lượng số hạng nhân với trung bình cộng của số hạng đầu và số hạng cuối.",
                "formula": r"S_n = \frac{n(u_1 + u_n)}{2} = \frac{n[2u_1 + (n-1)d]}{2}",
                "trap": "Bấm máy tính nhầm cụm $(n-1)$ thành $n$ trong công thức $S_n$ dẫn đến sai kết quả toàn bài.",
                "audio": "Tổng cấp số cộng bằng số lượng số hạng nhân với tổng số đầu và số cuối rồi chia đôi. Công thức rất đẹp và dễ nhớ.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng khi biết u1 và d",
                        "problem": "Tính tổng 10 số hạng đầu của cấp số cộng biết $u_1 = 2$ và $d = 3$.",
                        "solution": "- Áp dụng công thức $S_n = \\frac{n[2u_1 + (n-1)d]}{2}$.\n- $S_{10} = \\frac{10[2(2) + 9(3)]}{2} = 5[4 + 27] = 5 \\cdot 31 = 155$."
                    },
                    {
                        "title": "Ví dụ 2: Tính tổng khi biết số đầu và số cuối",
                        "problem": "Một cấp số cộng có 20 số hạng, số hạng đầu là 5 và số hạng cuối là 62. Tính tổng của cấp số cộng đó.",
                        "solution": "- Áp dụng công thức $S_n = \\frac{n(u_1 + u_n)}{2}$.\n- $S_{20} = \\frac{20(5 + 62)}{2} = 10 \\cdot 67 = 670$."
                    },
                    {
                        "title": "Ví dụ 3: Ứng dụng bài toán rạp hát",
                        "problem": "Một rạp hát có 10 hàng ghế. Hàng 1 có 20 ghế, mỗi hàng sau nhiều hơn hàng trước 2 ghế. Tổng số ghế là bao nhiêu?",
                        "solution": "- Đây là CSC với $u_1 = 20, d = 2, n = 10$.\n- $S_{10} = \\frac{10[2(20) + 9(2)]}{2} = 5(40 + 18) = 5 \\cdot 58 = 290$ (ghế)."
                    }
                ],
                "exercise": {
                    "id": "11_6_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính tổng 5 số hạng đầu của CSC có u1 = 2, d = 4.", 
                    "type": "NUMERIC", 
                    "target": "50", 
                    "options": []
                }
            }
        }
    },
    "Bài 7: Cấp số nhân": {
        "chapter": "Chương II: Dãy số. Cấp số cộng và cấp số nhân",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Số hạng tổng quát": {
                "theory": "Cấp số nhân (CSN) là dãy số có số hạng sau bằng số hạng ngay trước nó nhân với một số không đổi $q$ (công bội). Bình phương số hạng ở giữa bằng tích hai số hạng kề nó.",
                "formula": r"u_n = u_{n-1} \cdot q; \quad u_n = u_1 \cdot q^{n-1}; \quad u_{k-1} \cdot u_{k+1} = u_k^2",
                "trap": "Quên điều kiện chia các số hạng để tìm công bội: $q = u_2 / u_1$ với $u_1 \neq 0$.",
                "audio": "Trong cấp số nhân, số sau bằng số trước nhân công bội. Số hạng thứ n bằng u1 nhân với q mũ n trừ 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số hạng tổng quát",
                        "problem": "Cho cấp số nhân có $u_1 = 3$ và công bội $q = 2$. Tìm $u_4$.",
                        "solution": "- Áp dụng công thức $u_n = u_1 \\cdot q^{n-1}$.\n- $u_4 = 3 \\cdot 2^{4-1} = 3 \\cdot 2^3 = 3 \\cdot 8 = 24$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm công bội q",
                        "problem": "Cho cấp số nhân có $u_1 = 2$ và $u_3 = 18$. Tìm công bội $q$ biết $q > 0$.",
                        "solution": "- Ta có $u_3 = u_1 \\cdot q^2 \\implies 18 = 2 \\cdot q^2 \\implies q^2 = 9$.\n- Vì $q > 0$ nên $q = 3$."
                    },
                    {
                        "title": "Ví dụ 3: Tính chất các số hạng liên tiếp",
                        "problem": "Ba số $2, x, 8$ lập thành một cấp số nhân (với $x > 0$). Tìm $x$.",
                        "solution": "- Áp dụng tính chất: $x^2 = 2 \\cdot 8 = 16$.\n- Vì $x > 0$ nên $x = 4$."
                    }
                ],
                "exercise": {
                    "id": "11_7_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cấp số nhân có u1 = 2, q = 3. Số hạng u3 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "18", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tổng n số hạng đầu tiên": {
                "theory": "Tính tổng n số hạng đầu tiên của một cấp số nhân khi biết số hạng đầu và công bội $q \\neq 1$. Cấp số nhân lùi vô hạn là khi $|q| < 1$, ta có thể tính tổng của vô hạn số hạng.",
                "formula": r"S_n = u_1 \frac{1 - q^n}{1 - q} \ (q \neq 1); \quad S = \frac{u_1}{1 - q} \ (|q| < 1)",
                "trap": "Rút gọn phân số bị nhầm dấu khi $q > 1$. Nhầm công thức $q^n$ thành $q^{n-1}$ khi tính tổng.",
                "audio": "Tính tổng cấp số nhân có công thức u1 nhân với phân thức 1 trừ q mũ n chia cho 1 trừ q. Đừng viết nhầm mũ n thành n trừ 1 nhé.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng S_n",
                        "problem": "Tính tổng 4 số hạng đầu của cấp số nhân có $u_1 = 2$ và $q = 3$.",
                        "solution": "- Áp dụng $S_n = u_1 \\frac{1 - q^n}{1 - q}$.\n- $S_4 = 2 \\frac{1 - 3^4}{1 - 3} = 2 \\frac{1 - 81}{-2} = 2 \\frac{-80}{-2} = 80$."
                    },
                    {
                        "title": "Ví dụ 2: Bài toán thực tế sinh học",
                        "problem": "Một loại vi khuẩn cứ sau 1 giờ lại phân đôi 1 lần. Khởi đầu có 100 con. Hỏi sau 3 giờ có bao nhiêu con?",
                        "solution": "- Đây là cấp số nhân với $u_1 = 100$ (tại $t=0$), $q = 2$.\n- Sau 3 giờ là tìm $u_4$ (vì $u_1$ là lúc 0h, $u_2$ là 1h...).\n- $u_4 = 100 \\cdot 2^3 = 800$ con."
                    },
                    {
                        "title": "Ví dụ 3: Tổng cấp số nhân lùi vô hạn",
                        "problem": "Tính tổng vô hạn $S = 1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\dots$",
                        "solution": "- Đây là CSN lùi vô hạn với $u_1 = 1$ và $q = 1/2 < 1$.\n- Áp dụng công thức $S = \\frac{u_1}{1 - q} = \\frac{1}{1 - 1/2} = \\frac{1}{1/2} = 2$."
                    }
                ],
                "exercise": {
                    "id": "11_7_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tổng vô hạn của cấp số nhân u1 = 4, q = 1/2 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            }
        }
    },
    "Bài 8: Mẫu số liệu ghép nhóm": {
        "chapter": "Chương III: Các số đặc trưng đo xu thế trung tâm",
        "topics": {
            "Chủ điểm 1: Khái niệm, Tần số và Giá trị đại diện": {
                "theory": "Khi dữ liệu lớn, ta ghép chúng vào các nửa khoảng $[a; b)$ gọi là nhóm. Độ dài nhóm là $b - a$. Giá trị đại diện của nhóm là trung bình cộng của 2 đầu mút. Tần số tích lũy là tổng tần số của nhóm đó và tất cả các nhóm đứng trước nó.",
                "formula": r"c_i = \frac{a_i + a_{i+1}}{2}; \quad C_k = n_1 + n_2 + \dots + n_k",
                "trap": "Học sinh thường lấy nhầm giá trị đại diện bằng phép trừ $(b-a)/2$ thay vì phép cộng $(a+b)/2$. Độ dài nhóm thì mới dùng phép trừ.",
                "audio": "Giá trị đại diện là trung bình cộng của 2 đầu mút nhóm. Nhớ là cộng vào chia đôi chứ không phải trừ đi nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị đại diện",
                        "problem": "Tìm giá trị đại diện của nhóm số liệu $[20; 30)$.",
                        "solution": "- Công thức giá trị đại diện: $c = \\frac{a + b}{2}$.\n- $c = \\frac{20 + 30}{2} = 25$."
                    },
                    {
                        "title": "Ví dụ 2: Tính độ dài nhóm",
                        "problem": "Tính độ dài của nhóm số liệu $[15.5; 20.5)$.",
                        "solution": "- Độ dài nhóm = Đầu mút phải - Đầu mút trái.\n- Độ dài $= 20.5 - 15.5 = 5$."
                    },
                    {
                        "title": "Ví dụ 3: Tính tần số tích lũy",
                        "problem": "Mẫu số liệu có 3 nhóm với tần số lần lượt là: $n_1 = 5, n_2 = 12, n_3 = 8$. Tính tần số tích lũy của nhóm thứ 2.",
                        "solution": "- Tần số tích lũy nhóm 2 bằng tổng tần số nhóm 1 và nhóm 2.\n- $C_2 = n_1 + n_2 = 5 + 12 = 17$."
                    }
                ],
                "exercise": {
                    "id": "11_8_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị đại diện của nhóm [40; 50) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "45", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 2: BÀI 9 -> BÀI 16)
# ==============================================================================

GRADE_11_DATA.update({
    "Bài 9: Các số đặc trưng đo xu thế trung tâm": {
        "chapter": "Chương III: Các số đặc trưng đo xu thế trung tâm của mẫu ghép nhóm",
        "topics": {
            "Chủ điểm 1: Số trung bình và Mốt của mẫu ghép nhóm": {
                "theory": "Số trung bình bằng tổng các tích của tần số và giá trị đại diện chia cho cỡ mẫu. Mốt ($M_o$) là giá trị đại diện cho nhóm có tần số lớn nhất (nhóm chứa mốt), được tính bằng công thức nội suy.",
                "formula": r"\overline{x} = \frac{1}{n}\sum_{i=1}^k n_ic_i; \quad M_o = u_m + \frac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \cdot h",
                "trap": "Học sinh rất hay lấy sai $n_{m-1}$ (tần số nhóm liền trước) và $n_{m+1}$ (tần số nhóm liền sau) khi áp dụng công thức Mốt.",
                "audio": "Số trung bình tính bằng cách nhân tần số với trung điểm rồi cộng lại. Còn Mốt thì phụ thuộc vào nhóm có tần số đỉnh, cộng thêm phần nội suy.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính số trung bình",
                        "problem": "Cho mẫu số liệu: [10; 20) tần số 5, [20; 30) tần số 15. Tính số trung bình.",
                        "solution": "- Giá trị đại diện lần lượt là $c_1=15, c_2=25$. Cỡ mẫu $n = 5+15 = 20$.\n- $\\overline{x} = \\frac{5 \\cdot 15 + 15 \\cdot 25}{20} = \\frac{75 + 375}{20} = \\frac{450}{20} = 22.5$."
                    },
                    {
                        "title": "Ví dụ 2: Xác định nhóm chứa Mốt",
                        "problem": "Cho các nhóm: [0; 5) có 10 người, [5; 10) có 20 người, [10; 15) có 8 người. Xác định nhóm chứa mốt.",
                        "solution": "- Nhóm có tần số lớn nhất là nhóm [5; 10) với 20 người.\n- Vậy nhóm chứa mốt là [5; 10)."
                    },
                    {
                        "title": "Ví dụ 3: Tính Mốt (M_o)",
                        "problem": "Từ dữ liệu Ví dụ 2, hãy tính giá trị Mốt.",
                        "solution": "- Nhóm chứa mốt: $[5; 10) \\implies u_m=5, h=5, n_m=20$.\n- Nhóm trước: $n_{m-1} = 10$. Nhóm sau: $n_{m+1} = 8$.\n- $M_o = 5 + \\frac{20 - 10}{(20 - 10) + (20 - 8)} \\cdot 5 = 5 + \\frac{10}{10 + 12} \\cdot 5 = 5 + \\frac{50}{22} \\approx 7.27$."
                    }
                ],
                "exercise": {
                    "id": "11_9_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị đại diện của nhóm [40; 50) là bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "45", 
                    "options": []
                }
            },
            "Chủ điểm 2: Trung vị và Tứ phân vị": {
                "theory": "Trung vị ($M_e$) là tứ phân vị thứ hai ($Q_2$), chia mẫu số liệu làm hai nửa bằng nhau. Nhóm chứa trung vị là nhóm đầu tiên có tần số tích lũy lớn hơn hoặc bằng $n/2$.",
                "formula": r"M_e = Q_2 = u_m + \frac{\frac{n}{2} - C}{n_m} \cdot h",
                "trap": "Đại lượng $C$ trong công thức là tần số tích lũy của các nhóm ĐỨNG NGAY TRƯỚC nhóm chứa trung vị, không bao gồm nhóm hiện tại.",
                "audio": "Trung vị chia mẫu số liệu làm hai phần bằng nhau. Nhớ tính tần số tích lũy cẩn thận và xác định đúng nhóm chứa trung vị nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định nhóm chứa trung vị",
                        "problem": "Cỡ mẫu $n = 40$. Các nhóm [1;3) tần số 12, [3;5) tần số 15, [5;7) tần số 13. Tìm nhóm chứa trung vị.",
                        "solution": "- Tính $n/2 = 40/2 = 20$.\n- Tần số tích lũy: Nhóm 1 là 12 (<20). Nhóm 2 là $12+15=27$ ($\\ge 20$).\n- Nhóm chứa trung vị là [3; 5)."
                    },
                    {
                        "title": "Ví dụ 2: Tính Trung vị",
                        "problem": "Từ dữ liệu trên, hãy tính trung vị của mẫu số liệu.",
                        "solution": "- Nhóm chứa trung vị $[3; 5) \\implies u_m=3, h=2, n_m=15$.\n- $C = 12$ (tần số nhóm đứng trước).\n- $M_e = 3 + \\frac{20 - 12}{15} \\cdot 2 = 3 + \\frac{16}{15} \\approx 4.07$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định nhóm chứa Q1",
                        "problem": "Với mẫu $n=40$, vị trí của tứ phân vị thứ nhất $Q_1$ nằm ở giá trị thứ mấy và thuộc nhóm nào?",
                        "solution": "- Vị trí của $Q_1$ là $n/4 = 40/4 = 10$.\n- Nhóm đầu tiên [1; 3) có tần số 12 $\\ge 10$, nên nó chứa $Q_1$."
                    }
                ],
                "exercise": {
                    "id": "11_9_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu cỡ mẫu là n=100, nhóm chứa trung vị là nhóm có tần số tích lũy đạt tối thiểu bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "50", 
                    "options": []
                }
            }
        }
    },
    "Bài 10: Đường thẳng và mặt phẳng trong không gian": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "Chủ điểm 1: Các tính chất thừa nhận & Cách cho mặt phẳng": {
                "theory": "Có 3 cách xác định duy nhất một mặt phẳng: (1) Đi qua 3 điểm không thẳng hàng. (2) Đi qua 1 đường thẳng và 1 điểm không thuộc đường thẳng đó. (3) Đi qua 2 đường thẳng cắt nhau.",
                "formula": r"A, B, C \text{ không thẳng hàng} \implies \exists! \ (ABC)",
                "trap": "3 điểm thẳng hàng thì có vô số mặt phẳng đi qua chúng. Bắt buộc phải có chữ 'không thẳng hàng'.",
                "audio": "Ba điểm không thẳng hàng tạo nên một chiếc kiềng ba chân vững chắc, và đó cũng là cách cơ bản nhất để xác định một mặt phẳng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Số mặt phẳng qua 3 điểm",
                        "problem": "Có bao nhiêu mặt phẳng đi qua 3 điểm phân biệt không thẳng hàng?",
                        "solution": "- Theo tính chất thừa nhận, qua 3 điểm không thẳng hàng có duy nhất một mặt phẳng. Số lượng là 1."
                    },
                    {
                        "title": "Ví dụ 2: Số mặt phẳng trong tứ diện",
                        "problem": "Cho tứ diện ABCD. Có bao nhiêu mặt phẳng đi qua 3 trong 4 đỉnh của tứ diện?",
                        "solution": "- Tứ diện có 4 đỉnh không đồng phẳng. Chọn 3 đỉnh bất kỳ sẽ tạo thành 1 mặt.\n- Số mặt phẳng là $C_4^3 = 4$ mặt (chính là 4 mặt của tứ diện)."
                    },
                    {
                        "title": "Ví dụ 3: Xác định mặt phẳng qua đường thẳng và điểm",
                        "problem": "Cho đường thẳng d và điểm A không thuộc d. Có bao nhiêu mặt phẳng chứa d và A?",
                        "solution": "- Theo cách xác định mặt phẳng thứ hai: Có duy nhất 1 mặt phẳng."
                    }
                ],
                "exercise": {
                    "id": "11_10_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Một hình chóp tứ giác (đáy là hình tứ giác) có tổng cộng bao nhiêu mặt bên?", 
                    "type": "NUMERIC", 
                    "target": "4", 
                    "options": []
                }
            },
            "Chủ điểm 2: Giao tuyến của hai mặt phẳng và Giao điểm đường - mặt": {
                "theory": "Nếu hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường thẳng chung duy nhất đi qua điểm đó, gọi là giao tuyến. Để tìm giao tuyến, ta tìm 2 điểm chung phân biệt.",
                "formula": r"(P) \cap (Q) = d; \quad d \cap (P) = M",
                "trap": "Điểm chung thứ hai thường là giao điểm của hai đường thẳng cùng nằm trong một mặt phẳng đáy hoặc mặt bên. Rất nhiều học sinh cho hai đường thẳng chéo nhau cắt nhau.",
                "audio": "Giao tuyến của hai mặt phẳng là một đường thẳng. Để tìm nó, em chỉ cần tìm hai điểm chung của hai mặt phẳng là xong.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giao tuyến cơ bản",
                        "problem": "Cho hình chóp S.ABCD. Tìm giao tuyến của mặt phẳng (SAB) và (SBC).",
                        "solution": "- Hai mặt phẳng cùng chứa đỉnh S $\\implies$ S là điểm chung thứ nhất.\n- Hai mặt phẳng cùng chứa đỉnh B $\\implies$ B là điểm chung thứ hai.\n- Vậy giao tuyến là đường thẳng SB."
                    },
                    {
                        "title": "Ví dụ 2: Giao tuyến chứa đường chéo",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành tâm O. Tìm giao tuyến của (SAC) và (SBD).",
                        "solution": "- Điểm chung thứ nhất rõ ràng là S.\n- Trong mặt đáy (ABCD), hai đường chéo AC và BD cắt nhau tại O. O thuộc AC nên O thuộc (SAC). O thuộc BD nên O thuộc (SBD).\n- Vậy giao tuyến là đường thẳng SO."
                    },
                    {
                        "title": "Ví dụ 3: Giao điểm của đường và mặt",
                        "problem": "Cho hình chóp S.ABCD, M là trung điểm SC. Tìm giao điểm của AM và (SBD).",
                        "solution": "- Trong (SAC), gọi I là giao điểm của AM và SO.\n- Vì SO nằm trong (SBD) nên I nằm trong (SBD).\n- Vậy giao điểm của AM và (SBD) chính là I."
                    }
                ],
                "exercise": {
                    "id": "11_10_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giao tuyến của mặt phẳng (SAD) và (SCD) trong hình chóp S.ABCD là đường thẳng nào? (Nhập tên đường, vd: SA)", 
                    "type": "STRING", 
                    "target": "SD", 
                    "options": []
                }
            }
        }
    },
    "Bài 11: Hai đường thẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "Chủ điểm 1: Vị trí tương đối của hai đường thẳng": {
                "theory": "Trong không gian, 2 đường thẳng có 4 vị trí: Cắt nhau, Song song, Trùng nhau (Đồng phẳng) và Chéo nhau (Không đồng phẳng - không có mặt phẳng nào chứa cả hai đường).",
                "formula": r"a \parallel b \implies \text{Cùng thuộc } (P), a \cap b = \emptyset; \quad a, b \text{ chéo nhau} \implies \text{Không đồng phẳng}",
                "trap": "Nếu hai đường thẳng không có điểm chung, chúng có thể song song HOẶC chéo nhau. Không được vội kết luận là song song.",
                "audio": "Khác với hình học phẳng, trong không gian, hai đường thẳng không cắt nhau chưa chắc đã song song, chúng có thể chéo nhau đấy nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận dạng đường chéo nhau",
                        "problem": "Cho tứ diện ABCD. Đường thẳng AB và CD có vị trí tương đối thế nào?",
                        "solution": "- 4 đỉnh A, B, C, D không đồng phẳng.\n- Nếu AB và CD song song hoặc cắt nhau thì chúng phải đồng phẳng, vô lý.\n- Vậy AB và CD chéo nhau."
                    },
                    {
                        "title": "Ví dụ 2: Song song trong không gian",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành. Đường thẳng AB song song với đường thẳng nào?",
                        "solution": "- Vì ABCD là hình bình hành nên AB song song với CD.\n- Trong không gian, tính chất hình bình hành ở đáy vẫn được giữ nguyên."
                    },
                    {
                        "title": "Ví dụ 3: Định lý giao tuyến 3 mặt phẳng",
                        "problem": "Ba mặt phẳng cắt nhau theo 3 giao tuyến phân biệt thì 3 giao tuyến đó có tính chất gì?",
                        "solution": "- Theo định lý về giao tuyến của 3 mặt phẳng, 3 giao tuyến đó hoặc đồng quy tại 1 điểm, hoặc đôi một song song với nhau."
                    }
                ],
                "exercise": {
                    "id": "11_11_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hai đường thẳng không có điểm chung thì CHẮC CHẮN song song. Khẳng định này Đúng(1) hay Sai(0)?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 12: Đường thẳng và mặt phẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "Chủ điểm 1: Điều kiện để đường thẳng song song với mặt phẳng": {
                "theory": "Đường thẳng $d$ song song với mặt phẳng $(P)$ nếu $d$ KHÔNG nằm trong $(P)$ và $d$ song song với MỘT đường thẳng $a$ nằm trong $(P)$.",
                "formula": r"\begin{cases} d \not\subset (P) \\ a \subset (P) \\ d \parallel a \end{cases} \implies d \parallel (P)",
                "trap": "Bắt buộc phải có điều kiện 'd không nằm trong (P)'. Nếu quên, đường thẳng có thể trùng vào mặt phẳng.",
                "audio": "Để chứng minh đường thẳng song song mặt phẳng, em hãy tìm trong mặt phẳng đó một đường thẳng song song với đường thẳng đã cho.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường song song mặt",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành. Chứng minh AB song song với mặt phẳng (SCD).",
                        "solution": "- Ta có $AB \\parallel CD$ (do ABCD là hình bình hành).\n- $CD \\subset (SCD)$ và $AB \\not\\subset (SCD)$.\n- **Kết luận:** $AB \\parallel (SCD)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chất của đường song song mặt",
                        "problem": "Cho $d \\parallel (P)$. Một mặt phẳng $(Q)$ chứa $d$ và cắt $(P)$ theo giao tuyến $d'$. Nhận xét vị trí của $d$ và $d'$.",
                        "solution": "- Theo tính chất, giao tuyến của mặt phẳng chứa đường thẳng này với mặt phẳng kia sẽ song song với đường thẳng đó.\n- **Kết luận:** $d \\parallel d'$."
                    },
                    {
                        "title": "Ví dụ 3: Sai lầm thường gặp",
                        "problem": "Nếu $d \\parallel (P)$ thì $d$ song song với mọi đường thẳng nằm trong $(P)$ đúng không?",
                        "solution": "- Khẳng định này SAI. $d$ chỉ song song với các đường thẳng trong $(P)$ cùng phương với nó. Với các đường thẳng khác trong $(P)$, $d$ và chúng sẽ là hai đường thẳng chéo nhau."
                    }
                ],
                "exercise": {
                    "id": "11_12_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường thẳng d nằm hoàn toàn trong (P). Hỏi d có song song với (P) không? (1: Có, 0: Không)", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 13: Hai mặt phẳng song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "Chủ điểm 1: Điều kiện để hai mặt phẳng song song": {
                "theory": "Mặt phẳng $(P)$ song song với mặt phẳng $(Q)$ nếu $(P)$ chứa HAI đường thẳng CẮT NHAU cùng song song với $(Q)$.",
                "formula": r"\begin{cases} a, b \subset (P), \ a \cap b = I \\ a \parallel (Q), \ b \parallel (Q) \end{cases} \implies (P) \parallel (Q)",
                "trap": "Hai đường thẳng $a, b$ nằm trong mặt phẳng $(P)$ bắt buộc phải CẮT NHAU. Nếu chúng song song thì không đủ điều kiện kết luận.",
                "audio": "Để chứng minh hai mặt phẳng song song, em cần tìm hai đường thẳng cắt nhau trong mặt phẳng này, và chứng minh chúng lần lượt song song với mặt phẳng kia.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng song song",
                        "problem": "Cho hình chóp S.ABCD đáy hình bình hành. M, N, P lần lượt là trung điểm của SA, SB, SC. Chứng minh (MNP) // (ABCD).",
                        "solution": "- M, N là trung điểm SA, SB $\\implies MN \\parallel AB \\implies MN \\parallel (ABCD)$.\n- N, P là trung điểm SB, SC $\\implies NP \\parallel BC \\implies NP \\parallel (ABCD)$.\n- MN và NP cắt nhau tại N nằm trong (MNP).\n- **Kết luận:** $(MNP) \\parallel (ABCD)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chất mặt phẳng cắt hai mp song song",
                        "problem": "Hai mặt phẳng $(P)$ và $(Q)$ song song. Mặt phẳng $(R)$ cắt $(P)$ theo giao tuyến $a$, cắt $(Q)$ theo giao tuyến $b$. $a$ và $b$ như thế nào?",
                        "solution": "- Giao tuyến của một mặt phẳng với hai mặt phẳng song song luôn là hai đường thẳng song song.\n- **Kết luận:** $a \\parallel b$."
                    },
                    {
                        "title": "Ví dụ 3: Định lý Thales trong không gian",
                        "problem": "Ba mặt phẳng song song cắt 2 cát tuyến tạo ra các đoạn thẳng. Tính chất tỉ lệ là gì?",
                        "solution": "- Ba mặt phẳng song song chắn trên hai cát tuyến bất kỳ những đoạn thẳng tương ứng tỉ lệ. (Định lý Thales trong không gian)."
                    }
                ],
                "exercise": {
                    "id": "11_13_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hai mặt phẳng phân biệt cùng song song với một đường thẳng thì chắc chắn song song với nhau. Đúng(1) hay Sai(0)?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 14: Phép chiếu song song": {
        "chapter": "Chương IV: Quan hệ song song trong không gian",
        "topics": {
            "Chủ điểm 1: Tính chất của phép chiếu song song": {
                "theory": "Phép chiếu song song biến ba điểm thẳng hàng thành ba điểm thẳng hàng và bảo toàn thứ tự. Biến đường thẳng thành đường thẳng. Bảo toàn tính song song và tỉ số độ dài của hai đoạn thẳng cùng phương.",
                "formula": r"\text{Bảo toàn song song và tỉ số: } \frac{A'B'}{C'D'} = \frac{AB}{CD} \ (\text{Nếu } AB \parallel CD)",
                "trap": "Phép chiếu song song KHÔNG bảo toàn độ lớn của góc và KHÔNG bảo toàn khoảng cách (độ dài thực).",
                "audio": "Phép chiếu song song bảo toàn tính thẳng hàng, song song và tỉ số đoạn thẳng. Nhưng không bảo toàn số đo góc đâu nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Hình chiếu của các đa giác",
                        "problem": "Hình chiếu song song của một hình vuông có thể là hình gì?",
                        "solution": "- Phép chiếu song song bảo toàn tính song song của các cặp cạnh đối, nhưng không bảo toàn góc vuông.\n- **Kết luận:** Hình chiếu của hình vuông là một hình bình hành (hoặc 1 đoạn thẳng nếu mp chứa hình vuông song song phương chiếu)."
                    },
                    {
                        "title": "Ví dụ 2: Hình chiếu của đường tròn",
                        "problem": "Hình chiếu song song của một đường tròn lên một mặt phẳng là hình gì?",
                        "solution": "- Trừ trường hợp suy biến thành đoạn thẳng, hình chiếu song song của một đường tròn luôn là một hình elip."
                    },
                    {
                        "title": "Ví dụ 3: Bảo toàn tỉ số",
                        "problem": "M là trung điểm AB. Hình chiếu song song của M là M', của A là A', của B là B'. M' có vị trí gì?",
                        "solution": "- Phép chiếu song song bảo toàn tỉ số trên một đoạn thẳng. $\\frac{AM}{MB} = 1$.\n- Do đó $\\frac{A'M'}{M'B'} = 1 \\implies M'$ là trung điểm của $A'B'$."
                    }
                ],
                "exercise": {
                    "id": "11_14_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Phép chiếu song song có luôn bảo toàn số đo của một góc không? (1: Có, 0: Không)", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 15: Giới hạn của dãy số": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "Chủ điểm 1: Giới hạn phân thức hữu tỉ": {
                "theory": "Dãy số có giới hạn $0$ khi $n \to \\infty$ với các dạng $1/n^k$. Khử dạng vô định $\\frac{\\infty}{\\infty}$ bằng cách chia cả tử và mẫu cho lũy thừa bậc cao nhất của $n$.",
                "formula": r"\lim_{n \to +\infty} \frac{1}{n^k} = 0 \ (k > 0); \quad \lim q^n = 0 \ (|q| < 1)",
                "trap": "Học sinh thường chia sai các số hạng nằm trong dấu căn. Nhớ đưa $n$ vào trong căn bậc hai phải thành $n^2$.",
                "audio": "Cách giải kinh điển của giới hạn dãy số phân thức là chia cả tử và mẫu cho lũy thừa cao nhất của n.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chia cho n bậc nhất",
                        "problem": "Tính giới hạn $\\lim \\frac{4n + 3}{2n - 1}$.",
                        "solution": "- Bậc cao nhất của tử và mẫu là $n$. Chia cả tử và mẫu cho $n$:\n- $\\lim \\frac{4 + 3/n}{2 - 1/n} = \\frac{4 + 0}{2 - 0} = 2$."
                    },
                    {
                        "title": "Ví dụ 2: Bậc tử bé hơn bậc mẫu",
                        "problem": "Tính giới hạn $\\lim \\frac{n^2 + 1}{2n^3 - n}$.",
                        "solution": "- Bậc mẫu lớn hơn bậc tử. Chia cả 2 vế cho $n^3$:\n- $\\lim \\frac{1/n + 1/n^3}{2 - 1/n^2} = \\frac{0}{2} = 0$."
                    },
                    {
                        "title": "Ví dụ 3: Dãy số mũ",
                        "problem": "Tính giới hạn $\\lim \\frac{3^n + 2}{2 \\cdot 3^n - 1}$.",
                        "solution": "- Chia cả tử và mẫu cho $3^n$ (cơ số lớn nhất):\n- $\\lim \\frac{1 + 2/3^n}{2 - 1/3^n} = \\frac{1 + 0}{2 - 0} = 0.5$."
                    }
                ],
                "exercise": {
                    "id": "11_15_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính giới hạn: lim (6n + 5)/(2n + 1) khi n tiến ra dương vô cực.", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tổng cấp số nhân lùi vô hạn": {
                "theory": "Cấp số nhân lùi vô hạn là CSN có công bội $q$ thỏa mãn $|q| < 1$. Tổng của vô hạn số hạng hội tụ về một hằng số xác định.",
                "formula": r"S = u_1 + u_1 q + u_1 q^2 + \dots = \frac{u_1}{1 - q} \quad (|q| < 1)",
                "trap": "Nếu $|q| \\ge 1$ thì tổng sẽ phân kỳ ra vô cực, không được dùng công thức này.",
                "audio": "Tổng lùi vô hạn bằng số hạng đầu chia cho 1 trừ đi công bội. Rất ngắn gọn phải không nào.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng chuỗi phân số",
                        "problem": "Tính tổng $S = 1 + \\frac{1}{3} + \\frac{1}{9} + \\dots + \\left(\\frac{1}{3}\\right)^n + \dots$",
                        "solution": "- Đây là CSN lùi vô hạn với $u_1 = 1$, $q = 1/3$ (do $|1/3| < 1$).\n- $S = \\frac{1}{1 - 1/3} = \\frac{1}{2/3} = 1.5$."
                    },
                    {
                        "title": "Ví dụ 2: Dấu trừ xen kẽ",
                        "problem": "Tính tổng $S = 2 - 1 + \\frac{1}{2} - \\frac{1}{4} + \dots$",
                        "solution": "- Số hạng đầu $u_1 = 2$. Công bội $q = -1/2$.\n- $S = \\frac{2}{1 - (-1/2)} = \\frac{2}{3/2} = \\frac{4}{3}$."
                    },
                    {
                        "title": "Ví dụ 3: Đổi số thập phân vô hạn tuần hoàn",
                        "problem": "Đổi số $0.3333\\dots = 0.(3)$ ra phân số.",
                        "solution": "- $0.333 = 0.3 + 0.03 + 0.003 + \\dots = \\frac{3}{10} + \\frac{3}{100} + \\frac{3}{1000} + \\dots$\n- Đây là tổng lùi vô hạn với $u_1 = 3/10, q = 1/10$.\n- $S = \\frac{3/10}{1 - 1/10} = \\frac{3/10}{9/10} = \\frac{1}{3}$."
                    }
                ],
                "exercise": {
                    "id": "11_15_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính tổng vô hạn của cấp số nhân u1 = 1, q = 1/2. S bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 16: Giới hạn của hàm số": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "Chủ điểm 1: Giới hạn dạng 0/0": {
                "theory": "Khi thay $x = x_0$ vào phân thức mà cả tử và mẫu đều bằng 0, ta có dạng vô định $0/0$. Khử dạng này bằng cách phân tích đa thức thành nhân tử để triệt tiêu đại lượng $(x - x_0)$. Nếu có căn thức, phải nhân lượng liên hợp.",
                "formula": r"\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{(x-x_0)A(x)}{(x-x_0)B(x)} = \lim_{x \to x_0} \frac{A(x)}{B(x)}",
                "trap": "Rất nhiều học sinh quên ghi chữ 'lim' trong các bước nháp trung gian, đi thi tự luận sẽ bị trừ điểm trình bày.",
                "audio": "Gặp dạng 0 chia 0, em hãy dùng hằng đẳng thức hoặc bấm máy tính tách nghiệm để rút gọn nhân tử chung ở cả tử và mẫu nhé.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phân tích nhân tử cơ bản",
                        "problem": "Tính giới hạn $I = \\lim_{x \\to 1} \\frac{x^2 - 1}{x - 1}$.",
                        "solution": "- Thay $x=1$ thấy dạng $0/0$.\n- Tử số $x^2 - 1 = (x-1)(x+1)$.\n- $I = \\lim_{x \\to 1} \\frac{(x-1)(x+1)}{x-1} = \\lim_{x \\to 1} (x+1) = 2$."
                    },
                    {
                        "title": "Ví dụ 2: Đa thức bậc hai",
                        "problem": "Tính $\\lim_{x \\to 2} \\frac{x^2 - 5x + 6}{x - 2}$.",
                        "solution": "- Tử số bấm máy có 2 nghiệm là 2 và 3 $\\implies x^2 - 5x + 6 = (x-2)(x-3)$.\n- Rút gọn $(x-2)$: Giới hạn còn $\\lim_{x \\to 2} (x - 3) = -1$."
                    },
                    {
                        "title": "Ví dụ 3: Nhân lượng liên hợp",
                        "problem": "Tính $\\lim_{x \\to 0} \\frac{\\sqrt{x+1} - 1}{x}$.",
                        "solution": "- Nhân cả tử và mẫu với lượng liên hợp $(\\sqrt{x+1} + 1)$.\n- Tử số: $(\\sqrt{x+1} - 1)(\\sqrt{x+1} + 1) = x + 1 - 1 = x$.\n- Triệt tiêu $x$: Giới hạn còn $\\lim_{x \\to 0} \\frac{1}{\\sqrt{x+1} + 1} = \\frac{1}{2} = 0.5$."
                    }
                ],
                "exercise": {
                    "id": "11_16_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính giới hạn lim(x^2 - 4)/(x - 2) khi x tiến tới 2.", 
                    "type": "NUMERIC", 
                    "target": "4", 
                    "options": []
                }
            },
            "Chủ điểm 2: Giới hạn một bên": {
                "theory": "Giới hạn bên phải (khi $x \\to x_0^+$) và giới hạn bên trái (khi $x \\to x_0^-$). Hàm số chỉ có giới hạn tại $x_0$ khi và chỉ khi cả hai giới hạn một bên tồn tại và BẰNG NHAU.",
                "formula": r"\lim_{x \to x_0^+} f(x) = \lim_{x \to x_0^-} f(x) = L \iff \lim_{x \to x_0} f(x) = L",
                "trap": "Hàm phân nhánh thường gài bẫy giới hạn trái và phải khác nhau, khi đó phải kết luận hàm số KHÔNG có giới hạn tại điểm đó.",
                "audio": "Giới hạn bên phải và bên trái phải bằng nhau thì giới hạn chung tại điểm đó mới tồn tại. Đây là lý thuyết nền tảng cho bài Hàm số liên tục.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giới hạn một bên của phân thức",
                        "problem": "Tính $\\lim_{x \\to 1^+} \\frac{2x + 1}{x - 1}$.",
                        "solution": "- Tử số tiến đến 3 (>0).\n- Mẫu số tiến đến 0 và vì $x \\to 1^+$ (tức $x>1$) nên $x - 1 > 0$ (mẫu tiến về $0^+$).\n- Kết quả là số dương chia $0^+ \\implies +\\infty$."
                    },
                    {
                        "title": "Ví dụ 2: Hàm trị tuyệt đối",
                        "problem": "Tính $\\lim_{x \\to 0^+} \\frac{|x|}{x}$ và $\\lim_{x \\to 0^-} \\frac{|x|}{x}$.",
                        "solution": "- Khi $x \\to 0^+$, $x > 0 \\implies |x| = x \\implies$ Giới hạn phải bằng 1.\n- Khi $x \\to 0^-$, $x < 0 \\implies |x| = -x \\implies$ Giới hạn trái bằng -1.\n- (Do 1 khác -1 nên hàm không có giới hạn tại 0)."
                    },
                    {
                        "title": "Ví dụ 3: Định lý tồn tại",
                        "problem": "Nếu giới hạn trái bằng 3, giới hạn phải bằng 3 thì giới hạn của hàm số tại điểm đó bằng bao nhiêu?",
                        "solution": "- Bằng 3 theo đúng định lý tồn tại giới hạn."
                    }
                ],
                "exercise": {
                    "id": "11_16_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu giới hạn trái bằng 5 và giới hạn phải bằng 5 thì giới hạn hàm số bằng:", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 3: BÀI 17 -> BÀI 24)
# ==============================================================================

GRADE_11_DATA.update({
    "Bài 17: Hàm số liên tục": {
        "chapter": "Chương V: Giới hạn. Hàm số liên tục",
        "topics": {
            "Chủ điểm 1: Tính liên tục tại một điểm": {
                "theory": "Hàm số $y = f(x)$ liên tục tại điểm $x_0$ nếu giới hạn của hàm số khi $x \to x_0$ bằng chính giá trị của hàm số tại $x_0$. Nếu giới hạn không tồn tại hoặc không bằng $f(x_0)$ thì hàm số gián đoạn. Các hàm đa thức, phân thức liên tục trên từng khoảng xác định của chúng.",
                "formula": r"\lim_{x \to x_0} f(x) = f(x_0)",
                "trap": "Học sinh thường quên kiểm tra điều kiện $x_0$ có thuộc tập xác định hay không. Nếu không thuộc, kết luận ngay hàm số gián đoạn tại đó mà không cần tính giới hạn.",
                "audio": "Hàm số liên tục tại một điểm khi giới hạn tại điểm đó bằng chính giá trị của hàm số. Đồ thị của hàm số liên tục là một đường liền nét, không bị đứt gãy.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Kiểm tra tính liên tục tại một điểm",
                        "problem": "Xét tính liên tục của hàm số $f(x) = x^2 + 2x$ tại $x_0 = 1$.",
                        "solution": "- Tập xác định $D = \\mathbb{R}$, $1 \\in \\mathbb{R}$.\n- Tính $f(1) = 1^2 + 2(1) = 3$.\n- Tính $\\lim_{x \\to 1} (x^2 + 2x) = 1^2 + 2(1) = 3$.\n- Vì $\\lim_{x \\to 1} f(x) = f(1) = 3$ nên hàm số liên tục tại $x_0 = 1$."
                    },
                    {
                        "title": "Ví dụ 2: Hàm số cho bởi nhiều công thức (Hàm phân nhánh)",
                        "problem": "Cho $f(x) = \\frac{x^2 - 4}{x - 2}$ khi $x \\neq 2$, và $f(x) = 4$ khi $x = 2$. Xét tính liên tục tại $x_0 = 2$.",
                        "solution": "- Tính $f(2) = 4$.\n- Tính giới hạn: $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} \\frac{(x-2)(x+2)}{x-2} = \\lim_{x \\to 2} (x+2) = 4$.\n- Vì $\\lim_{x \\to 2} f(x) = f(2) = 4$, hàm số liên tục tại $x_0 = 2$."
                    },
                    {
                        "title": "Ví dụ 3: Tìm tham số để hàm số liên tục",
                        "problem": "Cho $f(x) = x + 1$ khi $x > 1$ và $f(x) = m$ khi $x \\le 1$. Tìm $m$ để hàm số liên tục tại $x = 1$.",
                        "solution": "- Giới hạn phải: $\\lim_{x \\to 1^+} (x + 1) = 2$.\n- Giới hạn trái: $\\lim_{x \\to 1^-} m = m$.\n- Giá trị tại điểm: $f(1) = m$.\n- Để hàm số liên tục, $\\lim_{x \\to 1^+} f(x) = \\lim_{x \\to 1^-} f(x) = f(1) \\implies m = 2$."
                    }
                ],
                "exercise": {
                    "id": "11_17_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Để hàm số f(x) = 3x khi x > 0 và f(x) = c khi x <= 0 liên tục tại x = 0 thì c bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            },
            "Chủ điểm 2: Định lý giá trị trung gian (Chứng minh có nghiệm)": {
                "theory": "Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \\cdot f(b) < 0$ thì phương trình $f(x) = 0$ có ít nhất một nghiệm nằm trong khoảng $(a; b)$. Ý nghĩa hình học: Đồ thị hàm số đi từ dưới trục hoành lên trên trục hoành (hoặc ngược lại) mà không bị đứt nét thì phải cắt trục hoành.",
                "formula": r"f(a) \cdot f(b) < 0 \implies \exists c \in (a; b): f(c) = 0",
                "trap": "Tuyệt đối không được quên ghi câu 'Hàm số f(x) liên tục trên đoạn [a; b]'. Nếu thiếu điều kiện liên tục, định lý không còn đúng.",
                "audio": "Nếu giá trị hai đầu mút trái dấu nhau và đồ thị đi liền nét thì chắc chắn nó phải cắt trục hoành ít nhất một lần.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh phương trình có nghiệm",
                        "problem": "Chứng minh phương trình $x^3 + 2x - 1 = 0$ có ít nhất 1 nghiệm trong khoảng $(0; 1)$.",
                        "solution": "- Xét hàm số $f(x) = x^3 + 2x - 1$. Đây là hàm đa thức nên liên tục trên $\\mathbb{R}$, suy ra liên tục trên đoạn $[0; 1]$.\n- Ta có $f(0) = 0^3 + 2(0) - 1 = -1$.\n- $f(1) = 1^3 + 2(1) - 1 = 2$.\n- Vì $f(0) \\cdot f(1) = -1 \\cdot 2 = -2 < 0$, phương trình có ít nhất 1 nghiệm thuộc khoảng $(0; 1)$."
                    },
                    {
                        "title": "Ví dụ 2: Chứng minh có nghiệm với hàm lượng giác",
                        "problem": "Chứng minh phương trình $\\cos x = x$ có nghiệm trên khoảng $(0; 1)$.",
                        "solution": "- Chuyển vế xét hàm $f(x) = \\cos x - x$. Hàm liên tục trên $\\mathbb{R}$, do đó liên tục trên $[0; 1]$.\n- $f(0) = \\cos 0 - 0 = 1 > 0$.\n- $f(1) = \\cos 1 - 1$. Vì $\\cos 1 < 1$ nên $f(1) < 0$.\n- Vì $f(0) \\cdot f(1) < 0$, phương trình $\\cos x = x$ có ít nhất 1 nghiệm thuộc $(0; 1)$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định dấu của f(a) và f(b)",
                        "problem": "Hàm số $f(x)$ liên tục trên $[-1; 2]$. Biết $f(-1) = 3$ và phương trình $f(x) = 0$ có nghiệm trong $(-1; 2)$. Có chắc chắn $f(2) < 0$ không?",
                        "solution": "- Không chắc chắn. Định lý phát biểu một chiều: 'Nếu tích âm thì có nghiệm'. Nhưng 'có nghiệm' thì chưa chắc giá trị 2 đầu mút đã trái dấu (đồ thị có thể cắt trục hoành 2 lần rồi quay lên dương)."
                    }
                ],
                "exercise": {
                    "id": "11_17_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Xét hàm f(x) = x^3 - x - 1 trên đoạn [1; 2]. Giá trị f(1).f(2) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "-5", 
                    "options": []
                }
            }
        }
    },
    "Bài 18: Lũy thừa với số mũ thực": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "Chủ điểm 1: Lũy thừa số mũ nguyên và hữu tỉ": {
                "theory": "Tính chất của lũy thừa: Nhân cùng cơ số thì cộng số mũ, chia cùng cơ số thì trừ số mũ. Căn bậc n của $a^m$ được viết dưới dạng lũy thừa số mũ hữu tỉ $\\frac{m}{n}$ (với điều kiện cơ số $a > 0$).",
                "formula": r"a^m \cdot a^n = a^{m+n}; \quad \frac{a^m}{a^n} = a^{m-n}; \quad a^{\frac{m}{n}} = \sqrt[n]{a^m} \ (a > 0)",
                "trap": "Rất nhiều học sinh bỏ qua điều kiện CƠ SỐ DƯƠNG. Công thức $a^{\\frac{m}{n}}$ chỉ có nghĩa khi $a > 0$. Ví dụ $(-2)^{1/2}$ là vô nghĩa, dù $\\sqrt{-2}$ cũng vô nghĩa nhưng bản chất viết dạng số mũ đòi hỏi cơ số dương khắt khe hơn.",
                "audio": "Khi nhân hai lũy thừa cùng cơ số ta cộng các số mũ, khi chia ta trừ các số mũ. Nhớ điều kiện cơ số phải dương khi chuyển từ căn thức sang số mũ hữu tỉ nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính toán cơ bản",
                        "problem": "Rút gọn biểu thức $A = 2^3 \\cdot 2^{-1} \\cdot 2^4$.",
                        "solution": "- Giữ nguyên cơ số 2, cộng các số mũ: $3 + (-1) + 4 = 6$.\n- $A = 2^6 = 64$."
                    },
                    {
                        "title": "Ví dụ 2: Chuyển căn thức sang số mũ",
                        "problem": "Viết biểu thức $P = x \\cdot \\sqrt[3]{x}$ dưới dạng một lũy thừa với số mũ hữu tỉ (với $x > 0$).",
                        "solution": "- Ta có $x = x^1$ và $\\sqrt[3]{x} = x^{\\frac{1}{3}}$.\n- $P = x^1 \\cdot x^{\\frac{1}{3}} = x^{1 + \\frac{1}{3}} = x^{\\frac{4}{3}}$."
                    },
                    {
                        "title": "Ví dụ 3: Lũy thừa của lũy thừa",
                        "problem": "Tính giá trị của biểu thức $Q = (2^3)^2$.",
                        "solution": "- Lũy thừa của lũy thừa thì nhân hai số mũ với nhau: $3 \\cdot 2 = 6$.\n- $Q = 2^6 = 64$."
                    }
                ],
                "exercise": {
                    "id": "11_18_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Rút gọn biểu thức x^2 * x^3 thu được x^c. Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Lũy thừa với số mũ vô tỉ": {
                "theory": "Các tính chất của lũy thừa với số mũ nguyên hay hữu tỉ đều được mở rộng giữ nguyên cho số mũ vô tỉ (số thực bất kỳ), với điều kiện bắt buộc cơ số $a$ phải là số dương.",
                "formula": r"(a^\alpha)^\beta = a^{\alpha\beta}; \quad (ab)^\alpha = a^\alpha b^\alpha \ (a, b > 0)",
                "trap": "Học sinh thường nhầm công thức $(a^\\alpha)^\\beta = a^{\\alpha + \\beta}$. Lũy thừa của lũy thừa phải NHÂN hai số mũ, nhân hai lũy thừa cùng cơ số mới CỘNG số mũ.",
                "audio": "Tính chất của số mũ thực hoàn toàn giống với số mũ nguyên. Lũy thừa của lũy thừa thì ta nhân các số mũ lại với nhau.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính toán với số mũ vô tỉ",
                        "problem": "Tính giá trị của biểu thức $B = (3^{\\sqrt{2}})^{\\sqrt{2}}$.",
                        "solution": "- Áp dụng $(a^\\alpha)^\\beta = a^{\\alpha\\beta}$.\n- $B = 3^{\\sqrt{2} \\cdot \\sqrt{2}} = 3^2 = 9$."
                    },
                    {
                        "title": "Ví dụ 2: Lũy thừa của một tích",
                        "problem": "Rút gọn biểu thức $C = (2^{\\sqrt{3}} \\cdot 5^{\\sqrt{3}})$.",
                        "solution": "- Cùng số mũ, ta gom cơ số: $C = (2 \\cdot 5)^{\\sqrt{3}} = 10^{\\sqrt{3}}$."
                    },
                    {
                        "title": "Ví dụ 3: Chia cùng cơ số",
                        "problem": "Rút gọn $D = \\frac{a^{\\pi + 1}}{a^{\\pi - 1}}$ (với $a > 0$).",
                        "solution": "- Áp dụng phép chia cùng cơ số (trừ số mũ):\n- $D = a^{(\\pi + 1) - (\\pi - 1)} = a^{\\pi + 1 - \\pi + 1} = a^2$."
                    }
                ],
                "exercise": {
                    "id": "11_18_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị của biểu thức (2^(căn 3))^(căn 3) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            }
        }
    },
    "Bài 19: Lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "Chủ điểm 1: Định nghĩa và tính chất cơ bản": {
                "theory": "Lôgarit cơ số $a$ của $b$, ký hiệu $\\log_a b$, là số mũ $c$ sao cho $a^c = b$. Điều kiện xác định rất quan trọng: Cơ số $a$ phải dương và khác 1, biểu thức bên trong $b$ phải dương.",
                "formula": r"\log_a b = c \iff a^c = b \quad (0 < a \neq 1, b > 0)",
                "trap": "Cực kỳ chú ý điều kiện tồn tại của lôgarit. Biểu thức $b$ nằm trong lôgarit bắt buộc phải $> 0$, không được bằng 0 hay âm.",
                "audio": "Lôgarit cơ số a của b chính là số mũ c sao cho a mũ c bằng b. Điều kiện tiên quyết là cơ số dương khác 1 và biểu thức trong lôgarit phải dương.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính lôgarit theo định nghĩa",
                        "problem": "Tính giá trị của $\\log_2 8$.",
                        "solution": "- Ta tìm số mũ $c$ sao cho $2^c = 8$.\n- Vì $2^3 = 8$ nên $\\log_2 8 = 3$."
                    },
                    {
                        "title": "Ví dụ 2: Lôgarit của 1 và chính cơ số",
                        "problem": "Tính $P = \\log_5 1 + \\log_3 3$.",
                        "solution": "- Với cơ số bất kỳ, $\\log_a 1 = 0$ (vì $a^0=1$). Nên $\\log_5 1 = 0$.\n- $\\log_a a = 1$ (vì $a^1=a$). Nên $\\log_3 3 = 1$.\n- Vậy $P = 0 + 1 = 1$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ thức cơ bản",
                        "problem": "Tính giá trị của biểu thức $Q = 4^{\\log_4 5}$.",
                        "solution": "- Áp dụng hệ thức cơ bản: $a^{\\log_a b} = b$.\n- Thay $a=4, b=5 \\implies Q = 5$."
                    }
                ],
                "exercise": {
                    "id": "11_19_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính giá trị của log_3(9).", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Quy tắc tính và công thức đổi cơ số": {
                "theory": "Lôgarit của một tích bằng tổng các lôgarit. Lôgarit của thương bằng hiệu các lôgarit. Đưa số mũ bên trong ra ngoài làm hệ số. Công thức đổi cơ số dùng để chuyển cơ số $a$ sang cơ số $c$ mới.",
                "formula": r"\log_a(xy) = \log_a x + \log_a y; \quad \log_a x^\alpha = \alpha \log_a x; \quad \log_a b = \frac{\log_c b}{\log_c a}",
                "trap": "Nhầm $\\log_a(x+y) = \log_a x + \log_a y$. Lôgarit của một TỔNG không có công thức khai triển.",
                "audio": "Lôgarit của một tích bằng tổng các lôgarit, lôgarit của một thương bằng hiệu các lôgarit. Lưu ý là lôgarit của một tổng thì không tách ra được đâu nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Quy tắc nhân chia",
                        "problem": "Biết $\\log_2 3 = a$ và $\\log_2 5 = b$. Tính $\\log_2 15$ theo $a, b$.",
                        "solution": "- Ta có $15 = 3 \\cdot 5$.\n- Áp dụng log của tích: $\\log_2 15 = \\log_2(3 \\cdot 5) = \\log_2 3 + \\log_2 5$.\n- **Kết luận:** $\\log_2 15 = a + b$."
                    },
                    {
                        "title": "Ví dụ 2: Đưa số mũ ra ngoài",
                        "problem": "Tính giá trị của $\\log_2 16$.",
                        "solution": "- Phân tích $16 = 2^4$.\n- Đưa số mũ ra ngoài: $\\log_2(2^4) = 4\\log_2 2 = 4 \\cdot 1 = 4$."
                    },
                    {
                        "title": "Ví dụ 3: Đổi cơ số nghịch đảo",
                        "problem": "Tính $\\log_3 2 \\cdot \\log_2 3$.",
                        "solution": "- Áp dụng công thức đổi cơ số nghịch đảo: $\\log_a b \\cdot \\log_b a = 1$.\n- **Kết luận:** Kết quả bằng 1."
                    }
                ],
                "exercise": {
                    "id": "11_19_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính giá trị của biểu thức P = log_2(3) * log_3(4).", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 20: Hàm số mũ và hàm số lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "Chủ điểm 1: Hàm số mũ": {
                "theory": "Hàm số mũ $y = a^x$ (với $0 < a \\neq 1$) có tập xác định là $D = \\mathbb{R}$, tập giá trị là $(0; +\\infty)$. Hàm số ĐỒNG BIẾN trên $\\mathbb{R}$ khi $a > 1$, và NGHỊCH BIẾN khi $0 < a < 1$. Đồ thị luôn nằm trên trục hoành.",
                "formula": r"y = a^x > 0 \ (\forall x \in \mathbb{R})",
                "trap": "Tập giá trị của hàm số mũ là các số DƯƠNG. Học sinh thường quên điều kiện này khi đặt ẩn phụ $t = a^x$, dẫn đến không loại các nghiệm $t \\le 0$.",
                "audio": "Hàm số mũ luôn nhận giá trị dương và đồ thị luôn nằm hoàn toàn phía trên trục hoành. Cơ số lớn hơn 1 thì hàm đồng biến, nhỏ hơn 1 thì hàm nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập giá trị",
                        "problem": "Tìm tập giá trị của hàm số $y = 3^x$.",
                        "solution": "- Với mọi giá trị của $x$, lũy thừa $3^x$ luôn lớn hơn 0.\n- Vậy tập giá trị là $T = (0; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 2: Xét tính đơn điệu",
                        "problem": "Hàm số $y = (0.5)^x$ đồng biến hay nghịch biến trên $\\mathbb{R}$?",
                        "solution": "- Cơ số $a = 0.5$. Vì $0 < 0.5 < 1$ nên hàm số mũ nghịch biến trên toàn trục số."
                    },
                    {
                        "title": "Ví dụ 3: Đồ thị hàm số mũ",
                        "problem": "Đồ thị hàm số $y = e^x$ luôn đi qua điểm nào trên trục tung?",
                        "solution": "- Cắt trục tung khi hoành độ $x = 0$.\n- Thay vào: $y = e^0 = 1$.\n- Đồ thị luôn đi qua điểm $(0; 1)$."
                    }
                ],
                "exercise": {
                    "id": "11_20_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đồ thị hàm số y = 5^x đi qua điểm (0; c). Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Hàm số lôgarit": {
                "theory": "Hàm số lôgarit $y = \\log_a x$ (với $0 < a \\neq 1$) có tập xác định là $(0; +\\infty)$, tập giá trị là $\\mathbb{R}$. Hàm số ĐỒNG BIẾN khi $a > 1$, và NGHỊCH BIẾN khi $0 < a < 1$. Đồ thị nằm bên phải trục tung.",
                "formula": r"y = \log_a x \implies \text{TXĐ: } x > 0",
                "trap": "Học sinh thường nhầm tập xác định của hàm logarit sang $\\mathbb{R}$ giống hàm số mũ.",
                "audio": "Hàm lôgarit là ngược của hàm mũ. Nó chỉ xác định với x dương, đồ thị nằm bên phải trục tung. Nhớ đặt điều kiện x dương trước khi khảo sát nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định",
                        "problem": "Tìm tập xác định của hàm số $y = \\log_2(x - 3)$.",
                        "solution": "- Điều kiện xác định: Biểu thức dưới dấu logarit phải dương.\n- Giải: $x - 3 > 0 \\implies x > 3$.\n- **Kết luận:** Tập xác định $D = (3; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính đơn điệu",
                        "problem": "Xét tính đơn điệu của hàm số $y = \\log_{1/3} x$.",
                        "solution": "- Cơ số $a = 1/3$. Vì $0 < 1/3 < 1$ nên hàm số nghịch biến trên tập xác định $(0; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 3: Đồ thị hàm lôgarit",
                        "problem": "Đồ thị hàm số $y = \\log_5 x$ cắt trục hoành tại điểm có hoành độ bằng bao nhiêu?",
                        "solution": "- Cắt trục hoành khi tung độ $y = 0$.\n- $\\log_5 x = 0 \\iff x = 5^0 = 1$.\n- **Kết luận:** Cắt trục hoành tại điểm có hoành độ $x=1$."
                    }
                ],
                "exercise": {
                    "id": "11_20_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hoành độ giao điểm của đồ thị y = log_2(x) với trục hoành là:", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 21: Phương trình, bất phương trình mũ và lôgarit": {
        "chapter": "Chương VI: Hàm số mũ và hàm số lôgarit",
        "topics": {
            "Chủ điểm 1: Giải phương trình mũ và lôgarit cơ bản": {
                "theory": "Phương trình mũ: Đưa về cùng cơ số $a^{f(x)} = a^{g(x)} \\implies f(x) = g(x)$. Hoặc logarit hóa. Phương trình logarit: Phải đặt điều kiện $f(x)>0$, dùng $a$ đội mũ 2 vế $\\log_a f(x) = c \\implies f(x) = a^c$.",
                "formula": r"a^{f(x)} = a^{g(x)} \iff f(x) = g(x); \quad \log_a f(x) = c \implies f(x) = a^c",
                "trap": "Khi giải phương trình logarit bằng phương pháp bỏ $\\log_a$, bắt buộc phải thử lại nghiệm vào đề bài ban đầu nếu trước đó không đặt điều kiện xác định.",
                "audio": "Giải phương trình mũ ta đưa về cùng cơ số. Giải phương trình lôgarit thì bước đầu tiên và quan trọng nhất là phải đặt điều kiện xác định.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phương trình mũ cơ bản",
                        "problem": "Giải phương trình $2^{x-1} = 8$.",
                        "solution": "- Ta viết lại $8 = 2^3$.\n- $2^{x-1} = 2^3 \\implies x - 1 = 3$.\n- Giải ra $x = 4$."
                    },
                    {
                        "title": "Ví dụ 2: Phương trình lôgarit",
                        "problem": "Giải phương trình $\\log_3(2x - 1) = 2$.",
                        "solution": "- Đội mũ 2 vế: $2x - 1 = 3^2 = 9$.\n- $2x = 10 \\implies x = 5$.\n- Thử lại: $2(5)-1=9 > 0$ (thỏa mãn điều kiện). Nghiệm $x=5$."
                    },
                    {
                        "title": "Ví dụ 3: Phương trình logarit cùng cơ số",
                        "problem": "Giải $\\log_2(x) = \\log_2(3x - 4)$.",
                        "solution": "- Điều kiện: $x > 0$ và $3x - 4 > 0 \\implies x > \\frac{4}{3}$.\n- Bỏ log: $x = 3x - 4 \\implies 2x = 4 \\implies x = 2$ (thỏa mãn).\n- Nghiệm $x=2$."
                    }
                ],
                "exercise": {
                    "id": "11_21_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nghiệm của phương trình 3^(x+1) = 27 là x bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Bất phương trình mũ và lôgarit": {
                "theory": "Khi loại bỏ cơ số để giải bất phương trình: NẾU cơ số $a > 1$, GIỮ NGUYÊN chiều bất phương trình. NẾU $0 < a < 1$, ĐỔI CHIỀU bất phương trình.",
                "formula": r"a^{f(x)} > a^{g(x)} \iff f(x) > g(x) \ (\text{nếu } a>1); \quad \log_a f(x) > \log_a g(x) \iff 0 < f(x) < g(x) \ (\text{nếu } 0<a<1)",
                "trap": "Không đổi chiều bất phương trình khi cơ số $a < 1$. Quên đặt điều kiện $f(x)>0$ cho phần nhỏ hơn của bất phương trình logarit.",
                "audio": "Cực kỳ cẩn thận với cơ số khi giải bất phương trình. Cơ số lớn hơn 1 giữ nguyên chiều, nhỏ hơn 1 nhớ quay ngược chiều lại nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bất phương trình mũ cơ số lớn hơn 1",
                        "problem": "Giải bất phương trình $2^{x-1} > 4$.",
                        "solution": "- Viết $4 = 2^2$. Phương trình: $2^{x-1} > 2^2$.\n- Vì cơ số $2 > 1$, giữ nguyên chiều: $x - 1 > 2 \\implies x > 3$.\n- Tập nghiệm $(3; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 2: Bất phương trình mũ cơ số nhỏ hơn 1",
                        "problem": "Giải bất phương trình $(0.5)^x < 0.25$.",
                        "solution": "- Ta viết $0.25 = (0.5)^2$. Phương trình: $(0.5)^x < (0.5)^2$.\n- Vì cơ số $0.5 < 1$, ĐỔI CHIỀU: $x > 2$.\n- Tập nghiệm $(2; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 3: Bất phương trình lôgarit",
                        "problem": "Giải bất phương trình $\\log_2(x-1) \\le 3$.",
                        "solution": "- Điều kiện $x - 1 > 0 \\implies x > 1$.\n- Đội mũ (cơ số $2 > 1$, giữ chiều): $x - 1 \\le 2^3 = 8 \\implies x \\le 9$.\n- Kết hợp điều kiện: $1 < x \\le 9$. Tập nghiệm $(1; 9]$."
                    }
                ],
                "exercise": {
                    "id": "11_21_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tập nghiệm của (1/2)^x < 1/4 là x > c. Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 22: Hai đường thẳng vuông góc": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Góc giữa hai đường thẳng": {
                "theory": "Trong không gian, góc giữa hai đường thẳng $a, b$ chéo nhau là góc giữa hai đường thẳng $a', b'$ cắt nhau và lần lượt song song với $a, b$. Góc giữa hai đường thẳng lớn nhất là $90^\\circ$.",
                "formula": r"0^\circ \le \widehat{(a, b)} \le 90^\circ",
                "trap": "Học sinh áp dụng định lý hàm cosin cho tam giác để tính góc nhưng quên lấy trị tuyệt đối hoặc phần bù nếu góc ra tù. Góc giữa 2 đường thẳng KHÔNG THỂ là góc tù.",
                "audio": "Góc giữa hai đường thẳng trong không gian được đưa về góc giữa hai đường thẳng cắt nhau. Nhớ rằng góc giữa hai đường thẳng không bao giờ là góc tù.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc qua đường song song",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D'. Tính góc giữa AB và A'D'.",
                        "solution": "- Ta có $A'D'$ song song với $AD$.\n- Do đó, góc giữa AB và A'D' chính là góc giữa AB và AD.\n- Vì ABCD là hình vuông nên góc giữa AB và AD là $90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Góc giữa hai đường chéo mặt",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D'. Tính góc giữa AB' và A'C'.",
                        "solution": "- Ta dời A'C' thành AC (do A'C' // AC).\n- Góc cần tính là góc giữa AB' và AC.\n- Tam giác AB'C là tam giác đều (ba cạnh là ba đường chéo của 3 mặt hình vuông bằng nhau).\n- Suy ra góc $\\widehat{B'AC} = 60^\\circ$."
                    },
                    {
                        "title": "Ví dụ 3: Giới hạn của góc",
                        "problem": "Góc giữa hai đường thẳng có thể nhận giá trị $120^\\circ$ không?",
                        "solution": "- Không. Góc giữa hai đường thẳng bị giới hạn từ $0^\\circ$ đến $90^\\circ$. Nếu tính ra góc tù giữa 2 vectơ chỉ phương, ta phải lấy góc bù (180 trừ đi nó) làm góc của 2 đường thẳng."
                    }
                ],
                "exercise": {
                    "id": "11_22_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hình lập phương ABCD.A'B'C'D'. Góc giữa AA' và BC bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            },
            "Chủ điểm 2: Hai đường thẳng vuông góc": {
                "theory": "Hai đường thẳng vuông góc với nhau nếu góc giữa chúng bằng $90^\\circ$. Hệ quả: Tích vô hướng của 2 vectơ chỉ phương tương ứng phải bằng 0. Chú ý: Hai đường thẳng vuông góc có thể cắt nhau hoặc chéo nhau.",
                "formula": r"a \perp b \iff \vec{u_a} \cdot \vec{u_b} = 0",
                "trap": "Học sinh thường mặc định 2 đường thẳng vuông góc thì phải CẮT NHAU như trong hình học phẳng. Điều này SAI trong không gian.",
                "audio": "Trong không gian, hai đường thẳng vuông góc với nhau chưa chắc đã cắt nhau, chúng hoàn toàn có thể chéo nhau đấy nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai đường chéo nhau vuông góc",
                        "problem": "Cho tứ diện đều ABCD cạnh a. Chứng minh AB vuông góc với CD.",
                        "solution": "- Gọi M là trung điểm CD. Xét tam giác ACD và BCD đều cạnh a, ta có AM $\\perp$ CD và BM $\\perp$ CD.\n- Do đó, tích vô hướng $\\vec{AB} \\cdot \\vec{CD} = (\\vec{AM} - \\vec{BM}) \\cdot \\vec{CD} = \\vec{AM}\\cdot\\vec{CD} - \\vec{BM}\\cdot\\vec{CD} = 0 - 0 = 0$.\n- Suy ra AB vuông góc với CD."
                    },
                    {
                        "title": "Ví dụ 2: Dùng tích vô hướng",
                        "problem": "Biết $\\vec{u_1} = (2; -1; 3)$ và $\\vec{u_2} = (-1; m; 1)$ là 2 VTCP của hai đường thẳng vuông góc. Tìm m.",
                        "solution": "- Áp dụng: $2(-1) + (-1)m + 3(1) = 0$.\n- $-2 - m + 3 = 0 \\implies 1 - m = 0 \\implies m = 1$."
                    },
                    {
                        "title": "Ví dụ 3: Khẳng định lý thuyết",
                        "problem": "Nếu a vuông góc với b, a có nhất thiết phải cắt b không? (1: Có, 0: Không)",
                        "solution": "- 0 (Không). Trong không gian, chúng có thể chéo nhau."
                    }
                ],
                "exercise": {
                    "id": "11_22_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu u.v = 0 thì góc giữa hai đường thẳng nhận u, v làm VTCP bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            }
        }
    },
    "Bài 23: Đường thẳng vuông góc với mặt phẳng": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Định lý đường thẳng vuông góc với mặt phẳng": {
                "theory": "Đường thẳng $d$ vuông góc với mặt phẳng $(P)$ nếu $d$ vuông góc với HAI đường thẳng CẮT NHAU nằm trong $(P)$. Khi đó, $d$ sẽ vuông góc với MỌI đường thẳng nằm trong $(P)$.",
                "formula": r"\begin{cases} d \perp a, d \perp b \\ a, b \subset (P), a \cap b = I \end{cases} \implies d \perp (P)",
                "trap": "Nhiều học sinh chỉ chứng minh được d vuông góc với 2 đường thẳng SONG SONG trong mặt phẳng rồi vội kết luận d vuông góc với mặt phẳng.",
                "audio": "Muốn chứng minh đường vuông góc với mặt, em phải chứng minh nó vuông góc với HAI đường thẳng CẮT NHAU nằm trong mặt phẳng đó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh đường vuông góc mặt",
                        "problem": "Cho hình chóp S.ABC có SA vuông góc với mặt đáy (ABC). Tam giác ABC vuông tại B. Chứng minh BC vuông góc với mặt phẳng (SAB).",
                        "solution": "- Ta có $BC \\perp AB$ (giả thiết tam giác ABC vuông tại B).\n- Ta có $SA \\perp (ABC) \\implies SA \\perp BC$.\n- Suy ra $BC$ vuông góc với hai đường cắt nhau là $AB$ và $SA$ cùng nằm trong mặt phẳng $(SAB)$.\n- **Kết luận:** $BC \\perp (SAB)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chất hệ quả",
                        "problem": "Từ Ví dụ 1, có thể suy ra BC vuông góc với đường thẳng SB không?",
                        "solution": "- Vì $BC \\perp (SAB)$ và đường thẳng $SB$ nằm trong mặt phẳng $(SAB)$.\n- Do đó, theo tính chất, $BC$ vuông góc với mọi đường thẳng nằm trong $(SAB)$, nên $BC \\perp SB$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định đường cao khối chóp",
                        "problem": "Cho hình chóp đều S.ABCD. Đường thẳng nối đỉnh S và tâm đáy O có vuông góc với đáy không? (1: Có, 0: Không)",
                        "solution": "- Có. Trong hình chóp đều, hình chiếu của đỉnh S trùng với tâm của đáy. Vậy SO vuông góc với (ABCD)."
                    }
                ],
                "exercise": {
                    "id": "11_23_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Để d vuông góc với (P) thì d cần vuông góc với tối thiểu bao nhiêu đường thẳng cắt nhau trong (P)?", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Mối liên hệ giữa quan hệ song song và vuông góc": {
                "theory": "Tính chất 1: Mặt phẳng nào vuông góc với một trong hai đường thẳng song song thì cũng vuông góc với đường thẳng kia. Tính chất 2: Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì song song với nhau.",
                "formula": r"a \parallel b, (P) \perp a \implies (P) \perp b; \quad a \perp (P), b \perp (P) \implies a \parallel b",
                "trap": "Học sinh thường nhầm: Hai đường thẳng cùng vuông góc với ĐƯỜNG THẲNG thứ 3 thì song song (SAI, trong không gian chúng có thể chéo nhau).",
                "audio": "Nếu một mặt phẳng đã chém thẳng góc xuống một đường thẳng, thì nó cũng sẽ chém vuông góc mọi đường thẳng song song với đường thẳng đó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Sử dụng liên hệ vuông góc - song song",
                        "problem": "Cho hình hộp chữ nhật ABCD.A'B'C'D'. Biết $AA' \\perp (ABCD)$. Chứng minh $CC' \\perp (ABCD)$.",
                        "solution": "- Trong hình hộp chữ nhật, các cạnh bên song song với nhau nên $CC' \\parallel AA'$.\n- Áp dụng tính chất: Vì $AA' \\perp (ABCD)$ nên $CC' \\perp (ABCD)$."
                    },
                    {
                        "title": "Ví dụ 2: Hai đường cùng vuông góc với 1 mặt",
                        "problem": "Cho hình chóp S.ABCD. Có SA và SH (H thuộc đáy) cùng vuông góc với đáy. Vị trí của A và H?",
                        "solution": "- Nếu SA và SH cùng vuông góc đáy thì chúng song song.\n- Nhưng chúng cùng đi qua S, nên SA phải trùng SH. Nghĩa là A trùng H."
                    },
                    {
                        "title": "Ví dụ 3: Sai lầm định lý",
                        "problem": "Hai mặt phẳng phân biệt cùng vuông góc với 1 mặt phẳng thì song song nhau. (1: Đúng, 0: Sai)",
                        "solution": "- 0 (Sai). Giao tuyến của chúng sẽ vuông góc với mặt phẳng kia, chứ 2 mặt phẳng không nhất thiết song song."
                    }
                ],
                "exercise": {
                    "id": "11_23_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hai đường thẳng phân biệt cùng vuông góc với một mặt phẳng thì tạo với nhau góc bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Định lý 3 đường vuông góc": {
                "theory": "Phép chiếu vuông góc là lấy hình chiếu theo phương vuông góc với mặt phẳng. Định lý 3 đường vuông góc: Cho $a$ nằm trong $(P)$, $b$ là đường xiên cắt $(P)$ tại $O$, $b'$ là hình chiếu vuông góc của $b$ trên $(P)$. Khi đó, $a$ vuông góc với $b$ khi và chỉ khi $a$ vuông góc với hình chiếu $b'$.",
                "formula": r"a \subset (P), \ b' \text{ là hình chiếu của } b \implies (a \perp b \iff a \perp b')",
                "trap": "Cực kỳ chú ý điều kiện: Đường thẳng $a$ BẮT BUỘC phải nằm hoàn toàn trong mặt phẳng $(P)$ thì định lý mới đúng.",
                "audio": "Định lý 3 đường vuông góc rất mạnh. Đường thẳng nằm trong mặt phẳng sẽ vuông góc với đường xiên khi và chỉ khi nó vuông góc với hình chiếu của đường xiên đó.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Ứng dụng định lý 3 đường vuông góc",
                        "problem": "Cho tứ diện OABC có OA vuông góc với (OBC). Vẽ OH vuông góc với BC. Chứng minh AH vuông góc với BC.",
                        "solution": "- Đường thẳng BC nằm trong mặt phẳng (OBC).\n- AH là đường xiên, OH là hình chiếu vuông góc của AH lên mặt phẳng (OBC) (do OA vuông góc đáy).\n- Vì BC $\\perp$ OH (hình chiếu) nên theo Định lý 3 đường vuông góc, suy ra BC $\\perp$ AH (đường xiên)."
                    },
                    {
                        "title": "Ví dụ 2: Tìm hình chiếu của đường xiên",
                        "problem": "Cho hình chóp S.ABCD có SA vuông góc đáy (ABCD). Hình chiếu vuông góc của đoạn SB lên (ABCD) là đoạn thẳng nào?",
                        "solution": "- Hình chiếu của điểm B lên (ABCD) chính là B (vì B nằm trên đáy).\n- Hình chiếu của S lên (ABCD) là A (do SA vuông góc đáy).\n- Nối lại, hình chiếu của đoạn thẳng SB là đoạn thẳng AB."
                    },
                    {
                        "title": "Ví dụ 3: Hình chiếu của đoạn thẳng vuông góc",
                        "problem": "Đoạn thẳng song song với mặt phẳng chiếu thì hình chiếu của nó có độ dài như thế nào so với ban đầu?",
                        "solution": "- Nó là hình chữ nhật nên độ dài hình chiếu bằng đúng độ dài ban đầu."
                    }
                ],
                "exercise": {
                    "id": "11_24_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho S.ABC có SA vuông góc đáy. Hình chiếu của SC lên (ABC) là cạnh nào? (Nhập tên cạnh, VD: AB)", 
                    "type": "STRING", 
                    "target": "AC", 
                    "options": []
                }
            },
            "Chủ điểm 2: Góc giữa đường thẳng và mặt phẳng": {
                "theory": "Nếu $d \\perp (P)$ thì góc bằng $90^\\circ$. Nếu $d$ không vuông góc $(P)$ và cắt $(P)$ tại $O$, góc giữa $d$ và $(P)$ là góc nhọn giữa $d$ và hình chiếu $d'$ của nó trên mặt phẳng $(P)$.",
                "formula": r"\widehat{(d, (P))} = \widehat{(d, d')} \quad (0^\circ \le \alpha \le 90^\circ)",
                "trap": "Sai lầm kinh điển: Học sinh xác định sai hình chiếu của đỉnh dẫn đến kẻ sai đoạn hình chiếu $d'$. Phải đi tìm đúng CHÂN đường vuông góc hạ từ đỉnh xuống mặt phẳng.",
                "audio": "Góc giữa đường thẳng và mặt phẳng chính là góc giữa đường thẳng đó và cái bóng hình chiếu vuông góc của nó trên mặt phẳng.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc cơ bản",
                        "problem": "Cho hình chóp S.ABC có SA vuông góc mặt đáy (ABC), $SA = a$ và $AB = a$. Tính góc giữa SB và mặt phẳng (ABC).",
                        "solution": "- Giao điểm của SB và (ABC) là B.\n- Hình chiếu vuông góc của S lên (ABC) là A (do SA vuông góc đáy).\n- Hình chiếu của SB là AB.\n- Góc giữa SB và (ABC) là góc $\\widehat{SBA}$.\n- Xét tam giác SAB vuông tại A, $\\tan \\widehat{SBA} = \\frac{SA}{AB} = \\frac{a}{a} = 1 \\implies \\widehat{SBA} = 45^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Tính góc với mặt bên",
                        "problem": "Vẫn dùng khối chóp VD1 (SA vuông góc đáy). Hỏi hình chiếu của AC lên mặt phẳng (SAB) là đường nào?",
                        "solution": "- Giả sử tam giác ABC vuông tại A. CA vuông góc với AB và SA, nên CA vuông góc (SAB).\n- Hình chiếu của C lên (SAB) là A. Hình chiếu của A là chính nó.\n- Vậy góc giữa AC và (SAB) bằng $90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 3: Góc của đường chéo hình lập phương",
                        "problem": "Tính tan của góc tạo bởi đường chéo AC' của hình lập phương ABCD.A'B'C'D' với mặt đáy (ABCD).",
                        "solution": "- Giao điểm là A. Hình chiếu của C' lên (ABCD) là C.\n- Góc cần tìm là $\\widehat{C'AC}$.\n- Tam giác C'CA vuông tại C. Nếu cạnh lập phương là $a$, thì $CC' = a$, $AC = a\\sqrt{2}$.\n- $\\tan \\widehat{C'AC} = \\frac{CC'}{AC} = \\frac{a}{a\\sqrt{2}} = \\frac{1}{\\sqrt{2}}$."
                    }
                ],
                "exercise": {
                    "id": "11_24_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho S.ABC có SA vuông góc đáy, tam giác SAB vuông cân tại A. Góc giữa SB và (ABC) bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "45", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE11.PY - HỌC LIỆU TOÁN 11 KẾT NỐI TRI THỨC (PHẦN 4: BÀI 25 -> BÀI 33)
# ==============================================================================

GRADE_11_DATA.update({
    "Bài 25: Hai mặt phẳng vuông góc": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Định lý và Tính chất hai mặt phẳng vuông góc": {
                "theory": "Hai mặt phẳng vuông góc với nhau nếu mặt phẳng này chứa MỘT đường thẳng vuông góc với mặt phẳng kia. Tính chất quan trọng: Nếu hai mặt phẳng vuông góc với nhau thì bất cứ đường thẳng nào nằm trong mặt phẳng này vuông góc với GIAO TUYẾN thì sẽ vuông góc với mặt phẳng kia.",
                "formula": r"\begin{cases} (P) \supset a \\ a \perp (Q) \end{cases} \implies (P) \perp (Q)",
                "trap": "Học sinh thường cho rằng hai mặt phẳng vuông góc thì BẤT KỲ đường nào nằm trong mặt này cũng vuông góc với mặt kia. Nhớ là nó phải vuông góc với GIAO TUYẾN mới được nhé.",
                "audio": "Để chứng minh hai mặt phẳng vuông góc, em chỉ cần tìm trong mặt phẳng này một đường thẳng chém thẳng góc xuống mặt phẳng kia là đủ.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh hai mặt phẳng vuông góc",
                        "problem": "Cho hình chóp S.ABC có SA vuông góc với đáy (ABC). Tam giác ABC vuông tại B. Chứng minh (SAB) vuông góc với (SBC).",
                        "solution": "- Ta có $BC \\perp AB$ (do $\\Delta ABC$ vuông tại B).\n- Lại có $BC \\perp SA$ (do $SA \\perp (ABC)$).\n- Suy ra $BC \\perp (SAB)$.\n- Vì $BC$ nằm trong mặt phẳng $(SBC)$ nên $(SBC) \\perp (SAB)$."
                    },
                    {
                        "title": "Ví dụ 2: Dùng tính chất giao tuyến",
                        "problem": "Hai mặt phẳng (P) và (Q) vuông góc với nhau theo giao tuyến d. Một đường thẳng a nằm trong (P) và vuông góc với d. Khẳng định nào sau đây đúng?",
                        "solution": "- Theo tính chất của hai mặt phẳng vuông góc: Đường thẳng nằm trong mặt phẳng này và vuông góc với giao tuyến thì sẽ vuông góc với mặt phẳng kia.\n- **Kết luận:** Đường thẳng $a \\perp (Q)$."
                    },
                    {
                        "title": "Ví dụ 3: Mặt phẳng chéo hình lập phương",
                        "problem": "Cho hình lập phương ABCD.A'B'C'D'. Mặt phẳng (ACC'A') có vuông góc với mặt phẳng (ABCD) không?",
                        "solution": "- Ta có cạnh bên $AA' \\perp (ABCD)$ (tính chất hình lập phương).\n- Vì mặt phẳng $(ACC'A')$ chứa đường thẳng $AA'$ nên $(ACC'A') \\perp (ABCD)$."
                    }
                ],
                "exercise": {
                    "id": "11_25_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hình chóp S.ABCD đáy hình vuông, SA vuông góc đáy. Mặt phẳng (SAB) và mặt phẳng (SAD) tạo với nhau góc bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            }
        }
    },
    "Bài 26: Khoảng cách trong không gian": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Khoảng cách từ một điểm đến mặt phẳng": {
                "theory": "Khoảng cách từ điểm M đến mặt phẳng (P) là độ dài đoạn vuông góc hạ từ M xuống (P). Trong thực hành, ta thường dùng phương pháp CHUYỂN ĐIỂM (dời điểm): Nối điểm cần tính (A) với điểm chân đường cao (H) cắt mặt phẳng tại giao điểm (I). Tỉ số khoảng cách bằng tỉ số khoảng cách từ điểm đến giao điểm.",
                "formula": r"\frac{d(A, (P))}{d(H, (P))} = \frac{IA}{IH} \quad \text{(Nếu } AH \cap (P) = I)",
                "trap": "Học sinh thường kẻ bừa một đường vuông góc vào một cạnh bất kỳ trên mặt phẳng rồi ngộ nhận đó là khoảng cách. Phải hạ vuông góc theo đúng quy trình 2 bước (kẻ vào giao tuyến đáy, rồi kẻ lên đỉnh).",
                "audio": "Tính khoảng cách từ chân đường cao là dễ nhất. Nếu đề hỏi điểm khác, em hãy tìm cách dời điểm đó về chân đường cao theo tỉ lệ nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Khoảng cách từ chân đường cao",
                        "problem": "Cho hình chóp S.ABC có SA vuông góc đáy, tam giác ABC vuông tại B. Lập công thức tính khoảng cách từ A đến (SBC).",
                        "solution": "- SA là đường cao, A là chân đường cao.\n- Ta kẻ $AH \\perp SB$. Vì $BC \\perp (SAB)$ nên $BC \\perp AH$.\n- Vậy $AH \\perp (SBC) \\implies d(A, (SBC)) = AH$.\n- Áp dụng hệ thức lượng: $\\frac{1}{AH^2} = \\frac{1}{SA^2} + \\frac{1}{AB^2}$."
                    },
                    {
                        "title": "Ví dụ 2: Dời điểm song song",
                        "problem": "Hình chóp S.ABCD có SA vuông góc đáy. Tính tỉ số khoảng cách từ D đến (SBC) và từ A đến (SBC).",
                        "solution": "- Ta có $AD \\parallel BC \\implies AD \\parallel (SBC)$.\n- Vì đường thẳng chứa 2 điểm song song với mặt phẳng nên khoảng cách từ chúng đến mặt phẳng là bằng nhau.\n- **Kết luận:** Tỉ số bằng 1."
                    },
                    {
                        "title": "Ví dụ 3: Dời điểm cắt nhau (Tỉ lệ)",
                        "problem": "Hình chóp S.ABCD tâm O. SA vuông góc đáy. C là điểm đối xứng của A qua O. Tính tỉ số d(C, (SBD)) / d(A, (SBD)).",
                        "solution": "- Đường nối AC cắt (SBD) tại O.\n- Tỉ số khoảng cách bằng $\\frac{CO}{AO}$.\n- Vì O là trung điểm AC nên $\\frac{CO}{AO} = 1$."
                    }
                ],
                "exercise": {
                    "id": "11_26_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu đoạn thẳng nối điểm M và N song song với mặt phẳng (P). Tỉ số d(M, (P)) / d(N, (P)) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Khoảng cách giữa hai đường thẳng chéo nhau": {
                "theory": "Cách 1: Dựng đường vuông góc chung. Cách 2 (Phổ biến nhất): Dựng mặt phẳng (P) chứa đường thẳng này và song song với đường thẳng kia. Khi đó khoảng cách giữa 2 đường thẳng bằng khoảng cách từ đường thẳng đó đến mặt phẳng (P).",
                "formula": r"d(a, b) = d(a, (P)) \text{ với } b \subset (P) \text{ và } a \parallel (P)",
                "trap": "Không nhận diện được hai đường thẳng có vuông góc với nhau hay không. Nếu chéo nhau và vuông góc, đường vuông góc chung rất dễ tìm (thường song song với 1 cạnh đáy).",
                "audio": "Để tính khoảng cách hai đường chéo nhau, hãy dựng một bức tường mặt phẳng chứa đường này và song song đường kia, rồi quy về khoảng cách từ một điểm.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Hai đường chéo nhau vuông góc",
                        "problem": "Cho tứ diện đều ABCD cạnh a. Gọi M, N là trung điểm AB và CD. Xác định khoảng cách giữa AB và CD.",
                        "solution": "- Tam giác ACD và BCD đều $\\implies AM \\perp CD$ và $BM \\perp CD \\implies CD \\perp (AMB)$.\n- Suy ra $CD \\perp MN$. Tương tự $AB \\perp MN$.\n- MN là đoạn vuông góc chung. $d(AB, CD) = MN$."
                    },
                    {
                        "title": "Ví dụ 2: Dùng mặt phẳng song song",
                        "problem": "Hình chóp S.ABCD đáy hình vuông cạnh a, SA vuông góc đáy. Tính $d(SA, BD)$.",
                        "solution": "- Mặt phẳng (SBD) chứa BD, nhưng SA cắt (SBD) tại S nên không dùng được.\n- Xét (SAB) chứa SA, không song song BD.\n- Dựng đường vuông góc chung: Từ A kẻ $AO \\perp BD$ (O là tâm đáy). Vì $SA \\perp (ABCD) \\implies SA \\perp AO$.\n- Vậy AO là đoạn vuông góc chung. $d(SA, BD) = AO = \\frac{a\\sqrt{2}}{2}$."
                    },
                    {
                        "title": "Ví dụ 3: Lập luận hình học",
                        "problem": "Khoảng cách giữa hai đường thẳng chéo nhau có phải là khoảng cách ngắn nhất giữa hai điểm bất kỳ trên hai đường thẳng đó không?",
                        "solution": "- Đúng. Đoạn vuông góc chung chính là đoạn thẳng có độ dài ngắn nhất nối 2 điểm nằm trên 2 đường chéo nhau."
                    }
                ],
                "exercise": {
                    "id": "11_26_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đoạn vuông góc chung của 2 đường thẳng chéo nhau tạo với mỗi đường thẳng một góc bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            }
        }
    },
    "Bài 27: Thể tích": {
        "chapter": "Chương VII: Quan hệ vuông góc trong không gian",
        "topics": {
            "Chủ điểm 1: Thể tích khối chóp và khối lăng trụ": {
                "theory": "Thể tích khối lăng trụ (đáy và nắp song song bằng nhau) bằng diện tích đáy nhân chiều cao. Thể tích khối chóp (1 đỉnh nhọn) bằng 1/3 diện tích đáy nhân chiều cao. Tỉ số thể tích khối chóp tam giác (Simpson) được tính bằng tích các tỉ số cạnh bên.",
                "formula": r"V_{langtru} = S_{day} \cdot h; \quad V_{chop} = \frac{1}{3} S_{day} \cdot h; \quad \frac{V_{S.A'B'C'}}{V_{S.ABC}} = \frac{SA'}{SA} \cdot \frac{SB'}{SB} \cdot \frac{SC'}{SC}",
                "trap": "Học sinh thường quên nhân hệ số 1/3 khi tính thể tích khối chóp. Tỉ số thể tích Simpson CHỈ áp dụng được cho chóp tam giác (đáy là tam giác).",
                "audio": "Nhớ kỹ nhé: Lăng trụ thì đáy nhân cao, còn khối chóp mũi nhọn thì bắt buộc phải có hệ số một phần ba ở đằng trước.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Thể tích lăng trụ",
                        "problem": "Khối lăng trụ tam giác đều có cạnh đáy bằng $a$, chiều cao $h = 2a$. Tính thể tích.",
                        "solution": "- Diện tích đáy (tam giác đều): $S = \\frac{a^2\\sqrt{3}}{4}$.\n- Thể tích lăng trụ: $V = S \\cdot h = \\frac{a^2\\sqrt{3}}{4} \\cdot 2a = \\frac{a^3\\sqrt{3}}{2}$."
                    },
                    {
                        "title": "Ví dụ 2: Thể tích khối chóp",
                        "problem": "Khối chóp S.ABCD có đáy hình vuông cạnh $a$, SA vuông góc đáy và $SA = 3a$. Tính thể tích.",
                        "solution": "- Diện tích đáy (hình vuông): $S = a^2$.\n- Chiều cao $h = SA = 3a$.\n- Thể tích: $V = \\frac{1}{3} S \\cdot h = \\frac{1}{3} \\cdot a^2 \\cdot 3a = a^3$."
                    },
                    {
                        "title": "Ví dụ 3: Tỉ số thể tích Simpson",
                        "problem": "Khối chóp S.ABC có V = 12. Gọi M, N, P là trung điểm của SA, SB, SC. Tính thể tích khối S.MNP.",
                        "solution": "- Áp dụng Simpson: $\\frac{V_{S.MNP}}{V_{S.ABC}} = \\frac{1}{2} \\cdot \\frac{1}{2} \\cdot \\frac{1}{2} = \\frac{1}{8}$.\n- $V_{S.MNP} = 12 \\cdot \\frac{1}{8} = 1.5$."
                    }
                ],
                "exercise": {
                    "id": "11_27_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Khối chóp tứ giác đều có diện tích đáy bằng 6, chiều cao bằng 4. Thể tích bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            }
        }
    },
    "Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "Chủ điểm 1: Biến cố hợp và Biến cố giao": {
                "theory": "Biến cố hợp $A \\cup B$ là biến cố xảy ra khi có ÍT NHẤT một trong hai biến cố A hoặc B xảy ra (A xảy ra, B xảy ra, hoặc cả 2 cùng xảy ra). Biến cố giao $AB$ (hoặc $A \\cap B$) là biến cố xảy ra khi CẢ HAI biến cố A và B ĐỒNG THỜI xảy ra.",
                "formula": r"A \cup B \iff \text{A hoặc B}; \quad AB \iff \text{A và B đồng thời}",
                "trap": "Rất nhiều bạn nhầm chữ 'hoặc' (biến cố hợp) mang nghĩa loại trừ nhau. Trong Toán học, chữ 'hoặc' bao hàm cả việc 2 biến cố cùng xảy ra.",
                "audio": "Hợp là phép lấy tất cả, chỉ cần một cái xảy ra là được. Giao là phần chung, bắt buộc cả hai điều kiện cùng phải xảy ra đồng thời.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện biến cố hợp",
                        "problem": "Gieo con xúc xắc. A: 'Số chấm chẵn', B: 'Số chấm lớn hơn 4'. C = $A \\cup B$ là tập hợp các số nào?",
                        "solution": "- Tập A = {2, 4, 6}. Tập B = {5, 6}.\n- Tập C là hợp của A và B: C = {2, 4, 5, 6}."
                    },
                    {
                        "title": "Ví dụ 2: Nhận diện biến cố giao",
                        "problem": "Gieo con xúc xắc. Tìm biến cố giao $D = AB$ từ ví dụ 1.",
                        "solution": "- Phần tử chung của A và B là mặt có 6 chấm.\n- Tập D = {6}."
                    },
                    {
                        "title": "Ví dụ 3: Biến cố xung khắc",
                        "problem": "A: 'Xúc xắc ra mặt 1', B: 'Xúc xắc ra mặt chẵn'. Biến cố giao AB có xảy ra không?",
                        "solution": "- Không thể vừa ra mặt 1 (lẻ) vừa ra mặt chẵn được.\n- Biến cố AB là biến cố không thể (rỗng). A và B xung khắc."
                    }
                ],
                "exercise": {
                    "id": "11_28_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hai biến cố xung khắc thì biến cố giao của chúng có số phần tử bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            },
            "Chủ điểm 2: Hai biến cố độc lập": {
                "theory": "Hai biến cố A và B được gọi là độc lập nếu việc xảy ra (hay không xảy ra) của biến cố này không làm ảnh hưởng đến xác suất xảy ra của biến cố kia.",
                "formula": r"A, B \text{ độc lập} \implies P(AB) = P(A) \cdot P(B)",
                "trap": "Rất hay nhầm lẫn giữa 'Độc lập' và 'Xung khắc'. Xung khắc là 'có A thì không có B', như vậy chúng có ảnh hưởng cực mạnh đến nhau (KHÔNG độc lập). Độc lập là hai người làm hai việc khác nhau.",
                "audio": "Xung khắc là sống chết có nhau, có mày thì không có tao. Độc lập là việc ai người nấy làm, không liên quan đến nhau.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận dạng tính độc lập",
                        "problem": "Người 1 bắn bia A, người 2 bắn bia B. Việc trúng đích của hai người là biến cố gì?",
                        "solution": "- Việc người 1 bắn trúng không làm người 2 bắn giỏi hơn hay kém đi.\n- Hai biến cố này là hai biến cố độc lập."
                    },
                    {
                        "title": "Ví dụ 2: Công thức thử độc lập",
                        "problem": "Biết $P(A) = 0.5, P(B) = 0.4$ và $P(AB) = 0.2$. A và B có độc lập không? (1: Có, 0: Không)",
                        "solution": "- Ta xét tích: $P(A) \\cdot P(B) = 0.5 \\cdot 0.4 = 0.2$.\n- Vì $P(AB) = P(A)P(B) = 0.2$ nên A và B là hai biến cố độc lập. Trả lời: 1."
                    },
                    {
                        "title": "Ví dụ 3: Tính chất đối của độc lập",
                        "problem": "Nếu A và B độc lập thì $\\overline{A}$ và B có độc lập không?",
                        "solution": "- Có. Nếu A và B độc lập thì các cặp ($\\overline{A}, B$), ($A, \\overline{B}$), ($\\overline{A}, \\overline{B}$) cũng độc lập với nhau."
                    }
                ],
                "exercise": {
                    "id": "11_28_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "P(A)=0.5, P(B)=0.6. Biết A, B độc lập. Giá trị của P(A.B) bằng:", 
                    "type": "NUMERIC", 
                    "target": "0.3", 
                    "options": []
                }
            }
        }
    },
    "Bài 29: Công thức cộng xác suất": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "Chủ điểm 1: Quy tắc cộng chung và Biến cố xung khắc": {
                "theory": "Xác suất của biến cố hợp $A \\cup B$ luôn bằng tổng xác suất của A và B trừ đi xác suất của biến cố giao (phần bị tính lặp 2 lần). Nếu A và B xung khắc (giao bằng rỗng), phần trừ sẽ bằng 0.",
                "formula": r"P(A \cup B) = P(A) + P(B) - P(AB); \quad P(A \cup B) = P(A) + P(B) \ (\text{Nếu xung khắc})",
                "trap": "Cứ thấy tính xác suất 'A hoặc B' là học sinh hay lấy $P(A)+P(B)$ mà quên đi phần giao, dẫn đến kết quả đôi khi lớn hơn 1 (vô lý).",
                "audio": "Khi tính xác suất hợp, đừng quên trừ đi xác suất giao của hai biến cố để bù trừ phần đã bị đếm lặp hai lần nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất hợp",
                        "problem": "Biết $P(A) = 0.4, P(B) = 0.5$ và $P(AB) = 0.1$. Tính xác suất của $A \\cup B$.",
                        "solution": "- Áp dụng công thức cộng: $P(A \\cup B) = P(A) + P(B) - P(AB)$.\n- Thay số: $P(A \\cup B) = 0.4 + 0.5 - 0.1 = 0.8$."
                    },
                    {
                        "title": "Ví dụ 2: Hai biến cố xung khắc",
                        "problem": "Trong hộp có 3 bi đỏ, 2 bi xanh. Xác suất rút được bi đỏ hoặc xanh (rút 1 viên) là bao nhiêu?",
                        "solution": "- Biến cố lấy bi đỏ và lấy bi xanh là xung khắc (rút 1 viên không thể ra 2 màu).\n- $P(D \\cup X) = P(D) + P(X) = 3/5 + 2/5 = 1$."
                    },
                    {
                        "title": "Ví dụ 3: Rút bài tú lơ khơ",
                        "problem": "Rút 1 lá từ bộ 52 lá. Tính XS rút được lá Át hoặc lá Cơ.",
                        "solution": "- $P(At) = 4/52$. $P(Co) = 13/52$.\n- Lá vừa Át vừa Cơ (Át cơ): $P(At \cap Co) = 1/52$.\n- $P = 4/52 + 13/52 - 1/52 = 16/52 = 4/13$."
                    }
                ],
                "exercise": {
                    "id": "11_29_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "P(A) = 0.6, P(B) = 0.5, P(A giao B) = 0.2. P(A hợp B) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0.9", 
                    "options": []
                }
            }
        }
    },
    "Bài 30: Công thức nhân xác suất cho hai biến cố độc lập": {
        "chapter": "Chương VIII: Các quy tắc tính xác suất",
        "topics": {
            "Chủ điểm 1: Quy tắc nhân và Xác suất có ít nhất 1 biến cố xảy ra": {
                "theory": "Nếu hai biến cố A và B độc lập, xác suất của biến cố giao (A và B cùng xảy ra) bằng tích hai xác suất thành phần. Bài toán 'Tính xác suất để có ÍT NHẤT một người bắn trúng' thường được giải nhanh nhất bằng cách dùng BIẾN CỐ ĐỐI (1 trừ đi xác suất cả hai đều trượt).",
                "formula": r"P(AB) = P(A) \cdot P(B); \quad P(\text{Ít nhất 1 xảy ra}) = 1 - P(\overline{A}) \cdot P(\overline{B})",
                "trap": "Gặp bài toán 'ít nhất', nếu chia trường hợp đếm xuôi sẽ rất dài và dễ thiếu. Cách tốt nhất luôn là dùng phần bù (số 1 trừ đi không có ai).",
                "audio": "Đối với các bài toán độc lập như cùng thi đậu, cùng bắn trúng bia. Nếu đề hỏi 'có ít nhất một', em hãy tính xác suất không có cái nào rồi lấy 1 trừ đi nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác suất đồng thời",
                        "problem": "Xác suất An đỗ ĐH là 0.8, Bình đỗ là 0.7. Tính XS cả 2 cùng đỗ.",
                        "solution": "- Việc An đỗ và Bình đỗ là độc lập.\n- $P = 0.8 \\cdot 0.7 = 0.56$."
                    },
                    {
                        "title": "Ví dụ 2: Xác suất có ít nhất một",
                        "problem": "Từ dữ liệu trên, tính XS có ít nhất 1 bạn đỗ ĐH.",
                        "solution": "- Xác suất An trượt là $1 - 0.8 = 0.2$. Bình trượt là $1 - 0.7 = 0.3$.\n- Xác suất cả 2 bạn cùng trượt là $0.2 \\cdot 0.3 = 0.06$.\n- Xác suất có ít nhất 1 bạn đỗ: $1 - 0.06 = 0.94$."
                    },
                    {
                        "title": "Ví dụ 3: Chỉ có một người trúng đích",
                        "problem": "Hai người bắn súng độc lập, P(trúng) lần lượt là 0.6 và 0.8. Tính XS chỉ có ĐÚNG 1 người trúng.",
                        "solution": "- Trường hợp 1: Người 1 trúng, người 2 trượt: $0.6 \\cdot (1 - 0.8) = 0.12$.\n- Trường hợp 2: Người 1 trượt, người 2 trúng: $(1 - 0.6) \\cdot 0.8 = 0.32$.\n- Cộng lại: $0.12 + 0.32 = 0.44$."
                    }
                ],
                "exercise": {
                    "id": "11_30_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "A, B độc lập. P(A)=0.5, P(B)=0.5. Xác suất để có ít nhất 1 biến cố xảy ra bằng:", 
                    "type": "NUMERIC", 
                    "target": "0.75", 
                    "options": []
                }
            }
        }
    },
    "Bài 31: Định nghĩa và ý nghĩa của đạo hàm": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "Chủ điểm 1: Định nghĩa đạo hàm tại một điểm": {
                "theory": "Đạo hàm của hàm số $y=f(x)$ tại $x_0$ là giới hạn (nếu có) của tỉ số giữa số gia của hàm số $\\Delta y$ và số gia của đối số $\\Delta x$ khi $\\Delta x \\to 0$.",
                "formula": r"f'(x_0) = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}",
                "trap": "Hàm số muốn có đạo hàm tại $x_0$ thì phải LÊN TỤC tại $x_0$. Nhưng chiều ngược lại thì sai (Liên tục chưa chắc đã có đạo hàm, ví dụ hàm $y=|x|$ tại điểm gãy $x=0$).",
                "audio": "Đạo hàm bản chất là tốc độ thay đổi tức thời của hàm số. Đồ thị bị đứt đứt gãy gãy, hoặc có điểm nhọn thì sẽ không có đạo hàm tại đó.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính đạo hàm bằng định nghĩa",
                        "problem": "Dùng định nghĩa tính đạo hàm của $f(x) = x^2$ tại $x_0 = 1$.",
                        "solution": "- Xét giới hạn: $\\lim_{x \\to 1} \\frac{x^2 - 1^2}{x - 1} = \\lim_{x \\to 1} \\frac{(x-1)(x+1)}{x-1} = \\lim_{x \\to 1} (x+1) = 2$.\n- Vậy $f'(1) = 2$."
                    },
                    {
                        "title": "Ví dụ 2: Nhận diện điểm không có đạo hàm",
                        "problem": "Hàm số $y = |x|$ có đạo hàm tại $x=0$ không?",
                        "solution": "- $\\lim_{x \\to 0^+} \\frac{|x|-0}{x-0} = 1$.\n- $\\lim_{x \\to 0^-} \\frac{|x|-0}{x-0} = -1$.\n- Giới hạn trái khác phải $\\implies$ Không có đạo hàm tại x=0."
                    },
                    {
                        "title": "Ví dụ 3: Đạo hàm hàm hằng",
                        "problem": "Tính đạo hàm của hàm $f(x) = 5$ tại $x = 100$.",
                        "solution": "- Theo định nghĩa, $\\Delta y = f(x) - f(x_0) = 5 - 5 = 0$.\n- Giới hạn $\\lim \\frac{0}{\\Delta x} = 0$. Vậy đạo hàm bằng 0."
                    }
                ],
                "exercise": {
                    "id": "11_31_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị đạo hàm của hàm số f(x) = 3x tại x_0 = 5 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            },
            "Chủ điểm 2: Ý nghĩa hình học và vật lý của đạo hàm": {
                "theory": "Ý nghĩa hình học: Đạo hàm $f'(x_0)$ là hệ số góc của tiếp tuyến của đồ thị $(C)$ tại điểm có hoành độ $x_0$. Ý nghĩa vật lý: Đạo hàm của phương trình chuyển động $s(t)$ là vận tốc tức thời $v(t)$.",
                "formula": r"y - y_0 = f'(x_0)(x - x_0) \quad \text{(Phương trình tiếp tuyến)}; \quad v(t) = s'(t)",
                "trap": "Viết phương trình tiếp tuyến, học sinh thường lấy nhầm điểm đi qua không nằm trên đồ thị. Phải xác định đủ 3 yếu tố: $x_0, y_0, f'(x_0)$.",
                "audio": "Hệ số góc của tiếp tuyến chính là giá trị đạo hàm tại tiếp điểm. Vận tốc tức thời trong vật lý chính là đạo hàm của quãng đường theo thời gian.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết phương trình tiếp tuyến",
                        "problem": "Viết PT tiếp tuyến của $(C): y = x^2$ tại điểm $M(2; 4)$.",
                        "solution": "- Đạo hàm $y' = 2x$. Hệ số góc tại $x_0 = 2$ là $k = y'(2) = 4$.\n- Phương trình tiếp tuyến: $y - 4 = 4(x - 2) \\iff y = 4x - 4$."
                    },
                    {
                        "title": "Ví dụ 2: Tính vận tốc tức thời",
                        "problem": "Phương trình rơi tự do $s(t) = \\frac{1}{2}gt^2$. Tính vận tốc tại thời điểm $t = 3$ (lấy $g=10$).",
                        "solution": "- Phương trình chuyển động: $s(t) = 5t^2$.\n- Hàm vận tốc: $v(t) = s'(t) = 10t$.\n- Vận tốc tại $t=3$ là $v(3) = 10 \\cdot 3 = 30$ (m/s)."
                    },
                    {
                        "title": "Ví dụ 3: Tiếp tuyến song song với đường thẳng",
                        "problem": "Tiếp tuyến của $y = x^2$ song song với $y = 4x + 1$ thì tiếp điểm có hoành độ là bao nhiêu?",
                        "solution": "- Hệ số góc của tiếp tuyến phải bằng hệ số góc đường thẳng: $k = 4$.\n- Ta giải $y' = 4 \\iff 2x = 4 \\implies x = 2$."
                    }
                ],
                "exercise": {
                    "id": "11_31_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tiếp tuyến của y = x^3 tại điểm có hoành độ x = 1 có hệ số góc bằng:", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 32: Các quy tắc tính đạo hàm": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "Chủ điểm 1: Đạo hàm tổng, hiệu, tích, thương": {
                "theory": "Học thuộc bảng đạo hàm cơ bản ($x^n, \\sin x, \\cos x...$). Áp dụng quy tắc đạo hàm của tích: Đạo hàm hàm thứ nhất nhân hàm thứ hai CỘNG hàm thứ nhất nhân đạo hàm hàm thứ hai. Thương tương tự nhưng dấu TRỪ và chia cho bình phương mẫu.",
                "formula": r"(uv)' = u'v + uv'; \quad \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}",
                "trap": "Học sinh 100% bị nhầm đạo hàm của $(u/v)'$ mang dấu cộng. Nhớ kỹ tử số của công thức thương mang dấu TRỪ, và có mẫu bình phương.",
                "audio": "Đạo hàm của tích là u phẩy v cộng u v phẩy. Đạo hàm của thương là u phẩy v trừ u v phẩy, tất cả chia cho v bình phương.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm đa thức",
                        "problem": "Tính đạo hàm của $y = 3x^4 - 2x^2 + 5$.",
                        "solution": "- $y' = 3(4x^3) - 2(2x) + 0 = 12x^3 - 4x$."
                    },
                    {
                        "title": "Ví dụ 2: Đạo hàm của tích",
                        "problem": "Tính đạo hàm $y = x \\sin x$.",
                        "solution": "- Gọi $u = x \\implies u' = 1$. Gọi $v = \\sin x \\implies v' = \\cos x$.\n- Áp dụng: $y' = 1 \\cdot \\sin x + x \\cdot \\cos x = \\sin x + x\\cos x$."
                    },
                    {
                        "title": "Ví dụ 3: Đạo hàm của thương bậc 1/1",
                        "problem": "Tính đạo hàm $y = \\frac{2x - 1}{x + 1}$.",
                        "solution": "- Áp dụng nhanh định thức: $y' = \\frac{2(1) - (-1)1}{(x+1)^2} = \\frac{3}{(x+1)^2}$."
                    }
                ],
                "exercise": {
                    "id": "11_32_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị đạo hàm của y = x.cos(x) tại x = 0 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Đạo hàm của hàm hợp": {
                "theory": "Hàm hợp là hàm được lồng vào nhau, ví dụ thay vì $x^2$ thì là $(2x+1)^2$. Quy tắc dây chuyền: Lấy đạo hàm của hàm ngoài theo hàm trong, rồi NHÂN VỚI đạo hàm của hàm trong theo x.",
                "formula": r"y'_x = y'_u \cdot u'_x \implies (u^\alpha)' = \alpha u^{\alpha-1} \cdot u'",
                "trap": "Lỗi kinh điển nhất là quên NHÂN với cái đuôi $u'$ ở phía sau. Ví dụ đạo hàm $\\sin(2x)$ cứ ghi là $\\cos(2x)$ (thiếu số 2).",
                "audio": "Khi gặp hàm hợp, cứ đạo hàm như bình thường, nhưng ở cuối cùng em bắt buộc phải nhân thêm u phẩy nhé.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đạo hàm hàm hợp lũy thừa",
                        "problem": "Tính đạo hàm $y = (x^2 + 1)^3$.",
                        "solution": "- Xem $u = x^2 + 1$. Đạo hàm của $u^3$ là $3u^2 \\cdot u'$.\n- $y' = 3(x^2 + 1)^2 \\cdot (x^2 + 1)' = 3(x^2 + 1)^2 \\cdot 2x = 6x(x^2 + 1)^2$."
                    },
                    {
                        "title": "Ví dụ 2: Đạo hàm hàm hợp lượng giác",
                        "problem": "Tính đạo hàm $y = \\sin(3x)$.",
                        "solution": "- Đạo hàm của $\\sin u$ là $\\cos u \\cdot u'$.\n- $y' = \\cos(3x) \\cdot (3x)' = 3\\cos(3x)$."
                    },
                    {
                        "title": "Ví dụ 3: Đạo hàm căn thức hàm hợp",
                        "problem": "Tính đạo hàm $y = \\sqrt{2x + 5}$.",
                        "solution": "- Đạo hàm của $\\sqrt{u}$ là $\\frac{u'}{2\\sqrt{u}}$.\n- $y' = \\frac{(2x+5)'}{2\\sqrt{2x+5}} = \\frac{2}{2\\sqrt{2x+5}} = \\frac{1}{\\sqrt{2x+5}}$."
                    }
                ],
                "exercise": {
                    "id": "11_32_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị đạo hàm của y = sin(2x) tại x = 0 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 33: Đạo hàm cấp hai": {
        "chapter": "Chương IX: Đạo hàm",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Ứng dụng vật lý của đạo hàm cấp hai": {
                "theory": "Đạo hàm cấp hai là lấy đạo hàm của kết quả đạo hàm cấp một. Trong Vật lý, nếu đạo hàm cấp một của quãng đường là Vận tốc $v(t)$, thì đạo hàm cấp hai là Gia tốc tức thời $a(t)$.",
                "formula": r"f''(x) = [f'(x)]'; \quad a(t) = v'(t) = s''(t)",
                "trap": "Học sinh hay tính sai dấu từ đạo hàm cấp một lượng giác, dẫn đến đạo hàm cấp hai sai dây chuyền. Nhớ: $\\sin' = \\cos$, $\\cos' = -\\sin$.",
                "audio": "Đạo hàm cấp hai đơn giản chỉ là đạo hàm hai lần liên tiếp. Trong vật lý, đạo hàm quãng đường ra vận tốc, đạo hàm vận tốc sẽ ra gia tốc.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính đạo hàm cấp hai hàm đa thức",
                        "problem": "Tính $y''$ của hàm số $y = x^4 - 3x^2 + 1$.",
                        "solution": "- Đạo hàm cấp 1: $y' = 4x^3 - 6x$.\n- Đạo hàm cấp 2: $y'' = (4x^3 - 6x)' = 12x^2 - 6$."
                    },
                    {
                        "title": "Ví dụ 2: Tính gia tốc tức thời",
                        "problem": "Phương trình chuyển động của ô tô $s(t) = t^3 - 2t^2 + 5t$. Tính gia tốc tại thời điểm $t=2$.",
                        "solution": "- Vận tốc $v(t) = s'(t) = 3t^2 - 4t + 5$.\n- Gia tốc $a(t) = s''(t) = 6t - 4$.\n- Gia tốc tại $t=2$: $a(2) = 6(2) - 4 = 8$."
                    },
                    {
                        "title": "Ví dụ 3: Đạo hàm cấp hai lượng giác",
                        "problem": "Chứng minh hàm số $y = \\sin x$ thỏa mãn phương trình $y'' + y = 0$.",
                        "solution": "- Đạo hàm cấp 1: $y' = \\cos x$.\n- Đạo hàm cấp 2: $y'' = -\\sin x$.\n- Xét $y'' + y = -\\sin x + \\sin x = 0$. Đẳng thức được chứng minh."
                    }
                ],
                "exercise": {
                    "id": "11_33_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho y = x^3. Giá trị đạo hàm cấp hai của hàm số tại x = 2 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "12", 
                    "options": []
                }
            }
        }
    }
})