import streamlit as st
import pickle
import pandas as pd

# 设置页面配置
st.set_page_config(
    page_title="企鹅物种分类器",
    page_icon="🐧",
    layout="wide",

)


with st.sidebar:
    st.image('rigth_logo.png',width=120)
    st.title('🐧 企鹅分类器导航')
    page=st.selectbox("📄 请选择页面",['简介页面','预测分类页面'])
    
if page=='简介页面':
    st.title("🐧 企鹅分类器：")
    st.header('📊数据集介绍')
    st.markdown('''帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门训练。
该数据集是由Gorman等收集，并发布在一个名为palmerpenguins的R语言包，以对南极企鹅种类进行分类和研究。
该数据集记录了344行观测数据，包含3个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各种信息。
''')

    st.header('📸 三种企鹅的卡通图像')
    st.image('penguins.png', caption="左到右依次为：帽带企鹅、巴布亚企鹅、阿德利企鹅", use_container_width=True)

elif page=="预测分类页面":
    st.header('🔍预测企鹅分类')
    st.markdown('这个web应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！👇')

    #该页面是3：0.5：2的布局
    col_form,col,col_logo=st.columns([3,0.5,2])
    
    with col_form:
        #运用表单和表单提交按钮
        
        island=st.selectbox('🌍企鹅栖息的岛屿',options=['托尔森岛', '比斯科群岛', '德里姆岛'])
        sex = st.selectbox('🚻性别', options=['雄性', '雌性'])
        bill_length = st.number_input('📏 喙的长度（毫米）', min_value=0.0)        
        bill_depth = st.number_input('📐喙的深度（毫米）', min_value=0.0)
        flipper_length = st.number_input('🦿 翅膀的长度（毫米）', min_value=0.0)
        body_mass = st.number_input('⚖️身体质量（克）', min_value=0.0)
        submitted=st.button('🐧预测分类')
        
        #初始化数据预处理格式中与岛屿相关的变量
        island_biscoe,island_dream,island_torgerson=0,0,0
        
        #根据用户输入的岛屿数据更改对应的值
        if island == '比斯科群岛':
            island_biscoe=1
        elif island == '德里姆岛':
            island_dream=1
        elif island == '托尔森岛':
            island_torgerson=1
            
        #初始化数据预处理格式中与性别相关的变量
        sex_female,sex_male=0,0
        
        #根据用户输入的性别数据更改对应的值       
        if sex=='雌性':
            sex_female=1
        elif sex=='雄性':
            sex_male=1
            
        #转化为数据预处理的格式
        format_data=[bill_length, bill_depth, flipper_length, body_mass,island_dream, island_torgerson, island_biscoe, sex_male,sex_female]

        with open('rfc_model.pkl', 'rb') as f:
            rfc_model = pickle.load(f)
        with open('output_uniques.pkl', 'rb') as f:
            output_uniques_map = pickle.load(f)
            
        if submitted:
            format_data_df=pd.DataFrame(data=[format_data],columns=rfc_model.feature_names_in_)
            predict_result_code=rfc_model.predict(format_data_df)
            predict_result_species=output_uniques_map[predict_result_code][0]
            st.write(f'🎉根据您输入的数据，预测该企鹅的物种名称是:**{predict_result_species}**')

        with col_logo:
            if not submitted:
                st.image('rigth_logo.png',width=300, caption="🐧企鹅分类器")
            else:
                st.image(f'{predict_result_species}.png',width=300,caption="预测结果")






# 侧边栏 - 站点辅助
with st.sidebar:
    st.header("📌 关于本站")
    
    # 网站简介
    st.markdown("""
    **企鹅分类科普平台**是一个致力于提供全面企鹅知识的教育资源。
    我们通过科学分类、图片展示和生态解读，帮助公众了解这些迷人的南极鸟类。
    """)
    
    # 联系方式
    st.subheader("📧 联系我们")
    st.write("有任何问题或建议？请通过以下方式联系我们：")
    st.write("- 邮箱：info@penguinclassifier.org")
    st.write("- 社交媒体：[Twitter](https://twitter.com/penguin_science) | [Instagram](https://www.instagram.com/penguin_lovers/)")
    
    # 订阅更新
    st.subheader("📫 订阅企鹅研究动态")
    email = st.text_input("输入您的邮箱地址", placeholder="your.email@example.com")
    if st.button("订阅"):
        if email:
            st.success(f"感谢订阅！您将收到最新的企鹅研究和保护资讯。")
        else:
            st.warning("请输入有效的邮箱地址")
    
    # 友情链接
    st.subheader("🔗 相关资源")
    for name, url in 友情链接.items():
        st.markdown(f"- [{name}]({url})")
    
    # 版权信息
    st.markdown("---")
    st.caption("© 2025 企鹅分类科普平台 | 保留所有权利")













