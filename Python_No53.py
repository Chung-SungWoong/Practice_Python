"""
클래스 소멸자 이해하기
"""
class MyClass:
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다.')

obj = MyClass()
del obj         # MyClass 인스턴스 객체가 메모리에서 제거됩니다' 가 출력됨

"""
클래스 인스턴스 객체가 메모리에서 제거될 때 자동적으로 호출되는 클래스 메소드가 클래스 소멸자입니다.
클래스 소멸자는 다음과 같은 이름을 가집니다.

인스턴스 객체를 메모리에서 제거하려면 del 키워드를 이용
"""