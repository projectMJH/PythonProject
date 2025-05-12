"""
  파이썬의 단점
  = 연산처리가 늦다
  = C언어를 도입 => numpy
  = sum / mean / std
  = 인덱싱 / 슬라이딩

  pandas
  = Spring-Boot : JPA, ThemeLeaf = AWS
    ---------------------------- CI/CD
  = 데이터 수집 : 데이터프레임 : 테이블 형식
    --------- CSV / 데이터베이스 / XML
               |                  |
               --------------------
"""
import numpy as np
import pandas as pd
# 파일(CSV) 읽기 => 자체 지원 붓꽃, 타이타닉
emp_df=pd.read_csv('c:/pydata/EMP.csv')
print(emp_df)
dept_df=pd.read_csv('c:/pydata/DEPT.csv')
print(dept_df)
# 값 읽기
# SELECT ename FROM emp
print(emp_df['ENAME'])
"""
  CREATE TABLE empcp
  WHERE deptno=30
"""
empcp=emp_df[emp_df['DEPTNO']==30]
print(empcp)
"""
  SELECT empno,ename,job,sal
  FROM emp WHERE deptno=20
"""
empcp=emp_df[emp_df['DEPTNO']==30][['EMPNO','ENAME','JOB','SAL']].copy()
print(empcp)
"""
  SELECT ename,job,hiredate,mgr
  FROM emp
  WHERE deptno=10

empcp=emp_df[emp_df['DEPTNO']==10][['ENAME',['JOB'],['HIREDATE'],['MGR']].copy()]

# SELECT empno,ename,sal FROM emp
print(emp_df[['EMPNO','ENAME','SAL']])
# SELECT empno,hiredate FROM emp
print(emp_df[['ENAME','HIREDATE']])
# SELECT ename,sal FROM emp WHERE deptno=10
"""
print(emp_df[['ENAME','SAL']][emp_df['DEPTNO']==10])
"""
  SELECT ename,sal,deptno,job
  FROM emp
  WHERE deptno=30 AND job='SALESMAN'
  GROUP BY => SUM, MEAN, MAX, COUNT, MIN, STD
"""
"""
  AND = &
  OR = |
"""
print(emp_df[(emp_df['DEPTNO']==30) & (emp_df['JOB']=='SALESMAN')][['ENAME','SAL','DEPTNO','JOB']])
print(emp_df[(emp_df['DEPTNO']==30) & (emp_df['JOB']=='SALESMAN')])
