'''
  제어문
    1) 조건문
        = 단일 조건문
          if 조건문:
            처리문장 = 조건이 True일 경우에 처리
        = 선택 조건문
          if 조건문:
            처리문장 = 조건이 True일 경우에 처리
          else:
            처리문장 = 조건이 False일 경우에 처리
        = 다중 조건문
          if 조건문:
            처리문장 => True일때 처리 => 종료
          elif 조건문:
            처리문장 => True일때 처리 => 종료
          elif 조건문:
            처리문장 => True일때 처리 => 종료
          else
            처리문장 => 처리 조건이 없는 경우
            => 생략이 가능
    2) 반복문
        = for
        = while
    3) 반복제어문
        = break
'''
import random

'''
# 단일 조건문
rand = random.randrange(1,101)
# 1~100까지 사이의 난수
if (rand%2==0):
  print(f"{rand}는(은) 짝수입니다")
if (rand%2!=0):
  print(f"{rand}는(은) 홀수입니다")

if (rand%2==0):
  print(f"{rand}는(은) 짝수입니다")
else:
  print(f"{rand}는(은) 홀수입니다")
'''
# 다중 조건문 => yml
rand = random.randrange(1,101)
if rand>= 90:
  print(f"{rand}: A학점")
elif rand>= 80:
  print(f"{rand}: B학점")
elif rand>= 70:
  print(f"{rand}: C학점")
elif rand>= 60:
  print(f"{rand}: D학점")
else:
  print(f"{rand}: F학점")