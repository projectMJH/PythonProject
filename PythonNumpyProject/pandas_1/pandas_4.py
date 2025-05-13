# 시각화 / 정규식 / => 데이터 읽어서 시각화
"""
  데이터 수집: 공공데이터, 크롤링, 데이터베이스
      |
   데이터 분석: numpy, pandas
      |
     시각화 : matplotlib, seaborn
    ----------------------------- 데이터 전처리
    머신러닝 / 딥러닝 = 라이브러리 (알고리즘)
    아파치 로그 파일 분석
    -------------------

    연산자 사용법
  between ~ and
    = 데이터프레임['컬럼'].between(값1,값2)
  in
    = 데이터프레임['컬럼'].isin(값1,값2...)
  is null
    = 데이터프레임['컬럼'].isnull()
  like
    = 데이터프레임['컬럼'].apply(lambda x:x[0])

  lambda x:express
           ======= 처리
         == 매개변수
  def 함수(매개변수):
    처리 => return

  자바에서
  new Runnable(()->{
    쓰레드 처리
  })

  자바스크립트
  function aaa(){
  }

  let aaa=()=>{
  }

  1. 람다의 단점 : 재사용이 어렵다, 가독성이 떨어진다
    1.8 => 람다
    => 코드는 줄어준다
    Spring-Boot
    => re : 정규식(형태), 형태소분석
          => 국어 => 데이터사전
          => 데이터사전 / 위탁 내용 추출
            => 프레임워크
          SI/SM 솔루션 아키텍처 프레임워크
                      ------  --------
                        설계    위탁
                -----SM
          -----
    짜고 짜면 .... 짜+
"""

import numpy as np
import pandas as pd
"""
"""
arr=np.array([
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5]
])
print(arr.shape)
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=(0,1)))

emp=pd.read_csv("c:/pydata/EMP.csv")

print(emp)
"""
s=pd.read_csv("c:/pydata/subway.csv")
print(s['지하철역'])
print(s.describe())
"""
s=pd.read_csv("c:/pydata/EMP.csv")
"""
  SELECT empno,ename,sal
  FROM emp
  WHERE sal BETWEEN 1000 AND 3000
"""
print(emp[['EMPNO','ENAME','SAL']][emp['SAL'].between(1000,3000)])

"""
  SELECT empno,ename,sal
  FROM emp
  WHERE job in ('CLERK','MANAGER')

print(emp[['EMPNO','ENAME','JOB']][emp['JOB'].isin(['CLERK','MANAGER'])])
"""
"""
  SELECT empno,ename,sal,comm
  FROM emp
  WHERE comm isnull()

print(emp[['EMPNO','ENAME','SAL','COMM']][emp['COMM'].isnull()])

print(emp['ENAME'])
emp['ename_two']=emp['ENAME'].apply(lambda x:x[1])
print(emp[['ENAME','ename_two']])
"""

# ename LIKE '_M%'
print(emp[['ENAME']][emp['ENAME'].apply(lambda x:x[1]=='M')])
# ename LIKE 'K%'
print(emp[['ENAME']][emp['ENAME'].apply(lambda x:x[0]=='K')])
# ename LIKE '%T'
print(emp[['ENAME']][emp['ENAME'].apply(lambda x:x[-1]=='T')])