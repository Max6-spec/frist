import streamlit as st

st.set_page_config(page_title='Streamlit 视频播放器', page_icon='🎬')

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

