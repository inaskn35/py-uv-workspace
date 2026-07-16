
import streamlit as st

#앱의 메인 타이틀을 출력 - 한번만 작성해주면 된다
st.title('oo대학교 등록 현황')

#큰 제목을 출력
st.header("학생 등록 명단")

#일반적인 문자열을 그대로 출력
st.text('26년 2학기 등록된 학생 명단입니다.')

name = st.selectbox("이름을 선택하세요", ["홍길동", "이순신", "유관순"])

regisno = st.selectbox("학번을 선택하세요", ["202601", "202602", "202603"])

# 드롭다운 형태로 항목 선택
major = st.selectbox("전공을 선택하세요", ["컴퓨터공학", "데이터사이언스", "인공지능학"])

st.write(f" **{name}** 학생(학번: **{regisno}**)의 등록 전공은 **{major}**입니다.")

st.text('학생증 사진을 등록하세요 3*4 규격. jpg,jpeg,png만 가능.')

import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("파일을 선택해주세요", accept_multiple_files=True,
type=["png","jpg","jpeg"])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    # st.write(bytes_data)
    st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)


