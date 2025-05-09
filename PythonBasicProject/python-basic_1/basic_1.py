'''
  변수 / 연산자 / 제어문 / 함수
  응용 = database 연동
        데이터 수집 bs4
        데이터 통계 / 분석 (numpy, pandas)
        시각화 (matplotlib, seaborn)
        = 데이터베이스, 공공 데이터 => CSV
        = 장고 = 스프링 (웹)
  1) 변수
      기본자료형
        정수 / 실수 / 문자열 / 논리형
        => 클래스형으로 인식
        <class 'int'>
        <class 'float'>
        <class 'str'> "",''
        <class 'bool'>

      집합자료형
        = list : [1,2,3,4,...]
          배열형 (1차원)
          중복 허용이 가능, 값을 변경해서 사용
        = tuple : (1,2,3,4,....)
          데이터베이스에서 값을 읽기
          중복 데이터 허용, 한번 정하면 변경이 불가능
        = 세트형(set) : 중복을 허용하지 않는다
                      {1,2,3,4,5,....}
        = 사전형(dict) : 키와 값 => JSON
                      {"키":"값,"키":"값,...}
                      => 키는 중복이 불가능
        = 상호 호환
          a=[1,2,3,...]
          b=set(a) => 세트형으로 변경
          c={1,2,3,4...}
          d=list(c)
          e=(1,2,3,4,..)
          f=list(e), set(e)
          i=tuple(a)
      => 사용법
        변수명 = 데이터 => 집합 데이터형
      => 데이터형 확인 type(변수명)
         데이터의 주소값 id(변수명)
      => 식별자
          알파벳으로 시작(한글 사용이 가능 = 비권장)
          대소문자 구분
          숫자 사용이 가능(맨 앞에 사용 불가)
          키워드 사용이 불가능 (if, for...)
      => 논리형 (True/False)

  2) 연산자
    1. 산술 연산자
      +, -, *, /, //, %, **
      -- 문자열 결합(문자만 가능)
        예) 'a'+'b' => 'ab'
            'a'+1 => 오류 발생
            'a'+str(1) => 'a1'
                ------ 문자열 변환후에 사용
            / => 정수/정수=실수
            // => 정수//정수=정수
            ** : 거듭제곱 10**2=> 10^2
        print("hello"*10) => hello 10번 반복
                             hellohellohellohellohellohellohellohellohello
    2. 비교 연산자
      ==, !=, <, >, <=, >=
      => 결과값 True/False
    3. 논리 연산자
      and, or, not
      &&   ||  ! => python에서는 사용이 불가능
      => 결과값 True/False
    4. 대입 연산자
      =(치환 연산자)
    5. 복합 대입 연산자
      +=, -=
      => ++, -- (X)
      => 형변환 연산자가 없다
         -----------------
          함수로 만들어져 있다
          문자열 => str(변수)
          정수 => int(변수)
          실수 => float(변수)
          논리 => bool(변수)
                     -----
                     문자열, 정수, 실수
                            ---------
                            0, 0.0 아닌 모든 수는 True
                            bool(1) = True
                            bool(0) = False
          집합데이터 : list(set, tuple)
                     set(list, tuple)
                     tuple(list, set)
                     ----------------
                     Collection
                          |
                  --------------------
                  |       |          |
                List     Set        Map
                ----     ----       ---
                        세트형       사전형
                list(일차배열)
  3) 제어문
    1. 조건문
      = 단일 조건문
        if 조건문:
          문장 -> 조건이 True일때 처리
      = 선택 조건문
        if 조건문:
          처리문장 -> 조건이 True일때 처리
        else:
          처리문장 -> 조건이 False일때 처리
      = 다중 조건문 => 조건에 맞는 조건문 1개만 수행
        if 조건문1:
          처리문장 -> 조건1이 True일때 처리
        elif 조건문2:
          처리문장 -> 조건2가 True일때 처리
        elif 조건문3:
          처리문장 -> 조건3이 True일때 처리
        else:
          처리문장 -> 해당 조건이 없을때 처리, 생략이 가능
      *** 들여쓰기 => yaml, yml
      *** switch-case는 없다
    2. 반복문
      while : 반복횟수가 없는 경우
              무한루프 while(True)
        형식)
          초기값
          while (조건) :
            반복 처리 문장
            증감식 => 복합대입연산자 사용
            i++ (X) i=i+1 i+=1
      for : 반복횟수가 있는 경우
        for 받는 변수 in range():
          반복 수행문장

        => range(1,10) => 1~9 : 마지막 제외
                          for(int i=1;i<10;i++)
        => range(5) => 5바퀴
        => range(1,10,2) => for(int i=1;i<10;i+=2)
                      -- 2씩 증가
        ------------------ 일반 for
        for-each
        for 받는 변수 in (list,set,tuple)
    3. 반복제어문
      break : 반복의 종료
      continue : 특정부분을 제외

#print("hello"*10)
i=1
while i<=10:
  #print("i="+str(i))
  #print(f"i={i}")
  print("i=%d" %i)
  i+=1
'''
for i in range(1,10): # 1~9
  print(f"i={i}")
print("----------")
for i in range(1,10,2): # 1~9
  print(f"i={i}")
print("----------")
for i in range(5): # 0~4
  print(f"i={i}")
print("----------")
a=["홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이","강감찬","이순신","박문수"]
for name in a:
  print(name,end=",")
print(type(a))
b=("홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이","강감찬","이순신","박문수")
for name in b:
  print(name,end=",")
c={"홍길동","심청이","강감찬","이순신","박문수","홍길동","심청이","강감찬","이순신","박문수"}
#순서가 없다, 중복 제거
print(type(b))
for name in c:
  print(name,end=",")
print(type(c))
d={"name":"홍길동","age":25,"sex":"남자"}
print(d["name"])
print(d["age"])
print(d['sex'])
#데이터베이스 => 브라우저 전송

