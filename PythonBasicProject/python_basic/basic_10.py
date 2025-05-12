'''
  함수 : 한개의 기능을 모아서 재사용이 가능
        = 명령문을 모아서 처리
        = 변수, 연산자, 제어문
        = 기능을 한개만 수행이 가능
        = 종류
          1) 라이브러리 : 제공 = 필요시마다 재사용
              print, range, ... append
          2) 사용자 정의
          = 리턴형: 여러개 전송이 가능
            return "a","b"
          = 매개변수: 여러개 / 없는 경우
          = 함수명: 변수의 식별자와 동일
          = 형식
            def 함수명(매개변수..):
              처리
              return ...
            => function 함수명(매개변수..)
            => fun 함수명(매개변수..){} => 코틀린 (var(변수), val(상수))
                                        dart
        1. 함수 형식
        -----------------------------------------
                      리턴형         매개변수
        -----------------------------------------
                        O              O
                        def 함수명(매개변수):
                          처리문장
                          return 값
        -----------------------------------------
                        O              X
                        def 함수명():
                          처리문장
                          return 값
        ----------------------------------------- void
                        X              O
                        def 함수명(매개변수):
                          처리문장
        -----------------------------------------
                        X              X
                        def 함수명():
                          처리문장
        -----------------------------------------
        System.out.printf("%d",1)
        System.out.printf("%d%d%d%d%d",1,2,3,4,5)
        매개변수 => 가변 매개변수
                  def func(*arge) => ...
                    func(1) func(2) func(1,2,3)
                  default 매개변수
                  => 매개변수는 앞에서부터 처리
                      def 함수명(매개변수,매개변수=값,매개변수=값)
                      def func(a=10,b=20,c=30)
                      func() => a=10,b=20,c=30
                      func(100) => a=100,b=20,c=30

        1. 변수 설정
        2. 연산자 => 자바와 다른점
        3. 제어문 => if / for
        4. 함수 (*******)

        데이터베이스 연동
        데이터 분석
'''
#print("Hello",end=" ")
#print("Hello",end=" ")
# 1. 리턴형(X), 매개변수(X)
'''
  30,40,10,50,20
  --
  10
     -- -- -- --
     40 30 50 20
     --
     20
        -- -- --
        40 50 30
        --
        30
           -- --
           50 40
           --
           40
              --
              50 
def sort():
  #지역변수
  data=[30,40,10,50,20]
  #리스트형 = 중복 저장이 가능, 수정이 가능
  #튜플형 (30,20,...) = 수정이 불가능 => 데이터베이스 SELECT
  #튜플 => 리스트형으로 변환
  #셀형 => {}, 딕트형 [키, 값] => JSON Map
  print(f"정렬 전:{data}")
  # for(int i=0;i<arr.length-1;i++)
  for i in range(len(data)-1):
    for j in range(i,len(data)):
      if data[i]>data[j]:
        temp=data[i]
        data[i]=data[j]
        data[j]=temp
  print(f"정렬 후:{data}")

sort()

# 2. 리턴형(O), 매개변수(X)

def getInfoata():
  return "홍길동"
name=getInfoata()
print(name)

def getInfoData2():
  return "심청이",25,"여자"
name,age,sex=getInfoData2()
print(f"이름:{name}")
print(f"나이:{age}")
print(f"성별:{sex}")
'''
