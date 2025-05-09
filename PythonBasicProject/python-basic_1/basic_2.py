'''
  함수
    = 명령문의 집합 (재사용)
    = 변수, 연산자, 제어문
    = 함수는 한개의 기능만 수행
    = 함수의 종류
      = 사용자 정의
          자바스크립트: function 함수명(매개변수)
          코틀린     : fun 함수명(매개변수)
          파이썬     : def 함수명(매개변수):
        def 함수명(매개변수):
          처리 ...
      = 라이브러리 (print, int, str...)

      = 함수
        1) 리턴형 => 여러개를 전송할 수 있다
            예) return a,b,c,d...
        2) 매개변수
            *** 디폴트 매개변수
            a(a=10,b=20,c=30) => a=10,b=20,c=30
            a(100,200,300)    => a=100,b=200,c=300
            a(100)            => a=100,b=20,c=30
            a(100,200)        => a=100,b=200,c=30
            print("",end="",sep="")
                            ------ default: '' =>  '-', ','
                     ------ default: '\n' => '\t', ','
            *** 가변형 매개변수
                Object... obj
                *args
        3) 함수명 = 식별자와 동일

      형식)
        1) 리턴형 (O), 매개변수 (O)
          def 함수명(매개변수...):
            처리문장
            return 값...
        2) 리턴형 (O), 매개변수 (X)
          def 함수명():
            처리문장
            return 값...
        3) 리턴형 (X), 매개변수 (O)
          def 함수명(매개변수...):
            처리문장
        4) 리턴형 (X), 매개변수 (X)
          def 함수명():
            처리문장
        -----------------------------
        매개변수 = default => 매개변수는 뒤에서부터 설정
        형식)
          def 함수명(a=100,b,c)
          함수명(200,300) => 오류 발생 => a=200,b=300,c (X)

          def 함수명(a,b=100,c=200)
          함수명(200)      => a=200,b=100,c=200
          함수명(100,200)  => a=100,b=200,c=200
        print(value,end="\n",sep="")
        print("hello")
        print("hello",end="\t")
        print("a,b,c",sep=",")

        매개변수: 가변
          def 함수명(*args) => C언어 (포인터), 자바(...)
          System.out.printf("%d",10)
          printf(String fmt,Object... obj)
          System.out.printf("%d%d%d",10,20,30)
          함수명(1)
          함수명(2,3,4,5,5,6...)
          => 사용자가 보내는 데이터가 확인이 안되는 경우
          => 데이터베이스 / 웹
          => ---------------
              분석 => 라이브러리
          => 반드시 재사용이 가능하게

#1. 유형 => 리턴형 (X), 매개변수 (O)
dan=int(input("2~9 사이의 정수 입력: "))
def gugudan(dan):
  for i in range(1,10):
    print(f"{dan}*{i}={dan*i}")
gugudan(dan)

def gugudan():
  dan = int(input("2~9 사이의 정수 입력: "))
  for i in range(1,10):
    print(f"{dan}*{i}={dan*i}")
gugudan()
'''
def emp_list():
  emp=["홍길동","심청이","박문수","춘향이","박문수"]
  return emp,len(emp)       #emp.__len__()
emp,total=emp_list()
for name in emp:
  print(name)
print(f"인원: {total} 명")
def defaultFunc(a=10,b=20,c=30):
  print(f"a={a}")
  print(f"b={b}")
  print(f"c={c}")
defaultFunc(100)                  # a=100,b=20,c=30
defaultFunc(100,200)        # a=100,b=200,c=30
defaultFunc(100,200,300) # a=100,b=200,c=300

def changeFunc(*args):
  for i in args:
    print(f"i={i}")
changeFunc(1)
changeFunc(1,2)
changeFunc(1,2,3)
changeFunc(1,2,3,4)
changeFunc("aaa","bbb","ccc")
