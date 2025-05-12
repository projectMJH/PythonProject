import numpy as np
import pandas as pd

# GROUP BY
# COUNT => deptno
"""
  SELECT deptno,COUNT(*) FROM emp
  GROUP BY deptno  
"""
emp_df=pd.read_csv('c:/pydata/EMP.csv')
dept_df=pd.read_csv('c:/pydata/DEPT.csv')

print(emp_df.groupby('DEPTNO')['SAL'].mean())
print(emp_df.groupby('DEPTNO')['SAL'].sum())
print(emp_df.groupby('DEPTNO')['SAL'].max())
print(emp_df.groupby('DEPTNO')['SAL'].min())
print(emp_df.groupby('DEPTNO')['SAL'].count())
print(emp_df.groupby('DEPTNO')['SAL'].median())

print(emp_df.groupby('DEPTNO')['SAL'].agg(['mean','max','sum','min']))
# JOIN
"""
  groupby
  ***count() : 갯수
  median() : 중간값
  max, min, sum, *** mean
  => merge
"""
"""
  SELECT * FROM emp e,dept d
  WHERE e.deptno=d.deptno
"""
pf_join=pd.merge(emp_df,dept_df,on='DEPTNO', how='inner')
print(pf_join)
# ORDER BY
print(emp_df.sort_values(by=['SAL'],ascending=True))

"""
  파일 읽기 read_csv => DataFrame (table 형식)
  file = open => csv.reader()
  
  => DataFrame
    = JOIN : merge
    = GROUP BY : groupby
                 -------
                 mean() / sum() / count()
"""

