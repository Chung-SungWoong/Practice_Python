import pyupbit
import sqlite3
import datetime
import pandas as pd

def date_range(start,end):                                          # datetime로 시작 날짜와 종료 날짜의 모든 날을 리스트 형태로 반환
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)                      # 시작 날과 종료날의 데이터를 모으기 위해서는 하루를 더해 구해야한다
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1)
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days + 1)]
    return dates

dates = date_range("2021-01-30","2021-02-02")               # 2023년 데이터는 불러 올 수 없음, data type None 이 뜸

print(dates)

for day in reversed(dates):                         # 날짜를 반대로 하여 최신 날짜가 위로 오게 바꾸기
    myDay = day + ' 00:00'
    print(myDay)

    ticker = 'KRW-BTC'
    interval = ' minute1'
    to = myDay
    count = 1440                                    # 하루 24시간을 분으로 치환
    price_now = pyupbit.get_ohlcv(ticker=ticker, interval= interval,to=to, count=count)         # 데이터 요청

    print(price_now)

    db_path = r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Crypto_Coin.db"
    
    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql("BTC", con, if_exists='append')

    con.close
'''

    readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC' " , con, index_col = 'index')

    readed_df.to_sql('BTC_NEW', con, if_exists = 'replace')
    
    print(readed_df)
'''


"""
ticker = 'KRW-BTC'
interval = 'minute1'
to = '2023-3-20'
count = 200
price_now = pyupbit.get_ohlcv(ticker = ticker, interval = interval, to = to, count=count)

db_path = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Crypto_Coin.db'

con = sqlite3.connect(db_path, isolation_level = None)
price_now.to_sql('BTC', con, if_exists = 'append')

con.close
"""

"""
coin_lists = pyupbit.get_tickers(fiat='KRW')
print(coin_lists)

price_now = pyupbit.get_current_price(["KRW-BTC","KRW-ETH"])
print(price_now)
"""