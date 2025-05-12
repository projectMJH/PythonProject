import pandas as pd
import numpy as np
import csv
"""
  GPT = 2년 / 3년차 = 셋팅
  아나콘다 / jupiter note book / vscode
  ---------------------------- 머신러닝 / 딥러닝
  파이참 : 커뮤니티
  => 문자열 : 모든 데이터
  => 컴파일 없이 인터프리터 : 한줄씩 번역 후 출력
  
  53페이지
    기본 문법
    -------
    변수 = 데이터형을 사용하지 않는다
          => type을 이용하면 어떤 데이터형인지 확인가능
          => <class 'int'>
  
  open => close
  => 1. txt
     2. csv
     3. 엑셀
     4. xml
     5. json
     
  => 정규식
  => 크롤링
  => 판다식 사용   
  => 시각화
             
"""
# 104 page
file=open('c:/pydata/EMP.csv')
emp=csv.reader(file)
print(emp)
for i in emp:
  print(i[1].lower())
file.close()