import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

file=open('c:\pydata\EMP.csv')
emp=csv.reader(file)
#print(emp)
data=[]
for i in emp:
  data.append(i[5])
print(data)

data2=[]
for i in data:
  if i!='SAL':
    data2.append(int(i))
print(data2)

plt.plot(data2)
plt.show()
