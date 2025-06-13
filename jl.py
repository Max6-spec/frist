import streamlit as st
from datetime import datetime


language=["英语", "日语", "法语", "德语", "西班牙语", "俄语", "汉语"]
time=["9:00","9:30","10:00" ,"10:30", "11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30", "随时可联系"]
skills= ["Python编程", "数据分析", "机器学习", "前端开发", "后端开发", "数据库管理", "项目管理"]
# 页面配置
st.set_page_config(
    page_title="个人简历生成器",page_icon="📄",layout="wide")

# 标题
st.title("🎨个人简历生成器")
st.write("使用streamlit创建您的个性化简历")

# 创建两列布局
col1, col2 = st.columns([1, 2])

with col1:
    st.header("个人信息表单")
    
    # 个人信息输入
    with st.form("personal_info"):
        st.session_state['name'] = st.text_input("姓名", placeholder="请输入您的姓名")
        st.session_state['position'] = st.text_input("职位", placeholder="请输入您的职位")
        st.session_state['phone'] = st.text_input("📱 电话", placeholder="请输入您的电话")
        st.session_state['email'] = st.text_input("📧 邮箱", placeholder="请输入您的邮箱")
        st.session_state['birth_date'] = st.text_input("🎂 出生日期",placeholder="请输入您的出生日期")
        
        st.write("🚻 性别")
        st.session_state['gender'] =check_1 = st.checkbox('男', value=True)
        st.session_state['gender'] =check_1 = st.checkbox('女')
        st.session_state['gender'] = check_1 = st.checkbox('其他')
        
        st.session_state['education'] = st.selectbox("🎓 学历", ["初中","高中","本科", "硕士", "博士", "大专", "其他"])
        st.session_state['languafes'] = st.multiselect("语言能力", language)
        st.session_state['skills'] = st.multiselect("技能（可多选）", skills)
        st.session_state['experience'] = st.slider("⏳ 工作经验(年)", 0, 30, 0)
        st.session_state['expectatioon'] = st.slider("💰 期望薪资范围（元）", 5000,50000,(6000,15000))
        
        # 其他信息
        st.session_state['bio'] = st.text_area("个人简介", placeholder="请简要介绍自己")
        st.session_state['time'] = st.selectbox("⏰ 每日最佳联系时间", time)
        uploaded_photo = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png", "gif"])
        if uploaded_photo is not None:
        # 显示上传的照片
                st.image(uploaded_photo, caption="您上传的照片")
        submitted = st.form_submit_button("生成简历")

with col2:
    st.header("简历实时预览")
    current_name = st.session_state.get("name_input", "姓名")
    current_position = st.session_state.get("position_input", "职位")
    current_email = st.session_state.get("email_input", "邮箱")
    current_birth_date = st.session_state.get("birth_date_input", datetime(1999, 12, 31))
    current_gender = st.session_state.get("gender_radio", "性别")
    current_education = st.session_state.get("education_select", "学历")
    current_experience = st.session_state.get("experience_slider", 0)
    current_salary_range = st.session_state.get("salary_slider", (10000, 20000))
    current_communication_score = st.session_state.get("communication_slider", 90)
    current_languages = st.session_state.get("languages_multiselect", [])
    current_bio = st.session_state.get("bio_textarea", "这个人很熟悉，她需要写作的对话。")
    

