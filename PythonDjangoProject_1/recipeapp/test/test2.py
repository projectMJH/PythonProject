list1=["aaa","bbb","ddd","eee"]
list2=["111","222","333","444"]
# 2개의 배열을 동시 출력하는 방법1
'''
for idx,val in enumerate(list1):
  print(f"{val}-{list2[idx]}")
'''
# 2개의 배열을 동시 출력하는 방법2
for s1,s2 in zip(list1,list2):
  print(f"{s1}-{s2}")