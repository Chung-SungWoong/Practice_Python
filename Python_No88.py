"""
문자열에서 좌우 공백 제거하기 (lstrip, rstrip, strip)
"""

txt = '   양쪽에 공백이 있는 문자열입니다   '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<' + txt + '>')
print('<' + ret1 + '>')
print('<' + ret2 + '>')
print('<' + ret3 + '>')
