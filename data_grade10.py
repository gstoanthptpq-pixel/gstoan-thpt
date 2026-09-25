# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 KẾT NỐI TRI THỨC (PHẦN 1: BÀI 1 -> BÀI 14)
# ==============================================================================

GRADE_10_DATA = {}

GRADE_10_DATA.update({
    "Bài 1: Mệnh đề toán học": {
        "chapter": "Chương I: Mệnh đề và tập hợp",
        "topics": {
            "I. Mệnh đề, mệnh đề chứa biến": {
                "theory": "Mệnh đề toán học là một khẳng định có tính đúng hoặc sai tuyệt đối. Không có mệnh đề nào vừa đúng vừa sai. Các câu hỏi, câu cảm thán không phải là mệnh đề. Mệnh đề chứa biến (ví dụ: $x > 5$) chưa phải là mệnh đề, nó chỉ trở thành mệnh đề khi gán cho x một giá trị cụ thể.",
                "formula": r"P \in \{\text{Đúng}, \text{Sai}\}",
                "trap": "Học sinh thường nhầm mệnh đề chứa biến là mệnh đề toán học. Phải nhớ: Chưa biết tính đúng sai thì chưa phải mệnh đề.",
                "audio": "Mệnh đề là một câu khẳng định chỉ nhận một trong hai giá trị là đúng hoặc sai. Câu cảm thán hay câu hỏi tuyệt đối không phải là mệnh đề nhé.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện mệnh đề",
                        "problem": "Trong các câu sau: (1) 'Trời đẹp quá!', (2) 'Số 15 là số nguyên tố', (3) '2 + 3 = 5'. Câu nào là mệnh đề toán học?",
                        "solution": "- Câu (1) là câu cảm thán $\\implies$ Không phải mệnh đề.\n- Câu (2) là khẳng định sai $\\implies$ Là mệnh đề toán học.\n- Câu (3) là khẳng định đúng $\\implies$ Là mệnh đề toán học."
                    },
                    {
                        "title": "Ví dụ 2: Mệnh đề chứa biến",
                        "problem": "Phát biểu $P(x): x^2 + 1 > 0$ có phải là mệnh đề không?",
                        "solution": "- Đây là mệnh đề chứa biến, bản thân nó chưa phải là mệnh đề vì chưa xác định x.\n- Nếu thay $x=1$, ta được mệnh đề đúng: $1^2 + 1 > 0$."
                    }
                ],
                "exercise": {"id": "10_1_1", "title": "Kiểm minh chứng", "content": "Trong các câu: 'Hôm nay ăn gì?', '2 < 1', 'x + 1 = 3'. Có mấy câu là mệnh đề toán học?", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Mệnh đề phủ định": {
                "theory": "Phủ định của mệnh đề P ký hiệu là $\\overline{P}$. Nếu P đúng thì $\\overline{P}$ sai, và ngược lại. Để phủ định một mệnh đề, ta thường thêm (hoặc bớt) từ 'không' hoặc 'không phải' vào trước vị ngữ.",
                "formula": r"\text{P Đúng} \implies \overline{P} \text{ Sai}",
                "trap": "Khi phủ định mệnh đề có chứa dấu toán học: Phủ định của $>$ là $\\le$, phủ định của $<$ là $\\ge$. Rất nhiều bạn quên dấu bằng.",
                "audio": "Phủ định của một mệnh đề là nói ngược lại. Phủ định của Đúng là Sai. Chú ý phủ định của dấu lớn hơn là nhỏ hơn hoặc bằng nhé.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết mệnh đề phủ định",
                        "problem": "Viết mệnh đề phủ định của P: 'Số 5 là số chẵn'.",
                        "solution": "- Mệnh đề phủ định $\\overline{P}$: 'Số 5 KHÔNG PHẢI là số chẵn'."
                    },
                    {
                        "title": "Ví dụ 2: Phủ định bất đẳng thức",
                        "problem": "Lập phủ định của mệnh đề Q: '$\pi > 3$'.",
                        "solution": "- Phủ định của $>$ là $\\le$.\n- Mệnh đề phủ định $\\overline{Q}$: '$\pi \\le 3$'."
                    }
                ],
                "exercise": {"id": "10_1_2", "title": "Kiểm minh chứng", "content": "Phủ định của x > 5 là x <= c. Giá trị của c bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "III. Mệnh đề kéo theo và Lượng từ": {
                "theory": "Mệnh đề kéo theo $P \implies Q$ chỉ SAI khi P đúng và Q sai. Các trường hợp còn lại đều đúng. Ký hiệu $\\forall$ là 'với mọi', $\\exists$ là 'tồn tại'. Phủ định của $\\forall$ là $\\exists$ và ngược lại.",
                "formula": r"\overline{\forall x \in X, P(x)} \iff \exists x \in X, \overline{P(x)}",
                "trap": "Học sinh hay bị lừa ở mệnh đề kéo theo: Nếu P sai thì $P \implies Q$ LUÔN ĐÚNG bất kể Q đúng hay sai.",
                "audio": "Mệnh đề kéo theo chỉ sai duy nhất trong trường hợp từ chân lý đúng suy ra điều sai trái. Còn phủ định của 'với mọi' chính là 'tồn tại'.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đúng sai của mệnh đề kéo theo",
                        "problem": "Mệnh đề 'Nếu $2 < 1$ thì Trái Đất hình vuông' đúng hay sai?",
                        "solution": "- Mệnh đề P ('$2 < 1$') là Sai.\n- Theo quy tắc, khi P sai thì $P \implies Q$ luôn luôn Đúng."
                    },
                    {
                        "title": "Ví dụ 2: Phủ định lượng từ",
                        "problem": "Viết phủ định của mệnh đề '$\\forall x \\in \\mathbb{R}, x^2 \\ge 0$'.",
                        "solution": "- Lượng từ $\\forall$ đổi thành $\\exists$. Dấu $\\ge$ đổi thành $<$.\n- Phủ định: '$\\exists x \\in \\mathbb{R}, x^2 < 0$'."
                    }
                ],
                "exercise": {"id": "10_1_3", "title": "Kiểm minh chứng", "content": "Mệnh đề 'Nếu 3 < 2 thì 5 = 10' là mệnh đề Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 2: Tập hợp và các phép toán trên tập hợp": {
        "chapter": "Chương I: Mệnh đề và tập hợp",
        "topics": {
            "I. Khái niệm tập hợp và Tập con": {
                "theory": "Tập hợp có thể xác định bằng cách liệt kê hoặc chỉ ra tính chất đặc trưng. Tập $A$ là tập con của $B$ ($A \subset B$) nếu mọi phần tử của $A$ đều thuộc $B$. Tập rỗng $\emptyset$ là tập con của mọi tập hợp.",
                "formula": r"A \subset B \iff (\forall x \in A \implies x \in B)",
                "trap": "Dùng sai ký hiệu $\in$ và $\subset$. Ký hiệu $\in$ dùng cho PHẦN TỬ, còn $\subset$ dùng cho TẬP HỢP.",
                "audio": "Phần tử thì 'thuộc' tập hợp, còn tập hợp thì 'là tập con' của tập hợp khác. Nhớ là tập rỗng luôn là con của mọi tập hợp nhé.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết tập hợp",
                        "problem": "Liệt kê phần tử tập $A = \{x \in \mathbb{N} \mid x < 4\}$.",
                        "solution": "- Các số tự nhiên nhỏ hơn 4 là 0, 1, 2, 3.\n- $A = \{0; 1; 2; 3\}$."
                    },
                    {
                        "title": "Ví dụ 2: Số tập con",
                        "problem": "Tập $X = \{1; 2\}$ có bao nhiêu tập con?",
                        "solution": "- Tập con 0 phần tử: $\emptyset$.\n- Tập con 1 phần tử: $\{1\}, \{2\}$.\n- Tập con 2 phần tử: $\{1; 2\}$.\n- Tổng cộng có $2^2 = 4$ tập con."
                    }
                ],
                "exercise": {"id": "10_2_1", "title": "Kiểm minh chứng", "content": "Tập hợp C = {1; 2; 3} có tổng cộng bao nhiêu tập con?", "type": "NUMERIC", "target": "8", "options": []}
            },
            "II. Các phép toán trên tập hợp": {
                "theory": "Giao ($A \cap B$): Lấy phần tử CHUNG. Hợp ($A \cup B$): Lấy TẤT CẢ. Hiệu ($A \setminus B$): Lấy phần tử thuộc A nhưng không thuộc B. Phần bù: Là phép hiệu khi A là tập con của B.",
                "formula": r"A \cap B = \{x \mid x \in A \text{ và } x \in B\}",
                "trap": "Khi lấy giao/hợp trên trục số, học sinh thường nhầm ngoặc vuông `[]` thành ngoặc tròn `()` tại các đầu mút.",
                "audio": "Giao là lấy phần chung, hợp là lấy tất cả. Hiệu của A trừ B là giữ lại những gì của riêng A mà B không có.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giao và Hợp",
                        "problem": "Cho $A = \{1; 2; 3\}$, $B = \{2; 3; 4\}$. Tìm $A \cap B$ và $A \cup B$.",
                        "solution": "- $A \cap B = \{2; 3\}$ (phần chung).\n- $A \cup B = \{1; 2; 3; 4\}$ (lấy tất cả, không lặp)."
                    },
                    {
                        "title": "Ví dụ 2: Phép toán trên trục số",
                        "problem": "Cho $A = (-1; 5)$ và $B = [3; 7]$. Tìm $A \cap B$.",
                        "solution": "- Giao của khoảng $(-1; 5)$ và đoạn $[3; 7]$ là phần trùng nhau từ 3 đến 5.\n- **Kết quả:** $[3; 5)$."
                    }
                ],
                "exercise": {"id": "10_2_2", "title": "Kiểm minh chứng", "content": "Cho A = [1; 4] và B = (2; 6). Có bao nhiêu số nguyên thuộc A giao B?", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 3: Bất phương trình bậc nhất hai ẩn": {
        "chapter": "Chương II: Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
        "topics": {
            "I. Khái niệm và Bất phương trình": {
                "theory": "Bất phương trình bậc nhất hai ẩn có dạng $ax + by < c$ (hoặc $\le, >, \ge$). Cặp số $(x_0; y_0)$ là nghiệm nếu thay vào BPT ta được một mệnh đề đúng.",
                "formula": r"ax + by \le c \quad (a^2 + b^2 \neq 0)",
                "trap": "Cần phân biệt rõ BPT bậc nhất hai ẩn (mũ của x và y phải là 1) với các BPT bậc hai.",
                "audio": "Cặp số x y được gọi là nghiệm nếu khi em thay tọa độ của chúng vào bất phương trình, ta thu được một phép toán đúng.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện BPT",
                        "problem": "BPT $2x^2 + y < 3$ có phải là BPT bậc nhất hai ẩn không?",
                        "solution": "- Không, vì x có số mũ là 2 (bậc hai)."
                    },
                    {
                        "title": "Ví dụ 2: Kiểm tra nghiệm",
                        "problem": "Cặp số $(1; -1)$ có phải là nghiệm của $x + 2y \le 0$ không?",
                        "solution": "- Thay $x=1, y=-1$ vào vế trái: $1 + 2(-1) = -1$.\n- Vì $-1 \le 0$ là Đúng, nên $(1; -1)$ là nghiệm."
                    }
                ],
                "exercise": {"id": "10_3_1", "title": "Kiểm minh chứng", "content": "Gốc O(0;0) có thuộc miền nghiệm của 3x - 2y < 5 không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "1", "options": []}
            },
            "II. Biểu diễn miền nghiệm": {
                "theory": "Biểu diễn miền nghiệm bằng 2 bước: (1) Vẽ đường thẳng bờ $d: ax+by=c$. (2) Lấy điểm thử (thường là O(0;0)) thay vào BPT. Nếu đúng thì gạch bỏ nửa kia, nếu sai thì gạch bỏ nửa chứa O.",
                "formula": r"\text{Bờ } d: ax + by = c",
                "trap": "Đường bờ d vẽ NÉT LIỀN nếu có dấu bằng ($\le, \ge$), vẽ NÉT ĐỨT nếu không có dấu bằng ($<, >$).",
                "audio": "Cách vẽ miền nghiệm rất dễ: vẽ bờ trước, chọn điểm thử thay vào, đúng thì giữ lại, sai thì gạch đi.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét miền nghiệm",
                        "problem": "Miền nghiệm của $2x + y > 2$ có chứa gốc tọa độ O không?",
                        "solution": "- Thay $O(0;0)$ vào BPT: $2(0) + 0 > 2 \iff 0 > 2$ (Sai).\n- Vậy miền nghiệm không chứa gốc tọa độ O."
                    }
                ],
                "exercise": {"id": "10_3_2", "title": "Kiểm minh chứng", "content": "Đường bờ của miền nghiệm x + y < 2 được vẽ bằng nét liền. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 4: Hệ bất phương trình bậc nhất hai ẩn": {
        "chapter": "Chương II: Bất phương trình và Hệ bất phương trình bậc nhất hai ẩn",
        "topics": {
            "I. Hệ bất phương trình bậc nhất hai ẩn": {
                "theory": "Hệ BPT gồm nhiều BPT bậc nhất 2 ẩn. Miền nghiệm của hệ là PHẦN GIAO của các miền nghiệm thành phần (phần mặt phẳng không bị gạch sau khi vẽ tất cả các bờ).",
                "formula": r"\text{Miền nghiệm là phần KHÔNG BỊ GẠCH}",
                "trap": "Học sinh thường gạch nhầm hướng do không xét điểm thử cẩn thận cho TỪNG bất phương trình.",
                "audio": "Miền nghiệm của hệ chính là phần đất còn lại sau khi em đã gạch bỏ đi những phần không thỏa mãn của từng bất phương trình con.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Điểm thuộc hệ",
                        "problem": "Điểm $M(1; 1)$ có thuộc miền nghiệm của hệ: $x > 0$ và $x + y \le 3$ không?",
                        "solution": "- Thỏa BPT 1: $1 > 0$ (Đúng).\n- Thỏa BPT 2: $1 + 1 \le 3$ (Đúng).\n- Vì thỏa mãn cả hai, $M(1; 1)$ là nghiệm của hệ."
                    }
                ],
                "exercise": {"id": "10_4_1", "title": "Kiểm minh chứng", "content": "Điểm (0;0) có thuộc miền nghiệm của hệ x >= 0 và y >= 1 không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            },
            "II. Ứng dụng giải toán tối ưu": {
                "theory": "Các bài toán thực tế (tìm lợi nhuận lớn nhất, chi phí nhỏ nhất) thường được đưa về bài toán tìm GTLN, GTNN của biểu thức $F(x, y) = ax + by$ trên một miền đa giác. Định lý: F luôn đạt giá trị tối ưu tại một trong CÁC ĐỈNH của đa giác.",
                "formula": r"\max F(x, y) = \max \{F(A), F(B), F(C)\}",
                "trap": "Nhiều bạn chỉ tính tại 1 đỉnh rồi kết luận luôn. Bắt buộc phải tính giá trị F tại TẤT CẢ các đỉnh rồi mới so sánh.",
                "audio": "Hàm chi phí hay lợi nhuận luôn đạt giá trị lớn nhất hoặc nhỏ nhất tại các đỉnh của đa giác miền nghiệm. Em cứ tính hết các đỉnh ra rồi so sánh nhé.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm GTLN",
                        "problem": "Đa giác miền nghiệm có 3 đỉnh $O(0;0), A(0;4), B(3;0)$. Tìm GTLN của $F = 2x + 3y$.",
                        "solution": "- $F(O) = 0$.\n- $F(A) = 2(0) + 3(4) = 12$.\n- $F(B) = 2(3) + 3(0) = 6$.\n- So sánh: GTLN là 12."
                    }
                ],
                "exercise": {"id": "10_4_2", "title": "Kiểm minh chứng", "content": "Với 3 đỉnh (0;0), (0;2), (3;0), GTLN của F = x + 5y bằng bao nhiêu?", "type": "NUMERIC", "target": "10", "options": []}
            }
        }
    },
    "Bài 5: Giá trị lượng giác của một góc từ 0 đến 180 độ": {
        "chapter": "Chương III: Hệ thức lượng trong tam giác",
        "topics": {
            "I. Nửa đường tròn lượng giác": {
                "theory": "Với góc $\alpha$ ($0^\circ \le \alpha \le 180^\circ$), trên nửa đường tròn đơn vị (R=1), điểm $M(x; y)$ biểu diễn góc $\alpha$ có hoành độ là $\cos\alpha$, tung độ là $\sin\alpha$. Từ đó $\tan\alpha = y/x$ và $\cot\alpha = x/y$.",
                "formula": r"\sin\alpha = y; \quad \cos\alpha = x; \quad \tan\alpha = \frac{\sin\alpha}{\cos\alpha}",
                "trap": "Góc tù (từ $90^\circ$ đến $180^\circ$) luôn có $\cos\alpha < 0$. Rất hay sai dấu khi khai căn.",
                "audio": "Trên nửa đường tròn lượng giác, tung độ là sin, hoành độ là cos. Nhớ là góc tù thì cos luôn mang dấu âm nhé.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính giá trị qua tọa độ",
                        "problem": "Điểm M biểu diễn góc $\alpha$ có tọa độ $(-1/2; \sqrt{3}/2)$. Tính $\cos\alpha$.",
                        "solution": "- $\cos\alpha$ chính là hoành độ của điểm M.\n- Vậy $\cos\alpha = -1/2$."
                    }
                ],
                "exercise": {"id": "10_5_1", "title": "Kiểm minh chứng", "content": "Điểm M(0; 1) biểu diễn góc alpha bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "II. Tính chất của hai góc bù nhau, phụ nhau": {
                "theory": "Hai góc BÙ NHAU ($\alpha$ và $180^\circ - \alpha$): Sin bằng nhau, Cos đối nhau. Hai góc PHỤ NHAU ($\alpha$ và $90^\circ - \alpha$): Chéo nhau (Sin góc này bằng Cos góc kia).",
                "formula": r"\sin(180^\circ - \alpha) = \sin\alpha; \quad \cos(180^\circ - \alpha) = -\cos\alpha",
                "trap": "Nhầm $\cos(180^\circ - \alpha) = \cos\alpha$. Cos của hai góc bù nhau phải ĐỐI NHAU (thêm dấu trừ).",
                "audio": "Sin bù, phụ chéo. Hai góc bù nhau có sin bằng nhau, còn cos, tan, cot đều phải thêm dấu trừ.",
                "svg": "LUONG_GIAC",
                "examples": [
                    {
                        "title": "Ví dụ 1: Dùng góc bù",
                        "problem": "Tính $\cos 120^\circ$ biết $\cos 60^\circ = 0.5$.",
                        "solution": "- $120^\circ$ và $60^\circ$ là 2 góc bù nhau.\n- $\cos 120^\circ = -\cos 60^\circ = -0.5$."
                    },
                    {
                        "title": "Ví dụ 2: Dùng góc phụ",
                        "problem": "Tính $\sin 30^\circ$ biết $\cos 60^\circ = 0.5$.",
                        "solution": "- $30^\circ$ và $60^\circ$ phụ nhau.\n- $\sin 30^\circ = \cos 60^\circ = 0.5$."
                    }
                ],
                "exercise": {"id": "10_5_2", "title": "Kiểm minh chứng", "content": "Biết sin(30 độ) = 0.5. Giá trị của sin(150 độ) bằng bao nhiêu?", "type": "NUMERIC", "target": "0.5", "options": []}
            }
        }
    },
    "Bài 6: Hệ thức lượng trong tam giác": {
        "chapter": "Chương III: Hệ thức lượng trong tam giác",
        "topics": {
            "I. Định lý côsin": {
                "theory": "Bình phương một cạnh của tam giác bằng tổng bình phương hai cạnh kia TRỪ ĐI 2 lần tích của chúng nhân với cosin của góc xen giữa. Đây là công cụ tính cạnh khi biết 2 cạnh và 1 góc.",
                "formula": r"a^2 = b^2 + c^2 - 2bc \cos A",
                "trap": "Học sinh thường quên nhân số 2 trong cụm $-2bc\cos A$, hoặc nhầm dấu trừ thành dấu cộng.",
                "audio": "Định lý Côsin là bản nâng cấp của định lý Pytago. Cứ lấy bình phương hai cạnh cộng lại, rồi trừ đi 2 lần tích của chúng nhân với cos góc xen giữa là ra.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính cạnh",
                        "problem": "Tam giác ABC có $b=3, c=4, A=60^\circ$. Tính cạnh $a$.",
                        "solution": "- $a^2 = 3^2 + 4^2 - 2(3)(4)\cos 60^\circ = 9 + 16 - 24(0.5) = 25 - 12 = 13$.\n- $a = \sqrt{13}$."
                    }
                ],
                "exercise": {"id": "10_6_1", "title": "Kiểm minh chứng", "content": "Tam giác có b=3, c=4, góc A=90 độ. Tính a^2.", "type": "NUMERIC", "target": "25", "options": []}
            },
            "II. Định lý sin và Công thức diện tích": {
                "theory": "Định lý Sin: Tỉ số giữa một cạnh và sin góc đối diện luôn bằng nhau và bằng đường kính ($2R$) đường tròn ngoại tiếp. Diện tích tam giác có thể tính bằng công thức Heron hoặc nửa tích 2 cạnh nhân sin góc xen giữa.",
                "formula": r"\frac{a}{\sin A} = \frac{b}{\sin B} = 2R; \quad S = \frac{1}{2}ab \sin C = \sqrt{p(p-a)(p-b)(p-c)}",
                "trap": "Trong công thức Heron, $p$ là NỬA chu vi ($p = (a+b+c)/2$). Rất nhiều bạn dùng chu vi để tính.",
                "audio": "Định lý Sin giúp ta tìm bán kính đường tròn ngoại tiếp. Còn để tính diện tích khi biết 3 cạnh, em hãy dùng công thức Heron với p là nửa chu vi nhé.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính bán kính R",
                        "problem": "Tam giác ABC có $a=10, A=30^\circ$. Tính bán kính đường tròn ngoại tiếp R.",
                        "solution": "- $\frac{a}{\sin A} = 2R \implies 2R = \frac{10}{\sin 30^\circ} = 20 \implies R = 10$."
                    },
                    {
                        "title": "Ví dụ 2: Tính diện tích góc xen giữa",
                        "problem": "Tam giác có 2 cạnh là 4 và 5, góc xen giữa $30^\circ$. Tính diện tích.",
                        "solution": "- $S = \frac{1}{2} \cdot 4 \cdot 5 \cdot \sin 30^\circ = 10 \cdot 0.5 = 5$."
                    }
                ],
                "exercise": {"id": "10_6_2", "title": "Kiểm minh chứng", "content": "Tam giác có 3 cạnh là 3, 4, 5. Diện tích bằng bao nhiêu?", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 7: Các khái niệm mở đầu về vectơ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "I. Khái niệm vectơ": {
                "theory": "Vectơ là một đoạn thẳng có hướng. Điểm đầu (gốc) và điểm cuối (ngọn) xác định hướng. Độ dài của vectơ chính là khoảng cách giữa điểm đầu và điểm cuối.",
                "formula": r"\vec{AB} \text{ (điểm đầu A, cuối B)}; \quad |\vec{AB}| = AB",
                "trap": "Ghi độ dài vectơ không có dấu trị tuyệt đối (ví dụ ghi $\vec{AB} = 5$ là sai, phải ghi $|\vec{AB}| = 5$).",
                "audio": "Vectơ đơn giản là một mũi tên chỉ đường, có điểm xuất phát, điểm kết thúc và độ dài cụ thể.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Đọc tên vectơ",
                        "problem": "Từ 2 điểm phân biệt A và B, có thể tạo ra bao nhiêu vectơ khác vectơ-không?",
                        "solution": "- Có 2 vectơ: $\vec{AB}$ (hướng từ A đến B) và $\vec{BA}$ (hướng từ B đến A)."
                    }
                ],
                "exercise": {"id": "10_7_1", "title": "Kiểm minh chứng", "content": "Tam giác đều ABC cạnh 2. Độ dài vectơ AB bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Hai vectơ cùng phương, cùng hướng, bằng nhau": {
                "theory": "Hai vectơ cùng phương nếu giá của chúng song song hoặc trùng nhau. Hai vectơ BẰNG NHAU khi chúng CÙNG HƯỚNG và CÙNG ĐỘ DÀI. Vectơ-không ($\vec{0}$) cùng phương, cùng hướng với mọi vectơ.",
                "formula": r"\vec{a} = \vec{b} \iff \vec{a} \uparrow\uparrow \vec{b} \text{ và } |\vec{a}| = |\vec{b}|",
                "trap": "Ngộ nhận hai vectơ bằng nhau khi chúng chỉ có độ dài bằng nhau và song song (chúng có thể ngược hướng).",
                "audio": "Để hai vectơ được coi là sinh đôi giống hệt nhau, chúng phải có cùng hướng đi và cùng chiều dài.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm vectơ bằng nhau",
                        "problem": "Hình bình hành ABCD. Vectơ nào bằng với $\vec{AB}$?",
                        "solution": "- Cạnh AB song song và bằng DC. Hướng từ A $\to$ B cùng hướng D $\to$ C.\n- Vậy $\vec{AB} = \vec{DC}$."
                    }
                ],
                "exercise": {"id": "10_7_2", "title": "Kiểm minh chứng", "content": "Trong hình bình hành ABCD, vectơ AB bằng vectơ CD. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 8: Tổng và hiệu của hai vectơ": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "I. Tổng của hai vectơ": {
                "theory": "Quy tắc 3 điểm (nối đuôi): $\vec{AB} + \vec{BC} = \vec{AC}$. Quy tắc hình bình hành (chung gốc): Nếu ABCD là hình bình hành thì tổng 2 cạnh bên bằng đường chéo $\vec{AB} + \vec{AD} = \vec{AC}$.",
                "formula": r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{AB} + \vec{AD} = \vec{AC}",
                "trap": "Cộng hai vectơ không nối đuôi nhau mà vẫn áp dụng quy tắc 3 điểm.",
                "audio": "Muốn cộng hai vectơ, em cứ ghép đuôi mũi tên này vào đầu mũi tên kia. Vectơ tổng sẽ nối từ điểm xuất phát đến điểm kết thúc cuối cùng.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức",
                        "problem": "Rút gọn biểu thức $\vec{MN} + \vec{NP} + \vec{PQ}$.",
                        "solution": "- Dùng quy tắc 3 điểm liên tiếp: $\vec{MN} + \vec{NP} = \vec{MP}$.\n- $\vec{MP} + \vec{PQ} = \vec{MQ}$."
                    }
                ],
                "exercise": {"id": "10_8_1", "title": "Kiểm minh chứng", "content": "Nếu ABCD là hình bình hành thì vectơ AB + AD = vectơ AE. E là điểm nào? (Nhập tên điểm)", "type": "STRING", "target": "C", "options": []}
            },
            "II. Hiệu của hai vectơ": {
                "theory": "Quy tắc trừ (chung gốc): $\vec{AB} - \vec{AC} = \vec{CB}$. (Lấy điểm ngọn của vectơ bị trừ làm gốc của kết quả). Hệ quả: Với I là trung điểm AB, $\vec{IA} + \vec{IB} = \vec{0}$.",
                "formula": r"\vec{AB} - \vec{AC} = \vec{CB}",
                "trap": "Học sinh thường trừ xuôi thành $\vec{BC}$. Nhớ kỹ phải TRỪ NGƯỢC LẠI thành $\vec{CB}$.",
                "audio": "Khi trừ hai vectơ chung gốc, điểm cuối của vectơ kết quả chính là điểm cuối của vectơ đứng trước. Nhớ đọc ngược lại từ sau ra trước nhé.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Phép trừ chung gốc",
                        "problem": "Rút gọn biểu thức $\vec{OB} - \vec{OA}$.",
                        "solution": "- Áp dụng đúng công thức trừ chung gốc: $\vec{OB} - \vec{OA} = \vec{AB}$."
                    },
                    {
                        "title": "Ví dụ 2: Tính độ dài",
                        "problem": "Tam giác đều ABC cạnh a. Tính $|\vec{AB} - \vec{AC}|$.",
                        "solution": "- Ta có $\vec{AB} - \vec{AC} = \vec{CB}$.\n- Độ dài $|\vec{CB}| = CB = a$."
                    }
                ],
                "exercise": {"id": "10_8_2", "title": "Kiểm minh chứng", "content": "Rút gọn MN - MP được vectơ QN. Q là điểm nào?", "type": "STRING", "target": "P", "options": []}
            }
        }
    },
    "Bài 9: Tích của một vectơ với một số": {
        "chapter": "Chương IV: Vectơ",
        "topics": {
            "I. Khái niệm và tính chất": {
                "theory": "Tích của số $k$ và vectơ $\vec{a}$ là một VECTƠ. Cùng hướng nếu $k > 0$, ngược hướng nếu $k < 0$. Độ dài thay đổi gấp $|k|$ lần. Hệ thức trung điểm: $I$ là trung điểm $AB$, $M$ bất kỳ $\implies \vec{MA} + \vec{MB} = 2\vec{MI}$.",
                "formula": r"|k\vec{a}| = |k| \cdot |\vec{a}|; \quad \vec{MA} + \vec{MB} = 2\vec{MI}",
                "trap": "Tính độ dài quên lấy trị tuyệt đối của số $k$. Ví dụ $|-3\vec{a}|$ phải bằng $3|\vec{a}|$, không phải $-3|\vec{a}|$.",
                "audio": "Nhân một số với một vectơ sẽ tạo ra một vectơ mới, dài ra hoặc ngắn đi. Nếu nhân số âm, mũi tên sẽ bị quay ngược lại 180 độ.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính độ dài",
                        "problem": "Vectơ $\vec{a}$ có độ dài 5. Tính độ dài của $-2\vec{a}$.",
                        "solution": "- $|-2\vec{a}| = |-2| \cdot |\vec{a}| = 2 \cdot 5 = 10$."
                    }
                ],
                "exercise": {"id": "10_9_1", "title": "Kiểm minh chứng", "content": "G là trọng tâm tam giác ABC, M bất kỳ. Tổng MA + MB + MC = c.MG. Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "II. Điều kiện để hai vectơ cùng phương": {
                "theory": "Hai vectơ $\vec{a}$ và $\vec{b}$ ($\vec{b} \neq \vec{0}$) cùng phương khi và chỉ khi TỒN TẠI số $k$ sao cho $\vec{a} = k\vec{b}$. Để chứng minh 3 điểm A, B, C thẳng hàng, ta chứng minh $\vec{AB} = k\vec{AC}$.",
                "formula": r"\vec{a} \parallel \vec{b} \iff \vec{a} = k\vec{b}; \quad A, B, C \text{ thẳng hàng} \iff \vec{AB} = k\vec{AC}",
                "trap": "Chứng minh 3 điểm thẳng hàng bằng cách chỉ ra $\vec{AB}$ cùng phương $\vec{CD}$ là sai, phải dùng 2 vectơ có CHUNG 1 điểm xuất phát.",
                "audio": "Để chứng minh ba điểm thẳng hàng bằng vectơ, em hãy chứng minh vectơ tạo bởi hai điểm này bằng k lần vectơ tạo bởi hai điểm kia.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chứng minh thẳng hàng",
                        "problem": "Cho $\vec{AB} = 2\vec{a}$ và $\vec{AC} = -4\vec{a}$. 3 điểm A, B, C có thẳng hàng không?",
                        "solution": "- Ta thấy $\vec{AC} = -2(2\vec{a}) = -2\vec{AB}$.\n- Hai vectơ có chung điểm A và tỉ lệ nhau, nên A, B, C thẳng hàng."
                    }
                ],
                "exercise": {"id": "10_9_2", "title": "Kiểm minh chứng", "content": "Nếu vectơ x = 4 vectơ y thì hai vectơ này có cùng hướng không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE10.PY - HỌC LIỆU TOÁN 10 KẾT NỐI TRI THỨC (PHẦN 2: BÀI 15 -> BÀI 27)
# ==============================================================================

GRADE_10_DATA.update({
    "Bài 15: Hàm số và đồ thị": {
        "chapter": "Chương VI: Hàm số, đồ thị và ứng dụng",
        "topics": {
            "I. Khái niệm hàm số và Tập xác định": {
                "theory": "Hàm số $y = f(x)$ xác định trên $D$ là quy tắc đặt tương ứng mỗi $x \in D$ với duy nhất một giá trị $y \in \mathbb{R}$. Điều kiện xác định thường gặp: Mẫu số khác 0, biểu thức dưới căn bậc hai không âm.",
                "formula": r"\frac{A}{B} \implies B \neq 0; \quad \sqrt{A} \implies A \ge 0",
                "trap": "Căn thức nằm ở mẫu số (dạng $\frac{1}{\sqrt{A}}$) thì điều kiện phải là $A > 0$, không được lấy dấu bằng.",
                "audio": "Tìm tập xác định hàm số cần nhớ hai điều kiện cốt lõi: mẫu số phải khác không và biểu thức dưới căn bậc chẵn phải không âm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tập xác định chứa căn và mẫu",
                        "problem": "Tìm tập xác định của hàm số $y = \frac{\sqrt{x - 1}}{x - 3}$.",
                        "solution": "- Điều kiện: $\begin{cases} x - 1 \ge 0 \\ x - 3 \neq 0 \end{cases} \iff \begin{cases} x \ge 1 \\ x \neq 3 \end{cases}$.\n- Vậy tập xác định là $D = [1; +\infty) \setminus \{3\}$."
                    }
                ],
                "exercise": {"id": "10_15_1", "title": "Kiểm minh chứng", "content": "Tập xác định của y = 1/căn(x - 2) có dạng (c; +vô cực). c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Sự đồng biến, nghịch biến của hàm số": {
                "theory": "Hàm số đồng biến trên $K$ nếu $x_1 < x_2 \implies f(x_1) < f(x_2)$ (đồ thị đi lên từ trái sang phải). Hàm số nghịch biến trên $K$ nếu $x_1 < x_2 \implies f(x_1) > f(x_2)$ (đồ thị đi xuống từ trái sang phải).",
                "formula": r"\frac{f(x_2) - f(x_1)}{x_2 - x_1} > 0 \implies \text{Đồng biến}; \quad \frac{f(x_2) - f(x_1)}{x_2 - x_1} < 0 \implies \text{Nghịch biến}",
                "trap": "Khi đọc khoảng đơn điệu từ đồ thị, mắt phải quét từ TRÁI sang PHẢI theo chiều tăng của trục hoành $Ox$.",
                "audio": "Nhìn đồ thị từ trái sang phải, đoạn nào dốc lên là hàm số đồng biến, đoạn nào dốc xuống là hàm số nghịch biến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét tính đơn điệu bằng định nghĩa",
                        "problem": "Xét tính đơn điệu của hàm số $y = f(x) = -2x + 3$ trên $\mathbb{R}$.",
                        "solution": "- Với $x_1 < x_2 \implies x_1 - x_2 < 0$.\n- Tỉ số: $\frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{(-2x_2 + 3) - (-2x_1 + 3)}{x_2 - x_1} = -2 < 0$.\n- Vậy hàm số luôn nghịch biến trên $\mathbb{R}$."
                    }
                ],
                "exercise": {"id": "10_15_2", "title": "Kiểm minh chứng", "content": "Hàm số y = 3x - 1 là hàm số đồng biến (1) hay nghịch biến (0) trên R?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 16: Hàm số bậc hai": {
        "chapter": "Chương VI: Hàm số, đồ thị và ứng dụng",
        "topics": {
            "I. Đồ thị hàm số bậc hai (Parabol)": {
                "theory": "Đồ thị hàm số $y = ax^2 + bx + c$ ($a \neq 0$) là parabol có đỉnh $I\left(-\frac{b}{2a}; -\frac{\Delta}{4a}\right)$, trục đối xứng là đường thẳng $x = -\frac{b}{2a}$. Bề lõm quay lên nếu $a > 0$, quay xuống nếu $a < 0$.",
                "formula": r"x_I = -\frac{b}{2a}; \quad y_I = f(x_I)",
                "trap": "Học sinh hay nhầm hoành độ đỉnh parabol thành $\frac{b}{2a}$ (quên dấu trừ).",
                "audio": "Đỉnh của parabol có hoành độ bằng trừ b trên 2a. Tung độ đỉnh em chỉ việc lấy hoành độ thay ngược vào hàm số ban đầu.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tọa độ đỉnh parabol",
                        "problem": "Tìm tọa độ đỉnh $I$ của parabol $(P): y = x^2 - 4x + 3$.",
                        "solution": "- Hoành độ đỉnh: $x_I = -\frac{-4}{2 \cdot 1} = 2$.\n- Tung độ đỉnh: $y_I = 2^2 - 4(2) + 3 = -1$.\n- Vậy đỉnh parabol là $I(2; -1)$."
                    }
                ],
                "exercise": {"id": "10_16_1", "title": "Kiểm minh chứng", "content": "Hoành độ đỉnh của parabol y = 2x^2 - 8x + 1 bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "II. Sự biến thiên và Giá trị lớn nhất, nhỏ nhất": {
                "theory": "Nếu $a > 0$: Hàm số nghịch biến trên $(-\infty; -b/2a)$ và đồng biến trên $(-b/2a; +\infty)$, đạt GTNN tại đỉnh. Nếu $a < 0$: Hàm số đồng biến trên $(-\infty; -b/2a)$ và nghịch biến trên $(-b/2a; +\infty)$, đạt GTLN tại đỉnh.",
                "formula": r"a > 0 \implies y_{\min} = f\left(-\frac{b}{2a}\right); \quad a < 0 \implies y_{\max} = f\left(-\frac{b}{2a}\right)",
                "trap": "Bảng biến thiên có mũi tên phụ thuộc vào dấu của $a$. Nhầm dấu $a$ sẽ đảo ngược hoàn toàn khoảng đồng biến, nghịch biến.",
                "audio": "Khi a dương parabol ngửa lên trên nên đạt giá trị nhỏ nhất tại đáy. Khi a âm parabol úp xuống nên đạt giá trị lớn nhất tại đỉnh.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giá trị nhỏ nhất của hàm bậc hai",
                        "problem": "Tìm giá trị nhỏ nhất của $y = x^2 - 6x + 11$.",
                        "solution": "- Vì $a = 1 > 0$ nên hàm số đạt GTNN tại đỉnh $x = -\frac{-6}{2} = 3$.\n- $y_{\min} = y(3) = 3^2 - 6(3) + 11 = 2$."
                    }
                ],
                "exercise": {"id": "10_16_2", "title": "Kiểm minh chứng", "content": "Giá trị lớn nhất của hàm số y = -x^2 + 4x - 1 bằng bao nhiêu?", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 17: Dấu của tam thức bậc hai": {
        "chapter": "Chương VI: Hàm số, đồ thị và ứng dụng",
        "topics": {
            "I. Định lý về dấu của tam thức bậc hai": {
                "theory": "Cho $f(x) = ax^2 + bx + c$ ($a \neq 0$). Nếu $\Delta < 0$, $f(x)$ cùng dấu với $a$ với mọi $x \in \mathbb{R}$. Nếu $\Delta = 0$, $f(x)$ cùng dấu với $a$ với mọi $x \neq -b/2a$. Nếu $\Delta > 0$, $f(x)$ có hai nghiệm $x_1 < x_2$ và tuân theo quy tắc: Trong trái dấu với a, ngoài cùng dấu với a.",
                "formula": r"\Delta < 0 \implies a \cdot f(x) > 0, \forall x \in \mathbb{R}",
                "trap": "Quy tắc 'Trong trái, ngoài cùng' chỉ áp dụng khi tam thức có 2 nghiệm phân biệt ($\Delta > 0$). Khi $\Delta < 0$ thì tam thức luôn cùng dấu với $a$.",
                "audio": "Quy tắc cốt lõi: Delta âm thì tam thức cùng dấu với a trên toàn trục số. Delta dương thì trong khoảng hai nghiệm trái dấu với a, ngoài khoảng hai nghiệm cùng dấu với a.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét dấu tam thức có 2 nghiệm phân biệt",
                        "problem": "Xét dấu của tam thức bậc hai $f(x) = x^2 - 4x + 3$.",
                        "solution": "- Phương trình $f(x) = 0$ có 2 nghiệm $x_1 = 1, x_2 = 3$.\n- Hệ số $a = 1 > 0$.\n- Trong khoảng $(1; 3)$: $f(x) < 0$ (trái dấu a).\n- Ngoài khoảng $(-\infty; 1)$ và $(3; +\infty)$: $f(x) > 0$ (cùng dấu a)."
                    }
                ],
                "exercise": {"id": "10_17_1", "title": "Kiểm minh chứng", "content": "Tam thức f(x) = x^2 - 5x + 6 mang dấu âm trên khoảng (2; c). Giá trị c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "II. Bất phương trình bậc hai một ẩn": {
                "theory": "Giải bất phương trình bậc hai $ax^2 + bx + c > 0$ (hoặc $\ge, <, \le$) là tìm các khoảng mà tại đó tam thức bậc hai mang dấu phù hợp với chiều của bất phương trình.",
                "formula": r"f(x) \ge 0 \implies \text{Lấy các khoảng mang dấu (+) kèm nghiệm f(x)=0}",
                "trap": "Khi bất phương trình có dấu bằng ($\le, \ge$), phải lấy ngoặc vuông `[]` tại các nghiệm của tam thức.",
                "audio": "Giải bất phương trình bậc hai bằng cách tìm nghiệm, vẽ trục xét dấu trong trái ngoài cùng rồi lấy đúng khoảng nghiệm theo yêu cầu đề bài.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải bất phương trình bậc hai",
                        "problem": "Giải bất phương trình $x^2 - 3x - 4 \le 0$.",
                        "solution": "- Tam thức có 2 nghiệm $x_1 = -1, x_2 = 4$; hệ số $a = 1 > 0$.\n- Dấu âm nằm bên trong hai nghiệm.\n- Vậy tập nghiệm là đoạn $[-1; 4]$."
                    }
                ],
                "exercise": {"id": "10_17_2", "title": "Kiểm minh chứng", "content": "Tập nghiệm của x^2 - 4 < 0 là khoảng (-2; c). Giá trị c bằng:", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 18: Phương trình quy về phương trình bậc hai": {
        "chapter": "Chương VI: Hàm số, đồ thị và ứng dụng",
        "topics": {
            "I. Phương trình dạng căn f(x) = căn g(x)": {
                "theory": "Để giải phương trình $\sqrt{f(x)} = \sqrt{g(x)}$, ta bình phương hai vế đưa về $f(x) = g(x)$ rồi giải. Sau đó bắt buộc phải thay nghiệm tìm được vào kiểm tra xem biểu thức trong căn có $\ge 0$ hay không.",
                "formula": r"\sqrt{f(x)} = \sqrt{g(x)} \implies f(x) = g(x) \quad (\text{Thử lại nghiệm})",
                "trap": "Bình phương hai vế là phép biến đổi hệ quả nên có thể sinh ra nghiệm ngoại lai. Phải thử lại nghiệm hoặc đặt điều kiện $f(x) \ge 0$.",
                "audio": "Dạng căn bằng căn chỉ cần bình phương hai vế cho mất căn rồi giải phương trình đại số bình thường, sau đó thử lại nghiệm vào đề bài.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình hai căn bậc hai",
                        "problem": "Giải phương trình $\sqrt{2x + 3} = \sqrt{x + 5}$.",
                        "solution": "- Bình phương hai vế: $2x + 3 = x + 5 \iff x = 2$.\n- Thử lại: Với $x = 2$, $\sqrt{7} = \sqrt{7}$ (thỏa mãn).\n- Vậy phương trình có nghiệm duy nhất $x = 2$."
                    }
                ],
                "exercise": {"id": "10_18_1", "title": "Kiểm minh chứng", "content": "Nghiệm của phương trình căn(3x - 1) = căn(2x + 4) là x bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "II. Phương trình dạng căn f(x) = g(x)": {
                "theory": "Phương trình $\sqrt{f(x)} = g(x)$ tương đương với hệ: $g(x) \ge 0$ và $f(x) = [g(x)]^2$. Điều kiện $g(x) \ge 0$ là bắt buộc trước khi bình phương hai vế.",
                "formula": r"\sqrt{f(x)} = g(x) \iff \begin{cases} g(x) \ge 0 \\ f(x) = [g(x)]^2 \end{cases}",
                "trap": "Quên đặt điều kiện $g(x) \ge 0$ dẫn đến việc nhận nhầm nghiệm ngoại lai làm vế phải âm (vô lý vì căn bậc hai luôn không âm).",
                "audio": "Căn bằng một đa thức thì điều kiện sống còn là đa thức vế phải phải lớn hơn hoặc bằng không rồi mới được bình phương hai vế.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Giải phương trình căn bằng đa thức",
                        "problem": "Giải phương trình $\sqrt{x^2 - 2x - 3} = x - 1$.",
                        "solution": "- Điều kiện vế phải: $x - 1 \ge 0 \iff x \ge 1$.\n- Bình phương hai vế: $x^2 - 2x - 3 = (x - 1)^2 \iff x^2 - 2x - 3 = x^2 - 2x + 1$.\n- Suy ra $-3 = 1$ (vô lý). Phương trình vô nghiệm."
                    }
                ],
                "exercise": {"id": "10_18_2", "title": "Kiểm minh chứng", "content": "Số nghiệm của phương trình căn(x + 1) = -2 là bao nhiêu?", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 19: Phương trình đường thẳng": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "I. Vectơ chỉ phương và Vectơ pháp tuyến": {
                "theory": "Vectơ chỉ phương $\vec{u} \neq \vec{0}$ có giá song song hoặc trùng với đường thẳng. Vectơ pháp tuyến $\vec{n} \neq \vec{0}$ có giá vuông góc với đường thẳng. Nếu $\vec{n} = (A; B)$ thì một VTCP là $\vec{u} = (-B; A)$.",
                "formula": r"\vec{n} = (A; B) \iff \vec{u} = (-B; A); \quad \vec{n} \cdot \vec{u} = 0",
                "trap": "Đổi từ VTPT sang VTCP quên đổi dấu một tọa độ (ví dụ $(2; 3)$ đổi thành $(3; 2)$ thay vì $(-3; 2)$).",
                "audio": "Pháp tuyến thì vuông góc, chỉ phương thì song song. Muốn đổi từ pháp tuyến sang chỉ phương ta đảo vị trí hai số và thêm một dấu trừ.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chuyển đổi giữa hai loại vectơ",
                        "problem": "Đường thẳng $\Delta$ có VTPT $\vec{n} = (2; -5)$. Tìm một VTCP của $\Delta$.",
                        "solution": "- Đảo vị trí và đổi dấu một tọa độ: $\vec{u} = (5; 2)$."
                    }
                ],
                "exercise": {"id": "10_19_1", "title": "Kiểm minh chứng", "content": "Đường thẳng có VTPT n = (3; 4) thì một VTCP u = (-4; b). b bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "II. Phương trình tổng quát và Phương trình tham số": {
                "theory": "Phương trình tổng quát qua $M_0(x_0; y_0)$ có VTPT $\vec{n}=(A; B)$ là $Ax + By + C = 0$. Phương trình tham số qua $M_0(x_0; y_0)$ có VTCP $\vec{u}=(u_1; u_2)$ là $\begin{cases} x = x_0 + u_1 t \\ y = y_0 + u_2 t \end{cases}$.",
                "formula": r"A(x - x_0) + B(y - y_0) = 0 \iff Ax + By + C = 0",
                "trap": "Học sinh thường nhầm vị trí tọa độ điểm đi qua và tọa độ vectơ khi viết phương trình tham số.",
                "audio": "Phương trình tổng quát gắn liền với vectơ pháp tuyến, phương trình tham số gắn liền với vectơ chỉ phương và tham số t.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập phương trình tổng quát",
                        "problem": "Lập PTTQ của đường thẳng đi qua $A(1; -2)$ và có VTPT $\vec{n} = (3; 2)$.",
                        "solution": "- Phương trình: $3(x - 1) + 2(y - (-2)) = 0 \iff 3x + 2y + 1 = 0$."
                    }
                ],
                "exercise": {"id": "10_19_2", "title": "Kiểm minh chứng", "content": "Đường thẳng x = 1 + 2t; y = 3 - t đi qua điểm M(1; c). c bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 20: Vị trí tương đối giữa hai đường thẳng. Góc và khoảng cách": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "I. Vị trí tương đối và Góc giữa hai đường thẳng": {
                "theory": "Vị trí tương đối giữa $\Delta_1$ và $\Delta_2$ xác định bằng số nghiệm của hệ phương trình tọa độ. Cosin của góc giữa hai đường thẳng bằng trị tuyệt đối cosin của góc giữa hai VTPT.",
                "formula": r"\cos(\Delta_1, \Delta_2) = \frac{|\vec{n_1} \cdot \vec{n_2}|}{|\vec{n_1}| \cdot |\vec{n_2}|}",
                "trap": "Góc giữa hai đường thẳng luôn thuộc $[0^\circ; 90^\circ]$ nên tử số bắt buộc phải có dấu giá trị tuyệt đối.",
                "audio": "Góc giữa hai đường thẳng không bao giờ là góc tù nên công thức cosin luôn có trị tuyệt đối ở tử số.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa hai đường thẳng",
                        "problem": "Tính góc giữa $\Delta_1: x - 2y + 1 = 0$ và $\Delta_2: 2x + y - 5 = 0$.",
                        "solution": "- $\vec{n_1} = (1; -2), \vec{n_2} = (2; 1)$.\n- Tích vô hướng: $\vec{n_1} \cdot \vec{n_2} = 1(2) + (-2)(1) = 0$.\n- Vì tích vô hướng bằng 0 nên góc giữa hai đường thẳng bằng $90^\circ$."
                    }
                ],
                "exercise": {"id": "10_20_1", "title": "Kiểm minh chứng", "content": "Hai đường thẳng vuông góc tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "II. Khoảng cách từ một điểm đến đường thẳng": {
                "theory": "Khoảng cách từ điểm $M_0(x_0; y_0)$ đến đường thẳng $\Delta: Ax + By + C = 0$ bằng trị tuyệt đối khi thay tọa độ điểm vào vế trái chia cho độ dài VTPT.",
                "formula": r"d(M_0, \Delta) = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
                "trap": "Học sinh thường quên căn bậc hai $\sqrt{A^2 + B^2}$ ở mẫu số.",
                "audio": "Tính khoảng cách từ điểm đến đường thẳng: thay tọa độ điểm vào tử số lấy trị tuyệt đối, mẫu số là độ dài vectơ pháp tuyến.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách từ điểm",
                        "problem": "Tính khoảng cách từ $A(2; -1)$ đến $\Delta: 3x - 4y + 5 = 0$.",
                        "solution": "- $d(A, \Delta) = \frac{|3(2) - 4(-1) + 5|}{\sqrt{3^2 + (-4)^2}} = \frac{|6 + 4 + 5|}{5} = \frac{15}{5} = 3$."
                    }
                ],
                "exercise": {"id": "10_20_2", "title": "Kiểm minh chứng", "content": "Khoảng cách từ O(0; 0) đến đường thẳng 3x + 4y - 15 = 0 bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 21: Đường tròn trong mặt phẳng tọa độ": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "I. Phương trình đường tròn": {
                "theory": "Phương trình chính tắc tâm $I(a; b)$ bán kính $R$ là $(x - a)^2 + (y - b)^2 = R^2$. Phương trình khai triển $x^2 + y^2 - 2ax - 2by + c = 0$ là đường tròn khi và chỉ khi $a^2 + b^2 - c > 0$ với $R = \sqrt{a^2 + b^2 - c}$.",
                "formula": r"(x - a)^2 + (y - b)^2 = R^2; \quad R = \sqrt{a^2 + b^2 - c}",
                "trap": "Khi đọc tọa độ tâm từ dạng khai triển, phải lấy hệ số của x và y chia cho -2.",
                "audio": "Phương trình đường tròn dạng chính tắc giúp đọc ngay tâm và bán kính. Với dạng khai triển nhớ chia hệ số x, y cho trừ 2 để tìm tâm.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tâm và bán kính từ dạng khai triển",
                        "problem": "Tìm tâm $I$ và bán kính $R$ của $(C): x^2 + y^2 - 6x + 2y - 6 = 0$.",
                        "solution": "- $a = -6/(-2) = 3; b = 2/(-2) = -1; c = -6$.\n- Tâm $I(3; -1)$. Bán kính $R = \sqrt{3^2 + (-1)^2 - (-6)} = \sqrt{9 + 1 + 6} = 4$."
                    }
                ],
                "exercise": {"id": "10_21_1", "title": "Kiểm minh chứng", "content": "Đường tròn (x - 2)^2 + (y + 1)^2 = 16 có bán kính R bằng:", "type": "NUMERIC", "target": "4", "options": []}
            },
            "II. Phương trình tiếp tuyến của đường tròn": {
                "theory": "Tiếp tuyến của $(C)$ tại điểm $M_0(x_0; y_0) \in (C)$ nhận vectơ $\vec{IM_0}$ làm vectơ pháp tuyến.",
                "formula": r"(x_0 - a)(x - x_0) + (y_0 - b)(y - y_0) = 0",
                "trap": "Tiếp tuyến TẠI một điểm trên đường tròn khác với tiếp tuyến KẺ TỪ một điểm bên ngoài đường tròn.",
                "audio": "Tiếp tuyến tại một điểm trên đường tròn luôn vuông góc với bán kính đi qua tiếp điểm đó.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết phương trình tiếp tuyến tại tiếp điểm",
                        "problem": "Viết PTTT của $(C): (x - 1)^2 + (y - 2)^2 = 25$ tại điểm $M(4; 6)$.",
                        "solution": "- Tâm $I(1; 2)$. Vectơ pháp tuyến $\vec{IM} = (3; 4)$.\n- Phương trình tiếp tuyến: $3(x - 4) + 4(y - 6) = 0 \iff 3x + 4y - 36 = 0$."
                    }
                ],
                "exercise": {"id": "10_21_2", "title": "Kiểm minh chứng", "content": "Khoảng cách từ tâm đường tròn đến tiếp tuyến bằng bán kính R. Đúng (1) hay Sai (0)?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 22: Ba đường conic": {
        "chapter": "Chương VII: Phương pháp tọa độ trong mặt phẳng",
        "topics": {
            "I. Đường Elip": {
                "theory": "Phương trình chính tắc của elip là $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$). Hai tiêu điểm $F_1(-c; 0), F_2(c; 0)$ với $c^2 = a^2 - b^2$. Độ dài trục lớn $2a$, trục nhỏ $2b$, tiêu cự $2c$.",
                "formula": r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a^2 = b^2 + c^2)",
                "trap": "Học sinh hay nhầm hệ thức elip $a^2 = b^2 + c^2$ với định lý Pytago.",
                "audio": "Trong elip, a là đại lượng lớn nhất: a bình bằng b bình cộng c bình. Trục lớn là 2a và tiêu cự là 2c.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định các yếu tố của Elip",
                        "problem": "Tìm độ dài trục lớn và tiêu cự của Elip $(E): \frac{x^2}{16} + \frac{y^2}{7} = 1$.",
                        "solution": "- $a^2 = 16 \implies a = 4$. Độ dài trục lớn $2a = 8$.\n- $b^2 = 7 \implies c^2 = a^2 - b^2 = 16 - 7 = 9 \implies c = 3$. Tiêu cự $2c = 6$."
                    }
                ],
                "exercise": {"id": "10_22_1", "title": "Kiểm minh chứng", "content": "Elip x^2/25 + y^2/16 = 1 có độ dài trục lớn 2a bằng:", "type": "NUMERIC", "target": "10", "options": []}
            },
            "II. Đường Hypebol và Parabol": {
                "theory": "Hypebol có PTCT $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ với $c^2 = a^2 + b^2$. Parabol có PTCT $y^2 = 2px$ ($p > 0$) với tiêu điểm $F(p/2; 0)$ và đường chuẩn $x = -p/2$.",
                "formula": r"\text{Hypebol: } c^2 = a^2 + b^2; \quad \text{Parabol: } y^2 = 2px",
                "trap": "Hypebol phương trình có dấu TRỪ giữa hai phân thức, liên hệ $c^2 = a^2 + b^2$ lại có dấu CỘNG.",
                "audio": "Hypebol phương trình mang dấu trừ, liên hệ c bình bằng a bình cộng b bình. Parabol có phương trình chính tắc y bình bằng 2 p x.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tham số tiêu của Parabol",
                        "problem": "Tìm tiêu điểm của parabol $(P): y^2 = 8x$.",
                        "solution": "- Ta có $2p = 8 \implies p = 4$.\n- Tiêu điểm $F(p/2; 0) = F(2; 0)$."
                    }
                ],
                "exercise": {"id": "10_22_2", "title": "Kiểm minh chứng", "content": "Parabol y^2 = 4x có tham số tiêu p bằng bao nhiêu?", "type": "NUMERIC", "target": "2", "options": []}
            }
        }
    },
    "Bài 23: Quy tắc đếm": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "I. Quy tắc cộng và Sơ đồ cây": {
                "theory": "Một công việc được hoàn thành bởi một trong hai hành động không giao nhau: hành động 1 có $m$ cách, hành động 2 có $n$ cách $\implies$ Có $m + n$ cách hoàn thành công việc. Sơ đồ cây giúp biểu diễn trực quan các phương án.",
                "formula": r"N = m + n",
                "trap": "Chỉ dùng quy tắc cộng khi các phương án độc lập và tách rời nhau (không có phần tử trùng lặp).",
                "audio": "Làm cách này HOẶC làm cách kia thì ta dùng quy tắc cộng. Công việc xong ngay trong từng phương án.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Áp dụng quy tắc cộng",
                        "problem": "Một kệ sách có 5 cuốn sách Toán và 7 cuốn sách Văn. Có bao nhiêu cách chọn 1 cuốn sách?",
                        "solution": "- Chọn 1 cuốn Toán (5 cách) hoặc 1 cuốn Văn (7 cách).\n- Số cách chọn là: $5 + 7 = 12$ cách."
                    }
                ],
                "exercise": {"id": "10_23_1", "title": "Kiểm minh chứng", "content": "Có 4 quả táo và 6 quả cam. Số cách chọn 1 quả trái cây là:", "type": "NUMERIC", "target": "10", "options": []}
            },
            "II. Quy tắc nhân": {
                "theory": "Một công việc gồm hai công đoạn liên tiếp: công đoạn 1 có $m$ cách, với mỗi cách đó công đoạn 2 có $n$ cách $\implies$ Có $m \cdot n$ cách hoàn thành công việc.",
                "formula": r"N = m \cdot n",
                "trap": "Học sinh hay nhầm lẫn giữa quy tắc cộng và quy tắc nhân. Cứ nhớ: Muốn xong việc phải làm bước 1 VÀ bước 2 thì dùng phép nhân.",
                "audio": "Phải trải qua nhiều công đoạn liên tiếp mới xong công việc thì ta nhân số cách của từng công đoạn lại với nhau.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập số tự nhiên bằng quy tắc nhân",
                        "problem": "Từ các chữ số {1, 2, 3, 4} có thể lập được bao nhiêu số tự nhiên có 2 chữ số khác nhau?",
                        "solution": "- Chọn chữ số hàng chục: 4 cách.\n- Chọn chữ số hàng đơn vị (khác hàng chục): 3 cách.\n- Số các số lập được: $4 \cdot 3 = 12$ số."
                    }
                ],
                "exercise": {"id": "10_23_2", "title": "Kiểm minh chứng", "content": "Đi từ A đến B có 3 đường, từ B đến C có 4 đường. Số đường đi từ A qua B đến C là:", "type": "NUMERIC", "target": "12", "options": []}
            }
        }
    },
    "Bài 24: Hoán vị, chỉnh hợp và tổ hợp": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "I. Hoán vị và Chỉnh hợp": {
                "theory": "Hoán vị $n$ phần tử: $P_n = n!$. Chỉnh hợp chập $k$ của $n$: Chọn $k$ phần tử từ $n$ phần tử VÀ SẮP THỨ TỰ chúng.",
                "formula": r"P_n = n!; \quad A_n^k = \frac{n!}{(n - k)!}",
                "trap": "Cứ bài toán có yếu tố 'xếp hàng', 'phân chức vụ', 'lập số' (thay đổi thứ tự tạo ra kết quả mới) là dùng chỉnh hợp.",
                "audio": "Chọn phần tử mà có sắp xếp vị trí trước sau thì dùng chỉnh hợp A. Đổi chỗ toàn bộ n phần tử thì dùng hoán vị n giai thừa.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bài toán xếp chỗ ngồi (Hoán vị)",
                        "problem": "Có bao nhiêu cách xếp 5 bạn học sinh vào một bàn dài có 5 ghế?",
                        "solution": "- Số cách xếp chính là số hoán vị của 5 phần tử: $P_5 = 5! = 120$ cách."
                    },
                    {
                        "title": "Ví dụ 2: Bầu ban cán sự (Chỉnh hợp)",
                        "problem": "Một tổ có 10 học sinh. Cần bầu ra 1 lớp trưởng và 1 lớp phó. Có bao nhiêu cách?",
                        "solution": "- Chọn 2 bạn và phân công 2 chức vụ (có thứ tự): $A_{10}^2 = \frac{10!}{8!} = 10 \cdot 9 = 90$ cách."
                    }
                ],
                "exercise": {"id": "10_24_1", "title": "Kiểm minh chứng", "content": "Giá trị của P_4 (4 giai thừa) bằng bao nhiêu?", "type": "NUMERIC", "target": "24", "options": []}
            },
            "II. Tổ hợp": {
                "theory": "Tổ hợp chập $k$ của $n$ phần tử: Chọn $k$ phần tử từ $n$ phần tử KHÔNG QUAN TÂM THỨ TỰ. Tính chất: $C_n^k = C_n^{n-k}$.",
                "formula": r"C_n^k = \frac{n!}{k!(n - k)!}",
                "trap": "Nhầm lẫn giữa Tổ hợp ($C$) và Chỉnh hợp ($A$). Không phân biệt thứ tự (chọn nhóm, chọn đội) thì dùng $C$.",
                "audio": "Chọn một nhóm người hay bốc một vốc bi mà không phân biệt ai trước ai sau thì dùng tổ hợp C.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Chọn đội tuyển",
                        "problem": "Một lớp có 30 học sinh. Có bao nhiêu cách chọn ra một nhóm 3 học sinh đi thi đua?",
                        "solution": "- Chọn 3 học sinh không xếp thứ tự: $C_{30}^3 = \frac{30 \cdot 29 \cdot 28}{3 \cdot 2 \cdot 1} = 4060$ cách."
                    }
                ],
                "exercise": {"id": "10_24_2", "title": "Kiểm minh chứng", "content": "Giá trị của tổ hợp C_5^2 bằng:", "type": "NUMERIC", "target": "10", "options": []}
            }
        }
    },
    "Bài 25: Nhị thức Newton": {
        "chapter": "Chương VIII: Đại số tổ hợp",
        "topics": {
            "I. Khai triển nhị thức Newton bậc 4 và bậc 5": {
                "theory": "Khai triển $(a + b)^4$ có 5 số hạng và $(a + b)^5$ có 6 số hạng. Hệ số đối xứng qua trung tâm, tính bằng các tổ hợp $C_n^k$.",
                "formula": r"(a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4",
                "trap": "Khi khai triển biểu thức có dấu trừ như $(a - b)^n$, dấu của các số hạng xen kẽ nhau: cộng rồi trừ.",
                "audio": "Nhị thức Newton bậc 4 và 5 có công thức hệ số đối xứng. Khi khai triển có dấu trừ, nhớ đan xen dấu cộng trừ liên tiếp nhé.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Khai triển nhị thức bậc 4",
                        "problem": "Khai triển biểu thức $(x + 2)^4$.",
                        "solution": "- Áp dụng: $(x + 2)^4 = x^4 + 4x^3(2) + 6x^2(2^2) + 4x(2^3) + 2^4$.\n- Rút gọn: $x^4 + 8x^3 + 24x^2 + 32x + 16$."
                    }
                ],
                "exercise": {"id": "10_25_1", "title": "Kiểm minh chứng", "content": "Số hạng tự do (không chứa x) trong khai triển (x + 2)^4 bằng:", "type": "NUMERIC", "target": "16", "options": []}
            }
        }
    },
    "Bài 26: Biến cố và định nghĩa cổ điển của xác suất": {
        "chapter": "Chương IX: Một số yếu tố xác suất",
        "topics": {
            "I. Không gian mẫu và Biến cố": {
                "theory": "Phép thử ngẫu nhiên là phép thử không đoán trước được kết quả. Không gian mẫu $\Omega$ là tập hợp mọi kết quả có thể xảy ra. Biến cố $A$ là tập con của không gian mẫu.",
                "formula": r"A \subset \Omega",
                "trap": "Xác định thiếu phần tử của không gian mẫu dẫn đến tính sai xác suất ở mẫu số.",
                "audio": "Không gian mẫu là tất cả các kết quả có thể xảy ra. Biến cố là những kết quả thỏa mãn điều kiện bài toán yêu cầu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định không gian mẫu",
                        "problem": "Gieo một đồng xu cân đối 2 lần liên tiếp. Liệt kê không gian mẫu.",
                        "solution": "- $\Omega = \{SS, SN, NS, NN\}$. Có 4 phần tử: $n(\Omega) = 4$."
                    }
                ],
                "exercise": {"id": "10_26_1", "title": "Kiểm minh chứng", "content": "Gieo một con xúc xắc 6 mặt cân đối. Số phần tử của không gian mẫu bằng:", "type": "NUMERIC", "target": "6", "options": []}
            },
            "II. Định nghĩa cổ điển của xác suất": {
                "theory": "Xác suất của biến cố $A$ là tỉ số giữa số kết quả thuận lợi cho $A$ và số kết quả có thể xảy ra của không gian mẫu.",
                "formula": r"P(A) = \frac{n(A)}{n(\Omega)} \quad (0 \le P(A) \le 1)",
                "trap": "Xác suất luôn nằm trong đoạn $[0; 1]$. Nếu tính ra số âm hoặc lớn hơn 1 thì chắc chắn đã làm sai.",
                "audio": "Xác suất bằng số kết quả thuận lợi cho biến cố chia cho tổng số phần tử không gian mẫu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất con xúc xắc",
                        "problem": "Gieo một con xúc xắc cân đối. Tính xác suất xuất hiện mặt chẵn.",
                        "solution": "- $n(\Omega) = 6$.\n- Mặt chẵn $A = \{2; 4; 6\} \implies n(A) = 3$.\n- $P(A) = 3/6 = 0.5$."
                    }
                ],
                "exercise": {"id": "10_26_2", "title": "Kiểm minh chứng", "content": "Gieo xúc xắc 6 mặt, xác suất xuất hiện mặt 6 chấm bằng bao nhiêu? (gợi ý phân số tối giản tử số bằng 1, mẫu số bằng c. c bằng:)", "type": "NUMERIC", "target": "6", "options": []}
            }
        }
    },
    "Bài 27: Thực hành tính xác suất theo định nghĩa cổ điển": {
        "chapter": "Chương IX: Một số yếu tố xác suất",
        "topics": {
            "I. Tính xác suất bằng sơ đồ hình cây": {
                "theory": "Sơ đồ hình cây phân nhánh các giai đoạn thử nghiệm, giúp đếm chính xác số kết quả có thể xảy ra và số kết quả thuận lợi mà không bị bỏ sót.",
                "formula": r"P(A) = \frac{n(A)}{n(\Omega)}",
                "trap": "Quên không phân nhánh các trường hợp đối ngẫu dẫn đến thiếu phần tử không gian mẫu.",
                "audio": "Sơ đồ cây vẽ rẽ nhánh từng bước giúp em không bao giờ bị đếm trùng hoặc đếm sót các trường hợp.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Dùng sơ đồ cây cho đồng xu",
                        "problem": "Gieo đồng xu 3 lần. Tính xác suất có đúng 2 lần xuất hiện mặt ngửa.",
                        "solution": "- Không gian mẫu có $2^3 = 8$ nhánh.\n- Các nhánh có đúng 2 mặt ngửa: $\{NNS, NSN, SNN\} \implies n(A) = 3$.\n- Xác suất $P(A) = 3/8 = 0.375$."
                    }
                ],
                "exercise": {"id": "10_27_1", "title": "Kiểm minh chứng", "content": "Gieo đồng xu 3 lần, tổng số kết quả có thể xảy ra ở không gian mẫu là:", "type": "NUMERIC", "target": "8", "options": []}
            },
            "II. Tính xác suất bằng phương pháp tổ hợp": {
                "theory": "Dùng công thức tổ hợp $C_n^k$ để tính số phần tử của không gian mẫu và biến cố khi lấy đồng thời nhiều phần tử từ một tập hợp.",
                "formula": r"P(A) = \frac{C_a^k \cdot C_b^m}{C_n^{k+m}}",
                "trap": "Rút đồng thời nhiều viên bi thì dùng Tổ hợp ($C$), không dùng Chỉnh hợp ($A$).",
                "audio": "Khi bốc cùng lúc nhiều đồ vật ra khỏi hộp, hãy dùng tổ hợp C để tính số phần tử không gian mẫu và biến cố.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút bi từ hộp",
                        "problem": "Hộp có 5 bi xanh và 3 bi đỏ. Lấy ngẫu nhiên 2 viên bi. Tính xác suất để lấy được 2 viên bi đỏ.",
                        "solution": "- $n(\Omega) = C_8^2 = 28$.\n- Lấy 2 bi đỏ: $n(A) = C_3^2 = 3$.\n- Xác suất $P(A) = \frac{3}{28}$."
                    }
                ],
                "exercise": {"id": "10_27_2", "title": "Kiểm minh chứng", "content": "Lấy ngẫu nhiên 2 viên bi từ hộp có 5 viên bi. Số phần tử không gian mẫu n(Omega) bằng:", "type": "NUMERIC", "target": "10", "options": []}
            }
        }
    }
})
