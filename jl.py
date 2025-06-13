import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="📄",
    layout="wide"
)

# 标题
st.title("个人简历生成器")

# 创建两列布局
col1, col2 = st.columns([1, 2])

with col1:
    st.header("个人信息表单")
    
    # 个人信息输入
    with st.form("personal_info"):
         st.session_state['name'] = st.text_input("姓名", placeholder="请输入您的姓名")
         st.session_state['position'] = st.text_input("职位", placeholder="请输入您的职位")
         st.session_state['major'] = st.text_input("专业", placeholder="请输入您的专业")
         st.session_state['email'] = st.text_input("邮箱", placeholder="请输入您的邮箱")
        
        # 分两列布局
        col1_1, col1_2 = st.columns(2)
        with col1_1:
             st.session_state['birth_date'] = st.date_input("出生日期", value=datetime(1990, 1, 1))
             st.session_state['gender'] = st.radio("性别", ["男", "女"])
        with col1_2:
             st.session_state['education'] = st.selectbox("学历", ["初中","高中","本科", "硕士", "博士", "大专", "其他"])
             st.session_state['experience'] = st.slider("工作经验(年)", 0, 30, 0)
        
        # 其他信息
         st.session_state['work_period'] = st.text_input("工作时间", placeholder="例如: 2005-2020/05")
         st.session_state['self_management'] = st.text_area("自我管理方式", placeholder="请描述您的自我管理方式")
         st.session_state['languages'] = st.text_input("语言能力", placeholder="例如: 英语(流利), 日语(基础)")
         st.session_state['bio'] = st.text_area("个人简介", placeholder="请简要介绍自己")
        
        submitted = st.form_submit_button("生成简历")

with col2:
    st.header("简历实时预览")
    
    # 简历预览样式
    if submitted or name:
        st.markdown(f"""
        <div style="
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            background-color: #f9f9f9;
            margin-bottom: 20px;
        ">
            <h2 style="color: #333; border-bottom: 2px solid #666; padding-bottom: 10px;">{name if name else "姓名"}</h2>
            <p><strong>职位:</strong> {position if position else "未填写"}</p>
            <p><strong>专业:</strong> {major if major else "未填写"}</p>
            <p><strong>邮箱:</strong> {email if email else "未填写"}</p>
            
            <div style="display: flex; justify-content: space-between; margin-top: 15px;">
                <div>
                    <p><strong>出生日期:</strong> {birth_date.strftime('%Y/%m/%d') if birth_date else "未填写"}</p>
                    <p><strong>性别:</strong> {gender if gender else "未填写"}</p>
                </div>
                <div>
                    <p><strong>学历:</strong> {education if education else "未填写"}</p>
                    <p><strong>工作经验:</strong> {experience}年</p>
                </div>
            </div>
            
            <div style="margin-top: 15px;">
                <p><strong>工作时间:</strong> {work_period if work_period else "未填写"}</p>
                <p><strong>自我管理方式:</strong> {self_management if self_management else "未填写"}</p>
                <p><strong>语言能力:</strong> {languages if languages else "未填写"}</p>
            </div>
            
            <div style="margin-top: 20px;">
                <h3 style="color: #444; border-bottom: 1px solid #ccc; padding-bottom: 5px;">个人简介</h3>
                <p>{bio if bio else "这个人很熟悉，没有留下任何介绍。"}</p>
            </div>
            
            <div style="margin-top: 30px; text-align: center; font-size: 0.9em; color: #666;">
                <p>作者简历发布，欢迎您咨询！</p>
                <p>请登录官网获取更多简历</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("请在左侧填写个人信息以生成简历预览")

# 添加一些样式
st.markdown("""
<style>
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        border-radius: 5px;
    }
    .stButton button {
        width: 100%;
        border-radius: 5px;
        background-color: #4CAF50;
        color: white;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
