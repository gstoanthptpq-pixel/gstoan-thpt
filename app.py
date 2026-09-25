import streamlit as st
from streamlit_gsheets import GSheetsConnection
from google import genai
import pandas as pd
from PIL import Image
from gtts import gTTS
import base64
import os
import hashlib

# Cấu hình giao diện Streamlit
st.set_page_config(page_title="GSToán - Hệ Sinh Thái Tự Học", page_icon="📐", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    div[data-baseweb="popover"] ul, div[role="listbox"] { max-height: 320px !important; overflow-y: auto !important; scrollbar-width: thin; scrollbar-color: #3B82F6 #F1F5F9; }
    div[data-testid="stVerticalBlockBorderWrapper"] { border-radius: 14px !important; background-color: #F8FAFC !important; border: 1px solid #E2E8F0 !important; padding: 16px !important; margin-bottom: 14px !important; }
    .stButton>button { border-radius: 10px; background: linear-gradient(90deg, #1E3A8A, #2563EB); color: white; font-weight: 600; border: none; padding: 8px 18px; transition: all 0.25s ease; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35); }
    .audio-box { background: linear-gradient(135deg, #F0FDF4, #DCFCE7); border: 1px solid #86EFAC; padding: 12px; border-radius: 10px; margin-top: 12px; }
    .img-box { background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 12px; padding: 10px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }
    .rule-box { background-color: #EFF6FF; border-left: 4px solid #3B82F6; padding: 10px 14px; border-radius: 8px; margin-bottom: 12px; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# Khởi tạo API & Âm thanh
client = None
if "GEMINI_API_KEY" in st.secrets:
    try: client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    except Exception: pass

def get_lecture_audio(text_script, audio_id):
    filename = f"lecture_{audio_id}.mp3"
    if not os.path.exists(filename):
        try:
            tts = gTTS(text=text_script, lang='vi', slow=False)
            tts.save(filename)
        except Exception: return None
    return filename

def render_svg_base64(svg_string):
    b64 = base64.b64encode(svg_string.encode('utf-8')).decode("utf-8")
    html = f'<div class="img-box"><img src="data:image/svg+xml;base64,{b64}" width="100%" style="max-height: 220px; object-fit: contain;"/></div>'
    st.markdown(html, unsafe_allow_html=True)

# Nạp cơ sở dữ liệu học liệu từ các module chuyên biệt
CURRICULUM_DATA = {"Khối 10": {}, "Khối 11": {}, "Khối 12": {}}

try:
    from data_grade12 import GRADE_12_DATA
    CURRICULUM_DATA["Khối 12"] = GRADE_12_DATA
except Exception:
    pass

try:
    from data_grade11 import GRADE_11_DATA
    CURRICULUM_DATA["Khối 11"] = GRADE_11_DATA
except Exception:
    pass

try:
    from data_grade10 import GRADE_10_DATA
    CURRICULUM_DATA["Khối 10"] = GRADE_10_DATA
except Exception:
    pass

# Quản lý tài khoản
if "auth_user" not in st.session_state: st.session_state["auth_user"] = None
if "students_db" not in st.session_state:
    st.session_state["students_db"] = [
        {"student_id": "HS12_01", "password": "123", "full_name": "Nguyễn Nam", "grade": 12, "flowers": 30},
        {"student_id": "HS11_01", "password": "123", "full_name": "Trần Minh", "grade": 11, "flowers": 30},
        {"student_id": "HS10_01", "password": "123", "full_name": "Lê Ngọc", "grade": 10, "flowers": 35}
    ]

def reward_student_flower(student_id, earned, reason):
    for s in st.session_state["students_db"]:
        if s["student_id"] == student_id:
            s["flowers"] = int(s.get("flowers", 30)) + earned
            st.toast(f"🌸 Tuyệt vời! Em nhận được +{earned} Bông hoa vì: {reason}!")
            if st.session_state["auth_user"] and st.session_state["auth_user"]["student_id"] == student_id:
                st.session_state["auth_user"]["flowers"] = s["flowers"]
            break

# Đăng nhập
if st.session_state["auth_user"] is None:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>📐 HỆ SINH THÁI TỰ HỌC TOÁN THPT 'GSTOÁN'</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569;'>Học liệu số chuẩn hóa 100% bám sát Vở tự học Kết nối tri thức (Khối 10, 11, 12)</p>", unsafe_allow_html=True)
    
    col_l1, col_box, col_l2 = st.columns([1, 1.2, 1])
    with col_box:
        with st.container(border=True):
            st.markdown("### 🔐 Cổng Đăng Nhập")
            user_input = st.text_input("Mã học sinh:", value="HS12_01")
            pass_input = st.text_input("Mật khẩu:", type="password", value="123")
            if st.button("Đăng Nhập Ngay", use_container_width=True):
                found = next((s for s in st.session_state["students_db"] if s["student_id"].upper() == user_input.strip().upper()), None)
                if found and str(found.get("password", "123")) == pass_input.strip():
                    st.session_state["auth_user"] = found
                    st.rerun()
                else: st.error("Sai mã học sinh hoặc mật khẩu!")
    st.stop()

# Sidebar
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state['auth_user']['full_name']}")
    st.caption(f"Mã định danh: **{st.session_state['auth_user']['student_id']}**")
    flowers = st.session_state['auth_user'].get('flowers', 30)
    with st.container(border=True):
        st.markdown(f"<h3 style='text-align: center; color: #BE185D;'>{flowers} 🌸</h3>", unsafe_allow_html=True)
        st.caption("Giải đúng BT +2 hoa. Nghe giảng +1 hoa. Khảo thí +3 hoa!")
    if st.button("🚪 Đăng xuất", use_container_width=True):
        st.session_state["auth_user"] = None
        st.rerun()

# Phân hệ Học sinh
student_info = st.session_state["auth_user"]
c_gr, c_les, c_top = st.columns([1, 1.8, 1.8])
with c_gr:
    user_grade_default = 2 if student_info.get("grade") == 12 else (0 if student_info.get("grade") == 10 else 1)
    sel_grade = st.selectbox("📚 Khối Lớp:", ["Khối 10", "Khối 11", "Khối 12"], index=user_grade_default)

grade_dict = CURRICULUM_DATA.get(sel_grade, {})
if not grade_dict:
    st.warning(f"Dữ liệu của {sel_grade} đang được đồng bộ. Vui lòng thêm file data tương ứng vào repository!")
    st.stop()

with c_les:
    lesson_list = list(grade_dict.keys())
    sel_lesson = st.selectbox(f"📖 Bài học ({len(lesson_list)} bài):", lesson_list)

cur_lesson_obj = grade_dict[sel_lesson]

with c_top:
    topic_list = list(cur_lesson_obj["topics"].keys())
    sel_topic = st.selectbox("🎯 Danh sách Chủ điểm (Vở tự học):", topic_list)

cur_topic_data = cur_lesson_obj["topics"][sel_topic]

# 5 TABS HỌC TẬP
tab1, tab_ex, tab2, tab3, tab4 = st.tabs([
    "📖 Cốt Lõi Kiến Thức (Hình Ảnh & Audio)",
    "💡 Ví Dụ Minh Họa (Bấm Xem Lời Giải)",
    "📝 Học Sinh Tự Giải (Kiểm Minh Chứng)",
    "📸 Trợ Lý AI: Soi Vở & Lời Khuyên",
    "🎯 Phòng Khảo Thí Khách Quan"
])

with tab1:
    st.subheader(f"📌 {cur_lesson_obj.get('chapter', 'Kiến thức trọng tâm')}")
    st.markdown(f"#### {sel_lesson} — *{sel_topic}*")

    col_img, col_n = st.columns([1.2, 1.1])
    with col_img:
        with st.container(border=True):
            st.markdown(f"🖼️ **Hình ảnh minh họa kiến thức (Tạo riêng cho chủ điểm):**")
            render_svg_base64(cur_topic_data.get("svg", ""))
            
            st.markdown("""
            <div class="audio-box">
                <b>🎙️ Âm Thanh Thuyết Minh Chủ Điểm (Trích Vở tự học):</b><br>
                <small>Nghe giảng cô đọng kiến thức cốt lõi và các bẫy sai lầm thường gặp:</small>
            </div>
            """, unsafe_allow_html=True)
            
            audio_hash = hashlib.md5((sel_lesson + sel_topic).encode('utf-8')).hexdigest()[:8]
            lecture_audio_file = get_lecture_audio(cur_topic_data.get("audio", ""), audio_hash)
            if lecture_audio_file: st.audio(lecture_audio_file, format="audio/mp3")

            if st.button("🌸 Đã nghe xong bài giảng vi mô (+1 hoa)", key=f"btn_audio_{sel_topic}"):
                reward_student_flower(student_info["student_id"], 1, "chăm chỉ nghe bài giảng vi mô")
                
    with col_n:
        with st.container(border=True):
            st.markdown("📝 **Ghi Chú Nhanh (Smart Notes)**")
            st.markdown(f"#### 1. Khái niệm & Định lý cốt lõi\n{cur_topic_data.get('theory', '')}")
            st.markdown("#### 2. Công thức Toán học trọng tâm")
            st.markdown(f"$${cur_topic_data.get('formula', '')}$$")
            st.markdown(f"#### 3. Cảnh báo bẫy đề thi\n- ⚠️ **Lưu ý:** {cur_topic_data.get('trap', '')}")

with tab_ex:
    st.subheader(f"💡 Ví Dụ Minh Họa Chuẩn Mực: {sel_topic}")
    st.caption("Danh sách các ví dụ cơ bản (đã loại bỏ bài chứa tham số m và VDC). Bấm vào từng đề bài để xem lời giải chi tiết và học cách trình bày.")
    examples_list = cur_topic_data.get("examples", [])
    for idx, ex_item in enumerate(examples_list):
        with st.expander(f"📌 {ex_item['title']}", expanded=(idx == 0)):
            st.markdown(f"**Đề bài yêu cầu:**\n\n{ex_item['problem']}")
            st.markdown("---")
            st.markdown("**✍️ Lời giải chi tiết chuẩn mực sư phạm:**")
            st.markdown(ex_item["solution"])

with tab2:
    ex = cur_topic_data.get("exercise", {})
    if ex:
        with st.container(border=True):
            st.subheader(f"📝 {ex.get('title', 'Bài tập')}")
            st.markdown(f"**Đề bài:** {ex.get('content', '')}")
            st.markdown("---")
            st.markdown("#### ✍️ Kiểm Minh Chứng: Em hãy tự làm ra nháp và điền kết quả")
            user_submitted_ans = st.text_input("Nhập đáp số của em:", key=f"n_{ex.get('id', '1')}")
            if st.button("🚀 Nộp Bài Giải Để Kiểm Tra Minh Chứng", key=f"chk_{ex.get('id', '1')}", use_container_width=True):
                if user_submitted_ans.strip() == str(ex.get("target", "")).strip():
                    st.balloons()
                    st.success("🎉 CHÍNH XÁC 100%! Em đã tự giải đúng bài tập và xứng đáng nhận thưởng +2 Bông hoa Tri thức!")
                    reward_student_flower(student_info["student_id"], 2, "tự lực giải đúng bài tập")
                else:
                    st.error("❌ Kết quả chưa chính xác! Em hãy xem lại Ví dụ minh họa và thử giải lại ra nháp nhé.")

with tab3:
    st.subheader("💬 Gia Sư AI: Soi Bài Viết Tay & Lời Khuyên Giọng Nói")
    st.caption("Chụp ảnh bài làm hoặc dùng Mic để hỏi AI về các bước đang vướng mắc.")
    st.info("Trợ lý AI đang sẵn sàng hỗ trợ nội dung bài học này.")

with tab4:
    st.subheader(f"🎯 Phòng Khảo Thí & Luyện Đề Chuẩn Hóa ({sel_grade})")
    st.info("Đề khảo thí chuẩn cấu trúc mới của Bộ GD&ĐT.")
