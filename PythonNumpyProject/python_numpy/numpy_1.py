import numpy as np

a=np.array([[-1,2,3],[3,4,8]])
s=np.sum(a)
print(s)
p=np.prod(a)
print(p)
# 평균  mean() / 표준 편차 std
# => 19/6
m=np.mean(a)
print(m)
ss=np.std(a)
print(ss)
"""
  10 8 10 8 8 4
  sum : 48
  mean : 48/6 = 8
  분산
    10  8 10  8  8  4
    -8 -8 -8 -8 -8 -8
    -----------------
     2  0  2  0  0  4
    2^2    2^2      4^2
    -----------------
     4     4       16 ===> 24
    24 / n-1 => 24/5 => 4.8
    
    4.8 루트 => 2....
    
  표준편차
    4.8 루트 => 2... => std  
     
  표준편차
"""