data="aaa^111\nbbb^222\nccc^333"
fm=data.split("\n")
a=[]
b=[]
for m in fm:
  k=m.split("^")
  a.append(k[0])
  b.append(k[1])
print(a)
print(b)

