"""
클래스 맴버와 인스턴스 맴버 이해하기
"""

class MyClass:
    var = '안녕하세요!!'                   # 메소드 바깥에서 선언되었으므로 클래스 맴버
    def sayHello(self):
        param1 = 'hello'                # 메소드 내에서만 유요한 지역변수 param1 정의
        self.param2 = 'Hi'              # param2 역시 인스턴스 맴버. 이 변수가 초기화되는 시점은 sayHello()가 호출되는 시점이므로 self.param2를 사용하려면 sayHello()가 호출된 이후여야한다
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
#obj.param1                             param1은 MyClass의 클래스 메소드인 sayHello()의 지역변수이므로 MyClass의 인스턴스 객체인 obj의 맴버로 참조가 불가능

"""
self.var 클래스 메소드 내에서 var을 참조할 경우
MyClass  클래스 밖에서 클래스 이름만으로 참조할 경우 (별로 안쓰인다)
obj.var  MyClass의 인스턴스 객체 obj에서 var을 참조할 경우
"""