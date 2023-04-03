import pandas as pd

file_path = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/excel.xls'
df_from_excel = pd.read_excel(file_path,engine='openpyxl')              # xlsx가 아닌 csv 파일로 바꿀 수 있으면 zipfile.BadZipFile: File is not a zip file 에러가 나지 않음
                                                                        # 파일 내용이 깨졌음
df_from_excel = df_from_excel.drop(index=[0,1])

df_from_excel.columns = ['년도','회차','추첨일','1등당첨자수','1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수','3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수','5등당첨금액','당첨번호1','당첨번호2','당첨번호3','당첨번호4','당첨번호5','당첨번호6','보너스번호']

print(df_from_excel.head())

print(df_from_excel['회차'].values)
print(df_from_excel['1등담첨금액'].values)