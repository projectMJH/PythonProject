
"""
  파이썬
    = 함수 = 데이터 분석
    = 클래스 = 데이터베이스 연동
  = 입문 과정 : 다방면 , 전문 : 필드에서
"""
# has-a
from _overlapped import NULL
class Sawon:
    __sabun=0 # private
    __name=''
    __dept='' #부서
    __job=''  #직위
class Member:
    sa=NULL
    def __init__(self):
        self.sa=Sawon()
    # 함수 => public
    def display(self):
        self.sa.__dept="영업부"
        print("부서:"+self.sa.__dept)
mem=Member()
mem.sa.__name="홍길동"
print(mem.sa.__name)
mem.display()

sa=Sawon()
sa.__dept="영업부"
print(sa.__dept)
