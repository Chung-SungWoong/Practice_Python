import streamlit as st
import datetime

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)
st.write('선택한 날짜:',d)

data_list = {1,2,3,4,5,6,7,8,9,10}

st.write('''

''')

st.line_chart(data_list)