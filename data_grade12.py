# data_grade12.py
# CHUẨN HÓA DỮ LIỆU THEO VỞ TỰ HỌC TOÁN 12 - BỘ KẾT NỐI TRI THỨC VỚI CUỘC SỐNG
# ĐẦY ĐỦ 19 BÀI HỌC VÀ BÀI 5 CHUẨN 5 CHỦ ĐIỂM THEO TÀI LIỆU GỐC

GRADE_12_DATA = {
    # =========================================================================
    # CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ
    # =========================================================================
    "Bài 1: Tính đơn điệu và cực trị của hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1. Tính đơn điệu của hàm số": {
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
                    "content": "Hàm số $y = -x^3 + 3x$ nghịch biến trên khoảng nào sau đây? (Nhập 1 nếu là khoảng (1; +vô cực), 0 nếu sai):",
                    "target": "1"
                }
            },
            "Chủ điểm 2. Cực trị của hàm số": {
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
    "Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1. Định nghĩa và tìm GTLN, GTNN trên khoảng": {
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
            "Chủ điểm 2. Quy tắc tìm GTLN, GTNN trên đoạn": {
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
    "Bài 3: Đường tiệm cận của đồ thị hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1. Đường tiệm cận đứng": {
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
            "Chủ điểm 2. Đường tiệm cận ngang": {
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
            "Chủ điểm 3. Đường tiệm cận xiên": {
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
    },
    "Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1. Sơ đồ khảo sát hàm số": {
                "theory": "1. Tìm tập xác định.\n2. Khảo sát sự biến thiên (đạo hàm $y'$, cực trị, tiệm cận, bảng biến thiên).\n3. Vẽ đồ thị (giao điểm trục tọa độ, tâm đối xứng, trục đối xứng).",
                "formula": "\\text{TXĐ} \\to y' \\to \\text{Cực trị/Tiệm cận} \\to \\text{BBT} \\to \\text{Đồ thị}",
                "trap": "Quên tìm tọa độ giao điểm với trục tung và trục hoành trước khi vẽ.",
                "audio": "Khảo sát hàm số gồm ba bước chính: tập xác định, sự biến thiên và vẽ đồ thị.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ: Khảo sát hàm số bậc ba",
                        "problem": "Khảo sát hàm số $y = x^3 - 3x$.",
                        "solution": "TXĐ: $D = \\mathbb{R}$. $y' = 3x^2 - 3 = 0 \\iff x = \\pm 1$. Đồ thị nhận gốc tọa độ O làm tâm đối xứng."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c1",
                    "title": "Bài tập tự giải",
                    "content": "Đồ thị hàm số $y = x^3 - 3x^2$ cắt trục hoành tại bao nhiêu điểm phân biệt?",
                    "target": "2"
                }
            },
            "Chủ điểm 2. Nhận dạng đồ thị hàm số và các hệ số": {
                "theory": "Nhận dạng dựa vào: Dấu hệ số $a$ từ nhánh vô cực; giao điểm với trục tung $y(0) = d$; tọa độ các điểm cực trị; các đường tiệm cận đứng và tiệm cận ngang.",
                "formula": "\\text{Nhánh cuối đi lên} \\implies a > 0; \\quad y(0) = d",
                "trap": "Nhầm dấu tiệm cận đứng và ngang khi đọc bảng biến thiên.",
                "audio": "Nhìn nhánh ngoài cùng bên phải để xác định dấu hệ số cao nhất, sau đó nhìn giao điểm với trục tung.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ: Nhận diện hệ số",
                        "problem": "Cho đồ thị hàm bậc ba cắt Oy tại $(0; 2)$ và nhánh phải đi xuống. Tìm dấu a và giá trị d.",
                        "solution": "$a < 0$ và $d = 2$."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c2",
                    "title": "Bài tập tự giải",
                    "content": "Cho hàm số $y = \\frac{ax + 1}{bx - 2}$ có tiệm cận đứng $x = 1$. Tìm b:",
                    "target": "2"
                }
            }
        }
    },

    # =========================================================================
    # BÀI 5: ĐẦY ĐỦ 5 CHỦ ĐIỂM THEO CHUẨN VỞ TỰ HỌC TOÁN 12 (ẢNH WORD GỐC)
    # =========================================================================
    "Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn": {
        "chapter": "CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ",
        "topics": {
            "Chủ điểm 1. Quy trình giải bài toán tối ưu trong thực tiễn": {
                "theory": "Quy trình giải bài toán tối ưu thực tiễn gồm 4 bước:\n- Bước 1: Xác định đại lượng cần tối ưu (lớn nhất hoặc nhỏ nhất), chọn ẩn $x$ và tìm điều kiện (miền) của $x$ theo ý nghĩa thực tế[cite: 4].\n- Bước 2: Biểu diễn đại lượng cần tối ưu thành hàm số $y = f(x)$ một biến[cite: 4].\n- Bước 3: Khảo sát hàm số $f(x)$ trên miền đã tìm (tìm GTLN hoặc GTNN bằng đạo hàm, bảng biến thiên)[cite: 4].\n- Bước 4: Kết luận: trả lời đúng câu hỏi (giá trị của $x$ hay giá trị lớn nhất, nhỏ nhất), kèm đơn vị[cite: 4].\n\n* Ý nghĩa đạo hàm là tốc độ thay đổi: Nếu $s = s(t)$ là quãng đường thì vận tốc tức thời $v(t) = s'(t)$, gia tốc $a(t) = v'(t) = s''(t)$[cite: 4]. Nếu $Q(t)$ là lượng (dân số, nồng độ, số ca bệnh...) thì $Q'(t)$ là tốc độ thay đổi của $Q$ tại thời điểm $t$[cite: 4].",
                "formula": "y = f(x); \\quad f'(x) = 0; \\quad v(t) = s'(t); \\quad a(t) = v'(t)",
                "trap": "Học sinh thường quên đặt điều kiện thực tế cho ẩn (ví dụ kích thước $x > 0$, phần cắt không vượt quá nửa cạnh).",
                "audio": "Quy trình giải bài toán tối ưu thực tế gồm bốn bước cơ bản: chọn ẩn và đặt điều kiện, thiết lập hàm mục tiêu, khảo sát đạo hàm tìm max min, và kết luận đúng yêu cầu kèm đơn vị.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Quy trình tối ưu chi phí rào chắn",
                        "problem": "Một bác nông dân muốn rào một khu đất hình chữ nhật có diện tích $200\\text{ m}^2$ giáp bờ sông (không cần rào phía bờ sông). Nêu các bước lập hàm số tính chiều dài hàng rào và tìm kích thước để tốn ít hàng rào nhất.",
                        "solution": "1. Gọi chiều rộng khu đất vuông góc với bờ sông là $x$ ($x > 0$, mét).\n2. Chiều dài khu đất song song bờ sông là $\\frac{200}{x}$.\n3. Chiều dài hàng rào cần làm là: $L(x) = 2x + \\frac{200}{x}$ với $x > 0$.\n4. Khảo sát: $L'(x) = 2 - \\frac{200}{x^2} = 0 \\iff x^2 = 100 \\iff x = 10$ (m).\n5. Kết luận: Chiều rộng $10\\text{ m}$, chiều dài $20\\text{ m}$ thì hàng rào ngắn nhất là $40\\text{ m}$."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Một mảnh vườn hình chữ nhật có diện tích 100 m2. Chu vi nhỏ nhất của mảnh vườn bằng bao nhiêu mét?",
                    "target": "40"
                }
            },
            "Chủ điểm 2. Bài toán tối ưu hình học: diện tích, thể tích": {
                "theory": "Áp dụng các công thức hình học không gian và hình học phẳng[cite: 4]:\n- Thể tích hình hộp, hình trụ: $V = B \\cdot h$.\n- Thể tích khối nón, chóp: $V = \\frac{1}{3} B \\cdot h$.\n- Diện tích xung quanh, diện tích toàn phần của các khối tròn xoay và khối đa diện.\n- Thường dùng phương pháp biểu diễn một biến phụ theo biến chính thông qua dữ kiện thể tích hoặc diện tích không đổi để rút về hàm một biến[cite: 4].",
                "formula": "V = S_{đáy} \\cdot h; \\quad S_{tp} = S_{xq} + S_{đáy}",
                "trap": "Cần chú ý đọc kỹ đề bài là hộp 'không có nắp' hay 'có nắp' để tính đúng diện tích toàn phần.",
                "audio": "Trong bài toán tối ưu hình học, các em dùng công thức thể tích hoặc diện tích để rút một ẩn phụ theo ẩn chính, sau đó thiết lập hàm mục tiêu một biến.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Cắt góc làm hộp có thể tích lớn nhất (Theo tài liệu gốc)",
                        "problem": "Từ một tấm tôn hình vuông cạnh 30 cm, người ta cắt bỏ bốn hình vuông nhỏ cạnh x ở bốn góc rồi gập lên thành một chiếc hộp không nắp. Tìm x để hộp có thể tích lớn nhất và tính thể tích lớn nhất đó[cite: 4].",
                        "solution": "1. Điều kiện của cạnh cắt: $0 < x < 15$ (cm).\n2. Đáy hộp là hình vuông cạnh $30 - 2x$, chiều cao hộp là $x$.\n3. Thể tích chiếc hộp là: $V(x) = x(30 - 2x)^2 = 4x^3 - 120x^2 + 900x$.\n4. Đạo hàm: $V'(x) = 12x^2 - 240x + 900 = 0 \\iff x = 5$ (nhận) hoặc $x = 15$ (loại).\n5. Lập BBT thấy $V(x)$ đạt cực đại tại $x = 5$.\n6. Kết luận: Cắt cạnh $x = 5\\text{ cm}$ thì thể tích lớn nhất là $V(5) = 5 \\cdot 20^2 = 2000\\text{ cm}^3$."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Từ tấm tôn vuông cạnh 18 cm, cắt 4 góc các hình vuông cạnh x rồi gập thành hộp không nắp. Thể tích lớn nhất đạt được khi x bằng bao nhiêu cm?",
                    "target": "3"
                }
            },
            "Chủ điểm 3. Bài toán tối ưu trong kinh tế (doanh thu, chi phí, lợi nhuận)": {
                "theory": "Mối quan hệ cốt lõi trong kinh tế học vi mô:\n- Doanh thu: $R(x) = x \\cdot p(x)$ (với $x$ là sản lượng, $p(x)$ là giá bán mỗi sản phẩm).\n- Lợi nhuận: $P(x) = R(x) - C(x)$ (với $C(x)$ là tổng hàm chi phí).\n- Điểm hòa vốn: $P(x) = 0 \\iff R(x) = C(x)$.\n- Lợi nhuận tối đa khi đạo hàm lợi nhuận bằng 0: $P'(x) = 0 \\iff R'(x) = C'(x)$ (Doanh thu biên bằng Chi phí biên).",
                "formula": "P(x) = R(x) - C(x); \\quad P'(x) = 0 \\iff R'(x) = C'(x)",
                "trap": "Học sinh thường nhầm lẫn giữa Doanh thu (tiền thu về) và Lợi nhuận (tiền thu về trừ chi phí).",
                "audio": "Trong kinh tế, lợi nhuận bằng doanh thu trừ chi phí. Lợi nhuận đạt cực đại khi doanh thu biên bằng chi phí biên.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tối đa hóa lợi nhuận của doanh nghiệp",
                        "problem": "Một công ty sản xuất x sản phẩm với hàm tổng chi phí $C(x) = x^2 + 20x + 100$ (triệu đồng) và hàm doanh thu $R(x) = 120x - x^2$ (triệu đồng). Tìm sản lượng x để công ty đạt lợi nhuận lớn nhất.",
                        "solution": "1. Hàm lợi nhuận: $P(x) = R(x) - C(x) = (120x - x^2) - (x^2 + 20x + 100) = -2x^2 + 100x - 100$.\n2. Đạo hàm: $P'(x) = -4x + 100 = 0 \\iff x = 25$.\n3. Vì hàm bậc hai có $a = -2 < 0$ nên đạt cực đại tại đỉnh $x = 25$.\n4. Kết luận: Sản xuất 25 sản phẩm thì lợi nhuận lớn nhất là $P(25) = 1150$ triệu đồng."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c3",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Một xưởng may bán x chiếc áo với giá p(x) = 150 - 0.5x (nghìn đồng). Doanh thu đạt cực đại khi may bao nhiêu chiếc áo?",
                    "target": "150"
                }
            },
            "Chủ điểm 4. Bài toán tối ưu trong chuyển động và vật lý": {
                "theory": "Mối quan hệ đạo hàm trong cơ học và động học[cite: 4]:\n- Vận tốc tức thời là đạo hàm bậc nhất của phương trình tọa độ/quãng đường: $v(t) = s'(t)$[cite: 4].\n- Gia tốc tức thời là đạo hàm của vận tốc (đạo hàm bậc hai của quãng đường): $a(t) = v'(t) = s''(t)$[cite: 4].\n- Vận tốc đạt giá trị lớn nhất khi $v'(t) = 0 \\iff a(t) = 0$.\n- Vật dừng lại hoặc đổi chiều chuyển động khi vận tốc triệt tiêu: $v(t) = 0$.",
                "formula": "v(t) = s'(t); \\quad a(t) = v'(t) = s''(t)",
                "trap": "Phải phân biệt: Thời điểm vật đạt vận tốc lớn nhất (gia tốc $a = 0$) khác với thời điểm vật đạt độ cao lớn nhất (vận tốc $v = 0$).",
                "audio": "Vận tốc là đạo hàm của quãng đường, gia tốc là đạo hàm của vận tốc. Vận tốc đạt cực đại khi gia tốc bằng 0.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm thời điểm vận tốc đạt cực đại",
                        "problem": "Một chất điểm chuyển động có phương trình quãng đường $s(t) = -t^3 + 9t^2 + t$ (với t tính bằng giây, s tính bằng mét). Tìm vận tốc lớn nhất của chất điểm trong 5 giây đầu.",
                        "solution": "1. Vận tốc của chất điểm: $v(t) = s'(t) = -3t^2 + 18t + 1$.\n2. Gia tốc: $a(t) = v'(t) = -6t + 18 = 0 \\iff t = 3$ (giây).\n3. Tính vận tốc: $v(0) = 1$, $v(3) = 28$, $v(5) = 16$.\n4. Kết luận: Vận tốc lớn nhất đạt được là $28\\text{ m/s}$ tại thời điểm $t = 3\\text{ s}$."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c4",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Một vật ném thẳng đứng lên cao theo phương trình h(t) = -5t^2 + 20t + 2 (mét). Độ cao cực đại mà vật đạt được bằng bao nhiêu mét?",
                    "target": "22"
                }
            },
            "Chủ điểm 5. Bài toán tối ưu thực tế liên môn (sinh học, môi trường, y tế)": {
                "theory": "Ứng dụng trong sinh học, y tế và môi trường:\n- Tốc độ tăng trưởng dân số hoặc số ca nhiễm dịch bệnh: $N'(t)$ (với $N(t)$ là số ca)[cite: 4]. Đỉnh dịch xuất hiện khi $N'(t) = 0$.\n- Nồng độ thuốc trong máu sau khi tiêm/uống: $C(t)$. Nồng độ đạt đỉnh tại thời điểm $C'(t) = 0$.\n- Tốc độ quang hợp, sự hấp thụ chất dinh dưỡng hay mức độ ô nhiễm môi trường.",
                "formula": "N'(t) = 0 \\implies \\text{đỉnh dịch bệnh/dân số}; \\quad C'(t) = 0 \\implies \\text{nồng độ thuốc đạt đỉnh}",
                "trap": "Cần chú ý điều kiện thời gian $t \\ge 0$ và làm tròn số học đúng theo yêu cầu thực tế.",
                "audio": "Trong y tế và sinh học, đỉnh điểm của dịch bệnh hoặc nồng độ thuốc trong máu đạt giá trị lớn nhất khi đạo hàm của hàm số biểu diễn bằng 0.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Nồng độ thuốc trong máu",
                        "problem": "Sau khi tiêm thuốc, nồng độ thuốc trong máu của bệnh nhân sau t giờ được xác định bởi hàm số $C(t) = \\frac{0.4t}{t^2 + 4}$ (mg/ml). Sau bao nhiêu giờ thì nồng độ thuốc đạt mức cao nhất?",
                        "solution": "1. TXĐ: $t \\ge 0$.\n2. Đạo hàm: $C'(t) = \\frac{0.4(t^2 + 4) - 0.4t(2t)}{(t^2 + 4)^2} = \\frac{0.4(4 - t^2)}{(t^2 + 4)^2}$.\n3. Cho $C'(t) = 0 \\iff 4 - t^2 = 0 \\iff t = 2$ (do $t \\ge 0$).\n4. Lập BBT thấy $C(t)$ đạt cực đại tại $t = 2$.\n5. Kết luận: Sau 2 giờ kể từ khi tiêm thì nồng độ thuốc đạt mức cao nhất."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c5",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Số ca nhiễm một loại virus sau t ngày được mô hình hóa bởi N(t) = -t^3 + 12t^2 + 100 (với t >= 0). Tốc độ lây lan lớn nhất tại ngày thứ mấy?",
                    "target": "4"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG II. TỌA ĐỘ CỦA VECTƠ TRONG KHÔNG GIAN
    # =========================================================================
    "Bài 6: Vectơ trong không gian": {
        "chapter": "CHƯƠNG II. TỌA ĐỘ CỦA VECTƠ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Khái niệm vectơ và các phép toán vectơ trong không gian": {
                "theory": "Vectơ trong không gian là đoạn thẳng có hướng. Quy tắc ba điểm, quy tắc hình bình hành và quy tắc hình hộp: $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$.",
                "formula": "\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}",
                "trap": "Nhầm quy tắc hình hộp với quy tắc hình bình hành đáy.",
                "audio": "Trong hình hộp, vectơ đường chéo xuất phát từ một đỉnh bằng tổng ba vectơ cạnh xuất phát từ đỉnh đó.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Quy tắc hình hộp",
                        "problem": "Cho hình hộp ABCD.A'B'C'D'. Rút gọn vectơ tổng $\\vec{AB} + \\vec{AD} + \\vec{AA'}$.",
                        "solution": "Theo quy tắc hình hộp, $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$."
                    }
                ],
                "exercise": {"id": "12_b6_c1", "title": "Bài tập", "content": "Cho hình lập phương ABCD.A'B'C' cạnh 1. Độ dài vectơ tổng AB + AD + AA' bằng căn mấy?", "target": "3"}
            },
            "Chủ điểm 2. Tích vô hướng của hai vectơ trong không gian": {
                "theory": "$\\vec{a} \\cdot \\vec{b} = |\\vec{a}| \\cdot |\\vec{b}| \\cdot \\cos(\\vec{a}, \\vec{b})$. Hai vectơ vuông góc khi và chỉ khi tích vô hướng bằng 0.",
                "formula": "\\vec{a} \\cdot \\vec{b} = |\\vec{a}| |\\vec{b}| \\cos(\\vec{a}, \\vec{b}); \\quad \\vec{a} \\perp \\vec{b} \\iff \\vec{a} \\cdot \\vec{b} = 0",
                "trap": "Góc giữa hai vectơ có thể tù (từ 0 đến 180 độ), còn góc giữa hai đường thẳng chỉ từ 0 đến 90 độ.",
                "audio": "Tích vô hướng bằng tích độ dài nhân cos góc xen giữa. Tích bằng 0 thì hai vectơ vuông góc.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Tính tích vô hướng",
                        "problem": "Cho tứ diện đều ABCD cạnh a. Tính tích vô hướng của $\\vec{AB} \\cdot \\vec{AC}$.",
                        "solution": "Tam giác ABC đều nên góc giữa AB và AC bằng 60 độ. Tích vô hướng bằng $a \\cdot a \\cdot \\cos 60^\\circ = \\frac{a^2}{2}$."
                    }
                ],
                "exercise": {"id": "12_b6_c2", "title": "Bài tập", "content": "Cho tam giác ABC đều cạnh 2. Tính tích vô hướng AB . AC:", "target": "2"}
            }
        }
    },
    "Bài 7: Hệ trục tọa độ trong không gian": {
        "chapter": "CHƯƠNG II. TỌA ĐỘ CỦA VECTƠ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Tọa độ của điểm và vectơ trong không gian": {
                "theory": "Hệ trục Oxyz gồm ba trục Ox, Oy, Oz vuông góc từng đôi một tại gốc O với các vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$. Vectơ $\\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\iff \\vec{u} = (x; y; z)$.",
                "formula": "\\vec{u} = (x; y; z) \\iff \\vec{u} = x\\vec{i} + y\\vec{j} + z\\vec{k}",
                "trap": "Nhầm thứ tự các trục hoành độ x, tung độ y và cao độ z.",
                "audio": "Hệ trục tọa độ Oxyz gồm trục hoành Ox, trục tung Oy và trục cao Oz đôi một vuông góc.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tọa độ vectơ",
                        "problem": "Cho $\\vec{a} = 2\\vec{i} - 3\\vec{j} + \\vec{k}$. Tìm tọa độ của $\\vec{a}$.",
                        "solution": "Tọa độ vectơ $\\vec{a} = (2; -3; 1)$."
                    }
                ],
                "exercise": {"id": "12_b7_c1", "title": "Bài tập", "content": "Tìm cao độ z của điểm M biết vectơ OM = 3i - 4j + 5k:", "target": "5"}
            },
            "Chủ điểm 2. Biểu thức tọa độ của các phép toán vectơ": {
                "theory": "Cho $\\vec{u} = (x; y; z), \\vec{v} = (x'; y'; z')$.\n- $\\vec{u} \\pm \\vec{v} = (x \\pm x'; y \\pm y'; z \\pm z')$.\n- $k\\vec{u} = (kx; ky; kz)$.\n- $\\vec{u} \\cdot \\vec{v} = xx' + yy' + zz'$.\n- Độ dài $|\\vec{u}| = \\sqrt{x^2 + y^2 + z^2}$.",
                "formula": "|\\vec{u}| = \\sqrt{x^2 + y^2 + z^2}; \\quad \\vec{u} \\cdot \\vec{v} = xx' + yy' + zz'",
                "trap": "Khi tính khoảng cách hai điểm quên lấy căn bậc hai.",
                "audio": "Tích vô hướng bằng tích hoành cộng tích tung cộng tích cao. Độ dài bằng căn của tổng bình phương các tọa độ.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tính độ dài vectơ",
                        "problem": "Tính độ dài vectơ $\\vec{u} = (1; 2; 2)$.",
                        "solution": "$|\\vec{u}| = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{9} = 3$."
                    }
                ],
                "exercise": {"id": "12_b7_c2", "title": "Bài tập", "content": "Tính khoảng cách giữa hai điểm A(1; 0; 0) và B(1; 3; 4):", "target": "5"}
            }
        }
    },
    "Bài 8: Biểu thức tọa độ của các phép toán vectơ": {
        "chapter": "CHƯƠNG II. TỌA ĐỘ CỦA VECTƠ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Tích có hướng của hai vectơ và ứng dụng": {
                "theory": "Tích có hướng $[\vec{a}, \\vec{b}]$ là một vectơ vuông góc với cả $\\vec{a}$ và $\\vec{b}$.\nỨng dụng: Diện tích tam giác $S = \\frac{1}{2} |[\\vec{AB}, \\vec{AC}]|$; Thể tích tứ diện $V = \\frac{1}{6} |[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}|$.",
                "formula": "S_{\\Delta} = \\frac{1}{2} |[\\vec{AB}, \\vec{AC}]|; \\quad V_{ABCD} = \\frac{1}{6} |[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD}|",
                "trap": "Hai vectơ cùng phương khi và chỉ khi tích có hướng của chúng bằng vectơ không.",
                "audio": "Tích có hướng của hai vectơ tạo ra một vectơ mới vuông góc với cả hai vectơ ban đầu.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Kiểm tra đồng phẳng",
                        "problem": "Kiểm tra bốn điểm đồng phẳng khi nào?",
                        "solution": "Bốn điểm A, B, C, D đồng phẳng khi và chỉ khi tích hỗn tạp $[\\vec{AB}, \\vec{AC}] \\cdot \\vec{AD} = 0$."
                    }
                ],
                "exercise": {"id": "12_b8_c1", "title": "Bài tập", "content": "Nếu hai vectơ cùng phương thì tích có hướng của chúng bằng vectơ nào? (Nhập 0 nếu là vectơ không):", "target": "0"}
            }
        }
    },

    # =========================================================================
    # CHƯƠNG III. CÁC SỐ ĐẶC TRƯNG ĐO MỨC ĐỘ PHÂN TÁN CHO MẪU SỐ LIỆU GHÉP NHÓM
    # =========================================================================
    "Bài 9: Khoảng biến thiên và khoảng tứ phân vị": {
        "chapter": "CHƯƠNG III. THỐNG KÊ",
        "topics": {
            "Chủ điểm 1. Khoảng biến thiên của mẫu số liệu ghép nhóm": {
                "theory": "Khoảng biến thiên $R = a_k - a_1$ là hiệu số giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên.",
                "formula": "R = a_k - a_1",
                "trap": "Không lấy giá trị đại diện mà lấy trực tiếp đầu mút của nhóm.",
                "audio": "Khoảng biến thiên là hiệu số giữa giá trị lớn nhất và nhỏ nhất của các nhóm dữ liệu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính khoảng biến thiên",
                        "problem": "Cho các nhóm $[20; 30), [30; 40), [40; 50)$. Tìm R.",
                        "solution": "$R = 50 - 20 = 30$."
                    }
                ],
                "exercise": {"id": "12_b9_c1", "title": "Bài tập", "content": "Cho mẫu số liệu ghép nhóm từ [10; 20) đến [50; 60). Khoảng biến thiên R bằng bao nhiêu?", "target": "50"}
            },
            "Chủ điểm 2. Khoảng tứ phân vị của mẫu số liệu ghép nhóm": {
                "theory": "Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$. Dùng để đo độ phân tán của 50% số liệu chính giữa mẫu.",
                "formula": "\\Delta_Q = Q_3 - Q_1",
                "trap": "Phải xác định đúng nhóm chứa tứ phân vị trước khi áp dụng công thức nội suy.",
                "audio": "Khoảng tứ phân vị bằng Q3 trừ Q1, đại diện cho độ phân tán của 50% dữ liệu ở giữa.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính khoảng tứ phân vị",
                        "problem": "Biết $Q_1 = 25$ và $Q_3 = 45$. Tìm $\\Delta_Q$.",
                        "solution": "$\\Delta_Q = 45 - 25 = 20$."
                    }
                ],
                "exercise": {"id": "12_b9_c2", "title": "Bài tập", "content": "Cho Q1 = 12.5 và Q3 = 22.5. Khoảng tứ phân vị Delta Q bằng bao nhiêu?", "target": "10"}
            }
        }
    },
    "Bài 10: Phương sai và độ lệch chuẩn": {
        "chapter": "CHƯƠNG III. THỐNG KÊ",
        "topics": {
            "Chủ điểm 1. Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm": {
                "theory": "Phương sai $s^2 = \\frac{1}{n} \\sum n_i (c_i - \\bar{x})^2$ đo mức độ phân tán quanh số trung bình. Độ lệch chuẩn $s = \\sqrt{s^2}$.",
                "formula": "s^2 = \\frac{1}{n} \\sum n_i c_i^2 - (\\bar{x})^2; \\quad s = \\sqrt{s^2}",
                "trap": "Nhầm lẫn giữa giá trị đại diện $c_i$ và tần số $n_i$.",
                "audio": "Độ lệch chuẩn là căn bậc hai của phương sai, cho biết độ phân tán dữ liệu quanh giá trị trung bình.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Độ lệch chuẩn",
                        "problem": "Một mẫu số liệu có phương sai $s^2 = 16$. Tìm độ lệch chuẩn s.",
                        "solution": "$s = \\sqrt{16} = 4$."
                    }
                ],
                "exercise": {"id": "12_b10_c1", "title": "Bài tập", "content": "Biết phương sai s^2 = 25. Tìm độ lệch chuẩn s:", "target": "5"}
            }
        }
    },

    # =========================================================================
    # CHƯƠNG IV. NGUYÊN HÀM VÀ TÍCH PHÂN
    # =========================================================================
    "Bài 11: Nguyên hàm": {
        "chapter": "CHƯƠNG IV. NGUYÊN HÀM VÀ TÍCH PHÂN",
        "topics": {
            "Chủ điểm 1. Định nghĩa và tính chất của nguyên hàm": {
                "theory": "$F(x)$ là nguyên hàm của $f(x)$ nếu $F'(x) = f(x)$. Họ nguyên hàm: $\\int f(x)dx = F(x) + C$.",
                "formula": "\\int f(x)dx = F(x) + C \\iff F'(x) = f(x)",
                "trap": "Khi tính nguyên hàm luôn luôn phải có hằng số cộng C.",
                "audio": "Nguyên hàm là phép toán ngược của đạo hàm. Họ tất cả nguyên hàm luôn có cộng C.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Bảng nguyên hàm cơ bản",
                        "problem": "Tìm họ nguyên hàm của $f(x) = 3x^2 + 2x$.",
                        "solution": "$\\int (3x^2 + 2x)dx = x^3 + x^2 + C$."
                    }
                ],
                "exercise": {"id": "12_b11_c1", "title": "Bài tập", "content": "Nguyên hàm của f(x) = 4x^3 là x^4 + C. Đúng nhập 1, sai nhập 0:", "target": "1"}
            },
            "Chủ điểm 2. Phương pháp đổi biến và từng phần": {
                "theory": "Đổi biến: $\\int f(u(x)) u'(x)dx = \\int f(u)du$. Từng phần: $\\int u dv = uv - \\int v du$.",
                "formula": "\\int u dv = uv - \\int v du",
                "trap": "Thứ tự ưu tiên đặt u trong nguyên hàm từng phần: Nhất lô, nhì đa, tam lượng, tứ mũ.",
                "audio": "Nguyên hàm từng phần dùng công thức u v trừ tích phân v d u.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Từng phần",
                        "problem": "Tìm $\\int x e^x dx$.",
                        "solution": "Đặt $u = x, dv = e^x dx \\implies du = dx, v = e^x$. Ta có: $\\int x e^x dx = x e^x - e^x + C$."
                    }
                ],
                "exercise": {"id": "12_b11_c2", "title": "Bài tập", "content": "Tích phân x dx từ 0 đến 2 bằng bao nhiêu?", "target": "2"}
            }
        }
    },
    "Bài 12: Tích phân": {
        "chapter": "CHƯƠNG IV. NGUYÊN HÀM VÀ TÍCH PHÂN",
        "topics": {
            "Chủ điểm 1. Khái niệm và tính chất của tích phân": {
                "theory": "$\\int_a^b f(x)dx = F(b) - F(a)$ (Công thức Newton-Leibniz). Tích phân không phụ thuộc vào biến số.",
                "formula": "\\int_a^b f(x)dx = F(b) - F(a)",
                "trap": "Đổi cận khi đổi biến số: Bắt buộc phải đổi cận từ x sang u.",
                "audio": "Tích phân từ a đến b của f x d x bằng F b trừ F a.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tính tích phân cơ bản",
                        "problem": "Tính $I = \\int_0^1 (2x + 1)dx$.",
                        "solution": "$I = [x^2 + x]_0^1 = (1 + 1) - 0 = 2$."
                    }
                ],
                "exercise": {"id": "12_b12_c1", "title": "Bài tập", "content": "Tính tích phân của f(x) = 3 từ 1 đến 4:", "target": "9"}
            }
        }
    },
    "Bài 13: Ứng dụng hình học của tích phân": {
        "chapter": "CHƯƠNG IV. NGUYÊN HÀM VÀ TÍCH PHÂN",
        "topics": {
            "Chủ điểm 1. Diện tích hình phẳng và thể tích khối tròn xoay": {
                "theory": "Diện tích: $S = \\int_a^b |f(x) - g(x)|dx$. Thể tích tròn xoay quanh trục Ox: $V = \\pi \\int_a^b f^2(x)dx$.",
                "formula": "S = \\int_a^b |f(x)|dx; \\quad V = \\pi \\int_a^b f^2(x)dx",
                "trap": "Thể tích khối tròn xoay quanh trục Ox bắt buộc phải có số pi ở phía trước.",
                "audio": "Diện tích hình phẳng có dấu trị tuyệt đối, còn thể tích tròn xoay có nhân thêm pi và bình phương hàm số.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Diện tích hình phẳng",
                        "problem": "Tính diện tích hình phẳng giới hạn bởi $y = x^2$, trục hoành, $x = 0, x = 3$.",
                        "solution": "$S = \\int_0^3 x^2 dx = [\\frac{x^3}{3}]_0^3 = 9$."
                    }
                ],
                "exercise": {"id": "12_b13_c1", "title": "Bài tập", "content": "Diện tích hình phẳng giới hạn bởi y = 2x, y = 0, x = 0, x = 2 bằng bao nhiêu?", "target": "4"}
            }
        }
    },

    # =========================================================================
    # CHƯƠNG V. PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN
    # =========================================================================
    "Bài 14: Phương trình mặt phẳng": {
        "chapter": "CHƯƠNG V. PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Vectơ pháp tuyến và phương trình tổng quát của mặt phẳng": {
                "theory": "Mặt phẳng đi qua $M_0(x_0; y_0; z_0)$ có VTPT $\\vec{n} = (A; B; C)$ có phương trình: $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$.",
                "formula": "Ax + By + Cz + D = 0 \\quad (A^2 + B^2 + C^2 > 0)",
                "trap": "Phương trình đoạn chắn đi qua $(a; 0; 0), (0; b; 0), (0; 0; c)$ là $\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1$.",
                "audio": "Mặt phẳng được xác định khi biết một điểm đi qua và một vectơ pháp tuyến vuông góc với mặt phẳng đó.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Viết phương trình mặt phẳng",
                        "problem": "Viết phương trình mặt phẳng qua $M(1; 2; 3)$ có VTPT $\\vec{n} = (2; -1; 1)$.",
                        "solution": "$2(x - 1) - 1(y - 2) + 1(z - 3) = 0 \\iff 2x - y + z - 3 = 0$."
                    }
                ],
                "exercise": {"id": "12_b14_c1", "title": "Bài tập", "content": "Cho mặt phẳng (P): 2x - 3y + z - 5 = 0. Tung độ của vectơ pháp tuyến bằng bao nhiêu?", "target": "-3"}
            }
        }
    },
    "Bài 15: Phương trình đường thẳng trong không gian": {
        "chapter": "CHƯƠNG V. PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Phương trình tham số và chính tắc của đường thẳng": {
                "theory": "Đường thẳng qua $M_0(x_0; y_0; z_0)$ có VTCP $\\vec{u} = (a; b; c)$:\nTham số: $x = x_0 + at, y = y_0 + bt, z = z_0 + ct$. Chính tắc: $\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c}$.",
                "formula": "\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c}",
                "trap": "Chỉ viết được dạng chính tắc khi tất cả các tọa độ của vectơ chỉ phương đều khác 0.",
                "audio": "Đường thẳng được xác định khi biết một điểm đi qua và một vectơ chỉ phương có giá song song hoặc trùng với đường thẳng.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Vectơ chỉ phương",
                        "problem": "Tìm VTCP của đường thẳng $d: \\frac{x - 1}{2} = \\frac{y + 2}{-3} = \\frac{z}{4}$.",
                        "solution": "$\\vec{u} = (2; -3; 4)$."
                    }
                ],
                "exercise": {"id": "12_b15_c1", "title": "Bài tập", "content": "Đường thẳng d có phương trình tham số x = 1 + 2t. Hoành độ của VTCP bằng bao nhiêu?", "target": "2"}
            }
        }
    },
    "Bài 16: Phương trình mặt cầu": {
        "chapter": "CHƯƠNG V. PHƯƠNG PHÁP TỌA ĐỘ TRONG KHÔNG GIAN",
        "topics": {
            "Chủ điểm 1. Phương trình mặt cầu tâm I bán kính R": {
                "theory": "Mặt cầu tâm $I(a; b; c)$, bán kính $R$: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.\nDạng khai triển: $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ với điều kiện $a^2 + b^2 + c^2 - d > 0$.",
                "formula": "(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2; \\quad R = \\sqrt{a^2 + b^2 + c^2 - d}",
                "trap": "Khi tìm tâm từ dạng khai triển nhớ chia hệ số của x, y, z cho -2.",
                "audio": "Mặt cầu tâm a b c bán kính R có phương trình x trừ a tất cả bình cộng y trừ b tất cả bình cộng z trừ c tất cả bình bằng R bình.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm tâm và bán kính mặt cầu",
                        "problem": "Tìm tâm và bán kính mặt cầu $(x - 1)^2 + (y + 2)^2 + z^2 = 16$.",
                        "solution": "Tâm $I(1; -2; 0)$ và bán kính $R = \\sqrt{16} = 4$."
                    }
                ],
                "exercise": {"id": "12_b16_c1", "title": "Bài tập", "content": "Bán kính mặt cầu (x - 1)^2 + (y - 2)^2 + (z - 3)^2 = 25 bằng bao nhiêu?", "target": "5"}
            }
        }
    },

    # =========================================================================
    # CHƯƠNG VI. XÁC SUẤT CÓ ĐIỀU KIỆN
    # =========================================================================
    "Bài 17: Xác suất có điều kiện": {
        "chapter": "CHƯƠNG VI. XÁC SUẤT CÓ ĐIỀU KIỆN",
        "topics": {
            "Chủ điểm 1. Định nghĩa và công thức nhân xác suất": {
                "theory": "Xác suất của biến cố A khi biết biến cố B đã xảy ra là: $P(A|B) = \\frac{P(AB)}{P(B)}$ với $P(B) > 0$.\nCông thức nhân xác suất: $P(AB) = P(B) \\cdot P(A|B) = P(A) \\cdot P(B|A)$.",
                "formula": "P(A|B) = \\frac{P(AB)}{P(B)}; \\quad P(AB) = P(B) \\cdot P(A|B)",
                "trap": "Phân biệt biến cố điều kiện $P(A|B)$ (biết B đã xảy ra) với $P(B|A)$ (biết A đã xảy ra).",
                "audio": "Xác suất của A với điều kiện B bằng xác suất của A giao B chia cho xác suất của B.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính xác suất điều kiện",
                        "problem": "Cho $P(B) = 0.5$ và $P(AB) = 0.2$. Tính $P(A|B)$.",
                        "solution": "$P(A|B) = \\frac{0.2}{0.5} = 0.4$."
                    }
                ],
                "exercise": {"id": "12_b17_c1", "title": "Bài tập", "content": "Cho P(B) = 0.4, P(AB) = 0.1. Tính P(A|B):", "target": "0.25"}
            }
        }
    },
    "Bài 18: Công thức xác suất toàn phần và công thức Bayes": {
        "chapter": "CHƯƠNG VI. XÁC SUẤT CÓ ĐIỀU KIỆN",
        "topics": {
            "Chủ điểm 1. Công thức xác suất toàn phần và công thức Bayes": {
                "theory": "Hệ đầy đủ $\\{B_1, B_2, \\dots, B_n\\}$.\n- Xác suất toàn phần: $P(A) = \\sum P(B_i) \\cdot P(A|B_i)$.\n- Công thức Bayes: $P(B_k|A) = \\frac{P(B_k) \\cdot P(A|B_k)}{P(A)}$.",
                "formula": "P(A) = \\sum_{i=1}^n P(B_i) P(A|B_i); \\quad P(B_k|A) = \\frac{P(B_k) P(A|B_k)}{P(A)}",
                "trap": "Tổng xác suất của hệ biến cố đầy đủ $\\sum P(B_i)$ luôn luôn phải bằng 1.",
                "audio": "Công thức Bayes dùng để tính xác suất hậu nghiệm khi đã biết kết quả của biến cố A.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Công thức xác suất toàn phần",
                        "problem": "Hai hộp bi. Hộp 1 có xác suất chọn 0.6, bắn trúng với xác suất 0.8. Hộp 2 có xác suất chọn 0.4, bắn trúng với xác suất 0.5. Tính xác suất bắn trúng.",
                        "solution": "$P(A) = 0.6 \\cdot 0.8 + 0.4 \\cdot 0.5 = 0.48 + 0.20 = 0.68$."
                    }
                ],
                "exercise": {"id": "12_b18_c1", "title": "Bài tập", "content": "Cho P(B1)=0.5, P(A|B1)=0.4, P(B2)=0.5, P(A|B2)=0.6. Tính P(A):", "target": "0.5"}
            }
        }
    },
    "Bài 19: Ôn tập chương và khảo thí tổng hợp cuối năm": {
        "chapter": "CHƯƠNG VI. XÁC SUẤT CÓ ĐIỀU KIỆN",
        "topics": {
            "Chủ điểm 1. Ma trận đề thi tốt nghiệp THPT chuẩn cấu trúc GDPT 2018": {
                "theory": "Cấu trúc đề thi mới bám sát khung năng lực của Bộ GD&ĐT gồm 3 phần:\n- Phần I: 12 câu trắc nghiệm 4 lựa chọn (3.0 điểm).\n- Phần II: 4 câu trắc nghiệm Đúng/Sai (4.0 điểm).\n- Phần III: 6 câu trắc nghiệm trả lời ngắn (3.0 điểm).",
                "formula": "\\text{Điểm tối đa} = 10.0; \\quad 22 \\text{ câu hỏi}",
                "trap": "Chiến thuật làm bài: Làm chắc Phần I và Phần II trước khi chuyển sang Phần III.",
                "audio": "Đề thi tốt nghiệp THPT theo chương trình mới gồm ba phần với tổng cộng hai mươi hai câu hỏi, làm bài trong 90 phút.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Phân bổ thời gian thi",
                        "problem": "Thời gian làm bài thi môn Toán tốt nghiệp THPT là bao nhiêu phút?",
                        "solution": "Thời gian làm bài chính thức là 90 phút."
                    }
                ],
                "exercise": {"id": "12_b19_c1", "title": "Bài tập", "content": "Số lượng câu hỏi trắc nghiệm Đúng/Sai ở Phần II là bao nhiêu câu?", "target": "4"}
            }
        }
    }
}
