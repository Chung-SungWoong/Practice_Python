"""
클래스 메소드 이해하기
"""

class MyClass:
    def sayHello(self):
        print('안녕하세요')

    
    def sayBye(self, name):
        print('%s! 다음에 보자!' %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('철수')

"""
클래스 내에서 정의되는 함수인 클래스 메소드는 첫 번째 인자가 반드시 self가 되어야한다.
클래스 메소드의 인자가 필요하다면 두 번째 인자부터 정의하면 된다
"""