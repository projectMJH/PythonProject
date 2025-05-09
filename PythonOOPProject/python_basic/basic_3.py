"""
  1. 접근지정어 : 다른 클래스에서 변수에 접근 금지
                => 함수를 이용해서 접근
                => 데이터를 가지고 가서 변형
     public
     protexted
     private
   class A
     name='' => public
     ------------------------
     _name='' => protected
     __name='' => private
     ------------------------ getter/setter
"""
from _overlapped import NULL


class Human:
  name = ''
  sex = ''
  age = 0

  def __init__(self, name, sex, age):
    self.name = name
    self.sex = sex
    self.age = age

  """
     public void run()
     {

     }
  """

  def run(self):
    pass

  def eat(self):
    pass


man = Human('홍길동', '남자', 20)
print("나이:{},sex:{},age:{}"
      .format(man.name, man.sex, man.age))
# 변수 , 메소드 (기본 : public) _ , __
"""
  1. 재사용 : is-a , has-a 
              상속    포함 클래스 
"""


# 상속 => 다중 상속이 가능
class Student(Human):
  school = ''
  subject = ''

  def __init__(self, school, subject):
    self.school = school
    self.subject = subject

  # 오버라이딩
  """
    1. 상속조건 
    2. 함수명이 동일 
    3. 매개변수가 동일 
    4. 리턴형이 동일 
    => 덮어쓴다 , 기존의 기능을 수정 
    => 오버로딩 / 오버라이딩 
         new      modify 
    => 면접 : 
         정의 / 부연 (반드시 => 프로젝트)
         ---- 
  """

  def run(self):
    print(f"{self.name} 학생이 달린다")

  def eat(self):
    print(f"{self.name} 학생이 먹는다")


# 객체 생성
std = Student("SIST", "Full Stack")
std.name = "홍길동"
std.sex = "남자"
std.age = 30
"""
  숫자+숫자 = 숫자
  문자+문자 = 문자
  문자+숫자 = X
      ---- str(숫자)
"""
# 출력
print("이름:" + std.name)
print("성별:" + std.sex)
print("나이:" + str(std.age))
print("학교명:" + std.school)
print("전공:" + std.subject)
