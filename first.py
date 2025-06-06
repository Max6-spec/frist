import streamlit as st
import pandas as pd
st.title('🕶️学生 小成 -数字档案')
st.header('🔑基础信息')

st.text("学生ID:2023-2-01") 

st.markdown("注册时间: '2023-9-10 16:41:54' |精神状态：✅正常")
st.markdown("当前教室: '实训楼301' |安全等级: '绝密'")


st.subheader('📊技能矩阵')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="95%", delta="2%")
c2.metric(label="Python", value="87%", delta="-1%")
c3.metric(label="Java", value="68%", delta="-10%")

st.markdown('### Streamlit课程进度')
st.text("streamlit课程进度")
st.progress(25)#Assuming 25% progress


st.markdown("## 📝任务日志")

data={
    '日期':["2023-10-01","2023-10-05","2023-10-12"],
    '任务':['学生数字档案','课程管理系统','数据图表展示'],
    '状态':['✔ 完成','● 进行中', '✕ 未完成'],
    '难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']
}
index=pd.Series([0,1,2],name='序号')
df=pd.DataFrame(data,index=index)

st.write(df)

with st.container():
    st.markdown("🔐最新代码成果")
    st.code('''
def matrix_breach( ):
    while True:
        if detect_vulnerability( ):
	exploit( )
	return"ACCESS GRANTED"
        else:
	stealth_evade( )
''')

st.markdown('***')

st.markdown("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")
st.markdown("`>> TARGET:` 课程管理系统")
st.markdown("`>> COUNTDOWN:` 2025-06-04 16:17:59")
st.markdown("系统状态：在线连接状态：已加密")