# data_grade10.py
# CHUẨN HÓA DỮ LIỆU TỪ VỞ TỰ HỌC TOÁN 10 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG

GRADE_10_DATA = {
    "Bài 1. Mệnh đề": {
        "chapter": "CHƯƠNG I. MỆNH ĐỀ VÀ TẬP HỢP",
        "topics": {
            "Chủ điểm 1: Mệnh đề và mệnh đề chứa biến": {
                "theory": "- Mệnh đề toán học là một khẳng định đúng hoặc sai. Một khẳng định không thể vừa đúng vừa sai.\n- Mệnh đề chứa biến là câu khẳng định chứa biến số, chưa xác định được tính đúng sai. Khi thay biến bằng giá trị cụ thể trong tập xác định thì câu đó trở thành một mệnh đề.",
                "formula": "P(x) \\text{ trở thành mệnh đề khi } x = x_0",
                "trap": "Các câu hỏi, câu cảm thán, câu cầu khiến không phải là mệnh đề toán học.",
                "audio": "Mệnh đề là một khẳng định có tính đúng sai rõ ràng. Các câu hỏi hoặc câu cảm thán thì không phải là mệnh đề toán học.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ: Nhận biết mệnh đề toán học",
                        "problem": "Trong các câu sau, câu nào là mệnh đề toán học?\na) Số 15 chia hết cho 3.\nb) Bạn có thích học Toán không?",
                        "solution": "a) 'Số 15 chia hết cho 3' là một khẳng định đúng nên là một mệnh đề toán học.\nb) 'Bạn có thích học Toán không?' là câu hỏi nên không phải là mệnh đề toán học."
                    }
                ],
                "exercise": {
                    "id": "10_b1_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Xét câu: 'Số 7 là số nguyên tố'. Đây là mệnh đề đúng hay sai? Nhập 1 nếu đúng, 0 nếu sai:",
                    "target": "1"
                }
            },
            "Chủ điểm 2: Mệnh đề phủ định, mệnh đề kéo theo và tương đương": {
                "theory": "- Phủ định của mệnh đề $P$ là $\\overline{P}$. Nếu $P$ đúng thì $\\overline{P}$ sai và ngược lại.\n- Mệnh đề kéo theo $P \\Rightarrow Q$ chỉ sai khi $P$ đúng mà $Q$ sai.\n- Mệnh đề tương đương $P \\Leftrightarrow Q$ đúng khi và chỉ khi cả $P$ và $Q$ cùng đúng hoặc cùng sai.",
                "formula": "\\overline{P}; \\quad P \\Rightarrow Q; \\quad P \\Leftrightarrow Q",
                "trap": "Phủ định của mệnh đề chứa 'với mọi' ($\\forall$) là 'tồn tại' ($\\exists$) và ngược lại.",
                "audio": "Phủ định của với mọi x thỏa mãn P(x) là tồn tại x để không thỏa mãn P(x).",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ: Phủ định của mệnh đề chứa kí hiệu lượng từ",
                        "problem": "Lập mệnh đề phủ định của mệnh đề: $P: '\\forall x \\in \\mathbb{R}, x^2 + 1 > 0'$.",
                        "solution": "Mệnh đề phủ định là: $\\overline{P}: '\\exists x \\in \\mathbb{R}, x^2 + 1 \\le 0'$."
                    }
                ],
                "exercise": {
                    "id": "10_b1_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Phủ định của mệnh đề $P: '\\exists x \\in \\mathbb{R}, x^2 = 2'$ là khẳng định đúng hay sai? (Nhập 1 nếu đúng, 0 nếu sai):",
                    "target": "0"
                }
            }
        }
    },
    "Bài 2. Tập hợp và các phép toán trên tập hợp": {
        "chapter": "CHƯƠNG I. MỆNH ĐỀ VÀ TẬP HỢP",
        "topics": {
            "Chủ điểm 1: Khái niệm tập hợp và các tập hợp số": {
                "theory": "- Tập hợp gồm các phần tử xác định. Kí hiệu $a \\in A$ hoặc $a \\notin A$.\n- Tập rỗng $\\emptyset$ là tập hợp không chứa phần tử nào.\n- Tập con: $A \\subset B \\iff (\\forall x \\in A \\implies x \\in B)$.\n- Các tập số cơ bản: $\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$.",
                "formula": "A \\subset B \\iff \\forall x, x \\in A \\implies x \\in B",
                "trap": "Nhầm lẫn giữa kí hiệu phần tử thuộc tập hợp ($\\in$) và tập con ($\\subset$). Ví dụ $\\{a\\} \\subset A$ chứ không viết $\\{a\\} \\in A$.",
                "audio": "Tập hợp con là mọi phần tử của tập A đều thuộc về tập B. Các em chú ý phân biệt dấu thuộc và dấu tập con.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ: Xác định tập hợp bằng cách liệt kê phần tử",
                        "problem": "Viết tập hợp $A = \\{x \\in \\mathbb{N} \\mid (2x - 1)(x^2 - 4) = 0\\}$ dưới dạng liệt kê.",
                        "solution": "Phương trình $(2x - 1)(x^2 - 4) = 0 \\iff x = \\frac{1}{2}$ hoặc $x = 2$ hoặc $x = -2$.\nVì $x \\in \\mathbb{N}$ nên chỉ nhận $x = 2$. Vậy $A = \\{2\\}$."
                    }
                ],
                "exercise": {
                    "id": "10_b2_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Số phần tử của tập hợp $A = \\{x \\in \\mathbb{Z} \\mid |x| \\le 2\\}$ là bao nhiêu?",
                    "target": "5"
                }
            },
            "Chủ điểm 2: Các phép toán giao, hợp, hiệu và các khoảng số thực": {
                "theory": "- Giao: $A \\cap B = \\{x \\mid x \\in A \\text{ và } x \\in B\\}$.\n- Hợp: $A \\cup B = \\{x \\mid x \\in A \\text{ hoặc } x \\in B\\}$.\n- Hiệu: $A \\setminus B = \\{x \\mid x \\in A \\text{ và } x \\notin B\\}$.\n- Phần bù: $C_E A = E \\setminus A$ (với $A \\subset E$).",
                "formula": "A \\cap B; \\quad A \\cup B; \\quad A \\setminus B; \\quad C_E A",
                "trap": "Khi lấy giao và hợp trên trục số thực, chú ý dấu ngoặc vuông $[,]$ (lấy mút) và ngoặc tròn $(,)$ (không lấy mút).",
                "audio": "Giao là lấy phần chung, hợp là gộp tất cả, hiệu là thuộc A nhưng không thuộc B.",
                "svg": "TAP_HOP",
                "examples": [
                    {
                        "title": "Ví dụ: Giao và hợp của hai khoảng số",
                        "problem": "Cho hai tập hợp $A = [-2; 3)$ và $B = (1; 5]$. Xác định tập $A \\cap B$.",
                        "solution": "Vẽ hai tập hợp trên trục số, phần giao nhau là $A \\cap B = (1; 3)$."
                    }
                ],
                "exercise": {
                    "id": "10_b2_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho $A = (-3; 2]$ và $B = (0; 4)$. Tập $A \\cap B$ là khoảng $(0; b]$. Nhập giá trị b:",
                    "target": "2"
                }
            }
        }
    },
    "Bài 7. Các khái niệm mở đầu về vectơ": {
        "chapter": "CHƯƠNG IV. HỆ THỨC LƯỢNG TRONG TAM GIÁC VÀ VECTƠ",
        "topics": {
            "Chủ điểm 1: Định nghĩa vectơ, độ dài và vectơ cùng phương, cùng hướng": {
                "theory": "- Vectơ là một đoạn thẳng có hướng (có điểm đầu và điểm cuối). Kí hiệu $\\vec{a}$ hoặc $\\vec{AB}$.\n- Độ dài vectơ là khoảng cách giữa điểm đầu và điểm cuối: $|\\vec{AB}| = AB$.\n- Giá của vectơ là đường thẳng đi qua điểm đầu và điểm cuối của nó.\n- Hai vectơ cùng phương nếu giá của chúng song song hoặc trùng nhau.",
                "formula": "|\\vec{AB}| = AB; \\quad \\vec{a} \\parallel \\vec{b} \\iff \\text{giá song song hoặc trùng}",
                "trap": "Vectơ không ($\\vec{0}$) cùng phương, cùng hướng với mọi vectơ.",
                "audio": "Vectơ là đoạn thẳng có hướng. Hai vectơ cùng phương nếu giá của chúng song song hoặc trùng nhau.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Nhận biết vectơ cùng hướng trong hình chữ nhật",
                        "problem": "Cho hình chữ nhật ABCD. So sánh hướng của hai vectơ $\\vec{AB}$ và $\\vec{DC}$.",
                        "solution": "Vì $AB \\parallel DC$ và chiều từ A sang B trùng với chiều từ D sang C nên $\\vec{AB}$ và $\\vec{DC}$ là hai vectơ cùng hướng."
                    }
                ],
                "exercise": {
                    "id": "10_b7_c1",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho hình vuông ABCD có cạnh bằng 3. Tính độ dài của vectơ $\\vec{AC}$ (làm tròn đến 1 chữ số thập phân):",
                    "target": "4.2"
                }
            },
            "Chủ điểm 2: Hai vectơ bằng nhau và vectơ đối": {
                "theory": "- Hai vectơ bằng nhau nếu chúng cùng hướng và cùng độ dài: $\\vec{a} = \\vec{b} \\iff \\vec{a} \\uparrow\\uparrow \\vec{b} \\text{ và } |\\vec{a}| = |\\vec{b}|$.\n- Vectơ đối của $\\vec{a}$ là vectơ ngược hướng và có cùng độ dài với $\\vec{a}$. Kí hiệu $-\\vec{a}$.",
                "formula": "\\vec{a} = \\vec{b} \\iff (\\vec{a} \\uparrow\\uparrow \\vec{b} \\text{ và } |\\vec{a}| = |\\vec{b}|); \\quad \\vec{BA} = -\\vec{AB}",
                "trap": "Chỉ có cùng độ dài thôi thì chưa đủ để kết luận hai vectơ bằng nhau, bắt buộc phải có cùng hướng.",
                "audio": "Hai vectơ bằng nhau khi và chỉ khi chúng cùng hướng và cùng độ dài.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ: Vectơ bằng nhau trong hình bình hành",
                        "problem": "Cho hình bình hành ABCD có tâm O. Chỉ ra các vectơ bằng vectơ $\\vec{AB}$.",
                        "solution": "Vì AB song song, cùng độ dài và cùng hướng với DC nên $\\vec{AB} = \\vec{DC}$."
                    }
                ],
                "exercise": {
                    "id": "10_b7_c2",
                    "title": "Bài tập tự giải kiểm minh chứng",
                    "content": "Cho tam giác ABC đều. Số lượng vectơ (khác vectơ-không) có điểm đầu và điểm cuối là các đỉnh của tam giác bằng bao nhiêu?",
                    "target": "6"
                }
            }
        }
    }
}
