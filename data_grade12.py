# ==============================================================================
# DATA_GRADE12.PY - HỌC LIỆU TOÁN 12 KẾT NỐI TRI THỨC (PHẦN 1: BÀI 1 -> BÀI 7)
# ==============================================================================

GRADE_12_DATA = {}

GRADE_12_DATA.update({
    "Bài 1: Tính đơn điệu và cực trị của hàm số": {
        "chapter": "Chương I: Ứng dụng đạo hàm khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Tính đơn điệu của hàm số": {
                "theory": "Hàm số đồng biến khi đạo hàm $y' \\ge 0$, nghịch biến khi $y' \\le 0$ trên một khoảng (với $y'=0$ tại hữu hạn điểm). Quy trình: Tìm TXĐ $\\rightarrow$ Tính $y'$ $\\rightarrow$ Tìm nghiệm $y'=0$ $\\rightarrow$ Lập bảng xét dấu.",
                "formula": r"f'(x) \ge 0, \forall x \in K \implies \text{Hàm số đồng biến trên } K",
                "trap": "Khi kết luận khoảng đơn điệu, bắt buộc phải viết rời nhau dùng chữ 'và' hoặc dấu phẩy, tuyệt đối không dùng ký hiệu hợp ($\\cup$).",
                "audio": "Hàm số đồng biến khi đạo hàm mang dấu dương, nghịch biến khi đạo hàm mang dấu âm. Hãy nhớ lập bảng xét dấu cẩn thận trước khi kết luận.",
                "svg": "DON_DIEU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm khoảng đơn điệu của hàm bậc ba",
                        "problem": "Tìm các khoảng đồng biến và nghịch biến của hàm số $y = x^3 - 3x^2 + 2$.",
                        "solution": "- Tập xác định: $D = \\mathbb{R}$.\n- Đạo hàm: $y' = 3x^2 - 6x = 3x(x - 2)$. Cho $y' = 0 \\iff x = 0$ hoặc $x = 2$.\n- Lập bảng xét dấu $y'$: $y' > 0$ trên $(-\\infty; 0)$ và $(2; +\\infty)$; $y' < 0$ trên $(0; 2)$.\n- **Kết luận:** Hàm số đồng biến trên khoảng $(-\\infty; 0)$ và $(2; +\\infty)$; nghịch biến trên khoảng $(0; 2)$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm khoảng đơn điệu của hàm phân thức bậc nhất",
                        "problem": "Xét tính đơn điệu của hàm số $y = \\frac{2x - 1}{x + 1}$.",
                        "solution": "- Tập xác định: $D = \\mathbb{R} \\setminus \\{-1\\}$.\n- Đạo hàm (công thức nhanh): $y' = \\frac{2 \\cdot 1 - (-1) \\cdot 1}{(x + 1)^2} = \\frac{3}{(x + 1)^2}$.\n- Nhận xét: $y' > 0$ với mọi $x \\neq -1$.\n- **Kết luận:** Hàm số đồng biến trên từng khoảng $(-\\infty; -1)$ và $(-1; +\\infty)$."
                    },
                    {
                        "title": "Ví dụ 3: Đọc khoảng đơn điệu từ bảng biến thiên",
                        "problem": "Cho hàm số có bảng biến thiên: $y'$ mang dấu $(-)$ trên khoảng $(1; 5)$ và mang dấu $(+)$ trên $(-\\infty; 1)$ và $(5; +\\infty)$. Tìm khoảng nghịch biến.",
                        "solution": "- Khoảng nghịch biến ứng với vùng đạo hàm $y'$ mang dấu âm $(-)$.\n- Dựa vào BBT, $y' < 0$ trên khoảng $(1; 5)$.\n- **Kết luận:** Hàm số nghịch biến trên khoảng $(1; 5)$."
                    }
                ],
                "exercise": {
                    "id": "12_1_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hàm số y = x^3 - 3x nghịch biến trên khoảng (-1; b). Giá trị của b là bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Cực trị của hàm số": {
                "theory": "Cực trị là điểm mà tại đó đồ thị nhô lên cao nhất (Cực đại) hoặc lõm xuống thấp nhất (Cực tiểu) so với vùng lân cận. Dấu hiệu nhận biết: Đạo hàm $y'$ đổi dấu khi đi qua điểm đó.",
                "formula": r"(+) \to (-) \implies \text{Điểm Cực Đại}; \quad (-) \to (+) \implies \text{Điểm Cực Tiểu}",
                "trap": "Học sinh rất hay nhầm lẫn giữa 'Điểm cực trị của hàm số' (là hoành độ $x$) và 'Giá trị cực trị' (là tung độ $y$). Đọc thật kỹ câu hỏi của đề bài.",
                "audio": "Cực trị xảy ra khi đạo hàm y phẩy đổi dấu. Đổi từ dương sang âm là cực đại, từ âm sang dương là cực tiểu.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm giá trị cực trị của hàm bậc ba",
                        "problem": "Tìm giá trị cực đại và giá trị cực tiểu của hàm số $y = -x^3 + 3x + 1$.",
                        "solution": "- Đạo hàm: $y' = -3x^2 + 3 = 0 \\iff x = 1$ hoặc $x = -1$.\n- Xét dấu: $y'$ đổi dấu từ $(-)$ sang $(+)$ tại $x = -1 \\implies$ Giá trị cực tiểu $y_{CT} = y(-1) = -1$.\n- $y'$ đổi dấu từ $(+)$ sang $(-)$ tại $x = 1 \\implies$ Giá trị cực đại $y_{CD} = y(1) = 3$."
                    },
                    {
                        "title": "Ví dụ 2: Cực trị của hàm số bậc bốn (trùng phương)",
                        "problem": "Hàm số $y = x^4 - 2x^2 + 3$ có bao nhiêu điểm cực trị?",
                        "solution": "- Đạo hàm: $y' = 4x^3 - 4x = 4x(x^2 - 1)$.\n- Cho $y' = 0 \\iff x = 0, x = 1, x = -1$.\n- Phương trình $y'=0$ có 3 nghiệm phân biệt và $y'$ đổi dấu khi qua cả 3 nghiệm này.\n- **Kết luận:** Hàm số có 3 điểm cực trị."
                    },
                    {
                        "title": "Ví dụ 3: Cực trị của hàm phân thức bậc hai trên bậc nhất",
                        "problem": "Tìm điểm cực tiểu của hàm số $y = \\frac{x^2 - x + 1}{x - 1}$.",
                        "solution": "- Tập xác định: $x \\neq 1$.\n- Đạo hàm: $y' = \\frac{(2x - 1)(x - 1) - (x^2 - x + 1)}{(x - 1)^2} = \\frac{x^2 - 2x}{(x - 1)^2}$.\n- Cho $y' = 0 \\iff x = 0$ hoặc $x = 2$.\n- Qua $x=2$, tử số đổi dấu từ $(-)$ sang $(+)$ nên $y'$ đổi từ $(-)$ sang $(+)$.\n- **Kết luận:** Điểm cực tiểu của hàm số là $x = 2$."
                    }
                ],
                "exercise": {
                    "id": "12_1_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị cực tiểu của hàm số y = x^3 - 3x + 2 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "0", 
                    "options": []
                }
            }
        }
    },
    "Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số": {
        "chapter": "Chương I: Ứng dụng đạo hàm khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Tìm GTLN, GTNN trên đoạn [a; b]": {
                "theory": "Phương pháp tối ưu không cần lập bảng biến thiên: Chỉ cần tìm các nghiệm của phương trình $f'(x) = 0$ nằm TRONG khoảng $(a; b)$. Sau đó tính các giá trị $f(a), f(b)$ và $f(x_i)$. Số lớn nhất là max, nhỏ nhất là min.",
                "formula": r"\max_{[a; b]} f(x) = \max\{f(a), f(b), f(x_i)\}",
                "trap": "Bẫy kinh điển: Học sinh quên loại bỏ các nghiệm $x_i$ nằm ngoài đoạn $[a; b]$, dẫn đến tính dư giá trị và chọn sai đáp án.",
                "audio": "Trên một đoạn kín, giá trị lớn nhất và nhỏ nhất luôn rơi vào một trong hai đầu mút hoặc tại các điểm đạo hàm bằng không.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm GTLN, GTNN của hàm đa thức",
                        "problem": "Tìm GTLN và GTNN của hàm số $y = x^3 - 3x + 1$ trên đoạn $[0; 2]$.",
                        "solution": "- Đạo hàm: $y' = 3x^2 - 3$. Cho $y' = 0 \\iff x = 1$ hoặc $x = -1$.\n- Đối chiếu đoạn $[0; 2]$: Nhận $x = 1$, loại $x = -1$.\n- Tính giá trị: $y(0) = 1$; $y(1) = -1$; $y(2) = 3$.\n- **Kết luận:** GTLN bằng 3 (tại $x=2$), GTNN bằng -1 (tại $x=1$)."
                    },
                    {
                        "title": "Ví dụ 2: GTLN, GTNN của hàm phân thức",
                        "problem": "Tìm GTNN của hàm số $y = \\frac{x + 2}{x - 1}$ trên đoạn $[2; 4]$.",
                        "solution": "- Hàm số xác định trên $[2; 4]$ (vì điểm gián đoạn $x=1$ không thuộc đoạn).\n- Đạo hàm: $y' = \\frac{-3}{(x - 1)^2} < 0, \\forall x \\in [2; 4]$. Hàm số luôn nghịch biến.\n- Do đó, GTLN là $y(2) = 4$ và GTNN là $y(4) = \\frac{6}{3} = 2$.\n- **Kết luận:** GTNN của hàm số bằng 2."
                    },
                    {
                        "title": "Ví dụ 3: Hàm chứa căn thức",
                        "problem": "Tìm GTLN của hàm số $y = \\sqrt{4 - x^2}$.",
                        "solution": "- Tập xác định: $4 - x^2 \\ge 0 \\iff x \\in [-2; 2]$. Ta xét hàm trên đoạn $[-2; 2]$.\n- Đạo hàm $y' = \\frac{-x}{\\sqrt{4 - x^2}} = 0 \\iff x = 0 \\in (-2; 2)$.\n- Tính các giá trị: $y(-2) = 0$; $y(2) = 0$; $y(0) = 2$.\n- **Kết luận:** GTLN của hàm số bằng 2."
                    }
                ],
                "exercise": {
                    "id": "12_2_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị lớn nhất của hàm số y = x^3 - 3x + 1 trên đoạn [0; 2] bằng:", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    },
    "Bài 3: Đường tiệm cận của đồ thị hàm số": {
        "chapter": "Chương I: Ứng dụng đạo hàm khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Tiệm cận đứng và Tiệm cận ngang": {
                "theory": "Đường thẳng $x = x_0$ là Tiệm cận đứng (TCĐ) nếu giới hạn khi $x \to x_0$ là vô cực (thường xảy ra khi mẫu = 0, tử khác 0). Đường thẳng $y = y_0$ là Tiệm cận ngang (TCN) nếu giới hạn khi $x \to \\pm\\infty$ bằng $y_0$.",
                "formula": r"\lim_{x \to x_0} y = \infty \implies \text{TCĐ } x = x_0; \quad \lim_{x \to \infty} y = y_0 \implies \text{TCN } y = y_0",
                "trap": "Nếu nghiệm của mẫu đồng thời là nghiệm của tử số (triệt tiêu nhau), đường thẳng đó chưa chắc là tiệm cận đứng. Phải rút gọn trước khi kết luận.",
                "audio": "Mẫu số triệt tiêu mà tử số khác không cho ta tiệm cận đứng x bằng hằng số. Giới hạn tại vô cực cho ta tiệm cận ngang y bằng hằng số.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tiệm cận hàm phân thức bậc 1/1",
                        "problem": "Tìm các đường tiệm cận của đồ thị hàm số $y = \\frac{2x - 1}{x - 3}$.",
                        "solution": "- Mẫu số $x - 3 = 0 \\implies x = 3$. Giới hạn $\\lim_{x \\to 3} y = \\infty \\implies$ TCĐ là đường thẳng $x = 3$.\n- Giới hạn vô cực $\\lim_{x \\to \\infty} \\frac{2x - 1}{x - 3} = 2 \\implies$ TCN là đường thẳng $y = 2$."
                    },
                    {
                        "title": "Ví dụ 2: Bẫy triệt tiêu nghiệm tử và mẫu",
                        "problem": "Tìm số đường tiệm cận đứng của đồ thị hàm số $y = \\frac{x - 1}{x^2 - 1}$.",
                        "solution": "- Mẫu số $x^2 - 1 = 0 \\implies x = 1$ hoặc $x = -1$.\n- Tại $x=1$, ta rút gọn hàm số: $\\lim_{x \\to 1} \\frac{x-1}{(x-1)(x+1)} = \\lim_{x \\to 1} \\frac{1}{x+1} = \\frac{1}{2}$. Vì giới hạn là số hữu hạn, $x=1$ KHÔNG là TCĐ.\n- Tại $x=-1$, giới hạn là $\\infty \\implies x=-1$ là TCĐ duy nhất."
                    },
                    {
                        "title": "Ví dụ 3: Hàm chứa căn thức",
                        "problem": "Tìm TCN của đồ thị hàm số $y = \\frac{\\sqrt{4x^2 + 1}}{x - 2}$.",
                        "solution": "- Khi $x \\to +\\infty$, ta có $\\lim_{x \\to +\\infty} \\frac{\\sqrt{4x^2}}{x} = \\frac{2x}{x} = 2 \\implies y = 2$ là TCN.\n- Khi $x \\to -\\infty$, $\\sqrt{4x^2} = -2x$ (vì $x < 0$). Ta có $\\lim_{x \\to -\\infty} \\frac{-2x}{x} = -2 \\implies y = -2$ là TCN.\n- **Kết luận:** Đồ thị có 2 đường TCN."
                    }
                ],
                "exercise": {
                    "id": "12_3_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đường tiệm cận ngang của đồ thị hàm số y = (2x - 3)/(x + 1) là đường thẳng y = c. Giá trị c bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tiệm cận xiên của đồ thị hàm số": {
                "theory": "Đường thẳng $y = ax + b$ ($a \\neq 0$) là tiệm cận xiên khi bậc của tử số lớn hơn bậc của mẫu số đúng 1 bậc. Có thể tìm nhanh bằng cách lấy đa thức tử chia cho đa thức mẫu, phần thương số chính là phương trình tiệm cận xiên.",
                "formula": r"y = ax + b \quad \text{với} \quad a = \lim_{x \to \infty} \frac{f(x)}{x}; \quad b = \lim_{x \to \infty} [f(x) - ax]",
                "trap": "Chỉ có hàm số phân thức hữu tỉ có bậc tử > bậc mẫu đúng 1 đơn vị mới sinh ra tiệm cận xiên. Các trường hợp khác không cần xét.",
                "audio": "Khi bậc của tử lớn hơn bậc của mẫu đúng 1 bậc, ta lấy tử chia cho mẫu, phần thương bậc nhất chính là phương trình đường tiệm cận xiên.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tiệm cận xiên bằng phép chia đa thức",
                        "problem": "Tìm phương trình đường tiệm cận xiên của đồ thị hàm số $y = \\frac{x^2 - 3x + 2}{x + 1}$.",
                        "solution": "- Thực hiện phép chia đa thức tử cho mẫu:\n  $\\frac{x^2 - 3x + 2}{x + 1} = x - 4 + \\frac{6}{x + 1}$.\n- Khi $x \\to \\pm\\infty$, phần dư $\\frac{6}{x + 1} \\to 0$.\n- **Kết luận:** Đường tiệm cận xiên là $y = x - 4$."
                    },
                    {
                        "title": "Ví dụ 2: Tiệm cận xiên hàm không có số hạng tự do",
                        "problem": "Viết phương trình tiệm cận xiên của đồ thị hàm số $y = \\frac{2x^2 - x}{x - 1}$.",
                        "solution": "- Tách tử số: $2x^2 - x = 2x^2 - 2x + x = 2x(x - 1) + x - 1 + 1$.\n- Chia cho mẫu: $y = 2x + 1 + \\frac{1}{x - 1}$.\n- **Kết luận:** Đường thẳng $y = 2x + 1$ là tiệm cận xiên."
                    },
                    {
                        "title": "Ví dụ 3: Tính diện tích tam giác tạo bởi hai tiệm cận",
                        "problem": "Cho hàm số $y = \\frac{x^2 + x}{x - 1}$. Giao điểm I của hai đường tiệm cận có tọa độ là bao nhiêu?",
                        "solution": "- Tiệm cận đứng: $x = 1$.\n- Tiệm cận xiên: $y = x + 2 + \\frac{2}{x - 1} \\implies y = x + 2$.\n- Giao điểm I thỏa mãn hệ: $x = 1$ và $y = 1 + 2 = 3$.\n- **Kết luận:** Tọa độ tâm đối xứng là $I(1; 3)$."
                    }
                ],
                "exercise": {
                    "id": "12_3_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tiệm cận xiên của đồ thị hàm số y = (x^2 + x + 1)/(x - 1) có dạng y = ax + b. Hệ số a bằng:", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số": {
        "chapter": "Chương I: Ứng dụng đạo hàm khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Khảo sát đồ thị hàm số đa thức (Bậc 3)": {
                "theory": "Quy trình khảo sát 5 bước chuẩn mực: (1) Tập xác định. (2) Đạo hàm và cực trị. (3) Giới hạn tại vô cực. (4) Lập bảng biến thiên. (5) Vẽ đồ thị qua các điểm cực trị và giao trục tọa độ. Tâm đối xứng của đồ thị bậc 3 là điểm uốn (nghiệm của $y''=0$).",
                "formula": r"y'' = 0 \implies \text{Hoành độ điểm uốn (Tâm đối xứng)}",
                "trap": "Khi vẽ đồ thị hàm bậc 3 có $a > 0$, nhánh cuối cùng (bên phải) luôn hướng đi lên $+\\infty$. Đừng vẽ ngược lại.",
                "audio": "Với hàm đa thức, bước quan trọng nhất là tính chính xác tọa độ các điểm cực trị để vẽ khung đồ thị.",
                "svg": "CUC_TRI",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định giao điểm với trục tung",
                        "problem": "Đồ thị hàm số $y = 2x^3 - 3x^2 + 5$ cắt trục tung tại điểm có tung độ bằng bao nhiêu?",
                        "solution": "- Giao điểm với trục tung là điểm có hoành độ $x = 0$.\n- Thay $x = 0$ vào hàm số: $y(0) = 2(0)^3 - 3(0)^2 + 5 = 5$.\n- **Kết luận:** Đồ thị cắt trục tung tại điểm $M(0; 5)$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm tâm đối xứng (điểm uốn)",
                        "problem": "Tìm tọa độ tâm đối xứng của đồ thị hàm số $y = x^3 - 3x^2 + 2$.",
                        "solution": "- Đạo hàm cấp 1: $y' = 3x^2 - 6x$.\n- Đạo hàm cấp 2: $y'' = 6x - 6$. Cho $y'' = 0 \\iff x = 1$.\n- Tính tung độ: $y(1) = 1^3 - 3(1)^2 + 2 = 0$.\n- **Kết luận:** Tâm đối xứng là điểm $I(1; 0)$."
                    },
                    {
                        "title": "Ví dụ 3: Đọc đồ thị nhận dạng hệ số",
                        "problem": "Đồ thị hàm số $y = ax^3 + bx^2 + cx + d$ có dạng chữ N, đi qua gốc tọa độ O. Khẳng định nào đúng về a và d?",
                        "solution": "- Đồ thị có dạng chữ N (nhánh cuối đi lên) $\\implies a > 0$.\n- Đồ thị đi qua gốc tọa độ $O(0;0) \\implies y(0) = d = 0$.\n- **Kết luận:** $a > 0$ và $d = 0$."
                    }
                ],
                "exercise": {
                    "id": "12_4_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tâm đối xứng của đồ thị hàm số y = x^3 - 3x^2 + 2 có hoành độ x bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Khảo sát đồ thị hàm số phân thức": {
                "theory": "Đối với hàm phân thức bậc 1/bậc 1: Tập xác định bị ngắt quãng. Phải tìm 2 đường tiệm cận. Đồ thị là hai nhánh Hypebol nhận giao điểm của 2 đường tiệm cận làm tâm đối xứng.",
                "formula": r"I\left(-\frac{d}{c}; \frac{a}{c}\right) \text{ là tâm đối xứng của } y = \frac{ax+b}{cx+d}",
                "trap": "Trong Bảng biến thiên, vị trí điểm gián đoạn $x = -d/c$ phải vẽ 2 vạch sọc `||` kéo dài xuyên suốt từ dòng $y'$ xuống dòng $y$.",
                "audio": "Đối với hàm phân thức, giao điểm của tiệm cận đứng và tiệm cận ngang chính là tâm đối xứng của đồ thị.",
                "svg": "TIEM_CAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tâm đối xứng của đồ thị",
                        "problem": "Tìm tọa độ tâm đối xứng của đồ thị hàm số $y = \\frac{2x - 1}{x + 1}$.",
                        "solution": "- Tiệm cận đứng: $x = -1$.\n- Tiệm cận ngang: $y = 2$.\n- Tâm đối xứng $I$ là giao của 2 đường tiệm cận.\n- **Kết luận:** Tâm đối xứng $I(-1; 2)$."
                    },
                    {
                        "title": "Ví dụ 2: Dấu của đạo hàm",
                        "problem": "Hàm số $y = \\frac{2x + 1}{x - 1}$ có đồ thị gồm 2 nhánh đi lên hay đi xuống từ trái sang phải?",
                        "solution": "- Đạo hàm $y' = \\frac{2(-1) - 1(1)}{(x-1)^2} = \\frac{-3}{(x-1)^2} < 0$.\n- Vì $y' < 0$, đồ thị hàm số nghịch biến trên từng khoảng xác định.\n- **Kết luận:** 2 nhánh đồ thị đi xuống từ trái sang phải."
                    },
                    {
                        "title": "Ví dụ 3: Xác định giao điểm trục hoành",
                        "problem": "Tìm tọa độ giao điểm của đồ thị $y = \\frac{x - 3}{x + 2}$ với trục hoành.",
                        "solution": "- Đồ thị cắt trục hoành khi $y = 0$.\n- $\\frac{x - 3}{x + 2} = 0 \\iff x - 3 = 0 \\iff x = 3$.\n- **Kết luận:** Giao điểm với trục hoành là $A(3; 0)$."
                    }
                ],
                "exercise": {
                    "id": "12_4_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tâm đối xứng của đồ thị hàm số y = (x + 2)/(x - 1) có hoành độ x bằng:", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 5: Ứng dụng đạo hàm giải quyết bài toán thực tiễn": {
        "chapter": "Chương I: Ứng dụng đạo hàm khảo sát và vẽ đồ thị hàm số",
        "topics": {
            "Chủ điểm 1: Mô hình hóa và Tối ưu hóa (GTLN, GTNN)": {
                "theory": "Bước 1: Chọn ẩn $x$ đại diện cho một đại lượng vật lý/hình học và tìm điều kiện của $x$ (thường là $x>0$). Bước 2: Thiết lập hàm mục tiêu $f(x)$ (thể tích, diện tích, chi phí). Bước 3: Dùng đạo hàm $f'(x)=0$ để tìm giá trị tối ưu.",
                "formula": r"V(x) \to \max \iff V'(x) = 0; \quad C(x) \to \min \iff C'(x) = 0",
                "trap": "Sau khi giải xong, học sinh thường quên lấy kết quả thay ngược vào biểu thức chi phí hoặc thể tích để trả lời câu hỏi cuối cùng của bài toán.",
                "audio": "Bài toán thực tiễn luôn yêu cầu ba bước: Lập hàm số, tính đạo hàm tìm cực trị, và đối chiếu điều kiện để đưa ra kết luận thực tế.",
                "svg": "GTLN_GTNN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Bài toán diện tích hình chữ nhật lớn nhất",
                        "problem": "Một người nông dân dùng 40 mét rào để rào 3 mặt của một khu vườn hình chữ nhật (mặt thứ 4 tựa vào bức tường). Tìm diện tích lớn nhất của khu vườn.",
                        "solution": "- Gọi chiều rộng của khu vườn là $x$ ($0 < x < 20$). Chiều dài là rào trừ đi 2 chiều rộng: $y = 40 - 2x$.\n- Hàm diện tích: $S(x) = x(40 - 2x) = 40x - 2x^2$.\n- Đạo hàm: $S'(x) = 40 - 4x = 0 \\iff x = 10$.\n- Tại $x=10$, diện tích lớn nhất là $S_{max} = 10(40 - 20) = 200\\text{ m}^2$."
                    },
                    {
                        "title": "Ví dụ 2: Bài toán thể tích hộp không nắp",
                        "problem": "Cần làm một cái hộp hình hộp chữ nhật không nắp, đáy là hình vuông, thể tích cố định là $V = 32\\text{ dm}^3$. Tính độ dài cạnh đáy để diện tích vật liệu tốn ít nhất.",
                        "solution": "- Gọi cạnh đáy vuông là $x$ ($x>0$), chiều cao là $h$. Ta có $x^2 \\cdot h = 32 \\implies h = \\frac{32}{x^2}$.\n- Diện tích vật liệu (1 đáy, 4 mặt bên): $S(x) = x^2 + 4xh = x^2 + 4x \\cdot \\frac{32}{x^2} = x^2 + \\frac{128}{x}$.\n- Đạo hàm: $S'(x) = 2x - \\frac{128}{x^2} = \\frac{2x^3 - 128}{x^2}$. Cho $S'(x) = 0 \\iff x^3 = 64 \\iff x = 4$.\n- **Kết luận:** Cạnh đáy bằng $4\\text{ dm}$ thì tốn ít vật liệu nhất."
                    },
                    {
                        "title": "Ví dụ 3: Bài toán kinh tế (Tối ưu lợi nhuận)",
                        "problem": "Hàm chi phí của nhà máy là $C(x) = x^2 - 10x + 100$ (triệu đồng). Sản xuất bao nhiêu sản phẩm $x$ thì chi phí đạt mức nhỏ nhất?",
                        "solution": "- Đạo hàm hàm chi phí: $C'(x) = 2x - 10$.\n- Cho $C'(x) = 0 \\iff 2x = 10 \\iff x = 5$.\n- **Kết luận:** Sản xuất 5 sản phẩm thì chi phí đạt mức nhỏ nhất (đỉnh parabol)."
                    }
                ],
                "exercise": {
                    "id": "12_5_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cần làm hộp không nắp đáy vuông thể tích 32 dm3. Hỏi diện tích vật liệu nhỏ nhất bằng bao nhiêu dm2?", 
                    "type": "NUMERIC", 
                    "target": "48", 
                    "options": []
                }
            }
        }
    },
    "Bài 6: Vectơ trong không gian": {
        "chapter": "Chương II: Vectơ và Hệ tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Phép toán và Quy tắc vectơ không gian": {
                "theory": "Mở rộng từ hình học phẳng: Quy tắc 3 điểm (nối tiếp), Quy tắc hình bình hành (chung gốc). Điểm mới: **Quy tắc hình hộp** với 3 cạnh xuất phát từ một đỉnh.",
                "formula": r"\vec{AB} + \vec{AD} + \vec{AA'} = \vec{AC'} \ (\text{Quy tắc hình hộp})",
                "trap": "Học sinh thường quên quy tắc trừ chung gốc: $\\vec{AB} - \\vec{AC} = \\vec{CB}$ (điểm sau thành điểm đầu, đọc ngược lại).",
                "audio": "Trong không gian, quy tắc quan trọng nhất là quy tắc hình hộp. Vectơ đường chéo bằng tổng của ba vectơ cạnh chung một đỉnh.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút gọn biểu thức vectơ",
                        "problem": "Cho tứ diện $ABCD$. Rút gọn biểu thức $\\vec{u} = \\vec{AB} + \\vec{BC} + \\vec{CD}$.",
                        "solution": "- Áp dụng quy tắc 3 điểm nối tiếp nhiều lần:\n  $\\vec{AB} + \\vec{BC} = \\vec{AC}$.\n  Tiếp tục: $\\vec{AC} + \\vec{CD} = \\vec{AD}$.\n- **Kết luận:** $\\vec{u} = \\vec{AD}$."
                    },
                    {
                        "title": "Ví dụ 2: Áp dụng quy tắc hình hộp",
                        "problem": "Cho hình hộp $ABCD.A'B'C'D'$. Đẳng thức nào biểu diễn vectơ đường chéo $\\vec{AC'}$ theo 3 cạnh xuất phát từ đỉnh $A$?",
                        "solution": "- 3 cạnh xuất phát từ $A$ là $\\vec{AB}, \\vec{AD}, \\vec{AA'}$.\n- Theo quy tắc hình hộp, ta có:\n  $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ thức trọng tâm tứ diện",
                        "problem": "Cho tứ diện $ABCD$ có trọng tâm $G$. Biểu diễn hệ thức liên hệ giữa các vectơ $\\vec{GA}, \\vec{GB}, \\vec{GC}, \\vec{GD}$.",
                        "solution": "- Tương tự như trọng tâm tam giác trong mặt phẳng, trọng tâm $G$ của tứ diện triệt tiêu tổng 4 vectơ tới 4 đỉnh.\n- **Kết luận:** $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$."
                    }
                ],
                "exercise": {
                    "id": "12_6_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho hình hộp ABCD.A'B'C'D'. Tổng vectơ AB + AD + AA' bằng vectơ nào? (Điền tên vectơ, ví dụ: AC')", 
                    "type": "NUMERIC", 
                    "target": "AC'", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tích vô hướng của hai vectơ": {
                "theory": "Tích vô hướng là một SỐ THỰC, bằng tích của 2 độ dài nhân với cosin của góc xen giữa. Đây là công cụ chủ lực để chứng minh hai đường thẳng vuông góc.",
                "formula": r"\vec{u} \cdot \vec{v} = |\vec{u}| \cdot |\vec{v}| \cdot \cos(\vec{u}, \vec{v}); \quad \vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0",
                "trap": "Tuyệt đối không được viết kết quả của tích vô hướng là một vectơ (có mũi tên trên đầu). Nó phải là một số.",
                "audio": "Tích vô hướng là một hằng số. Hai vectơ vuông góc với nhau khi và chỉ khi tích vô hướng của chúng bằng không.",
                "svg": "VECTOR",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc giữa hai vectơ",
                        "problem": "Cho tứ diện đều $ABCD$ cạnh $a$. Tính góc giữa hai vectơ $\\vec{AB}$ và $\\vec{AC}$.",
                        "solution": "- Tam giác $ABC$ là tam giác đều vì các mặt của tứ diện đều là tam giác đều.\n- Góc giữa $\\vec{AB}$ và $\\vec{AC}$ chính là góc $\\widehat{BAC}$.\n- Vì tam giác đều nên $\\widehat{BAC} = 60^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Tính tích vô hướng",
                        "problem": "Cho hình vuông $ABCD$ cạnh $a$. Tính tích vô hướng $\\vec{AB} \\cdot \\vec{AC}$.",
                        "solution": "- Độ dài $\vert{}\\vec{AB}\vert{} = a$, đường chéo $\vert{}\\vec{AC}\vert{} = a\\sqrt{2}$.\n- Góc giữa $\\vec{AB}$ và $\\vec{AC}$ là góc $\\widehat{BAC} = 45^\\circ$.\n- $\\vec{AB} \\cdot \\vec{AC} = a \\cdot a\\sqrt{2} \\cdot \\cos 45^\\circ = a \\cdot a\\sqrt{2} \\cdot \\frac{\\sqrt{2}}{2} = a^2$."
                    },
                    {
                        "title": "Ví dụ 3: Sử dụng tích vô hướng chứng minh vuông góc",
                        "problem": "Cho hình lập phương $ABCD.A'B'C'D'$. Tính tích vô hướng $\\vec{AB} \\cdot \\vec{AD'}$.",
                        "solution": "- Vì $AB \\perp (ADD'A')$ nên đường thẳng $AB$ vuông góc với mọi đường thẳng trong mặt phẳng $(ADD'A')$, đặc biệt là $AD'$.\n- Góc giữa chúng bằng $90^\\circ$.\n- Do đó, $\\vec{AB} \\cdot \\vec{AD'} = 0$."
                    }
                ],
                "exercise": {
                    "id": "12_6_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho hình lập phương ABCD.A'B'C'D'. Góc giữa hai vectơ AB và AD' bằng bao nhiêu độ?", 
                    "type": "NUMERIC", 
                    "target": "90", 
                    "options": []
                }
            }
        }
    },
    "Bài 7: Hệ trục tọa độ trong không gian": {
        "chapter": "Chương II: Vectơ và Hệ tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Hệ trục Oxyz, Tọa độ điểm và Vectơ": {
                "theory": "Hệ trục $Oxyz$ gồm 3 trục vuông góc từng đôi một. Điểm $M(x; y; z)$ tương đương với đẳng thức vectơ $\\vec{OM} = x\\vec{i} + y\\vec{j} + z\\vec{k}$.\nHình chiếu vuông góc của điểm $M(x;y;z)$ lên một trục/mặt phẳng tọa độ: Chiếu lên cái gì thì giữ lại tọa độ đó, các tọa độ còn lại cho bằng $0$.",
                "formula": r"\vec{u} = (x; y; z) \iff \vec{u} = x\vec{i} + y\vec{j} + z\vec{k}; \quad M_{Oxy}(x; y; 0)",
                "trap": "Học sinh thường quên tọa độ điểm đối xứng. Đối xứng qua $Ox$: giữ nguyên $x$, đổi dấu $y$ và $z$.",
                "audio": "Trong hệ tọa độ không gian, khi chiếu điểm lên trục hay mặt phẳng nào, ta giữ nguyên tọa độ đó và cho các tọa độ không liên quan bằng không.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận diện tọa độ từ đẳng thức vectơ",
                        "problem": "Cho vectơ $\\vec{u} = 2\\vec{i} - 3\\vec{j} + 5\\vec{k}$. Tìm tọa độ của vectơ $\\vec{u}$.",
                        "solution": "- Tọa độ của vectơ $\\vec{u}$ chính là các hệ số đứng trước $\\vec{i}, \\vec{j}, \\vec{k}$.\n- Lần lượt lấy các hệ số: $x=2, y=-3, z=5$.\n- **Kết luận:** Tọa độ $\\vec{u} = (2; -3; 5)$."
                    },
                    {
                        "title": "Ví dụ 2: Tọa độ điểm chiếu vuông góc",
                        "problem": "Tìm tọa độ hình chiếu vuông góc của điểm $M(1; -2; 4)$ lên mặt phẳng tọa độ $(Oxy)$.",
                        "solution": "- Quy tắc chiếu: Chiếu lên mặt phẳng $(Oxy)$ thì tọa độ $z$ sẽ bị triệt tiêu (bằng 0), còn $x$ và $y$ giữ nguyên.\n- Giữ nguyên: $x = 1, y = -2$. Cho $z = 0$.\n- **Kết luận:** Hình chiếu là $M'(1; -2; 0)$."
                    },
                    {
                        "title": "Ví dụ 3: Tọa độ trung điểm của đoạn thẳng",
                        "problem": "Cho hai điểm $A(1; 2; 3)$ và $B(3; 0; 1)$. Tìm tọa độ trung điểm $I$ của đoạn thẳng $AB$.",
                        "solution": "- Công thức trung điểm: $x_I = \\frac{x_A + x_B}{2} = \\frac{1+3}{2} = 2$.\n- $y_I = \\frac{2+0}{2} = 1$.\n- $z_I = \\frac{3+1}{2} = 2$.\n- **Kết luận:** Tọa độ trung điểm là $I(2; 1; 2)$."
                    }
                ],
                "exercise": {
                    "id": "12_7_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Hình chiếu vuông góc của điểm M(5; -1; 3) lên trục Oz có cao độ z bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "3", 
                    "options": []
                }
            }
        }
    }
})
# ==============================================================================
# DATA_GRADE12.PY - HỌC LIỆU TOÁN 12 KẾT NỐI TRI THỨC (PHẦN 3: BÀI 14 -> BÀI 19)
# ==============================================================================

