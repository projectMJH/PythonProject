"""
  데이터 수집: 크롤링 / 공공데이터 / 데이터셋
      | -- BS4, 셀레니움 ... CSV, 엑셀, text, 오라클 ...
     분석
      | -- Numpy / Pandas
     출력 (시각화) -- Matplotlib seaborn
     ----------- 데이터 전처리
                      |
                    머신러닝 (학습)
                    딥러닝
                    ------- AI
  Numpy : 배열, 행렬 = 복잡한 연산 처리
    = 집합 데이터형
      리스트형(list) => 배열 => []
      = 여러개의 값을 하나의 단위로 묶어주는 자료형: 배열
      = 형식 [1,2,3,4,5]
      = 데이터 관리시 효율적으로 관리하기 위해 사용
                    ----------------
                    접근이 쉽고 수정이 가능
      = 인덱스로 처리 => 순서가 존재, 중복 데이터 허용
        => ArrayList
      = 사용되는 위치 : 크롤링 데이터가 저장
      score=[100,200,[300,400,500],600]
              0   1   -----------   3
                            2
      = JSON / CSV / XML
"""
"""
import numpy as np
a=[10,30,20]
b=[100,300,200]
c=a+b
print(c)
a1=np.array(a)
b1=np.array(b)
c1=a1+b1
print(c1)

score=[100,[200,300,400],500,600]
# 인텍싱
#
print(score[0])
# 2차원 배열 사용
print(score[1][0])
print(score[1][1])
print(score[1][2])
print(score[2])
print(score[3])


member=["홍길동",90,"박문수",90,"심청이",80,"이순신",100,"강감찬",75]
print(member[0:2])
print(member[2:])
print(member[:])
"""
"""
  1. list => 크롤링 []
  2. tuple => 데이터베이스 ()
  3. dict => JSON {키:값}
  4. CSV => DataFrame => table(2차원)
            --------- Matplotlib
            ------------
            column...
            ------------
            value...
            ------------
            value...
            ------------
  5. 중복데이터 삭제 => set {}         
"""
# nums=[10,20,30,40,50,60,70,80,90]
# 요소 변경 / 추가 / 삭제
nums=list(range(10))
print(nums)
#범위내 요소 변경
nums[2:4]=[20,30]
print(nums)
nums[6:]=[60,70,80,90]
print(nums)
# 데이터 추가 => 맨뒤에 추가
nums.append(50)
print(nums)
nums.append([100,200,300])
print(nums)
# 중간에 첨부
nums.insert(0,1000)
print(nums)
nums=[10,20,30,40,50,60,70]
#      0  1  2  3  4  5  6
del nums[3]
print(nums)
del nums[3:]
print(nums)
# 전체 삭제 => nums[:} => clear
nums.clear()
print(nums)
# 주요 함수
score=[86,74,56,90,88]
score.reverse()
print(score)
score.sort()
print(score)
score.sort(reverse=True)
print(score)
# sort() / reverse(), del, append(), insert, clear
data=[1,2,3,1,4,5,6,4,2,1,6,7,9,8,8]
print(list(set(data)))
"""
  분석에 필요한 데이터형 : list, dict, tuple, set
        |
        연산처리 => 연산자
                | 복잡한 연산처리 : Numpy
                | 분석 : Pandas, R
                | 시각화 : Matplotlib
                    |
                   머신러닝: 통계 / 확률
                           이산수학 (미적분) 
                   수학 / 물리 / 국어        
        제어문        
"""
"""
  tuple
    : 리스트와 비슷하지만 한번 값이 정해지면 변경이 불가능하다
    : 데이터베이스 값 읽기
    : () 

score=(90)
print(score)
score=(90,)
print(score)
score=10,20,30,40,50 #() 생략 가능
print(score)
# 순서를 가지고 있다 => 인텍스번호가 만들어진다 => 0
print(score[1:2])
#score[0]=100
a=list(score)
print(a)
print(tuple(a))
"""
"""
  set : 중복을 허용하지 않는다
        순서가 없는 자료형 (인텍스 번호가 없다)
"""