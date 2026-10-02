# data_grade11.py
# CHUẨN HÓA DỮ LIỆU TỪ VỞ TỰ HỌC TOÁN 11 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG

GRADE_11_DATA = {
    "Bài 1. Giá trị lượng giác của góc lượng giác": {
        "chapter": "CHƯƠNG I. HÀM SỐ LƯỢNG GIÁC VÀ PHƯƠNG TRÌNH LƯỢNG GIÁC",
        "topics": {
            "Chủ điểm 1: Góc lượng giác và đơn vị radian": {
                "theory": "- Đường tròn bán kính $R$, cung có độ dài $l = R$ có số đo 1 radian (1 rad).\n- Quan hệ giữa độ và radian: $180^\\circ = \\pi \\text{ rad} \\implies 1^\\circ = \\frac{\\pi}{180} \\text{ rad}, \\ 1 \\text{ rad} = \\left(\\frac{180}{\\pi}\\right)^\\circ$.\n- Độ dài cung tròn có số đo $\\alpha$ rad trên đường tròn bán kính $R$ là: $l = R\\alpha$.",
                "formula": "180^\\circ = \\pi \\text{ rad}; \\quad l = R \\alpha",
                "trap": "Khi tính độ dài cung tròn bằng công thức $l = R\\alpha$, góc $\\alpha$ bắt buộc phải đổi sang đơn vị radian.",
                "audio": "Khi tính độ dài cung tròn, góc alpha bắt buộc phải ở đơn vị radian. Một trăm tám mươi độ tương ứng với pi radian.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ: Đổi đơn vị đo góc",
                        "problem": "Đổi góc có số đo $60^\\circ$ sang radian.",
                        "solution": "$60^\\circ = 60 \\cdot \\frac{\\pi}{180} = \\frac{\\pi}{3} \\text{ rad}$."
                    }
                ],
                "exercise": {
                    "id": "11_b1_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Một bánh xe có bán kính 20 cm quay được góc 3 radian. Tính quãng đường đi được của một điểm trên vành bánh xe (cm):",
                    "target": "60"
                }
            },
            "Chủ điểm 2: Giá trị lượng giác của một góc lượng giác": {
                "theory": "Trên đường tròn lượng giác, điểm $M(x_0; y_0)$ biểu diễn góc lượng giác $\\alpha$:\n$$\\cos \\alpha = x_0; \\quad \\sin \\alpha = y_0; \\quad \\tan \\alpha = \\frac{y_0}{x_0} \\ (x_0 \\ne 0); \\quad \\cot \\alpha = \\frac{x_0}{y_0} \\ (y_0 \\ne 0)$$\n- Các hằng đẳng thức cốt lõi:\n$$\\sin^2 \\alpha + \\cos^2 \\alpha = 1; \\quad 1 + \\tan^2 \\alpha = \\frac{1}{\\cos^2 \\alpha}; \\quad 1 + \\cot^2 \\alpha = \\frac{1}{\\sin^2 \\alpha}$$",
                "formula": "\\sin^2\\alpha + \\cos^2\\alpha = 1; \\quad 1 + \\tan^2\\alpha = \\frac{1}{\\cos^2\\alpha}",
                "trap": "Xác định dấu của các giá trị lượng giác phụ thuộc vào góc phần tư: Phải chú ý góc $\\alpha$ thuộc góc phần tư thứ mấy để lấy dấu âm/dương khi khai căn.",
                "audio": "Trục hoành là trục cos, trục tung là trục sin. Chú ý góc phần tư để chọn dấu khi tính sin và cos.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ: Tính giá trị lượng giác theo góc phần tư",
                        "problem": "Cho $\\sin \\alpha = \\frac{3}{5}$ với $\\frac{\\pi}{2} < \\alpha < \\pi$. Tính $\\cos \\alpha$.",
                        "solution": "Ta có $\\cos^2 \\alpha = 1 - \\sin^2 \\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$.\nVì $\\frac{\\pi}{2} < \\alpha < \\pi$ (góc phần tư thứ II) nên $\\cos \\alpha < 0$. Do đó $\\cos \\alpha = -\\frac{4}{5}$."
                    }
                ],
                "exercise": {
                    "id": "11_b1_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho $\\cos \\alpha = 0.6$. Tính giá trị của biểu thức $P = \\sin^2 \\alpha$:",
                    "target": "0.64"
                }
            }
        }
    },
    "Bài 5. Dãy số": {
        "chapter": "CHƯƠNG II. DÃY SỐ. CẤP SỐ CỘNG VÀ CẤP SỐ NHÂN",
        "topics": {
            "Chủ điểm 1: Định nghĩa và cách cho một dãy số": {
                "theory": "- Dãy số vô hạn là hàm số xác định trên tập các số nguyên dương $\\mathbb{N}^*$. Kí hiệu $(u_n)$.\n- Dãy số có thể được cho bằng: Công thức số hạng tổng quát; Phương pháp mô tả; Phương pháp quy hồi.",
                "formula": "u_n = f(n), \\ n \\in \\mathbb{N}^*",
                "trap": "Chỉ số $n$ của dãy số luôn bắt đầu từ 1 ($n \\ge 1, n \\in \\mathbb{N}^*$), không bao giờ lấy $n = 0$.",
                "audio": "Dãy số là một hàm số xác định trên tập số nguyên dương. Chỉ số n luôn bắt đầu từ số 1.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm số hạng tổng quát",
                        "problem": "Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = 2n - 1$. Viết 3 số hạng đầu tiên.",
                        "solution": "$u_1 = 2(1) - 1 = 1$; $u_2 = 2(2) - 1 = 3$; $u_3 = 2(3) - 1 = 5$."
                    }
                ],
                "exercise": {
                    "id": "11_b5_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho dãy số $(u_n)$ xác định bởi $u_n = n^2 + 1$. Tìm số hạng thứ 4 của dãy số:",
                    "target": "17"
                }
            },
            "Chủ điểm 2: Dãy số tăng, dãy số giảm và dãy số bị chặn": {
                "theory": "- Dãy số $(u_n)$ tăng nếu $u_{n+1} > u_n, \\forall n \\in \\mathbb{N}^*$.\n- Dãy số $(u_n)$ giảm nếu $u_{n+1} < u_n, \\forall n \\in \\mathbb{N}^*$.\n- Dãy số $(u_n)$ bị chặn nếu tồn tại hai số $m, M$ sao cho $m \\le u_n \\le M, \\forall n \\in \\mathbb{N}^*$.",
                "formula": "u_{n+1} - u_n > 0 \\implies (u_n) \\nearrow; \\quad m \\le u_n \\le M \\implies (u_n) \\text{ bị chặn}",
                "trap": "Để xét tính tăng giảm, phương pháp chuẩn là xét dấu của hiệu số $u_{n+1} - u_n$. Chỉ được so sánh tỉ số $\\frac{u_{n+1}}{u_n}$ với 1 khi mọi số hạng đều dương.",
                "audio": "Để xét dãy số tăng hay giảm, ta lập hiệu u n cộng một trừ đi u n rồi xét dấu hiệu số đó.",
                "svg": "DAY_SO",
                "examples": [
                    {
                        "title": "Ví dụ: Xét tính tăng giảm",
                        "problem": "Xét tính tăng giảm của dãy số $u_n = \\frac{n}{n + 1}$.",
                        "solution": "Xét hiệu $u_{n+1} - u_n = \\frac{n+1}{n+2} - \\frac{n}{n+1} = \\frac{(n+1)^2 - n(n+2)}{(n+1)(n+2)} = \\frac{1}{(n+1)(n+2)} > 0, \\forall n \\ge 1$.\nVậy dãy số $(u_n)$ là dãy số tăng."
                    }
                ],
                "exercise": {
                    "id": "11_b5_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Dãy số $u_n = \\frac{1}{n}$ bị chặn trên bởi số nào? (Nhập 1 nếu là 1, 0 nếu không bị chặn):",
                    "target": "1"
                }
            }
        }
    },
    "Bài 11. Hai đường thẳng song song trong không gian": {
        "chapter": "CHƯƠNG IV. QUAN HỆ SONG SONG TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1: Vị trí tương đối của hai đường thẳng": {
                "theory": "Trong không gian, hai đường thẳng $a$ và $b$ có 4 vị trí tương đối:\n1. Cắt nhau: Có duy nhất một điểm chung (đồng phẳng).\n2. Song song: Cùng nằm trong một mặt phẳng và không có điểm chung.\n3. Trùng nhau: Có vô số điểm chung.\n4. Chéo nhau: Không cùng thuộc bất kì mặt phẳng nào.",
                "formula": "\\text{Chéo nhau } \\iff \\text{không đồng phẳng}",
                "trap": "Hai đường thẳng không có điểm chung trong không gian có thể song song HOẶC chéo nhau (khác với hình học phẳng).",
                "audio": "Trong không gian, hai đường thẳng không có điểm chung thì có thể song song hoặc chéo nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ: Xác định hai đường thẳng chéo nhau",
                        "problem": "Cho tứ diện ABCD. Xét vị trí tương đối của hai đường thẳng AB và CD.",
                        "solution": "Bốn điểm A, B, C, D không đồng phẳng nên AB và CD không cùng thuộc một mặt phẳng. Do đó AB và CD chéo nhau."
                    }
                ],
                "exercise": {
                    "id": "11_b11_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho hình chóp S.ABCD đáy hình vuông. Đường thẳng SA và BC có chéo nhau không? (Nhập 1 nếu có, 0 nếu không):",
                    "target": "1"
                }
            },
            "Chủ điểm 2: Tính chất hai đường thẳng song song": {
                "theory": "- Định lí: Trong không gian, qua một điểm nằm ngoài đường thẳng cho trước có một và chỉ một đường thẳng song song với đường thẳng đó.\n- Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau: $a \\parallel c$ và $b \\parallel c \\implies a \\parallel b$.\n- Định lí giao tuyến: Ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến đó hoặc đồng quy hoặc đôi một song song.",
                "formula": "a \\parallel c \\text{ và } b \\parallel c \\implies a \\parallel b",
                "trap": "Cần kiểm tra kĩ điều kiện các đường thẳng phân biệt trước khi áp dụng tính chất bắc cầu.",
                "audio": "Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm giao tuyến bằng tính chất song song",
                        "problem": "Cho hình chóp S.ABCD có đáy ABCD là hình bình hành. Tìm giao tuyến của $(SAB)$ và $(SCD)$.",
                        "solution": "Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AB$ và $CD$. Do đó giao tuyến của chúng là đường thẳng $d$ đi qua $S$ và song song với $AB, CD$."
                    }
                ],
                "exercise": {
                    "id": "11_b11_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho hình chóp S.ABCD đáy là hình bình hành. Giao tuyến của mặt phẳng (SAD) và (SBC) là đường thẳng đi qua S và song song với AD đúng hay sai? (Nhập 1 nếu đúng, 0 nếu sai):",
                    "target": "1"
                }
            }
        }
    }
}
