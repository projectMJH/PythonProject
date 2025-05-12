'''
  = 문자열 제어
    String
      표현 : '',"" 사이에 들어간 문자들
      'Hellp Python', "안녕하세요"
      index번호가 0부터 시작
      msg="Hello Python"
      => msg[0] => 추출 (배열형식으로 추출)
      => 슬라이싱

msg="Hello Python"
print(msg)
print(msg[0])
for s in msg:
  print(s,end="")
print()
ss="ABCDEFGHIJ"
#   01234
#          -2-1
print(f"ss={ss}")
print(f"ss[0]={ss[0]}") # 처음 문자
print(f"ss[-1]={ss[-1]}") # 마지막 문자
print(f"ss[0:3]={ss[0:3]}") # 처음부터 3글자
print(f"ss[1:]={ss[1:]}") # 두번째부터 마지막
print(f"ss[-3:-1]={ss[-3:-1]}")
print(f"ss[:]={ss[:]}") # 전체 출력
print(f"ss[0:3:2]={ss[0:3:2]}")
'''
'''
  문자열의 주요 함수
  
'''
data=' Hello Python '
print(data.upper()) # 대문자
print(data.lower()) # 소문자
# trim() : 공백 제거
print(data.rstrip()) # 오른쪽 공백 제거
print(data.lstrip()) # 왼쪽 공백 제거
print(data.strip()) # 좌우 공백 제거
# 대/소 문자 교환
print(data.swapcase())
# 문자 길이
print(data.__len__())
print(len(data))
# 시작 문자열
print(data.startswith(" He"))
# 첫번째 문자를 찾기 => 문자의 index
print(data.find("l"))
# 찾기 => 갯수
print(data.count("l"))
print(data.index("e")) # indexOf
print(data.split(" "))
