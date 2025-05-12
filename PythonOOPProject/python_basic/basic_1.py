"""
  Java / Python
  ------------- Oracle / MySQL
  ------------- Vue / React
  ------------- AWS / Docker
  1. 파이썬
     = 기본 문법
       = 변수 / 데이터형 / 형변환 / 연산자 / 제어문
         = 변수
           데이터형을 사용하지 않는다
           -------
           int / float / bool / str
           list / tuple / set / dict
            |       |      |     |
                          Set   Map
           List   데이터베이스
           형변환
             => int("10") = 10
             => bool(숫자,문자) => True/False
             => str(10) => "10"
         = 연산자
           산술연산자 : +
             | 같은 데이터형만 연산이 된다
             | "aaa"+str(10)
             / => 실수 , // => 정수
             ** => 거듭제곱
             10**2  => 10^2 => 100
           => 단항연산자는 없다
           => 논리연산자 : and , or , not
         = 제어문
           while / for
           while
           -----
             초기값
             while 조건문:
                반복실행문장
                증가식 => i+=1
           *** {}이 없다 => 반드시 들여쓰기
           자바 (주과목 ) => 파이썬

           for
           for 변수 int 집합데이터(list,set,tuple)
                        range(1,10) => 마지막은 제외
           if , if~else if~elif ~ elif ~ else
           => 동작 / 흐름은 자바와 동일

     =  함수
        = 데이터형을 사용하지 않는다
        = 가독성 => 변수의 의미를 부여
        사용법
          def 함수명(매개변수...):
            기능 수행
            return 값
              매개변수 리턴값
        ---------------------
                 O     O
        ---------------------
                 O     X
        ---------------------
                 X     O
        ---------------------
                 X     X
        ---------------------
     = 예외처리
       => 오류방지 => 비정상 종료 방지
       try:
         정상 수행문장
       except Exception  as e:
         예외처리 => 복구
       finally:
          try / except와 관계없이 무조건 수행
          서버 / 데이터베이스 닫기
      = 라이브러리
        오라클 / MySql ... Numpy , Pandas / BS4

      파이썬의 객체지향 프로그램 (OOP)
      1) 클래스 구성 => 멤버변수의 상태 관리
                    state : 상태 관리
                            Vuex , Redux
         1. 멤버변수
         2. 멤버함수 : 독립적 / 클래스 종속
            ------- 변수에 대한 처리
            ------- 다른 클래스와 통신 (소프트웨어: 메세지)
         3. 생성자 : 변수 초기화 , 소멸자함수
      2) 상속 : 재사용기법
      3) 오버라이딩 : 함수 변경
      4) 추상클래스/인터페이스

      = 클래스 선언
        = 식별자
          알파벳으로 시작(대소문자 구분)
          숫자 사용이 가능 (앞에 사용 금지)
          특수문자 사용이 가능 : _
          예약어는 사용 금지 (if , for...)
     예)
         class 클래스명<(상속클래스)>:
            멤버변수
            def 함수명(self): this => self
               메소드 처리
"""
# 멤버변수 사용
class Member: # id name
    id=''
    name=''
    sex=''
    addr=''
    tel=''
#메모리 할당 => new를 사용하지 않는다
mem=Member()
mem.id="admin"
mem.name="홍길동"
mem.sex="남자"
mem.addr="서울"
mem.tel="010-1111-1111"
#출력
print(f"id:{mem.id}")
print(f"name:{mem.name}")
print(f"sex:{mem.sex}")
print(f"addr:{mem.addr}")
print(f"tel:{mem.tel}")