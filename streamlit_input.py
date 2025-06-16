import streamlit as st
island=st.selectbox('企鹅栖息的岛屿',options=['托尔森岛', '比斯科群岛', '德里姆岛'])
sex = st.selectbox('性别', options=['雄性', '雌性'])
bill_length = st.number_input('喙的长度（毫米）', min_value=0.0)
bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0)
flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0)
body_mass = st.number_input('身体质量（克）', min_value=0.0)

st.write("用户输入的数据是：")
st.text(f"岛屿: {island}, 性别: {sex}, 喙长: {bill_length}mm, 喙深: {bill_depth}mm, 翅长: {flipper_length}mm, 体重: {body_mass}g")
