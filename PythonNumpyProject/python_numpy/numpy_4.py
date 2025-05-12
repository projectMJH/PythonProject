import numpy as np
# 0~1 사이의 난수 발생
a=np.random.rand(5) # 난수 5개 생성
print(a)
b=np.random.rand(2,3) # 2행 3열
print(b)

c=np.random.randint(2,size=5) # 0,1
print(c)
d=np.random.randint(2,4,size=5) # 2~4 => 2,3
print(d)
e=np.random.randint(1,5,size=(2,3))
print(e)
a=np.random.randn(5) # 표준 편차
print(a)