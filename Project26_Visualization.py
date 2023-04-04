import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

file_path = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/excel.xls'
df_from_excel = pd.read_excel(file_path,engine='openpyxl')              # xlsx가 아닌 csv 파일로 바꿀 수 있으면 zipfile.BadZipFile: File is not a zip file 에러가 나지 않음
                                                                        # 파일 내용이 깨졌음
df_from_excel = df_from_excel.drop(index=[0,1])

df_from_excel.columns = ['년도','회차','추첨일','1등당첨자수','1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수','3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수','5등당첨금액','당첨번호1','당첨번호2','당첨번호3','당첨번호4','당첨번호5','당첨번호6','보너스번호']

df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ 가-힣,]+',repl=r'',regex=True)
df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ 가-힣,]+',repl=r'',regex=True)
df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ 가-힣,]+',repl=r'',regex=True)
df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ 가-힣,]+',repl=r'',regex=True)
df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ 가-힣,]+',repl=r'',regex=True)

print(df_from_excel.head([['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']]))

font_path = 'C:/Windows/Fonts/NGULIM.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font)

x = df_from_excel['회차'].iloc[:100].values
price = df_from_excel['1등담첨금액'].iloc[:100].values / 100000000

plt.figure(figsize=(10,6))
plt.xlabel('회차')
plt.ylabel('당첨금액(단위:억원)')

plt.bar(x,price,width=0.4)

plt.show()
"""
print(df_from_excel['회차'].values)
print(df_from_excel['1등담첨금액'].values)
"""