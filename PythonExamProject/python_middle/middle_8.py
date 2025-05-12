import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
  CSV 파일 읽기 / CSV 파일 추출
  JSON 파싱 / XML 파싱방법
  파이썬 = 변수 (데이터형 확인 => type)
          list / dict
          연산자 / 제어문 / 함수 / 예외처리
          웹 = spring / spring-boot
                        jpa / my-sql 
"""

emp_df=pd.read_csv("c:\pydata\EMP.csv")
print(emp_df)
#create table empcp as select * from emp where deptno=30
#empcp=emp_df[emp_df['DEPTNO']==30]
#print(empcp)
# emp_df => select ename from emp
print(emp_df['ENAME'])
# empno, ename, job, sal => deptno=20
data=emp_df[emp_df['DEPTNO']==20][['EMPNO','ENAME','JOB','SAL']].copy()
print(data)
# select empno,ename,job from emp where job='MANAGER';
data=emp_df[emp_df['JOB']=='MANAGER'][['EMPNO','ENAME','JOB']].copy()
print(data)
print(emp_df[['EMPNO','ENAME','JOB']][emp_df['JOB']=='MANAGER'])

names=emp_df['ENAME']
print(names)
values=emp_df['SAL']
print(values)
df=pd.DataFrame({"names":names,"sals":values})
print(df)
plt.plot(names,values)
plt.xticks(rotation=45)
plt.show()