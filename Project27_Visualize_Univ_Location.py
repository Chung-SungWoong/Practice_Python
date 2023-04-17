"""

"""

import pandas as pd

filePath = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/고등교육기관 주소록(2022).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].tolist()

df_from_excel = df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)
print(df_from_excel['주소'].values)