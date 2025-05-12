#문자열
'''
name = "홍길동"
print(name)
data = """
유럽축구 이적시장 전문가 파브리치오 로마노가 김민재의 연봉을 지적했다.
현재 김민재가 바이에른 뮌헨에서 높은 연봉을 받고 있기 때문에
김민재가 올여름 바이에른 뮌헨을 떠나 유럽 내 다른 구단으로 이적하려면 연봉 삭감을 해야 한다
"""
print(data)
'''
import random

'''
b = True
c = False
print(b)
print(c)

# 입력
print('이름 입력:')
name = input()
print(name,'님 반갑습니다')

num = input("정수 입력:")
print(f"num={num}")
'''
'''
    파이썬 연산자
    1) 산술연산자
        +, -, * , /, %
        +
            문자열 + 문자열
            문자열 + 정수 (X)
            문자열 + 실수 (X)
        / => 실수, // => 정수
            정수 / 정수 = 실수
            0으로 나눈 경우: ZeroDivisionError (에러)
        %
            나머지 값의 부호는 나누는 값에 따른다
        ** 
            10**2 => 100 => 10^2
                   
    2) 비교연산자
        ==, !=, <, >, <=, >= => True/False
    3) 논리연산자
        and, or, not
        && (X), || (X) ! (X)
    4) 대입연산자
        =
    5) 복합대입연산자
        +=, -=, /=, %=, **=, //=
    
    형변환 연산자 (X) => (int) 10.5  int(10.5)
    증감 연산자 (X), 삼항연산자 (X)
    +=, -=  if ~ else

a = "Hello"
b = 10
print(a+str(b)) # 정수는 문자열 변환 후에 사용
# str() = String.valueOf()

a = 10
b = 2
print(a**b)
print(not(a)) # ! => not()
print(not(bool(a)))

c = 10>9 and 10==9
print(c)

# 정수 / 정수 = 실수
print(5/2)
# 정수 // 정수 = 정수
print(5//2)
'''

# 변수 = 반드시 초기화
a = random.randrange(1,101) # Random.next(101)
while(True):
    user = int(input("정수 입력(1~100):"))
    if user<a:
        print("입력값 보다 큰값을 입력하세요")
    elif user>a:
        print("입력값 보다 작은 값을 입력하세요")
    else:
        print("정답입니다")
        break
print("Game Over!!")