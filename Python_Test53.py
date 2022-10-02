op=input('원하는 연산을 선택? A(덧셈), S(뺄셈), M(곱셈), D(나눗셈)') 
num1=int(input('첫번째 정수를 입력하세요?')) 
num2=int(input('두번째 정수를 입력하세요?')) 
op = op.upper()
if(op=='A'): 
    print(num1, '+', num2, '=' ,num1+num2) 
elif(op=='S'): 
    print(num1, '-', num2, '=' ,num1-num2) 
elif(op=='M'): 
    print(num1, '*', num2, '=' ,num1*num2) 
elif(op=='D'): 
    print(num1, '/', num2, '=' ,num1/num2) 
else: 
    print("연산자를 잘못 입력하셨습니다.") 