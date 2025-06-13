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
col1, col2 = st.columns([4, 6])


with col1:
    st.header("个人信息表单")
    #设置蓝条
    st.markdown("""
<hr style="height:5px;border:none;color:#1e90ff;background-color:#1e90ff;"/>
""", unsafe_allow_html=True)
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
        st.session_state['expectation'] = st.slider("💰 期望薪资范围（元）", 5000,50000,(6000,15000))
        
        # 其他信息
        st.session_state['bio'] = st.text_area("个人简介", placeholder="请简要介绍自己")
        st.session_state['time'] = st.selectbox("⏰ 每日最佳联系时间", time)
        uploaded_photo = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png", "gif"])
        if uploaded_photo is not None:
        # 显示上传的照片
            st.session_state['photo'] = uploaded_photo
            st.image(uploaded_photo, caption="您上传的照片")
        else:
            st.session_state['photo'] = None
        submitted = st.form_submit_button("生成简历")

with col2:
    st.header("简历实时预览")
    #设置蓝条
    st.markdown("""
<hr style="height:5px;border:none;color:#1e90ff;background-color:#1e90ff;"/>
""", unsafe_allow_html=True)

    # 检查是否有表单数据
    if 'name' in st.session_state:
        # 个人信息部分
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"### {st.session_state.get('name', '')}")
            if st.session_state['photo'] is not None:
                st.image(st.session_state['photo'], width=150)
            st.write(f"**职位:** {st.session_state.get('position', '')}")
            st.write(f"**电话:** {st.session_state.get('phone', '')}")
            st.write(f"**邮箱:** {st.session_state.get('email', '')}")
            st.write(f"**出生日期:** {st.session_state.get('birth_date', '')}")
            
        with col2:
            
            st.write(f"**性别:** {st.session_state.get('gender', '')}")
            st.write(f"**学历:** {st.session_state.get('education', '')}")
            st.write(f"**工作经验:** {st.session_state.get('experience', 0)}年")
            st.write(f"**期望薪资:** {st.session_state.get('expectation', (0, 0))[0]} - {st.session_state.get('expectation', (0, 0))[1]}元")
            st.write(f"**最佳联系时间:** {st.session_state.get('time', '')}")
            st.write(f"**语言能力:** {', '.join(st.session_state.get('languages', []))}")

        #分隔线
        st.markdown('***')


        # 个人简介部分
        st.write("### 个人简介")
        st.write(st.session_state['bio'])


        # 专业技能部分
        st.write("### 专业技能")
        for skill in st.session_state['skills']:
            st.write(f"- {skill}")
        #分隔线
        st.markdown('***')
    else:
        # 没有表单数据时显示提示
        st.info("请在左侧表单中填写您的个人信息，实时预览将显示在这里。")
