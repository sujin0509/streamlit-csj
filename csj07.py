import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def  plotting_demo():
    
    #uploaded_file = st.file_uploader("Choose a file")
    # money=pd.read_csv(uploaded_file)
    money = pd.read_csv("money_data7.csv")

    option = st.selectbox(
        'How would you like to choice year ?',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('현재 선택년도 :', option)

    money = money[:] [money['A_YEAR']== option2]
    
    global  aa
    
    aa = money

    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='lightcoral' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('America rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='lightsteelblue' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='darkseagreen' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='peru' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('House Price')

    st.pyplot(fig)
    #st.dataframe(money)
       

        
        
def bar_chart():

    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

    df = pd.DataFrame([]) 

    for    i    in     years: 
        df1 = pd.read_html( url + i  )[0]
        df1['년도'] =  i 
        df = pd.concat([df, df1], axis=0)
        
    baseball = df    

    baseball.팀.replace({'두산':'Dusan','삼성':'SS','키움':'KU','한화': 'HH','롯데':'Lotte','넥센':'NecSen'}, inplace=True)
    
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

    option2 = option

    st.write('현재 선택년도 : ', option)

    df7  =  baseball[:] [ baseball.년도==option2 ]
    x = df7.팀
    y = df7.승률
    
    global  bb
    
    bb = df7
    
    fig, ax = plt.subplots(figsize=(12,8))

    colors = ['mistyrose','lightpink','moccasin','peachpuff','darkkhaki','tan','lavender','lightsteelblue','thistle','plum']
    plt.bar(  x,  y,  color= colors ) 

    for   num ,   v    in   enumerate( y ):
        plt.text (  num -0.4  ,   v + 0.01 ,  v   )

    plt.title( "year korea baseball winrate data", position=(0.5,1.1))
    st.pyplot(fig)
    #st.dataframe(df7)

     
        
        
st.set_page_config(layout="centered")          
        

with st.form(key ='Form1'):
    with st.sidebar:
        
        select_language = st.sidebar.radio('데이터 분석 결과', ('금리와 집값 파악', '야구 순위와 승률 파악', '기타 데이터'))
        
        
if select_language =='금리와 집값 파악':           
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
   
    with tab1:
        tab1.subheader("A tab with a chart")
        plotting_demo()
        
    with tab2:
        tab2.subheader("A tab with the data")
        st.dataframe(aa)

        
elif select_language =='야구 순위와 승률 파악':
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
   
    with tab1:
        tab1.subheader("A tab with a chart")
        bar_chart()
        
    with tab2:
        tab2.subheader("A tab with the data")
        st.dataframe(bb)
        
