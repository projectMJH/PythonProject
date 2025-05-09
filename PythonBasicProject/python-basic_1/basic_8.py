'''
  변수 설정
    => 변수 = 값 : 변수에 데이터형을 사용하지 않는다
                  자동으로 지정하는 데이터
       <class 'int'>
       <class 'float'>
       <class 'bool'>
       <class 'str'>
       예) a=10 => a <class 'int'>
          b=10.5 => b float
          c=True => c bool
          d='aaa' => d str
            "aaa"

          => 자바스크립트: let, const
             코틀린: var, val
          => 형변환
              정수: int()
              실수: float()
              문자: str()
              논리형: bool() => 0,0.0, 기타숫자
                               -----  ------
                               False   True
    ------------------------------------ 단일 변수
    집합 데이터형
    -----------
    list:[] => 배열 => Numpy
         순서가 존재(인덱스가 존재), 데이터 중복 허용
         데이터 변경이 가능, 가장 많이 사용된 데이터형
    tuple:() => 데이터베이스 값 출력
         순서가 존재, 데이터 중복 허용
         데이터 변경은 불가능
    set:{} => 순서가 존재하지 않는다
         데이터 중복은 허용하지 않는다
    dict:{키:값} => JSON
         Map => 키와 값으로 설정
    tuple,set,list는 상호 변환이 가능
'''
a=[1,2,3,4,5,5,4,3]
b=(1,2,3,4,5,5,4,3)
c={1,2,3,4,5,5,4,3}
print(a)
print(b)
print(c)
print(list(b))
print(list(c))
print(tuple(a))
print(tuple(c))
print(set(a))
print(set(b))