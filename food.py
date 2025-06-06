import streamlit as st  # 导入Streamlit并用st代表它
import pandas as pd
import numpy as np

st.set_page_config(page_title='南宁美食地图')

st.title('🍔南宁美食探索')
st.text('探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。')

st.header('📍南宁美食地图')

#创建简单的地图
st.map(pd.DataFrame({
    "latitude":[22.812163,22.817654,22.813661,22.684570,22.853129],   
    "longitude":[108.392937,108.334131,108.383764,108.264763,108.225565],
}))


st.header('⭐餐厅评分')
data = {
    '店铺名称': ["大头椰·椰子鸡火锅", "青和居酒屋", "达美乐比萨", "德意客意式餐厅", "Myway咖啡·小食光"],
    '评分': [4.9, 4.5, 5.0, 4.8, 4.1] 
}
df = pd.DataFrame(data)
# 显示条形图
st.bar_chart(
    df.set_index('店铺名称'),
    width=400,
    height=300,
    use_container_width=False)


st.header('💰不同类型餐厅价格')

data = {
    "餐厅类型": ["中餐", "日式", "快餐", "西餐"],
    "平均价格(元)": [45, 80, 120, 60],
    "最低价格(元)": [30, 50, 90, 40],
    "最高价格(元)": [60, 110, 150, 80]
}
df = pd.DataFrame(data).set_index("餐厅类型")

# 通过width、height和use_container_width指定折线图的宽度和高度
st.line_chart(df, width=600, height=500, use_container_width=False)



st.header('🕥用餐高峰时段')
data={
    '时间':[11,12,13,14,18],
    "大头椰·椰子鸡火锅":[50,100,120,100,90],
    "青和居酒屋":[40,45,50,45,60],
    "达美乐比萨":[50,70,100,85,80],
    "德意客意式餐厅":[30,50,70,65,90],
    "Myway咖啡·小食光":[25,40,50,45,60]
}

df=pd.DataFrame(data)
index = pd.Series([1,2,3,4,5], name='序号')
df.index = index

st.area_chart(df, y=["大头椰·椰子鸡火锅", "青和居酒屋", "达美乐比萨", "德意客意式餐厅", "Myway咖啡·小食光"])



def my_format_func(option):
    return f'{option}'

st.header('🍽餐厅详情')
dp = st.selectbox(
    '选择餐厅查看详情',
    ["大头椰·椰子鸡火锅", "青和居酒屋", "达美乐比萨", "德意客意式餐厅", "Myway咖啡·小食光"],
    format_func=my_format_func,
    index=0
)

if dp == '大头椰·椰子鸡火锅':
    
    st.subheader('大头椰·椰子鸡火锅')
    c1,c2=st.columns(2)
    c1.metric(labe='评分',value="4.9/5.0 ")
    c2.metric(labe='推荐菜品：',value="· 大头椰椰水锅",value="· 腊味煲仔饭",value="· 文昌鸡")
    st.metric(label='人均消费',value="83元")
    
    st.markdown('### 当前拥挤程度')
    st.text("76%拥挤")
    st.progress(76)
elif dp == '青和居酒屋':
    st.subheader('青和居酒屋')
    st.markdown("""
    **评分**  
    4.5/5.0  

    **人均消费**  
    59元  

    **推荐菜品：**  
    - 鳗鱼 
    - 人气荔枝酒  
    - 前菜四品
    """)
    st.markdown('### 当前拥挤程度')
    st.text("48%拥挤")
    st.progress(48)
elif dp == '达美乐比萨':
    st.subheader('达美乐比萨')
    st.markdown("""
    **评分**  
    5.0/5.0  

    **人均消费**  
    53元  

    **推荐菜品：**  
    - 经典意式肉酱比萨
    - 金沙咸蛋黄嫩鸡比萨
    - 苏丹王榴莲多多比萨
    """)
    st.markdown('### 当前拥挤程度')
    st.text("92%拥挤")
    st.progress(92)
elif dp == '德意客意式餐厅':
    st.subheader('德意客意式餐厅')
    st.markdown("""
    **评分**  
    4.8/5.0  

    **人均消费**  
    54元  

    **推荐菜品：**  
    - 澳洲黑松露原切肉
    - 营养儿童餐
    - 金桔百香果汁
    """)
    st.markdown('### 当前拥挤程度')
    st.text("69%拥挤")
    st.progress(69)
else:
    st.subheader('Myway咖啡·小食光')
    st.markdown("""
    **评分**  
    4.1/5.0  

    **人均消费**  
    57元  

    **推荐菜品：**  
    - 太阳蛋菠萝油
    - 番茄肉酱意面
    - 诸事顺利
    """)
    st.markdown('### 当前拥挤程度')
    st.text("37%拥挤")
    st.progress(37)
