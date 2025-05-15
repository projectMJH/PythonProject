"""
  파이썬 => 라이브러리 설정
  터미널 : pip install pandas numpy matplotlib seaborn konlp konlpy django lxml
          => bs4 oracledb
  장고 : 프로젝트 생성
        1. admin 생성
          1. django-admin startproject config .  => config 파일(환경설정) 위치 지정
          2. python manage.py migrate : admin 생성, db에(sqllite) 저장
          3. python manage.py createsuperuser : 관리자 계정 생성
              = username
              = email
              = password
          4. client 프로그램  만들기
              python manage.py startapp 폴더명 (web)
          5. 서버 구동
              python manage.py runserver
              => port: 8000

          폴더 / 파일명
          config => 서버 구동을 위한 환경 설정
                 => settings.py
                    app 설정
                    cross origin 설정 (port가 다를 때)
                    static 폴더
                    ----------
                      image / js / css 파일 저장
                 => urls.py
                    -------
                    @RequestMapping
                    사이트 경로 = 호출 함수 지정
          ----------------------------------------------
            Spring : XML (server.xml, web.xml)
                     => maven
            Spring-Boot : XML을 제외
                  => application.properties
                  => application.yml
                  => tomcat => 내장
                  => 나머지는 SpringFramework와 동일
                             ---------------
                             | 그대로 적용
                             | gradle 을 주로 사용
                               => CI/CD 적용이 편리하다
                  => Spring-Cloud / AI
                     ------------ MSA
                  => NoSQL 지원: ElasticSearch
          web
            models.py : DAO = 데이터베이스 연동
              foodModels.py, recipeModels.py
            views.py : Model = 브라우저와 연결
              foodViews.py, recipeViews.py
            ----------------------------------
              폴더별로 구분

  파이썬 기본 문법
    1. 데이터형을 사용하지 않는다 => 가독성이 떨어짐
        a=10
        a='aaa'
        a=pd.DataFrame()
        a=[]
        => 변수 type => <class 'int'>
                        <class 'float'>
                        <class 'str'>
                        <class 'bool'>
        => 집합데이터
          1) list: [] => 1차원 배열
          2) tuple: () => 데이터베이스 값
          3) set: {} => 중복을 허용하지 않는다
          4) dict: {"키":"값"} => JSON 과 동일
          5) DataFrame : table 형식
            => database: table, csv
        => print() : 출력
        => 들여쓰기 : yml, python
        => 식별자는 자바와 동일
        => 연산자 : 단항연산자가 없다
                   ---------- 복합대입 연산자 대치\
            | => 데이터분석
            1) 산술
              + => 숫자+숫자, 숫자+문자 (X)
                             ----------
                             => str(숫자)+문자 (O)
              / => 실수
              // => 정수
              ** => 거듭제공
            2) 형변환 연산자
              int(), float(), str(), bool()
              bool() => bool(숫자) : 0,0.0 이외는 True
                        bool(문자) : null,"" 이외는 True
              list => list(set()), list(tuple()) : for-loop 수행
              set => set(list()), set(tuple()) : 중복제거
              tuple => tuple(list()), tuple(set()): 변경 불가
            3) 복합 대입 연산자
               문자열 결합 => += => a=a+문자
               ---------------------------
               f"{변수} aaaaaa"
            4) 데이터분석 : 문자열
               문자열 => 인덱싱
               H e l l o
               0 1 2 3 4 => 앞에서 부터
                    -2-1 => 뒤에서 부터  
               [:] [0:5]
               find(찾는 문자열) => indexOf()
               replace()
               split()     
            5) 제어문
               조건문
                  if 조건문:
                    처리문장
                  -----------
                  if 조건문:
                    처리문장
                  else:
                    처리문장
                  -----------
                  if 조건문:
                    처리문장
                  elif 조건문:
                    처리문장
                    ...
                  else:
                    처리문장
               반복문
                  초기값
                  while 조건:
                    반복문장
                    증감식 => i++(X) => i+=1
                  -------------------------
                  for 변수 in range(1,10):
                    처리문장
                  for 변수 in 문자열|리스트|튜플:
                    처리문장     => for-each
               반복제어문
                  break : 반복문 중단
                  continue : 특정 부분을 제외 후 계속 수행

               ** do~while/switch (X)
               => if/for
            6) 함수
               = 명령문을 모아서 처리 (재사용)
                ------
                변수, 제어문, 연산자
               = 반드시 한개의 기능 수행
               = 종류
                 사용자 정의 함수, 라이브러리
                 *** 라이브러리 활용
                     --------- pip install ...
                 def 함수명(매개변수):
                    함수 정의 => 정의가 없는 경우 pass
            7) BS4
               => Jsoup
               => find()
               => findall()
               => select(태그명, class_="")
            8) 예외처리
               => 에러를 사전에 방지
               => 비정상 종료를 방지 => 정상 상태 유지
               try:
                  정상수행문장
               except 예외처리 클래스 선언:
                  에러처리 => 에러 복구
               finally:
                  서버/파일/데이터베이스
            9) 파일 입출력
               f=open("파일명",'r')
                 r / w => 파일 초기화 / a => 파일에 첨부
               f.close()

               f=pd.read_csv()
               f=sns.read_html() => seaborn에서 사용, <table> 로 구성된 문서만 가능

  Numpy : 연산을 위한 라이브러리
          행렬/배열 연산
          난수 생성
          import numpy as np
          ----------------------------------
          a=[[1,2,3],[4,5,6]]
          => b=np.array(a) => 행렬
          => b.ndim => 배열의 열수(차원)
          => b.shape => 행/열 => (2,3)
          => 특수배열
             np.arrange(10) => 1차원 배열
             np.arrange(5,10) => 5,6,7,8,9
             np.zeros(2,2) => [[0,0],[0,0]]
                           => b[0,0]
          => 연산자
             add()        +
             substract()  -
             multiply()   *
             divide()     /
          => mean() : 평균
             sum()
             prod() : 모든 데이터 곱
             std() : 표준 편차

  Pandas : 통계
          => DataFrame 처리
             --------- 2차원 배열
             column / row
          emp_df=pd.DataFrame()
          emp_df['column']
          => groupby
             => mean() / max() / min() / sum() / count()
          => 여러개를 동시에 처리
             => merge (join)
          => emp_df.sort_value(by="", ascending=False)
          => emp_df.reset_index() => 0번부터 초기화
             emp_df.set_index("존재하는 컬럼")
  시각화(MatplotLib, Seaborn) : bar / line / pie / scatter
                               wordcloud
"""
"""
  개발자 취업시장 현황
    = SI / SM => 2800~3200
    ---------------
    = 빅데이터 분석 => 3400~3800
    = AI
    ---------------

"""