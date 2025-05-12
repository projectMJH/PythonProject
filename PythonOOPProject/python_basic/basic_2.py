
# 생성자 => 멤버변수에 대한 초기화
# front : window.onload=function(){}
#         --------------------------
# $(function(){}) , mounted() , useEffect() : hooks
"""
   C++ :
        class A
        {
           A(){}
           ~A(){}
        }
    자바 :
         class A
         {
            A(this){} => GC
            ------- 생략이 가능
         }
   class A
    def __init__(self) : 생성자
    def __del__(self) : 소멸자
"""
class Sawon:
    name=''
    def __init__(self,name): #생성자
        self.name=name
        print(f"생성자 Call...:{name}")
    def __del__(self): #소멸자
        print("소멸자 함수 Call...")
hong=Sawon("홍길동")
print(f"이름:{hong.name}")
# getter/setter
# 데이터 수정 / 생성자 = 실행시에 초기화
