'''
money=1000
age=25
if money>=500:
  item="사과"
  if age<=30:
    msg="new"
  else:
    msg="old"
print(item,msg)
'''
'''
  반복문
  while / for
  while : 무한 루프 = 지정된 횟수가 없는 경우
  for : 횟수가 지정된 경우
  
  while 형식
  초기화
  while 조건문:
    반복수행문장
    증가식

i=1
while i<=10:
  print("i=%d" %i)
  i+=1 # i=i+1
print("===============") # \n
i=1
while i<=10:
  if i%2==0:
    print("i=%d" %i)
  i+=1
print("==========")

i=1
while i<=10:
  if i%2!=0:
    print("i=%d 홀수" %i)
  i+=1
print("=================")

sum=0
i=1
while i<=100:
  sum+=i
  i+=1
print(f"1~100까지 누적합:{sum}")

sum=evensum=oddsum=0

i=1
while i<=100:
  if i%2==0:
    evensum+=i
  else:
    oddsum+=i
  sum+=i
  i+=1
print(f"1~100까지 누적합: {sum}")
print(f"1~100까지 홀수합: {oddsum}")
print(f"1~100까지 짝수합: {evensum}")
print("======================")

#단을 입력을 받아서 구구단 출력
i=1
dan=int(input("(2~9)단 입력:"))
while i<=9:
  print(f"{dan} * {i} = {dan*i}")
  i+=1
'''

