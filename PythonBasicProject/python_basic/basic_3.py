'''
    변수 설정:
        변수 = 값 (데이터형을 사용하지 않는다)
              반드시 초기화값을 부여
        연산자
            = 형변환 연산
                정수 : int(문자열)
                실수 : float()
                문자열 : str()
                논리형 : bool()
            = 정수//정수 = 정수
            = 제곱근
                **
            = 논리연산자
                && => and, || => or, ! => not()
            = 증감연산자(++,--), 삼항연산자(X)

# 치환 연산자 (대입연산자)
a = 10 # int a=10
# 복수의 주소에 저장
b = c = d = 10 # int a,b,c; a=b=c=10
e,f = 100, 200 # int e=100, f=200

# 산술연산자
a = 10
b = 3
print(a+b) # 13
print(a-b) # 7
print(a*b) # 30
print(a/b) # 3.3333333333333335
print(a//b) # 3
print(a%b) # 1
print(a**b) # 1000

name1 = '홍'
name2 = '길동'
print(type(name1))
print(type(name2))

print('홍'+'길'+'동') # 홍길동
print('홍길동'*3) # 3번 출력(반복) # 홍길동홍길동홍길동
a=3
print('홍길동'*a) # a번 출력(반복) # 홍길동홍길동홍길동
print('홍길동'+str(10)) # 홍길동10
print(int("10")+10) # 20
print(10.5+10) # 20.5
print(10.5+float(10)) # 20.5
print(bool(0),bool(-1),bool(0.0),bool(0.1)) # False True False True
# 0, 0.0 제외
print(bool(0)+bool(-1),bool(0.0),bool(0.1)) # 1 False True

print(bool('홍'),bool('')) # True False

# 문자열은 공백을 제외한 모든 문자는 True
# int(), fload(), bool(), str()
# 비교연산자
a = 10
b = 9
print(id(a),id(b)) # 140703644329160 140703644329128
print(a==b) # False
print(a is b) # 주소값 비교(참조하는 주소)
print(a!=b) # True
print(a>b) # True
print(a<b) # False
print(a>=b) # True
print(a<b) # False
'''
'''
      and / or
    -----------------------------------
               and(직렬)    or(병렬)                 
    -----------------------------------
      T  T         T           T             
    -----------------------------------
      T  F         F          T                     
    -----------------------------------
      F  T        F           T                     
    -----------------------------------
      F  F        F           F                     
    -----------------------------------
    
    (조건) and (조건)
    -----     -----
      |         |
      -----------
          |
         결과값
    
    부정연산자 : not() ==> True/False      
                0, 0.0, '', "" 제외한 나머지는 False                       

a = 10
b = 20
c = 0
print(not(a<b)) # False
print(not(a)) # False
print(not(b)) # False
print(not(c)) # True
'''
x = 10
y = 9
print(x<y and x==y+1) # False
print(x>y and x==y+1) # True
print(x>y or x==y+1) # True
print(x>y or x==y+1) # True

x += 20 # x=x+20  x++ x+=1
y -= 10 # y=y-10  x-- x-=1
print(x,y) # 30 -1