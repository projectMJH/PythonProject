import numpy as np
import pandas as pd
import oracledb as db
import matplotlib.pyplot as plt

conn=db.connect("hr/happy@localhost:1521/XE")
cur=conn.cursor()
sql="""
      SELECT * 
      FROM emp
    """
cur.execute(sql)
emp=cur.fetchall()
cur.close()
conn.close()
print(emp)
column=['empno','ename','job','mgr','hiredate','sal','comm','deptno']
emp_df=pd.DataFrame(emp,columns=column)
print(emp_df)
print(emp_df['ename'])
print(emp_df['sal'])
print(emp_df['ename'][emp_df['ename'].apply(lambda x:x[-1]=='T')])

names=emp_df['ename']
values=emp_df['sal']

plt.plot(names, values, marker='o')  # 선 그래프
#plt.xticks(names, names)  # x축에 문자열 라벨 붙이기

plt.title('Line Plot Example')
plt.xlabel('Names')
plt.ylabel('Values')
plt.grid(True)
plt.show()