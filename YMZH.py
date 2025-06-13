import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import random
st.set_page_config(
    page_title="五行合一",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown('# :blue[广西职业师范学院]')

tab1,tab2,tab3, tab4, tab5=st.tabs(["数字档案","南宁美食地图","相册","视频播放器","个人简历"])

with tab1:
    st.title('🕶️学生 小成 -数字档案')
    st.header('🔑基础信息')

    st.text("学生ID:2023-2-01") 

    st.markdown("注册时间:`2023-9-10 16:41:54` |精神状态：✅正常")
    st.markdown("当前教室: `实训楼301` |安全等级: `绝密`")


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
        '状态':['✅ 完成','🕒 进行中', '❌未完成'],
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



with tab2:

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
        c1, c2 = st.columns(2)
        c1.metric(label='评分', value="4.9/5.0")
        c2.metric(label='人均消费', value="83元")
        st.markdown("**推荐菜品：**")
        st.write("・ 大头椰椰水锅  \n・ 腊味煲仔饭  \n・ 文昌鸡")
    
        st.markdown('### 当前拥挤程度')
        st.text("76%拥挤")
        st.progress(76)
    
    elif dp == '青和居酒屋':
        st.subheader('青和居酒屋')
        c1, c2 = st.columns(2)
        c1.metric(label='评分', value="4.5/5.0")
        c2.metric(label='人均消费', value="59元")
        st.markdown("**推荐菜品：**")
        st.write("・ 鳗鱼  \n・ 人气荔枝酒  \n・ 前菜四品")
        st.markdown('### 当前拥挤程度')
        st.text("48%拥挤")
        st.progress(48)
    
    elif dp == '达美乐比萨':
        st.subheader('达美乐比萨')
        c1, c2 = st.columns(2)
        c1.metric(label='评分', value="5.0/5.0")
        c2.metric(label='人均消费', value="53元")
        st.markdown("**推荐菜品：**")
        st.write("・ 经典意式肉酱比萨  \n・ 金沙咸蛋黄嫩鸡比萨  \n・ 苏丹王榴莲多多比萨")
        st.markdown('### 当前拥挤程度')
        st.text("92%拥挤")
        st.progress(92)
    
    elif dp == '德意客意式餐厅':
        st.subheader('德意客意式餐厅')
        c1, c2 = st.columns(2)
        c1.metric(label='评分', value="4.8/5.0")
        c2.metric(label='人均消费', value="54元")
        st.markdown("**推荐菜品：**")
        st.write("・ 澳洲黑松露原切肉  \n・ 营养儿童餐  \n・ 金桔百香果汁")
        st.markdown('### 当前拥挤程度')
        st.text("69%拥挤")
        st.progress(69)
    else:
        st.subheader('Myway咖啡·小食光')
        c1, c2 = st.columns(2)
        c1.metric(label='评分', value="4.1/5.0")
        c2.metric(label='人均消费', value="57元")
        st.markdown("**推荐菜品：**")
        st.write("・ 太阳蛋菠萝油  \n・ 番茄肉酱意面  \n・ 诸事顺利")
        st.markdown('### 当前拥挤程度')
        st.text("37%拥挤")
        st.progress(37)

    import random

    lunch_options = [
    {
        "name": "椰子鸡",
        "image": "https://picsum.photos/800/400?random=1",
        "description": "享受美味！"
        
    },
    {
        "name": "烤猪蹄",
        "image": "https://pic.nximg.cn/file/20221031/2611739_145650583108_2.jpg",
        "description": "享受美味！"
    },
    {
        "name": "牛排",
        "image": "https://img95.699pic.com/photo/50082/6444.jpg_wh860.jpg",
        "description": "享受美味！"
    },
    {
        "name": "披萨",
        "image": "https://picsum.photos/800/400?random=6",
        "description": "享受美味！"
    },
    {
        "name": "鳗鱼饭",
        "image": "https://picsum.photos/800/400?random=5",
        "description": "享受美味！"
    }
    
    ]

    st.header('🎲今日午餐推荐')
    if st.button("帮我选午餐！"):
    # 随机选择一个午餐选项
        selected_lunch = random.choice(lunch_options)
        st.subheader(f"推荐午餐：{selected_lunch['name']}")
        st.image(selected_lunch["image"], caption=selected_lunch["description"], width=400)



with tab3:

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



with tab4:


# 初始化当前视频索引
    if 'current_video' not in st.session_state:
        st.session_state['current_video'] = 0

    # 视频数据
    video_library = [
    {
        'cover_url': 'https://images.wallpapersden.com/image/download/anime-naruto-hd-2023-ai_bW5mbGmUmZqaraWkpJRma21lrWZlamU.jpg',
        'video_url': 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
          'title': '动画',
        'description': '视觉盛宴',
        'duration': '0:10',
        'category': '动画1'
    },{
        
        'cover_url': 'https://img.fotocommunity.com/portrait-de-tigre-b414cb5c-b28d-4e13-a956-c8503d730e77.jpg?height=1000',
        'video_url': 'https://www.w3schools.com/html/movie.mp4',
        'title': '野生动物',
        'description': '自然纪录片',
        'duration': '0:12',
        'category': '动物',
    },{
        
        'cover_url': 'http://img.netbian.com/file/2023/0428/001406UwUZU.jpg',
        'video_url': 'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title': '动漫',
        'description': '美女的冒险',
        'duration': '0:52',
        'category': '动画2',
    }
    ]
    st.title('Streamlit 视频播放器')
    st.write('点击下方视频封面选择要播放的视频')

    current = video_library[st.session_state['current_video']]

    st.header('视频播放')
    st.video(current['video_url'])

    st.markdown(f"""
    - **{current['title']}**  
      描述: {current['description']}  
      时长: {current['duration']} | 分类: {current['category']}  
    """)




    st.header('视频库')
    st.text('点击图片选择视频')


    dp=st.selectbox('按分类筛选：',['动画1','动物','动画2','全部'])
    if dp=='动画1':
        st.subheader('动画1')
        video_file = 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'
        st.video(video_file)
        st.text('动画1')
        st.text('0:10|动画')
    
    elif dp=='动物':
        st.subheader('动物')
        video_file = 'https://www.w3schools.com/html/movie.mp4'
        st.video(video_file)
        st.text('动物')
        st.text('0:12|动物')
    
    elif dp=='动画2':
        st.subheader('动画2')
        video_file = 'https://media.w3.org/2010/05/sintel/trailer.mp4'
        st.video(video_file)
        st.text('动画2')
        st.text('0:52|动画2')
    
    else:
        st.subheader('动画1')
        video_file = 'https://www.w3school.com.cn/example/html5/mov_bbb.mp4'
        st.video(video_file)
        st.text('动画1')
        st.text('0:10|动画')

        st.subheader('动物')
        video_file = 'https://www.w3schools.com/html/movie.mp4'
        st.video(video_file)
        st.text('动物')
        st.text('0:12|动物')
    
        st.subheader('动画2')
        video_file = 'https://media.w3.org/2010/05/sintel/trailer.mp4'
        st.video(video_file)
        st.text('动画2')
        st.text('0:52|动画2')


with tab5:
    
    language=["英语", "日语", "法语", "德语", "西班牙语", "俄语", "汉语"]
    time=["9:00","9:30","10:00" ,"10:30", "11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30", "随时可联系"]
    skills= ["Python编程", "数据分析", "机器学习", "前端开发", "后端开发", "数据库管理", "项目管理"]


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
            st.session_state['languages'] = st.multiselect("语言能力", language)
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

