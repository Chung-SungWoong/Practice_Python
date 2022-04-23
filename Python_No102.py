"""
리스트에서 특정 위치의 요소를 변경하기
"""

solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)