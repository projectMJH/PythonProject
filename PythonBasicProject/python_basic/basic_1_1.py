'''
    자료형(데이터형) = 기본문법
    파이썬 : 자료형
    1. 정수형: <class 'int'>
    2. 실수형: <class 'float'>
    3. 문자열: <class 'str'>
    4. 논리형: <class 'bool'>

    a=10
    a='aaa'

    5. 집합 자료형
    리스트형: 중복 데이터 허용 = [] (배열형)
    튜플형: 데이터베이스, 중복 허용,
           한번 값이 지정되면 변경이 불가능 ()
           ('name','홍길동')
    셀형: 중복데이터 허용(X) => Set => {}
    딕트형(사전형) => Map => 키, 값 => ["키","값"]
                    웹 => JSON전송
    변수: 변경이 가능한 값
         프로그램 종료시 자동으로 사라진다 (RAM)
    1. 변수 식별자
       = 알파벳, 한글로 시작한다
         ----- 대소문자 구분한다
       = 숫자사용이 가능 (단, 뒤에만 사용한다)
       = 키워드는 사용 금지
         if, else, for, while, else if
                               elif
       = 특수문자(_)
       = 공백이 없다
    2. 연산자
       정수/정수 = 실수
       ** // 제곱근
       bool => True/False (true/false -> 오류)

'''
# 변수 => 출력
a = 10
print(a)
print(type(a)) # 데이터형 type(변수명)
print(id(a)) #주소값을 확인 id(변수명)
b = 10.5
print(b)
print(type(b))
c = True
print(c)
print(type(c))
d = 'Python'
print(d)
print(type(d))

print(float(a))
print(bool(a))
# bool => 0, 0.0 (False), 나머지는 True
'''
    str(변수,값) = 문자열 변환
    bool(변수, 값) = 논리형 변환
    float(변수,값) = 실수형
'''
# 출력 형식
a = 10
print(a)
print("a는 %d이다" %a)
b,c,d = 10,20,30
#print("b:{},c:{},d:{}".format(*args:b,c,d))
print("b:{},c:{},d:{}".format(*[b,c,d]))
print("b=%d,c=%d,d=%d" %(b,c,d))
# %d(정수) %f(실수) %s(문자열)
print(f"b={b},c={c},d={d}")
# sql=f"select * from emp where empno={empno}"
# 같은 값을 가지고 있는 경우 => 주소값이 동일
a1 = 3
b1 = 3
print(id(a1),id(b1))

m = 10
n = 20
# end = "\n"
print(f"m={m}",end="\t") # print
print(f"n={n}") #println
print("m:%d" %m , "n:%d" %n, sep="-")
# 구분자 sep
# 출력물 / end / sep