# ==============================================================================
# DATA_GRADE12.PY - HỌC LIỆU TOÁN 12 KẾT NỐI TRI THỨC (PHẦN 2: BÀI 8 -> BÀI 13)
# ==============================================================================

GRADE_12_DATA.update({
    "Bài 8: Biểu thức tọa độ của các phép toán vectơ": {
        "chapter": "Chương II: Vectơ và Hệ tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Các phép toán cộng, trừ, nhân vectơ với một số": {
                "theory": "Trong hệ không gian Oxyz, cộng (hoặc trừ) hai vectơ là cộng (hoặc trừ) các tọa độ tương ứng. Nhân một số với một vectơ là nhân số đó vào từng tọa độ của vectơ. Tọa độ của vectơ $\\vec{AB}$ bằng tọa độ điểm B trừ điểm A.",
                "formula": r"\vec{a} \pm \vec{b} = (x_a \pm x_b; \ y_a \pm y_b; \ z_a \pm z_b); \quad \vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A)",
                "trap": "Học sinh rất hay tính sai tọa độ vectơ $\\vec{AB}$ vì lấy tọa độ điểm A trừ điểm B. Quy tắc đúng luôn là: Điểm cuối trừ điểm đầu.",
                "audio": "Để tính tọa độ vectơ AB, hãy lấy tọa độ điểm B trừ đi điểm A. Các phép toán cộng trừ vectơ thực hiện trên từng trục tọa độ tương ứng.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tổng và hiệu hai vectơ",
                        "problem": "Trong không gian Oxyz, cho $\\vec{a} = (1; 2; -3)$ và $\\vec{b} = (2; -1; 5)$. Tìm tọa độ của vectơ $\\vec{u} = \\vec{a} + \\vec{b}$ và $\\vec{v} = 2\\vec{a}$.",
                        "solution": "- Tính $\\vec{u} = \\vec{a} + \\vec{b} = (1+2; \ 2 + (-1); \ -3 + 5) = (3; 1; 2)$.\n- Tính $\\vec{v} = 2\\vec{a} = (2 \\cdot 1; \ 2 \\cdot 2; \ 2 \\cdot (-3)) = (2; 4; -6)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính tọa độ vectơ từ hai điểm",
                        "problem": "Cho hai điểm $A(1; 0; -2)$ và $B(4; -3; 1)$. Tìm tọa độ của vectơ $\\vec{AB}$.",
                        "solution": "- Áp dụng công thức ngọn trừ gốc:\n  $x_{AB} = 4 - 1 = 3$\n  $y_{AB} = -3 - 0 = -3$\n  $z_{AB} = 1 - (-2) = 3$\n- **Kết luận:** $\\vec{AB} = (3; -3; 3)$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định trung điểm đoạn thẳng",
                        "problem": "Cho hai điểm $M(2; 4; 6)$ và $N(4; 0; -2)$. Tìm tọa độ trung điểm $I$ của đoạn $MN$.",
                        "solution": "- Hoành độ: $x_I = \\frac{2+4}{2} = 3$.\n- Tung độ: $y_I = \\frac{4+0}{2} = 2$.\n- Cao độ: $z_I = \\frac{6 + (-2)}{2} = 2$.\n- **Kết luận:** Tọa độ trung điểm $I(3; 2; 2)$."
                    }
                ],
                "exercise": {
                    "id": "12_8_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Cho a = (1; 2; 3) và b = (-1; 0; 2). Vectơ tổng a + b có cao độ z bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tích vô hướng, độ dài vectơ và góc": {
                "theory": "Tích vô hướng của hai vectơ là tổng của ba tích các tọa độ tương ứng. Từ tích vô hướng, ta có thể tính được độ dài của một vectơ, khoảng cách giữa hai điểm và côsin góc tạo bởi hai vectơ.",
                "formula": r"\vec{u} \cdot \vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2; \quad |\vec{u}| = \sqrt{x^2 + y^2 + z^2}",
                "trap": "Rất nhiều học sinh nhầm lẫn tích vô hướng là một vectơ. Khẳng định lại: Tích vô hướng luôn luôn cho ra một hằng số thực.",
                "audio": "Tích vô hướng bằng hoành nhân hoành, cộng tung nhân tung, cộng cao nhân cao. Hai vectơ vuông góc với nhau thì tích vô hướng bằng 0.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tích vô hướng và độ dài vectơ",
                        "problem": "Cho $\\vec{u} = (2; -1; 3)$ và $\\vec{v} = (1; 4; -2)$. Tính tích vô hướng $\\vec{u} \\cdot \\vec{v}$ và độ dài $|\\vec{u}|$.",
                        "solution": "- Tích vô hướng: $\\vec{u} \\cdot \\vec{v} = 2(1) + (-1)4 + 3(-2) = 2 - 4 - 6 = -8$.\n- Độ dài vectơ $\\vec{u}$: $|\\vec{u}| = \\sqrt{2^2 + (-1)^2 + 3^2} = \\sqrt{4 + 1 + 9} = \\sqrt{14}$."
                    },
                    {
                        "title": "Ví dụ 2: Tính khoảng cách giữa hai điểm",
                        "problem": "Tính khoảng cách giữa hai điểm $A(1; 1; 1)$ và $B(3; -1; 2)$.",
                        "solution": "- Khoảng cách chính là độ dài vectơ $\\vec{AB}$.\n- Tọa độ $\\vec{AB} = (2; -2; 1)$.\n- Khoảng cách $AB = \\sqrt{2^2 + (-2)^2 + 1^2} = \\sqrt{4+4+1} = \\sqrt{9} = 3$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định hai vectơ vuông góc",
                        "problem": "Vectơ $\\vec{a} = (1; 2; 1)$ và $\\vec{b} = (-2; 1; 0)$ có vuông góc với nhau không?",
                        "solution": "- Tính tích vô hướng: $\\vec{a} \\cdot \\vec{b} = 1(-2) + 2(1) + 1(0) = -2 + 2 + 0 = 0$.\n- Vì tích vô hướng bằng 0 nên hai vectơ vuông góc với nhau."
                    }
                ],
                "exercise": {
                    "id": "12_8_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Độ dài của vectơ a = (2; -3; 6) bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "7", 
                    "options": []
                }
            }
        }
    },
    "Bài 9: Khoảng biến thiên và khoảng tứ phân vị": {
        "chapter": "Chương III: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "topics": {
            "Chủ điểm 1: Khoảng biến thiên của mẫu ghép nhóm": {
                "theory": "Khoảng biến thiên (R) của mẫu số liệu ghép nhóm là hiệu số giữa đầu mút phải của nhóm cuối cùng và đầu mút trái của nhóm đầu tiên chứa dữ liệu. Số này đo lường độ phân tán lớn nhất của dữ liệu.",
                "formula": r"R = a_{k+1} - a_1",
                "trap": "Học sinh thường lấy trung điểm (giá trị đại diện) của nhóm cuối trừ nhóm đầu. Phải lấy ĐẦU MÚT.",
                "audio": "Để tính khoảng biến thiên của mẫu ghép nhóm, em lấy giới hạn trên của nhóm cuối cùng trừ đi giới hạn dưới của nhóm đầu tiên.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng biến thiên",
                        "problem": "Cho mẫu số liệu ghép nhóm về thời gian chạy có nhóm đầu tiên là $[10; 15)$ và nhóm cuối cùng là $[30; 35)$. Tính khoảng biến thiên.",
                        "solution": "- Đầu mút trái của nhóm đầu tiên $a_1 = 10$.\n- Đầu mút phải của nhóm cuối cùng $a_{k+1} = 35$.\n- Khoảng biến thiên $R = 35 - 10 = 25$."
                    },
                    {
                        "title": "Ví dụ 2: Ứng dụng so sánh",
                        "problem": "Tổ A có khoảng biến thiên điểm số là $R_A = 4$, tổ B có $R_B = 2.5$. Tổ nào có điểm số phân tán rộng hơn?",
                        "solution": "- Khoảng biến thiên càng lớn thì độ phân tán của số liệu càng rộng.\n- Vì $R_A > R_B$ nên điểm số của tổ A phân tán (không đồng đều) rộng hơn tổ B."
                    }
                ],
                "exercise": {
                    "id": "12_9_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nhóm đầu là [20; 30), nhóm cuối là [70; 80). Khoảng biến thiên R bằng:", 
                    "type": "NUMERIC", 
                    "target": "60", 
                    "options": []
                }
            },
            "Chủ điểm 2: Khoảng tứ phân vị của mẫu ghép nhóm": {
                "theory": "Khoảng tứ phân vị ($\\Delta_Q$) là hiệu số giữa Tứ phân vị thứ ba ($Q_3$) và Tứ phân vị thứ nhất ($Q_1$). Nó đo lường độ phân tán của $50\\%$ số liệu nằm ở trung tâm, không bị ảnh hưởng bởi các giá trị quá lớn hoặc quá nhỏ.",
                "formula": r"\Delta_Q = Q_3 - Q_1; \quad Q_p = u_m + \frac{\frac{p \cdot n}{4} - C}{n_m} \cdot h",
                "trap": "Tính sai tần số tích lũy $C$ (tần số tích lũy của các nhóm TRƯỚC nhóm chứa tứ phân vị) dẫn đến kết quả sai hoàn toàn.",
                "audio": "Khoảng tứ phân vị bằng Q3 trừ Q1. Ưu điểm lớn nhất của nó là không bị nhiễu bởi các số liệu đột biến ở hai đầu.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng tứ phân vị khi đã biết Q1, Q3",
                        "problem": "Một mẫu số liệu tính được $Q_1 = 12.5$ và $Q_3 = 18.2$. Tính khoảng tứ phân vị.",
                        "solution": "- Áp dụng công thức định nghĩa:\n  $\\Delta_Q = Q_3 - Q_1 = 18.2 - 12.5 = 5.7$."
                    },
                    {
                        "title": "Ví dụ 2: Lựa chọn đại lượng đo độ phân tán",
                        "problem": "Khi trong mẫu số liệu xuất hiện một vài giá trị bất thường (quá lớn hoặc quá nhỏ), ta nên dùng Khoảng biến thiên hay Khoảng tứ phân vị để đo độ phân tán?",
                        "solution": "- Khoảng biến thiên $R$ sử dụng giá trị ở 2 đầu mút nên bị ảnh hưởng rất mạnh bởi giá trị bất thường.\n- Khoảng tứ phân vị $\\Delta_Q$ chỉ đo ở đoạn giữa nên ổn định hơn.\n- **Kết luận:** Nên dùng Khoảng tứ phân vị."
                    }
                ],
                "exercise": {
                    "id": "12_9_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu mẫu số liệu có Q1 = 45 và Q3 = 60.5 thì khoảng tứ phân vị bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "15.5", 
                    "options": []
                }
            }
        }
    },
    "Bài 10: Phương sai và độ lệch chuẩn": {
        "chapter": "Chương III: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "topics": {
            "Chủ điểm 1: Tính phương sai và độ lệch chuẩn": {
                "theory": "Phương sai ($s^2$) đo lường sự phân tán của các số liệu xung quanh số trung bình. Độ lệch chuẩn ($s$) bằng căn bậc hai của phương sai, nó cùng đơn vị với dữ liệu gốc nên dễ hình dung hơn.",
                "formula": r"s^2 = \frac{1}{n}\sum_{i=1}^k n_i c_i^2 - (\overline{x})^2; \quad s = \sqrt{s^2}",
                "trap": "Bước tính phương sai rất dài, học sinh thường quên trừ đi bình phương số trung bình $(\\overline{x})^2$ ở cuối công thức.",
                "audio": "Phương sai bằng trung bình cộng các bình phương trừ đi bình phương của số trung bình. Độ lệch chuẩn là căn bậc hai của phương sai.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Mối quan hệ giữa phương sai và độ lệch chuẩn",
                        "problem": "Biết phương sai của một mẫu số liệu ghép nhóm là $s^2 = 16$. Tính độ lệch chuẩn của mẫu số liệu đó.",
                        "solution": "- Độ lệch chuẩn là căn bậc hai số học của phương sai.\n- $s = \\sqrt{s^2} = \\sqrt{16} = 4$."
                    },
                    {
                        "title": "Ví dụ 2: Ý nghĩa của độ lệch chuẩn",
                        "problem": "Hai học sinh A và B có cùng điểm trung bình môn Toán là 7.0. Độ lệch chuẩn điểm số của A là 0.5, của B là 1.8. Nhận xét về sức học của hai bạn.",
                        "solution": "- Độ lệch chuẩn càng nhỏ thì số liệu càng tập trung đều đặn quanh số trung bình.\n- Vì $s_A < s_B$ (0.5 < 1.8) nên phong độ học tập của bạn A ổn định và đồng đều hơn bạn B."
                    },
                    {
                        "title": "Ví dụ 3: Xác định giá trị đại diện",
                        "problem": "Trong công thức tính phương sai, $c_i$ là gì? Tìm $c_i$ của nhóm $[20; 30)$.",
                        "solution": "- $c_i$ là giá trị đại diện của nhóm, được tính bằng trung bình cộng của 2 đầu mút.\n- Nhóm $[20; 30)$ có $c_i = \\frac{20 + 30}{2} = 25$."
                    }
                ],
                "exercise": {
                    "id": "12_10_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Một mẫu số liệu có phương sai bằng 25. Độ lệch chuẩn của mẫu đó bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            }
        }
    },
    "Bài 11: Nguyên hàm": {
        "chapter": "Chương IV: Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Khái niệm và tính chất nguyên hàm": {
                "theory": "Hàm số $F(x)$ là nguyên hàm của $f(x)$ nếu $F'(x) = f(x)$. Họ tất cả các nguyên hàm ký hiệu là $\\int f(x)dx = F(x) + C$. Nguyên hàm của một tổng/hiệu bằng tổng/hiệu các nguyên hàm, hằng số được đưa ra ngoài dấu tích phân.",
                "formula": r"\int f(x)dx = F(x) + C \iff F'(x) = f(x)",
                "trap": "Học sinh thường quên cộng thêm hằng số $C$ vào kết quả cuối cùng. Ký hiệu $\\int f(x)dx$ là một HỌ hàm số, không phải 1 hàm duy nhất.",
                "audio": "Nguyên hàm là bài toán ngược của đạo hàm. Tìm nguyên hàm tức là đi tìm một hàm số mà khi đạo hàm nó, ta được biểu thức ban đầu. Nhớ cộng thêm hằng số C nhé.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Kiểm tra nguyên hàm bằng đạo hàm",
                        "problem": "Hàm số $F(x) = x^3 + 2x$ có phải là một nguyên hàm của hàm số $f(x) = 3x^2 + 2$ không?",
                        "solution": "- Ta tính đạo hàm của $F(x)$:\n  $F'(x) = (x^3 + 2x)' = 3x^2 + 2$.\n- Vì $F'(x) = f(x)$ nên $F(x)$ chính là một nguyên hàm của $f(x)$."
                    },
                    {
                        "title": "Ví dụ 2: Tính nguyên hàm tổng hợp cơ bản",
                        "problem": "Tìm họ nguyên hàm của hàm số $f(x) = 4x^3 - 2x$.",
                        "solution": "- Áp dụng công thức nguyên hàm đa thức:\n  $\\int (4x^3 - 2x) dx = 4 \\cdot \\frac{x^4}{4} - 2 \\cdot \\frac{x^2}{2} + C = x^4 - x^2 + C$."
                    },
                    {
                        "title": "Ví dụ 3: Tìm hằng số C khi biết điều kiện",
                        "problem": "Cho $F(x)$ là một nguyên hàm của $f(x) = 2x$ và $F(1) = 4$. Tìm $F(x)$.",
                        "solution": "- Ta có $\\int 2x dx = x^2 + C \\implies F(x) = x^2 + C$.\n- Thay $x = 1$: $F(1) = 1^2 + C = 1 + C$.\n- Theo đề $F(1) = 4 \\implies 1 + C = 4 \\implies C = 3$.\n- **Kết luận:** $F(x) = x^2 + 3$."
                    }
                ],
                "exercise": {
                    "id": "12_11_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nguyên hàm của f(x) = 2x là F(x) = x^2 + C. Nếu F(0) = 5 thì giá trị của C bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 2: Bảng nguyên hàm của các hàm số sơ cấp": {
                "theory": "Sử dụng trực tiếp bảng nguyên hàm cơ bản để tính toán: Hàm đa thức, phân thức cơ bản, hàm mũ, hàm lượng giác.",
                "formula": r"\int x^\alpha dx = \frac{x^{\alpha+1}}{\alpha+1} + C \ (\alpha \neq -1); \quad \int \frac{1}{x} dx = \ln|x| + C; \quad \int \sin x dx = -\cos x + C",
                "trap": "Nguyên hàm của $\\sin x$ là $-\\cos x$ (có dấu trừ), rất hay nhầm với đạo hàm của $\\sin x$ là $\\cos x$. Nguyên hàm của $1/x$ là $\\ln|x|$ bắt buộc phải có dấu giá trị tuyệt đối.",
                "audio": "Bảng nguyên hàm là vũ khí bắt buộc phải thuộc. Hãy lưu ý sự ngược dấu của hàm lượng giác so với đạo hàm.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nguyên hàm của hàm phân thức 1/x",
                        "problem": "Tìm nguyên hàm $\\int \\frac{3}{x} dx$.",
                        "solution": "- Đưa hằng số ra ngoài: $3 \\int \\frac{1}{x} dx$.\n- Áp dụng công thức cơ bản: $3 \\ln|x| + C$."
                    },
                    {
                        "title": "Ví dụ 2: Nguyên hàm lượng giác",
                        "problem": "Tìm họ nguyên hàm của $f(x) = \\cos x - \\sin x$.",
                        "solution": "- Ta có $\\int \\cos x dx = \\sin x + C_1$.\n- $\\int \\sin x dx = -\\cos x + C_2$.\n- Vậy $\\int (\\cos x - \\sin x) dx = \\sin x - (-\\cos x) + C = \\sin x + \\cos x + C$."
                    },
                    {
                        "title": "Ví dụ 3: Nguyên hàm hàm số mũ e^x",
                        "problem": "Tìm nguyên hàm của hàm số $f(x) = e^x + 1$.",
                        "solution": "- Áp dụng: $\\int e^x dx = e^x + C$ và $\\int 1 dx = x + C$.\n- Vậy $\\int (e^x + 1) dx = e^x + x + C$."
                    }
                ],
                "exercise": {
                    "id": "12_11_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị của f(x) sao cho nguyên hàm của nó là F(x) = e^x + x. f(0) bằng:", 
                    "type": "NUMERIC", 
                    "target": "2", 
                    "options": []
                }
            }
        }
    },
    "Bài 12: Tích phân": {
        "chapter": "Chương IV: Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Định nghĩa và Định lý Newton-Leibniz": {
                "theory": "Tích phân xác định từ $a$ đến $b$ của $f(x)$ bằng giá trị nguyên hàm tại cận trên trừ đi giá trị nguyên hàm tại cận dưới. Giá trị của tích phân chỉ phụ thuộc vào hàm $f$ và các cận $a, b$, KHÔNG phụ thuộc vào ký hiệu biến số ($x, t, u...$).",
                "formula": r"\int_a^b f(x)dx = F(b) - F(a) = F(x)\Big|_a^b",
                "trap": "Học sinh thường hấp tấp tính sai dấu khi lấy cận trên trừ cận dưới, hoặc thay cận dưới trừ cận trên làm đảo ngược kết quả.",
                "audio": "Tích phân từ a đến b bằng F của b trừ F của a, trong đó F lớn là nguyên hàm. Nhớ luôn lấy cận trên trừ cận dưới.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính tích phân cơ bản",
                        "problem": "Tính tích phân $I = \\int_1^2 3x^2 dx$.",
                        "solution": "- Nguyên hàm của $3x^2$ là $x^3$.\n- Thay cận Newton-Leibniz: $I = x^3 \\Big|_1^2 = 2^3 - 1^3 = 8 - 1 = 7$."
                    },
                    {
                        "title": "Ví dụ 2: Tính không phụ thuộc biến số",
                        "problem": "Biết $\\int_0^1 f(x) dx = 5$. Tính $K = \\int_0^1 f(t) dt$.",
                        "solution": "- Theo tính chất tích phân không phụ thuộc biến số, $\\int_0^1 f(t) dt = \\int_0^1 f(x) dx$.\n- Vậy $K = 5$."
                    },
                    {
                        "title": "Ví dụ 3: Đảo cận tích phân",
                        "problem": "Tính $J = \\int_2^1 3x^2 dx$.",
                        "solution": "- Đảo cận thì đổi dấu: $J = - \\int_1^2 3x^2 dx$.\n- Theo kết quả ví dụ 1, $J = -7$."
                    }
                ],
                "exercise": {
                    "id": "12_12_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Tích phân từ 0 đến 2 của (2x + 1) dx bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "6", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tính chất của Tích phân": {
                "theory": "Tính chất tuyến tính: Tích phân của một tổng/hiệu bằng tổng/hiệu các tích phân. Có thể đưa hằng số k ra ngoài. Tính chất nối cận (Chasles): Tích phân từ a đến c bằng tổng tích phân từ a đến b và từ b đến c.",
                "formula": r"\int_a^c f(x)dx = \int_a^b f(x)dx + \int_b^c f(x)dx; \quad \int [f(x) \pm g(x)]dx = \int f(x)dx \pm \int g(x)dx",
                "trap": "Rất nhiều học sinh sai lầm cho rằng tích phân của một tích bằng tích các tích phân. Tuyệt đối không có tính chất này.",
                "audio": "Tích phân có thể tách tổng, hiệu và đưa hệ số ra ngoài. Đặc biệt tính chất nối cận rất hay gặp trong đề thi.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính chất tuyến tính",
                        "problem": "Biết $\\int_0^1 f(x) dx = 3$ và $\\int_0^1 g(x) dx = -2$. Tính $I = \\int_0^1 [2f(x) - g(x)] dx$.",
                        "solution": "- Tách tích phân: $I = 2\\int_0^1 f(x) dx - \\int_0^1 g(x) dx$.\n- Thay số: $I = 2(3) - (-2) = 6 + 2 = 8$."
                    },
                    {
                        "title": "Ví dụ 2: Tính chất nối cận (Chèn điểm)",
                        "problem": "Cho $\\int_1^2 f(x) dx = 4$ và $\\int_2^5 f(x) dx = 6$. Tính $J = \\int_1^5 f(x) dx$.",
                        "solution": "- Áp dụng nối cận: $\\int_1^5 f(x) dx = \\int_1^2 f(x) dx + \\int_2^5 f(x) dx$.\n- Tính toán: $J = 4 + 6 = 10$."
                    },
                    {
                        "title": "Ví dụ 3: Nối cận chiều ngược",
                        "problem": "Cho $\\int_0^3 f(x) dx = 10$ và $\\int_1^3 f(x) dx = 4$. Tính $\\int_0^1 f(x) dx$.",
                        "solution": "- Ta có $\\int_0^3 f(x) dx = \\int_0^1 f(x) dx + \\int_1^3 f(x) dx$.\n- Suy ra $\\int_0^1 f(x) dx = 10 - 4 = 6$."
                    }
                ],
                "exercise": {
                    "id": "12_12_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Nếu tích phân từ 1 đến 2 của f(x) bằng 5 và từ 2 đến 4 của f(x) bằng -1. Thì tích phân từ 1 đến 4 bằng:", 
                    "type": "NUMERIC", 
                    "target": "4", 
                    "options": []
                }
            },
            "Chủ điểm 3: Phương pháp đổi biến số": {
                "theory": "Khi đặt biến số mới $u = u(x)$, ta phải thực hiện 2 việc bắt buộc: (1) Tính vi phân $du = u'(x)dx$ để thay thế. (2) Đổi cận tương ứng với biến $u$.",
                "formula": r"\int_a^b f[u(x)]u'(x)dx = \int_{u(a)}^{u(b)} f(u)du",
                "trap": "Bước đổi cận là nơi thí sinh mất điểm nhiều nhất vì quên thực hiện, dẫn đến thay luôn cận cũ của x vào hàm biến u.",
                "audio": "Đổi biến số là kỹ thuật quan trọng nhất. Cứ hễ đặt ẩn phụ u, việc đầu tiên em phải làm là đổi cận.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm cận mới khi đổi biến",
                        "problem": "Xét tích phân $\\int_0^1 (2x + 1)^3 dx$. Đặt $u = 2x + 1$, hãy xác định cận mới của tích phân theo $u$.",
                        "solution": "- Cận dưới: $x = 0 \\implies u = 2(0) + 1 = 1$.\n- Cận trên: $x = 1 \\implies u = 2(1) + 1 = 3$.\n- Vậy cận mới là từ 1 đến 3."
                    },
                    {
                        "title": "Ví dụ 2: Vi phân",
                        "problem": "Đặt $u = x^2 + 1$. Biểu diễn $xdx$ theo $du$.",
                        "solution": "- Đạo hàm hai vế lấy vi phân: $du = 2x dx$.\n- Suy ra: $xdx = \\frac{1}{2} du$."
                    },
                    {
                        "title": "Ví dụ 3: Đổi biến hoàn chỉnh",
                        "problem": "Tính $I = \\int_0^1 2x(x^2 + 1)^2 dx$.",
                        "solution": "- Đặt $u = x^2 + 1 \\implies du = 2xdx$.\n- Đổi cận: $x=0 \\to u=1; x=1 \\to u=2$.\n- Tích phân mới: $I = \\int_1^2 u^2 du = \\frac{u^3}{3} \\Big|_1^2 = \\frac{8}{3} - \\frac{1}{3} = \\frac{7}{3}$."
                    }
                ],
                "exercise": {
                    "id": "12_12_3", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Đặt u = 3x - 1, khi x = 2 thì giá trị của u bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "5", 
                    "options": []
                }
            },
            "Chủ điểm 4: Phương pháp tích phân từng phần": {
                "theory": "Sử dụng khi hàm dưới dấu tích phân là tích của 2 hàm khác loại (VD: đa thức nhân lượng giác, đa thức nhân mũ, đa thức nhân logarit). Thứ tự ưu tiên đặt $u$: 'Nhất lô (logarit), nhì đa (đa thức), tam lượng (lượng giác), tứ mũ (e^x)'. Đại lượng còn lại là $dv$.",
                "formula": r"\int_a^b u dv = uv\Big|_a^b - \int_a^b v du",
                "trap": "Học sinh hay tính sai dấu âm trong công thức $uv - \\int v du$.",
                "audio": "Tích phân từng phần dùng công thức u nhân v trừ tích phân v du. Nhớ quy tắc đặt u: Nhất lô, nhì đa, tam lượng, tứ mũ.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Nhận dạng đại lượng u",
                        "problem": "Để tính tích phân $\\int_1^e x \\ln x dx$, theo thứ tự ưu tiên, ta đặt $u$ và $dv$ là gì?",
                        "solution": "- Quy tắc 'Nhất lô, nhì đa': Hàm logarit ($\\ln x$) ưu tiên cao hơn hàm đa thức ($x$).\n- Vậy ta đặt $u = \\ln x$ và $dv = x dx$."
                    },
                    {
                        "title": "Ví dụ 2: Tính các thành phần u, v",
                        "problem": "Cho $u = x$ và $dv = e^x dx$. Tính $du$ và $v$.",
                        "solution": "- $du = dx$ (lấy đạo hàm của x).\n- $v = \\int e^x dx = e^x$ (lấy một nguyên hàm của e^x)."
                    },
                    {
                        "title": "Ví dụ 3: Hoàn thiện công thức",
                        "problem": "Tính $I = \\int_0^1 x e^x dx$.",
                        "solution": "- Đặt $u=x, dv=e^x dx \\implies du=dx, v=e^x$.\n- Áp dụng: $I = x e^x \\Big|_0^1 - \\int_0^1 e^x dx = (1 \\cdot e^1 - 0) - e^x \\Big|_0^1$.\n- $I = e - (e^1 - e^0) = e - e + 1 = 1$."
                    }
                ],
                "exercise": {
                    "id": "12_12_4", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Giá trị của tích phân từ 0 đến 1 của x.e^x dx bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    },
    "Bài 13: Ứng dụng hình học của tích phân": {
        "chapter": "Chương IV: Nguyên hàm và tích phân",
        "topics": {
            "Chủ điểm 1: Tính diện tích hình phẳng": {
                "theory": "Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f(x)$, trục hoành $y = 0$, và hai đường thẳng $x = a, x = b$ được tính bằng tích phân của trị tuyệt đối $|f(x)|$. Nếu giới hạn bởi 2 đường cong $f(x)$ và $g(x)$ thì ta dùng $|f(x) - g(x)|$.",
                "formula": r"S = \int_a^b |f(x)| dx; \quad S = \int_a^b |f(x) - g(x)| dx",
                "trap": "Bỏ quên dấu giá trị tuyệt đối $|...|$ dẫn đến kết quả diện tích mang dấu âm vô lý. Diện tích là đại lượng luôn dương.",
                "audio": "Diện tích hình phẳng luôn phải có dấu giá trị tuyệt đối bên trong tích phân. Lấy hàm trên trừ hàm dưới hoặc xét dấu cẩn thận.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Diện tích cơ bản (hàm số nằm trên trục hoành)",
                        "problem": "Tính diện tích hình phẳng giới hạn bởi parabol $y = x^2$, trục hoành $y = 0$ và các đường $x = 0, x = 1$.",
                        "solution": "- Vì $x^2 \\ge 0$ trên đoạn $[0; 1]$ nên $|x^2| = x^2$.\n- $S = \\int_0^1 x^2 dx = \\frac{x^3}{3} \\Big|_0^1 = \\frac{1}{3} - 0 = \\frac{1}{3}$."
                    },
                    {
                        "title": "Ví dụ 2: Diện tích khi hàm số mang dấu âm",
                        "problem": "Tính diện tích hình phẳng giới hạn bởi đường thẳng $y = -2x$, trục hoành và hai đường $x = 1, x = 2$.",
                        "solution": "- Trên đoạn $[1; 2]$, hàm $y = -2x$ mang giá trị âm. Do đó $|-2x| = 2x$.\n- $S = \\int_1^2 2x dx = x^2 \\Big|_1^2 = 4 - 1 = 3$."
                    },
                    {
                        "title": "Ví dụ 3: Diện tích giới hạn bởi hai đồ thị",
                        "problem": "Thiết lập công thức tính diện tích hình phẳng giới hạn bởi $y = x^2$ và $y = x$ trên đoạn $[0; 1]$.",
                        "solution": "- Ta xét hiệu: $S = \\int_0^1 |x - x^2| dx$.\n- Vì trên đoạn $[0; 1]$, đồ thị $y = x$ nằm trên $y = x^2$ (tức là $x \\ge x^2$), nên $|x - x^2| = x - x^2$.\n- $S = \\int_0^1 (x - x^2) dx$."
                    }
                ],
                "exercise": {
                    "id": "12_13_1", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Diện tích hình phẳng giới hạn bởi y = 3x^2, Ox, x=0, x=1 bằng bao nhiêu?", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            },
            "Chủ điểm 2: Tính thể tích khối tròn xoay": {
                "theory": "Khi quay hình phẳng giới hạn bởi $y = f(x)$, trục $Ox$, $x = a, x = b$ xung quanh trục $Ox$, ta được một khối tròn xoay. Thể tích khối này bằng $\\pi$ nhân với tích phân của BÌNH PHƯƠNG hàm số $f(x)$.",
                "formula": r"V = \pi \int_a^b [f(x)]^2 dx",
                "trap": "Sai lầm kinh điển nhất: Quên nhân với số $\\pi$ trước tích phân, hoặc quên bình phương hàm số $[f(x)]^2$.",
                "audio": "Thể tích tròn xoay luôn có mặt số Pi nhân với tích phân của bình phương hàm số. Đừng bao giờ quên số Pi nhé.",
                "svg": "TICH_PHAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Thể tích khối nón tạo từ tam giác quay",
                        "problem": "Tính thể tích khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi $y = x$, $y = 0$, $x = 0$, $x = 2$ quanh trục Ox.",
                        "solution": "- Áp dụng công thức $V = \\pi \\int_a^b [f(x)]^2 dx$.\n- $V = \\pi \\int_0^2 x^2 dx = \\pi \\left[ \\frac{x^3}{3} \\right]_0^2 = \\frac{8\\pi}{3}$."
                    },
                    {
                        "title": "Ví dụ 2: Thể tích khối tạo từ đường cong căn thức",
                        "problem": "Quay hình phẳng giới hạn bởi $y = \\sqrt{x}$, $Ox, x = 1, x = 4$ quanh $Ox$. Khối tròn xoay tạo thành có thể tích dạng $V = c \\cdot \\pi$. Tìm c.",
                        "solution": "- Ta có $f(x) = \\sqrt{x} \\implies [f(x)]^2 = x$.\n- $V = \\pi \\int_1^4 x dx = \\pi \\left[ \\frac{x^2}{2} \\right]_1^4 = \\pi \\left( \\frac{16}{2} - \\frac{1}{2} \\right) = \\frac{15\\pi}{2}$.\n- Vậy $c = \\frac{15}{2} = 7.5$."
                    },
                    {
                        "title": "Ví dụ 3: Nhận dạng sai lầm công thức",
                        "problem": "Một học sinh tính thể tích vật tròn xoay sinh bởi $y = x+1, Ox, x=0, x=1$ bằng công thức $V = \\int_0^1 (x+1)^2 dx$. Học sinh này sai ở đâu?",
                        "solution": "- Công thức thể tích khối tròn xoay quanh trục hoành bắt buộc phải có hằng số $\\pi$.\n- Học sinh đã thiếu $\\pi$. Công thức đúng phải là $V = \\pi \\int_0^1 (x+1)^2 dx$."
                    }
                ],
                "exercise": {
                    "id": "12_13_2", 
                    "title": "Bài tập tự luyện kiểm minh chứng", 
                    "content": "Quay y = căn(2x) quanh Ox (x từ 0 đến 1) được thể tích V = c * pi. Tính c:", 
                    "type": "NUMERIC", 
                    "target": "1", 
                    "options": []
                }
            }
        }
    }
})
GRADE_12_DATA.update({
    "Bài 14: Phương trình mặt phẳng": {
        "chapter": "Chương V: Phương pháp tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Vectơ pháp tuyến và Cặp VTCP": {
                "theory": "Vectơ $\\vec{n} \\neq \\vec{0}$ có giá vuông góc với mặt phẳng là vectơ pháp tuyến (VTPT). Nếu biết cặp vectơ chỉ phương $\\vec{a}, \\vec{b}$ không cùng phương, ta tìm được VTPT qua tích có hướng $\\vec{n} = [\\vec{a}, \\vec{b}]$.",
                "formula": r"\vec{n} \perp (\alpha) \iff \vec{n} \cdot \vec{u} = 0; \quad \vec{n} = [\vec{a}, \vec{b}]",
                "trap": "Hai vectơ chỉ phương bắt buộc phải không cùng phương thì tích có hướng mới khác vectơ không.",
                "audio": "Vectơ pháp tuyến vuông góc với mặt phẳng. Tích có hướng của hai vectơ chỉ phương không cùng phương sẽ tạo ra một vectơ pháp tuyến.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm VTPT từ cặp vectơ chỉ phương",
                        "problem": "Tìm một VTPT của mặt phẳng chứa hai VTCP $\\vec{a}=(1; 2; -1)$ và $\\vec{b}=(0; 3; 2)$.",
                        "solution": "- Tính tích có hướng $\\vec{n} = [\\vec{a}, \\vec{b}]$.\n- Hoành độ: $2(2) - (-1)3 = 7$.\n- Tung độ: $(-1)0 - 1(2) = -2$.\n- Cao độ: $1(3) - 2(0) = 3$.\n- **Kết luận:** $\\vec{n} = (7; -2; 3)$."
                    },
                    {
                        "title": "Ví dụ 2: VTPT của mặt phẳng qua 3 điểm",
                        "problem": "Cho 3 điểm $A(1;0;0), B(0;2;0), C(0;0;3)$. Tìm VTPT của mặt phẳng $(ABC)$.",
                        "solution": "- $\\vec{AB} = (-1; 2; 0)$ và $\\vec{AC} = (-1; 0; 3)$.\n- $\\vec{n} = [\\vec{AB}, \\vec{AC}] = (6; 3; 2)$."
                    },
                    {
                        "title": "Ví dụ 3: Xác định VTPT từ phương trình tổng quát",
                        "problem": "Xác định VTPT của mặt phẳng $(P): 3x - 4y + 5 = 0$.",
                        "solution": "- Hệ số của x, y, z lần lượt là $A=3, B=-4, C=0$ (do không có z).\n- **Kết luận:** VTPT $\\vec{n} = (3; -4; 0)$."
                    }
                ],
                "exercise": {"id": "12_14_1", "title": "Bài tập tự luyện", "content": "Mặt phẳng 3x - 4y + z - 5 = 0 có VTPT n = (3; b; 1). b bằng:", "type": "NUMERIC", "target": "-4", "options": []}
            },
            "Chủ điểm 2: Phương trình tổng quát và đoạn chắn": {
                "theory": "Mặt phẳng đi qua $M_0(x_0; y_0; z_0)$ có VTPT $\\vec{n}=(A; B; C)$ có phương trình $A(x-x_0) + B(y-y_0) + C(z-z_0) = 0$. Mặt phẳng cắt 3 trục tại $(a;0;0), (0;b;0), (0;0;c)$ có phương trình đoạn chắn $\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1$.",
                "formula": r"Ax + By + Cz + D = 0; \quad \frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1",
                "trap": "Cẩn thận nhầm dấu hệ số tự do D khi khai triển phá ngoặc phương trình.",
                "audio": "Phương trình mặt phẳng qua một điểm có dạng A nhân x trừ x không, cộng B nhân y trừ y không, cộng C nhân z trừ z không bằng không.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ 1: Lập PT mặt phẳng",
                        "problem": "Lập PT mặt phẳng qua $M(1;2;-3)$ có VTPT $\\vec{n}=(2;-1;4)$.",
                        "solution": "- Phương trình: $2(x-1) - 1(y-2) + 4(z - (-3)) = 0$.\n- Khai triển: $2x - 2 - y + 2 + 4z + 12 = 0 \\iff 2x - y + 4z + 12 = 0$."
                    },
                    {
                        "title": "Ví dụ 2: Phương trình mặt phẳng trung trực",
                        "problem": "Viết phương trình mặt phẳng trung trực của đoạn $AB$ với $A(2; 0; 0)$ và $B(0; 2; 0)$.",
                        "solution": "- Trung điểm $I(1; 1; 0)$. VTPT là $\\vec{AB} = (-2; 2; 0)$. Rút gọn chọn $\\vec{n} = (1; -1; 0)$.\n- PT qua $I(1;1;0)$ với $\\vec{n}=(1;-1;0)$: $1(x-1) - 1(y-1) + 0 = 0 \\iff x - y = 0$."
                    },
                    {
                        "title": "Ví dụ 3: Phương trình đoạn chắn",
                        "problem": "Viết PT mặt phẳng qua $M(2;0;0), N(0;-3;0), P(0;0;4)$.",
                        "solution": "- Áp dụng PT đoạn chắn: $\\frac{x}{2} + \\frac{y}{-3} + \\frac{z}{4} = 1$."
                    }
                ],
                "exercise": {"id": "12_14_2", "title": "Bài tập tự luyện", "content": "Mặt phẳng trung trực của đoạn A(2;0;0), B(0;2;0) là x - y = c. c bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "Chủ điểm 3: Vị trí tương đối của hai mặt phẳng": {
                "theory": "Hai mặt phẳng song song khi tỉ lệ tọa độ VTPT bằng nhau nhưng hệ số tự do khác nhau. Hai mặt phẳng vuông góc khi tích vô hướng hai VTPT bằng 0.",
                "formula": r"\vec{n}_1 \cdot \vec{n}_2 = 0 \iff (P) \perp (Q); \quad \frac{A_1}{A_2} = \frac{B_1}{B_2} = \frac{C_1}{C_2} \neq \frac{D_1}{D_2} \iff (P) \parallel (Q)",
                "trap": "Hai mặt phẳng song song thì tỉ lệ hệ số tự do D bắt buộc phải khác tỉ lệ các hệ số A, B, C.",
                "audio": "Hai mặt phẳng vuông góc với nhau khi tích vô hướng của hai vectơ pháp tuyến bằng không.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét vuông góc",
                        "problem": "Mặt phẳng $(P): 2x+3y-4z=0$ và $(Q): 3x-2y+5=0$ có vuông góc không?",
                        "solution": "- VTPT $\\vec{n}_P = (2; 3; -4), \\vec{n}_Q = (3; -2; 0)$.\n- Tích vô hướng: $2(3) + 3(-2) + (-4)0 = 6 - 6 = 0$.\n- **Kết luận:** Hai mặt phẳng vuông góc."
                    },
                    {
                        "title": "Ví dụ 2: Tìm m để song song",
                        "problem": "Tìm m để $(P): x + my + z - 2 = 0$ song song $(Q): 2x + 4y + 2z - 5 = 0$.",
                        "solution": "- Lập tỉ lệ: $\\frac{1}{2} = \\frac{m}{4} = \\frac{1}{2} \\neq \\frac{-2}{-5}$.\n- Ta suy ra $m = 2$."
                    },
                    {
                        "title": "Ví dụ 3: MP qua điểm song song MP cho trước",
                        "problem": "Viết PTMP $(\\alpha)$ qua $A(1;1;1)$ song song $(P): x+y+z-5=0$.",
                        "solution": "- $(\\alpha)$ song song $(P)$ nên có VTPT $\\vec{n}=(1;1;1)$.\n- PT: $1(x-1) + 1(y-1) + 1(z-1) = 0 \\iff x+y+z-3=0$."
                    }
                ],
                "exercise": {"id": "12_14_3", "title": "Bài tập tự luyện", "content": "Cho (P): x + 2y + cz - 1 = 0 vuông góc (Q): 2x - y + 3z + 4 = 0. c bằng:", "type": "NUMERIC", "target": "0", "options": []}
            },
            "Chủ điểm 4: Khoảng cách từ một điểm đến mặt phẳng": {
                "theory": "Thay tọa độ điểm vào vế trái phương trình lấy trị tuyệt đối, chia cho độ dài VTPT. Khoảng cách giữa 2 MP song song được tính bằng cách lấy 1 điểm trên MP này tính k/c tới MP kia.",
                "formula": r"d(M_0, (P)) = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}",
                "trap": "Tuyệt đối không được quên dấu giá trị tuyệt đối trên tử số.",
                "audio": "Khoảng cách tính bằng trị tuyệt đối tử số chia cho căn bậc hai tổng bình phương ở mẫu số.",
                "svg": "KHOANG_CACH_MP",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính khoảng cách cơ bản",
                        "problem": "Khoảng cách từ gốc tọa độ $O$ đến $2x - 2y + z - 9 = 0$.",
                        "solution": "- Thay O(0;0;0) vào tử: $|2(0) - 2(0) + 0 - 9| = |-9| = 9$.\n- Mẫu số: $\\sqrt{2^2 + (-2)^2 + 1^2} = 3$.\n- Khoảng cách $d = 9/3 = 3$."
                    },
                    {
                        "title": "Ví dụ 2: Điểm bất kỳ",
                        "problem": "Tính khoảng cách từ $A(1; -2; 3)$ đến $(P): x + 2y - 2z + 4 = 0$.",
                        "solution": "- $d = \\frac{|1 + 2(-2) - 2(3) + 4|}{\\sqrt{1^2 + 2^2 + (-2)^2}} = \\frac{|1 - 4 - 6 + 4|}{\\sqrt{9}} = \\frac{|-5|}{3} = \\frac{5}{3}$."
                    },
                    {
                        "title": "Ví dụ 3: Khoảng cách 2 mặt phẳng song song",
                        "problem": "Tính khoảng cách giữa $(P): x-y+z-1=0$ và $(Q): x-y+z+5=0$.",
                        "solution": "- Chọn điểm $M(1;0;0) \\in (P)$.\n- $d((P),(Q)) = d(M, (Q)) = \\frac{|1 - 0 + 0 + 5|}{\\sqrt{1^2 + (-1)^2 + 1^2}} = \\frac{6}{\\sqrt{3}} = 2\\sqrt{3}$."
                    }
                ],
                "exercise": {"id": "12_14_4", "title": "Bài tập tự luyện", "content": "Khoảng cách từ gốc tọa độ O đến 2x - 2y + z - 9 = 0 bằng:", "type": "NUMERIC", "target": "3", "options": []}
            }
        }
    },
    "Bài 15: Phương trình đường thẳng trong không gian": {
        "chapter": "Chương V: Phương pháp tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: PT tham số và Vectơ chỉ phương": {
                "theory": "Đường thẳng qua điểm $M_0(x_0; y_0; z_0)$ có VTCP $\\vec{u}=(a; b; c)$. Phương trình tham số biểu thị từng tọa độ x, y, z phụ thuộc vào tham số $t$.",
                "formula": r"\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}",
                "trap": "Cần chú ý hệ số gắn với t chính là tọa độ của vectơ chỉ phương.",
                "audio": "Phương trình tham số của đường thẳng gồm ba phương trình nhỏ x, y, z biểu diễn qua tham số t.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết PT tham số",
                        "problem": "Viết PT tham số của đường thẳng qua $M(1; -2; 3)$ có VTCP $\\vec{u} = (2; 0; -1)$.",
                        "solution": "- $x = 1 + 2t$\n- $y = -2$\n- $z = 3 - t$"
                    },
                    {
                        "title": "Ví dụ 2: Lấy điểm và VTCP từ phương trình",
                        "problem": "Cho đường thẳng d: $x=2-t, y=1+3t, z=4$. Xác định 1 điểm đi qua và VTCP.",
                        "solution": "- Điểm đi qua (lấy hệ số tự do): $M(2; 1; 4)$.\n- VTCP (lấy hệ số của t): $\\vec{u} = (-1; 3; 0)$."
                    },
                    {
                        "title": "Ví dụ 3: PT đường thẳng qua 2 điểm",
                        "problem": "Viết PT tham số của đường thẳng $AB$ với $A(1;1;1)$ và $B(2;3;4)$.",
                        "solution": "- VTCP $\\vec{u} = \\vec{AB} = (1; 2; 3)$.\n- PT: $x=1+t, y=1+2t, z=1+3t$."
                    }
                ],
                "exercise": {"id": "12_15_1", "title": "Bài tập tự luyện", "content": "Đường thẳng x=1+2t có hoành độ vectơ chỉ phương bằng:", "type": "NUMERIC", "target": "2", "options": []}
            },
            "Chủ điểm 2: Phương trình chính tắc": {
                "theory": "Nếu cả 3 tọa độ của VTCP đều khác 0 ($a,b,c \\neq 0$), ta khử tham số $t$ để được phương trình chính tắc.",
                "formula": r"\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}",
                "trap": "Nếu một trong các tọa độ VTCP bằng 0, đường thẳng không có phương trình chính tắc.",
                "audio": "Phương trình chính tắc là dạng ba phân thức bằng nhau. Mẫu số chính là tọa độ của vectơ chỉ phương.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Viết PT chính tắc",
                        "problem": "Viết PT chính tắc đường thẳng qua $M(1; -2; 5)$ có VTCP $\\vec{u}=(2; 3; -4)$.",
                        "solution": "- PT: $\\frac{x - 1}{2} = \\frac{y + 2}{3} = \\frac{z - 5}{-4}$."
                    },
                    {
                        "title": "Ví dụ 2: Lấy thông tin từ PT",
                        "problem": "Đường thẳng $\\frac{x-2}{3} = \\frac{y+1}{-1} = \\frac{z}{2}$ có VTCP là gì?",
                        "solution": "- VTCP lấy ở mẫu số: $\\vec{u} = (3; -1; 2)$."
                    },
                    {
                        "title": "Ví dụ 3: Chuyển tham số sang chính tắc",
                        "problem": "Chuyển đường thẳng $x=1+2t, y=3-t, z=4t$ sang dạng chính tắc.",
                        "solution": "- Rút t: $t = \\frac{x-1}{2} = \\frac{y-3}{-1} = \\frac{z}{4}$."
                    }
                ],
                "exercise": {"id": "12_15_2", "title": "Bài tập tự luyện", "content": "Đường thẳng $\\frac{x-1}{2}=\\frac{y+3}{-1}=\\frac{z}{4}$ có tung độ điểm đi qua là:", "type": "NUMERIC", "target": "-3", "options": []}
            },
            "Chủ điểm 3: Vị trí tương đối hai đường thẳng": {
                "theory": "Dùng tích có hướng của 2 VTCP và vectơ nối 2 điểm thuộc 2 đường thẳng để xét tính đồng phẳng. Nếu không đồng phẳng thì chéo nhau.",
                "formula": r"[\vec{u}_1, \vec{u}_2] \cdot \vec{M_1M_2} \neq 0 \implies \text{Chéo nhau}",
                "trap": "Đừng nhầm lẫn giữa song song (cùng phương, không điểm chung) và chéo nhau (không cùng phương, không điểm chung).",
                "audio": "Để xét chéo nhau, ta kiểm tra xem tích hỗn tạp của hai vectơ chỉ phương và vectơ nối hai điểm có khác không hay không.",
                "svg": "DUONG_THANG_OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xét song song",
                        "problem": "Đường $d_1$: $\\frac{x}{1}=\\frac{y}{2}=\\frac{z}{3}$ và $d_2$: $\\frac{x-1}{2}=\\frac{y-2}{4}=\\frac{z-3}{6}$ có song song không?",
                        "solution": "- VTCP $\\vec{u}_1=(1;2;3)$ và $\\vec{u}_2=(2;4;6)$. Rõ ràng $\\vec{u}_2 = 2\\vec{u}_1$ nên cùng phương.\n- $O(0;0;0) \\in d_1$ nhưng không thuộc $d_2$. Vậy $d_1 \\parallel d_2$."
                    },
                    {
                        "title": "Ví dụ 2: Tìm giao điểm",
                        "problem": "Giao điểm của $d_1: x=t, y=1-t, z=2+t$ và $d_2: x=1+2k, y=k, z=3-k$.",
                        "solution": "- Giải hệ: $t = 1+2k; 1-t = k; 2+t = 3-k$.\n- Thay pt 1 vào pt 2: $1-(1+2k)=k \\implies -2k=k \\implies k=0$.\n- Suy ra $t=1$. Thay vào pt 3 thấy $2+1 = 3-0$ (thỏa mãn).\n- Tọa độ giao điểm $(1; 0; 3)$."
                    },
                    {
                        "title": "Ví dụ 3: Xét tính chéo nhau",
                        "problem": "Hai đường thẳng không có điểm chung và VTCP không cùng phương thì gọi là gì?",
                        "solution": "- Đó là định nghĩa của hai đường thẳng chéo nhau trong không gian."
                    }
                ],
                "exercise": {"id": "12_15_3", "title": "Bài tập tự luyện", "content": "Hai đường thẳng chéo nhau có cắt nhau không? (1: Có, 0: Không)", "type": "NUMERIC", "target": "0", "options": []}
            }
        }
    },
    "Bài 16: Công thức tính góc trong không gian": {
        "chapter": "Chương V: Phương pháp tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Góc giữa hai đường thẳng (Cos)": {
                "theory": "Cosin góc giữa 2 đường thẳng bằng trị tuyệt đối cosin góc giữa 2 VTCP.",
                "formula": r"\cos(d_1, d_2) = \frac{|\vec{u}_1 \cdot \vec{u}_2|}{|\vec{u}_1||\vec{u}_2|}",
                "trap": "Góc giữa hai đường thẳng luôn $\\le 90^\\circ$ nên bắt buộc tử số phải có trị tuyệt đối.",
                "audio": "Góc giữa hai đường thẳng và góc giữa hai mặt phẳng đều dùng hàm Cosin có trị tuyệt đối ở tử số.",
                "svg": "OXYZ",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc cơ bản",
                        "problem": "Tính góc giữa 2 đường thẳng có VTCP $\\vec{u}_1=(1;0;0)$ và $\\vec{u}_2=(0;1;0)$.",
                        "solution": "- $\\cos\\varphi = \\frac{|1(0)+0(1)+0(0)|}{1 \\cdot 1} = 0 \\implies \\varphi = 90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Tính cosin",
                        "problem": "Tính cosin góc giữa $d_1: x=t, y=t, z=0$ và trục $Ox$.",
                        "solution": "- $d_1$ có VTCP $\\vec{u}=(1;1;0)$. Trục Ox có VTCP $\\vec{i}=(1;0;0)$.\n- $\\cos\\varphi = \\frac{|1(1)+0+0|}{\\sqrt{2}\\sqrt{1}} = \\frac{1}{\\sqrt{2}} \\implies \\varphi = 45^\\circ$."
                    },
                    {
                        "title": "Ví dụ 3: Trắc nghiệm vuông góc",
                        "problem": "Hai đường thẳng vuông góc thì tích vô hướng hai VTCP bằng bao nhiêu?",
                        "solution": "- Bằng 0."
                    }
                ],
                "exercise": {"id": "12_16_1", "title": "Bài tập tự luyện", "content": "Trục Ox và trục Oy tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "Chủ điểm 2: Góc giữa đường thẳng và mặt phẳng (Sin)": {
                "theory": "Sin góc giữa đường thẳng và mặt phẳng bằng trị tuyệt đối cosin góc giữa VTCP và VTPT.",
                "formula": r"\sin(d, (P)) = \frac{|\vec{u} \cdot \vec{n}|}{|\vec{u}||\vec{n}|}",
                "trap": "Đây là trường hợp DUY NHẤT dùng hàm Sin. Đừng nhầm sang Cosin.",
                "audio": "Rất đặc biệt! Để tính góc giữa ĐƯỜNG và MẶT, ta dùng hàm SIN chứ không dùng COS.",
                "svg": "HINH_KHONG_GIAN",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính góc",
                        "problem": "Tính sin góc giữa đường $d$ có $\\vec{u}=(1;1;1)$ và mp $(P)$ có $\\vec{n}=(1;1;1)$.",
                        "solution": "- $\\sin\\varphi = \\frac{|1+1+1|}{\\sqrt{3}\\sqrt{3}} = \\frac{3}{3} = 1 \\implies \\varphi = 90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2: Góc với mặt tọa độ",
                        "problem": "Tính sin góc giữa trục $Oz$ và mặt phẳng $(Oxy)$.",
                        "solution": "- Trục $Oz$ có $\\vec{k}=(0;0;1)$. Mp $(Oxy)$ có VTPT $\\vec{k}=(0;0;1)$.\n- $\\sin\\varphi = 1 \\implies 90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 3: Song song",
                        "problem": "Đường thẳng song song mặt phẳng thì góc bằng bao nhiêu?",
                        "solution": "- Góc bằng 0 độ."
                    }
                ],
                "exercise": {"id": "12_16_2", "title": "Bài tập tự luyện", "content": "Đường thẳng vuông góc với mặt phẳng thì góc giữa chúng bằng bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            },
            "Chủ điểm 3: Góc giữa hai mặt phẳng (Cos)": {
                "theory": "Cosin góc giữa 2 mặt phẳng bằng trị tuyệt đối cosin góc giữa 2 VTPT.",
                "formula": r"\cos((P), (Q)) = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}",
                "trap": "Góc giữa 2 mặt phẳng không bao giờ tù.",
                "audio": "Tính góc hai mặt phẳng, ta dùng hàm Cosin của hai vectơ pháp tuyến có trị tuyệt đối ở tử số.",
                "svg": "MAT_PHANG",
                "examples": [
                    {
                        "title": "Ví dụ 1",
                        "problem": "Tính góc giữa $(Oxy)$ và $(Oyz)$.",
                        "solution": "- VTPT lần lượt là $\\vec{k}=(0;0;1)$ và $\\vec{i}=(1;0;0)$. Tích vô hướng bằng 0 nên góc là $90^\\circ$."
                    },
                    {
                        "title": "Ví dụ 2",
                        "problem": "Góc giữa $x+y+z=0$ và $x+y+z-5=0$.",
                        "solution": "- Hai VTPT trùng nhau nên góc bằng $0^\\circ$ (hai mp song song)."
                    },
                    {
                        "title": "Ví dụ 3",
                        "problem": "Cosin góc giữa $x+y=0$ và $y+z=0$.",
                        "solution": "- $\\vec{n}_1=(1;1;0), \\vec{n}_2=(0;1;1)$.\n- $\\cos\\varphi = \\frac{|1|}{\\sqrt{2}\\sqrt{2}} = 0.5$."
                    }
                ],
                "exercise": {"id": "12_16_3", "title": "Bài tập tự luyện", "content": "Hai mặt phẳng vuông góc tạo với nhau góc bao nhiêu độ?", "type": "NUMERIC", "target": "90", "options": []}
            }
        }
    },
    "Bài 17: Phương trình mặt cầu": {
        "chapter": "Chương V: Phương pháp tọa độ trong không gian",
        "topics": {
            "Chủ điểm 1: Phương trình chính tắc của mặt cầu": {
                "theory": "Mặt cầu tâm $I(a; b; c)$ bán kính $R$ có phương trình dạng $(x-a)^2+(y-b)^2+(z-c)^2=R^2$.",
                "formula": r"(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2",
                "trap": "Nhớ đổi dấu khi đọc tọa độ tâm I từ phương trình chính tắc.",
                "audio": "Mặt cầu tâm I bán kính R có phương trình chính tắc dạng bình phương ba cụm tọa độ bằng R bình phương. Nhớ đổi dấu tọa độ tâm nhé.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tìm tâm và bán kính",
                        "problem": "Tìm tâm và bán kính của $(x-1)^2 + (y+2)^2 + (z-3)^2 = 16$.",
                        "solution": "- Đổi dấu: Tâm $I(1; -2; 3)$.\n- Lấy căn: Bán kính $R = \\sqrt{16} = 4$."
                    },
                    {
                        "title": "Ví dụ 2: Lập PT mặt cầu",
                        "problem": "Lập PT mặt cầu tâm $O(0;0;0)$ bán kính $R=5$.",
                        "solution": "- $x^2 + y^2 + z^2 = 25$."
                    },
                    {
                        "title": "Ví dụ 3: Mặt cầu đường kính AB",
                        "problem": "Viết PT mặt cầu đường kính AB với $A(1;1;1), B(3;3;3)$.",
                        "solution": "- Tâm I là trung điểm AB $\\implies I(2;2;2)$.\n- Bán kính $R = AB/2 = \\sqrt{12}/2 = \\sqrt{3}$.\n- PT: $(x-2)^2 + (y-2)^2 + (z-2)^2 = 3$."
                    }
                ],
                "exercise": {"id": "12_17_1", "title": "Bài tập tự luyện", "content": "Bán kính của mặt cầu $(x-1)^2 + y^2 + (z+3)^2 = 25$ bằng:", "type": "NUMERIC", "target": "5", "options": []}
            },
            "Chủ điểm 2: Phương trình mặt cầu dạng khai triển": {
                "theory": "Dạng $x^2+y^2+z^2-2ax-2by-2cz+d=0$ là mặt cầu khi $a^2+b^2+c^2-d > 0$.",
                "formula": r"I(a;b;c); \quad R = \sqrt{a^2+b^2+c^2-d}",
                "trap": "Chia hệ số của x, y, z cho -2 để tìm tọa độ tâm I.",
                "audio": "Muốn tìm tâm mặt cầu dạng khai triển, ta lấy hệ số của x, y, z chia cho âm hai.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Xác định tâm",
                        "problem": "Tìm tâm của $x^2+y^2+z^2-4x+2y-6z-1=0$.",
                        "solution": "- $a = -4/(-2) = 2; b = 2/(-2) = -1; c = -6/(-2) = 3$.\n- Vậy tâm $I(2; -1; 3)$."
                    },
                    {
                        "title": "Ví dụ 2: Xác định bán kính",
                        "problem": "Tính bán kính của mặt cầu $x^2+y^2+z^2-2x-4y-4=0$.",
                        "solution": "- Tâm $I(1; 2; 0)$. $d = -4$.\n- $R = \\sqrt{1^2+2^2+0 - (-4)} = \\sqrt{5+4} = 3$."
                    },
                    {
                        "title": "Ví dụ 3: Điều kiện là mặt cầu",
                        "problem": "Pt $x^2+y^2+z^2-2x+d=0$ là mặt cầu khi nào?",
                        "solution": "- Tâm $I(1;0;0)$. Điều kiện: $1^2 - d > 0 \\iff d < 1$."
                    }
                ],
                "exercise": {"id": "12_17_2", "title": "Bài tập tự luyện", "content": "Hoành độ tâm của $x^2+y^2+z^2-6x+2y=0$ bằng:", "type": "NUMERIC", "target": "3", "options": []}
            },
            "Chủ điểm 3: Vị trí tương đối của MP và Mặt cầu": {
                "theory": "Dựa vào khoảng cách từ tâm I đến (P) ký hiệu là d. Nếu d < R (cắt theo đường tròn), d = R (tiếp xúc), d > R (không giao nhau).",
                "formula": r"d(I, (P)) = R \implies \text{Tiếp diện}",
                "trap": "Tính sai khoảng cách d dẫn đến nhận định sai.",
                "audio": "Nếu khoảng cách từ tâm đến mặt phẳng bằng bán kính thì mặt phẳng tiếp xúc mặt cầu.",
                "svg": "MAT_CAU",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tiếp xúc",
                        "problem": "Mặt cầu tâm $I(0;0;0)$ bán kính $R=3$. Mặt phẳng $2x-2y+z-9=0$ có vị trí tương đối thế nào?",
                        "solution": "- $d(I, P) = |-9|/3 = 3$.\n- Vì $d = R = 3$ nên mặt phẳng tiếp xúc mặt cầu."
                    },
                    {
                        "title": "Ví dụ 2: Không giao",
                        "problem": "Mặt phẳng $x=5$ và mặt cầu tâm O bán kính 4.",
                        "solution": "- $d = 5 > R=4$. Không giao nhau."
                    },
                    {
                        "title": "Ví dụ 3: Bán kính đường tròn giao tuyến",
                        "problem": "Công thức bán kính đường tròn giao tuyến $r$?",
                        "solution": "- $r = \\sqrt{R^2 - d^2}$ (Định lý Pytago)."
                    }
                ],
                "exercise": {"id": "12_17_3", "title": "Bài tập tự luyện", "content": "Nếu d(I, P) = R thì MP và mặt cầu có bao nhiêu điểm chung?", "type": "NUMERIC", "target": "1", "options": []}
            }
        }
    },
    "Bài 18: Xác suất có điều kiện": {
        "chapter": "Chương VI: Xác suất có điều kiện",
        "topics": {
            "Chủ điểm 1: Công thức xác suất có điều kiện": {
                "theory": "Xác suất của biến cố A với điều kiện biến cố B đã xảy ra, ký hiệu $P(A|B)$, bằng xác suất của biến cố giao chia cho xác suất của B.",
                "formula": r"P(A|B) = \frac{P(AB)}{P(B)}",
                "trap": "Rất dễ nhầm lẫn giữa P(A|B) và P(AB). Đọc kỹ từ 'biết rằng'.",
                "audio": "Xác suất có điều kiện bằng xác suất giao chia cho xác suất của điều kiện.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính P(A|B)",
                        "problem": "Biết $P(AB) = 0.2$ và $P(B) = 0.5$. Tính $P(A|B)$.",
                        "solution": "- $P(A|B) = 0.2 / 0.5 = 0.4$."
                    },
                    {
                        "title": "Ví dụ 2: Tính P(AB)",
                        "problem": "Biết $P(A|B) = 0.6, P(B) = 0.3$. Tính $P(AB)$.",
                        "solution": "- $P(AB) = P(B) \\cdot P(A|B) = 0.3 \\cdot 0.6 = 0.18$."
                    },
                    {
                        "title": "Ví dụ 3: Biến cố độc lập",
                        "problem": "A và B độc lập thì P(A|B) bằng gì?",
                        "solution": "- Bằng $P(A)$ do việc B xảy ra không ảnh hưởng đến A."
                    }
                ],
                "exercise": {"id": "12_18_1", "title": "Bài tập tự luyện", "content": "Biết P(AB)=0.3, P(B)=0.6. P(A|B) bằng:", "type": "NUMERIC", "target": "0.5", "options": []}
            },
            "Chủ điểm 2: Sơ đồ hình cây và công thức nhân": {
                "theory": "Sơ đồ hình cây giúp phân tích các giai đoạn của phép thử. Xác suất của một nhánh bằng tích các xác suất dọc theo nhánh đó.",
                "formula": r"P(AB) = P(A) \cdot P(B|A)",
                "trap": "Tính sai xác suất ở giai đoạn 2 do không trừ bớt số lượng (trong bài toán rút không hoàn lại).",
                "audio": "Dùng sơ đồ hình cây, nhân các xác suất dọc theo nhánh để tìm xác suất giao.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Rút bi không hoàn lại",
                        "problem": "Hộp có 3 bi đỏ, 2 bi xanh. Rút lần lượt 2 bi không trả lại. Tính XS cả 2 bi đều đỏ.",
                        "solution": "- P(đỏ lần 1) = 3/5.\n- P(đỏ lần 2 | đỏ lần 1) = 2/4 = 1/2.\n- P = (3/5) * (1/2) = 3/10 = 0.3."
                    },
                    {
                        "title": "Ví dụ 2: Quy tắc nhân",
                        "problem": "Xác suất trời mưa là 0.4. Nếu mưa, XS đến muộn là 0.8. Tính XS trời mưa và đến muộn.",
                        "solution": "- P = 0.4 * 0.8 = 0.32."
                    },
                    {
                        "title": "Ví dụ 3: Rút bi có hoàn lại",
                        "problem": "Hộp 3 đỏ 2 xanh. Rút 2 bi CÓ hoàn lại. XS 2 bi đỏ?",
                        "solution": "- Do có hoàn lại nên độc lập: P = (3/5) * (3/5) = 9/25 = 0.36."
                    }
                ],
                "exercise": {"id": "12_18_2", "title": "Bài tập tự luyện", "content": "P(A)=0.5, P(B|A)=0.4. P(AB) bằng:", "type": "NUMERIC", "target": "0.2", "options": []}
            }
        }
    },
    "Bài 19: Công thức xác suất toàn phần và công thức Bayes": {
        "chapter": "Chương VI: Xác suất có điều kiện",
        "topics": {
            "Chủ điểm 1: Công thức xác suất toàn phần": {
                "theory": "Dùng để tính xác suất của biến cố A dựa trên một hệ biến cố đầy đủ $B_1, B_2...$ (các trường hợp phân hoạch không gian mẫu).",
                "formula": r"P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2)",
                "trap": "Hệ biến cố B1, B2 phải là hệ đầy đủ (tổng xác suất bằng 1 và xung khắc từng đôi).",
                "audio": "Xác suất toàn phần là tổng của các tích xác suất theo từng trường hợp xảy ra.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Tính xác suất phế phẩm",
                        "problem": "Máy 1 sx 60% sp, tỉ lệ phế phẩm 1%. Máy 2 sx 40% sp, tỉ lệ 2%. Chọn 1 sp, tính XS nó là phế phẩm.",
                        "solution": "- $P(A) = 0.6(0.01) + 0.4(0.02) = 0.006 + 0.008 = 0.014$."
                    },
                    {
                        "title": "Ví dụ 2: Hai hộp bi",
                        "problem": "Hộp 1 có tỉ lệ bi đỏ 0.3. Hộp 2 có tỉ lệ 0.8. Chọn ngẫu nhiên 1 hộp (xác suất 0.5-0.5) rồi lấy 1 bi. XS bi đỏ?",
                        "solution": "- $P(Do) = 0.5(0.3) + 0.5(0.8) = 0.15 + 0.4 = 0.55$."
                    },
                    {
                        "title": "Ví dụ 3: Hệ đầy đủ",
                        "problem": "Nếu $P(B_1)=0.3, P(B_2)=0.7$, $P(A|B_1)=1, P(A|B_2)=0$. Tính $P(A)$.",
                        "solution": "- $P(A) = 0.3(1) + 0.7(0) = 0.3$."
                    }
                ],
                "exercise": {"id": "12_19_1", "title": "Bài tập tự luyện", "content": "P(B1)=0.4, P(B2)=0.6. P(A|B1)=0.5, P(A|B2)=0.5. P(A) bằng:", "type": "NUMERIC", "target": "0.5", "options": []}
            },
            "Chủ điểm 2: Công thức Bayes": {
                "theory": "Được dùng để tính lại xác suất của một nguyên nhân $B_k$ khi ĐÃ BIẾT biến cố $A$ xảy ra (Xác suất hậu nghiệm).",
                "formula": r"P(B_1|A) = \frac{P(B_1)P(A|B_1)}{P(A)}",
                "trap": "Phải tính đúng Xác suất toàn phần P(A) làm mẫu số trước khi tính Bayes.",
                "audio": "Bayes dùng để truy ngược nguyên nhân. Lấy nhánh nguyên nhân đó chia cho xác suất toàn phần.",
                "svg": "XAC_SUAT",
                "examples": [
                    {
                        "title": "Ví dụ 1: Truy xuất nguyên nhân",
                        "problem": "Tiếp ví dụ 1 trên (P(A)=0.014). Biết sp lấy ra là phế phẩm, tính XS nó do máy 1 sản xuất.",
                        "solution": "- $P(M_1|A) = \\frac{0.6 \\times 0.01}{0.014} = \\frac{0.006}{0.014} = \\frac{3}{7} \\approx 0.428$."
                    },
                    {
                        "title": "Ví dụ 2: Công thức",
                        "problem": "Theo công thức Bayes, tử số của $P(B_1|A)$ là gì?",
                        "solution": "- Tử số là $P(A \cap B_1)$ hay $P(B_1)P(A|B_1)$."
                    },
                    {
                        "title": "Ví dụ 3: Ứng dụng y tế",
                        "problem": "Người bệnh xét nghiệm dương tính. Xác suất người này thực sự mắc bệnh gọi là xác suất gì?",
                        "solution": "- Xác suất hậu nghiệm (tính bằng công thức Bayes)."
                    }
                ],
                "exercise": {"id": "12_19_2", "title": "Bài tập tự luyện", "content": "P(A)=0.2, P(B1)=0.5, P(A|B1)=0.1. P(B1|A) bằng:", "type": "NUMERIC", "target": "0.25", "options": []}
            }
        }
    }
})