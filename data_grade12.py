# data_grade12.py
# CHUẨN HÓA THEO VỞ TỰ HỌC TOÁN 12 - BỘ KẾT NỐI TRI THỨC VỚI CUỘC SỐNG

GRADE_12_DATA = {
    "Bài 1. Tính đơn điệu và cực trị của hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1: Tính đơn điệu của hàm số": {
                "theory": "Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $K$.\n- Nếu $f'(x) > 0, \\forall x \\in K$ thì hàm số đồng biến trên $K$.\n- Nếu $f'(x) < 0, \\forall x \\in K$ thì hàm số nghịch biến trên $K$.\n- Mở rộng: Nếu $f'(x) \\ge 0$ (hoặc $\\le 0$), $\\forall x \\in K$ và bằng 0 tại hữu hạn điểm thì hàm số đồng biến (hoặc nghịch biến) trên $K$.",
                "formula": "f'(x) > 0 \\implies f(x) \\nearrow; \\quad f'(x) < 0 \\implies f(x) \\searrow",
                "trap": "Học sinh thường kết luận hàm số đồng biến trên hợp các khoảng hoặc viết $D = \\mathbb{R} \\setminus \\{x_0\\}$. Bắt buộc phải kết luận trên từng khoảng rời nhau.",
                "audio": "Khi xét tính đơn điệu, các em tính đạo hàm, tìm nghiệm và lập bảng xét dấu. Kết luận đồng biến nghịch biến trên từng khoảng xác định rời nhau.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đơn điệu của hàm số bậc ba",
                        "problem": "Tìm các khoảng đơn điệu của hàm số $y = x^3 - 3x^2 + 2$.",
                        "solution": "1. TXĐ: $D = \\mathbb{R}$.\n2. Đạo hàm: $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 \\iff x = 0$ hoặc $x = 2$.\n3. Bảng xét dấu: $y' > 0$ trên $(-\\infty; 0)$ và $(2; +\\infty)$; $y' < 0$ trên $(0; 2)$.\n4. Kết luận: Hàm số đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên $(0; 2)$."
                    }
                ],
                "exercise": {
                    "id": "12_b1_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Hàm số $y = -x^3 + 3x$ nghịch biến trên khoảng nào sau đây? (Nhập 1 nếu là khoảng (1; +vô cực), 0 nếu sai)",
                    "target": "1"
                }
            },
            "Chủ điểm 2: Cực trị của hàm số": {
                "theory": "Giả sử hàm số $y = f(x)$ liên tục trên $(a; b)$ chứa $x_0$ và có đạo hàm trên $(a; b) \\setminus \\{x_0\\}$.\n- Nếu $f'(x)$ đổi dấu từ dương sang âm khi qua $x_0$ thì $x_0$ là điểm cực đại.\n- Nếu $f'(x)$ đổi dấu từ âm sang dương khi qua $x_0$ thì $x_0$ là điểm cực tiểu.",
                "formula": "f'(x_0) = 0 \\text{ và đổi dấu qua } x_0 \\implies x_0 \\text{ là điểm cực trị}",
                "trap": "Phân biệt rõ: Điểm cực trị của hàm số là $x_0$; Giá trị cực trị là $y_0 = f(x_0)$; Điểm cực trị của đồ thị là $M(x_0; y_0)$.",
                "audio": "Điểm cực trị là điểm làm cho đạo hàm đổi dấu. Nếu đổi dấu từ dương sang âm là cực đại, từ âm sang dương là cực tiểu.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm cực trị của hàm số bậc ba",
                        "problem": "Tìm các điểm cực trị của hàm số $y = x^3 - 3x + 1$.",
                        "solution": "1. TXĐ: $D = \\mathbb{R}$.\n2. $y' = 3x^2 - 3 = 0 \\iff x = \\pm 1$.\n- Tại $x = -1$, $y'$ đổi dấu từ dương sang âm $\\implies x = -1$ là điểm cực đại, giá trị cực đại $y_{CĐ} = 3$.\n- Tại $x = 1$, $y'$ đổi dấu từ âm sang dương $\\implies x = 1$ là điểm cực tiểu, giá trị cực tiểu $y_{CT} = -1$."
                    }
                ],
                "exercise": {
                    "id": "12_b1_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tính giá trị cực đại của hàm số $y = -x^3 + 3x^2 - 1$:",
                    "target": "3"
                }
            }
        }
    },
    "Bài 2. Giá trị lớn nhất và giá trị nhỏ nhất của hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1: Định nghĩa và tìm GTLN, GTNN trên khoảng": {
                "theory": "Số $M$ là GTLN của $f(x)$ trên $D$ nếu $f(x) \\le M, \\forall x \\in D$ và $\\exists x_0 \\in D: f(x_0) = M$.\nSố $m$ là GTNN của $f(x)$ trên $D$ nếu $f(x) \\ge m, \\forall x \\in D$ và $\\exists x_0 \\in D: f(x_0) = m$.",
                "formula": "\\max_{D} f(x) = M; \\quad \\min_{D} f(x) = m",
                "trap": "Hàm số trên khoảng mở $(a; b)$ có thể không đạt GTLN hoặc GTNN nếu dấu bằng không xảy ra trong khoảng.",
                "audio": "Để tìm GTLN, GTNN trên khoảng mở, các em phải lập bảng biến thiên để xác định xu hướng của đồ thị.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm GTNN trên khoảng",
                        "problem": "Tìm GTNN của $y = x + \\frac{4}{x}$ trên $(0; +\\infty)$.",
                        "solution": "Áp dụng BĐT Cô-si: $x + \\frac{4}{x} \\ge 2\\sqrt{x \\cdot \\frac{4}{x}} = 4$. Dấu bằng xảy ra khi $x = 2$. Vậy $\\min_{(0; +\\infty)} y = 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tìm giá trị nhỏ nhất của hàm số $y = x + \\frac{9}{x}$ trên khoảng $(0; +\\infty)$:",
                    "target": "6"
                }
            },
            "Chủ điểm 2: Quy tắc tìm GTLN, GTNN trên đoạn": {
                "theory": "Tìm GTLN, GTNN của hàm liên tục trên $[a; b]$:\n1. Tìm nghiệm $x_i \\in (a; b)$ của $f'(x) = 0$.\n2. Tính $f(a), f(b)$ và các $f(x_i)$.\n3. So sánh các giá trị đã tính để chọn ra số lớn nhất và nhỏ nhất.",
                "formula": "\\max_{[a;b]} f(x) = \\max \\{f(a), f(b), f(x_i)\\}",
                "trap": "Quên loại bỏ các nghiệm của đạo hàm nằm ngoài đoạn $[a; b]$.",
                "audio": "Trên đoạn đóng, các em chỉ cần tính giá trị tại 2 đầu mút và các nghiệm nằm trong khoảng, không cần lập bảng biến thiên.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm max min trên đoạn",
                        "problem": "Tìm GTLN của hàm số $y = x^3 - 3x + 2$ trên đoạn $[0; 2]$.",
                        "solution": "$y' = 3x^2 - 3 = 0 \\iff x = 1 \\in (0; 2)$ (loại $x = -1$).\n$y(0) = 2, y(1) = 0, y(2) = 4$. Vậy GTLN bằng 4."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tìm giá trị lớn nhất của $y = -x^3 + 3x$ trên đoạn $[0; 2]$:",
                    "target": "2"
                }
            }
        }
    },
    "Bài 3. Đường tiệm cận của đồ thị hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1: Đường tiệm cận đứng": {
                "theory": "Đường thẳng $x = x_0$ là tiệm cận đứng nếu ít nhất một trong các giới hạn một bên khi $x \\to x_0^+$ hoặc $x \\to x_0^-$ bằng $+\\infty$ hoặc $-\\infty$.",
                "formula": "\\lim_{x \\to x_0^\\pm} f(x) = \\pm \\infty \\implies x = x_0 \\text{ là TCĐ}",
                "trap": "Nghiệm của mẫu số nhưng đồng thời làm triệt tiêu tử số thì chưa chắc là tiệm cận đứng.",
                "audio": "Tiệm cận đứng là đường thẳng x bằng x không, thường là nghiệm của mẫu số không làm triệt tiêu tử số.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tiệm cận đứng",
                        "problem": "Tìm tiệm cận đứng của $y = \\frac{2x - 1}{x - 3}$.",
                        "solution": "Vì $\\lim_{x \\to 3^+} \\frac{2x - 1}{x - 3} = +\\infty$ nên $x = 3$ là tiệm cận đứng."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tìm tiệm cận đứng của đồ thị $y = \\frac{x + 1}{x - 4}$. Nhập hoành độ x:",
                    "target": "4"
                }
            },
            "Chủ điểm 2: Đường tiệm cận ngang": {
                "theory": "Đường thẳng $y = y_0$ là tiệm cận ngang nếu $\\lim_{x \\to +\\infty} f(x) = y_0$ hoặc $\\lim_{x \\to -\\infty} f(x) = y_0$.",
                "formula": "\\lim_{x \\to \\pm \\infty} f(x) = y_0 \\implies y = y_0 \\text{ là TCN}",
                "trap": "Với hàm chứa căn thức, tiệm cận ngang khi $x \\to +\\infty$ và $x \\to -\\infty$ có thể khác nhau.",
                "audio": "Tiệm cận ngang là đường y bằng y không khi x tiến ra vô cực.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tiệm cận ngang",
                        "problem": "Tìm tiệm cận ngang của $y = \\frac{3x - 1}{x + 1}$.",
                        "solution": "$\\lim_{x \\to \\pm \\infty} \\frac{3x - 1}{x + 1} = 3 \\implies y = 3$ là tiệm cận ngang."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tìm tung độ tiệm cận ngang của đồ thị $y = \\frac{4x - 1}{2x + 3}$:",
                    "target": "2"
                }
            },
            "Chủ điểm 3: Đường tiệm cận xiên": {
                "theory": "Đường thẳng $y = ax + b$ ($a \\ne 0$) là tiệm cận xiên nếu $\\lim_{x \\to \\pm \\infty} [f(x) - (ax + b)] = 0$.\nCách tìm: $a = \\lim \\frac{f(x)}{x}, b = \\lim [f(x) - ax]$ hoặc thực hiện phép chia đa thức tử cho mẫu.",
                "formula": "y = ax + b \\quad (a = \\lim_{x \\to \\pm\\infty} \\frac{f(x)}{x}, \\ b = \\lim_{x \\to \\pm\\infty} [f(x) - ax])",
                "trap": "Chỉ xét tiệm cận xiên khi bậc của tử lớn hơn bậc của mẫu đúng 1 bậc.",
                "audio": "Tiệm cận xiên xuất hiện khi bậc tử hơn bậc mẫu một bậc. Các em chia đa thức để lấy phần thương.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tiệm cận xiên",
                        "problem": "Tìm tiệm cận xiên của $y = \\frac{x^2 + 2x - 3}{x + 1}$.",
                        "solution": "Chia đa thức: $y = x + 1 - \\frac{4}{x + 1}$. Vậy $y = x + 1$ là tiệm cận xiên."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c3",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Tìm hệ số góc a của tiệm cận xiên của đồ thị $y = \\frac{3x^2 - x + 1}{x - 2}$:",
                    "target": "3"
                }
            }
        }
    }
}
