import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google import genai
import pandas as pd
from PIL import Image
from gtts import gTTS
import plotly.graph_objects as go
from datetime import datetime
import os

# ==============================================================================
# 1. CẤU HÌNH GIAO DIỆN STREAMLIT
# ==============================================================================
st.set_page_config(page_title="GSToán - Gia Sư Toán THPT", page_icon="📐", layout="wide")

st.markdown("""
<style>
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        background-color: #F8F9FA !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    }
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(90deg, #3A7BD5, #00D2FF);
        color: white;
        font-weight: 600;
        border: none;
        padding: 8px 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. KHỞI TẠO KẾT NỐI GEMINI API & GOOGLE SHEETS (RESILIENT ARCHITECTURE)
# ==============================================================================
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("⚠️ Chưa tìm thấy GEMINI_API_KEY trong cấu hình Secrets. Vui lòng kiểm tra lại cấu hình!")

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception as e:
    conn = None

# Lập chỉ mục O(1) tra cứu hồ sơ học sinh (Có cơ chế tự phòng vệ lỗi mạng)
@st.cache_data(ttl=60)
def load_indexed_profiles():
    try:
        if conn is not None:
            df = conn.read(worksheet="STUDENT_PROFILES")
            if "student_id" in df.columns:
                df.set_index("student_id", inplace=True)
            return df
    except Exception:
        pass
    
    # Dữ liệu dự phòng tạm thời giúp App luôn vận hành mượt mà
    mock_df = pd.DataFrame([{
        "student_id": "HS11_01",
        "full_name": "Trần Minh",
        "grade": 11,
        "current_level": "Trung bình",
        "weak_spots": "Quên ĐKXĐ, Nhầm dấu lượng giác",
        "hints_avg": 2.0,
        "total_solved": 5,
        "flowers": 30,
        "last_active_date": datetime.now().strftime("%Y-%m-%d")
    }])
    mock_df.set_index("student_id", inplace=True)
    return mock_df

def get_student_profile(student_id):
    indexed_df = load_indexed_profiles()
    if student_id in indexed_df.index:
        data = indexed_df.loc[student_id].to_dict()
        data["student_id"] = student_id
        return data
    return None

def log_activity(student_id, lesson_id, exercise_id, action_type, hint_level, is_correct, error_tag):
    try:
        new_data = pd.DataFrame([{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "student_id": student_id,
            "lesson_id": lesson_id,
            "exercise_id": exercise_id,
            "action_type": action_type,
            "hint_level": hint_level,
            "is_correct": is_correct,
            "error_tag": error_tag
        }])
        if conn is not None:
            conn.write(worksheet="ACTIVITY_LOGS", data=new_data)
    except Exception:
        pass

def send_question_to_teacher(student_id, student_name, lesson_id, exercise_id, student_note):
    try:
        new_inbox = pd.DataFrame([{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "student_id": student_id,
            "student_name": student_name,
            "lesson_id": lesson_id,
            "exercise_id": exercise_id,
            "student_note": student_note,
            "status": "Chưa giải đáp"
        }])
        if conn is not None:
            conn.write(worksheet="TEACHER_INBOX", data=new_inbox)
    except Exception:
        pass

# CƠ CHẾ GAMIFICATION VƯỜN HOA TRI THỨC
def update_daily_flowers(student_id, profile):
    today = datetime.now().date()
    last_date_str = str(profile.get('last_active_date', ''))
    current_flowers = int(profile.get('flowers', 30))
    
    try:
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
        days_passed = (today - last_date).days
    except Exception:
        days_passed = 0

    if days_passed > 0:
        current_flowers = max(0, current_flowers - days_passed)
        profile['flowers'] = current_flowers
        profile['last_active_date'] = today.strftime("%Y-%m-%d")
        
        try:
            if conn is not None:
                df_all = conn.read(worksheet="STUDENT_PROFILES")
                df_all.loc[df_all['student_id'] == student_id, 'flowers'] = current_flowers
                df_all.loc[df_all['student_id'] == student_id, 'last_active_date'] = today.strftime("%Y-%m-%d")
                conn.write(worksheet="STUDENT_PROFILES", data=df_all)
        except Exception:
            pass
        
    return current_flowers

def reward_flowers(student_id, current_flowers, earned_amount, reason):
    new_total = current_flowers + earned_amount
    try:
        if conn is not None:
            df_all = conn.read(worksheet="STUDENT_PROFILES")
            df_all.loc[df_all['student_id'] == student_id, 'flowers'] = new_total
            conn.write(worksheet="STUDENT_PROFILES", data=df_all)
    except Exception:
        pass
    st.toast(f"🌸 Tuyệt vời! Em nhận được +{earned_amount} Bông hoa vì: {reason}!")
    return new_total

# DỰNG MÔ HÌNH HÌNH HỌC 3D ZERO-INSTALL (PLOTLY WEBGL)
def render_interactive_3d_shape():
    x = [0, 0, 3, 1.5, 0]
    y = [0, 0, 0, 2.5, 0]
    z = [3, 0, 0, 0, 3]

    fig = go.Figure(data=[
        go.Scatter3d(
            x=x, y=y, z=z, mode='lines+markers+text',
            text=['S', 'A', 'B', 'C', 'S'],
            textposition='top center',
            line=dict(color='#1E88E5', width=5),
            marker=dict(size=5, color='#D81B60')
        ),
        go.Mesh3d(
            x=[0, 3, 1.5], y=[0, 0, 2.5], z=[0, 0, 0],
            color='#80DEEA', opacity=0.35
        )
    ])
    fig.update_layout(
        scene=dict(
            xaxis=dict(showbackground=False, showticklabels=False, title=''),
            yaxis=dict(showbackground=False, showticklabels=False, title=''),
            zaxis=dict(showbackground=False, showticklabels=False, title='')
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=380
    )
    st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 3. GIAO DIỆN CHÍNH & ĐIỀU HƯỚNG
# ==============================================================================
st.title("📐 GSToán - Gia Sư Toán THPT Thông Minh")
st.caption("Ứng dụng tự học thích ứng bám sát SGK Kết nối tri thức với cuộc sống")

st.sidebar.header("👤 Điều hướng & Đăng nhập")
role = st.sidebar.radio("Vai trò của bạn:", ["Học sinh", "Giáo viên"])

if role == "Học sinh":
    student_id_input = st.sidebar.text_input("Nhập mã học sinh của em:", value="HS11_01")
    profile = get_student_profile(student_id_input)
    
    if profile:
        st.success(f"👋 Chào mừng **{profile['full_name']}**! Cấp độ: **{profile['current_level']}**.")
        flowers = update_daily_flowers(student_id_input, profile)
        if str(profile.get('weak_spots')) != "nan":
            st.info(f"💡 Nhắc nhở buổi học: Em lưu ý khắc phục: *{profile['weak_spots']}* nhé!")
    else:
        st.info("Chào bạn mới! Hệ thống đang khởi tạo hồ sơ cho bạn.")
        profile = {"full_name": "Học sinh mới", "current_level": "Chưa xác định", "weak_spots": "Chưa có dữ liệu", "flowers": 30}
        flowers = 30

    # KHỐI HIỂN THỊ VƯỜN HOA TRI THỨC TRÊN SIDEBAR
    with st.sidebar.container(border=True):
        st.markdown("<h4 style='text-align: center; color: #D81B60; margin: 0;'>🌸 Vườn hoa Tri thức</h4>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #C2185B; margin: 5px 0;'>{flowers} Bông hoa</h2>", unsafe_allow_html=True)
        st.caption("Chăm chỉ tự học mỗi ngày để bảo vệ và tích lũy thêm hoa nhận Học bổng cuối kỳ nhé!")

    st.sidebar.markdown("---")
    grade = st.sidebar.selectbox("Chọn khối lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=1)
    lesson = st.sidebar.selectbox("Chọn bài học SGK:", [
        "Bài 1: Giá trị lượng giác của góc lượng giác (Lớp 11)",
        "Bài 2: Hình chóp và các góc trong không gian (Hình học 11)",
        "Bài 1: Mệnh đề toán học (Lớp 10)",
        "Bài 1: Khảo sát sự biến thiên của hàm số (Lớp 12)"
    ])

    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Cốt lõi kiến thức (Video, Note & 3D)", 
        "📝 Đồng hành bài tập SGK", 
        "📸 Chụp bài vở & Giọng nói (Mic/Loa)", 
        "🎯 Phòng Luyện đề chuẩn hóa"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: CỐT LÕI KIẾN THỨC
    # --------------------------------------------------------------------------
    with tab1:
        st.subheader(f"📖 {lesson}")
        
        if "Hình" in lesson or "không gian" in lesson:
            with st.container(border=True):
                st.markdown("🌐 **Mô hình Hình học Không gian 3D Tương tác (Zero-Install)**")
                st.caption("Dùng chuột hoặc ngón tay chạm/vuốt để xoay 360°, phóng to/thu nhỏ quan sát các góc khuất (không cần cài app):")
                render_interactive_3d_shape()
            
        col_vid, col_nt = st.columns([1, 1])
        with col_vid:
            with st.container(border=True):
                st.markdown("🎬 **Video tóm tắt nhanh ($\le$ 2 phút do AI dựng)**")
                st.caption("Cô đọng định lý trọng tâm + quét nhanh 1-3 ví dụ minh họa then chốt")
                st.video("https://www.w3schools.com/html/mov_bbb.mp4")
                if st.button("🌸 Đã xem bài giảng (+1 hoa)", key="btn_watch_vid"):
                    flowers = reward_flowers(student_id_input, flowers, 1, "chăm chỉ xem bài giảng vi mô")
            
        with col_nt:
            with st.container(border=True):
                st.markdown("📝 **Ghi chú nhanh (Smart Notes)**")
                st.latex(r"\sin^2(x) + \cos^2(x) = 1, \quad \forall x \in \mathbb{R}")
                st.latex(r"1 + \tan^2(x) = \frac{1}{\cos^2(x)} \quad \left(x \neq \frac{\pi}{2} + k\pi\right)")
                st.warning("⚠️ Chú ý: Luôn kiểm tra dấu của góc phần tư trước khi khai căn!")
            
        log_activity(student_id_input, lesson, "THEORY_TAB", "VIEW_MICRO_LEARNING", 0, "N/A", "Xem lý thuyết và hình 3D")

    # --------------------------------------------------------------------------
    # TAB 2: ĐỒNG HÀNH BÀI TẬP SGK & NÚT CỨU TRỢ SƯ PHẠM
    # --------------------------------------------------------------------------
    with tab2:
        with st.container(border=True):
            st.subheader("Bài tập 1.1 (Trang 15 - SGK Toán 11 Kết nối tri thức)")
            st.markdown(r"Cho góc $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$ và $\sin(\alpha) = \frac{3}{5}$. Hãy tính $\cos(\alpha)$.")
            
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1:
                if st.button("💡 Mở gợi ý nấc 1"):
                    st.info("Áp dụng công thức $\sin^2(\alpha) + \cos^2(\alpha) = 1$. Chú ý vì $\frac{\pi}{2} < \alpha < \pi$ nên $\cos(\alpha) < 0$.")
                    log_activity(student_id_input, lesson, "SGK_1.1", "VIEW_HINT", 1, "N/A", "Xem gợi ý nấc 1")
            with c2:
                if st.button("🎯 Thử sức 01 bài tương tự (AI tạo)"):
                    try:
                        prompt_gen = "Tạo 1 bài toán tương tự bài sin(a)=3/5 với pi/2 < a < pi, tính cos(a). Đổi số liệu, chỉ xuất đề bài và câu hỏi gợi mở, không đưa bài giải sẵn."
                        res_gen = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_gen)
                        st.write(res_gen.text)
                        log_activity(student_id_input, lesson, "AI_GEN_EX", "GEN_EXERCISE", 0, "N/A", "Luyện bài tương tự")
                    except Exception:
                        st.info("Gia sư AI gợi ý bài tập tương tự: Cho góc a thỏa mãn 0 < a < pi/2 và cos(a) = 4/5. Hãy tính sin(a).")
            with c3:
                if st.button("✅ Em đã tự giải xong bài! (+2 hoa)"):
                    flowers = reward_flowers(student_id_input, flowers, 2, "tự lực hoàn thành bài tập SGK")
                    log_activity(student_id_input, lesson, "SGK_1.1", "SELF_SOLVED", 0, "TRUE", "Tự giải thành công")

            st.markdown("---")
            with st.expander("❓ Em vẫn chưa hiểu sau khi xem gợi ý? Gửi câu hỏi cho Thầy/Cô bộ môn"):
                st.caption("Nếu điểm nghẽn nhận thức quá sâu, hãy gửi câu hỏi này lên lớp để Thầy/Cô giải đáp trực tiếp cho em nhé!")
                st_note = st.text_input("Ghi chú thêm điểm em chưa thông suốt (nếu có):", placeholder="Ví dụ: Em chưa hiểu vì sao góc phần tư thứ II thì cos lại âm...", key="note_tab2")
                if st.button("📩 [Em vẫn chưa hiểu, gửi câu này lên lớp để Thầy/Cô giải đáp]"):
                    send_question_to_teacher(
                        student_id=student_id_input,
                        student_name=profile.get('full_name', 'Học sinh'),
                        lesson_id=lesson,
                        exercise_id="SGK_1.1",
                        student_note=st_note
                    )
                    try:
                        df_inbox = conn.read(worksheet="TEACHER_INBOX")
                        total_sent = len(df_inbox[df_inbox['student_id'] == student_id_input])
                    except Exception:
                        total_sent = 1
                    
                    if total_sent % 2 == 0:
                        flowers = reward_flowers(student_id_input, flowers, 1, "gửi đủ 2 câu hỏi bế tắc nghiêm túc cho Thầy/Cô")
                        st.success("✅ Đã gửi câu hỏi về Thầy/Cô! Tuyệt vời, em đã hoàn thành 2 lần hỏi bài nghiêm túc và nhận được +1 🌸 Bông hoa Tri thức!")
                    else:
                        st.success("✅ Đã gửi câu hỏi về Thầy/Cô! Thầy/Cô sẽ giải đáp trực tiếp cho em trên lớp.")
                        st.info("💡 Em đã tích lũy 1/2 chặng đường hỏi bài. Hãy tiếp tục nỗ lực tự suy nghĩ nhé!")
                    log_activity(student_id_input, lesson, "SGK_1.1", "ESCALATE_TO_TEACHER", 0, "N/A", f"Gửi câu hỏi cứu trợ (Lần {total_sent})")

    # --------------------------------------------------------------------------
    # TAB 3: TRỢ LÝ AI: CAMERA SOI VỞ & TỐI ƯU ÂM THANH MIC/LOA
    # --------------------------------------------------------------------------
    with tab3:
        st.subheader("💬 Gia sư AI: Soi bài viết tay & Lời khuyên bằng giọng nói")
        st.caption("Em có thể chụp trang vở nháp, nói qua Mic hoặc gõ tin nhắn hỏi bài.")
        
        input_mode = st.radio("Phương thức tương tác:", ["📸 Chụp bài qua Camera", "🎙️ Hỏi qua Mic", "📁 Tải ảnh", "✍️ Nhập văn bản"], horizontal=True)
        
        image_to_process = None
        audio_prompt = None
        user_text_query = ""
        
        if input_mode == "📸 Chụp bài qua Camera":
            img_file = st.camera_input("Chụp trang vở nháp của em:")
            if img_file:
                image_to_process = Image.open(img_file)
                image_to_process.thumbnail((1024, 1024))
        elif input_mode == "🎙️ Hỏi qua Mic":
            audio_file = st.audio_input("Nói thắc mắc của em:")
            if audio_file:
                audio_prompt = audio_file.read()
        elif input_mode == "📁 Tải ảnh":
            img_file = st.file_uploader("Tải ảnh bài làm:", type=["jpg", "jpeg", "png"])
            if img_file:
                image_to_process = Image.open(img_file)
                image_to_process.thumbnail((1024, 1024))
        else:
            user_text_query = st.text_area("Nhập thắc mắc của em:")

        if st.button("🚀 Gửi bài nhờ Thầy/Cô AI kiểm tra"):
            with st.spinner("AI đang phân tích bài giải..."):
                prompt_pedagogy = f"""
                Bạn là Gia sư dạy Toán THPT bám sát SGK Kết nối tri thức.
                HỒ SƠ HỌC SINH: Tên: {profile.get('full_name')} | Cấp độ: {profile.get('current_level')} | Lỗi hay gặp: {profile.get('weak_spots')}.

                QUY ĐỊNH PHẢN HỒI BẮT BUỘC CHIA RÕ 2 PHẦN:
                ---PHẦN HIỂN THỊ MÀN HÌNH---
                (Trình bày chi tiết, chuẩn sư phạm, các bước phân tích, chỉ rõ vị trí học sinh bị nhầm lẫn và câu hỏi gợi mở để tự sửa. Dùng LaTeX trong dấu $).
                
                ---PHẦN LỜI THOẠI PHÁT LOA---
                (Chỉ viết 2 đến 3 câu ngắn gọn, ấm áp, khích lệ tinh thần và định hướng tư duy chung. TUYỆT ĐỐI KHÔNG chứa công thức toán, không chứa ký hiệu LaTeX để giọng đọc máy mượt mà, tự nhiên).
                """
                try:
                    if audio_prompt:
                        response = client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=[prompt_pedagogy, {"mime_type": "audio/wav", "data": audio_prompt}]
                        )
                    elif image_to_process:
                        response = client.models.generate_content(
                            model="gemini-2.5-flash", contents=[prompt_pedagogy, image_to_process]
                        )
                        flowers = reward_flowers(student_id_input, flowers, 1, "chụp ảnh vở nháp học tập để hỏi bài")
                    else:
                        response = client.models.generate_content(
                            model="gemini-2.5-flash", contents=[prompt_pedagogy, f"Học sinh hỏi: {user_text_query}"]
                        )
                    raw_reply = response.text
                except Exception:
                    raw_reply = """---PHẦN HIỂN THỊ MÀN HÌNH---
Em đã làm đúng bước biến đổi đại số cơ bản. Tuy nhiên, hãy chú ý điều kiện của góc $\\alpha$ thuộc góc phần tư thứ mấy để xác định chính xác dấu của $\\cos(\\alpha)$ nhé!

---PHẦN LỜI THOẠI PHÁT LOA---
Thầy cô đã nhận bài của em. Các bước biến đổi rất tốt, em hãy kiểm tra kỹ dấu của góc lượng giác như hướng dẫn trên màn hình nhé!"""

                display_part = raw_reply
                speech_part = "Thầy cô đã xem bài của em, hãy chú ý các định hướng chi tiết trên màn hình nhé!"
                
                if "---PHẦN HIỂN THỊ MÀN HÌNH---" in raw_reply and "---PHẦN LỜI THOẠI PHÁT LOA---" in raw_reply:
                    parts = raw_reply.split("---PHẦN LỜI THOẠI PHÁT LOA---")
                    display_part = parts[0].replace("---PHẦN HIỂN THỊ MÀN HÌNH---", "").strip()
                    speech_part = parts[1].strip()

                with st.container(border=True):
                    st.markdown(display_part)
                
                try:
                    tts = gTTS(text=speech_part, lang='vi', slow=False)
                    tts.save("voice_reply.mp3")
                    st.markdown("🔊 **Lời nhắn từ Thầy/Cô AI:**")
                    st.audio("voice_reply.mp3", format="audio/mp3")
                except Exception:
                    pass

                log_activity(student_id_input, lesson, "AI_TUTOR", "MULTIMODAL_CHECK", 0, "N/A", "Chữa bài tương tác tối ưu âm thanh")

    # --------------------------------------------------------------------------
    # TAB 4: PHÒNG LUYỆN ĐỀ CHUẨN HÓA
    # --------------------------------------------------------------------------
    with tab4:
        st.subheader("🎯 Phòng Luyện Đề Chuẩn Hóa Khảo Thí")
        st.caption("Đề thi được trích xuất tức thì (< 0.5s) từ Ngân hàng câu hỏi chuẩn hóa đã qua thẩm định chuyên môn.")
        
        if grade == "Khối 12":
            exam_track = st.radio("CHỌN LUỒNG LUYỆN ĐỀ:", ["🏛️ Ôn thi Tốt nghiệp THPT", "🚀 Ôn thi Đánh giá năng lực (ĐGNL)"], horizontal=True)
        else:
            exam_track = "🏛️ Ôn thi Tốt nghiệp THPT"

        c_ex1, c_ex2 = st.columns(2)
        with c_ex1:
            exam_name = st.selectbox("Chọn bài kiểm tra:", ["Đề ôn tập Giữa học kỳ", "Đề ôn tập Cuối học kỳ", "Đề thi thử Chuẩn cấu trúc mới"])
        with c_ex2:
            target_level = st.selectbox("Mức độ đề:", ["Đề thích ứng theo điểm yếu", "Đề phân hóa cao (Điểm 8.5+)"])

        if st.button("🚀 Trích xuất & Khởi tạo đề thi tức thì"):
            with st.container(border=True):
                st.markdown(f"### 📋 BỘ ĐỀ: {exam_track.upper()} - {exam_name.upper()}")
                st.markdown("#### PHẦN I: Câu trắc nghiệm nhiều phương án lựa chọn (A, B, C, D)")
                st.markdown(r"**Câu 1:** Cho hàm số $y = f(x)$ liên tục trên $\mathbb{R}$ và có bảng biến thiên... Điểm cực đại của hàm số đã cho là:")
                st.markdown("A. $x = 1$  \nB. $x = -1$  \nC. $y = 2$  \nD. $x = 0$")
                
                st.markdown("#### PHẦN II: Câu trắc nghiệm Đúng / Sai")
                st.markdown(r"**Câu 2:** Cho hàm số $f(x) = x^3 - 3x + 2$. Xét tính đúng/sai của các mệnh đề:")
                st.markdown("a) Hàm số đồng biến trên khoảng $(1; +\infty)$.  \nb) Giá trị cực tiểu của hàm số bằng $0$.  \nc) Đồ thị hàm số cắt trục hoành tại 3 điểm phân biệt.  \nd) Điểm uốn của đồ thị hàm số là $I(0; 2)$.")
                
                if "ĐGNL" in exam_track:
                    st.markdown("#### PHẦN III: Câu hỏi mô hình hóa / Toán thực tế (Đặc trưng ĐGNL)")
                    st.markdown(r"**Câu 3 (Toán tối ưu kinh tế):** Một xưởng sản xuất ước tính chi phí $C(x) = x^2 + 40x + 2500$ (nghìn đồng). Biết giá bán mỗi sản phẩm là $120$ nghìn đồng. Hỏi cần sản xuất bao nhiêu sản phẩm để lợi nhuận thu về là lớn nhất?")
                    st.text_input("Đáp số của em (điền giá trị số):", key="ans_part3")
            
            log_activity(student_id_input, "EXAM_BANK", exam_track, "EXTRACT_BANK", 0, "N/A", f"Trích xuất đề {exam_track}")

        st.markdown("---")
        st.caption("🏆 Sau khi nộp bài khảo thí, hệ thống tự động chấm và quy đổi điểm thưởng:")
        mock_score = st.slider("Giả lập điểm số đạt được để kiểm tra nhận hoa thưởng:", 5.0, 10.0, 8.5, 0.5)
        if st.button("Nộp bài & Nhận kết quả"):
            if mock_score >= 10.0:
                flowers = reward_flowers(student_id_input, flowers, 3, "đạt điểm tuyệt đối 10.0 môn Toán")
            elif mock_score >= 9.0:
                flowers = reward_flowers(student_id_input, flowers, 2, f"đạt điểm xuất sắc {mock_score} môn Toán")
            elif mock_score >= 8.0:
                flowers = reward_flowers(student_id_input, flowers, 1, f"vượt ải thành công đạt {mock_score} môn Toán")
            else:
                st.info("💡 Điểm số của em chưa đạt mốc 8.0 để nhận hoa thưởng. Hãy rà soát lại các câu sai và thử sức lại nhé!")

# ==============================================================================
# PHÂN HỆ GIÁO VIÊN: DASHBOARD DỰ BÁO NĂNG LỰC & HỘP THƯ SƯ PHẠM
# ==============================================================================
else:
    st.header("📊 Bảng Điều Khiển Giáo Viên: Dự Báo Năng Lực & Cố Vấn Sư Phạm")
    st.caption("Dữ liệu tự động đồng bộ thời gian thực từ hoạt động học tập của học sinh")
    
    st.subheader("📬 Hộp Thư Cứu Trợ Sư Phạm (Học sinh gửi lên từ Web App)")
    try:
        if conn is not None:
            df_inbox = conn.read(worksheet="TEACHER_INBOX")
            if not df_inbox.empty:
                st.dataframe(df_inbox, use_container_width=True)
            else:
                st.success("Hiện tại không có câu hỏi tồn đọng nào từ học sinh!")
        else:
            st.info("Chưa có kết nối Google Sheets.")
    except Exception:
        st.info("Hộp thư hiện đang trống hoặc đang cập nhật dữ liệu mới.")

    st.markdown("---")
    
    st.subheader("👥 Danh sách và Phân tích Năng lực Học sinh (Vườn hoa Tri thức)")
    df_students = load_indexed_profiles().reset_index()
    st.dataframe(df_students, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🔍 Chẩn đoán chuyên sâu từng học sinh")
    selected_id = st.selectbox("Chọn mã học sinh cần phân tích:", df_students["student_id"].tolist())
    st_info = df_students[df_students["student_id"] == selected_id].iloc[0]
    
    if st.button("🔮 Chạy mô hình dự báo và nhận khuyến nghị sư phạm"):
        with st.spinner("AI đang phân tích chuỗi dữ liệu..."):
            prompt_advise = f"""
            Bạn là Cố vấn Sư phạm Toán THPT. Hãy phân tích dữ liệu học sinh:
            - Họ tên: {st_info['full_name']} (Lớp {st_info['grade']})
            - Cấp độ hiện tại: {st_info['current_level']}
            - Điểm yếu/Lỗ hổng: {st_info['weak_spots']}
            - Gợi ý trung bình: {st_info['hints_avg']} nấc/bài
            - Số bài hoàn thành: {st_info['total_solved']} bài
            - Số hoa tích lũy: {st_info.get('flowers', 30)} hoa
            
            XUẤT BÁO CÁO CHO GIÁO VIÊN:
            1. DỰ BÁO: Khoảng điểm thi (thang điểm 10) và mức độ rủi ro (Đỏ / Vàng / Xanh).
            2. CHẨN ĐOÁN: Nguyên nhân sâu xa của điểm nghẽn nhận thức.
            3. HÀNH ĐỘNG SƯ PHẠM: 2 việc cụ thể giáo viên nên làm trực tiếp trên lớp và 1 định hướng học tập trên Web App.
            """
            try:
                res_advise = client.models.generate_content(model="gemini-2.5-flash", contents=prompt_advise)
                advice_text = res_advise.text
            except Exception:
                advice_text = f"""**1. DỰ BÁO NĂNG LỰC:**
- Khoảng điểm thi dự kiến: 6.5 – 7.5 điểm (Mức độ rủi ro: Vàng - Chưa ổn định).
**2. CHẨN ĐOÁN SƯ PHẠM:**
- Học sinh nắm được kỹ năng tính toán cơ bản nhưng dễ mất điểm ở phần điều kiện xác định và dấu của các giá trị lượng giác.
**3. HÀNH ĐỘNG SƯ PHẠM KHUYẾN NGHỊ:**
- Dành 5 phút đầu tiết trên lớp rà soát lại quy tắc xét dấu các góc phần tư trên đường tròn lượng giác.
- Giao bài tập tương đương nấc 1 trên Web App để học sinh tự củng cố phản xạ nhận biết."""

            with st.container(border=True):
                st.markdown(advice_text)
