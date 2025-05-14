import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sna
import csv
"""
df=pd.read_csv('c:/pydata/data_population.csv')
#print(type(df))
#print(df.columns)
# 1 'Province',   특별시/광역시/도
  2 'City',       구/군/시
  3 'Population', 인구수
  4 'Households', 가구수
  5 'PersInHou',  평균 가족수 
  6 'Male',       남성
  7 'Female',     여성
  8 'GenderRatio' 성비
"""
f=open("c:/pydata/data_population.csv")
data=csv.reader(f)
next(data)
"""
# 데이터에 저장
result=[]
for row in data:
  if row[2]!=" ":
    result.append(row[3])
print(result)
print(len(result))
"""
city=input("지역 입력(광역시/특별시/도):")
seoul_pop=[]
seoul_city=[]
for row in data:
  if row[2]!=" ":
    if row[1]==city:
      seoul_pop.append(float(row[3]))
      seoul_city.append(str(row[2]))
plt.rc('font',family="Malgun Gothic")
plt.figure(figsize=(12,10))
plt.bar(seoul_city,seoul_pop)
plt.title(f'{city} 인구 통계')
plt.xticks(rotation=90)
plt.show()