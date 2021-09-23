"""
파이썬 모듈 임포트 이해하기 (import ~ as)
"""

import mypackage as mp
import mypackage.mylib as ml

ret1 = mp.mylib.add_txt('대한민국','1등')
ret2 = ml.reverse(1,2,3)