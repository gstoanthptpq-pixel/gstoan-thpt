# data_grade12.py
# CHUẨN HÓA 100% CẤU TRÚC 19 BÀI VÀ CÁC CHỦ ĐIỂM THEO VỞ TỰ HỌC TOÁN 12

GRADE_12_DATA = {
    # =========================================================================
    # CHƯƠNG I. ỨNG DỤNG ĐẠO HÀM ĐỂ KHẢO SÁT VÀ VẼ ĐỒ THỊ HÀM SỐ
    # =========================================================================
    "Bài 1. Tính đơn điệu và cực trị của hàm số": {
        "chapter": "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Tính đơn điệu của hàm số": {
                "theory": "Cho hàm số $y = f(x)$ xác định trên $K$.\n- Đồng biến trên $K$: $\\forall x_1 < x_2 \\implies f(x_1) < f(x_2)$ (đồ thị đi lên từ trái sang phải).\n- Nghịch biến trên $K$: $\\forall x_1 < x_2 \\implies f(x_1) > f(x_2)$ (đồ thị đi xuống từ trái sang phải).\n- Liên hệ đạo hàm: $f'(x) > 0, \\forall x \\in K \\implies$ hàm số đồng biến; $f'(x) < 0, \\forall x \\in K \\implies$ hàm số nghịch biến.\n- Mở rộng: Nếu $f'(x) \\ge 0$ (hoặc $\\le 0$), $\\forall x \\in K$ và dấu bằng chỉ xảy ra tại hữu hạn điểm thì hàm số vẫn đồng biến (nghịch biến).",
                "formula": "f'(x) > 0 \\implies f(x) \\nearrow; \\quad f'(x) < 0 \\implies f(x) \\searrow",
                "trap": "Tuyệt đối không kết luận đồng biến trên $R \\setminus {x_0}$ hoặc dùng ký hiệu hợp (∪). Phải kết luận trên từng khoảng xác định rời nhau.",
                "audio": "Khi xét tính đơn điệu, các em tính đạo hàm, tìm nghiệm và lập bảng xét dấu. Luôn nhớ kết luận trên từng khoảng xác định rời nhau.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đơn điệu của hàm số đa thức bậc ba",
                        "problem": "Xét tính đơn điệu của hàm số $y = x^3 - 3x^2 + 1$.",
                        "solution": "1. TXĐ: $\\mathbb{R}$.\n2. Đạo hàm: $y' = 3x^2 - 6x = 3x(x - 2) = 0 \\iff x = 0$ hoặc $x = 2$.\n3. Bảng xét dấu: $y' > 0$ trên $(-\\infty; 0)$ và $(2; +\\infty)$; $y' < 0$ trên $(0; 2)$.\n4. Kết luận: Hàm số đồng biến trên các khoảng $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên khoảng $(0; 2)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính đơn điệu của hàm phân thức bậc nhất trên bậc nhất",
                        "problem": "Xét tính đơn điệu của hàm số $y = \\frac{2x - 1}{x + 1}$.",
                        "solution": "1. TXĐ: $\\mathbb{R} \\setminus \\{-1\\}$.\n2. Đạo hàm: $y' = \\frac{2(1) - (-1)(1)}{(x + 1)^2} = \\frac{3}{(x + 1)^2} > 0, \\forall x \\ne -1$.\n3. Kết luận: Hàm số đồng biến trên từng khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$."
                    }
                ],
                "exercise": {
                    "id": "12_b1_c1",
                    "title": "Bài tập tự giải",
                    "content": "Hàm số $y = -x^3 + 3x$ nghịch biến trên khoảng nào? (Nhập 1 nếu là (1; +vô cực), 0 nếu sai):",
                    "target": "1"
                }
            },
            "Chủ điểm 2: Cực trị của hàm số": {
                "theory": "Giả sử hàm số $y = f(x)$ liên tục trên $(a; b)$ chứa $x_0$ và có đạo hàm trên $(a; b) \\setminus \\{x_0\\}$.\n- Nếu $f'(x)$ đổi dấu từ dương sang âm khi $x$ qua $x_0$ thì $x_0$ là điểm cực đại.\n- Nếu $f'(x)$ đổi dấu từ âm sang dương khi $x$ qua $x_0$ thì $x_0$ là điểm cực tiểu.",
                "formula": "f'(x_0) = 0 \\text{ và } f'(x) \\text{ đổi dấu qua } x_0 \\implies x_0 \\text{ là điểm cực trị}",
                "trap": "Phân biệt rõ: Điểm cực trị của hàm số là $x_0$; Giá trị cực trị là $y_0 = f(x_0)$; Điểm cực trị của đồ thị hàm số là $M(x_0; y_0)$.",
                "audio": "Điểm cực trị là điểm làm cho đạo hàm đổi dấu. Đổi dấu từ dương sang âm là cực đại, từ âm sang dương là cực tiểu.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm điểm cực trị của hàm số bậc ba",
                        "problem": "Tìm điểm cực trị của hàm số $y = x^3 - 3x^2 + 1$.",
                        "solution": "$y' = 3x^2 - 6x = 3x(x - 2)$. $y'$ đổi dấu từ (+) sang (-) tại $x = 0$ và từ (-) sang (+) tại $x = 2$.\nHàm số đạt cực đại tại $x = 0$ với $y_{CĐ} = 1$; đạt cực tiểu tại $x = 2$ với $y_{CT} = -3$."
                    }
                ],
                "exercise": {
                    "id": "12_b1_c2",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị cực tiểu của hàm số $y = x^3 - 3x^2 + 1$ bằng:",
                    "target": "-3"
                }
            }
        }
    },

    "Bài 2. Giá trị lớn nhất và giá trị nhỏ nhất của hàm số": {
        "chapter": "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Khái niệm giá trị lớn nhất, giá trị nhỏ nhất": {
                "theory": "Cho hàm số $y = f(x)$ xác định trên tập $D$.\n- $M = \\max_D f(x) \\iff f(x) \\le M, \\forall x \\in D$ và tồn tại $x_0 \\in D$ sao cho $f(x_0) = M$.\n- $m = \\min_D f(x) \\iff f(x) \\ge m, \\forall x \\in D$ và tồn tại $x_0 \\in D$ sao cho $f(x_0) = m$.",
                "formula": "\\max_D f(x) = M; \\quad \\min_D f(x) = m",
                "trap": "Hàm số trên khoảng mở $(a; b)$ có thể không có GTLN hoặc GTNN nếu giá trị biên tiến ra vô cực hoặc không có dấu bằng.",
                "audio": "GTLN và GTNN nếu có là duy nhất, tuy nhiên có thể đạt được tại nhiều vị trí x khác nhau.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Đọc GTLN, GTNN từ bảng biến thiên",
                        "problem": "Cho hàm số xác định trên $(0; +\\infty)$ có BBT giảm từ $+\\infty$ về 2 rồi tăng lên $+\\infty$. Tìm GTLN, GTNN.",
                        "solution": "Từ bảng biến thiên, $f(x) \\ge 2, \\forall x > 0$ và đạt tại $x = 1$ nên $\\min f(x) = 2$. Hàm số tiến ra $+\\infty$ nên không có GTLN."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c1",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị nhỏ nhất của hàm số $y = x^2 + 2$ trên R bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 2: Tìm GTLN, GTNN của hàm số liên tục trên một đoạn": {
                "theory": "Quy tắc tìm GTLN, GTNN của $y = f(x)$ liên tục trên đoạn $[a; b]$:\n1. Tìm các nghiệm $x_1, x_2, \\dots, x_n \\in (a; b)$ của $f'(x) = 0$.\n2. Tính các giá trị $f(a), f(b), f(x_1), \\dots, f(x_n)$.\n3. Số lớn nhất trong các giá trị đó là $\\max$, số nhỏ nhất là $\\min$.",
                "formula": "\\max_{[a;b]} f(x) = \\max\\{f(a), f(b), f(x_i)\\}; \\quad \\min_{[a;b]} f(x) = \\min\\{f(a), f(b), f(x_i)\\}",
                "trap": "Quên loại các nghiệm của đạo hàm nằm ngoài đoạn $[a; b]$.",
                "audio": "Khi tìm max min trên một đoạn đóng, các em chỉ cần tính giá trị tại hai đầu mút và các nghiệm nằm trong khoảng, không cần lập bảng biến thiên.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm max, min trên đoạn",
                        "problem": "Tìm GTLN và GTNN của hàm số $y = x^3 - 3x^2 - 9x + 35$ trên $[-4; 4]$.",
                        "solution": "$y' = 3x^2 - 6x - 9 = 0 \\iff x = -1 \\in [-4; 4]$ hoặc $x = 3 \\in [-4; 4]$.\nTính các giá trị: $y(-4) = -41; y(-1) = 40; y(3) = 8; y(4) = 15$.\nVậy $\\max_{[-4; 4]} y = 40$ (tại $x = -1$) và $\\min_{[-4; 4]} y = -41$ (tại $x = -4$)."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c2",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị lớn nhất của hàm số $y = -x^2 + 4$ trên đoạn [-1; 2] là:",
                    "target": "4"
                }
            },
            "Chủ điểm 3: Tìm GTLN, GTNN trên khoảng, nửa khoảng (dùng bảng biến thiên)": {
                "theory": "Khi xét trên khoảng $(a; b)$ hoặc nửa khoảng: lập bảng biến thiên trên tập đó, chú ý giới hạn tại các đầu mút. Từ bảng biến thiên kết luận GTLN, GTNN (nếu có).",
                "formula": "x + \\frac{k}{x} \\ge 2\\sqrt{k} \\quad (x > 0, k > 0)",
                "trap": "Không tính các giới hạn tại đầu mút dẫn đến kết luận nhầm lẫn cực trị địa phương là GTLN.",
                "audio": "Trên khoảng mở, luôn phải tính giới hạn tại các đầu mút và quan sát bảng biến thiên để xác định đúng giá trị lớn nhất hoặc nhỏ nhất.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm GTNN trên khoảng dương",
                        "problem": "Tìm GTNN của hàm số $y = x + \\frac{4}{x}$ trên khoảng $(0; +\\infty)$.",
                        "solution": "$y' = 1 - \\frac{4}{x^2} = \\frac{x^2 - 4}{x^2} = 0 \\iff x = 2$ (do $x > 0$).\nBBT cho thấy hàm số nghịch biến trên $(0; 2)$ và đồng biến trên $(2; +\\infty)$. Do đó $\\min_{(0; +\\infty)} y = y(2) = 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c3",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị nhỏ nhất của $y = x + \\frac{9}{x}$ trên $(0; +\\infty)$ bằng:",
                    "target": "6"
                }
            },
            "Chủ điểm 4: Bài toán chứa tham số": {
                "theory": "Khảo sát tính đơn điệu của hàm số theo tham số $m$ để biện luận vị trí đạt GTLN hoặc GTNN trên đoạn.",
                "formula": "y = \\frac{ax+b}{cx+d} \\implies y' = \\frac{ad-bc}{(cx+d)^2}",
                "trap": "Hàm phân thức bậc nhất trên bậc nhất luôn đơn điệu trên từng khoảng xác định nên max min trên đoạn luôn đạt tại một trong hai đầu mút.",
                "audio": "Với hàm phân thức bậc nhất trên bậc nhất, đạo hàm luôn mang một dấu nên giá trị lớn nhất nhỏ nhất luôn nằm ở hai đầu mút của đoạn.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm tham số để GTNN bằng giá trị cho trước",
                        "problem": "Tìm $m$ để GTNN của hàm số $y = \\frac{x + m}{x - 1}$ trên đoạn $[2; 4]$ bằng 3.",
                        "solution": "$y' = \\frac{-1 - m}{(x - 1)^2}$.\nNếu $m > -1 \\implies y' < 0$, hàm số nghịch biến nên $\\min_{[2; 4]} y = y(4) = \\frac{4 + m}{3} = 3 \\iff m = 5$ (thỏa mãn).\nNếu $m < -1 \\implies y' > 0$, hàm đồng biến nên $\\min = y(2) = 2 + m = 3 \\iff m = 1$ (loại). Vậy $m = 5$."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c4",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị của m tìm được trong ví dụ trên bằng:",
                    "target": "5"
                }
            },
            "Chủ điểm 5: Ứng dụng: bài toán thực tế": {
                "theory": "Phương pháp: Đặt ẩn $x$, xác định điều kiện thực tế của biến số, lập hàm mục tiêu và dùng đạo hàm tìm GTLN hoặc GTNN.",
                "formula": "L(x) = 2x + \\frac{S}{x} \\implies L'(x) = 0",
                "trap": "Quên kiểm tra điều kiện thực tế của biến số (độ dài, số sản phẩm phải dương).",
                "audio": "Giải toán thực tế tối ưu: chọn ẩn thích hợp, đặt điều kiện, thiết lập hàm số mục tiêu và dùng đạo hàm để tìm điểm tối ưu.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Rào đất sát bờ sông tiết kiệm hàng rào",
                        "problem": "Rào mảnh đất hình chữ nhật diện tích 800 m2 sát bờ sông thẳng (không rào phía bờ sông). Tìm chiều dài hàng rào ngắn nhất.",
                        "solution": "Gọi $x$ (m) là độ dài cạnh vuông góc bờ sông ($x > 0$), cạnh kia dài $\\frac{800}{x}$.\nChiều dài hàng rào $L(x) = 2x + \\frac{800}{x}$. $L'(x) = 2 - \\frac{800}{x^2} = 0 \\iff x = 20$.\nVậy hàng rào ngắn nhất là $L(20) = 40 + 40 = 80$ m."
                    }
                ],
                "exercise": {
                    "id": "12_b2_c5",
                    "title": "Bài tập tự giải",
                    "content": "Chiều dài hàng rào ngắn nhất (m) là:",
                    "target": "80"
                }
            }
        }
    },

    "Bài 3. Đường tiệm cận của đồ thị hàm số": {
        "chapter": "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Đường tiệm cận ngang": {
                "theory": "Đường thẳng $y = y_0$ là tiệm cận ngang của đồ thị hàm số $y = f(x)$ nếu:\n$$\\lim_{x \\to +\\infty} f(x) = y_0 \\quad \\text{hoặc} \\quad \\lim_{x \\to -\\infty} f(x) = y_0$$\nĐồ thị có tối đa hai tiệm cận ngang.",
                "formula": "\\lim_{x \\to \\pm \\infty} f(x) = y_0 \\implies y = y_0 \\text{ là TCN}",
                "trap": "Hàm chứa căn thức có thể có hai tiệm cận ngang khác nhau khi $x \\to +\\infty$ và $x \\to -\\infty$.",
                "audio": "Tiệm cận ngang là đường thẳng nằm ngang y bằng y không khi x tiến ra dương vô cùng hoặc âm vô cùng.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm tiệm cận ngang của hàm phân thức",
                        "problem": "Tìm tiệm cận ngang của đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$.",
                        "solution": "Ta có $\\lim_{x \\to \\pm\\infty} \\frac{2x - 1}{x + 1} = 2$. Do đó đường thẳng $y = 2$ là tiệm cận ngang."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c1",
                    "title": "Bài tập tự giải",
                    "content": "Tung độ tiệm cận ngang của đồ thị $y = \\frac{4x + 1}{2x - 3}$ bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 2: Đường tiệm cận đứng": {
                "theory": "Đường thẳng $x = x_0$ là tiệm cận đứng nếu ít nhất một trong các giới hạn một bên khi $x \\to x_0^+$ hoặc $x \\to x_0^-$ bằng $+\\infty$ hoặc $-\\infty$.\nVới hàm phân thức tối giản $y = \\frac{P(x)}{Q(x)}$, tiệm cận đứng là các nghiệm của $Q(x) = 0$ mà $P(x) \\ne 0$.",
                "formula": "\\lim_{x \\to x_0^\\pm} f(x) = \\pm \\infty \\implies x = x_0 \\text{ là TCĐ}",
                "trap": "Nghiệm của mẫu số triệt tiêu hoàn toàn với nghiệm của tử số thì không phải là tiệm cận đứng.",
                "audio": "Tiệm cận đứng là đường thẳng đứng x bằng x không, thường là nghiệm của mẫu số không làm triệt tiêu tử số.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Rút gọn trước khi tìm tiệm cận đứng",
                        "problem": "Tìm số tiệm cận đứng của đồ thị $y = \\frac{x^2 - 3x + 2}{x^2 - 1}$.",
                        "solution": "Ta có $y = \\frac{(x - 1)(x - 2)}{(x - 1)(x + 1)} = \\frac{x - 2}{x + 1}$ ($x \\ne 1$).\nTại $x = 1$, giới hạn hữu hạn (bằng $-1/2$). Tại $x = -1$, giới hạn tiến ra vô cực nên $x = -1$ là tiệm cận đứng duy nhất."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c2",
                    "title": "Bài tập tự giải",
                    "content": "Số tiệm cận đứng của đồ thị $y = \\frac{x - 1}{x^2 - 1}$ là:",
                    "target": "1"
                }
            },
            "Chủ điểm 3: Đường tiệm cận xiên": {
                "theory": "Đường thẳng $y = ax + b$ ($a \\ne 0$) là tiệm cận xiên nếu $\\lim_{x \\to \\pm \\infty} [f(x) - (ax + b)] = 0$.\nVới hàm phân thức bậc hai trên bậc nhất: thực hiện phép chia đa thức tử cho mẫu $f(x) = ax + b + \\frac{r}{dx + e}$.",
                "formula": "y = ax + b \\quad (a = \\lim \\frac{f(x)}{x}; \\ b = \\lim [f(x) - ax])",
                "trap": "Đồ thị chỉ có tiệm cận xiên khi bậc của tử lớn hơn bậc của mẫu đúng 1 bậc.",
                "audio": "Tiệm cận xiên xuất hiện khi bậc tử hơn bậc mẫu một bậc. Thực hiện phép chia đa thức thì phần thương chính là phương trình tiệm cận xiên.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm tiệm cận xiên",
                        "problem": "Tìm tiệm cận xiên của đồ thị $y = \\frac{x^2 - 2x + 2}{x - 1}$.",
                        "solution": "Chia tử cho mẫu: $y = x - 1 + \\frac{1}{x - 1}$. Vì $\\lim_{x \\to \\pm\\infty} \\frac{1}{x - 1} = 0$ nên đường thẳng $y = x - 1$ là tiệm cận xiên."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hệ số góc a của tiệm cận xiên của $y = \\frac{3x^2 + 1}{x - 1}$ bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 4: Tiệm cận qua bảng biến thiên": {
                "theory": "Đọc giới hạn ở các đầu mút $\\pm\\infty$ trên dòng $x$ và giá trị tương ứng ở dòng $y$ để tìm TCN. Nhìn điểm không xác định có giới hạn tiến ra $\\pm\\infty$ để tìm TCĐ.",
                "formula": "\\text{Đọc } x \\to \\pm\\infty \\implies y_0 \\text{ (TCN)}; \\quad x \\to x_0 \\implies \\pm\\infty \\text{ (TCĐ)}",
                "trap": "Nhầm lẫn giữa giá trị cực trị và đường tiệm cận ngang trên bảng biến thiên.",
                "audio": "Nhìn các đầu mút vô cực trên dòng x của bảng biến thiên để tìm tiệm cận ngang, nhìn dấu hai vạch tiến ra vô cực để tìm tiệm cận đứng.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Xác định tiệm cận từ bảng biến thiên",
                        "problem": "Bảng biến thiên có $\\lim_{x \\to \\pm\\infty} y = 2$; $\\lim_{x \\to -1^-} y = +\\infty$ và $\\lim_{x \\to 1^+} y = +\\infty$. Đồ thị có bao nhiêu tiệm cận?",
                        "solution": "Đồ thị có 1 tiệm cận ngang $y = 2$ và 2 tiệm cận đứng $x = -1, x = 1$. Tổng cộng có 3 đường tiệm cận."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c4",
                    "title": "Bài tập tự giải",
                    "content": "Tổng số đường tiệm cận trong ví dụ trên bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 5: Bài toán chứa tham số": {
                "theory": "Biện luận số nghiệm của mẫu số không trùng với nghiệm của tử để xác định số lượng đường tiệm cận đứng theo tham số $m$.",
                "formula": "\\Delta_{mẫu} > 0 \\text{ và } \\text{nghiệm mẫu khác nghiệm tử}",
                "trap": "Quên điều kiện loại trừ nghiệm của mẫu làm tử số bằng 0.",
                "audio": "Khi chứa tham số, cần tìm điều kiện để mẫu có nghiệm phân biệt và các nghiệm đó không làm triệt tiêu tử số.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm m để có số tiệm cận cho trước",
                        "problem": "Tìm $m$ để đồ thị $y = \\frac{2x + 1}{x^2 - 2x + m}$ có đúng 2 đường tiệm cận.",
                        "solution": "Đồ thị luôn có TCN $y = 0$. Cần có đúng 1 TCĐ $\\iff$ mẫu có nghiệm kép ($m = 1$) hoặc mẫu có 2 nghiệm trong đó 1 nghiệm là $x = -1/2$ ($m = -5/4$)."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c5",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị m nguyên dương để đồ thị có đúng 2 tiệm cận là:",
                    "target": "1"
                }
            },
            "Chủ điểm 6: Ứng dụng thực tế": {
                "theory": "Hiện tượng giới hạn bão hòa nồng độ thuốc hoặc chi phí làm sạch môi trường tăng vọt vô hạn được mô tả bởi các đường tiệm cận.",
                "formula": "\\lim_{p \\to 100^-} C(p) = +\\infty",
                "trap": "Nhầm đơn vị thời gian hoặc đơn vị tiền tệ trong các bài toán thực tế.",
                "audio": "Tiệm cận đứng trong thực tế biểu thị một giới hạn không thể vượt qua, ví dụ chi phí làm sạch ô nhiễm tiến ra vô cực khi độ sạch đạt 100%.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Giới hạn nồng độ thuốc trong máu",
                        "problem": "Nồng độ thuốc sau $t$ giờ là $C(t) = \\frac{20t}{t + 4}$ (mg/lít). Khi $t$ tăng vô hạn, nồng độ tiến gần tới bao nhiêu?",
                        "solution": "Ta có $\\lim_{t \\to +\\infty} \\frac{20t}{t + 4} = 20$. Nồng độ thuốc tiến gần tới 20 mg/lít."
                    }
                ],
                "exercise": {
                    "id": "12_b3_c6",
                    "title": "Bài tập tự giải",
                    "content": "Nồng độ thuốc tối đa (mg/lít) tiến đến là:",
                    "target": "20"
                }
            }
        }
    },

    "Bài 4. Khảo sát sự biến thiên và vẽ đồ thị của hàm số": {
        "chapter": "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Sơ đồ khảo sát và vẽ đồ thị hàm số": {
                "theory": "Sơ đồ chuẩn 3 bước:\n1. Tìm tập xác định.\n2. Khảo sát sự biến thiên (tính $y'$, tìm cực trị, tìm tiệm cận nếu có, lập BBT).\n3. Vẽ đồ thị (xác định giao điểm với $Ox, Oy$, tâm đối xứng).",
                "formula": "\\text{TXĐ} \\to y' \\to \\text{Cực trị/Tiệm cận} \\to \\text{BBT} \\to \\text{Đồ thị}",
                "trap": "Quên tìm tọa độ giao điểm với các trục tọa độ trước khi vẽ đồ thị.",
                "audio": "Khảo sát hàm số gồm 3 bước: tập xác định, sự biến thiên và vẽ đồ thị đi qua các điểm đặc biệt.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ: Khảo sát hàm số bậc ba",
                        "problem": "Khảo sát sự biến thiên và vẽ đồ thị hàm số $y = x^3 - 3x^2 + 4$.",
                        "solution": "TXĐ: $\\mathbb{R}$. $y' = 3x(x - 2) = 0 \\iff x = 0$ hoặc $x = 2$.\nHàm đồng biến trên $(-\\infty; 0)$ và $(2; +\\infty)$, nghịch biến trên $(0; 2)$. Cực đại $(0; 4)$, cực tiểu $(2; 0)$. Tâm đối xứng là điểm uốn $I(1; 2)$."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c1",
                    "title": "Bài tập tự giải",
                    "content": "Tung độ tâm đối xứng của đồ thị hàm số $y = x^3 - 3x^2 + 4$ là:",
                    "target": "2"
                }
            },
            "Chủ điểm 2: Khảo sát hàm số bậc ba y = ax^3 + bx^2 + cx + d (a ≠ 0)": {
                "theory": "- Đồ thị có 2 cực trị khi $y'=0$ có 2 nghiệm phân biệt, không có cực trị khi $\\Delta'_{y'} \\le 0$.\n- Luôn nhận điểm uốn $I(x_0; y_0)$ với $y''(x_0) = 0$ làm tâm đối xứng.",
                "formula": "y'' = 6ax + 2b = 0 \\implies x_0 = -\\frac{b}{3a}",
                "trap": "Hàm bậc ba chỉ có 2 cực trị hoặc không có cực trị nào, không bao giờ có đúng 1 cực trị.",
                "audio": "Đồ thị hàm bậc ba luôn nhận điểm uốn có đạo hàm cấp hai bằng không làm tâm đối xứng.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ: Tâm đối xứng hàm bậc ba",
                        "problem": "Tìm tâm đối xứng của đồ thị $y = -x^3 + 3x^2 - 3x + 2$.",
                        "solution": "$y' = -3(x - 1)^2 \\le 0$. $y'' = -6x + 6 = 0 \\iff x = 1 \\implies y(1) = 1$. Tâm đối xứng là $I(1; 1)$."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c2",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ tâm đối xứng của hàm số $y = x^3 - 6x^2 + 1$ là:",
                    "target": "2"
                }
            },
            "Chủ điểm 3: Khảo sát hàm phân thức bậc nhất/bậc nhất y = (ax+b)/(cx+d)": {
                "theory": "- Đạo hàm $y' = \\frac{ad - bc}{(cx + d)^2}$: luôn đồng biến hoặc luôn nghịch biến trên từng khoảng xác định. Không có cực trị.\n- Tiệm cận đứng $x = -d/c$, tiệm cận ngang $y = a/c$. Giao điểm 2 tiệm cận là tâm đối xứng.",
                "formula": "I\\left(-\\frac{d}{c}; \\frac{a}{c}\\right) \\text{ là tâm đối xứng}",
                "trap": "Hàm phân thức bậc nhất trên bậc nhất không bao giờ có cực trị.",
                "audio": "Hàm phân thức bậc nhất trên bậc nhất có đồ thị hypebol, nhận giao điểm hai đường tiệm cận làm tâm đối xứng.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tâm đối xứng đồ thị hypebol",
                        "problem": "Tìm tâm đối xứng của đồ thị $y = \\frac{x + 2}{x - 1}$.",
                        "solution": "TCĐ là $x = 1$, TCN là $y = 1$. Do đó giao điểm $I(1; 1)$ là tâm đối xứng."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ tâm đối xứng của đồ thị $y = \\frac{3x + 1}{x - 2}$ bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 4: Khảo sát hàm phân thức bậc hai/bậc nhất": {
                "theory": "Chia đa thức $y = mx + n + \\frac{r}{dx + e}$. Tiệm cận đứng $x = -e/d$, tiệm cận xiên $y = mx + n$. Tâm đối xứng là giao điểm hai tiệm cận.",
                "formula": "y = mx + n \\text{ (TCX)}; \\quad x = -\\frac{e}{d} \\text{ (TCĐ)}",
                "trap": "Cực đại của hàm phân thức bậc hai trên bậc nhất có thể có giá trị nhỏ hơn cực tiểu.",
                "audio": "Đồ thị hàm phân thức bậc hai trên bậc nhất có một tiệm cận đứng và một tiệm cận xiên cắt nhau tại tâm đối xứng.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ: Khảo sát hàm phân thức bậc hai trên bậc nhất",
                        "problem": "Tìm tâm đối xứng của đồ thị $y = \\frac{x^2 + x - 1}{x + 2}$.",
                        "solution": "Chia tử cho mẫu: $y = x - 1 + \\frac{1}{x + 2}$. TCĐ là $x = -2$, TCX là $y = x - 1$. Thay $x = -2$ vào TCX được $y = -3$. Tâm đối xứng là $I(-2; -3)$."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c4",
                    "title": "Bài tập tự giải",
                    "content": "Tung độ tâm đối xứng trong ví dụ trên bằng:",
                    "target": "-3"
                }
            },
            "Chủ điểm 5: Ứng dụng đồ thị: nhận dạng, tương giao, biện luận nghiệm": {
                "theory": "- Số nghiệm của phương trình $f(x) = m$ bằng số giao điểm của đồ thị $y = f(x)$ với đường thẳng $y = m$.\n- Nhận dạng hệ số: nhánh phải cùng xác định dấu $a$, giao với $Oy$ xác định hệ số tự do.",
                "formula": "f(x) = m \\iff \\text{số giao điểm với } y = m",
                "trap": "Nhầm dấu các hệ số khi đọc đồ thị do nhầm chiều các trục tọa độ.",
                "audio": "Biện luận số nghiệm phương trình bằng cách cho đường thẳng nằm ngang y = m tịnh tiến cắt đồ thị.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ: Biện luận số nghiệm",
                        "problem": "Phương trình $x^3 - 3x^2 + 4 = m$ có 3 nghiệm phân biệt khi nào?",
                        "solution": "Đồ thị có cực tiểu tại 0 và cực đại tại 4. Đường thẳng $y = m$ cắt đồ thị tại 3 điểm khi $0 < m < 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c5",
                    "title": "Bài tập tự giải",
                    "content": "Số nghiệm của phương trình $x^3 - 3x^2 + 4 = 2$ là:",
                    "target": "3"
                }
            },
            "Chủ điểm 6: Ứng dụng thực tế": {
                "theory": "Sử dụng đạo hàm tìm thời điểm chất điểm đổi chiều chuyển động hoặc đạt vận tốc triệt tiêu.",
                "formula": "v(t) = s'(t) = 0 \\implies \\text{thời điểm đổi chiều}",
                "trap": "Nhầm lẫn giữa vận tốc bằng 0 với quãng đường bằng 0.",
                "audio": "Khi vận tốc đổi dấu thì chất điểm đổi chiều chuyển động.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ: Thời điểm đổi chiều chuyển động",
                        "problem": "Chất điểm có $s(t) = t^3 - 6t^2 + 9t$ ($t \\ge 0$). Tìm thời điểm vật đổi chiều.",
                        "solution": "$v(t) = s'(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3) = 0 \\iff t = 1$ hoặc $t = 3$. Tại hai thời điểm này vận tốc đổi dấu nên chất điểm đổi chiều."
                    }
                ],
                "exercise": {
                    "id": "12_b4_c6",
                    "title": "Bài tập tự giải",
                    "content": "Thời điểm đầu tiên vật đổi chiều là t bằng mấy giây?",
                    "target": "1"
                }
            }
        }
    },

    "Bài 5. Ứng dụng đạo hàm để giải quyết một số vấn đề liên quan đến thực tiễn": {
        "chapter": "Chương I. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Quy trình giải bài toán tối ưu trong thực tiễn": {
                "theory": "Quy trình 4 bước:\n1. Chọn ẩn $x$ và tìm điều kiện thực tế.\n2. Thiết lập hàm mục tiêu $y = f(x)$.\n3. Khảo sát hàm số tìm $\\max/\\min$.\n4. Kết luận kèm đơn vị đo.",
                "formula": "v(t) = s'(t); \\quad a(t) = v'(t) = s''(t)",
                "trap": "Không đặt đúng điều kiện cho ẩn số theo ý nghĩa hình học hoặc thực tế.",
                "audio": "Đạo hàm biểu thị tốc độ thay đổi tức thời của một đại lượng thực tiễn.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Gấp hộp từ tấm tôn vuông",
                        "problem": "Từ tấm tôn vuông cạnh 30 cm, cắt 4 góc vuông cạnh $x$ rồi gập thành hộp không nắp. Tìm $x$ để thể tích lớn nhất.",
                        "solution": "$V(x) = x(30 - 2x)^2$ với $0 < x < 15$. $V'(x) = 0 \\iff x = 5$. Thể tích lớn nhất bằng 2000 cm3."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c1",
                    "title": "Bài tập tự giải",
                    "content": "Độ dài cạnh cắt x (cm) trong bài toán trên bằng:",
                    "target": "5"
                }
            },
            "Chủ điểm 2: Bài toán tối ưu hình học: diện tích, thể tích": {
                "theory": "Tối ưu hóa hình trụ, hình hộp chữ nhật để tiết kiệm diện tích toàn phần vật liệu.",
                "formula": "V = \\pi r^2 h; \\quad S_{tp} = 2\\pi r^2 + 2\\pi rh",
                "trap": "Quên phân biệt hộp có nắp (2 đáy) và hộp không nắp (1 đáy).",
                "audio": "Với lon hình trụ có nắp, diện tích toàn phần nhỏ nhất khi chiều cao gấp đôi bán kính đáy.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Thiết kế lon nước ngọt tiết kiệm",
                        "problem": "Lon hình trụ có thể tích $16\\pi$ cm3. Tìm bán kính đáy $r$ để diện tích toàn phần nhỏ nhất.",
                        "solution": "$h = 16/r^2$. $S(r) = 2\\pi r^2 + \\frac{32\\pi}{r}$. $S'(r) = 0 \\iff r = 2$ cm."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c2",
                    "title": "Bài tập tự giải",
                    "content": "Bán kính r (cm) để tiết kiệm vật liệu nhất là:",
                    "target": "2"
                }
            },
            "Chủ điểm 3: Bài toán tối ưu kinh tế: doanh thu, chi phí, lợi nhuận": {
                "theory": "- Doanh thu: $R(x) = p \\cdot x$.\n- Lợi nhuận: $P(x) = R(x) - C(x)$.\n- Lợi nhuận cực đại khi đạo hàm $P'(x) = 0$.",
                "formula": "P(x) = R(x) - C(x) \\implies P'(x) = 0",
                "trap": "Nhầm lẫn giữa doanh thu cực đại và lợi nhuận cực đại.",
                "audio": "Lợi nhuận bằng doanh thu trừ chi phí. Đạo hàm bằng không sẽ cho lượng sản phẩm tối ưu.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Tối ưu doanh thu cho thuê phòng",
                        "problem": "Có 50 căn hộ cho thuê giá 2 triệu. Mỗi lần tăng 100 nghìn thì trống 1 căn. Tìm số lần tăng giá để doanh thu lớn nhất.",
                        "solution": "$R(x) = (2 + 0.1x)(50 - x) = 100 + 3x - 0.1x^2$. $R'(x) = 3 - 0.2x = 0 \\iff x = 15$."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c3",
                    "title": "Bài tập tự giải",
                    "content": "Số lần tăng giá x tối ưu là:",
                    "target": "15"
                }
            },
            "Chủ điểm 4: Chuyển động và tốc độ thay đổi": {
                "theory": "Độ cao cực đại đạt được khi vận tốc $v(t) = 0$. Tốc độ lây lan dịch bệnh cực đại khi đạo hàm cấp hai bằng 0.",
                "formula": "v(t) = h'(t) = 0 \\implies h_{max}",
                "trap": "Nhầm thời điểm đạt vận tốc lớn nhất với thời điểm đạt độ cao lớn nhất.",
                "audio": "Vật ném lên đạt độ cao lớn nhất khi vận tốc triệt tiêu.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Độ cao lớn nhất của vật",
                        "problem": "Độ cao vật ném lên là $h(t) = 20t - 5t^2$ (m). Tìm độ cao lớn nhất.",
                        "solution": "$v(t) = h'(t) = 20 - 10t = 0 \\iff t = 2$ s. Độ cao lớn nhất là $h(2) = 20$ m."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c4",
                    "title": "Bài tập tự giải",
                    "content": "Độ cao lớn nhất (m) của vật là:",
                    "target": "20"
                }
            },
            "Chủ điểm 5: Bài toán đường đi tối ưu (thời gian ngắn nhất)": {
                "theory": "Lập hàm thời gian $T(x) = \\frac{s_1}{v_1} + \\frac{s_2}{v_2}$ và giải phương trình $T'(x) = 0$.",
                "formula": "T(x) = \\frac{\\sqrt{d^2+x^2}}{v_1} + \\frac{L-x}{v_2}",
                "trap": "Quên lấy căn bậc hai khi tính quãng đường chéo bằng định lý Pytago.",
                "audio": "Bài toán đường đi ngắn nhất: lập hàm tổng thời gian theo quãng đường rẽ nhánh và giải đạo hàm bằng không.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ: Đi đường ngắn nhất kết hợp chèo thuyền và đi bộ",
                        "problem": "Cách bờ 3 km, chèo thuyền vận tốc 4 km/h đến điểm M trên bờ rồi đi bộ 5 km/h. Tìm $x = CM$ để thời gian ngắn nhất.",
                        "solution": "$T(x) = \\frac{\\sqrt{9 + x^2}}{4} + \\frac{8 - x}{5}$. $T'(x) = 0 \\iff 5x = 4\\sqrt{9 + x^2} \\iff x = 4$ km."
                    }
                ],
                "exercise": {
                    "id": "12_b5_c5",
                    "title": "Bài tập tự giải",
                    "content": "Khoảng cách x (km) tối ưu bằng:",
                    "target": "4"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG II. VECTƠ VÀ HỆ TRỤC TOẠ ĐỘ TRONG KHÔNG GIAN
    # =========================================================================
    "Bài 6. Vectơ trong không gian": {
        "chapter": "Chương II. Vectơ và hệ trục toạ độ trong không gian",
        "topics": {
            "Chủ điểm 1: Khái niệm vectơ trong không gian": {
                "theory": "Đoạn thẳng có hướng. Hai vectơ cùng phương nếu giá song song hoặc trùng nhau. Bằng nhau nếu cùng hướng và cùng độ dài.",
                "formula": "\\vec{BA} = -\\vec{AB}; \\quad |\\vec{AB}| = AB",
                "trap": "Hai vectơ có cùng độ dài nhưng khác hướng thì không bằng nhau.",
                "audio": "Vectơ trong không gian có đầy đủ các tính chất như trong hình học phẳng.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Vectơ trong hình lập phương",
                        "problem": "Trong hình lập phương $ABCD.A'B'C'D'$, tìm các vectơ bằng $\\vec{AB}$.",
                        "solution": "Ta có $\\vec{AB} = \\vec{DC} = \\vec{A'B'} = \\vec{D'C'}$."
                    }
                ],
                "exercise": {
                    "id": "12_b6_c1",
                    "title": "Bài tập tự giải",
                    "content": "Hình lập phương cạnh 2 có độ dài đường chéo mặt đáy AC bằng 2 căn mấy?",
                    "target": "2"
                }
            },
            "Chủ điểm 2: Tổng và hiệu của hai vectơ": {
                "theory": "- Quy tắc 3 điểm: $\\vec{AB} + \\vec{BC} = \\vec{AC}$.\n- Quy tắc hình hộp: $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$.\n- Trọng tâm tứ diện $G$: $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$.",
                "formula": "\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}",
                "trap": "Quy tắc hình hộp chỉ đúng khi 3 vectơ xuất phát từ cùng một đỉnh.",
                "audio": "Tổng 3 vectơ cạnh chung đỉnh của hình hộp bằng vectơ đường chéo xuất phát từ đỉnh đó.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Biểu diễn vectơ qua trọng tâm",
                        "problem": "Cho tứ diện $ABCD$, $G$ là trọng tâm $\\triangle BCD$. Rút gọn $\\vec{AB} + \\vec{AC} + \\vec{AD}$.",
                        "solution": "Vì $\\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$ nên $\\vec{AB} + \\vec{AC} + \\vec{AD} = 3\\vec{AG}$."
                    }
                ],
                "exercise": {
                    "id": "12_b6_c2",
                    "title": "Bài tập tự giải",
                    "content": "Hệ số k trong đẳng thức vectơ AB + AC + AD = k AG bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 3: Tích của một số với một vectơ": {
                "theory": "$k\\vec{a}$ cùng hướng $\\vec{a}$ nếu $k > 0$, ngược hướng nếu $k < 0$. $|k\\vec{a}| = |k||\\vec{a}|$.\nTính chất trung điểm: $\\vec{MN} = \\frac{1}{2}(\\vec{AC} + \\vec{BD})$.",
                "formula": "\\vec{a} \\parallel \\vec{b} \\iff \\vec{a} = k\\vec{b}",
                "trap": "Quên đổi chiều vectơ khi nhân với số âm.",
                "audio": "Phép nhân vectơ với một số cho ra vectơ cùng phương.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Vectơ đoạn nối trung điểm",
                        "problem": "Cho $M, N$ là trung điểm $AB$ và $CD$. Chứng minh $\\vec{MN} = \\frac{1}{2}(\\vec{AC} + \\vec{BD})$.",
                        "solution": "Cộng hai vế $\\vec{MN} = \\vec{MA} + \\vec{AC} + \\vec{CN}$ và $\\vec{MN} = \\vec{MB} + \\vec{BD} + \\vec{DN}$, do $M, N$ là trung điểm nên được điều phải chứng minh."
                    }
                ],
                "exercise": {
                    "id": "12_b6_c3",
                    "title": "Bài tập tự giải",
                    "content": "Cho vectơ a có độ dài 3. Độ dài vectơ -2a bằng:",
                    "target": "6"
                }
            },
            "Chủ điểm 4: Góc giữa hai vectơ và tích vô hướng": {
                "theory": "$\\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos(\\vec{a}, \\vec{b})$.\nHai vectơ vuông góc khi và chỉ khi tích vô hướng bằng 0.",
                "formula": "\\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos(\\vec{a}, \\vec{b}); \\quad \\vec{a} \\perp \\vec{b} \\iff \\vec{a} \\cdot \\vec{b} = 0",
                "trap": "Phải đưa về chung gốc mới xác định đúng góc xen giữa.",
                "audio": "Tích vô hướng bằng tích độ dài nhân cos góc xen giữa. Vuông góc thì tích vô hướng bằng không.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Cạnh đối diện vuông góc trong tứ diện đều",
                        "problem": "Cho tứ diện đều $ABCD$ cạnh $a$. Tính $\\vec{AB} \\cdot \\vec{CD}$.",
                        "solution": "$\\vec{AB} \\cdot (\\vec{AD} - \\vec{AC}) = \\vec{AB} \\cdot \\vec{AD} - \\vec{AB} \\cdot \\vec{AC} = \\frac{a^2}{2} - \\frac{a^2}{2} = 0 \\implies AB \\perp CD$."
                    }
                ],
                "exercise": {
                    "id": "12_b6_c4",
                    "title": "Bài tập tự giải",
                    "content": "Góc giữa hai cạnh đối diện trong tứ diện đều bằng bao nhiêu độ?",
                    "target": "90"
                }
            },
            "Chủ điểm 5: Ứng dụng vectơ trong vật lí": {
                "theory": "- Hợp lực: $\\vec{F} = \\vec{F}_1 + \\vec{F}_2$.\n- Công cơ học: $A = \\vec{F} \\cdot \\vec{s} = |\\vec{F}||\\vec{s}|\\cos\\varphi$.",
                "formula": "A = |\\vec{F}||\\vec{s}|\\cos\\varphi",
                "trap": "Góc phi là góc giữa lực tác dụng và hướng chuyển động của vật.",
                "audio": "Công của lực bằng tích vô hướng giữa vectơ lực và vectơ độ dịch chuyển.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Tính công cơ học",
                        "problem": "Kéo vật dịch chuyển 10 m bằng lực 20 N hợp phương ngang góc 60 độ. Tính công.",
                        "solution": "$A = 20 \\cdot 10 \\cdot \\cos 60^\\circ = 100$ J."
                    }
                ],
                "exercise": {
                    "id": "12_b6_c5",
                    "title": "Bài tập tự giải",
                    "content": "Công của lực kéo trong ví dụ trên bằng bao nhiêu Jun?",
                    "target": "100"
                }
            }
        }
    },

    "Bài 7. Hệ trục toạ độ trong không gian": {
        "chapter": "Chương II. Vectơ và hệ trục toạ độ trong không gian",
        "topics": {
            "Chủ điểm 1: Hệ trục toạ độ Oxyz": {
                "theory": "Ba trục $Ox, Oy, Oz$ đôi một vuông góc. Các vectơ đơn vị $\\vec{i}, \\vec{j}, \\vec{k}$ có độ dài bằng 1 và tích vô hướng từng đôi bằng 0.",
                "formula": "|\\vec{i}| = |\\vec{j}| = |\\vec{k}| = 1; \\quad \\vec{i} \\cdot \\vec{j} = \\vec{j} \\cdot \\vec{k} = \\vec{k} \\cdot \\vec{i} = 0",
                "trap": "Nhầm lẫn giữa trục tung Oy và trục cao Oz.",
                "audio": "Hệ toạ độ Oxyz gồm trục hoành Ox, trục tung Oy và trục cao Oz đôi một vuông góc tại gốc O.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tọa độ đỉnh hình hộp chữ nhật",
                        "problem": "Hình hộp chữ nhật có 3 cạnh trên các trục tọa độ với $A(2;0;0), B(0;3;0), C(0;0;3)$. Tìm đỉnh đối diện gốc $O$.",
                        "solution": "Đỉnh đối diện gốc tọa độ là $M(2; 3; 3)$."
                    }
                ],
                "exercise": {
                    "id": "12_b7_c1",
                    "title": "Bài tập tự giải",
                    "content": "Cao độ z của điểm M trong ví dụ trên bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 2: Toạ độ của một điểm": {
                "theory": "$M(x; y; z) \\iff \\vec{OM} = x\\vec{i} + y\\vec{j} + z\\vec{k}$.\n- Chiếu lên $Oxy$: $(x; y; 0)$, chiếu lên $Ox$: $(x; 0; 0)$.\n- Đối xứng qua $Oxy$: $(x; y; -z)$, qua gốc $O$: $(-x; -y; -z)$.",
                "formula": "M(x; y; z) \\implies \\text{Chiếu lên } Oxy: (x; y; 0)",
                "trap": "Chiếu lên mặt phẳng hoặc trục nào thì giữ nguyên tọa độ đó, các tọa độ còn lại bằng 0.",
                "audio": "Hình chiếu lên trục hay mặt phẳng nào thì chỉ giữ lại chữ cái của trục hoặc mặt phẳng đó.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm hình chiếu và đối xứng",
                        "problem": "Cho $M(2; -3; 4)$. Tìm hình chiếu lên $Oxy$ và điểm đối xứng qua gốc $O$.",
                        "solution": "Hình chiếu lên $Oxy$ là $(2; -3; 0)$. Đối xứng qua gốc $O$ là $(-2; 3; -4)$."
                    }
                ],
                "exercise": {
                    "id": "12_b7_c2",
                    "title": "Bài tập tự giải",
                    "content": "Cao độ z của hình chiếu điểm M(2; -3; 4) lên mặt phẳng Oxy là:",
                    "target": "0"
                }
            },
            "Chủ điểm 3: Toạ độ của vectơ": {
                "theory": "$\\vec{a} = x\\vec{i} + y\\vec{j} + z\\vec{k} \\iff \\vec{a} = (x; y; z)$.\nVectơ $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)$.",
                "formula": "\\vec{AB} = (x_B - x_A; \\ y_B - y_A; \\ z_B - z_A)",
                "trap": "Lấy nhầm tọa độ điểm đầu trừ điểm cuối thay vì điểm cuối trừ điểm đầu.",
                "audio": "Tọa độ vectơ AB bằng tọa độ điểm B trừ đi tọa độ điểm A tương ứng.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm tọa độ vectơ",
                        "problem": "Cho $A(1; -2; 3)$ và $B(4; 0; -1)$. Tính $\\vec{AB}$.",
                        "solution": "$\\vec{AB} = (4 - 1; 0 - (-2); -1 - 3) = (3; 2; -4)$."
                    }
                ],
                "exercise": {
                    "id": "12_b7_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ của vectơ AB trong ví dụ trên bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 4: Đặt hệ trục toạ độ vào hình hộp chữ nhật – mô hình hoá": {
                "theory": "Chọn gốc tọa độ tại một đỉnh, 3 tia dọc theo 3 cạnh vuông góc xuất phát từ đỉnh đó để chuyển bài toán không gian sang tọa độ.",
                "formula": "A(0;0;0), \\ B(a;0;0), \\ D(0;b;0), \\ A'(0;0;c)",
                "trap": "Xác định nhầm thứ tự các trục khi gán số liệu thực tế.",
                "audio": "Gắn hệ trục Oxyz vào một góc tường của căn phòng giúp dễ dàng định vị các thiết bị trong không gian.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Vị trí bóng đèn trong phòng",
                        "problem": "Phòng kích thước $8 \\times 6 \\times 3$ m. Bóng đèn treo chính giữa trần nhà. Tìm tọa độ bóng đèn.",
                        "solution": "Tâm trần nhà có tọa độ: $x = 8/2 = 4, y = 6/2 = 3, z = 3$. Vậy tọa độ đèn là $(4; 3; 3)$."
                    }
                ],
                "exercise": {
                    "id": "12_b7_c4",
                    "title": "Bài tập tự giải",
                    "content": "Cao độ z của bóng đèn treo ở trần phòng cao 3m là:",
                    "target": "3"
                }
            }
        }
    },

    "Bài 8. Biểu thức toạ độ của các phép toán vectơ": {
        "chapter": "Chương II. Vectơ và hệ trục toạ độ trong không gian",
        "topics": {
            "Chủ điểm 1: Toạ độ của tổng, hiệu và tích của một số với một vectơ": {
                "theory": "Cho $\\vec{a} = (a_1; a_2; a_3), \\vec{b} = (b_1; b_2; b_3)$:\n- $\\vec{a} \\pm \\vec{b} = (a_1 \\pm b_1; a_2 \\pm b_2; a_3 \\pm b_3)$.\n- $k\\vec{a} = (ka_1; ka_2; ka_3)$.\n- Cùng phương khi các tọa độ tỉ lệ.",
                "formula": "k\\vec{a} = (ka_1; ka_2; ka_3); \\quad \\frac{a_1}{b_1} = \\frac{a_2}{b_2} = \\frac{a_3}{b_3}",
                "trap": "Quên nhân phân phối hệ số k cho cả 3 thành phần tọa độ.",
                "audio": "Cộng trừ hai vectơ ta cộng trừ các tọa độ tương ứng. Nhân vectơ với một số ta nhân số đó vào từng tọa độ.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tính tọa độ vectơ kết hợp",
                        "problem": "Cho $\\vec{a} = (2; -1; 3)$ và $\\vec{b} = (1; 4; -2)$. Tính $2\\vec{a} - 3\\vec{b}$.",
                        "solution": "$2\\vec{a} = (4; -2; 6), 3\\vec{b} = (3; 12; -6)$. $2\\vec{a} - 3\\vec{b} = (1; -14; 12)$."
                    }
                ],
                "exercise": {
                    "id": "12_b8_c1",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ của vectơ 2a - 3b trong ví dụ trên bằng:",
                    "target": "1"
                }
            },
            "Chủ điểm 2: Biểu thức toạ độ của tích vô hướng, độ dài, khoảng cách, góc": {
                "theory": "- Tích vô hướng: $\\vec{a} \\cdot \\vec{b} = a_1b_1 + a_2b_2 + a_3b_3$.\n- Độ dài: $|\\vec{a}| = \\sqrt{a_1^2 + a_2^2 + a_3^2}$.\n- Khoảng cách: $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.\n- Vuông góc khi $\\vec{a} \\cdot \\vec{b} = 0$.",
                "formula": "\\vec{a} \\cdot \\vec{b} = a_1b_1 + a_2b_2 + a_3b_3; \\quad |\\vec{a}| = \\sqrt{a_1^2 + a_2^2 + a_3^2}",
                "trap": "Bình phương số âm quên đóng ngoặc dẫn đến tính sai khoảng cách.",
                "audio": "Tích vô hướng bằng hoành nhân hoành cộng tung nhân tung cộng cao nhân cao.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tính tích vô hướng và độ dài",
                        "problem": "Cho $\\vec{a} = (1; -2; 2), \\vec{b} = (2; 1; -2)$. Tính $\\vec{a} \\cdot \\vec{b}$ và độ dài $|\\vec{a}|$.",
                        "solution": "$\\vec{a} \\cdot \\vec{b} = 1(2) + (-2)(1) + 2(-2) = -4$. $|\\vec{a}| = \\sqrt{1 + 4 + 4} = 3$."
                    }
                ],
                "exercise": {
                    "id": "12_b8_c2",
                    "title": "Bài tập tự giải",
                    "content": "Độ dài của vectơ a = (1; -2; 2) bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 3: Toạ độ trung điểm và trọng tâm": {
                "theory": "- Trung điểm $M$ của $AB$: $M\\left(\\frac{x_A+x_B}{2}; \\frac{y_A+y_B}{2}; \\frac{z_A+z_B}{2}\\right)$.\n- Trọng tâm $G$ của $\\triangle ABC$: $G\\left(\\frac{x_A+x_B+x_C}{3}; \\frac{y_A+y_B+y_C}{3}; \\frac{z_A+z_B+z_C}{3}\\right)$.",
                "formula": "x_M = \\frac{x_A+x_B}{2}; \\quad x_G = \\frac{x_A+x_B+x_C}{3}",
                "trap": "Trung điểm chia 2 nhưng trọng tâm tam giác phải chia cho 3.",
                "audio": "Tọa độ trung điểm bằng trung bình cộng 2 đầu mút, tọa độ trọng tâm tam giác bằng trung bình cộng 3 đỉnh.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm trung điểm",
                        "problem": "Cho $A(2; -1; 3)$ và $B(4; 3; -1)$. Tìm tọa độ trung điểm $M$.",
                        "solution": "$M = \\left(\\frac{2+4}{2}; \\frac{-1+3}{2}; \\frac{3-1}{2}\\right) = (3; 1; 1)$."
                    }
                ],
                "exercise": {
                    "id": "12_b8_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ trung điểm M của AB trong ví dụ trên là:",
                    "target": "3"
                }
            },
            "Chủ điểm 4: Ứng dụng: lực, công, chuyển động trong không gian": {
                "theory": "- Công của lực không đổi $\\vec{F}$ dịch chuyển vật dọc theo $\\vec{AB}$: $A = \\vec{F} \\cdot \\vec{AB}$.\n- Vị trí sau $t$ giây với vận tốc $\\vec{v}$: $\\vec{OM}(t) = \\vec{OM}_0 + t\\vec{v}$.",
                "formula": "A = \\vec{F} \\cdot \\vec{AB} = F_x \\Delta x + F_y \\Delta y + F_z \\Delta z",
                "trap": "Quên kiểm tra tính đồng bộ của đơn vị đo (mét, Newton, Jun).",
                "audio": "Công của lực trong không gian bằng tích vô hướng giữa vectơ lực và vectơ độ dịch chuyển.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tính công của lực",
                        "problem": "Lực $\\vec{F} = (2; 3; 1)$ (N) làm dịch chuyển từ $A(1; 1; 1)$ đến $B(4; 5; 3)$ (m). Tính công.",
                        "solution": "$\\vec{AB} = (3; 4; 2)$. Công $A = 2(3) + 3(4) + 1(2) = 20$ J."
                    }
                ],
                "exercise": {
                    "id": "12_b8_c4",
                    "title": "Bài tập tự giải",
                    "content": "Công của lực kéo trong ví dụ trên bằng bao nhiêu Jun?",
                    "target": "20"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG III. CÁC SỐ ĐẶC TRƯNG ĐO MỨC ĐỘ PHÂN TÁN CHO MẪU GHÉP NHÓM
    # =========================================================================
    "Bài 9. Khoảng biến thiên, khoảng tứ phân vị": {
        "chapter": "Chương III. Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "topics": {
            "Chủ điểm 1: Mẫu số liệu ghép nhóm và khoảng biến thiên": {
                "theory": "Khoảng biến thiên $R$ là hiệu giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên:\n$$R = a_{m+1} - a_1$$",
                "formula": "R = a_{m+1} - a_1",
                "trap": "Nhầm giá trị đại diện với đầu mút biên của nhóm.",
                "audio": "Khoảng biến thiên bằng đầu mút phải của nhóm lớn nhất trừ đi đầu mút trái của nhóm nhỏ nhất.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính khoảng biến thiên",
                        "problem": "Các nhóm $[0; 10), [10; 20), \\dots, [40; 50)$. Tìm $R$.",
                        "solution": "$R = 50 - 0 = 50$."
                    }
                ],
                "exercise": {
                    "id": "12_b9_c1",
                    "title": "Bài tập tự giải",
                    "content": "Khoảng biến thiên R của mẫu ghép nhóm trên bằng:",
                    "target": "50"
                }
            },
            "Chủ điểm 2: Khoảng tứ phân vị": {
                "theory": "Công thức tứ phân vị: $Q_k = u_m + \\frac{\\frac{kn}{4} - C}{n_m}(u_{m+1} - u_m)$.\nKhoảng tứ phân vị: $\\Delta_Q = Q_3 - Q_1$.",
                "formula": "\\Delta_Q = Q_3 - Q_1",
                "trap": "Cộng dồn tần số tích luỹ $C$ sai dẫn đến chọn sai nhóm chứa tứ phân vị.",
                "audio": "Khoảng tứ phân vị bằng tứ phân vị thứ 3 trừ đi tứ phân vị thứ nhất, đo độ phân tán của 50% số liệu chính giữa.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính khoảng tứ phân vị",
                        "problem": "Mẫu có $Q_1 = 17.5$ và $Q_3 = 32.5$. Tính $\\Delta_Q$.",
                        "solution": "$\\Delta_Q = 32.5 - 17.5 = 15$."
                    }
                ],
                "exercise": {
                    "id": "12_b9_c2",
                    "title": "Bài tập tự giải",
                    "content": "Khoảng tứ phân vị trong ví dụ trên bằng:",
                    "target": "15"
                }
            },
            "Chủ điểm 3: Ý nghĩa và so sánh mức độ phân tán": {
                "theory": "- $\\Delta_Q$ đo độ phân tán của 50% số liệu ở giữa, ít bị ảnh hưởng bởi giá trị ngoại lệ bất thường hơn $R$.\n- Mẫu có $\\Delta_Q$ lớn hơn thì độ phân tán lớn hơn.",
                "formula": "\\Delta_Q \\text{ lớn hơn} \\implies \\text{phân tán hơn}",
                "trap": "Cho rằng hai mẫu có cùng khoảng biến thiên R thì độ phân tán giống nhau.",
                "audio": "Khoảng tứ phân vị ưu việt hơn khoảng biến thiên vì không bị sai lệch bởi các giá trị bất thường quá lớn hay quá bé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: So sánh độ phân tán",
                        "problem": "Lớp 12A có $\\Delta_Q = 18$, lớp 12B có $\\Delta_Q = 20$. Lớp nào phân tán hơn?",
                        "solution": "Lớp 12B có khoảng tứ phân vị lớn hơn nên điểm số phân tán hơn."
                    }
                ],
                "exercise": {
                    "id": "12_b9_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hiệu khoảng tứ phân vị giữa lớp 12B và 12A bằng:",
                    "target": "2"
                }
            }
        }
    },

    "Bài 10. Phương sai, độ lệch chuẩn": {
        "chapter": "Chương III. Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "topics": {
            "Chủ điểm 1: Giá trị đại diện và số trung bình của mẫu số liệu ghép nhóm": {
                "theory": "Giá trị đại diện $c_i = \\frac{a_i + a_{i+1}}{2}$.\nSố trung bình: $\\overline{x} = \\frac{1}{n} \\sum m_i c_i$.",
                "formula": "c_i = \\frac{a_i+a_{i+1}}{2}; \\quad \\overline{x} = \\frac{1}{n}\\sum m_i c_i",
                "trap": "Quên nhân tần số $m_i$ với giá trị đại diện khi tính số trung bình.",
                "audio": "Giá trị đại diện của nhóm là trung điểm của hai đầu mút của nhóm đó.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính số trung bình",
                        "problem": "Nhóm $[0; 2)$ có tần số 2, $[2; 4)$ có tần số 4, $[4; 6)$ có tần số 3, $[6; 8)$ có 1. Tìm $\\overline{x}$.",
                        "solution": "Giá trị đại diện: 1, 3, 5, 7. $\\overline{x} = \\frac{2(1) + 4(3) + 3(5) + 1(7)}{10} = 3.6$."
                    }
                ],
                "exercise": {
                    "id": "12_b10_c1",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị đại diện của nhóm [4; 6) bằng:",
                    "target": "5"
                }
            },
            "Chủ điểm 2: Phương sai và độ lệch chuẩn": {
                "theory": "Phương sai: $s^2 = \\frac{1}{n}\\sum m_i c_i^2 - \\overline{x}^2$.\nĐộ lệch chuẩn: $s = \\sqrt{s^2}$.",
                "formula": "s^2 = \\frac{1}{n}\\sum m_i c_i^2 - \\overline{x}^2; \\quad s = \\sqrt{s^2}",
                "trap": "Nhầm lẫn giữa phương sai $s^2$ và độ lệch chuẩn $s$.",
                "audio": "Độ lệch chuẩn là căn bậc hai của phương sai và có cùng đơn vị với số liệu ban đầu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính phương sai",
                        "problem": "Mẫu có $\\overline{x} = 3.6$, $\\frac{1}{n}\\sum m_i c_i^2 = 16.2$. Tính $s^2$ và $s$.",
                        "solution": "$s^2 = 16.2 - 3.6^2 = 3.24 \\implies s = \\sqrt{3.24} = 1.8$."
                    }
                ],
                "exercise": {
                    "id": "12_b10_c2",
                    "title": "Bài tập tự giải",
                    "content": "Độ lệch chuẩn s trong ví dụ trên bằng:",
                    "target": "1.8"
                }
            },
            "Chủ điểm 3: Ý nghĩa, so sánh và tính chất": {
                "theory": "- Độ lệch chuẩn càng nhỏ thì số liệu càng đồng đều, ổn định quanh số trung bình.\n- Cộng hằng số $c$: $\\overline{x}$ tăng $c$, $s$ không đổi.\n- Nhân hằng số $k$: $\\overline{x}$ nhân $k$, $s$ nhân $|k|$.",
                "formula": "y = x + c \\implies s_y = s_x; \\quad y = kx \\implies s_y = |k|s_x",
                "trap": "Nghĩ rằng cộng thêm một số vào tất cả số liệu sẽ làm độ lệch chuẩn thay đổi.",
                "audio": "Khi cộng thêm cùng một hằng số vào tất cả số liệu thì độ phân tán và độ lệch chuẩn không thay đổi.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính chất độ lệch chuẩn",
                        "problem": "Mẫu số liệu có $s = 1.8$. Nếu cộng thêm 10 vào mọi số liệu thì $s$ mới bằng bao nhiêu?",
                        "solution": "Độ lệch chuẩn không đổi, $s = 1.8$."
                    }
                ],
                "exercise": {
                    "id": "12_b10_c3",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị độ lệch chuẩn mới bằng:",
                    "target": "1.8"
                }
            },
            "Chủ điểm 4: Ứng dụng: so sánh sự ổn định – mô hình hoá": {
                "theory": "Xạ thủ hay dây chuyền sản xuất có độ lệch chuẩn nhỏ hơn thì hoạt động ổn định và chính xác hơn.",
                "formula": "s_A < s_B \\implies A \\text{ ổn định hơn } B",
                "trap": "Chỉ nhìn số trung bình mà quên so sánh độ lệch chuẩn khi đánh giá mức độ ổn định.",
                "audio": "Trong thể thao hay sản xuất, người có độ lệch chuẩn nhỏ hơn là người có phong độ ổn định hơn.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: So sánh độ ổn định 2 xạ thủ",
                        "problem": "Xạ thủ A có $s = 0.9$, xạ thủ B có $s = 0.83$. Ai bắn ổn định hơn?",
                        "solution": "Xạ thủ B có độ lệch chuẩn nhỏ hơn nên bắn ổn định hơn."
                    }
                ],
                "exercise": {
                    "id": "12_b10_c4",
                    "title": "Bài tập tự giải",
                    "content": "Độ lệch chuẩn của xạ thủ B (0.83) nhỏ hơn xạ thủ A đúng hay sai? Nhập 1 nếu đúng, 0 nếu sai:",
                    "target": "1"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG IV. NGUYÊN HÀM VÀ TÍCH PHÂN
    # =========================================================================
    "Bài 11. Nguyên hàm": {
        "chapter": "Chương IV. Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Khái niệm nguyên hàm": {
                "theory": "$F(x)$ là nguyên hàm của $f(x)$ nếu $F'(x) = f(x)$. Họ nguyên hàm: $\\int f(x)dx = F(x) + C$.",
                "formula": "\\int f(x)dx = F(x) + C",
                "trap": "Quên ghi hằng số cộng $C$ trong họ nguyên hàm.",
                "audio": "Nguyên hàm là phép toán ngược của đạo hàm. Mọi nguyên hàm chỉ sai khác nhau một hằng số C.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm nguyên hàm cơ bản",
                        "problem": "Tìm nguyên hàm của $f(x) = 2x - 3$.",
                        "solution": "$\\int (2x - 3)dx = x^2 - 3x + C$."
                    }
                ],
                "exercise": {
                    "id": "12_b11_c1",
                    "title": "Bài tập tự giải",
                    "content": "Nguyên hàm của f(x) = 2x là x mũ mấy?",
                    "target": "2"
                }
            },
            "Chủ điểm 2: Bảng nguyên hàm của một số hàm số thường gặp": {
                "theory": "- $\\int x^\\alpha dx = \\frac{x^{\\alpha+1}}{\\alpha+1} + C$ ($\\alpha \\ne -1$);\n- $\\int \\frac{1}{x}dx = \\ln|x| + C$;\n- $\\int e^x dx = e^x + C$; $\\int a^x dx = \\frac{a^x}{\\ln a} + C$;\n- $\\int \\cos x dx = \\sin x + C$; $\\int \\sin x dx = -\\cos x + C$.",
                "formula": "\\int \\sin x dx = -\\cos x + C; \\quad \\int \\cos x dx = \\sin x + C",
                "trap": "Hay nhầm lẫn dấu âm: nguyên hàm của $\\sin x$ là $-\\cos x$, khác với đạo hàm.",
                "audio": "Các em hết sức lưu ý: nguyên hàm của sin x có dấu trừ là trừ cos x.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Nguyên hàm lượng giác và đa thức",
                        "problem": "Tính $\\int (3x^2 - 2x + 1)dx$.",
                        "solution": "$x^3 - x^2 + x + C$."
                    }
                ],
                "exercise": {
                    "id": "12_b11_c2",
                    "title": "Bài tập tự giải",
                    "content": "Hệ số của x^3 trong nguyên hàm của 3x^2 bằng:",
                    "target": "1"
                }
            },
            "Chủ điểm 3: Nguyên hàm thoả điều kiện cho trước": {
                "theory": "Cho $F(x_0) = y_0$, sau khi tính nguyên hàm có chứa $C$, thay $x = x_0$ vào để tìm giá trị cụ thể của $C$.",
                "formula": "F(x_0) + C = y_0 \\implies C",
                "trap": "Thay nhầm giá trị biến vào hàm số ban đầu thay vì nguyên hàm.",
                "audio": "Khi biết một điểm mà đồ thị nguyên hàm đi qua, ta thay tọa độ vào để xác định chính xác hằng số C.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Xác định hằng số C",
                        "problem": "Tìm $F(x)$ biết $F'(x) = 4x^3 - 2x + 1$ và $F(1) = 3$.",
                        "solution": "$F(x) = x^4 - x^2 + x + C$. $F(1) = 1 - 1 + 1 + C = 3 \\implies C = 2$. Vậy $F(x) = x^4 - x^2 + x + 2$."
                    }
                ],
                "exercise": {
                    "id": "12_b11_c3",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị hằng số C tìm được bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 4: Ứng dụng nguyên hàm trong vật lí và thực tế": {
                "theory": "- $v(t) = \\int a(t)dt$; $s(t) = \\int v(t)dt$.\n- Chi phí sản xuất: $C(x) = \\int C'(x)dx$.",
                "formula": "s(t) = \\int v(t)dt; \\quad v(t) = \\int a(t)dt",
                "trap": "Quên cộng hằng số vận tốc ban đầu hoặc vị trí ban đầu.",
                "audio": "Trong cơ học, quãng đường là nguyên hàm của vận tốc, vận tốc là nguyên hàm của gia tốc.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm phương trình quãng đường",
                        "problem": "Vận tốc $v(t) = 3t^2 + 2$ (m/s). Ban đầu ở gốc tọa độ $s(0) = 0$. Tìm $s(2)$.",
                        "solution": "$s(t) = \\int (3t^2 + 2)dt = t^3 + 2t + C$. $s(0) = 0 \\implies C = 0$. $s(2) = 2^3 + 2(2) = 12$ m."
                    }
                ],
                "exercise": {
                    "id": "12_b11_c4",
                    "title": "Bài tập tự giải",
                    "content": "Quãng đường vật đi được sau 2 giây bằng bao nhiêu mét?",
                    "target": "12"
                }
            }
        }
    },

    "Bài 12. Tích phân": {
        "chapter": "Chương IV. Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Khái niệm tích phân và công thức Newton – Leibniz": {
                "theory": "Cho $f(x)$ liên tục trên $[a; b]$. Công thức Newton – Leibniz:\n$$\\int_a^b f(x)dx = F(b) - F(a) = F(x)\\Big|_a^b$$",
                "formula": "\\int_a^b f(x)dx = F(b) - F(a)",
                "trap": "Tính nhầm dấu $F(a) - F(b)$ thay vì cận trên trừ cận dưới.",
                "audio": "Tích phân bằng giá trị nguyên hàm tại cận trên trừ đi giá trị nguyên hàm tại cận dưới.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tính tích phân cơ bản",
                        "problem": "Tính $\\int_0^1 (2x + 3)dx$.",
                        "solution": "$(x^2 + 3x)\\Big|_0^1 = (1 + 3) - 0 = 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b12_c1",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị tích phân từ 0 đến 1 của (2x + 3)dx bằng:",
                    "target": "4"
                }
            },
            "Chủ điểm 2: Tính chất của tích phân": {
                "theory": "- $\\int_a^b = \\int_a^c + \\int_c^b$;\n- $\\int_a^b k f(x)dx = k \\int_a^b f(x)dx$;\n- $\\int_a^b f(x)dx = -\\int_b^a f(x)dx$.",
                "formula": "\\int_a^b = \\int_a^c + \\int_c^b; \\quad \\int_a^b = -\\int_b^a",
                "trap": "Đổi cận không đổi dấu tích phân.",
                "audio": "Tích phân có tính chất chèn cận liên tiếp và đổi cận thì phải đổi dấu.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Chèn cận tích phân",
                        "problem": "Cho $\\int_0^2 f = 3$ và $\\int_2^5 f = -1$. Tính $\\int_0^5 f$.",
                        "solution": "$\\int_0^5 f = \\int_0^2 f + \\int_2^5 f = 3 + (-1) = 2$."
                    }
                ],
                "exercise": {
                    "id": "12_b12_c2",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị của tích phân từ 0 đến 5 bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 3: Tính tích phân bằng bảng nguyên hàm": {
                "theory": "Sử dụng bảng nguyên hàm kết hợp phân tách hàm trị tuyệt đối $f(x)$ thành các đoạn dấu xác định.",
                "formula": "\\int_0^3 |x-1|dx = \\int_0^1 (1-x)dx + \\int_1^3 (x-1)dx",
                "trap": "Quên phá dấu giá trị tuyệt đối khi tính tích phân hàm chứa trị tuyệt đối.",
                "audio": "Khi gặp biểu thức chứa trị tuyệt đối, cần xét dấu và tách tích phân thành các đoạn con thích hợp.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Tích phân trị tuyệt đối",
                        "problem": "Tính $\\int_0^3 |x-1|dx$.",
                        "solution": "$\\int_0^1 (1-x)dx + \\int_1^3 (x-1)dx = \\frac{1}{2} + 2 = 2.5$."
                    }
                ],
                "exercise": {
                    "id": "12_b12_c3",
                    "title": "Bài tập tự giải",
                    "content": "Giá trị tích phân từ 0 đến 3 của |x - 1|dx bằng:",
                    "target": "2.5"
                }
            },
            "Chủ điểm 4: Ứng dụng của tích phân trong vật lí và thực tế": {
                "theory": "- Quãng đường: $s = \\int_{t_1}^{t_2} |v(t)|dt$.\n- Lượng biến thiên: $Q(t_2) - Q(t_1) = \\int_{t_1}^{t_2} Q'(t)dt$.",
                "formula": "s = \\int_{t_1}^{t_2} v(t)dt \\quad (v(t) \\ge 0)",
                "trap": "Khi vận tốc đổi chiều, phải tính tích phân của trị tuyệt đối vận tốc để tìm quãng đường.",
                "audio": "Quãng đường vật đi được trong khoảng thời gian từ t1 đến t2 chính là tích phân của vận tốc.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Lượng nước chảy vào bể",
                        "problem": "Nước chảy với tốc độ $Q'(t) = 3t^2$ (m3/h). Tính lượng nước chảy từ giờ 1 đến giờ 3.",
                        "solution": "$\\Delta Q = \\int_1^3 3t^2 dt = t^3\\Big|_1^3 = 27 - 1 = 26$ m3."
                    }
                ],
                "exercise": {
                    "id": "12_b12_c4",
                    "title": "Bài tập tự giải",
                    "content": "Lượng nước chảy vào bể (m3) bằng:",
                    "target": "26"
                }
            }
        }
    },

    "Bài 13. Ứng dụng hình học của tích phân": {
        "chapter": "Chương IV. Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Diện tích hình phẳng": {
                "theory": "- Giới hạn bởi $y = f(x)$, $Ox$, $x = a, x = b$: $S = \\int_a^b |f(x)|dx$.\n- Giới hạn bởi 2 đồ thị: $S = \\int_a^b |f(x) - g(x)|dx$.",
                "formula": "S = \\int_a^b |f(x) - g(x)|dx",
                "trap": "Quên tìm các giao điểm trung gian để xét dấu trị tuyệt đối.",
                "audio": "Diện tích hình phẳng bằng tích phân từ a đến b của trị tuyệt đối hiệu hai hàm số.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Diện tích giữa parabol và đường thẳng",
                        "problem": "Tính diện tích hình phẳng giới hạn bởi $y = x^2$ và $y = 2x$.",
                        "solution": "Hoành độ giao điểm: $x^2 = 2x \\iff x = 0, x = 2$. $S = \\int_0^2 (2x - x^2)dx = \\frac{4}{3}$."
                    }
                ],
                "exercise": {
                    "id": "12_b13_c1",
                    "title": "Bài tập tự giải",
                    "content": "Tử số của phân số tối giản diện tích trong ví dụ trên bằng:",
                    "target": "4"
                }
            },
            "Chủ điểm 2: Thể tích của vật thể": {
                "theory": "Vật thể cắt bởi mặt phẳng vuông góc với $Ox$ tại $x$ có diện tích thiết diện $S(x)$:\n$$V = \\int_a^b S(x)dx$$",
                "formula": "V = \\int_a^b S(x)dx",
                "trap": "Nhầm công thức vật thể tổng quát với thể tích tròn xoay (không có nhân pi).",
                "audio": "Thể tích vật thể bất kỳ bằng tích phân diện tích thiết diện cắt ngang.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Khối kim tự tháp thiết diện vuông",
                        "problem": "Thiết diện vuông có cạnh là $x$ với $0 \\le x \\le 3$. Tính thể tích.",
                        "solution": "$S(x) = x^2$. $V = \\int_0^3 x^2 dx = 9$."
                    }
                ],
                "exercise": {
                    "id": "12_b13_c2",
                    "title": "Bài tập tự giải",
                    "content": "Thể tích khối kim tự tháp trong ví dụ trên bằng:",
                    "target": "9"
                }
            },
            "Chủ điểm 3: Thể tích khối tròn xoay": {
                "theory": "Quay hình phẳng giới hạn bởi $y = f(x)$, $Ox$, $x = a, x = b$ quanh trục $Ox$:\n$$V = \\pi \\int_a^b [f(x)]^2 dx$$",
                "formula": "V = \\pi \\int_a^b [f(x)]^2 dx",
                "trap": "Quên nhân hằng số $\\pi$ ở ngoài hoặc quên bình phương hàm số.",
                "audio": "Thể tích khối tròn xoay có nhân thêm số pi ở ngoài và bình phương hàm số dưới dấu tích phân.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Khối tròn xoay căn thức",
                        "problem": "Quay hình phẳng giới hạn bởi $y = \\sqrt{x}, y = 0, x = 0, x = 4$ quanh $Ox$.",
                        "solution": "$V = \\pi \\int_0^4 (\\sqrt{x})^2 dx = \\pi \\int_0^4 x dx = 8\\pi$."
                    }
                ],
                "exercise": {
                    "id": "12_b13_c3",
                    "title": "Bài tập tự giải",
                    "content": "Hệ số k trong thể tích V = k.pi của khối tròn xoay trên là:",
                    "target": "8"
                }
            },
            "Chủ điểm 4: Ứng dụng: bài toán thực tế": {
                "theory": "Tính thể tích ly nước, thùng gỗ hay bồn chứa dạng khối tròn xoay trong thực tiễn.",
                "formula": "V = \\pi \\int_a^b [f(x)]^2 dx",
                "trap": "Đổi sai đơn vị từ dm3 (lít) sang m3 hoặc cm3.",
                "audio": "Mô hình hóa hình dáng vật thể thực tế bằng đường cong rồi dùng tích phân tính thể tích chính xác.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ: Thể tích quả bóng bàn",
                        "problem": "Bóng bàn hình cầu bán kính 2 cm. Tính thể tích bằng tích phân.",
                        "solution": "Nửa đường tròn $y = \\sqrt{4 - x^2}$ quay quanh $Ox$: $V = \\pi \\int_{-2}^2 (4 - x^2)dx = \\frac{32\\pi}{3}$ cm3."
                    }
                ],
                "exercise": {
                    "id": "12_b13_c4",
                    "title": "Bài tập tự giải",
                    "content": "Tử số phân số tối giản của thể tích trên (không tính pi) là:",
                    "target": "32"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG V. PHƯƠNG TRÌNH MẶT PHẲNG, ĐƯỜNG THẲNG, MẶT CẦU
    # =========================================================================
    "Bài 14. Phương trình mặt phẳng": {
        "chapter": "Chương V. Phương trình mặt phẳng, đường thẳng, mặt cầu trong không gian",
        "topics": {
            "Chủ điểm 1: Vectơ pháp tuyến của mặt phẳng": {
                "theory": "VTPT $\\vec{n} \\ne \\vec{0}$ vuông góc với mặt phẳng. Nếu biết 2 vectơ không cùng phương $\\vec{a}, \\vec{b}$ có giá song song hoặc nằm trên $(P)$ thì $\\vec{n} = [\\vec{a}, \\vec{b}]$.",
                "formula": "\\vec{n} = [\\vec{a}, \\vec{b}]",
                "trap": "Tính sai định thức khi tính tích có hướng.",
                "audio": "Tích có hướng của hai vectơ chỉ phương sẽ cho ta vectơ pháp tuyến vuông góc với mặt phẳng.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm VTPT từ cặp VTCP",
                        "problem": "Cho $\\vec{a} = (1; 2; -1)$ và $\\vec{b} = (2; -1; 3)$. Tìm VTPT $\\vec{n}$.",
                        "solution": "$[\\vec{a}, \\vec{b}] = (5; -5; -5)$. Chọn $\\vec{n} = (1; -1; -1)$."
                    }
                ],
                "exercise": {
                    "id": "12_b14_c1",
                    "title": "Bài tập tự giải",
                    "content": "Cao độ z của vectơ pháp tuyến tối giản (1; -1; z) là:",
                    "target": "-1"
                }
            },
            "Chủ điểm 2: Phương trình tổng quát của mặt phẳng": {
                "theory": "Mặt phẳng qua $M_0(x_0; y_0; z_0)$ có VTPT $\\vec{n} = (A; B; C)$:\n$$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0 \\iff Ax + By + Cz + D = 0$$\nĐoạn chắn qua $(a;0;0), (0;b;0), (0;0;c)$: $\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1$.",
                "formula": "A(x - x_0) + B(y - y_0) + C(z - z_0) = 0; \\quad \\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1",
                "trap": "Phương trình đoạn chắn vế phải luôn bằng 1, không bằng 0.",
                "audio": "Mặt phẳng cắt 3 trục tọa độ được viết rất nhanh bằng phương trình đoạn chắn.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Phương trình đoạn chắn",
                        "problem": "Mặt phẳng qua $A(1;0;0), B(0;2;0), C(0;0;3)$.",
                        "solution": "$\\frac{x}{1} + \\frac{y}{2} + \\frac{z}{3} = 1 \\iff 6x + 3y + 2z - 6 = 0$."
                    }
                ],
                "exercise": {
                    "id": "12_b14_c2",
                    "title": "Bài tập tự giải",
                    "content": "Hệ số tự do D của phương trình tổng quát trên là:",
                    "target": "-6"
                }
            },
            "Chủ điểm 3: Vị trí tương đối của hai mặt phẳng": {
                "theory": "Dựa vào tỉ lệ hai VTPT $\\vec{n}_1, \\vec{n}_2$:\n- Song song khi VTPT tỉ lệ nhưng hệ số tự do không cùng tỉ lệ;\n- Vuông góc khi $\\vec{n}_1 \\cdot \\vec{n}_2 = 0$.",
                "formula": "(P) \\perp (Q) \\iff A_1A_2 + B_1B_2 + C_1C_2 = 0",
                "trap": "Hai mặt phẳng trùng nhau nếu cả 4 hệ số đều cùng tỉ lệ.",
                "audio": "Hai mặt phẳng vuông góc với nhau khi tích vô hướng của hai vectơ pháp tuyến bằng không.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Xét vị trí vuông góc",
                        "problem": "Cho $(P): x - 2y + z - 1 = 0$ và $(R): x + y + z = 0$. Chứng minh $(P) \\perp (R)$.",
                        "solution": "$\\vec{n}_P \\cdot \\vec{n}_R = 1(1) + (-2)(1) + 1(1) = 0 \\implies (P) \\perp (R)$."
                    }
                ],
                "exercise": {
                    "id": "12_b14_c3",
                    "title": "Bài tập tự giải",
                    "content": "Tích vô hướng của 2 vectơ pháp tuyến trên bằng:",
                    "target": "0"
                }
            },
            "Chủ điểm 4: Khoảng cách từ một điểm đến mặt phẳng": {
                "theory": "$$d(M_0, (P)) = \\frac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}$$",
                "formula": "d(M_0, (P)) = \\frac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}",
                "trap": "Quên lấy giá trị tuyệt đối trên tử số.",
                "audio": "Khoảng cách từ điểm đến mặt phẳng bằng trị tuyệt đối khi thay tọa độ điểm chia cho độ dài vectơ pháp tuyến.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Tính khoảng cách",
                        "problem": "Tính khoảng cách từ $M(1; 2; -3)$ đến $(P): 2x - 2y + z + 3 = 0$.",
                        "solution": "$d = \\frac{|2(1) - 2(2) + (-3) + 3|}{\\sqrt{4 + 4 + 1}} = \\frac{|-2|}{3} = \\frac{2}{3}$."
                    }
                ],
                "exercise": {
                    "id": "12_b14_c4",
                    "title": "Bài tập tự giải",
                    "content": "Tử số của khoảng cách trên bằng:",
                    "target": "2"
                }
            }
        }
    },

    "Bài 15. Phương trình đường thẳng trong không gian": {
        "chapter": "Chương V. Phương trình mặt phẳng, đường thẳng, mặt cầu trong không gian",
        "topics": {
            "Chủ điểm 1: Vectơ chỉ phương và phương trình của đường thẳng": {
                "theory": "Đường thẳng qua $M_0(x_0; y_0; z_0)$ có VTCP $\\vec{u} = (a; b; c)$:\n- Tham số: $x = x_0 + at, y = y_0 + bt, z = z_0 + ct$.\n- Chính tắc: $\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c}$ ($abc \\ne 0$).",
                "formula": "\\begin{cases} x = x_0 + at \\\\ y = y_0 + bt \\\\ z = z_0 + ct \\end{cases}; \\quad \\frac{x-x_0}{a} = \\frac{y-y_0}{b} = \\frac{z-z_0}{c}",
                "trap": "Nếu một tọa độ của VTCP bằng 0 thì không viết được phương trình dạng chính tắc.",
                "audio": "Đường thẳng được xác định khi biết một điểm đi qua và một vectơ chỉ phương.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Viết phương trình tham số",
                        "problem": "Đường thẳng qua $A(1; 2; -1)$ có VTCP $\\vec{u} = (2; -1; 3)$.",
                        "solution": "$x = 1 + 2t, y = 2 - t, z = -1 + 3t$."
                    }
                ],
                "exercise": {
                    "id": "12_b15_c1",
                    "title": "Bài tập tự giải",
                    "content": "Hoành độ x của điểm thuộc đường thẳng khi t = 1 là:",
                    "target": "3"
                }
            },
            "Chủ điểm 2: Vị trí tương đối của hai đường thẳng": {
                "theory": "- Song song hoặc trùng nhau khi hai VTCP cùng phương.\n- Cắt nhau khi hệ phương trình tọa độ giao điểm có nghiệm duy nhất.\n- Chéo nhau khi hai VTCP không cùng phương và hệ giao điểm vô nghiệm.",
                "formula": "[\\vec{u}_1, \\vec{u}_2] \\cdot \\vec{M_1M_2} \\ne 0 \\implies \\text{chéo nhau}",
                "trap": "Trong không gian, hai đường thẳng không có điểm chung có thể song song hoặc chéo nhau.",
                "audio": "Hai đường thẳng không cùng phương và không cắt nhau trong không gian được gọi là hai đường thẳng chéo nhau.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Xét vị trí vuông góc",
                        "problem": "Cho $\\vec{u}_1 = (1; 1; -1)$ và $\\vec{u}_2 = (2; -1; 1)$. Chứng minh $d_1 \\perp d_2$.",
                        "solution": "$\\vec{u}_1 \\cdot \\vec{u}_2 = 1(2) + 1(-1) + (-1)(1) = 0 \\implies d_1 \\perp d_2$."
                    }
                ],
                "exercise": {
                    "id": "12_b15_c2",
                    "title": "Bài tập tự giải",
                    "content": "Tích vô hướng của 2 vectơ chỉ phương trên bằng:",
                    "target": "0"
                }
            },
            "Chủ điểm 3: Đường thẳng và mặt phẳng": {
                "theory": "Thay tọa độ tham số của đường thẳng $d$ vào phương trình mặt phẳng $(P)$:\n- 1 nghiệm $t$: cắt nhau;\n- Vô nghiệm: $d \\parallel (P)$;\n- Vô số nghiệm: $d \\subset (P)$.",
                "formula": "A(x_0+at) + B(y_0+bt) + C(z_0+ct) + D = 0 \\implies t",
                "trap": "Quên tìm tọa độ giao điểm sau khi đã giải ra giá trị tham số $t$.",
                "audio": "Để tìm giao điểm giữa đường thẳng và mặt phẳng, ta thay phương trình tham số của đường thẳng vào mặt phẳng.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm giao điểm",
                        "problem": "Tìm giao điểm của $d: x = 1+t, y = 2-2t, z = 3-t$ và $(P): 2x + y + z - 10 = 0$.",
                        "solution": "$2(1+t) + (2-2t) + (3-t) - 10 = 0 \\iff -3 - t = 0 \\iff t = -3$. Điểm giao là $(-2; 8; 6)$."
                    }
                ],
                "exercise": {
                    "id": "12_b15_c3",
                    "title": "Bài tập tự giải",
                    "content": "Cao độ z của giao điểm tìm được là:",
                    "target": "6"
                }
            },
            "Chủ điểm 4: Ứng dụng: chuyển động thẳng đều và bài toán thực tế": {
                "theory": "Vật chuyển động thẳng đều từ $M_0$ với vận tốc $\\vec{v}$ thì tọa độ sau $t$ giây là $M(t) = M_0 + t\\vec{v}$. Tốc độ là $|\\vec{v}|$.",
                "formula": "M(t) = M_0 + t\\vec{v}; \\quad v = |\\vec{v}| = \\sqrt{v_x^2+v_y^2+v_z^2}",
                "trap": "Nhầm lẫn giữa vận tốc (vectơ) và tốc độ (độ dài vô hướng).",
                "audio": "Chuyển động thẳng đều trong không gian có quỹ đạo là một đường thẳng với vectơ chỉ phương chính là vectơ vận tốc.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Tốc độ của drone",
                        "problem": "Drone xuất phát từ $A(0;0;10)$ bay đều với $\\vec{v} = (3; 4; 12)$ m/s. Tính tốc độ.",
                        "solution": "Tốc độ $v = \\sqrt{3^2 + 4^2 + 12^2} = \\sqrt{169} = 13$ m/s."
                    }
                ],
                "exercise": {
                    "id": "12_b15_c4",
                    "title": "Bài tập tự giải",
                    "content": "Tốc độ bay của drone trong ví dụ trên bằng bao nhiêu m/s?",
                    "target": "13"
                }
            }
        }
    },

    "Bài 16. Công thức tính góc trong không gian": {
        "chapter": "Chương V. Phương trình mặt phẳng, đường thẳng, mặt cầu trong không gian",
        "topics": {
            "Chủ điểm 1: Góc giữa hai đường thẳng": {
                "theory": "Góc $\\varphi$ giữa 2 đường thẳng có VTCP $\\vec{u}_1, \\vec{u}_2$ ($0^\\circ \\le \\varphi \\le 90^\\circ$):\n$$\\cos \\varphi = \\frac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1||\\vec{u}_2|}$$",
                "formula": "\\cos\\varphi = \\frac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1||\\vec{u}_2|}",
                "trap": "Quên lấy giá trị tuyệt đối trên tử số (góc giữa hai đường thẳng không được vượt quá 90 độ).",
                "audio": "Góc giữa hai đường thẳng luôn là góc nhọn hoặc góc vuông nên cosin luôn không âm.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ: Góc giữa 2 đường thẳng",
                        "problem": "Cho $\\vec{u}_1 = (1; 1; 0)$ và $\\vec{u}_2 = (0; 1; 1)$. Tính góc $\\varphi$.",
                        "solution": "$\\cos\\varphi = \\frac{|0 + 1 + 0|}{\\sqrt{2}\\sqrt{2}} = \\frac{1}{2} \\implies \\varphi = 60^\\circ$."
                    }
                ],
                "exercise": {
                    "id": "12_b16_c1",
                    "title": "Bài tập tự giải",
                    "content": "Số đo góc giữa 2 đường thẳng trong ví dụ trên bằng bao nhiêu độ?",
                    "target": "60"
                }
            },
            "Chủ điểm 2: Góc giữa đường thẳng và mặt phẳng": {
                "theory": "Góc $\\varphi$ giữa đường thẳng có VTCP $\\vec{u}$ và mặt phẳng có VTPT $\\vec{n}$ ($0^\\circ \\le \\varphi \\le 90^\\circ$):\n$$\\sin \\varphi = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}||\\vec{n}|}$$",
                "formula": "\\sin\\varphi = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}||\\vec{n}|}",
                "trap": "Nhầm dùng hàm cos thay vì hàm sin khi tính góc giữa đường thẳng và mặt phẳng.",
                "audio": "Rất quan trọng: góc giữa đường thẳng và mặt phẳng sử dụng hàm sin, không phải hàm cos.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Góc đường thẳng và mặt phẳng",
                        "problem": "Cho $\\vec{u} = (3; 4; 5)$ và mặt phẳng $Oxy$ có $\\vec{k} = (0; 0; 1)$. Tính góc $\\varphi$.",
                        "solution": "$\\sin\\varphi = \\frac{|5|}{\\sqrt{50} \\cdot 1} = \\frac{5}{5\\sqrt{2}} = \\frac{\\sqrt{2}}{2} \\implies \\varphi = 45^\\circ$."
                    }
                ],
                "exercise": {
                    "id": "12_b16_c2",
                    "title": "Bài tập tự giải",
                    "content": "Số đo góc giữa đường thẳng và mặt đáy trong ví dụ trên bằng bao nhiêu độ?",
                    "target": "45"
                }
            },
            "Chủ điểm 3: Góc giữa hai mặt phẳng": {
                "theory": "Góc $\\varphi$ giữa 2 mặt phẳng có VTPT $\\vec{n}_1, \\vec{n}_2$ ($0^\\circ \\le \\varphi \\le 90^\\circ$):\n$$\\cos \\varphi = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1||\\vec{n}_2|}$$",
                "formula": "\\cos\\varphi = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1||\\vec{n}_2|}",
                "trap": "Nhầm lẫn công thức hàm cos của góc 2 mặt phẳng với hàm sin của đường thẳng và mặt phẳng.",
                "audio": "Góc giữa hai mặt phẳng được đo thông qua góc giữa hai vectơ pháp tuyến và sử dụng hàm cos.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Góc giữa 2 mặt phẳng",
                        "problem": "Tính góc giữa $(P): x + y - 2 = 0$ và $(Q): y + z + 1 = 0$.",
                        "solution": "$\\vec{n}_1 = (1; 1; 0), \\vec{n}_2 = (0; 1; 1)$. $\\cos\\varphi = \\frac{|1|}{\\sqrt{2}\\sqrt{2}} = \\frac{1}{2} \\implies \\varphi = 60^\\circ$."
                    }
                ],
                "exercise": {
                    "id": "12_b16_c3",
                    "title": "Bài tập tự giải",
                    "content": "Góc giữa hai mặt phẳng P và Q bằng bao nhiêu độ?",
                    "target": "60"
                }
            },
            "Chủ điểm 4: Ứng dụng: góc trong bài toán thực tế": {
                "theory": "Tính góc cất cánh của máy bay so với mặt đất hoặc góc nghiêng của mái nhà so với sàn nhà.",
                "formula": "\\sin\\varphi_{bay} = \\frac{|\\vec{u} \\cdot \\vec{k}|}{|\\vec{u}|}",
                "trap": "Xác định sai vectơ pháp tuyến của sàn nhà (mặt sàn Oxy có VTPT là (0;0;1)).",
                "audio": "Góc cất cánh của máy bay chính là góc giữa vectơ vận tốc đường bay và vectơ pháp tuyến của mặt phẳng mặt đất.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ: Góc nghiêng mái nhà",
                        "problem": "Mái nhà có $(P): 4y + 3z - 12 = 0$. Mặt sàn $Oxy$ có $\\vec{k} = (0; 0; 1)$. Tính $\\cos$ góc nghiêng.",
                        "solution": "$\\vec{n}_P = (0; 4; 3)$. $\\cos\\varphi = \\frac{|3|}{\\sqrt{16+9} \\cdot 1} = \\frac{3}{5} = 0.6$."
                    }
                ],
                "exercise": {
                    "id": "12_b16_c4",
                    "title": "Bài tập tự giải",
                    "content": "Cosin góc nghiêng mái nhà bằng (viết dưới dạng số thập phân):",
                    "target": "0.6"
                }
            }
        }
    },

    "Bài 17. Phương trình mặt cầu": {
        "chapter": "Chương V. Phương trình mặt phẳng, đường thẳng, mặt cầu trong không gian",
        "topics": {
            "Chủ điểm 1: Phương trình mặt cầu": {
                "theory": "Mặt cầu tâm $I(a; b; c)$, bán kính $R > 0$:\n$$(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$$",
                "formula": "(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2",
                "trap": "Quên lấy căn bậc hai của vế phải khi đọc bán kính $R$.",
                "audio": "Mặt cầu tâm I bán kính R là tập hợp các điểm cách I một khoảng đúng bằng R.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ: Xác định tâm và bán kính",
                        "problem": "Tìm tâm và bán kính của $(x+2)^2 + (y-1)^2 + z^2 = 9$.",
                        "solution": "Tâm $I(-2; 1; 0)$, bán kính $R = \\sqrt{9} = 3$."
                    }
                ],
                "exercise": {
                    "id": "12_b17_c1",
                    "title": "Bài tập tự giải",
                    "content": "Bán kính của mặt cầu (x - 1)^2 + y^2 + (z + 2)^2 = 16 là:",
                    "target": "4"
                }
            },
            "Chủ điểm 2: Phương trình dạng khai triển": {
                "theory": "$$x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$$\nĐiều kiện là mặt cầu: $a^2 + b^2 + c^2 - d > 0$. Bán kính $R = \\sqrt{a^2 + b^2 + c^2 - d}$.",
                "formula": "R = \\sqrt{a^2 + b^2 + c^2 - d} \\quad (a^2+b^2+c^2-d > 0)",
                "trap": "Quên chia hệ số của x, y, z cho -2 để tìm tọa độ tâm a, b, c.",
                "audio": "Để tìm tâm mặt cầu dạng khai triển, ta chia hệ số đứng trước x, y, z cho trừ hai.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm bán kính mặt cầu khai triển",
                        "problem": "Mặt cầu $x^2 + y^2 + z^2 - 2x + 4y - 6z - 11 = 0$ có bán kính bao nhiêu?",
                        "solution": "$a = 1, b = -2, c = 3, d = -11$. $R = \\sqrt{1 + 4 + 9 - (-11)} = \\sqrt{25} = 5$."
                    }
                ],
                "exercise": {
                    "id": "12_b17_c2",
                    "title": "Bài tập tự giải",
                    "content": "Bán kính R của mặt cầu khai triển trên bằng:",
                    "target": "5"
                }
            },
            "Chủ điểm 3: Lập phương trình mặt cầu": {
                "theory": "- Đường kính $AB$: tâm là trung điểm $AB$, bán kính $R = AB/2$.\n- Tiếp xúc mặt phẳng $(P)$: $R = d(I, (P))$.",
                "formula": "R = \\frac{AB}{2}; \\quad R = d(I, (P))",
                "trap": "Nhầm tính $R = AB$ thay vì lấy một nửa độ dài đường kính.",
                "audio": "Mặt cầu tiếp xúc với mặt phẳng thì bán kính đúng bằng khoảng cách từ tâm đến mặt phẳng đó.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ: Mặt cầu tiếp xúc mặt phẳng",
                        "problem": "Tâm $I(1; 2; -1)$ tiếp xúc $(P): x + 2y + 2z - 9 = 0$. Viết phương trình.",
                        "solution": "$R = d(I, (P)) = \\frac{|1 + 4 - 2 - 9|}{\\sqrt{1+4+4}} = \\frac{6}{3} = 2$. Phương trình: $(x-1)^2 + (y-2)^2 + (z+1)^2 = 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b17_c3",
                    "title": "Bài tập tự giải",
                    "content": "Bán kính R của mặt cầu tiếp xúc mặt phẳng trên bằng:",
                    "target": "2"
                }
            },
            "Chủ điểm 4: Vị trí tương đối của điểm, mặt phẳng với mặt cầu": {
                "theory": "Khoảng cách $d = d(I, (P))$:\n- $d < R$: Cắt theo đường tròn có bán kính $r = \\sqrt{R^2 - d^2}$;\n- $d = R$: Tiếp xúc;\n- $d > R$: Không cắt.",
                "formula": "r = \\sqrt{R^2 - d^2}",
                "trap": "Nhầm lẫn giữa bán kính mặt cầu $R$ và bán kính đường tròn giao tuyến $r$.",
                "audio": "Khi mặt phẳng cắt mặt cầu, bán kính đường tròn giao tuyến được tính bằng định lý Pytago.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ: Bán kính đường tròn giao tuyến",
                        "problem": "Mặt cầu bán kính $R = 5$, khoảng cách đến mặt phẳng $d = 3$. Tính bán kính đường tròn giao tuyến.",
                        "solution": "$r = \\sqrt{5^2 - 3^2} = \\sqrt{16} = 4$."
                    }
                ],
                "exercise": {
                    "id": "12_b17_c4",
                    "title": "Bài tập tự giải",
                    "content": "Bán kính r của đường tròn giao tuyến bằng:",
                    "target": "4"
                }
            }
        }
    },

    # =========================================================================
    # CHƯƠNG VI. XÁC SUẤT CÓ ĐIỀU KIỆN
    # =========================================================================
    "Bài 18. Xác suất có điều kiện": {
        "chapter": "Chương VI. Xác suất có điều kiện",
        "topics": {
            "Chủ điểm 1: Định nghĩa xác suất có điều kiện": {
                "theory": "Xác suất của biến cố $A$ khi biết biến cố $B$ đã xảy ra ($P(B) > 0$):\n$$P(A|B) = \\frac{P(AB)}{P(B)}$$",
                "formula": "P(A|B) = \\frac{P(AB)}{P(B)}",
                "trap": "Nhầm lẫn giữa $P(A|B)$ và $P(B|A)$.",
                "audio": "Xác suất của A với điều kiện B bằng xác suất của biến cố giao chia cho xác suất của B.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tính xác suất có điều kiện",
                        "problem": "Gieo xúc xắc. $A$: 'số chấm chia hết cho 3', $B$: 'số chẵn'. Tính $P(A|B)$.",
                        "solution": "$B = \\{2, 4, 6\\}$, $AB = \\{6\\}$. $P(A|B) = \\frac{n(AB)}{n(B)} = \\frac{1}{3}$."
                    }
                ],
                "exercise": {
                    "id": "12_b18_c1",
                    "title": "Bài tập tự giải",
                    "content": "Mẫu số của phân số tối giản xác suất P(A|B) ở ví dụ trên bằng:",
                    "target": "3"
                }
            },
            "Chủ điểm 2: Tính chất và biến cố độc lập": {
                "theory": "- $P(A|B) + P(\\overline{A}|B) = 1$.\n- $A$ và $B$ độc lập $\\iff P(A|B) = P(A) \\iff P(AB) = P(A)P(B)$.",
                "formula": "A, B \\text{ độc lập} \\iff P(AB) = P(A) \\cdot P(B)",
                "trap": "Chỉ nhân xác suất trực tiếp $P(A)P(B)$ khi hai biến cố độc lập.",
                "audio": "Hai biến cố độc lập khi việc biến cố này xảy ra không làm thay đổi xác suất của biến cố kia.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Kiểm tra tính độc lập",
                        "problem": "Cho $P(A) = 0.4, P(B) = 0.5, P(AB) = 0.2$. $A$ và $B$ có độc lập không?",
                        "solution": "$P(A) \\cdot P(B) = 0.4 \\cdot 0.5 = 0.2 = P(AB)$. Vậy hai biến cố độc lập."
                    }
                ],
                "exercise": {
                    "id": "12_b18_c2",
                    "title": "Bài tập tự giải",
                    "content": "Hai biến cố A và B độc lập đúng hay sai? Nhập 1 nếu đúng, 0 nếu sai:",
                    "target": "1"
                }
            },
            "Chủ điểm 3: Công thức nhân xác suất": {
                "theory": "$$P(AB) = P(B) \\cdot P(A|B) = P(A) \\cdot P(B|A)$$\nÁp dụng cho các phép thử liên tiếp không hoàn lại.",
                "formula": "P(AB) = P(A) \\cdot P(B|A)",
                "trap": "Không cập nhật lại tổng số phần tử ở bước thứ hai khi lấy không hoàn lại.",
                "audio": "Khi lấy không hoàn lại, mẫu số ở lần lấy sau sẽ bị giảm đi một phần tử.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Lấy bi không hoàn lại",
                        "problem": "Hộp 6 bi đỏ, 4 bi xanh. Lấy lần lượt 2 bi không hoàn lại. Tính xác suất 2 bi đều đỏ.",
                        "solution": "$P = \\frac{6}{10} \\cdot \\frac{5}{9} = \\frac{1}{3}$."
                    }
                ],
                "exercise": {
                    "id": "12_b18_c3",
                    "title": "Bài tập tự giải",
                    "content": "Mẫu số của phân số tối giản xác suất lấy 2 bi đỏ là:",
                    "target": "3"
                }
            },
            "Chủ điểm 4: Sơ đồ hình cây": {
                "theory": "Biểu diễn trực quan các giai đoạn thực hiện. Xác suất của mỗi đường đi bằng tích các xác suất trên các nhánh của đường đó.",
                "formula": "P(\\text{đường đi}) = \\prod P(\\text{nhánh})",
                "trap": "Cộng nhầm nhánh thay vì nhân các nhánh trên cùng một đường đi.",
                "audio": "Sơ đồ cây giúp ta phân nhánh rõ ràng các trường hợp liên tiếp để tính xác suất chuẩn xác.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Bắn súng 2 lần liên tiếp",
                        "problem": "Lần 1 trúng xác suất 0.8. Nếu lần 1 trúng thì lần 2 trúng xác suất 0.9. Tính xác suất cả 2 lần đều trúng.",
                        "solution": "$P = 0.8 \\cdot 0.9 = 0.72$."
                    }
                ],
                "exercise": {
                    "id": "12_b18_c4",
                    "title": "Bài tập tự giải",
                    "content": "Xác suất cả hai lần bắn trúng bằng:",
                    "target": "0.72"
                }
            }
        }
    },

    "Bài 19. Xác suất toàn phần và công thức Bayes": {
        "chapter": "Chương VI. Xác suất có điều kiện",
        "topics": {
            "Chủ điểm 1: Công thức xác suất toàn phần": {
                "theory": "Với $0 < P(B) < 1$:\n$$P(A) = P(B) \\cdot P(A|B) + P(\\overline{B}) \\cdot P(A|\\overline{B})$$",
                "formula": "P(A) = P(B)P(A|B) + P(\\overline{B})P(A|\\overline{B})",
                "trap": "Quên kiểm tra tổng $P(B) + P(\\overline{B}) = 1$.",
                "audio": "Công thức xác suất toàn phần cộng gộp xác suất của biến cố A trong mọi kịch bản của B.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tỉ lệ phế phẩm 2 máy",
                        "problem": "Máy I sản xuất 60% tỉ lệ lỗi 2%, Máy II sản xuất 40% tỉ lệ lỗi 3%. Chọn ngẫu nhiên 1 sản phẩm, tính xác suất bị lỗi.",
                        "solution": "$P(A) = 0.6(0.02) + 0.4(0.03) = 0.012 + 0.012 = 0.024$."
                    }
                ],
                "exercise": {
                    "id": "12_b19_c1",
                    "title": "Bài tập tự giải",
                    "content": "Xác suất chọn phải phế phẩm trong ví dụ trên bằng:",
                    "target": "0.024"
                }
            },
            "Chủ điểm 2: Công thức Bayes": {
                "theory": "Xác suất hậu nghiệm cập nhật nguyên nhân $B$ khi đã biết kết quả $A$ xảy ra:\n$$P(B|A) = \\frac{P(B)P(A|B)}{P(A)} = \\frac{P(B)P(A|B)}{P(B)P(A|B) + P(\\overline{B})P(A|\\overline{B})}$$",
                "formula": "P(B|A) = \\frac{P(B)P(A|B)}{P(A)}",
                "trap": "Nhầm xác suất tiên nghiệm $P(B)$ với xác suất hậu nghiệm $P(B|A)$.",
                "audio": "Công thức Bayes dùng để tìm xác suất của nguyên nhân ban đầu khi đã thấy kết quả xảy ra.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Tìm nguyên nhân phế phẩm",
                        "problem": "Ở ví dụ trước, biết sản phẩm chọn ra bị lỗi. Tính xác suất nó do Máy I sản xuất.",
                        "solution": "$P(B|A) = \\frac{P(B)P(A|B)}{P(A)} = \\frac{0.6 \\cdot 0.02}{0.024} = \\frac{0.012}{0.024} = 0.5$."
                    }
                ],
                "exercise": {
                    "id": "12_b19_c2",
                    "title": "Bài tập tự giải",
                    "content": "Xác suất sản phẩm lỗi do máy I làm ra bằng:",
                    "target": "0.5"
                }
            },
            "Chủ điểm 3: Sơ đồ cây kết hợp công thức xác suất toàn phần, Bayes": {
                "theory": "Sử dụng sơ đồ cây để tính $P(A)$ (tổng các đường dẫn đến $A$) và tính $P(B|A)$ bằng tỷ số của đường nhánh $BA$ chia cho tổng $P(A)$.",
                "formula": "P(B|A) = \\frac{P(\\text{đường nhánh } BA)}{P(A)}",
                "trap": "Xác định sai nhánh cần tính tỷ lệ.",
                "audio": "Sơ đồ cây kết hợp với công thức Bayes giúp việc tính toán xác suất đảo điều kiện trở nên trực quan.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ: Lọc thư rác",
                        "problem": "30% thư là rác. 80% thư rác chứa từ 'khuyến mãi', thư thường chỉ 10% chứa từ này. Thư chứa từ 'khuyến mãi', tính xác suất là thư rác.",
                        "solution": "$P(K) = 0.3(0.8) + 0.7(0.1) = 0.31$. $P(S|K) = \\frac{0.3 \\cdot 0.8}{0.31} = \\frac{24}{31} \\approx 0.774$."
                    }
                ],
                "exercise": {
                    "id": "12_b19_c3",
                    "title": "Bài tập tự giải",
                    "content": "Tử số của phân số xác suất P(S|K) ở ví dụ trên bằng:",
                    "target": "24"
                }
            }
        }
    }
}
