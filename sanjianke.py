import streamlit as st

st.set_page_config(page_title='相册')

images = [{
"url":"https://www.sea-help.eu/wp-content/uploads/2023-04-05_seahelp_meeresleuchten-bioluminescence.jpg",
    "caption":'海洋'},
{"url":"https://images6.alphacoders.com/773/773201.jpg",
    "caption":'海豚'},
{"url":"https://wallup.net/wp-content/uploads/2019/10/97666-landscape-sea-sunset-beauty-coast-beach-water-sky-lighthouse-sand-reflection-shine.jpg",
"caption":'海边落日'}
]

# 初始化当前图片索引
if 'current_image_index' not in st.session_state:
    st.session_state.current_image_index = 0


# 图片显示区域
def display_image():
    try:
        current_image = images[st.session_state.current_image_index]
        
        # 验证数据格式
        if not isinstance(current_image, dict):
            raise ValueError("图片数据必须是字典格式")
        if "url" not in current_image or "caption" not in current_image:
            raise ValueError("图片数据必须包含'url'和'caption'字段")
        if not current_image["url"].startswith(('http://', 'https://')):
            raise ValueError("图片URL格式不正确")
        
        # 显示图片
        st.image(
            current_image["url"],
            caption=current_image["caption"],
            use_column_width=True
        )
        
    except Exception as e:
        st.error(f"图片加载失败: {str(e)}")
        st.warning("正在尝试加载默认图片...")
        st.image(
            "https://via.placeholder.com/600x400?text=图片加载失败",
            caption="默认占位图",
            use_column_width=True
        )

# 主界面
st.title("海洋美景相册")
display_image()









# 创建两列布局放置按钮
col1, col2 = st.columns(2)

with col1:
    # 上一张按钮
    if st.button("上一张"):
        st.session_state.current_image_index -= 1
        # 如果已经是第一张，循环到最后一张
        if st.session_state.current_image_index < 0:
            st.session_state.current_image_index = len(images) - 1
        st.rerun()

with col2:
    # 下一张按钮
    if st.button("下一张"):
        st.session_state.current_image_index += 1
        # 如果已经是最后一张，循环到第一张
        if st.session_state.current_image_index >= len(images):
            st.session_state.current_image_index = 0
        st.rerun()
