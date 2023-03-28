import pyupbit
import sqlite3
import pandas as pd

db_path = r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Crypto_Coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC' " , con, index_col = 'index')

print(readed_df)

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