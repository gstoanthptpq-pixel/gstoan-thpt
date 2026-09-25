# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 KẾT NỐI TRI THỨC (PHẦN 1: BÀI 1 -> BÀI 9)
# ==============================================================================

GRADE_10_DATA = {}

GRADE_10_DATA.update({
    "Bài 1: Mệnh đề toán học": {
        "chapter": "Chương I: Mệnh đề và tập hợp",
        "topics": {
            "Chủ điểm 1: Khái niệm mệnh đề toán học": {
                "theory": "Mệnh đề toán học là một khẳng định có tính đúng hoặc sai tuyệt đối. Không có mệnh đề nào vừa đúng vừa sai hoặc không biết được tính đúng sai. Câu hỏi, câu cảm thán, câu mệnh lệnh không phải là mệnh đề.",
                "formula": r"P \in \{\text{Đúng}, \text{Sai}\}",
                "trap": "Mệnh đề chứa biến (ví dụ: $x > 5$) CHƯA PHẢI là mệnh đề toán học, vì tính đúng sai của nó phụ thuộc vào giá trị của x. Chỉ khi thay x bằng một số cụ thể, nó mới trở thành mệnh đề.",
                "audio": "Mệnh đề là một câu khẳng định chỉ nhận một trong hai giá trị là đúng hoặc sai. Câu cảm thán hay câu hỏi tuyệt đối không phải là mệnh đề nhé.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện mệnh đề",
                        "problem": "Trong các câu sau: (1) 'Trời hôm nay đẹp quá!', (2) 'Số 15 là số nguyên tố', (3) '2 + 3 = 5'. Câu nào là mệnh đề?",
                        "solution": "- Câu (1) là câu cảm thán $\\implies$ Không phải mệnh đề.\n- Câu (2) là khẳng định sai $\\implies$ Là mệnh đề toán học (Mệnh đề Sai).\n- Câu (3) là khẳng định đúng $\\implies$ Là mệnh đề toán học (Mệnh đề Đúng)."
                    },
                    {
                        "title": "Ví dụ 2: Mệnh đề chứa biến",
                        "problem": "Phát biểu '$P(x): x^2 + 1 > 0$' có phải là mệnh đề không?",
                        "solution": "- Đây là một mệnh đề chứa biến, bản thân nó chưa phải là mệnh đề.\n- Nhưng nếu thêm lượng từ 'Với mọi x thuộc R' thì nó trở thành một mệnh đề đúng."
                    }
                ],
                "exercise": {
                    "id": "10_1_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Trong các câu: 'Hôm nay ăn gì?', '2 < 1', 'x + 1 = 3'. Có bao nhiêu câu là mệnh đề toán học?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Mệnh đề phủ định và Lượng từ": {
                "theory": "Phủ định của mệnh đề P là $\\overline{P}$. Phủ định của 'Đúng' là 'Sai'. Ký hiệu $\\forall$ đọc là 'với mọi', $\\exists$ đọc là 'tồn tại'. Phủ định của $\\forall$ là $\\exists$, phủ định của $>$ là $\\le$.",
                "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
                "trap": "Sai lầm kinh điển: Học sinh lấy phủ định của dấu LỚN HƠN ($>$) thành dấu NHỎ HƠN ($<$). Sự thật là phải lấy NHỎ HƠN HOẶC BẰNG ($\\le$).",
                "audio": "Phủ định của với mọi là tồn tại, phủ định của tồn tại là với mọi. Đặc biệt lưu ý, phủ định của dấu lớn hơn là nhỏ hơn hoặc bằng.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết mệnh đề phủ định",
                        "problem": "Viết mệnh đề phủ định của $P$: 'Mọi số thực x đều có $x^2 \\ge 0$'.",
                        "solution": "- Lượng từ 'Mọi' ($\\forall$) đổi thành 'Tồn tại' ($\\exists$).\n- Dấu '$\\ge$' đổi thành dấu '$<$'.\n- Mệnh đề phủ định $\\overline{P}$: 'Tồn tại số thực x sao cho $x^2 < 0$'."
                    },
                    {
                        "title": "Ví dụ 2: Xét tính đúng sai của mệnh đề chứa lượng từ",
                        "problem": "Mệnh đề '$\\exists x \\in \\mathbb{R}, x^2 - x + 1 = 0$' đúng hay sai?",
                        "solution": "- Xét phương trình $x^2 - x + 1 = 0$, có $\\Delta = 1^2 - 4(1)(1) = -3 < 0$.\n- Phương trình vô nghiệm trên $\\mathbb{R}$, tức là không tồn tại x thỏa mãn.\n- **Kết luận:** Mệnh đề Sai."
                    }
                ],
                "exercise": {
                    "id": "10_1_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Phủ định của x > 5 là x <= c. Giá trị của c bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            }
        }
    },
    "Bài 2: Tập hợp và các phép toán trên tập hợp": {
        "chapter": "Chương I: Mệnh đề và tập hợp",
        "topics": {
            "Chủ điểm 1: Khái niệm tập hợp và Tập con": {
                "theory": "Tập hợp có thể xác định bằng cách liệt kê phần tử hoặc chỉ ra tính chất đặc trưng. $A$ là tập con của $B$ ($A \\subset B$) nếu MỌI phần tử của $A$ đều thuộc $B$. Tập rỗng $\\emptyset$ là tập con của mọi tập hợp.",
                "formula": r"A \subset B \iff (\forall x \in A \implies x \in B)",
                "trap": "Ký hiệu $\\in$ dùng giữa PHẦN TỬ và TẬP HỢP. Ký hiệu $\\subset$ dùng giữa HAI TẬP HỢP. Viết $1 \\subset A$ là sai, phải viết $1 \\in A$.",
                "audio": "Tập hợp rỗng là tập con của mọi tập hợp. Nhớ kỹ sự khác biệt giữa thuộc và là tập con: một bên dùng cho phần tử, một bên dùng cho tập hợp nhé.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm số phần tử của tập hợp",
                        "problem": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid x < 5\\}$. Liệt kê các phần tử của A.",
                        "solution": "- Tập số tự nhiên $\\mathbb{N} = \\{0, 1, 2, 3, 4, 5, \\dots\\}$.\n- Các số nhỏ hơn 5: $0, 1, 2, 3, 4$.\n- $A = \\{0; 1; 2; 3; 4\\}$. Tập A có 5 phần tử."
                    },
                    {
                        "title": "Ví dụ 2: Liệt kê các tập con",
                        "problem": "Tập hợp $B = \\{1; 2\\}$ có bao nhiêu tập hợp con?",
                        "solution": "- Tập con không có phần tử nào: $\\emptyset$.\n- Tập con có 1 phần tử: $\\{1\\}, \\{2\\}$.\n- Tập con có 2 phần tử: $\\{1; 2\\}$.\n- **Kết luận:** Có tất cả 4 tập con. Công thức nhanh là $2^n = 2^2 = 4$."
                    }
                ],
                "exercise": {
                    "id": "10_2_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tập hợp C = {1; 2; 3} có tổng cộng bao nhiêu tập hợp con?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            },
            "Chủ điểm 2: Giao, Hợp và Hiệu của hai tập hợp": {
                "theory": "Phép Giao ($A \\cap B$): Lấy phần tử CHUNG. Phép Hợp ($A \\cup B$): Lấy TẤT CẢ các phần tử (không lặp lại). Phép Hiệu ($A \\setminus B$): Lấy những phần tử THUỘC A nhưng KHÔNG THUỘC B.",
                "formula": r"A \cap B = \{x \mid x \in A, x \in B\}; \quad A \setminus B = \{x \mid x \in A, x \notin B\}",
                "trap": "Khi thực hiện phép toán trên các khoảng/đoạn số thực, học sinh vẽ trục số nhưng thường gạch sai phần dư, hoặc nhầm ngoặc vuông thành ngoặc tròn ở các điểm đầu mút.",
                "audio": "Giao là lấy phần chung, hợp là lấy tất cả. Còn hiệu A trừ B là giữ lại những gì của riêng A mà B không có.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phép toán trên tập hợp liệt kê",
                        "problem": "Cho $A = \\{1; 2; 3; 4\\}$ và $B = \\{3; 4; 5\\}$. Tìm $A \\cap B$ và $A \\setminus B$.",
                        "solution": "- Phần tử chung của cả A và B là 3, 4 $\\implies A \\cap B = \\{3; 4\\}$.\n- Thuộc A nhưng không thuộc B là 1, 2 $\\implies A \\setminus B = \\{1; 2\\}$."
                    },
                    {
                        "title": "Ví dụ 2: Phép toán trên trục số",
                        "problem": "Cho hai khoảng $A = (1; 5)$ và $B = [3; 7]$. Tìm $A \\cap B$.",
                        "solution": "- Biểu diễn trên trục số, ta lấy phần giao nhau giữa $(1; 5)$ và $[3; 7]$.\n- Đầu mút bên trái giao nhau bắt đầu từ 3 (có dấu ngoặc vuông).\n- Đầu mút bên phải kết thúc tại 5 (có dấu ngoặc tròn).\n- **Kết luận:** $A \\cap B = [3; 5)$."
                    }
                ],
                "exercise": {
                    "id": "10_2_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho A = [1; 4] và B = (2; 6). Có bao nhiêu số nguyên thuộc A giao B?", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 3: Bất phương trình bậc nhất hai ẩn": {
        "chapter": "Chương II: Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
        "topics": {
            "Chủ điểm 1: Khái niệm và Biểu diễn miền nghiệm": {
                "theory": "Bất phương trình bậc nhất 2 ẩn có dạng $ax + by \\le c$. Miền nghiệm của nó là một nửa mặt phẳng có bờ là đường thẳng $d: ax + by = c$. Để xác định miền nghiệm, ta chọn một điểm thử (thường là gốc tọa độ $O(0;0)$) không nằm trên bờ $d$, thay vào BPT để xét đúng sai.",
                "formula": r"ax + by \le c \quad (a^2 + b^2 > 0)",
                "trap": "Nếu BPT có dấu '$\\le$' hoặc '$\\ge$', ta vẽ bờ d bằng nét LIỀN. Nếu chỉ có '$<$' hoặc '$>$', ta phải vẽ bờ d bằng nét ĐỨT.",
                "audio": "Để biểu diễn miền nghiệm, em vẽ đường thẳng trước. Sau đó lấy điểm O không không thay vào. Nếu đúng thì gạch bỏ nửa kia, nếu sai thì gạch bỏ nửa chứa điểm O.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Điểm thuộc miền nghiệm",
                        "problem": "Điểm $M(1; -2)$ có thuộc miền nghiệm của bất phương trình $2x + y > 1$ không?",
                        "solution": "- Thay tọa độ $x = 1, y = -2$ vào vế trái của BPT:\n- $VT = 2(1) + (-2) = 2 - 2 = 0$.\n- Xét thấy $0 > 1$ là một mệnh đề Sai.\n- **Kết luận:** M không thuộc miền nghiệm."
                    },
                    {
                        "title": "Ví dụ 2: Xác định nửa mặt phẳng",
                        "problem": "Xác định miền nghiệm của $x + y - 2 \\le 0$.",
                        "solution": "- Vẽ bờ là đường thẳng $d: x + y - 2 = 0$ (nét liền).\n- Lấy điểm thử $O(0;0) \\notin d$, thay vào BPT: $0 + 0 - 2 \\le 0 \\iff -2 \\le 0$ (Đúng).\n- Miền nghiệm là nửa mặt phẳng bờ $d$ chứa gốc tọa độ $O$."
                    }
                ],
                "exercise": {
                    "id": "10_3_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Gốc tọa độ O(0;0) có thuộc miền nghiệm của 3x - 2y < 5 không? (1: Có, 0: Không)", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 4: Hệ bất phương trình bậc nhất hai ẩn": {
        "chapter": "Chương II: Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
        "topics": {
            "Chủ điểm 1: Miền nghiệm của hệ và Bài toán tối ưu": {
                "theory": "Miền nghiệm của hệ là phần giao của các miền nghiệm thành phần (thường là một đa giác). Biểu thức cần tối ưu $F(x, y) = ax + by$ luôn đạt giá trị lớn nhất (hoặc nhỏ nhất) tại một trong CÁC ĐỈNH của đa giác miền nghiệm.",
                "formula": r"\max F(x, y) = \max \{F(A), F(B), F(C), \dots \} \text{ (A, B, C là các đỉnh)}",
                "trap": "Học sinh thường đoán mò đỉnh tối ưu. Quy trình chuẩn là bắt buộc phải tính giá trị F tại TẤT CẢ CÁC ĐỈNH của đa giác rồi mới kết luận được.",
                "audio": "Miền nghiệm của hệ là phần không bị gạch. Muốn tìm giá trị lớn nhất hay nhỏ nhất của hàm F, em cứ tính giá trị F tại tất cả các đỉnh của đa giác là ra ngay.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét điểm thuộc hệ",
                        "problem": "Điểm $O(0;0)$ có phải là nghiệm của hệ $\\begin{cases} x + y \\le 2 \\\\ 2x - y > 1 \\end{cases}$ không?",
                        "solution": "- Thay $x=0, y=0$ vào BPT 1: $0 + 0 \\le 2$ (Đúng).\n- Thay $x=0, y=0$ vào BPT 2: $0 - 0 > 1$ (Sai).\n- Hệ yêu cầu phải thỏa mãn đồng thời, nên $O(0;0)$ không thuộc miền nghiệm của hệ."
                    },
                    {
                        "title": "Ví dụ 2: Bài toán tối ưu kinh tế",
                        "problem": "Một đa giác miền nghiệm có 3 đỉnh $A(0; 2), B(2; 1), C(3; 0)$. Tìm GTLN của biểu thức lợi nhuận $F(x, y) = 40x + 10y$.",
                        "solution": "- Tính tại A: $F(A) = 40(0) + 10(2) = 20$.\n- Tính tại B: $F(B) = 40(2) + 10(1) = 80 + 10 = 90$.\n- Tính tại C: $F(C) = 40(3) + 10(0) = 120$.\n- So sánh 3 giá trị: $120 > 90 > 20$. GTLN bằng 120 (đạt tại đỉnh C)."
                    }
                ],
                "exercise": {
                    "id": "10_4_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Miền nghiệm có các đỉnh O(0;0), A(0;3), B(4;0). Giá trị lớn nhất của F = 2x + y bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            }
        }
    },
    "Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ": {
        "chapter": "Chương III: Hệ thức lượng trong tam giác",
        "topics": {
            "Chủ điểm 1: Nửa đường tròn lượng giác và Góc bù nhau": {
                "theory": "Trên nửa đường tròn lượng giác (bán kính R=1, $y \\ge 0$), $\\sin\\alpha$ là tung độ, $\\cos\\alpha$ là hoành độ. Tính chất của hai góc bù nhau (tổng bằng $180^\\circ$): Sin bằng nhau, các giá trị khác đối nhau.",
                "formula": r"\sin(180^\circ - \alpha) = \sin\alpha; \quad \cos(180^\circ - \alpha) = -\cos\alpha",
                "trap": "Góc tù (từ $90^\\circ$ đến $180^\\circ$) luôn có $\\cos < 0$. Học sinh giải phương trình tìm góc tam giác hay quên kiểm tra điều kiện này khi khai căn.",
                "audio": "Sin bù, phụ chéo. Hai góc bù nhau có Sin bằng nhau, nhưng Cos của chúng sẽ ngược dấu nhau. Đây là điểm nhấn quan trọng nhất của bài.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính cos của góc tù",
                        "problem": "Cho $\\sin 150^\\circ = 0.5$. Tính $\\cos 150^\\circ$ mà không dùng máy tính.",
                        "solution": "- Ta có $150^\\circ$ và $30^\\circ$ là hai góc bù nhau.\n- $\\cos 150^\\circ = -\\cos 30^\\circ = -\\frac{\\sqrt{3}}{2}$."
                    },
                    {
                        "title": "Ví dụ 2: Tính biểu thức",
                        "problem": "Tính giá trị biểu thức $A = \\sin 120^\\circ + \\cos 60^\\circ$.",
                        "solution": "- Vì $\\sin 120^\\circ = \\sin(180^\\circ - 60^\\circ) = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$.\n- Và $\\cos 60^\\circ = \\frac{1}{2}$.\n- Vậy $A = \\frac{\\sqrt{3} + 1}{2}$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ thức cơ bản",
                        "problem": "Biết $\\sin\\alpha = \\frac{1}{3}$ và $90^\\circ < \\alpha < 180^\\circ$. Tính $\\cos\\alpha$.",
                        "solution": "- $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\frac{1}{9} = \\frac{8}{9}$.\n- Vì $\\alpha$ là góc tù nên $\\cos\\alpha < 0 \\implies \\cos\\alpha = -\\frac{\\sqrt{8}}{3} = -\\frac{2\\sqrt{2}}{3}$."
                    }
                ],
                "exercise": {
                    "id": "10_5_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị của biểu thức P = sin(30 độ) + cos(120 độ) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 6: Hệ thức lượng trong tam giác": {
        "chapter": "Chương III: Hệ thức lượng trong tam giác",
        "topics": {
            "Chủ điểm 1: Định lý Cosin và Định lý Sin": {
                "theory": "Định lý Côsin mở rộng từ Pytago: Bình phương một cạnh bằng tổng bình phương 2 cạnh kia trừ đi 2 lần tích của chúng với cosin góc xen giữa. Định lý Sin dùng để tính cạnh và góc khi biết 1 cặp cạnh-góc đối diện, đồng thời liên hệ với bán kính đường tròn ngoại tiếp R.",
                "formula": r"a^2 = b^2 + c^2 - 2bc \cos A; \quad \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R",
                "trap": "Học sinh thường quên nhân hệ số 2 trong cụm $-2bc\\cos A$ của định lý Côsin, dẫn đến tính sai cạnh hoàn toàn.",
                "audio": "Định lý Côsin áp dụng khi biết 2 cạnh và 1 góc xen giữa. Định lý Sin dùng khi biết một cạnh và góc đối diện của nó. Nhớ công thức R lớn bằng a chia 2 sin A nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng định lý Côsin",
                        "problem": "Tam giác ABC có $b=8, c=5$ và góc $A = 60^\\circ$. Tính cạnh $a$.",
                        "solution": "- Áp dụng: $a^2 = b^2 + c^2 - 2bc\\cos A$.\n- $a^2 = 8^2 + 5^2 - 2(8)(5)\\cos 60^\\circ = 64 + 25 - 80(0.5) = 89 - 40 = 49$.\n- $a = \\sqrt{49} = 7$."
                    },
                    {
                        "title": "Ví dụ 2: Áp dụng định lý Sin",
                        "problem": "Tam giác ABC có $a=10$ và góc $A = 30^\\circ$. Tính bán kính đường tròn ngoại tiếp R.",
                        "solution": "- Áp dụng: $\\frac{a}{\\sin A} = 2R$.\n- $2R = \\frac{10}{\\sin 30^\\circ} = \\frac{10}{0.5} = 20 \\implies R = 10$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ quả tìm góc",
                        "problem": "Tam giác ABC có $a=3, b=4, c=5$. Tính $\\cos C$.",
                        "solution": "- Đây là tam giác vuông tại C (Pytago đảo), nên góc $C=90^\\circ \\implies \\cos C = 0$.\n- Thử bằng hệ quả: $\\cos C = \\frac{a^2+b^2-c^2}{2ab} = \\frac{9+16-25}{24} = 0$."
                    }
                ],
                "exercise": {
                    "id": "10_6_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tam giác có a=3, b=4, góc C=90 độ. Cạnh c bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Các công thức tính diện tích tam giác": {
                "theory": "Diện tích tam giác có 5 công thức chính: (1) Cạnh đáy $\\times$ chiều cao / 2. (2) Theo góc xen giữa: $S = \\frac{1}{2}ab\\sin C$. (3) Công thức Heron (theo 3 cạnh). (4) Theo bán kính nội tiếp: $S = p \\cdot r$. (5) Theo bán kính ngoại tiếp: $S = \\frac{abc}{4R}$.",
                "formula": r"S = \frac{1}{2}ab \sin C; \quad S = \sqrt{p(p-a)(p-b)(p-c)}",
                "trap": "Ở công thức Heron, đại lượng $p$ là NỬA chu vi ($p = \\frac{a+b+c}{2}$), rất nhiều bạn nhầm lấy cả chu vi để tính.",
                "audio": "Khi biết hai cạnh và góc xen giữa, công thức 1/2 a b sin C là nhanh nhất. Biết ba cạnh thì dùng công thức Heron với nửa chu vi p.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính diện tích theo góc xen giữa",
                        "problem": "Tính diện tích tam giác ABC biết $a=4, b=5$ và góc $C = 30^\\circ$.",
                        "solution": "- $S = \\frac{1}{2}ab\\sin C = \\frac{1}{2}(4)(5)\\sin 30^\\circ$.\n- $S = 10 \\cdot 0.5 = 5$."
                    },
                    {
                        "title": "Ví dụ 2: Công thức Heron",
                        "problem": "Tam giác ABC có 3 cạnh là 3, 4, 5. Tính diện tích bằng công thức Heron.",
                        "solution": "- Nửa chu vi $p = \\frac{3+4+5}{2} = 6$.\n- $S = \\sqrt{6(6-3)(6-4)(6-5)} = \\sqrt{6 \\cdot 3 \\cdot 2 \\cdot 1} = \\sqrt{36} = 6$."
                    }
                ],
                "exercise": {
                    "id": "10_6_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tam giác đều cạnh bằng 2. Diện tích S bằng căn bậc hai của c. Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 7: Các khái niệm mở đầu về vectơ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Vectơ cùng phương, bằng nhau": {
                "theory": "Vectơ là một đoạn thẳng có hướng. Đặc trưng bởi độ dài và hướng. Hai vectơ cùng phương nếu giá của chúng song song hoặc trùng nhau. Hai vectơ BẰNG NHAU khi chúng CÙNG HƯỚNG và CÙNG ĐỘ DÀI. Vectơ-không ($\\vec{0}$) cùng phương, cùng hướng với mọi vectơ.",
                "formula": r"\vec{a} = \vec{b} \iff \begin{cases} \vec{a} \uparrow\uparrow \vec{b} \\ |\vec{a}| = |\vec{b}| \end{cases}",
                "trap": "Hai vectơ có cùng độ dài và giá song song với nhau CHƯA CHẮC bằng nhau, vì chúng có thể ngược hướng (gọi là hai vectơ đối nhau).",
                "audio": "Để hai vectơ bằng nhau, chúng phải hội đủ hai yếu tố: cùng chỉ về một hướng và có độ dài dài bằng y hệt nhau.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm vectơ bằng nhau",
                        "problem": "Cho hình bình hành ABCD. Vectơ nào bằng với vectơ $\\vec{AB}$?",
                        "solution": "- Trong hình bình hành ABCD, cạnh AB song song và bằng cạnh DC.\n- Hướng từ A đến B cùng hướng với từ D đến C.\n- **Kết luận:** $\\vec{AB} = \\vec{DC}$ (Chú ý: không phải $\\vec{CD}$)."
                    },
                    {
                        "title": "Ví dụ 2: Tính độ dài vectơ",
                        "problem": "Cho hình vuông ABCD cạnh $a$. Tính độ dài của vectơ $\\vec{AC}$.",
                        "solution": "- Độ dài của vectơ $\\vec{AC}$ chính là độ dài đoạn thẳng AC.\n- Theo Pytago, đường chéo hình vuông $AC = a\\sqrt{2}$.\n- Vậy $|\\vec{AC}| = a\\sqrt{2}$."
                    }
                ],
                "exercise": {
                    "id": "10_7_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho tam giác đều ABC cạnh 5. Độ dài của vectơ AB bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            }
        }
    },
    "Bài 8: Tổng và hiệu của hai vectơ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "Chủ điểm 1: Quy tắc 3 điểm và Quy tắc hình bình hành": {
                "theory": "Quy tắc 3 điểm (nối đuôi): $\\vec{AB} + \\vec{BC} = \\vec{AC}$. Quy tắc hình bình hành (chung gốc): Nếu ABCD là hình bình hành thì $\\vec{AB} + \\vec{AD} = \\vec{AC}$. Quy tắc trừ (chung gốc): $\\vec{AB} - \\vec{AC} = \\vec{CB}$ (lấy điểm sau làm gốc, đọc ngược lại).",
                "formula": r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{AB} - \vec{AC} = \vec{CB}",
                "trap": "Lỗi cực kỳ phổ biến ở phép trừ: Học sinh viết $\\vec{AB} - \\vec{AC} = \\vec{BC}$. Đúng ra phải là $\\vec{CB}$.",
                "audio": "Quy tắc ba điểm là nối đuôi nhau. Còn phép trừ hai vectơ chung gốc thì em nhớ lấy ngọn của vectơ bị trừ ghép với ngọn của vectơ kia theo chiều ngược lại nhé.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn tổng",
                        "problem": "Rút gọn biểu thức $\\vec{MN} + \\vec{PQ} + \\vec{NP}$.",
                        "solution": "- Giao hoán và nhóm: $(\\vec{MN} + \\vec{NP}) + \\vec{PQ}$.\n- Áp dụng quy tắc 3 điểm: $\\vec{MP} + \\vec{PQ} = \\vec{MQ}$."
                    },
                    {
                        "title": "Ví dụ 2: Rút gọn hiệu",
                        "problem": "Rút gọn $\\vec{AB} - \\vec{AD}$.",
                        "solution": "- Hai vectơ chung gốc A.\n- Áp dụng quy tắc trừ: $\\vec{AB} - \\vec{AD} = \\vec{DB}$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ thức trung điểm",
                        "problem": "Cho I là trung điểm của AB. Tính $\\vec{IA} + \\vec{IB}$.",
                        "solution": "- Vì I là trung điểm nên $\\vec{IA}$ và $\\vec{IB}$ là hai vectơ đối nhau (cùng độ dài, ngược hướng).\n- Tổng hai vectơ đối luôn bằng $\\vec{0}$."
                    }
                ],
                "exercise": {
                    "id": "10_8_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Rút gọn vectơ OM - ON ta được vectơ NM. Đúng (1) hay Sai (0)?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 9: Tích của một vectơ với một số": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Điều kiện cùng phương": {
                "theory": "Tích của số $k$ và vectơ $\\vec{a}$ là một VECTƠ. Cùng hướng nếu $k > 0$, ngược hướng nếu $k < 0$, độ dài tăng lên $|k|$ lần. Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương khi và chỉ khi tồn tại số $k$ sao cho $\\vec{a} = k\\vec{b}$. (Đây là cách duy nhất để chứng minh 3 điểm thẳng hàng bằng vectơ).",
                "formula": r"\vec{a} = k\vec{b} \iff \vec{a} \parallel \vec{b}; \quad \vec{AB} = k\vec{AC} \iff A, B, C \text{ thẳng hàng}",
                "trap": "Học sinh chứng minh 3 điểm $A, B, C$ thẳng hàng bằng cách chỉ ra $\\vec{AB}$ cùng phương $\\vec{CD}$ là sai bản chất, vì nó có thể là 2 đường song song. Phải là $\\vec{AB}$ và $\\vec{AC}$ (có chung điểm A).",
                "audio": "Nhân một số với một vectơ sẽ tạo ra một vectơ mới, dài ra hoặc ngắn đi. Nếu hệ số âm, vectơ sẽ bị quay ngược 180 độ.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài",
                        "problem": "Cho vectơ $\\vec{a}$ có độ dài bằng 4. Tính độ dài của vectơ $-3\\vec{a}$.",
                        "solution": "- $|-3\\vec{a}| = |-3| \\cdot |\\vec{a}| = 3 \\cdot 4 = 12$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chất trung điểm",
                        "problem": "I là trung điểm AB, M là điểm bất kỳ. Biểu diễn $\\vec{MA} + \\vec{MB}$ theo $\\vec{MI}$.",
                        "solution": "- Theo hệ thức trung điểm mở rộng: $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$."
                    },
                    {
                        "title": "Ví dụ 3: Trọng tâm tam giác",
                        "problem": "G là trọng tâm $\\Delta ABC$. M là điểm bất kỳ. Tổng $\\vec{MA} + \\vec{MB} + \\vec{MC}$ bằng mấy lần $\\vec{MG}$?",
                        "solution": "- Áp dụng hệ thức trọng tâm: $\\vec{MA} + \\vec{MB} + \\vec{MC} = 3\\vec{MG}$."
                    }
                ],
                "exercise": {
                    "id": "10_9_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho I là trung điểm AB. M là điểm bất kì. Vectơ MA + MB = c.MI. Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 KẾT NỐI TRI THỨC (PHẦN 2: BÀI 10 -> BÀI 18)
# ==============================================================================

GRADE_10_DATA.update({
    "Bài 10: Vectơ trong mặt phẳng tọa độ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "Chủ điểm 1: Tọa độ của vectơ và Tọa độ của điểm": {
                "theory": "Trên hệ trục tọa độ Oxy, vectơ $\\vec{u} = x\\vec{i} + y\\vec{j}$ có tọa độ là $(x; y)$. Tọa độ của vectơ nối hai điểm $\\vec{AB}$ bằng tọa độ điểm cuối $B$ trừ đi tọa độ điểm đầu $A$. Tọa độ trung điểm của đoạn thẳng bằng trung bình cộng tọa độ 2 đầu mút.",
                "formula": r"\vec{AB} = (x_B - x_A; y_B - y_A); \quad x_I = \frac{x_A + x_B}{2}, y_I = \frac{y_A + y_B}{2}",
                "trap": "Học sinh thường hay lấy tọa độ điểm A trừ điểm B để tính $\\vec{AB}$. Phải nhớ luôn lấy 'ngọn trừ gốc' (sau trừ trước).",
                "audio": "Để tính tọa độ của một vectơ, em nhớ lấy tọa độ điểm cuối trừ đi điểm đầu nhé. Còn trung điểm thì cứ cộng lại chia đôi là xong.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tọa độ vectơ từ hai điểm",
                        "problem": "Cho $A(1; 3)$ và $B(4; -2)$. Tìm tọa độ của vectơ $\\vec{AB}$.",
                        "solution": "- Hoành độ: $x_{AB} = 4 - 1 = 3$.\n- Tung độ: $y_{AB} = -2 - 3 = -5$.\n- **Kết luận:** $\\vec{AB} = (3; -5)$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm tọa độ điểm khi biết trung điểm",
                        "problem": "Cho $A(2; -1)$ và trung điểm $I(3; 4)$ của đoạn $AB$. Tìm tọa độ điểm $B$.",
                        "solution": "- Áp dụng: $x_B = 2x_I - x_A = 2(3) - 2 = 4$.\n- $y_B = 2y_I - y_A = 2(4) - (-1) = 9$.\n- **Kết luận:** $B(4; 9)$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định tọa độ trọng tâm tam giác",
                        "problem": "Cho $\\Delta ABC$ với $A(1; 1), B(2; 3), C(-3; 5)$. Tìm tọa độ trọng tâm $G$.",
                        "solution": "- Trọng tâm là trung bình cộng 3 đỉnh.\n- $x_G = \\frac{1 + 2 + (-3)}{3} = 0$.\n- $y_G = \\frac{1 + 3 + 5}{3} = 3$.\n- **Kết luận:** $G(0; 3)$."
                    }
                ],
                "exercise": {
                    "id": "10_10_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho A(1; 5) và B(3; 1). Trung điểm I của AB có tung độ y bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            },
            "Chủ điểm 2: Biểu thức tọa độ của các phép toán vectơ": {
                "theory": "Cộng, trừ hai vectơ là cộng, trừ các tọa độ tương ứng. Nhân một số với một vectơ là nhân số đó với từng tọa độ. Hai vectơ cùng phương khi và chỉ khi hoành độ và tung độ của chúng tỉ lệ với nhau.",
                "formula": r"\vec{u} + \vec{v} = (x_1+x_2; y_1+y_2); \quad \vec{u} \parallel \vec{v} \iff \frac{x_1}{x_2} = \frac{y_1}{y_2} \ (x_2, y_2 \neq 0)",
                "trap": "Khi lập tỉ số để kiểm tra sự cùng phương, nếu mẫu số bằng 0 thì không được dùng phân số, phải dùng định nghĩa $\\vec{u} = k\\vec{v}$.",
                "audio": "Cộng trừ vectơ ta cứ cộng trừ tương ứng hoành với hoành, tung với tung. Để kiểm tra cùng phương, lập tỉ số hoành chia hoành xem có bằng tung chia tung không.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phép toán vectơ cơ bản",
                        "problem": "Cho $\\vec{a} = (2; -3)$ và $\\vec{b} = (-1; 4)$. Tìm tọa độ $\\vec{c} = 2\\vec{a} + \\vec{b}$.",
                        "solution": "- $2\\vec{a} = (4; -6)$.\n- $\\vec{c} = (4 + (-1); -6 + 4) = (3; -2)$."
                    },
                    {
                        "title": "Ví dụ 2: Hai vectơ cùng phương",
                        "problem": "Tìm $m$ để $\\vec{u} = (2; m)$ cùng phương với $\\vec{v} = (4; -6)$.",
                        "solution": "- Lập tỉ lệ: $\\frac{2}{4} = \\frac{m}{-6}$.\n- Giải phương trình: $4m = -12 \\implies m = -3$."
                    },
                    {
                        "title": "Ví dụ 3: Chứng minh 3 điểm thẳng hàng",
                        "problem": "Cho $A(1; 1), B(2; 3), C(4; 7)$. Hỏi 3 điểm có thẳng hàng không? (1: Có, 0: Không)",
                        "solution": "- $\\vec{AB} = (1; 2)$. $\\vec{AC} = (3; 6)$.\n- Ta thấy $\\vec{AC} = 3\\vec{AB}$ nên 3 điểm thẳng hàng. (Đáp án: 1)."
                    }
                ],
                "exercise": {
                    "id": "10_10_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho a = (1; -2). Tọa độ của vectơ 3a có hoành độ bằng:", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 11: Tích vô hướng của hai vectơ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "Chủ điểm 1: Biểu thức tọa độ của tích vô hướng": {
                "theory": "Tích vô hướng của hai vectơ là MỘT SỐ, bằng hoành nhân hoành cộng tung nhân tung. Từ đây tính được độ dài vectơ và khoảng cách giữa 2 điểm. Hai vectơ vuông góc khi tích vô hướng của chúng bằng 0.",
                "formula": r"\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2; \quad |\vec{u}| = \sqrt{x^2 + y^2}",
                "trap": "Học sinh thường ghi nhầm kết quả của tích vô hướng là một vectơ (có tọa độ). Lặp lại: Tích vô hướng là một HẰNG SỐ.",
                "audio": "Tích vô hướng bằng hoành nhân hoành cộng tung nhân tung. Và hãy nhớ kỹ, hai vectơ vuông góc khi tích vô hướng của chúng bằng 0.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tích vô hướng",
                        "problem": "Cho $\\vec{u} = (2; -3)$ và $\\vec{v} = (4; 1)$. Tính $\\vec{u} \\cdot \\vec{v}$.",
                        "solution": "- $\\vec{u} \\cdot \\vec{v} = 2(4) + (-3)1 = 8 - 3 = 5$."
                    },
                    {
                        "title": "Ví dụ 2: Tính khoảng cách (độ dài đoạn thẳng)",
                        "problem": "Tính độ dài đoạn thẳng $AB$ với $A(1; 2)$ và $B(4; -2)$.",
                        "solution": "- $\\vec{AB} = (3; -4)$.\n- $AB = |\\vec{AB}| = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5$."
                    },
                    {
                        "title": "Ví dụ 3: Tìm tham số để 2 vectơ vuông góc",
                        "problem": "Tìm $k$ để $\\vec{a} = (k; 2)$ vuông góc với $\\vec{b} = (4; -6)$.",
                        "solution": "- Để vuông góc thì $\\vec{a} \\cdot \\vec{b} = 0$.\n- $k(4) + 2(-6) = 0 \\implies 4k - 12 = 0 \\implies k = 3$."
                    }
                ],
                "exercise": {
                    "id": "10_11_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho u = (3; 4) và v = (-4; 3). Tích vô hướng u.v bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tính góc giữa hai vectơ": {
                "theory": "Cosin góc giữa hai vectơ bằng tích vô hướng chia cho tích độ dài của chúng. Góc giữa hai vectơ có thể từ $0^\\circ$ đến $180^\\circ$.",
                "formula": r"\cos(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}| \cdot |\vec{v}|} = \frac{x_1 x_2 + y_1 y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}",
                "trap": "Không được lấy trị tuyệt đối trên tử số. Nếu tích vô hướng âm thì cosin âm, góc giữa hai vectơ là góc tù.",
                "audio": "Cosin góc giữa hai vectơ bằng tích vô hướng chia cho tích độ dài. Đừng tự ý thêm trị tuyệt đối như khi tính góc đường thẳng nhé.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa 2 vectơ",
                        "problem": "Tìm góc giữa $\\vec{a} = (1; 1)$ và $\\vec{b} = (0; 2)$.",
                        "solution": "- Tích vô hướng: $\\vec{a} \\cdot \\vec{b} = 1(0) + 1(2) = 2$.\n- Tích độ dài: $|\\vec{a}| = \\sqrt{1^2+1^2} = \\sqrt{2}$; $|\\vec{b}| = \\sqrt{0^2+2^2} = 2$.\n- $\\cos\\varphi = \\frac{2}{2\\sqrt{2}} = \\frac{1}{\\sqrt{2}} \\implies \\varphi = 45^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Tính góc của tam giác",
                        "problem": "Cho tam giác OAB vuông cân tại O. Tính góc giữa $\\vec{OA}$ và $\\vec{AB}$.",
                        "solution": "- Vẽ hình ta thấy, khi tịnh tiến chung gốc, góc giữa $\\vec{OA}$ và $\\vec{AB}$ là góc tù bằng $135^\\circ$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định tính chất góc",
                        "problem": "Nếu $\\vec{u} \\cdot \\vec{v} < 0$ thì góc giữa hai vectơ là góc nhọn hay góc tù?",
                        "solution": "- Tử số âm, mẫu số luôn dương nên $\\cos < 0$. Góc giữa hai vectơ là góc tù."
                    }
                ],
                "exercise": {
                    "id": "10_11_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho a = (1; 0) và b = (1; 1). Góc giữa hai vectơ này bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "45", 
                    "options": []
                }
            }
        }
    },
    "Bài 12: Số gần đúng và sai số": {
        "chapter": "Chương V: Các số đặc trưng đo xu thế trung tâm và đo độ phân tán",
        "topics": {
            "Chủ điểm 1: Sai số tuyệt đối và Sai số tương đối": {
                "theory": "Sai số tuyệt đối $\\Delta_a$ là trị tuyệt đối của hiệu giữa số đúng và số gần đúng. Độ chính xác $d$ là giới hạn trên của sai số tuyệt đối. Sai số tương đối $\\delta_a$ đánh giá chất lượng của phép đo (càng nhỏ phép đo càng chính xác).",
                "formula": r"\Delta_a = |a - \overline{a}| \le d; \quad \delta_a = \frac{\Delta_a}{|a|} \le \frac{d}{|a|}",
                "trap": "Học sinh thường quên nhân $100\\%$ khi viết kết quả sai số tương đối, làm cho người đọc khó hình dung độ chính xác.",
                "audio": "Sai số tuyệt đối cho biết mức độ chênh lệch. Nhưng để biết phép đo đó tốt hay dở, em phải dùng sai số tương đối tính theo phần trăm nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính sai số tuyệt đối",
                        "problem": "Giá trị đúng là $a = 3.14159$, giá trị gần đúng là $3.14$. Tính sai số tuyệt đối.",
                        "solution": "- $\\Delta_a = |3.14159 - 3.14| = 0.00159$."
                    },
                    {
                        "title": "Ví dụ 2: Đọc độ chính xác d",
                        "problem": "Đo chiều dài bàn $L = 120 \\pm 0.5$ (cm). Độ chính xác của phép đo là bao nhiêu?",
                        "solution": "- Số đứng sau dấu $\\pm$ chính là độ chính xác $d$.\n- **Kết luận:** $d = 0.5$ cm."
                    },
                    {
                        "title": "Ví dụ 3: So sánh chất lượng phép đo",
                        "problem": "Đo 10m sai số 1cm và đo 1000m sai số 10cm. Phép đo nào chính xác hơn?",
                        "solution": "- Tính sai số tương đối: $\\delta_1 = 1/1000 = 0.1\\%$. $\\delta_2 = 10/100000 = 0.01\\%$.\n- $\\delta_2 < \\delta_1$ nên phép đo thứ hai chính xác hơn."
                    }
                ],
                "exercise": {
                    "id": "10_12_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Chiều dài a = 200 +/- 2 (m). Độ chính xác d bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Quy tròn số gần đúng": {
                "theory": "Quy tắc làm tròn: Xét chữ số ngay sau hàng quy tròn. Nếu nó $\\ge 5$ thì cộng thêm 1 vào hàng quy tròn. Nếu nó $< 5$ thì giữ nguyên hàng quy tròn. Các chữ số ở hàng thấp hơn đổi thành 0 (hoặc bỏ đi nếu ở phần thập phân).",
                "formula": r"\text{Năm lên, Bốn xuống } (\ge 5 \to +1)",
                "trap": "Khi quy tròn dựa vào độ chính xác $d$, phải xác định hàng lớn nhất của $d$, rồi quy tròn số $a$ ở HÀNG GẤP 10 LẦN hàng đó.",
                "audio": "Từ số 5 trở lên thì làm tròn lên, dưới 5 thì giữ nguyên. Nếu đề cho độ chính xác d, nhớ làm tròn ở hàng lớn hơn d một bậc nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Quy tròn số thập phân",
                        "problem": "Làm tròn số $3.14159$ đến hàng phần trăm.",
                        "solution": "- Hàng phần trăm là số 4. Chữ số ngay sau nó là 1 $< 5$.\n- Giữ nguyên số 4.\n- **Kết luận:** $3.14$."
                    },
                    {
                        "title": "Ví dụ 2: Làm tròn số nguyên",
                        "problem": "Quy tròn số $123456$ đến hàng nghìn.",
                        "solution": "- Hàng nghìn là số 3. Chữ số sau nó là 4 $< 5$.\n- Giữ nguyên số 3, các số sau thành 0.\n- **Kết luận:** $123000$."
                    },
                    {
                        "title": "Ví dụ 3: Quy tròn theo độ chính xác d",
                        "problem": "Cho số $a = 153.456 \\pm 0.02$. Hãy quy tròn số $153.456$.",
                        "solution": "- Độ chính xác $d = 0.02$ có hàng lớn nhất là phần trăm.\n- Ta phải quy tròn $a$ ở hàng lớn hơn 1 bậc, tức là hàng phần mười (số 4).\n- Số sau số 4 là 5 $\\implies$ Cộng 1.\n- **Kết luận:** $153.5$."
                    }
                ],
                "exercise": {
                    "id": "10_12_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Làm tròn số 12.345 đến hàng phần mười ta được số bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "12.3", 
                    "options": []
                }
            }
        }
    },
    "Bài 13: Các số đặc trưng đo xu thế trung tâm": {
        "chapter": "Chương V: Các số đặc trưng đo xu thế trung tâm và đo độ phân tán",
        "topics": {
            "Chủ điểm 1: Số trung bình, Trung vị và Mốt": {
                "theory": "Số trung bình cộng $\\bar{x}$ dùng khi dữ liệu đồng đều. Nếu có giá trị bất thường, ta dùng Trung vị ($M_e$ - số đứng ở chính giữa sau khi đã sắp xếp). Mốt ($M_o$) là giá trị xuất hiện nhiều lần nhất.",
                "formula": r"\bar{x} = \frac{x_1+x_2+...+x_n}{n}; \quad M_e = \text{Giá trị chính giữa}",
                "trap": "Khi tìm Trung vị, học sinh hay vội lấy số chính giữa luôn mà quên SẮP XẾP dãy số theo thứ tự tăng dần.",
                "audio": "Số trung bình rất dễ bị bóp méo bởi các số quá lớn hoặc quá nhỏ. Khi đó, trung vị sẽ là lựa chọn đại diện tốt nhất cho tập dữ liệu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính số trung bình",
                        "problem": "Điểm thi của 5 học sinh: 6, 7, 8, 9, 10. Tính điểm trung bình.",
                        "solution": "- $\\bar{x} = \\frac{6+7+8+9+10}{5} = \\frac{40}{5} = 8$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm Trung vị",
                        "problem": "Tìm trung vị của mẫu số liệu: 3, 1, 9, 4, 7.",
                        "solution": "- Bước 1: Sắp xếp tăng dần: 1, 3, 4, 7, 9.\n- Bước 2: Vì có 5 số (lẻ), số chính giữa là số thứ 3.\n- **Kết luận:** $M_e = 4$."
                    },
                    {
                        "title": "Ví dụ 3: Tìm Mốt",
                        "problem": "Cho mẫu: 2, 2, 3, 4, 4, 4, 5. Tìm mốt.",
                        "solution": "- Số 4 xuất hiện nhiều nhất (3 lần).\n- **Kết luận:** $M_o = 4$."
                    }
                ],
                "exercise": {
                    "id": "10_13_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Dãy số: 5, 2, 8, 3, 9. Sắp xếp lại và tìm trung vị. M_e bằng:", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tứ phân vị": {
                "theory": "Ba tứ phân vị $Q_1, Q_2, Q_3$ chia mẫu số liệu đã sắp xếp thành 4 phần bằng nhau. $Q_2$ chính là Trung vị. $Q_1$ là trung vị của nửa số liệu bên trái, $Q_3$ là trung vị của nửa số liệu bên phải.",
                "formula": r"Q_2 = M_e; \quad Q_1 = M_e(\text{nửa trái}); \quad Q_3 = M_e(\text{nửa phải})",
                "trap": "Khi mẫu có số lượng N là lẻ, phần tử chính giữa $Q_2$ sẽ bị BỎ RA khi chia hai nửa để tính $Q_1$ và $Q_3$. Rất nhiều bạn gom nó vào tính tiếp.",
                "audio": "Ba tứ phân vị giống như ba nhát cắt, chia cái bánh dữ liệu thành bốn phần bằng nhau. Cắt ở giữa trước để tìm Q2, rồi chia đôi hai nửa để tìm Q1 và Q3.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm các tứ phân vị (N lẻ)",
                        "problem": "Tìm $Q_1, Q_2, Q_3$ của mẫu: 1, 3, 5, 7, 9, 11, 13.",
                        "solution": "- Mẫu đã sắp xếp, $n=7$.\n- $Q_2$ là số chính giữa (thứ 4): $Q_2 = 7$.\n- Bỏ số 7, nửa trái là {1, 3, 5} $\\implies Q_1 = 3$.\n- Nửa phải là {9, 11, 13} $\\implies Q_3 = 11$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm các tứ phân vị (N chẵn)",
                        "problem": "Tìm $Q_1, Q_2$ của mẫu: 2, 4, 6, 8, 10, 12.",
                        "solution": "- Có $n=6$. $Q_2$ là trung bình cộng số thứ 3 và 4: $Q_2 = (6+8)/2 = 7$.\n- Nửa trái {2, 4, 6} $\\implies Q_1 = 4$."
                    },
                    {
                        "title": "Ví dụ 3: Ý nghĩa tứ phân vị",
                        "problem": "Có bao nhiêu phần trăm số liệu nhỏ hơn hoặc bằng Tứ phân vị thứ ba $Q_3$?",
                        "solution": "- $Q_3$ là mốc chia 3/4 dữ liệu.\n- Vậy có $75\\%$ số liệu nhỏ hơn hoặc bằng $Q_3$."
                    }
                ],
                "exercise": {
                    "id": "10_13_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Mẫu số liệu: 1, 2, 3, 4, 5. Giá trị của tứ phân vị thứ hai Q2 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 14: Các số đặc trưng đo độ phân tán": {
        "chapter": "Chương V: Các số đặc trưng đo xu thế trung tâm và đo độ phân tán",
        "topics": {
            "Chủ điểm 1: Khoảng biến thiên và Khoảng tứ phân vị": {
                "theory": "Khoảng biến thiên $R$ bằng giá trị lớn nhất trừ giá trị nhỏ nhất. Khoảng tứ phân vị $\\Delta_Q$ bằng $Q_3 - Q_1$. $\\Delta_Q$ đánh giá độ phân tán của $50\\%$ số liệu ở giữa, không bị ảnh hưởng bởi giá trị bất thường.",
                "formula": r"R = x_{\max} - x_{\min}; \quad \Delta_Q = Q_3 - Q_1",
                "trap": "Khi phát hiện các giá trị ngoại lệ (outlier), không nên dùng Khoảng biến thiên R vì nó sẽ làm sai lệch bức tranh tổng thể.",
                "audio": "Khoảng biến thiên đo độ rộng của toàn tập dữ liệu. Còn khoảng tứ phân vị chỉ đo độ rộng của phân nửa cốt lõi ở giữa nên nó chính xác hơn khi có số liệu bất thường.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng biến thiên",
                        "problem": "Cho mẫu số liệu: 2, 5, 8, 10, 20. Tính R.",
                        "solution": "- $x_{\\max} = 20, x_{\\min} = 2$.\n- $R = 20 - 2 = 18$."
                    },
                    {
                        "title": "Ví dụ 2: Tính khoảng tứ phân vị",
                        "problem": "Biết $Q_1 = 4$ và $Q_3 = 9$. Tính $\\Delta_Q$.",
                        "solution": "- $\\Delta_Q = Q_3 - Q_1 = 9 - 4 = 5$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định giá trị ngoại lệ",
                        "problem": "Một số liệu x được gọi là ngoại lệ dưới nếu $x < Q_1 - 1.5\\Delta_Q$. Cho $Q_1 = 4, \\Delta_Q = 2$. Giá trị x=0 có phải ngoại lệ không?",
                        "solution": "- Biên dưới: $4 - 1.5(2) = 4 - 3 = 1$.\n- Vì $0 < 1$, nên $x=0$ là giá trị ngoại lệ."
                    }
                ],
                "exercise": {
                    "id": "10_14_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Mẫu: 10, 12, 15, 30. Khoảng biến thiên R bằng:", 
                    "type": "NUMERIC", 
                    "target": "20", 
                    "options": []
                }
            },
            "Chủ điểm 2: Phương sai và Độ lệch chuẩn": {
                "theory": "Phương sai ($s^2$) đo độ phân tán quanh giá trị trung bình. Độ lệch chuẩn ($s$) là căn bậc hai của phương sai. Phương sai càng nhỏ thì các số liệu càng tập trung sát với giá trị trung bình.",
                "formula": r"s^2 = \frac{1}{n} \sum (x_i - \overline{x})^2; \quad s = \sqrt{s^2}",
                "trap": "Tính phương sai rất dài và dễ bấm máy sai. Nên dùng chức năng thống kê (phím STAT) trên máy tính cầm tay Casio để tính trực tiếp cho chính xác.",
                "audio": "Độ lệch chuẩn càng nhỏ thì lớp học có học lực càng đều. Nếu độ lệch chuẩn lớn, nghĩa là có bạn điểm rất cao nhưng cũng có bạn điểm rất thấp.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính phương sai",
                        "problem": "Mẫu số liệu: 4, 6. Tính phương sai.",
                        "solution": "- $\\bar{x} = (4+6)/2 = 5$.\n- $s^2 = \\frac{1}{2} [(4-5)^2 + (6-5)^2] = \\frac{1}{2} (1 + 1) = 1$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm độ lệch chuẩn",
                        "problem": "Nếu phương sai của mẫu là 9, tính độ lệch chuẩn.",
                        "solution": "- Độ lệch chuẩn $s = \\sqrt{s^2} = \\sqrt{9} = 3$."
                    },
                    {
                        "title": "Ví dụ 3: So sánh độ phân tán",
                        "problem": "Lớp A có độ lệch chuẩn điểm số là 1.2. Lớp B là 0.8. Lớp nào học đều hơn?",
                        "solution": "- Độ lệch chuẩn lớp B nhỏ hơn, nên điểm số lớp B ít phân tán hơn, tức là học đều hơn."
                    }
                ],
                "exercise": {
                    "id": "10_14_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Một mẫu có phương sai s^2 = 16. Độ lệch chuẩn s bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "4", 
                    "options": []
                }
            }
        }
    },
    "Bài 15: Hàm số và đồ thị": {
        "chapter": "Chương VI: Hàm số, Đồ thị và Ứng dụng",
        "topics": {
            "Chủ điểm 1: Tập xác định của hàm số": {
                "theory": "Tập xác định là tập hợp các giá trị của x để hàm số có nghĩa. Các điều kiện cơ bản: Mẫu số phải khác 0; Biểu thức trong căn bậc hai (căn chẵn) phải lớn hơn hoặc bằng 0.",
                "formula": r"\frac{A}{B} \implies B \neq 0; \quad \sqrt{A} \implies A \ge 0",
                "trap": "Hàm số chứa căn dưới mẫu (ví dụ $\\frac{1}{\\sqrt{A}}$) thì điều kiện là $A > 0$, không được có dấu bằng.",
                "audio": "Nhớ kỹ hai rào cản: Mẫu số tuyệt đối không được bằng không, và biểu thức trong căn chẵn không được mang dấu âm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Hàm số chứa mẫu",
                        "problem": "Tìm tập xác định của $y = \\frac{2x + 1}{x - 3}$.",
                        "solution": "- Điều kiện: $x - 3 \\neq 0 \\iff x \\neq 3$.\n- Tập xác định: $D = \\mathbb{R} \\setminus \\{3\\}$."
                    },
                    {
                        "title": "Ví dụ 2: Hàm số chứa căn",
                        "problem": "Tìm tập xác định của $y = \\sqrt{x - 2}$.",
                        "solution": "- Điều kiện: $x - 2 \\ge 0 \\iff x \\ge 2$.\n- Tập xác định: $D = [2; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 3: Căn nằm dưới mẫu",
                        "problem": "Tìm tập xác định của $y = \\frac{1}{\\sqrt{x + 1}}$.",
                        "solution": "- Điều kiện gộp: $x + 1 > 0 \\iff x > -1$.\n- Tập xác định: $D = (-1; +\\infty)$."
                    }
                ],
                "exercise": {
                    "id": "10_15_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tập xác định của y = căn(x - 5) là [c; +vô cực). Giá trị c bằng:", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Sự đồng biến, nghịch biến và Đồ thị": {
                "theory": "Hàm số đồng biến (tăng) trên K nếu $x_1 < x_2 \\implies f(x_1) < f(x_2)$. Nghịch biến (giảm) nếu $x_1 < x_2 \\implies f(x_1) > f(x_2)$. Trên đồ thị, từ trái sang phải: đồ thị đi lên là đồng biến, đi xuống là nghịch biến.",
                "formula": r"\frac{f(x_2) - f(x_1)}{x_2 - x_1} > 0 \implies \text{Đồng biến}",
                "trap": "Học sinh thường nhìn đồ thị từ phải sang trái rồi kết luận ngược. Quy tắc đọc đồ thị luôn phải nhìn theo chiều mũi tên trục Ox (Từ Trái sang Phải).",
                "audio": "Luôn trượt mắt trên đồ thị từ trái sang phải. Nếu thấy nét vẽ đi lên dốc, hàm số đồng biến. Nếu tuột dốc, hàm số nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh bằng định nghĩa",
                        "problem": "Chứng minh $y = 2x + 1$ đồng biến trên $\\mathbb{R}$.",
                        "solution": "- Lấy $x_1 < x_2 \\implies x_1 - x_2 < 0$.\n- Xét $f(x_1) - f(x_2) = (2x_1+1) - (2x_2+1) = 2(x_1 - x_2) < 0$.\n- Vì $f(x_1) < f(x_2)$, hàm số đồng biến."
                    },
                    {
                        "title": "Ví dụ 2: Đọc đồ thị Parabol",
                        "problem": "Đồ thị Parabol có đỉnh tại $x=1$, bề lõm hướng lên. Hàm số đồng biến trên khoảng nào?",
                        "solution": "- Bề lõm hướng lên $\\implies$ đồ thị đi xuống đến $x=1$ rồi đi lên.\n- Từ trái sang phải, sau điểm x=1 đồ thị đi lên.\n- Hàm số đồng biến trên $(1; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định điểm thuộc đồ thị",
                        "problem": "Điểm $M(1; 3)$ có thuộc đồ thị hàm $y = x^2 + 2$ không? (1: Có, 0: Không)",
                        "solution": "- Thay $x=1$ vào hàm: $y = 1^2 + 2 = 3$.\n- Bằng tung độ điểm M. (Đáp án: 1)."
                    }
                ],
                "exercise": {
                    "id": "10_15_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Điểm M(2; 4) thuộc đồ thị y = c*x^2. Giá trị của c bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 16: Hàm số bậc hai": {
        "chapter": "Chương VI: Hàm số, Đồ thị và Ứng dụng",
        "topics": {
            "Chủ điểm 1: Đồ thị hàm số bậc hai (Parabol)": {
                "theory": "Đồ thị hàm số $y = ax^2 + bx + c$ ($a \\neq 0$) là một Parabol. Đỉnh $I(-b/2a; -\Delta/4a)$. Trục đối xứng là đường thẳng $x = -b/2a$. Bề lõm hướng lên nếu $a > 0$, hướng xuống nếu $a < 0$.",
                "formula": r"x_I = -\frac{b}{2a}; \quad y_I = f(x_I)",
                "trap": "Học sinh thường nhớ sai dấu của hoành độ đỉnh thành $b/2a$ (thiếu dấu trừ). Không cần nhớ công thức $y_I$, chỉ cần lấy $x_I$ thay vào hàm số là ra $y_I$.",
                "audio": "Nhớ kỹ tọa độ đỉnh Parabol là trừ b trên 2a. Nếu hệ số a dương, đồ thị ngửa lên như một cái phễu hứng nước mưa.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tọa độ đỉnh",
                        "problem": "Tìm tọa độ đỉnh của Parabol $y = x^2 - 4x + 3$.",
                        "solution": "- Hoành độ: $x_I = -\\frac{-4}{2(1)} = 2$.\n- Tung độ: Thay $x=2$ vào $\\implies y_I = 2^2 - 4(2) + 3 = -1$.\n- **Kết luận:** Đỉnh $I(2; -1)$."
                    },
                    {
                        "title": "Ví dụ 2: Xác định trục đối xứng",
                        "problem": "Trục đối xứng của Parabol $y = -2x^2 + 8x$ là đường thẳng nào?",
                        "solution": "- Áp dụng: $x = -\\frac{8}{2(-2)} = -\\frac{8}{-4} = 2$.\n- Trục đối xứng là đường thẳng $x = 2$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định dấu của hệ số a",
                        "problem": "Parabol có đỉnh cao nhất là $I(1; 5)$ và 2 nhánh hướng xuống dưới. Hỏi hệ số $a$ âm hay dương?",
                        "solution": "- Bề lõm hướng xuống dưới (như cái ô) $\\implies a < 0$ (Âm)."
                    }
                ],
                "exercise": {
                    "id": "10_16_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hoành độ đỉnh Parabol y = x^2 - 6x + 5 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            },
            "Chủ điểm 2: Sự biến thiên và GTLN, GTNN": {
                "theory": "Nếu $a > 0$: Hàm số đạt GTNN tại đỉnh $x = -b/2a$, nghịch biến bên trái đỉnh và đồng biến bên phải đỉnh. Nếu $a < 0$: Hàm số đạt GTLN tại đỉnh, đồng biến bên trái đỉnh và nghịch biến bên phải đỉnh.",
                "formula": r"\min f(x) = f\left(-\frac{b}{2a}\right) \ (\text{khi } a>0)",
                "trap": "Khi lập bảng biến thiên, phải quan sát thật kỹ dấu của hệ số a để vẽ mũi tên đi lên hay đi xuống ở phần đầu tiên. Sai một mũi tên là sai toàn bộ bài.",
                "audio": "Trục đối xứng chia Parabol thành 2 nửa: một nửa đi lên, một nửa đi xuống. Tùy vào dấu của a để biết đỉnh là đáy thung lũng hay đỉnh ngọn núi nhé.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập bảng biến thiên (a > 0)",
                        "problem": "Cho hàm số $y = x^2 - 2x$. Hàm số nghịch biến trên khoảng nào?",
                        "solution": "- Đỉnh $x_I = -\\frac{-2}{2} = 1$.\n- Hệ số $a = 1 > 0$, bề lõm hướng lên.\n- Đồ thị đi xuống trên $(-\\infty; 1)$ và đi lên trên $(1; +\\infty)$.\n- **Kết luận:** Hàm số nghịch biến trên $(-\\infty; 1)$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm GTLN (a < 0)",
                        "problem": "Tìm giá trị lớn nhất của $y = -x^2 + 4x + 1$.",
                        "solution": "- Đỉnh $x_I = -\\frac{4}{-2} = 2$.\n- Vì $a = -1 < 0$, đồ thị có bề lõm hướng xuống, đạt GTLN tại đỉnh.\n- GTLN = $y(2) = -(2^2) + 4(2) + 1 = -4 + 8 + 1 = 5$."
                    },
                    {
                        "title": "Ví dụ 3: Ứng dụng thực tế",
                        "problem": "Độ cao của quả bóng sau $t$ giây là $h(t) = -5t^2 + 10t$ (m). Quả bóng đạt độ cao lớn nhất tại giây thứ mấy?",
                        "solution": "- Hàm bậc hai với $a = -5 < 0$. GTLN đạt tại đỉnh.\n- Thời gian: $t = -\\frac{10}{2(-5)} = 1$.\n- **Kết luận:** Quả bóng lên cao nhất tại giây thứ 1."
                    }
                ],
                "exercise": {
                    "id": "10_16_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị nhỏ nhất của hàm số y = x^2 - 4x + 5 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 17: Dấu của tam thức bậc hai": {
        "chapter": "Chương VI: Hàm số, Đồ thị và Ứng dụng",
        "topics": {
            "Chủ điểm 1: Định lý về dấu của tam thức bậc hai": {
                "theory": "Xét $f(x) = ax^2 + bx + c$ ($a \\neq 0$). Nếu $\\Delta < 0$, $f(x)$ cùng dấu với $a$ trên $\\mathbb{R}$. Nếu $\\Delta = 0$, $f(x)$ cùng dấu với $a$ với mọi $x \\neq -b/2a$. Nếu $\\Delta > 0$, $f(x)$ có 2 nghiệm $x_1, x_2$, dấu của $f(x)$ tuân theo quy tắc TRONG TRÁI - NGOÀI CÙNG.",
                "formula": r"\Delta < 0 \implies a \cdot f(x) > 0; \quad \Delta > 0 \implies \text{Trong trái, Ngoài cùng}",
                "trap": "Rất nhiều học sinh áp dụng máy móc câu 'Trong trái ngoài cùng' cho cả trường hợp tam thức vô nghiệm ($\\Delta < 0$). Nhớ là chỉ có 2 nghiệm phân biệt mới có khái niệm Cửa 'Trong' và 'Ngoài'.",
                "audio": "Khi Delta âm, tam thức luôn luôn cùng dấu với hệ số a. Chỉ khi có hai nghiệm phân biệt, chúng ta mới được dùng thần chú Trong trái ngoài cùng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét dấu khi Delta > 0",
                        "problem": "Xét dấu tam thức $f(x) = x^2 - 5x + 6$.",
                        "solution": "- Nghiệm của $x^2 - 5x + 6 = 0$ là $x = 2$ và $x = 3$.\n- Hệ số $a = 1 > 0$. Theo quy tắc 'Trong trái ngoài cùng':\n- Bên trong $(2; 3)$: $f(x)$ trái dấu a $\\implies f(x) < 0$.\n- Bên ngoài $(-\\infty; 2)$ và $(3; +\\infty)$: $f(x)$ cùng dấu a $\\implies f(x) > 0$."
                    },
                    {
                        "title": "Ví dụ 2: Xét dấu khi Delta < 0",
                        "problem": "Xét dấu tam thức $f(x) = x^2 + x + 1$.",
                        "solution": "- Phương trình $x^2 + x + 1 = 0$ vô nghiệm ($\\Delta = -3 < 0$).\n- Hệ số $a = 1 > 0$.\n- Vậy $f(x)$ luôn cùng dấu với a $\\implies f(x) > 0$ với mọi $x \\in \\mathbb{R}$."
                    },
                    {
                        "title": "Ví dụ 3: Xét dấu khi Delta = 0",
                        "problem": "Xét dấu tam thức $f(x) = -x^2 + 4x - 4$.",
                        "solution": "- Ta có $f(x) = -(x - 2)^2$.\n- Vì $(x - 2)^2 \\ge 0 \\implies -(x - 2)^2 \\le 0$ với mọi $x$.\n- Vậy $f(x) < 0$ với mọi $x \\neq 2$, và $f(2) = 0$."
                    }
                ],
                "exercise": {
                    "id": "10_17_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tam thức f(x) = x^2 - 3x + 2 mang dấu âm trên khoảng (1; c). Giá trị của c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Giải bất phương trình bậc hai một ẩn": {
                "theory": "Để giải $ax^2 + bx + c > 0$ (hoặc $< 0, \\ge 0, \\le 0$), ta xét dấu của tam thức bậc hai rồi chọn các khoảng nghiệm thỏa mãn chiều của bất phương trình.",
                "formula": r"f(x) > 0 \iff \text{Lấy các khoảng có dấu } (+)",
                "trap": "Trường hợp $\\ge 0$ hoặc $\\le 0$, học sinh rất hay quên sử dụng dấu ngoặc vuông `[]` ở các điểm nghiệm $x_1, x_2$.",
                "audio": "Giải bất phương trình bậc hai đơn giản là lập trục xét dấu của biểu thức vế trái, sau đó gặt hái kết quả tùy thuộc vào dấu lớn hơn hay nhỏ hơn của đề bài.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải BPT lớn hơn 0",
                        "problem": "Giải bất phương trình $-x^2 + 4x - 3 > 0$.",
                        "solution": "- Nghiệm của $-x^2 + 4x - 3 = 0$ là $x = 1, x = 3$.\n- Hệ số $a = -1 < 0$. Trong trái (dương), ngoài cùng (âm).\n- BPT yêu cầu $>0$ (lấy phần dương) $\\implies$ lấy phần bên trong.\n- **Kết luận:** Tập nghiệm $S = (1; 3)$."
                    },
                    {
                        "title": "Ví dụ 2: Giải BPT có dấu bằng",
                        "problem": "Giải bất phương trình $x^2 - 4 \\le 0$.",
                        "solution": "- Nghiệm: $x = 2, x = -2$.\n- Hệ số $a = 1 > 0$. Dấu bên trong là âm (-).\n- Yêu cầu $\\le 0$ (lấy âm và số 0). Phải dùng ngoặc vuông.\n- **Kết luận:** Tập nghiệm $S = [-2; 2]$."
                    },
                    {
                        "title": "Ví dụ 3: BPT vô nghiệm",
                        "problem": "Giải bất phương trình $x^2 + 2x + 5 < 0$.",
                        "solution": "- Tam thức $x^2 + 2x + 5$ có $\\Delta < 0$, $a = 1 > 0$ nên luôn lớn hơn 0 với mọi $x$.\n- Không có x nào làm nó $< 0$ cả.\n- **Kết luận:** BPT vô nghiệm."
                    }
                ],
                "exercise": {
                    "id": "10_17_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Bất phương trình x^2 - x - 2 < 0 có tập nghiệm là khoảng (-1; c). Giá trị c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 18: Phương trình quy về phương trình bậc hai": {
        "chapter": "Chương VI: Hàm số, Đồ thị và Ứng dụng",
        "topics": {
            "Chủ điểm 1: Giải phương trình chứa ẩn dưới dấu căn": {
                "theory": "Phương trình $\\sqrt{f(x)} = \\sqrt{g(x)}$: Bình phương hai vế $f(x) = g(x)$ và phải thử lại nghiệm, hoặc đặt điều kiện $f(x) \\ge 0$. Phương trình $\\sqrt{f(x)} = g(x)$: Bắt buộc phải đặt điều kiện $g(x) \\ge 0$ rồi mới bình phương $f(x) = g^2(x)$.",
                "formula": r"\sqrt{f(x)} = g(x) \iff \begin{cases} g(x) \ge 0 \\ f(x) = [g(x)]^2 \end{cases}",
                "trap": "Học sinh thường bình phương hai vế một cách máy móc mà KHÔNG đặt điều kiện $g(x) \\ge 0$, dẫn đến nhận vào các 'nghiệm ngoại lai' (nghiệm làm cho $g(x)$ âm).",
                "audio": "Giải phương trình có căn, bình phương hai vế là cách nhanh nhất. Nhưng cẩn thận nhé, vế không chứa căn phải mang dấu dương thì mới được phép bình phương.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Dạng căn f(x) = căn g(x)",
                        "problem": "Giải phương trình $\\sqrt{2x - 1} = \\sqrt{x + 2}$.",
                        "solution": "- Bình phương hai vế: $2x - 1 = x + 2 \\implies x = 3$.\n- Thử lại: Thay $x=3$ vào, $\\sqrt{5} = \\sqrt{5}$ (Đúng).\n- **Kết luận:** Nghiệm $x=3$."
                    },
                    {
                        "title": "Ví dụ 2: Dạng căn f(x) = g(x) (Bẫy nghiệm ngoại lai)",
                        "problem": "Giải phương trình $\\sqrt{x^2 - 3x + 2} = x - 2$.",
                        "solution": "- Đặt điều kiện: $x - 2 \\ge 0 \\iff x \\ge 2$.\n- Bình phương 2 vế: $x^2 - 3x + 2 = (x - 2)^2$.\n- $x^2 - 3x + 2 = x^2 - 4x + 4 \\implies x = 2$.\n- Kiểm tra điều kiện $x \\ge 2$ thấy thỏa mãn. Nghiệm là $x=2$."
                    },
                    {
                        "title": "Ví dụ 3: Loại nghiệm",
                        "problem": "Giải $\\sqrt{x+1} = -2$.",
                        "solution": "- Vế phải bằng $-2 < 0$. Mà căn bậc hai luôn không âm.\n- **Kết luận:** Phương trình vô nghiệm ngay lập tức, không cần bình phương."
                    }
                ],
                "exercise": {
                    "id": "10_18_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Số nghiệm của phương trình căn(x) = x là bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 KẾT NỐI TRI THỨC (PHẦN 3: BÀI 19 -> BÀI 27)
# ==============================================================================

GRADE_10_DATA.update({
    "Bài 19: Phương trình đường thẳng": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "Chủ điểm 1: Vectơ pháp tuyến và Vectơ chỉ phương": {
                "theory": "Đường thẳng $\\Delta$ có Vectơ pháp tuyến (VTPT) $\\vec{n} = (A; B)$ thì vuông góc với đường thẳng. Vectơ chỉ phương (VTCP) $\\vec{u} = (-B; A)$ hoặc $(B; -A)$ có giá song song hoặc trùng với đường thẳng.",
                "formula": r"\vec{n} = (A; B) \implies \vec{u} = (-B; A) \text{ là VTCP}",
                "trap": "Học sinh rất hay nhầm lẫn đổi dấu hoành độ và tung độ khi chuyển từ VTPT sang VTCP.",
                "audio": "Vectơ pháp tuyến vuông góc với đường thẳng, còn vectơ chỉ phương song song. Biết VTPT (A; B), ta lập tức suy ra VTCP bằng cách đổi chỗ hai tọa độ và đổi dấu một trong hai số.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chuyển đổi VTPT sang VTCP",
                        "problem": "Đường thẳng $\\Delta$ có VTPT $\\vec{n} = (3; -4)$. Tìm một VTCP của $\\Delta$.",
                        "solution": "- Đổi chỗ hai tọa độ và đổi dấu một vị trí: $\\vec{u} = (4; 3)$ hoặc $(-4; -3)$."
                    },
                    {
                        "title": "Ví dụ 2: Lấy VTPT từ phương trình tổng quát",
                        "problem": "Cho đường thẳng $\\Delta: 2x - 3y + 5 = 0$. Xác định một VTPT.",
                        "solution": "- Tọa độ VTPT chính là các hệ số của $x$ và $y$ $\\implies \\vec{n} = (2; -3)$."
                    },
                    {
                        "title": "Ví dụ 3: Lấy VTCP từ phương trình tham số",
                        "problem": "Cho đường thẳng $d: \\begin{cases} x = 1 + 2t \\\\ y = -3 + 4t \\end{cases}$. Tìm VTCP.",
                        "solution": "- VTCP lấy theo hệ số của tham số $t \\implies \\vec{u} = (2; 4)$ (hoặc rút gọn là $(1; 2)$)."
                    }
                ],
                "exercise": {
                    "id": "10_19_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường thẳng 5x - 2y + 1 = 0 có hoành độ của VTPT bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Phương trình tổng quát và Phương trình tham số": {
                "theory": "Phương trình tổng quát: $A(x - x_0) + B(y - y_0) = 0 \\iff Ax + By + C = 0$. Phương trình tham số: Đi qua $M_0(x_0; y_0)$ và VTCP $\\vec{u}=(a; b)$.",
                "formula": r"Ax + By + C = 0 \quad (\text{với } A^2 + B^2 > 0)",
                "trap": "Học sinh thường quên nhân phá ngoặc chính xác khi lập phương trình tổng quát từ điểm và VTPT.",
                "audio": "Phương trình tổng quát cần một điểm đi qua và một vectơ pháp tuyến. Cứ lắp công thức A nhân x trừ x không cộng B nhân y trừ y không là ra.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết phương trình tổng quát",
                        "problem": "Viết phương trình tổng quát đường thẳng đi qua $M(1; 2)$ và có VTPT $\\vec{n} = (3; -1)$.",
                        "solution": "- $3(x - 1) - 1(y - 2) = 0$.\n- Khai triển: $3x - 3 - y + 2 = 0 \\iff 3x - y - 1 = 0$."
                    },
                    {
                        "title": "Ví dụ 2: Viết phương trình tham số",
                        "problem": "Viết phương trình tham số đường thẳng đi qua $A(2; -1)$ có VTCP $\\vec{u} = (3; 4)$.",
                        "solution": "- $x = 2 + 3t$\n- $y = -1 + 4t$"
                    }
                ],
                "exercise": {
                    "id": "10_19_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường thẳng đi qua M(1; 1) có VTPT n = (2; 3) có phương trình tổng quát 2x + 3y + C = 0. Giá trị C bằng:", 
                    "type": "NUMERIC", 
                    "target": "-5", 
                    "options": []
                }
            }
        }
    },
    "Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "Chủ điểm 1: Vị trí tương đối và Góc giữa hai đường thẳng": {
                "theory": "Hai đường thẳng có thể cắt nhau, song song hoặc trùng nhau. Góc giữa hai đường thẳng được tính thông qua cosin góc giữa hai VTPT (lấy trị tuyệt đối vì góc $\\le 90^\\circ$).",
                "formula": r"\cos(\Delta_1, \Delta_2) = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1| \cdot |\vec{n}_2|}",
                "trap": "Quên lấy trị tuyệt đối ở tử số, dẫn đến cosin mang giá trị âm, sai định nghĩa góc giữa hai đường thẳng.",
                "audio": "Góc giữa hai đường thẳng luôn là góc nhọn hoặc vuông, do đó công thức tính cosin bắt buộc phải có dấu giá trị tuyệt đối ở tử số.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét vị trí tương đối",
                        "problem": "Xét vị trí tương đối của hai đường thẳng $\\Delta_1: x + 2y - 3 = 0$ và $\\Delta_2: 2x + 4y + 5 = 0$.",
                        "solution": "- Lập tỉ lệ hệ số: $\\frac{1}{2} = \\frac{2}{4} \\neq \\frac{-3}{5}$.\n- **Kết luận:** Hai đường thẳng song song với nhau."
                    },
                    {
                        "title": "Ví dụ 2: Tính góc giữa hai đường thẳng",
                        "problem": "Tính góc giữa hai đường thẳng $\\Delta_1: x - y = 0$ và $\\Delta_2: x = 0$.",
                        "solution": "- $\\vec{n}_1 = (1; -1)$ và $\\vec{n}_2 = (1; 0)$.\n- $\\cos = \\frac{|1(1) + (-1)0|}{\\sqrt{2} \\cdot 1} = \\frac{1}{\\sqrt{2}} \\implies \\text{Góc bằng } 45^\\circ$."
                    }
                ],
                "exercise": {
                    "id": "10_20_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường thẳng x + y = 0 và x - y = 0 tạo với nhau một góc bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            },
            "Chủ điểm 2: Khoảng cách từ một điểm đến một đường thẳng": {
                "theory": "Khoảng cách từ điểm $M_0(x_0; y_0)$ đến đường thẳng $\\Delta: Ax + By + C = 0$ được tính bằng công thức thay tọa độ điểm vào vế trái lấy trị tuyệt đối chia cho độ dài VTPT.",
                "formula": r"d(M_0, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
                "trap": "Học sinh thường quên mất căn bậc hai ở mẫu số, hoặc quên dấu giá trị tuyệt đối ở tử số.",
                "audio": "Công thức tính khoảng cách rất giống trong không gian Oxyz. Lấy tọa độ điểm thay vào phương trình đường thẳng, lấy trị tuyệt đối rồi chia cho căn a bình cộng b bình.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách từ điểm đến đường thẳng",
                        "problem": "Tính khoảng cách từ điểm $M(1; 2)$ đến đường thẳng $\\Delta: 3x - 4y + 5 = 0$.",
                        "solution": "- Tử số: $|3(1) - 4(2) + 5| = |3 - 8 + 5| = 0$.\n- **Kết luận:** Điểm M nằm trên đường thẳng nên khoảng cách bằng 0."
                    },
                    {
                        "title": "Ví dụ 2: Khoảng cách từ gốc tọa độ",
                        "problem": "Tính khoảng cách từ gốc tọa độ $O(0;0)$ đến đường thẳng $4x + 3y - 10 = 0$.",
                        "solution": "- $d = \\frac{|4(0) + 3(0) - 10|}{\\sqrt{4^2 + 3^2}} = \\frac{10}{5} = 2$."
                    }
                ],
                "exercise": {
                    "id": "10_20_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Khoảng cách từ gốc tọa độ O đến đường thẳng 3x + 4y - 10 = 0 bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 21: Đường tròn trong mặt phẳng tọa độ": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "Chủ điểm 1: Phương trình đường tròn": {
                "theory": "Đường tròn $(C)$ tâm $I(a; b)$ bán kính $R$ có phương trình chính tắc $(x - a)^2 + (y - b)^2 = R^2$. Dạng khai triển: $x^2 + y^2 - 2ax - 2by + c = 0$ với điều kiện $a^2 + b^2 - c > 0$.",
                "formula": r"(x - a)^2 + (y - b)^2 = R^2; \quad R = \sqrt{a^2 + b^2 - c}",
                "trap": "Học sinh rất hay quên điều kiện $a^2 + b^2 - c > 0$ khi kiểm tra phương trình tổng quát có phải là đường tròn hay không.",
                "audio": "Phương trình đường tròn dạng chính tắc có bình phương hai hiệu tọa độ bằng R bình. Nhớ đổi dấu tọa độ tâm I nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tâm và bán kính",
                        "problem": "Tìm tâm và bán kính của đường tròn $(x - 2)^2 + (y + 3)^2 = 25$.",
                        "solution": "- Đổi dấu tọa độ: Tâm $I(2; -3)$.\n- Lấy căn bậc hai: Bán kính $R = \\sqrt{25} = 5$."
                    },
                    {
                        "title": "Ví dụ 2: Xác định tâm từ dạng khai triển",
                        "problem": "Tìm tọa độ tâm đường tròn $x^2 + y^2 - 4x + 6y - 3 = 0$.",
                        "solution": "- Lấy hệ số của x, y chia cho $-2$:\n- $a = -4/(-2) = 2$; $b = 6/(-2) = -3$.\n- **Kết luận:** Tâm $I(2; -3)$."
                    }
                ],
                "exercise": {
                    "id": "10_21_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường tròn (x - 1)^2 + (y - 2)^2 = 9 có bán kính R bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 22: Ba đường conic": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "Chủ điểm 1: Phương trình chính tắc của Elip": {
                "theory": "Elip có phương trình chính tắc $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ (với $a > b > 0$). Tiêu cự $2c$ với $c^2 = a^2 - b^2$. Độ dài trục lớn $2a$, trục nhỏ $2b$.",
                "formula": r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1; \quad c^2 = a^2 - b^2",
                "trap": "Trong công thức liên hệ của Elip, $c^2 = a^2 - b^2$ (dấu TRỪ), học sinh hay nhầm lẫn với định lý Pytago thành dấu cộng.",
                "audio": "Elip có công thức c bình bằng a bình trừ b bình. Trục lớn là 2a, trục nhỏ là 2b. Đừng nhầm lẫn với dấu cộng nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm độ dài trục lớn và trục nhỏ",
                        "problem": "Cho Elip $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$. Tìm độ dài trục lớn và trục nhỏ.",
                        "solution": "- Ta có $a^2 = 25 \\implies a = 5$; $b^2 = 9 \\implies b = 3$.\n- Độ dài trục lớn $2a = 10$. Độ dài trục nhỏ $2b = 6$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm tiêu cự",
                        "problem": "Từ Elip trên, tính tiêu cự $2c$.",
                        "solution": "- $c^2 = a^2 - b^2 = 25 - 9 = 16 \\implies c = 4$.\n- Tiêu cự $2c = 8$."
                    }
                ],
                "exercise": {
                    "id": "10_22_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho Elip x^2/25 + y^2/9 = 1. Tiêu cự 2c bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "8", 
                    "options": []
                }
            }
        }
    },
    "Bài 23: Quy tắc đếm": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "Chủ điểm 1: Quy tắc cộng và Quy tắc nhân": {
                "theory": "Quy tắc cộng: Một công việc hoàn thành bằng 1 trong các phương án độc lập (hoặc phương án này, hoặc phương án kia) thì dùng CỘNG. Quy tắc nhân: Công việc hoàn thành qua nhiều công đoạn liên tiếp (đoạn này rồi đoạn kia) thì dùng NHÂN.",
                "formula": r"N = m + n \ (\text{Cộng}); \quad N = m \cdot n \ (\text{Nhân})",
                "trap": "Học sinh thường loạn trí không biết lúc nào dùng cộng, lúc nào dùng nhân. Cứ nhớ: 'Hoàn thành ngay' dùng cộng, 'Phải qua nhiều bước mới xong' dùng nhân.",
                "audio": "Hoặc phương án này hoặc phương án kia thì cộng lại. Còn phải trải qua nhiều công đoạn nối tiếp nhau thì ta nhân các cách lại với nhau.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc cộng",
                        "problem": "Hộp có 3 bi đỏ và 4 bi xanh. Lấy ngẫu nhiên 1 viên bi. Có bao nhiêu cách chọn?",
                        "solution": "- Chọn 1 bi đỏ (3 cách) hoặc 1 bi xanh (4 cách).\n- Áp dụng quy tắc cộng: $3 + 4 = 7$ cách."
                    },
                    {
                        "title": "Ví dụ 2: Áp dụng quy tắc nhân",
                        "problem": "Từ thành phố A đến B có 2 con đường, từ B đến C có 3 con đường. Hỏi có bao nhiêu cách đi từ A qua B đến C?",
                        "solution": "- Phải qua 2 bước liên tiếp: Bước 1 (2 cách), Bước 2 (3 cách).\n- Quy tắc nhân: $2 \\times 3 = 6$ cách."
                    }
                ],
                "exercise": {
                    "id": "10_23_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Có 3 áo và 4 quần. Số cách chọn 1 bộ quần áo bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "12", 
                    "options": []
                }
            }
        }
    },
    "Bài 24: Hoán vị, chỉnh hợp và tổ hợp": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "Chủ điểm 1: Phân biệt Hoán vị, Chỉnh hợp và Tổ hợp": {
                "theory": "Hoán vị $P_n = n!$ (sắp xếp n phần tử). Chỉnh hợp $A_n^k$ (chọn k phần tử từ n phần tử CÓ QUAN TÂM THỨ TỰ và không lặp). Tổ hợp $C_n^k$ (chọn k phần tử KHÔNG QUAN TÂM THỨ TỰ).",
                "formula": r"A_n^k = \frac{n!}{(n-k)!}; \quad C_n^k = \frac{n!}{k!(n-k)!}",
                "trap": "Nhầm lẫn giữa Tổ hợp và Chỉnh hợp. Cứ thấy bài toán có từ 'xếp hàng', 'lập số', 'phân công chức vụ' (có thứ tự) thì dùng Chỉnh hợp. Chỉ 'chọn nhóm', 'bốc thăm' thì dùng Tổ hợp.",
                "audio": "Chọn mà có sắp xếp, có quan tâm vị trí thứ tự thì dùng chỉnh hợp. Còn chọn một nhóm chung chung không quan tâm ai trước ai sau thì dùng tổ hợp.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổ hợp",
                        "problem": "Tính giá trị của $C_5^2$.",
                        "solution": "- $C_5^2 = \\frac{5!}{2!(5-2)!} = \\frac{5 \\cdot 4}{2 \\cdot 1} = 10$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chỉnh hợp",
                        "problem": "Tính giá trị của $A_4^2$.",
                        "solution": "- $A_4^2 = \\frac{4!}{(4-2)!} = 4 \\cdot 3 = 12$."
                    }
                ],
                "exercise": {
                    "id": "10_24_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tính giá trị của tổ hợp C_4^2 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "6", 
                    "options": []
                }
            }
        }
    },
    "Bài 25: Nhị thức Newton": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "Chủ điểm 1: Khai triển nhị thức Newton và Số hạng tổng quát": {
                "theory": "Công thức khai triển $(a + b)^n$ có $n+1$ số hạng. Số hạng tổng quát (số hạng thứ $k+1$) có dạng $T_{k+1} = C_n^k a^{n-k} b^k$.",
                "formula": r"T_{k+1} = C_n^k a^{n-k} b^k \quad (0 \le k \le n)",
                "trap": "Học sinh rất hay nhầm lẫn số hạng tổng quát là $T_k$ thay vì $T_{k+1}$. Điều này làm lệch chỉ số mũ của a và b.",
                "audio": "Số hạng tổng quát trong khai triển nhị thức Newton luôn mang chỉ số k cộng một. Hãy nhớ công thức C chập k của n nhân a mũ n trừ k nhân b mũ k.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Số lượng số hạng",
                        "problem": "Khai triển biểu thức $(x + 2)^5$ có tất cả bao nhiêu số hạng?",
                        "solution": "- Số mũ là $n = 5$ nên số lượng số hạng là $n + 1 = 6$ số hạng."
                    },
                    {
                        "title": "Ví dụ 2: Tìm số hạng cụ thể",
                        "problem": "Tìm số hạng chứa $x^3$ trong khai triển $(x + 2)^4$.",
                        "solution": "- Số hạng tổng quát: $T_{k+1} = C_4^k x^{4-k} 2^k$.\n- Để có $x^3$ thì số mũ của x phải bằng 3 $\\implies 4 - k = 3 \\implies k = 1$.\n- Số hạng đó là: $C_4^1 x^3 2^1 = 4 \\cdot 2 \\cdot x^3 = 8x^3$."
                    }
                ],
                "exercise": {
                    "id": "10_25_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Khai triển biểu thức (x + 1)^4 có tổng cộng bao nhiêu số hạng?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            }
        }
    },
    "Bài 26: Biến cố và định nghĩa cổ điển của xác suất": {
        "chapter": "Chương IX: Một số yếu tố xác suất",
        "topics": {
            "Chủ điểm 1: Xác suất theo định nghĩa cổ điển": {
                "theory": "Không gian mẫu $\\Omega$ là tập hợp tất cả các kết quả có thể xảy ra của phép thử. Xác suất của biến cố A bằng số phần tử thuận lợi chia cho số phần tử của không gian mẫu.",
                "formula": r"P(A) = \frac{n(A)}{n(\Omega)} \quad (0 \le P(A) \le 1)",
                "trap": "Xác suất của một biến cố phải luôn nằm trong đoạn từ 0 đến 1. Nếu tính ra số âm hoặc lớn hơn 1 thì chắc chắn đã bị sai.",
                "audio": "Xác suất cổ điển rất trực diện: Lấy số kết quả thuận lợi chia cho tổng số kết quả có thể xảy ra trong không gian mẫu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Gieo xúc xắc",
                        "problem": "Gieo một con xúc xắc cân đối 6 mặt. Tính xác suất xuất hiện mặt có số chấm là số nguyên tố.",
                        "solution": "- Không gian mẫu $n(\\Omega) = 6$ ({1, 2, 3, 4, 5, 6}).\n- Các mặt là số nguyên tố là: 2, 3, 5 $\\implies n(A) = 3$.\n- Xác suất $P(A) = 3/6 = 0.5$."
                    },
                    {
                        "title": "Ví dụ 2: Rút bài",
                        "problem": "Rút ngẫu nhiên 1 lá bài từ bộ 52 lá. Tính xác suất rút được lá Át.",
                        "solution": "- $n(\\Omega) = 52$. Số lá Át là $n(A) = 4$.\n- $P(A) = 4/52 = 1/13$."
                    }
                ],
                "exercise": {
                    "id": "10_26_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Gieo đồng thời 2 con xúc xắc cân đối. Số phần tử của không gian mẫu n(Omega) bằng:", 
                    "type": "NUMERIC", 
                    "target": "36", 
                    "options": []
                }
            }
        }
    },
    "Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển": {
        "chapter": "Chương IX: Một số yếu tố xác suất",
        "topics": {
            "Chủ điểm 1: Tính xác suất bằng phương pháp đếm tổ hợp": {
                "theory": "Sử dụng các công thức Tổ hợp ($C_n^k$), Chỉnh hợp ($A_n^k$) để đếm số phần tử của không gian mẫu và số phần tử của biến cố phức hợp trong các bài toán bốc thăm, chọn người.",
                "formula": r"P(A) = \frac{C_{n_1}^{k_1} \cdot C_{n_2}^{k_2}}{C_n^k}",
                "trap": "Chọn đồng thời nhiều vật thì dùng Tổ hợp ($C_n^k$), không dùng chỉnh hợp vì việc đổi chỗ các vật được chọn không tạo ra nhóm mới.",
                "audio": "Khi chọn một nhóm người hay bốc một lúc nhiều viên bi, ta dùng tổ hợp C để tính số phần tử cho cả không gian mẫu và biến cố.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bốc bi từ hộp",
                        "problem": "Hộp có 4 bi đỏ và 3 bi xanh. Chọn ngẫu nhiên 2 viên bi. Tính xác suất chọn được 2 viên cùng màu.",
                        "solution": "- Không gian mẫu: chọn ngẫu nhiên 2 viên từ 7 viên $\\implies n(\\Omega) = C_7^2 = 21$.\n- Biến cố A: Chọn 2 bi đỏ ($C_4^2 = 6$) hoặc 2 bi xanh ($C_3^2 = 3$).\n- $n(A) = 6 + 3 = 9$.\n- Xác suất $P(A) = 9/21 = 3/7$."
                    },
                    {
                        "title": "Ví dụ 2: Chọn học sinh",
                        "problem": "Tổ có 5 nam và 4 nữ. Chọn ngẫu nhiên 3 học sinh. Tính xác suất có đúng 2 nam.",
                        "solution": "- $n(\\Omega) = C_9^3 = 84$.\n- Chọn 2 nam từ 5 nam ($C_5^2 = 10$) và 1 nữ từ 4 nữ ($C_4^1 = 4$).\n- $n(A) = 10 \\times 4 = 40$.\n- $P(A) = 40/84 = 10/21$."
                    }
                ],
                "exercise": {
                    "id": "10_27_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Chọn ngẫu nhiên 2 viên bi từ hộp gồm 3 bi đỏ và 2 bi vàng. Số phần tử không gian mẫu n(Omega) bằng:", 
                    "type": "NUMERIC", 
                    "target": "10", 
                    "options": []
                }
            }
        }
    }
})