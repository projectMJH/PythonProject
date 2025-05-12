'''
  집합 데이터형 (자바 => Collection)
    1. list => List / ArrayList, Array
      = 중복데이터를 허용
      = 인덱스 번호 => 순서가 존재
      = name=["","","","","","",""...] => 그래프 작업
        일차원 배열

        데이터 수집 (크롤링, 데이터베이스)
                    |
              데이터를 모아서 관리 (CSV, TXT)
                    |
                분석 (Numpy, Pandas)
                    |
                  시각화 (MatplotLib, Seaborn)
                    |
                  완료 => 데이터베이스 누적


'''
names=["홍길동","심청이","이순신","강감찬","박문수"]
print(names)
for name in names:
  print(name)
print(f"인원:{len(names)}")
# 추가 append => 마지막에 추가
names.append("을지문덕") # add
names.insert(1,"김두한") # add(index, 문자)
print(names)
#여러개를 동시에 추가
names.extend(["김유신","춘향이"])
print(names)
# 정렬
names.sort()
print(names)
# 역순 출력
names.sort(reverse=True)
print(names)
# 삭제
names.remove('홍길동')
print(names)
