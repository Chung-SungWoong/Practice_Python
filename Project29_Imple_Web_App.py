import streamlit as st
import datetime
import pyupbit


d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

# st.write('비트코인 1일 차트')
# ticker = 'KRC-BTC'
# to = str(d+datetime.timedelta(days=1))
# count = 24
# price_now = pyupbit.get_ohlcv(ticker=ticker, interval = interval, to=to, count=count)
# st.line_chart(price_now.close)
st.write('선택한 날짜:',d)

data_list = {1,2,3,4,5,6,7,8,9,10}

st.write('''

''')

st.line_chart(data_list)