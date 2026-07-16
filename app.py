
import pandas as pd
import streamlit as st 

st.header("헤더")

no=st.text_input("학번:")
name=st.text_input("이름:")
major=st.text_input("전공:")

if 'students' not in st.session_state :
    st.session_state['students']=[]

if st.button("등록") :
    st.session_state['students'].append(
        {
            '학번': no,
            '이름' : name,
            '전공' : major
        }
    )

df = pd.DataFrame(st.session_state['students'])

st.subheader("학생 정보 : ")
st.dataframe(df)
