"""
시퀸스 자료형 이해하기
"""

strdata = 'abcde'
listdata = [1,[2,3],'안녕']
tupledata = (100,200,300)

"""
시퀸스 자료형의 공통적인 특성:
인덱싱 = 인덱스를 통해 해당 값에 접근할 수 있습니다. 인덱스는 0부터 시작
슬라이싱 = 특정 구간의 값을 취할 수 있습니다. 구간은 시작 인덱스와 끝 인덱스로 정의합니다.
연결 = "+" 연산자를 사용하여 시퀀스 자료를 여러 번 반복하여 새로운 시퀀스 자료로 사용합니다.
맴버체크 = 'in' 키워드를 사용하여 특정 값이 시퀀스 자료의 요소로 속해 있는지 확인 할 수 있습니다.
반복 = "*" 연산자를 이용하여 시퀀스 자료의 요소로 속해 있는지 확인할 수 있습니다.
크기정보 = len()를 사용하여 시퀀스 자료의 크기를 알 수 있슴니다. 시퀀스 자료의 크기는 문자열의 경우 문자의 개수, 리스트와 튜플의 경우 맴버의 개수
"""