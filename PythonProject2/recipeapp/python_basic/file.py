from hmac import digest_size

import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns

emp=pd.read_csv("c:/pydata/EMP.csv")
print (emp)
# SELECT deptno,sal
# FROM emp GROUP BY deptno
'''
result=emp.groupby("DEPTNO")['SAL'].mean().reset_index()
print(result)
result.plot.bar(x='DEPTNO',figsize=(8,5))
'''
result=emp.groupby("JOB")['SAL'].sum().reset_index()
colors=sns.color_palette()
result['SAL'].plot.pie(labels=emp['JOB'],colors=colors,autopct="%0.0f%%")
plt.show()