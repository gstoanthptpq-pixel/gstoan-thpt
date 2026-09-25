# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 (PHẦN 1: BÀI 1 -> BÀI 14)
# Chuẩn hóa theo Vở tự học: Các chủ điểm là mục 1, 2, 3... thuộc PHẦN I
# ==============================================================================

GRADE_10_DATA = {}

GRADE_10_DATA.update({
    "Bài 1: Mệnh đề toán học": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Mệnh đề, mệnh đề chứa biến": {
                "theory": "Mệnh đề toán học là một khẳng định đúng hoặc sai. Một mệnh đề không thể vừa đúng vừa sai. Câu hỏi, câu cảm thán, câu mệnh lệnh không phải là mệnh đề. Mệnh đề chứa biến P(x) là câu khẳng định chứa biến số, tính đúng sai phụ thuộc vào giá trị cụ thể của x.",
                "formula": r"P \in \{\text{Đúng}, \text{Sai}\}",
                "trap": "Học sinh thường nhầm mệnh đề chứa biến là mệnh đề toán học. Ví dụ câu 'x > 3' chưa biết đúng hay sai nên chưa phải là mệnh đề toán học.",
                "audio": "Mệnh đề toán học là một câu khẳng định có tính đúng sai tuyệt đối. Câu cảm thán hay câu hỏi thì không phải là mệnh đề.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện mệnh đề toán học",
                        "problem": "Trong các câu sau, câu nào là mệnh đề toán học: (1) 'Số 12 là số chẵn', (2) 'Bạn học lớp mấy?', (3) '2x + 1 = 5'?",
                        "solution": "- Câu (1) là câu khẳng định đúng $\\implies$ Là mệnh đề toán học.\n- Câu (2) là câu hỏi $\\implies$ Không phải mệnh đề.\n- Câu (3) là mệnh đề chứa biến $\\implies$ Không phải mệnh đề toán học."
                    }
                ],
                "exercise": {"id": "10_1_1", "title": "Kiểm minh chứng", "content": "Trong các câu: 'Hôm nay trời đẹp quá!', '3 < 1', 'x - 2 = 0'. Có bao nhiêu mệnh đề toán học?", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Mệnh đề phủ định": {
                "theory": "Mệnh đề phủ định của P là $\\overline{P}$. Nếu P đúng thì $\\overline{P}$ sai; nếu P sai thì $\\overline{P}$ đúng. Để phủ định, ta thêm hoặc bớt từ 'không' (hoặc 'không phải') vào vị ngữ.",
                "formula": r"\text{P Đúng} \iff \overline{P} \text{ Sai}",
                "trap": "Phủ định của dấu lớn hơn ($>$) là dấu nhỏ hơn hoặc bằng ($\\le$), không được thiếu dấu bằng.",
                "audio": "Phủ định của một khẳng định là phát biểu ngược lại. Nhớ rằng phủ định của dấu lớn hơn là nhỏ hơn hoặc bằng.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập mệnh đề phủ định",
                        "problem": "Tìm mệnh đề phủ định của P: 'Tam giác ABC là tam giác vuông'.",
                        "solution": "- Mệnh đề phủ định $\\overline{P}$: 'Tam giác ABC không phải là tam giác vuông'."
                    }
                ],
                "exercise": {"id": "10_1_2", "title": "Kiểm minh chứng", "content": "Phủ định của bất đẳng thức x > 4 là x <= c. Giá trị của c bằng:", "type": "NUMERIC", "target": "4", "options": []}
            },
            "3. Mệnh đề kéo theo, mệnh đề đảo và kí hiệu lượng từ": {
                "theory": "Mệnh đề 'Nếu P thì Q' gọi là mệnh đề kéo theo, kí hiệu $P \\implies Q$. Nó chỉ SAI khi P đúng mà Q sai. Mệnh đề đảo của $P \\implies Q$ là $Q \\implies P$. Kí hiệu $\\forall$ (với mọi), $\\exists$ (tồn tại). Phủ định của $\\forall$ là $\\exists$, phủ định của $\\ge$ là $<$.",
                "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
                "trap": "Mệnh đề kéo theo $P \\implies Q$ luôn ĐÚNG khi giả thiết P sai, bất kể kết luận Q đúng hay sai.",
                "audio": "Mệnh đề kéo theo chỉ sai khi từ cái đúng dẫn đến cái sai. Phủ định của 'với mọi' là 'tồn tại'.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phủ định mệnh đề chứa lượng từ",
                        "problem": "Lập mệnh đề phủ định của '$\\forall x \\in \\mathbb{R}, x^2 + 1 > 0$'.",
                        "solution": "- Lượng từ $\\forall$ đổi thành $\\exists$, dấu $>$ đổi thành $\\le$.\n- Phủ định là: '$\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0$'."
                    }
                ],
                "exercise": {"id": "10_1_3", "title": "Kiểm minh chứng", "content": "Mệnh đề 'Nếu 2 > 5 thì 1 = 1' là mệnh đề Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 2: Tập hợp và các phép toán trên tập hợp": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Các khái niệm cơ bản về tập hợp": {
                "theory": "Tập hợp được xác định bằng cách liệt kê phần tử hoặc nêu tính chất đặc trưng. $A \\subset B$ nếu mọi phần tử của A đều thuộc B. Tập rỗng $\\emptyset$ là tập con của mọi tập hợp. Tập hợp có n phần tử thì có $2^n$ tập con.",
                "formula": r"A \subset B \iff (\forall x \in A \implies x \in B); \quad \text{Số tập con} = 2^n",
                "trap": "Kí hiệu $\\in$ dùng cho phần tử thuộc tập hợp; kí hiệu $\\subset$ dùng cho tập con nằm trong tập hợp.",
                "audio": "Phần tử thì thuộc tập hợp, còn tập hợp thì là tập con của tập hợp khác. Tập hợp rỗng là con của mọi tập hợp.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đếm số tập con",
                        "problem": "Tập hợp $A = \\{a; b; c\\}$ có bao nhiêu tập con?",
                        "solution": "- Số phần tử $n = 3$.\n- Số tập con là: $2^3 = 8$ tập con."
                    }
                ],
                "exercise": {"id": "10_2_1", "title": "Kiểm minh chứng", "content": "Tập hợp X = {1; 2} có tất cả bao nhiêu tập con?", "type": "NUMERIC", "target": "4", "options": []}
            },
            "2. Các phép toán trên tập hợp (Giao, Hợp, Hiệu)": {
                "theory": "Giao ($A \\cap B$): Lấy phần tử chung của cả hai tập. Hợp ($A \\cup B$): Lấy tất cả các phần tử. Hiệu ($A \\setminus B$): Lấy phần tử thuộc A nhưng không thuộc B.",
                "formula": r"A \cap B = \{x \mid x \in A, x \in B\}; \quad A \\setminus B = \{x \mid x \in A, x \notin B\}",
                "trap": "Khi lấy giao hoặc hợp các khoảng, đoạn số thực trên trục số, học sinh rất hay nhầm lẫn giữa ngoặc tròn `()` và ngoặc vuông `[]` tại các mút.",
                "audio": "Giao là lấy phần chung, hợp là gộp tất cả. Còn hiệu A trừ B là phần tử chỉ thuộc riêng A mà không nằm trong B.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giao của hai khoảng số thực",
                        "problem": "Tìm $A \\cap B$ với $A = (-2; 4]$ và $B = [1; 6)$.",
                        "solution": "- Biểu diễn trên trục số, phần chung nhau giữa $(-2; 4]$ và $[1; 6)$ là từ 1 đến 4.\n- Kết quả: $A \\cap B = [1; 4]$."
                    }
                ],
                "exercise": {"id": "10_2_2", "title": "Kiểm minh chứng", "content": "Cho A = [1; 5] và B = (3; 7). Số nguyên nằm trong A giao B là bao nhiêu số?", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 3: Bất phương trình bậc nhất hai ẩn": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khái niệm bất phương trình bậc nhất hai ẩn": {
                "theory": "Bất phương trình bậc nhất hai ẩn x, y có dạng tổng quát $ax + by \\le c$ (hoặc $<, >, \\ge$) với $a, b$ không đồng thời bằng 0. Cặp số $(x_0; y_0)$ là nghiệm nếu thay vào cho ta bất đẳng thức đúng.",
                "formula": r"ax + by \le c \quad (a^2 + b^2 \neq 0)",
                "trap": "Biểu thức chứa $x^2, y^2$ hoặc tích $xy$ không phải là bất phương trình bậc nhất hai ẩn.",
                "audio": "Bất phương trình bậc nhất hai ẩn có bậc của cả x và y đều bằng một. Cặp số x y thỏa mãn thì gọi là nghiệm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Kiểm tra nghiệm",
                        "problem": "Điểm $M(1; 2)$ có phải là nghiệm của $2x - y + 1 > 0$ không?",
                        "solution": "- Thay $x = 1, y = 2$ vào vế trái: $2(1) - 2 + 1 = 1$.\n- Vì $1 > 0$ là Đúng, nên $M(1; 2)$ là một nghiệm của bất phương trình."
                    }
                ],
                "exercise": {"id": "10_3_1", "title": "Kiểm minh chứng", "content": "Gốc tọa độ O(0; 0) có là nghiệm của 2x - 3y < 4 không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Biểu diễn miền nghiệm của bất phương trình": {
                "theory": "Đường thẳng $d: ax + by = c$ chia mặt phẳng thành hai nửa mặt phẳng. Để biểu diễn miền nghiệm: (1) Vẽ đường thẳng d; (2) Lấy một điểm thử $M_0$ (thường là gốc $O(0;0)$) không thuộc d thay vào BPT; (3) Kết luận nửa mặt phẳng chứa điểm thử (nếu đúng) hoặc không chứa (nếu sai).",
                "formula": r"\text{Bờ } d: ax + by = c",
                "trap": "BPT có dấu $\\le, \\ge$ thì đường bờ d vẽ NÉT LIỀN (lấy cả bờ). Nếu có dấu $<, >$ thì bờ d vẽ NÉT ĐỨT (không lấy bờ).",
                "audio": "Vẽ đường bờ d rồi lấy gốc tọa độ thay vào. Đúng thì giữ lại nửa mặt phẳng chứa gốc O, sai thì gạch bỏ đi.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định miền nghiệm",
                        "problem": "Miền nghiệm của bất phương trình $x + y \\le 2$ có chứa điểm $A(2; 2)$ không?",
                        "solution": "- Thay $x = 2, y = 2$ vào vế trái: $2 + 2 = 4$.\n- Thấy $4 \\le 2$ là Sai, nên điểm A không thuộc miền nghiệm."
                    }
                ],
                "exercise": {"id": "10_3_2", "title": "Kiểm minh chứng", "content": "Bờ của miền nghiệm 2x + y > 1 được vẽ bằng nét liền (1) hay nét đứt (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 4: Hệ bất phương trình bậc nhất hai ẩn": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Hệ bất phương trình và Biểu diễn miền nghiệm": {
                "theory": "Hệ BPT bậc nhất hai ẩn gồm nhiều bất phương trình bậc nhất hai ẩn. Miền nghiệm của hệ là phần giao của các miền nghiệm thành phần, thường là một miền đa giác phẳng.",
                "formula": r"\text{Miền nghiệm là phần mặt phẳng KHÔNG BỊ GẠCH}",
                "trap": "Học sinh thường gạch nhầm hướng do xét sai dấu điểm thử cho từng bất phương trình riêng rẽ.",
                "audio": "Miền nghiệm của hệ bất phương trình là phần mặt phẳng không bị gạch sau khi đã loại bỏ các phần vi phạm của từng bất phương trình con.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Kiểm tra nghiệm của hệ",
                        "problem": "Điểm $M(1; 1)$ có là nghiệm của hệ $\\begin{cases} x \\ge 0 \\\\ x + y \\le 3 \\end{cases}$ không?",
                        "solution": "- Thỏa BPT 1: $1 \\ge 0$ (Đúng).\n- Thỏa BPT 2: $1 + 1 \\le 3$ (Đúng).\n- Vì thỏa mãn cả hai, $M(1; 1)$ là nghiệm của hệ."
                    }
                ],
                "exercise": {"id": "10_4_1", "title": "Kiểm minh chứng", "content": "Điểm (0; 0) có thuộc miền nghiệm của hệ x >= 1 và y >= 0 không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "2. Ứng dụng giải bài toán tối ưu thực tế": {
                "theory": "Biểu thức mục tiêu $F(x, y) = ax + by$ trên một miền đa giác lồi luôn đạt giá trị lớn nhất hoặc nhỏ nhất tại một trong các ĐỈNH của đa giác đó.",
                "formula": r"\max F(x, y) = \max \{F(A), F(B), F(C), \dots\}",
                "trap": "Phải tính giá trị của F tại TẤT CẢ các đỉnh của miền đa giác rồi mới so sánh để tìm GTLN, GTNN.",
                "audio": "Muốn tối ưu chi phí hay lợi nhuận, em tìm tọa độ tất cả các đỉnh của đa giác miền nghiệm rồi thay vào tính F, số lớn nhất là max, nhỏ nhất là min.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giá trị lớn nhất tại đỉnh",
                        "problem": "Miền đa giác có 3 đỉnh $A(0; 2), B(2; 1), C(3; 0)$. Tìm GTLN của $F = 2x + 3y$.",
                        "solution": "- $F(A) = 2(0) + 3(2) = 6$.\n- $F(B) = 2(2) + 3(1) = 7$.\n- $F(C) = 2(3) + 3(0) = 6$.\n- So sánh thấy giá trị lớn nhất là 7 (đạt tại đỉnh B)."
                    }
                ],
                "exercise": {"id": "10_4_2", "title": "Kiểm minh chứng", "content": "Với 2 đỉnh O(0; 0) và A(2; 3), giá trị lớn nhất của F = 3x + y bằng bao nhiêu?", "type": "NUMERIC", "target": "9", "options": []}
            }
        }
    },
    "Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa giá trị lượng giác trên nửa đường tròn": {
                "theory": "Với góc $\\alpha$ ($0^\circ \\le \\alpha \\le 180^\circ$), điểm $M(x_0; y_0)$ trên nửa đường tròn đơn vị: $\\sin\\alpha = y_0$, $\\cos\\alpha = x_0$, $\\tan\\alpha = \\frac{y_0}{x_0}$ ($x_0 \\neq 0$), $\\cot\\alpha = \\frac{x_0}{y_0}$ ($y_0 \\neq 0$).",
                "formula": r"\sin^2\alpha + \cos^2\alpha = 1; \quad 1 + \tan^2\alpha = \frac{1}{\cos^2\alpha}",
                "trap": "Góc tù $\\alpha \\in (90^\circ; 180^\circ]$ luôn có $\\cos\\alpha < 0$, $\\tan\\alpha < 0$, $\\cot\\alpha < 0$. Chỉ có $\\sin\\alpha > 0$.",
                "audio": "Tung độ là sin, hoành độ là cos. Nhớ là góc tù thì hoành độ âm nên cos luôn mang dấu âm nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị lượng giác còn lại",
                        "problem": "Cho $\\sin\\alpha = \\frac{3}{5}$ với $\\alpha$ là góc tù. Tính $\\cos\\alpha$.",
                        "solution": "- $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$.\n- Vì $\\alpha$ tù nên $\\cos\\alpha < 0 \\implies \\cos\\alpha = -\\frac{4}{5} = -0.8$."
                    }
                ],
                "exercise": {"id": "10_5_1", "title": "Kiểm minh chứng", "content": "Điểm M(0; 1) trên nửa đường tròn đơn vị ứng với góc alpha bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "2. Mối quan hệ giữa hai góc bù nhau, phụ nhau": {
                "theory": "Hai góc bù nhau (tổng bằng $180^\circ$): Sin bằng nhau, Cos đối nhau ($\\sin(180^\circ - \\alpha) = \\sin\\alpha$, $\\cos(180^\circ - \\alpha) = -\\cos\\alpha$). Hai góc phụ nhau (tổng bằng $90^\circ$): Sin góc này bằng Cos góc kia.",
                "formula": r"\sin(180^\circ - \alpha) = \sin\alpha; \quad \cos(180^\circ - \alpha) = -\cos\alpha",
                "trap": "Học sinh thường quên dấu trừ khi tính cos của góc bù: $\\cos(180^\circ - \\alpha) = -\\cos\\alpha$.",
                "audio": "Sin bù, phụ chéo. Hai góc bù nhau có sin bằng nhau, còn cosin thì ngược dấu.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính nhanh qua góc bù",
                        "problem": "Tính $\\cos 150^\circ$ biết $\\cos 30^\circ = \\frac{\\sqrt{3}}{2}$.",
                        "solution": "- Do $150^\circ$ và $30^\circ$ bù nhau nên $\\cos 150^\circ = -\\cos 30^\circ = -\\frac{\\sqrt{3}}{2}$."
                    }
                ],
                "exercise": {"id": "10_5_2", "title": "Kiểm minh chứng", "content": "Giá trị của biểu thức sin(30 độ) + cos(120 độ) bằng:", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 6: Hệ thức lượng trong tam giác": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định lí côsin": {
                "theory": "Trong tam giác ABC: $a^2 = b^2 + c^2 - 2bc\\cos A$. Hệ quả tính góc: $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}$. Định lí áp dụng khi biết 2 cạnh và góc xen giữa, hoặc biết cả 3 cạnh.",
                "formula": r"a^2 = b^2 + c^2 - 2bc \cos A; \quad \cos A = \frac{b^2 + c^2 - a^2}{2bc}",
                "trap": "Quên nhân 2 ở số hạng $2bc\\cos A$, hoặc nhầm lẫn dấu trừ thành dấu cộng.",
                "audio": "Định lí Côsin mở rộng từ Pytago: Bình phương một cạnh bằng tổng bình phương hai cạnh kia trừ đi hai lần tích của chúng nhân cos góc xen giữa.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính cạnh tam giác",
                        "problem": "Tam giác ABC có $b = 5, c = 8, \\widehat{A} = 60^\circ$. Tính cạnh $a$.",
                        "solution": "- $a^2 = 5^2 + 8^2 - 2(5)(8)\\cos 60^\circ = 25 + 64 - 80(0.5) = 49$.\n- Suy ra $a = 7$."
                    }
                ],
                "exercise": {"id": "10_6_1", "title": "Kiểm minh chứng", "content": "Tam giác có b = 3, c = 4 và góc A = 90 độ. Cạnh a bằng bao nhiêu?", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Định lí sin và Công thức tính diện tích": {
                "theory": "Định lí Sin: $\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R$. Công thức diện tích: $S = \\frac{1}{2}bc\\sin A = \\frac{abc}{4R} = pr = \\sqrt{p(p-a)(p-b)(p-c)}$ với $p = \\frac{a+b+c}{2}$.",
                "formula": r"\frac{a}{\sin A} = 2R; \quad S = \frac{1}{2}ab \sin C = \sqrt{p(p-a)(p-b)(p-c)}",
                "trap": "Trong công thức Heron, $p$ là NỬA chu vi. Rất nhiều bạn lấy cả chu vi để tính dẫn đến kết quả sai hoàn toàn.",
                "audio": "Định lí Sin dùng để tính bán kính đường tròn ngoại tiếp R. Công thức diện tích Heron dùng khi đề bài cho biết độ dài ba cạnh.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính bán kính R",
                        "problem": "Tam giác ABC có $a = 6, \\widehat{A} = 30^\circ$. Tính $R$.",
                        "solution": "- Áp dụng định lí sin: $2R = \\frac{a}{\\sin A} = \\frac{6}{\\sin 30^\circ} = 12 \\implies R = 6$."
                    }
                ],
                "exercise": {"id": "10_6_2", "title": "Kiểm minh chứng", "content": "Tam giác vuông có hai cạnh góc vuông là 6 và 8. Bán kính ngoại tiếp R bằng:", "type": "NUMERIC", "target": "5", "options": []}
            }
        }
    },
    "Bài 7: Các khái niệm mở đầu về vectơ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa vectơ và Độ dài": {
                "theory": "Vectơ là một đoạn thẳng có hướng. Điểm A là điểm đầu, B là điểm cuối thì kí hiệu là $\\vec{AB}$. Độ dài của vectơ là khoảng cách giữa điểm đầu và điểm cuối: $|\\vec{AB}| = AB$.",
                "formula": r"|\vec{AB}| = AB; \quad |\vec{0}| = 0",
                "trap": "Kí hiệu độ dài vectơ bắt buộc phải có hai vạch đứng $|\\vec{a}|$. Viết $\\vec{AB} = 5$ là sai quy ước toán học.",
                "audio": "Vectơ là một đoạn thẳng có hướng xác định. Độ dài vectơ chính là chiều dài của đoạn thẳng nối điểm đầu và điểm cuối.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài vectơ",
                        "problem": "Cho hình vuông ABCD cạnh bằng 3. Tính độ dài của vectơ $\\vec{AC}$.",
                        "solution": "- Độ dài $|\\vec{AC}| = AC$. Theo Pytago: $AC = \\sqrt{3^2 + 3^2} = 3\\sqrt{2}$."
                    }
                ],
                "exercise": {"id": "10_7_1", "title": "Kiểm minh chứng", "content": "Cho tam giác đều ABC cạnh 4. Độ dài của vectơ BC bằng bao nhiêu?", "type": "NUMERIC", "target": "4", "options": []}
            },
            "2. Hai vectơ cùng phương, cùng hướng, bằng nhau": {
                "theory": "Hai vectơ cùng phương nếu giá của chúng song song hoặc trùng nhau. Hai vectơ BẰNG NHAU khi chúng CÙNG HƯỚNG và CÙNG ĐỘ DÀI. Vectơ-không $\\vec{0}$ cùng phương, cùng hướng với mọi vectơ.",
                "formula": r"\vec{a} = \vec{b} \iff \begin{cases} \vec{a} \uparrow\uparrow \vec{b} \\ |\vec{a}| = |\vec{b}| \end{cases}",
                "trap": "Hai vectơ cùng độ dài và giá song song chưa chắc bằng nhau vì chúng có thể ngược hướng nhau.",
                "audio": "Để hai vectơ bằng nhau, chúng phải thỏa mãn cả hai điều kiện: cùng chỉ về một hướng và có độ dài bằng nhau.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện vectơ bằng nhau",
                        "problem": "Cho hình bình hành ABCD. Vectơ nào bằng vectơ $\\vec{AB}$?",
                        "solution": "- Cạnh AB song song và bằng DC, hướng từ A sang B trùng hướng D sang C.\n- Vậy $\\vec{AB} = \\vec{DC}$."
                    }
                ],
                "exercise": {"id": "10_7_2", "title": "Kiểm minh chứng", "content": "Trong hình bình hành ABCD, vectơ AB bằng vectơ CD. Khẳng định này Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 8: Tổng và hiệu của hai vectơ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Tổng của hai vectơ": {
                "theory": "Quy tắc ba điểm (nối đuôi): $\\vec{AB} + \\vec{BC} = \\vec{AC}$. Quy tắc hình bình hành (chung gốc): Nếu ABCD là hình bình hành thì $\\vec{AB} + \\vec{AD} = \\vec{AC}$.",
                "formula": r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{AB} + \vec{AD} = \vec{AC}",
                "trap": "Chỉ áp dụng quy tắc 3 điểm khi điểm cuối của vectơ này là điểm đầu của vectơ kia.",
                "audio": "Cộng vectơ theo quy tắc ba điểm là nối đuôi nhau. Điểm đầu của mũi tên này nối tiếp vào điểm cuối của mũi tên kia.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức tổng",
                        "problem": "Rút gọn tổng $\\vec{AB} + \\vec{BC} + \\vec{CD}$.",
                        "solution": "- Áp dụng liên tiếp quy tắc 3 điểm: $(\\vec{AB} + \\vec{BC}) + \\vec{CD} = \\vec{AC} + \\vec{CD} = \\vec{AD}$."
                    }
                ],
                "exercise": {"id": "10_8_1", "title": "Kiểm minh chứng", "content": "Nếu ABCD là hình bình hành thì AB + AD bằng vectơ đường chéo nào? (Điền AC hoặc BD)", "type": "STRING", "target": "AC", "options": []}
            },
            "2. Hiệu của hai vectơ": {
                "theory": "Vectơ đối của $\\vec{a}$ là $-\\vec{a}$. Hiệu $\\vec{a} - \\vec{b} = \\vec{a} + (-\\vec{b})$. Quy tắc trừ chung gốc: $\\vec{AB} - \\vec{AC} = \\vec{CB}$ (lấy ngọn của vectơ trừ ghép với ngọn của vectơ bị trừ). Hệ thức trung điểm: I là trung điểm AB $\\iff \\vec{IA} + \\vec{IB} = \\vec{0}$.",
                "formula": r"\vec{AB} - \vec{AC} = \vec{CB}; \quad \vec{IA} + \vec{IB} = \vec{0}",
                "trap": "Phép trừ hai vectơ chung gốc rất hay bị viết ngược thành $\\vec{BC}$. Phải là $\\vec{CB}$.",
                "audio": "Trừ hai vectơ chung gốc thì lấy điểm cuối của vectơ thứ hai ghép với điểm cuối của vectơ thứ nhất, đọc ngược từ sau ra trước.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc trừ",
                        "problem": "Rút gọn biểu thức $\\vec{OB} - \\vec{OA}$.",
                        "solution": "- Chung gốc O, áp dụng quy tắc trừ: $\\vec{OB} - \\vec{OA} = \\vec{AB}$."
                    }
                ],
                "exercise": {"id": "10_8_2", "title": "Kiểm minh chứng", "content": "Rút gọn vectơ MN - MP thu được vectơ nào? (Điền PN hoặc NP)", "type": "STRING", "target": "PN", "options": []}
            }
        }
    },
    "Bài 9: Tích của một vectơ với một số": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định nghĩa và Tính chất": {
                "theory": "Tích của số $k$ với vectơ $\\vec{a}$ là vectơ $k\\vec{a}$ cùng hướng với $\\vec{a}$ nếu $k > 0$, ngược hướng nếu $k < 0$. Độ dài $|k\\vec{a}| = |k| \\cdot |\\vec{a}|$. Tính chất trung điểm: $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$. Trọng tâm: $\\vec{MA} + \\vec{MB} + \\vec{MC} = 3\\vec{MG}$.",
                "formula": r"\vec{MA} + \vec{MB} = 2\vec{MI}; \quad \vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}",
                "trap": "Học sinh hay quên hệ số 2 trong công thức trung điểm và hệ số 3 trong công thức trọng tâm.",
                "audio": "Nhân vectơ với một số dương giữ nguyên hướng, nhân với số âm đảo ngược hướng. Nhớ công thức trung điểm có số 2 và trọng tâm có số 3.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài tích vectơ với số",
                        "problem": "Cho $|\\vec{a}| = 4$. Tính độ dài của vectơ $-3\\vec{a}$.",
                        "solution": "- $|-3\\vec{a}| = |-3| \\cdot |\\vec{a}| = 3 \\cdot 4 = 12$."
                    }
                ],
                "exercise": {"id": "10_9_1", "title": "Kiểm minh chứng", "content": "G là trọng tâm tam giác ABC, M bất kì. MA + MB + MC = c.MG. Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "2. Điều kiện để hai vectơ cùng phương": {
                "theory": "Vectơ $\\vec{a}$ cùng phương với $\\vec{b} \\neq \\vec{0}$ khi và chỉ khi có số $k$ sao cho $\\vec{a} = k\\vec{b}$. Ba điểm A, B, C thẳng hàng khi và chỉ khi $\\vec{AB} = k\\vec{AC}$.",
                "formula": r"\vec{a} \parallel \vec{b} \iff \vec{a} = k\vec{b}; \quad A, B, C \text{ thẳng hàng} \iff \vec{AB} = k\vec{AC}",
                "trap": "Để chứng minh ba điểm thẳng hàng, hai vectơ phải có CHUNG một điểm (ví dụ $\\vec{AB}$ và $\\vec{AC}$).",
                "audio": "Hai vectơ cùng phương khi vectơ này bằng k lần vectơ kia. Ba điểm thẳng hàng khi hai vectơ chung gốc cùng phương.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh thẳng hàng",
                        "problem": "Biết $\\vec{AB} = 2\\vec{u}$ và $\\vec{AC} = 6\\vec{u}$. Ba điểm A, B, C có thẳng hàng không?",
                        "solution": "- Ta thấy $\\vec{AC} = 3\\vec{AB}$. Hai vectơ cùng phương và chung điểm A nên A, B, C thẳng hàng."
                    }
                ],
                "exercise": {"id": "10_9_2", "title": "Kiểm minh chứng", "content": "Nếu vectơ a = -2 vectơ b thì hai vectơ này cùng hướng (1) hay ngược hướng (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 10: Vectơ trong mặt phẳng tọa độ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Tọa độ của vectơ và Tọa độ của điểm": {
                "theory": "Vectơ $\\vec{u} = x\\vec{i} + y\\vec{j} \\iff \\vec{u} = (x; y)$. Tọa độ điểm $M$ chính là tọa độ vectơ $\\vec{OM}$. Vectơ nối hai điểm: $\\vec{AB} = (x_B - x_A; y_B - y_A)$. Tọa độ trung điểm: $x_I = \\frac{x_A+x_B}{2}, y_I = \\frac{y_A+y_B}{2}$.",
                "formula": r"\vec{AB} = (x_B - x_A; y_B - y_A); \quad x_I = \frac{x_A+x_B}{2}, y_I = \frac{y_A+y_B}{2}",
                "trap": "Tính tọa độ vectơ $\\vec{AB}$ phải lấy tọa độ điểm cuối B trừ điểm đầu A. Học sinh hay làm ngược lại.",
                "audio": "Tọa độ vectơ bằng tọa độ điểm sau trừ điểm trước. Tọa độ trung điểm bằng trung bình cộng tọa độ hai đầu mút.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tọa độ vectơ",
                        "problem": "Cho $A(1; 3)$ và $B(5; -1)$. Tìm tọa độ $\\vec{AB}$ và trung điểm $I$.",
                        "solution": "- $\\vec{AB} = (5 - 1; -1 - 3) = (4; -4)$.\n- Trung điểm $I: x_I = \\frac{1+5}{2} = 3; y_I = \\frac{3 + (-1)}{2} = 1 \\implies I(3; 1)$."
                    }
                ],
                "exercise": {"id": "10_10_1", "title": "Kiểm minh chứng", "content": "Cho A(2; 4) và B(4; 0). Trung điểm I của AB có tung độ y bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Biểu thức tọa độ của các phép toán vectơ": {
                "theory": "Cho $\\vec{u} = (x_1; y_1), \\vec{v} = (x_2; y_2)$: Tổng $\\vec{u} + \\vec{v} = (x_1+x_2; y_1+y_2)$; Tích số $k\\vec{u} = (kx_1; ky_1)$. Hai vectơ cùng phương khi $\\frac{x_1}{x_2} = \\frac{y_1}{y_2}$ ($x_2, y_2 \\neq 0$).",
                "formula": r"\vec{u} \pm \vec{v} = (x_1 \pm x_2; y_1 \pm y_2); \quad \vec{u} \parallel \vec{v} \iff x_1y_2 - x_2y_1 = 0",
                "trap": "Nhân một số với một vectơ là nhân số đó vào CẢ hoành độ và tung độ.",
                "audio": "Cộng trừ hai vectơ thì làm trên từng trục hoành với hoành, tung với tung. Nhân số vào thì nhân cho cả hai tọa độ.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tọa độ vectơ tổng hợp",
                        "problem": "Cho $\\vec{a} = (1; 2)$ và $\\vec{b} = (3; -1)$. Tìm tọa độ $\\vec{u} = 2\\vec{a} + \\vec{b}$.",
                        "solution": "- $2\\vec{a} = (2; 4)$.\n- $\\vec{u} = (2 + 3; 4 + (-1)) = (5; 3)$."
                    }
                ],
                "exercise": {"id": "10_10_2", "title": "Kiểm minh chứng", "content": "Cho a = (2; -1). Vectơ 3a có hoành độ bằng bao nhiêu?", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 11: Tích vô hướng của hai vectơ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Biểu thức tọa độ của tích vô hướng": {
                "theory": "Tích vô hướng của hai vectơ là một SỐ THỰC: $\\vec{u} \\cdot \\vec{v} = x_1x_2 + y_1y_2$. Độ dài vectơ $|\\vec{u}| = \\sqrt{x^2 + y^2}$. Khoảng cách $AB = \\sqrt{(x_B-x_A)^2 + (y_B-y_A)^2}$. Hai vectơ vuông góc $\\iff \\vec{u} \\cdot \\vec{v} = 0$.",
                "formula": r"\vec{u} \cdot \vec{v} = x_1x_2 + y_1y_2; \quad \vec{u} \perp \vec{v} \iff x_1x_2 + y_1y_2 = 0",
                "trap": "Tích vô hướng cho ra một số thực, KHÔNG PHẢI là một vectơ.",
                "audio": "Tích vô hướng bằng hoành nhân hoành cộng tung nhân tung. Hai vectơ vuông góc khi và chỉ khi tích vô hướng bằng 0.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tích vô hướng",
                        "problem": "Cho $\\vec{u} = (3; 2)$ và $\\vec{v} = (1; -4)$. Tính $\\vec{u} \\cdot \\vec{v}$.",
                        "solution": "- $\\vec{u} \\cdot \\vec{v} = 3(1) + 2(-4) = 3 - 8 = -5$."
                    }
                ],
                "exercise": {"id": "10_11_1", "title": "Kiểm minh chứng", "content": "Độ dài của vectơ u = (3; 4) bằng bao nhiêu?", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Góc giữa hai vectơ": {
                "theory": "Cosin góc giữa hai vectơ $\\vec{u}$ và $\\vec{v}$ bằng tích vô hướng chia cho tích độ dài.",
                "formula": r"\cos(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| \cdot |\vec{v}|} = \frac{x_1x_2 + y_1y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}",
                "trap": "Không thêm trị tuyệt đối ở tử số như công thức góc đường thẳng. Góc giữa 2 vectơ có thể là góc tù khi tích vô hướng âm.",
                "audio": "Cosin góc giữa hai vectơ bằng tích vô hướng chia cho tích độ dài. Nhớ đừng cho thêm trị tuyệt đối vào tử số.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa hai vectơ",
                        "problem": "Cho $\\vec{a} = (1; 0)$ và $\\vec{b} = (1; 1)$. Tính góc giữa $\\vec{a}$ và $\\vec{b}$.",
                        "solution": "- $\\vec{a} \\cdot \\vec{b} = 1(1) + 0(1) = 1$.\n- $|\\vec{a}| = 1, |\\vec{b}| = \\sqrt{2}$.\n- $\\cos = \\frac{1}{1 \\cdot \\sqrt{2}} = \\frac{\\sqrt{2}}{2} \\implies \\text{Góc bằng } 45^\circ$."
                    }
                ],
                "exercise": {"id": "10_11_2", "title": "Kiểm minh chứng", "content": "Góc giữa hai vectơ vuông góc nhau bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 12: Số gần đúng và sai số": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Số gần đúng, sai số tuyệt đối và sai số tương đối": {
                "theory": "Sai số tuyệt đối $\\Delta_a = |a - \\overline{a}| \\le d$ ($d$ là độ chính xác). Sai số tương đối $\\delta_a = \\frac{\\Delta_a}{|a|} \\le \\frac{d}{|a|}$ đo chất lượng của phép đo (càng nhỏ càng tốt).",
                "formula": r"\Delta_a = |a - \overline{a}| \le d; \quad \delta_a = \frac{d}{|a|}",
                "trap": "Học sinh thường quên viết ký hiệu $\\pm d$ biểu thị độ chính xác của số gần đúng.",
                "audio": "Sai số tuyệt đối cho biết độ lệch thực tế. Sai số tương đối tính theo tỉ lệ phần trăm để đánh giá phép đo có chuẩn xác hay không.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đọc độ chính xác",
                        "problem": "Phép đo cho kết quả $a = 150 \\pm 0.2$ m. Độ chính xác $d$ bằng bao nhiêu?",
                        "solution": "- Số đứng sau dấu $\\pm$ là độ chính xác $d = 0.2$ m."
                    }
                ],
                "exercise": {"id": "10_12_1", "title": "Kiểm minh chứng", "content": "Kết quả đo lường L = 50 +/- 0.5 (cm). Độ chính xác d bằng:", "type": "NUMERIC", "target": "0.5", "options": []}
            },
            "2. Quy tròn số gần đúng": {
                "theory": "Quy tắc làm tròn: Chữ số ngay sau hàng quy tròn $\\ge 5$ thì cộng 1 vào hàng quy tròn, $< 5$ thì giữ nguyên. Các số sau hàng quy tròn chuyển thành số 0 (hoặc bỏ đi nếu ở phần thập phân). Khi biết độ chính xác $d$, ta quy tròn số ở hàng lớn hơn hàng của $d$ một bậc.",
                "formula": r"\text{Chữ số sau } \ge 5 \implies +1; \quad < 5 \implies \text{Giữ nguyên}",
                "trap": "Phải xác định đúng hàng cao nhất của độ chính xác d rồi quy tròn ở hàng liền trước nó một bậc.",
                "audio": "Từ năm trở lên thì cộng thêm một, dưới năm thì giữ nguyên. Chú ý hàng làm tròn phụ thuộc vào độ chính xác d.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Quy tròn số thập phân",
                        "problem": "Quy tròn số $3.1415$ đến hàng phần trăm.",
                        "solution": "- Hàng phần trăm là số 4. Chữ số ngay sau nó là 1 ($< 5$).\n- Giữ nguyên: Kết quả là $3.14$."
                    }
                ],
                "exercise": {"id": "10_12_2", "title": "Kiểm minh chứng", "content": "Làm tròn số 15.678 đến hàng phần mười được số bao nhiêu?", "type": "NUMERIC", "target": "15.7", "options": []}
            }
        }
    },
    "Bài 13: Các số đặc trưng đo xu thế trung tâm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Số trung bình và Trung vị": {
                "theory": "Số trung bình $\\overline{x}$ bằng tổng các giá trị chia cho cỡ mẫu. Trung vị $M_e$ là giá trị đứng chính giữa mẫu số liệu sau khi đã sắp xếp thứ tự tăng dần. Nếu cỡ mẫu n chẵn, trung vị bằng trung bình cộng hai số ở giữa.",
                "formula": r"\overline{x} = \frac{\sum x_i}{n}; \quad M_e = \text{Giá trị chính giữa}",
                "trap": "Muốn tìm trung vị, BẮT BUỘC phải sắp xếp mẫu số liệu theo thứ tự không giảm trước tiên.",
                "audio": "Trung vị là số đứng ở chính giữa mẫu số liệu đã sắp xếp. Nhớ phải xếp các số từ bé đến lớn trước khi tìm nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm trung vị",
                        "problem": "Tìm trung vị của mẫu: 5, 2, 9, 1, 7.",
                        "solution": "- Sắp xếp tăng dần: 1, 2, 5, 7, 9.\n- Mẫu có 5 số (lẻ), số chính giữa ở vị trí thứ 3: $M_e = 5$."
                    }
                ],
                "exercise": {"id": "10_13_1", "title": "Kiểm minh chứng", "content": "Trung vị của mẫu số liệu đã sắp xếp: 2, 4, 6, 8 bằng bao nhiêu?", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Tứ phân vị và Mốt": {
                "theory": "Tứ phân vị gồm $Q_1, Q_2, Q_3$ chia mẫu làm 4 phần đều nhau. $Q_2$ chính là trung vị $M_e$. $Q_1$ là trung vị nửa dưới, $Q_3$ là trung vị nửa trên. Mốt ($M_o$) là giá trị xuất hiện nhiều lần nhất trong mẫu.",
                "formula": r"Q_2 = M_e; \quad Q_1 = M_e(\text{nửa trái}); \quad Q_3 = M_e(\text{nửa phải})",
                "trap": "Khi cỡ mẫu n lẻ, giá trị trung vị $Q_2$ sẽ không được đưa vào nửa dưới và nửa trên khi tìm $Q_1, Q_3$.",
                "audio": "Ba tứ phân vị chia mẫu làm bốn phần bằng nhau. Q2 là trung vị ở giữa, Q1 chia đôi nửa dưới, Q3 chia đôi nửa trên.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm mốt",
                        "problem": "Tìm mốt của mẫu điểm số: 7, 8, 8, 9, 10.",
                        "solution": "- Số 8 xuất hiện nhiều nhất (2 lần) $\\implies M_o = 8$."
                    }
                ],
                "exercise": {"id": "10_13_2", "title": "Kiểm minh chứng", "content": "Mẫu số liệu: 1, 2, 2, 3, 4 có mốt Mo bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 14: Các số đặc trưng đo độ phân tán": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khoảng biến thiên và Khoảng tứ phân vị": {
                "theory": "Khoảng biến thiên $R = x_{\\max} - x_{\\min}$. Khoảng tứ phân vị $\\Delta_Q = Q_3 - Q_1$ đo độ phân tán của 50% số liệu ở trung tâm và không bị ảnh hưởng bởi các giá trị bất thường.",
                "formula": r"R = x_{\max} - x_{\min}; \quad \Delta_Q = Q_3 - Q_1",
                "trap": "Khoảng biến thiên R bị ảnh hưởng rất mạnh bởi các giá trị đột biến quá lớn hoặc quá nhỏ.",
                "audio": "Khoảng biến thiên bằng số lớn nhất trừ số nhỏ nhất. Khoảng tứ phân vị bằng Q3 trừ Q1 đo độ phân tán phần trung tâm.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng biến thiên",
                        "problem": "Cho mẫu số liệu: 3, 5, 7, 12. Tính khoảng biến thiên $R$.",
                        "solution": "- $R = x_{\\max} - x_{\\min} = 12 - 3 = 9$."
                    }
                ],
                "exercise": {"id": "10_14_1", "title": "Kiểm minh chứng", "content": "Mẫu số liệu có Q1 = 4 và Q3 = 10. Khoảng tứ phân vị delta_Q bằng:", "type": "NUMERIC", "target": "6", "options": []}
            },
            "2. Phương sai và Độ lệch chuẩn": {
                "theory": "Phương sai $s^2$ là trung bình cộng bình phương độ lệch giữa mỗi giá trị và số trung bình. Độ lệch chuẩn $s = \\sqrt{s^2}$. Chúng đo lường mức độ biến động xung quanh số trung bình.",
                "formula": r"s^2 = \frac{1}{n}\sum (x_i - \overline{x})^2; \quad s = \sqrt{s^2}",
                "trap": "Độ lệch chuẩn phải lấy căn bậc hai số học của phương sai, không được quên dấu căn.",
                "audio": "Phương sai và độ lệch chuẩn càng nhỏ thì dữ liệu càng tập trung đều đặn quanh số trung bình.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ lệch chuẩn",
                        "problem": "Biết phương sai của mẫu số liệu là $s^2 = 25$. Tìm độ lệch chuẩn $s$.",
                        "solution": "- $s = \\sqrt{s^2} = \\sqrt{25} = 5$."
                    }
                ],
                "exercise": {"id": "10_14_2", "title": "Kiểm minh chứng", "content": "Một mẫu có phương sai bằng 9 thì độ lệch chuẩn s bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 (PHẦN 2: BÀI 15 -> BÀI 27)
# Chuẩn hóa theo Vở tự học: Các chủ điểm là mục 1, 2, 3... thuộc PHẦN I
# ==============================================================================

GRADE_10_DATA.update({
    "Bài 15: Hàm số và đồ thị": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khái niệm hàm số và Tập xác định": {
                "theory": "Hàm số $y = f(x)$ xác định trên $D$ là quy tắc đặt tương ứng mỗi số $x \\in D$ với duy nhất một số $y \\in \\mathbb{R}$. Điều kiện xác định cơ bản: Phân thức $\\frac{A}{B}$ có nghĩa khi $B \\neq 0$; Căn thức bậc chẵn $\\sqrt{A}$ có nghĩa khi $A \\ge 0$.",
                "formula": r"\frac{A}{B} \implies B \neq 0; \quad \sqrt{A} \implies A \ge 0; \quad \frac{1}{\sqrt{A}} \implies A > 0",
                "trap": "Căn thức nằm ở mẫu số thì biểu thức trong căn phải LỚN HƠN 0 nghiêm ngặt ($A > 0$), tuyệt đối không lấy dấu bằng.",
                "audio": "Tìm tập xác định hàm số em nhớ hai điều cốt lõi: mẫu số phải khác không và biểu thức dưới căn bậc chẵn phải không âm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định chứa căn và mẫu",
                        "problem": "Tìm tập xác định của hàm số $y = \\frac{\\sqrt{x - 1}}{x - 3}$.",
                        "solution": "- Điều kiện xác định: $\\begin{cases} x - 1 \\ge 0 \\\\ x - 3 \\neq 0 \\end{cases} \\iff \\begin{cases} x \\ge 1 \\\\ x \\neq 3 \\end{cases}$.\n- Vậy tập xác định của hàm số là $D = [1; +\\infty) \\setminus \\{3\\}$."
                    }
                ],
                "exercise": {"id": "10_15_1", "title": "Kiểm minh chứng", "content": "Tập xác định của hàm số y = 1/căn(x - 2) có dạng (c; +vô cực). Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "2. Sự đồng biến, nghịch biến của hàm số": {
                "theory": "Hàm số đồng biến (tăng) trên khoảng $K$ nếu $x_1 < x_2 \\implies f(x_1) < f(x_2)$ (đồ thị đi lên từ trái sang phải). Hàm số nghịch biến (giảm) trên khoảng $K$ nếu $x_1 < x_2 \\implies f(x_1) > f(x_2)$ (đồ thị đi xuống từ trái sang phải).",
                "formula": r"\frac{f(x_2) - f(x_1)}{x_2 - x_1} > 0 \implies \text{Đồng biến}; \quad \frac{f(x_2) - f(x_1)}{x_2 - x_1} < 0 \implies \text{Nghịch biến}",
                "trap": "Khi quan sát đồ thị hàm số, mắt bắt buộc phải quét từ TRÁI sang PHẢI theo chiều tăng của trục hoành $Ox$.",
                "audio": "Nhìn đồ thị từ trái sang phải: đoạn nào đồ thị dốc lên là hàm số đồng biến, đoạn nào dốc xuống là hàm số nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đơn điệu bằng định nghĩa",
                        "problem": "Chứng minh hàm số $y = f(x) = 3x - 2$ đồng biến trên $\\mathbb{R}$.",
                        "solution": "- Lấy $x_1, x_2 \\in \\mathbb{R}$ tùy ý sao cho $x_1 < x_2 \\implies x_1 - x_2 < 0$.\n- Xét hiệu: $f(x_1) - f(x_2) = (3x_1 - 2) - (3x_2 - 2) = 3(x_1 - x_2) < 0$.\n- Vì $f(x_1) < f(x_2)$ nên hàm số luôn đồng biến trên $\\mathbb{R}$."
                    }
                ],
                "exercise": {"id": "10_15_2", "title": "Kiểm minh chứng", "content": "Hàm số y = -2x + 5 là hàm số đồng biến (1) hay nghịch biến (0) trên R?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 16: Hàm số bậc hai": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Đồ thị hàm số bậc hai (Parabol)": {
                "theory": "Đồ thị hàm số $y = ax^2 + bx + c$ ($a \\neq 0$) là đường parabol có đỉnh $I\\left(-\\frac{b}{2a}; -\\frac{\\Delta}{4a}\\right)$, trục đối xứng là đường thẳng $x = -\\frac{b}{2a}$. Bề lõm quay lên trên nếu $a > 0$, quay xuống dưới nếu $a < 0$.",
                "formula": r"x_I = -\frac{b}{2a}; \quad y_I = f(x_I)",
                "trap": "Học sinh thường nhớ sai dấu của hoành độ đỉnh parabol thành $\\frac{b}{2a}$ (quên dấu trừ).",
                "audio": "Đỉnh của parabol có hoành độ bằng trừ b trên 2a. Tung độ đỉnh em chỉ cần lấy hoành độ thay ngược vào hàm số ban đầu là xong.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tọa độ đỉnh parabol",
                        "problem": "Tìm tọa độ đỉnh $I$ của parabol $(P): y = x^2 - 4x + 3$.",
                        "solution": "- Hoành độ đỉnh: $x_I = -\\frac{-4}{2 \\cdot 1} = 2$.\n- Tung độ đỉnh: $y_I = 2^2 - 4(2) + 3 = -1$.\n- Vậy tọa độ đỉnh parabol là $I(2; -1)$."
                    }
                ],
                "exercise": {"id": "10_16_1", "title": "Kiểm minh chứng", "content": "Hoành độ đỉnh của parabol y = x^2 - 6x + 5 bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            },
            "2. Sự biến thiên và Giá trị lớn nhất, nhỏ nhất": {
                "theory": "Nếu $a > 0$: Hàm số nghịch biến trên $(-\\infty; -b/2a)$ và đồng biến trên $(-b/2a; +\\infty)$, đạt GTNN tại đỉnh. Nếu $a < 0$: Hàm số đồng biến trên $(-\\infty; -b/2a)$ và nghịch biến trên $(-b/2a; +\\infty)$, đạt GTLN tại đỉnh.",
                "formula": r"a > 0 \implies y_{\min} = f\left(-\frac{b}{2a}\right); \quad a < 0 \implies y_{\max} = f\left(-\frac{b}{2a}\right)",
                "trap": "Xác định nhầm dấu của hệ số $a$ sẽ làm đảo ngược hoàn toàn khoảng đồng biến, nghịch biến và đảo ngược GTLN thành GTNN.",
                "audio": "Khi a dương parabol ngửa lên nên đạt giá trị nhỏ nhất tại đáy. Khi a âm parabol úp xuống nên đạt giá trị lớn nhất tại đỉnh.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giá trị nhỏ nhất",
                        "problem": "Tìm giá trị nhỏ nhất của hàm số $y = x^2 - 4x + 7$.",
                        "solution": "- Hệ số $a = 1 > 0$ nên hàm số đạt GTNN tại đỉnh $x = -\\frac{-4}{2} = 2$.\n- $y_{\\min} = y(2) = 2^2 - 4(2) + 7 = 3$."
                    }
                ],
                "exercise": {"id": "10_16_2", "title": "Kiểm minh chứng", "content": "Giá trị lớn nhất của hàm số y = -x^2 + 2x + 3 bằng bao nhiêu?", "type": "NUMERIC", "target": "4", "options": []}
            }
        }
    },
    "Bài 17: Dấu của tam thức bậc hai": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Định lí về dấu của tam thức bậc hai": {
                "theory": "Cho $f(x) = ax^2 + bx + c$ ($a \\neq 0$). Nếu $\\Delta < 0$, $f(x)$ cùng dấu với $a$ với mọi $x \\in \\mathbb{R}$. Nếu $\\Delta = 0$, $f(x)$ cùng dấu với $a$ với mọi $x \\neq -b/2a$. Nếu $\\Delta > 0$, $f(x)$ có hai nghiệm $x_1 < x_2$ và tuân theo quy tắc: Trong trái dấu với a, ngoài cùng dấu với a.",
                "formula": r"\Delta < 0 \implies a \cdot f(x) > 0, \forall x \in \mathbb{R}; \quad \Delta > 0 \implies \text{Trong trái, Ngoài cùng}",
                "trap": "Quy tắc 'Trong trái ngoài cùng' chỉ áp dụng khi tam thức có 2 nghiệm phân biệt ($\\Delta > 0$). Khi $\\Delta < 0$ thì tam thức luôn mang cùng dấu với $a$.",
                "audio": "Quy tắc cốt lõi: Delta âm thì tam thức luôn cùng dấu với hệ số a. Delta dương thì trong khoảng hai nghiệm trái dấu với a, ngoài khoảng cùng dấu với a.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét dấu tam thức bậc hai",
                        "problem": "Xét dấu của tam thức bậc hai $f(x) = x^2 - 5x + 6$.",
                        "solution": "- Phương trình $f(x) = 0$ có 2 nghiệm phân biệt $x_1 = 2, x_2 = 3$.\n- Hệ số $a = 1 > 0$.\n- Trong khoảng $(2; 3)$: $f(x) < 0$ (trái dấu a).\n- Ngoài khoảng $(-\\infty; 2)$ và $(3; +\\infty)$: $f(x) > 0$ (cùng dấu a)."
                    }
                ],
                "exercise": {"id": "10_17_1", "title": "Kiểm minh chứng", "content": "Tam thức f(x) = x^2 - 4x + 3 mang dấu âm trên khoảng (1; c). Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "2. Bất phương trình bậc hai một ẩn": {
                "theory": "Bất phương trình bậc hai một ẩn là bất phương trình có dạng $f(x) > 0$ (hoặc $\\ge, <, \\le$). Giải BPT là tìm các khoảng mà tại đó tam thức $f(x)$ mang dấu phù hợp với chiều của BPT.",
                "formula": r"f(x) \ge 0 \implies \text{Lấy các khoảng mang dấu (+) kèm theo các nghiệm } f(x) = 0",
                "trap": "Khi bất phương trình có dấu bằng ($\\le, \\ge$), phải lấy ngoặc vuông `[]` tại các nghiệm của tam thức.",
                "audio": "Giải bất phương trình bậc hai bằng cách bấm máy tìm nghiệm, vẽ trục xét dấu trong trái ngoài cùng rồi lấy đúng khoảng nghiệm mà đề bài yêu cầu.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải bất phương trình bậc hai",
                        "problem": "Giải bất phương trình $x^2 - 3x - 4 \\le 0$.",
                        "solution": "- Tam thức có 2 nghiệm $x_1 = -1, x_2 = 4$; hệ số $a = 1 > 0$.\n- Dấu âm nằm bên trong hai nghiệm.\n- Vậy tập nghiệm của bất phương trình là đoạn $[-1; 4]$."
                    }
                ],
                "exercise": {"id": "10_17_2", "title": "Kiểm minh chứng", "content": "Tập nghiệm của bất phương trình x^2 - 9 < 0 là khoảng (-3; c). Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 18: Phương trình quy về phương trình bậc hai": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phương trình dạng căn f(x) = căn g(x)": {
                "theory": "Để giải phương trình $\\sqrt{f(x)} = \\sqrt{g(x)}$, ta bình phương hai vế đưa về $f(x) = g(x)$ rồi giải. Sau đó bắt buộc phải thay nghiệm tìm được vào kiểm tra xem biểu thức trong căn có $\\ge 0$ hay không.",
                "formula": r"\sqrt{f(x)} = \sqrt{g(x)} \implies f(x) = g(x) \quad (\text{Thử lại nghiệm})",
                "trap": "Bình phương hai vế là phép biến đổi hệ quả nên có thể sinh ra nghiệm ngoại lai. Bước thử lại nghiệm là bắt buộc.",
                "audio": "Dạng căn bằng căn chỉ cần bình phương hai vế cho mất căn rồi giải phương trình đại số, sau đó nhớ thử lại nghiệm vào đề bài.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình hai căn bậc hai",
                        "problem": "Giải phương trình $\\sqrt{2x + 3} = \\sqrt{x + 5}$.",
                        "solution": "- Bình phương hai vế: $2x + 3 = x + 5 \\iff x = 2$.\n- Thử lại: Với $x = 2$, $\\sqrt{7} = \\sqrt{7}$ (thỏa mãn).\n- Vậy phương trình có nghiệm duy nhất $x = 2$."
                    }
                ],
                "exercise": {"id": "10_18_1", "title": "Kiểm minh chứng", "content": "Nghiệm của phương trình căn(3x - 1) = căn(2x + 4) là x bằng bao nhiêu?", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Phương trình dạng căn f(x) = g(x)": {
                "theory": "Phương trình $\\sqrt{f(x)} = g(x)$ tương đương với hệ: $g(x) \\ge 0$ và $f(x) = [g(x)]^2$. Điều kiện $g(x) \\ge 0$ là bắt buộc trước khi bình phương hai vế.",
                "formula": r"\sqrt{f(x)} = g(x) \iff \begin{cases} g(x) \ge 0 \\ f(x) = [g(x)]^2 \end{cases}",
                "trap": "Quên đặt điều kiện $g(x) \\ge 0$ dẫn đến việc nhận nhầm nghiệm ngoại lai làm vế phải mang giá trị âm (vô lý vì căn bậc hai luôn không âm).",
                "audio": "Căn bằng một đa thức thì điều kiện sống còn là đa thức vế phải phải lớn hơn hoặc bằng không rồi mới được bình phương hai vế.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình căn bằng đa thức",
                        "problem": "Giải phương trình $\\sqrt{x^2 - 2x - 3} = x - 1$.",
                        "solution": "- Điều kiện vế phải: $x - 1 \\ge 0 \\iff x \\ge 1$.\n- Bình phương 2 vế: $x^2 - 2x - 3 = (x - 1)^2 \\iff x^2 - 2x - 3 = x^2 - 2x + 1$.\n- Suy ra $-3 = 1$ (vô lý). Phương trình vô nghiệm."
                    }
                ],
                "exercise": {"id": "10_18_2", "title": "Kiểm minh chứng", "content": "Số nghiệm của phương trình căn(x + 2) = -1 là bao nhiêu?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 19: Phương trình đường thẳng": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Vectơ chỉ phương và Vectơ pháp tuyến": {
                "theory": "Vectơ chỉ phương (VTCP) $\\vec{u} \\neq \\vec{0}$ có giá song song hoặc trùng với đường thẳng. Vectơ pháp tuyến (VTPT) $\\vec{n} \\neq \\vec{0}$ có giá vuông góc với đường thẳng. Nếu $\\vec{n} = (A; B)$ thì một VTCP là $\\vec{u} = (-B; A)$.",
                "formula": r"\vec{n} = (A; B) \iff \vec{u} = (-B; A); \quad \vec{n} \cdot \vec{u} = 0",
                "trap": "Đổi từ VTPT sang VTCP quên đổi dấu một tọa độ (ví dụ $(2; 3)$ đổi thành $(3; 2)$ thay vì $(-3; 2)$).",
                "audio": "Pháp tuyến thì vuông góc, chỉ phương thì song song. Muốn đổi từ pháp tuyến sang chỉ phương ta đảo vị trí hai số và thêm một dấu trừ.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chuyển đổi giữa hai loại vectơ",
                        "problem": "Đường thẳng $\\Delta$ có VTPT $\\vec{n} = (3; -4)$. Tìm một VTCP của $\\Delta$.",
                        "solution": "- Đảo vị trí và đổi dấu một tọa độ: $\\vec{u} = (4; 3)$."
                    }
                ],
                "exercise": {"id": "10_19_1", "title": "Kiểm minh chứng", "content": "Đường thẳng có VTPT n = (1; 2) thì một VTCP u = (-2; b). Giá trị b bằng:", "type": "NUMERIC", "target": "1", "options": []}
            },
            "2. Phương trình tổng quát và Phương trình tham số": {
                "theory": "Phương trình tổng quát qua $M_0(x_0; y_0)$ có VTPT $\\vec{n}=(A; B)$ là $Ax + By + C = 0$. Phương trình tham số qua $M_0(x_0; y_0)$ có VTCP $\\vec{u}=(u_1; u_2)$ là $\\begin{cases} x = x_0 + u_1 t \\\\ y = y_0 + u_2 t \\end{cases}$.",
                "formula": r"A(x - x_0) + B(y - y_0) = 0 \iff Ax + By + C = 0; \quad \begin{cases} x = x_0 + u_1 t \\ y = y_0 + u_2 t \end{cases}",
                "trap": "Học sinh thường nhầm vị trí tọa độ điểm đi qua và tọa độ vectơ khi viết phương trình tham số.",
                "audio": "Phương trình tổng quát gắn liền với vectơ pháp tuyến, phương trình tham số gắn liền với vectơ chỉ phương và tham số t.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập phương trình tổng quát",
                        "problem": "Lập PTTQ của đường thẳng đi qua $A(1; -2)$ và có VTPT $\\vec{n} = (3; 2)$.",
                        "solution": "- Phương trình: $3(x - 1) + 2(y - (-2)) = 0 \\iff 3x + 2y + 1 = 0$."
                    }
                ],
                "exercise": {"id": "10_19_2", "title": "Kiểm minh chứng", "content": "Đường thẳng x = 2 + 3t; y = -1 + 4t đi qua điểm M(2; c). Giá trị c bằng:", "type": "NUMERIC", "target": "-1", "options": []}
            }
        }
    },
    "Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Vị trí tương đối và Góc giữa hai đường thẳng": {
                "theory": "Vị trí tương đối xác định bằng số nghiệm của hệ phương trình 2 đường thẳng. Cosin góc giữa hai đường thẳng bằng trị tuyệt đối cosin góc giữa hai VTPT.",
                "formula": r"\cos(\Delta_1, \Delta_2) = \frac{|\vec{n_1} \cdot \vec{n_2}|}{|\vec{n_1}| \cdot |\vec{n_2}|} \quad (0^\circ \le \varphi \le 90^\circ)",
                "trap": "Góc giữa hai đường thẳng luôn là góc nhọn hoặc góc vuông nên tử số của công thức cosin bắt buộc phải có dấu giá trị tuyệt đối.",
                "audio": "Góc giữa hai đường thẳng không bao giờ là góc tù nên công thức cosin luôn có trị tuyệt đối ở tử số.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa hai đường thẳng",
                        "problem": "Tính góc giữa $\\Delta_1: x - 2y + 1 = 0$ và $\\Delta_2: 2x + y - 5 = 0$.",
                        "solution": "- $\\vec{n_1} = (1; -2), \\vec{n_2} = (2; 1)$.\n- Tích vô hướng: $\\vec{n_1} \\cdot \\vec{n_2} = 1(2) + (-2)(1) = 0$.\n- Vì tích vô hướng bằng 0 nên góc giữa hai đường thẳng bằng $90^\\circ$."
                    }
                ],
                "exercise": {"id": "10_20_1", "title": "Kiểm minh chứng", "content": "Hai đường thẳng vuông góc tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "2. Khoảng cách từ một điểm đến đường thẳng": {
                "theory": "Khoảng cách từ điểm $M_0(x_0; y_0)$ đến đường thẳng $\\Delta: Ax + By + C = 0$ bằng trị tuyệt đối khi thay tọa độ điểm vào vế trái chia cho độ dài VTPT.",
                "formula": r"d(M_0, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
                "trap": "Học sinh thường quên căn bậc hai $\\sqrt{A^2 + B^2}$ ở mẫu số.",
                "audio": "Tính khoảng cách từ điểm đến đường thẳng: thay tọa độ điểm vào tử số lấy trị tuyệt đối, mẫu số là độ dài vectơ pháp tuyến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách",
                        "problem": "Tính khoảng cách từ điểm $A(2; -1)$ đến đường thẳng $\\Delta: 3x - 4y + 5 = 0$.",
                        "solution": "- $d(A, \\Delta) = \\frac{|3(2) - 4(-1) + 5|}{\\sqrt{3^2 + (-4)^2}} = \\frac{|6 + 4 + 5|}{5} = \\frac{15}{5} = 3$."
                    }
                ],
                "exercise": {"id": "10_20_2", "title": "Kiểm minh chứng", "content": "Khoảng cách từ gốc tọa độ O(0; 0) đến đường thẳng 3x + 4y - 15 = 0 bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 21: Đường tròn trong mặt phẳng tọa độ": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Phương trình đường tròn": {
                "theory": "Phương trình chính tắc tâm $I(a; b)$ bán kính $R$ là $(x - a)^2 + (y - b)^2 = R^2$. Phương trình khai triển $x^2 + y^2 - 2ax - 2by + c = 0$ là đường tròn khi và chỉ khi $a^2 + b^2 - c > 0$ với $R = \\sqrt{a^2 + b^2 - c}$.",
                "formula": r"(x - a)^2 + (y - b)^2 = R^2; \quad R = \sqrt{a^2 + b^2 - c}",
                "trap": "Khi đọc tọa độ tâm từ dạng khai triển, phải lấy hệ số của x và y chia cho -2.",
                "audio": "Phương trình đường tròn chính tắc giúp đọc ngay tâm và bán kính. Với dạng khai triển nhớ chia hệ số x và y cho trừ 2 để tìm tâm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tâm và bán kính từ dạng khai triển",
                        "problem": "Tìm tâm $I$ và bán kính $R$ của $(C): x^2 + y^2 - 6x + 2y - 6 = 0$.",
                        "solution": "- $a = -6/(-2) = 3; b = 2/(-2) = -1; c = -6$.\n- Tâm $I(3; -1)$. Bán kính $R = \\sqrt{3^2 + (-1)^2 - (-6)} = \\sqrt{9 + 1 + 6} = 4$."
                    }
                ],
                "exercise": {"id": "10_21_1", "title": "Kiểm minh chứng", "content": "Đường tròn (x - 2)^2 + (y + 1)^2 = 25 có bán kính R bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Phương trình tiếp tuyến của đường tròn": {
                "theory": "Tiếp tuyến của $(C)$ tại điểm $M_0(x_0; y_0) \\in (C)$ nhận vectơ $\\vec{IM_0}$ làm vectơ pháp tuyến.",
                "formula": r"(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0",
                "trap": "Tiếp tuyến TẠI một điểm trên đường tròn khác với tiếp tuyến KẺ TỪ một điểm bên ngoài đường tròn.",
                "audio": "Tiếp tuyến tại một điểm trên đường tròn luôn vuông góc với bán kính đi qua tiếp điểm đó.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết phương trình tiếp tuyến tại tiếp điểm",
                        "problem": "Viết PTTT của $(C): (x - 1)^2 + (y - 2)^2 = 25$ tại điểm $M(4; 6)$.",
                        "solution": "- Tâm $I(1; 2)$. Vectơ pháp tuyến $\\vec{IM} = (3; 4)$.\n- Phương trình tiếp tuyến: $3(x - 4) + 4(y - 6) = 0 \\iff 3x + 4y - 36 = 0$."
                    }
                ],
                "exercise": {"id": "10_21_2", "title": "Kiểm minh chứng", "content": "Khoảng cách từ tâm đường tròn đến tiếp tuyến đúng bằng bán kính R. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 22: Ba đường conic": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Đường Elip": {
                "theory": "Phương trình chính tắc của elip là $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ ($a > b > 0$). Hai tiêu điểm $F_1(-c; 0), F_2(c; 0)$ với $c^2 = a^2 - b^2$. Độ dài trục lớn $2a$, trục nhỏ $2b$, tiêu cự $2c$.",
                "formula": r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a^2 = b^2 + c^2)",
                "trap": "Học sinh hay nhầm hệ thức elip $a^2 = b^2 + c^2$ với định lý Pytago.",
                "audio": "Trong elip, a là bán trục lớn nhất: a bình bằng b bình cộng c bình. Trục lớn là 2a và tiêu cự là 2c.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định các yếu tố của Elip",
                        "problem": "Tìm độ dài trục lớn và tiêu cự của Elip $(E): \\frac{x^2}{25} + \\frac{y^2}{9} = 1$.",
                        "solution": "- $a^2 = 25 \\implies a = 5$. Độ dài trục lớn $2a = 10$.\n- $b^2 = 9 \\implies c^2 = a^2 - b^2 = 25 - 9 = 16 \\implies c = 4$. Tiêu cự $2c = 8$."
                    }
                ],
                "exercise": {"id": "10_22_1", "title": "Kiểm minh chứng", "content": "Elip x^2/25 + y^2/9 = 1 có độ dài trục lớn 2a bằng:", "type": "NUMERIC", "target": "10", "options": []}
            },
            "2. Đường Hypebol và Parabol": {
                "theory": "Hypebol có PTCT $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$. Parabol có PTCT $y^2 = 2px$ ($p > 0$) với tiêu điểm $F(p/2; 0)$ và đường chuẩn $x = -p/2$.",
                "formula": r"\text{Hypebol: } c^2 = a^2 + b^2; \quad \text{Parabol: } y^2 = 2px",
                "trap": "Hypebol phương trình có dấu TRỪ giữa hai phân thức, nhưng liên hệ $c^2 = a^2 + b^2$ lại có dấu CỘNG.",
                "audio": "Hypebol phương trình mang dấu trừ, liên hệ c bình bằng a bình cộng b bình. Parabol có phương trình chính tắc y bình bằng 2 p x.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tham số tiêu của Parabol",
                        "problem": "Tìm tiêu điểm của parabol $(P): y^2 = 8x$.",
                        "solution": "- Ta có $2p = 8 \\implies p = 4$.\n- Tiêu điểm $F(p/2; 0) = F(2; 0)$."
                    }
                ],
                "exercise": {"id": "10_22_2", "title": "Kiểm minh chứng", "content": "Parabol y^2 = 6x có tham số tiêu p bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 23: Quy tắc đếm": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Quy tắc cộng và Sơ đồ cây": {
                "theory": "Một công việc được hoàn thành bởi một trong hai hành động không giao nhau: hành động 1 có $m$ cách, hành động 2 có $n$ cách $\implies$ Có $m + n$ cách hoàn thành công việc.",
                "formula": r"N = m + n",
                "trap": "Chỉ dùng quy tắc cộng khi các phương án hoàn toàn tách rời nhau (không có phần tử trùng lặp).",
                "audio": "Làm phương án này HOẶC phương án kia thì ta dùng quy tắc cộng. Công việc hoàn thành ngay trong từng phương án.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc cộng",
                        "problem": "Một kệ sách có 4 cuốn Toán và 6 cuốn Văn. Có bao nhiêu cách chọn 1 cuốn sách?",
                        "solution": "- Chọn 1 cuốn Toán (4 cách) hoặc 1 cuốn Văn (6 cách).\n- Số cách chọn là: $4 + 6 = 10$ cách."
                    }
                ],
                "exercise": {"id": "10_23_1", "title": "Kiểm minh chứng", "content": "Có 5 áo trắng và 4 áo xanh. Số cách chọn 1 chiếc áo để mặc là:", "type": "NUMERIC", "target": "9", "options": []}
            },
            "2. Quy tắc nhân": {
                "theory": "Một công việc gồm hai công đoạn liên tiếp: công đoạn 1 có $m$ cách, với mỗi cách đó công đoạn 2 có $n$ cách $\implies$ Có $m \\cdot n$ cách hoàn thành công việc.",
                "formula": r"N = m \cdot n",
                "trap": "Muốn xong việc phải làm bước 1 VÀ bước 2 thì bắt buộc phải dùng phép nhân.",
                "audio": "Phải trải qua nhiều công đoạn nối tiếp nhau mới xong công việc thì ta nhân số cách của từng công đoạn lại với nhau.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập số tự nhiên",
                        "problem": "Từ tập {1, 2, 3} có thể lập được bao nhiêu số có 2 chữ số khác nhau?",
                        "solution": "- Hàng chục có 3 cách chọn.\n- Hàng đơn vị có 2 cách chọn (khác hàng chục).\n- Số các số lập được: $3 \\cdot 2 = 6$ số."
                    }
                ],
                "exercise": {"id": "10_23_2", "title": "Kiểm minh chứng", "content": "Có 3 quần và 4 áo. Số cách chọn 1 bộ gồm 1 quần và 1 áo là:", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 24: Hoán vị, chỉnh hợp và tổ hợp": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Hoán vị và Chỉnh hợp": {
                "theory": "Hoán vị $n$ phần tử: $P_n = n!$. Chỉnh hợp chập $k$ của $n$: Chọn $k$ phần tử từ $n$ phần tử VÀ SẮP THỨ TỰ chúng: $A_n^k = \\frac{n!}{(n - k)!}$.",
                "formula": r"P_n = n!; \quad A_n^k = \frac{n!}{(n - k)!}",
                "trap": "Cứ bài toán có yếu tố 'xếp hàng', 'phân chức vụ', 'lập số' (thay đổi thứ tự tạo ra kết quả mới) là dùng chỉnh hợp.",
                "audio": "Chọn phần tử mà có sắp xếp vị trí trước sau thì dùng chỉnh hợp A. Đổi chỗ toàn bộ n phần tử thì dùng hoán vị n giai thừa.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bầu ban cán sự (Chỉnh hợp)",
                        "problem": "Một tổ có 8 học sinh. Cần bầu ra 1 tổ trưởng và 1 tổ phó. Có bao nhiêu cách?",
                        "solution": "- Chọn 2 bạn và phân công 2 chức vụ (có thứ tự): $A_8^2 = \\frac{8!}{6!} = 8 \\cdot 7 = 56$ cách."
                    }
                ],
                "exercise": {"id": "10_24_1", "title": "Kiểm minh chứng", "content": "Giá trị của P_3 (3 giai thừa) bằng bao nhiêu?", "type": "NUMERIC", "target": "6", "options": []}
            },
            "2. Tổ hợp": {
                "theory": "Tổ hợp chập $k$ của $n$ phần tử: Chọn $k$ phần tử từ $n$ phần tử KHÔNG QUAN TÂM THỨ TỰ. Công thức: $C_n^k = \\frac{n!}{k!(n - k)!}$.",
                "formula": r"C_n^k = \frac{n!}{k!(n - k)!}",
                "trap": "Nhầm lẫn giữa Tổ hợp ($C$) và Chỉnh hợp ($A$). Không phân biệt thứ tự (chọn nhóm, chọn đội) thì dùng $C$.",
                "audio": "Chọn một nhóm người hay bốc một vốc bi mà không phân biệt ai trước ai sau thì dùng tổ hợp C.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chọn nhóm học sinh",
                        "problem": "Một lớp có 20 học sinh. Có bao nhiêu cách chọn ra một nhóm 2 học sinh đi trực nhật?",
                        "solution": "- Chọn 2 học sinh không phân công chức vụ: $C_{20}^2 = \\frac{20 \\cdot 19}{2} = 190$ cách."
                    }
                ],
                "exercise": {"id": "10_24_2", "title": "Kiểm minh chứng", "content": "Giá trị của tổ hợp C_6^2 bằng bao nhiêu?", "type": "NUMERIC", "target": "15", "options": []}
            }
        }
    },
    "Bài 25: Nhị thức Newton": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Khai triển nhị thức Newton bậc 4 và bậc 5": {
                "theory": "Khai triển $(a + b)^4$ có 5 số hạng và $(a + b)^5$ có 6 số hạng. Hệ số đối xứng qua trung tâm, tính bằng các tổ hợp $C_n^k$.",
                "formula": r"(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4",
                "trap": "Khi khai triển biểu thức có dấu trừ như $(a - b)^n$, dấu của các số hạng xen kẽ nhau: cộng rồi trừ.",
                "audio": "Nhị thức Newton bậc 4 và 5 có công thức hệ số đối xứng. Khi khai triển có dấu trừ, nhớ đan xen dấu cộng trừ liên tiếp.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Khai triển nhị thức bậc 4",
                        "problem": "Khai triển biểu thức $(x + 1)^4$.",
                        "solution": "- $(x + 1)^4 = x^4 + 4x^3(1) + 6x^2(1^2) + 4x(1^3) + 1^4 = x^4 + 4x^3 + 6x^2 + 4x + 1$."
                    }
                ],
                "exercise": {"id": "10_25_1", "title": "Kiểm minh chứng", "content": "Khai triển (x + 2)^4 có tất cả bao nhiêu số hạng?", "type": "NUMERIC", "target": "5", "options": []}
            },
            "2. Ứng dụng xác định hệ số số hạng": {
                "theory": "Để tìm hệ số của số hạng chứa $x^k$ trong khai triển, ta xác định số hạng tổng quát rồi cho số mũ của $x$ bằng $k$ để tìm hệ số tương ứng.",
                "formula": r"T_{k+1} = C_n^k a^{n-k} b^k",
                "trap": "Học sinh hay nhầm lẫn giữa 'hệ số của số hạng' (chỉ lấy phần số) và 'số hạng' (bao gồm cả phần biến x).",
                "audio": "Muốn tìm hệ số của số hạng chứa x mũ k, em lập số hạng tổng quát rồi cho số mũ bằng k để rút ra hệ số số học.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm hệ số của x^3",
                        "problem": "Tìm hệ số của $x^3$ trong khai triển $(x + 2)^4$.",
                        "solution": "- Số hạng chứa $x^3$ là $4x^3(2) = 8x^3$.\n- Vậy hệ số của $x^3$ là 8."
                    }
                ],
                "exercise": {"id": "10_25_2", "title": "Kiểm minh chứng", "content": "Hệ số của x^4 trong khai triển (x + 3)^4 bằng bao nhiêu?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 26: Biến cố và định nghĩa cổ điển của xác suất": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Không gian mẫu và Biến cố": {
                "theory": "Không gian mẫu $\\Omega$ là tập hợp tất cả các kết quả có thể xảy ra của phép thử. Biến cố $A$ là một tập con của không gian mẫu $\\Omega$.",
                "formula": r"A \subset \Omega",
                "trap": "Liệt kê thiếu kết quả của không gian mẫu sẽ dẫn đến mẫu số bị sai.",
                "audio": "Không gian mẫu gom tất cả các kết quả có thể xảy ra. Biến cố là tập con gồm các kết quả thỏa mãn điều kiện đề bài.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định không gian mẫu",
                        "problem": "Gieo một đồng xu cân đối 2 lần liên tiếp. Liệt kê không gian mẫu.",
                        "solution": "- $\\Omega = \\{SS, SN, NS, NN\\} \\implies n(\\Omega) = 4$."
                    }
                ],
                "exercise": {"id": "10_26_1", "title": "Kiểm minh chứng", "content": "Gieo con xúc xắc 6 mặt một lần. Số phần tử của không gian mẫu n(Omega) bằng:", "type": "NUMERIC", "target": "6", "options": []}
            },
            "2. Định nghĩa cổ điển của xác suất": {
                "theory": "Xác suất của biến cố $A$ bằng số kết quả thuận lợi cho $A$ chia cho tổng số kết quả của không gian mẫu: $P(A) = \\frac{n(A)}{n(\\Omega)}$. Luôn có $0 \\le P(A) \\le 1$.",
                "formula": r"P(A) = \frac{n(A)}{n(\Omega)} \quad (0 \le P(A) \le 1)",
                "trap": "Xác suất luôn nằm trong đoạn $[0; 1]$. Nếu tính ra số âm hoặc lớn hơn 1 thì chắc chắn đã làm sai.",
                "audio": "Xác suất bằng số kết quả thuận lợi cho biến cố chia cho tổng số phần tử không gian mẫu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất con xúc xắc",
                        "problem": "Gieo con xúc xắc cân đối. Tính xác suất xuất hiện mặt có số chấm chia hết cho 2.",
                        "solution": "- $n(\\Omega) = 6$.\n- Mặt chia hết cho 2: $A = \\{2; 4; 6\\} \\implies n(A) = 3$.\n- Xác suất $P(A) = 3/6 = 0.5$."
                    }
                ],
                "exercise": {"id": "10_26_2", "title": "Kiểm minh chứng", "content": "Gieo xúc xắc 6 mặt, xác suất xuất hiện mặt 1 chấm bằng bao nhiêu? (Dạng 1/c, c bằng:)", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển": {
        "chapter": "PHẦN I. TÓM TẮT LÝ THUYẾT VÀ VÍ DỤ MINH HOẠ",
        "topics": {
            "1. Tính xác suất bằng sơ đồ cây": {
                "theory": "Sơ đồ cây phân nhánh các giai đoạn thử nghiệm, giúp đếm chính xác số kết quả có thể xảy ra và số kết quả thuận lợi mà không bị bỏ sót.",
                "formula": r"P(A) = \frac{n(A)}{n(\Omega)}",
                "trap": "Quên không phân nhánh các trường hợp đối ngẫu dẫn đến thiếu phần tử không gian mẫu.",
                "audio": "Sơ đồ cây vẽ rẽ nhánh từng bước giúp em không bao giờ bị đếm trùng hoặc đếm sót các trường hợp.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Dùng sơ đồ cây cho đồng xu",
                        "problem": "Gieo đồng xu 3 lần. Tính xác suất có đúng 2 lần xuất hiện mặt ngửa.",
                        "solution": "- Không gian mẫu có $2^3 = 8$ nhánh.\n- Các nhánh có đúng 2 mặt ngửa: $\\{NNS, NSN, SNN\\} \\implies n(A) = 3$.\n- Xác suất $P(A) = 3/8 = 0.375$."
                    }
                ],
                "exercise": {"id": "10_27_1", "title": "Kiểm minh chứng", "content": "Gieo đồng xu 3 lần, tổng số kết quả có thể xảy ra ở không gian mẫu là:", "type": "NUMERIC", "target": "8", "options": []}
            },
            "2. Tính xác suất bằng phương pháp tổ hợp": {
                "theory": "Dùng công thức tổ hợp $C_n^k$ để tính số phần tử của không gian mẫu và biến cố khi lấy đồng thời nhiều phần tử từ một tập hợp.",
                "formula": r"P(A) = \frac{C_a^k \cdot C_b^m}{C_n^{k+m}}",
                "trap": "Rút đồng thời nhiều viên bi thì dùng Tổ hợp ($C$), không dùng Chỉnh hợp ($A$).",
                "audio": "Khi bốc cùng lúc nhiều đồ vật ra khỏi hộp, hãy dùng tổ hợp C để tính số phần tử không gian mẫu và biến cố.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút bi từ hộp",
                        "problem": "Hộp có 5 bi xanh và 3 bi đỏ. Lấy ngẫu nhiên 2 viên bi. Tính xác suất để lấy được 2 viên bi đỏ.",
                        "solution": "- $n(\\Omega) = C_8^2 = 28$.\n- Lấy 2 bi đỏ: $n(A) = C_3^2 = 3$.\n- Xác suất $P(A) = \\frac{3}{28}$."
                    }
                ],
                "exercise": {"id": "10_27_2", "title": "Kiểm minh chứng", "content": "Lấy ngẫu nhiên 2 viên bi từ hộp có 6 viên bi. Số phần tử không gian mẫu n(Omega) bằng:", "type": "NUMERIC", "target": "15", "options": []}
            }
        }
    }
})
