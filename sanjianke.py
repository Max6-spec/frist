import streamlit as st

st.set_page_config(page_title='bird')
st.image("https://www.lilesnet.com/wow/birds/1-birds.jpg", caption='小鸟')

import streamlit as st

# 图片URL列表
images = [
    "https://www.sea-help.eu/wp-content/uploads/2023-04-05_seahelp_meeresleuchten-bioluminescence.jpg",caption='海洋',
    "https://images6.alphacoders.com/773/773201.jpg",caption='海豚',
    "https://wallup.net/wp-content/uploads/2019/10/97666-landscape-sea-sunset-beauty-coast-beach-water-sky-lighthouse-sand-reflection-shine.jpg"caption='落日']

# 初始化当前图片索引
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0

st.subheader("相册")

# 显示当前图片
current_image = images[st.session_state.current_image_index]
st.image(current_image)

# 图片标题（可以根据需要自定义）
image_titles = ["海洋", "海豚", "落日"]
st.write(image_titles[st.session_state.current_image_index])

# 创建两列布局放置按钮
col1, col2 = st.columns(2)

with col1:
    # 上一张按钮
    if st.button("上一张"):
        st.session_state.current_image_index -= 1
        # 如果已经是第一张，循环到最后一张
        if st.session_state.current_image_index < 0:
            st.session_state.current_image_index = len(images) - 1

with col2:
    # 下一张按钮
    if st.button("下一张"):
        st.session_state.current_image_index += 1
        # 如果已经是最后一张，循环到第一张
        if st.session_state.current_image_index >= len(images):
            st.session_state.current_image_index = 0
