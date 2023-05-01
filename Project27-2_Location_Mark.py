import pandas as pd
import folium

filePath = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/uni_map.xlsx'
df_from_excel = pd.read_excel(filePath,engine='openyxl', header= None)
df_from_excel.columns = ['학교이름','주소','x','y']

name_list = df_from_excel['학교이름'].to_list()
addr_list = df_from_excel['주소'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

map = folium.Map(location=[37,127],zoom_start=7)

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i],position_x_list[i]],popup=name_list[i],icon = folium.Icon(color='blue'))
        marker.add_to(map)

map.save(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/uni_map.html')

marker = folium.Marker([37.341435483,26.733026596],popup='한국공학대학교',icon=folium.Icon(color='blue'))

marker.add_to(map)
map.save(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/uni_map.html')
