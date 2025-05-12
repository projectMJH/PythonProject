# 데이터베이스 CRUD => sqlite
"""
   프로그램 : 데이터를 모아서 관리
            => 변수
   파이썬 클래스 구성 요소
      class class명:
        -----------
          멤버변수 영역
            name : public
            _name : protected
            __name : private
        -----------
          생성자
          def __init__(self):
          소멸자
          def __del__(self):
          ** self => this
        -----------
          함수정의
          => 매개변수에는 self를 포함하고 있다
        -----------

        상속 : 수정후에 재사용
        포함 : 변경없이 있는 그대로 사용
"""
import sqlite3
from _overlapped import NULL
class StudentVO:
    hakbun=0
    name=''
    kor=0
    eng=0
    math=0
    """
    def setHakbun(self,hakbun):
        self.hakbun=hakbun
    def getHakbun(self):
        return self.hakbun
    """
class StudentDAO:
    conn=NULL
    cursor=NULL
    def __init__(self):
        print("생성자 함수 호출")
    def __del__(self):
        print("소멸자 함수 호출")
    def getConnection(self):
        self.conn=sqlite3.connect("student.db")
        self.cursor=self.conn.cursor()
    def disConnection(self):
        self.cursor.close()
        self.conn.close()
    def dbCreate(self):
        self.getConnection()
        sql="""
            CREATE TABLE IF NOT EXISTS student(
            hakbun int,name text,kor int,eng int,math int)
            """
        self.cursor.execute(sql)
        self.disConnection()
    def insert(self,vo):
        self.getConnection()
        data=(vo.hakbun,vo.name,vo.kor,vo.eng,vo.math)
        sql="INSERT INTO student VALUES(?,?,?,?,?)"
        self.cursor.execute(sql,data)
        self.conn.commit()
        print("학생 등록 완료")
        self.disConnection()
    def selectList(self):
        self.getConnection()
        sql="SELECT * FROM student"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        # => session.selectList()
        self.disConnection()
        return data
    def delete(self,hakbun):
        self.getConnection()
        sql=f"DELETE FROM student WHERE hakbun={hakbun}"
        self.cursor.execute(sql)
        self.conn.commit()
        self.disConnection()
    def selectOne(self,hakbun):
        self.getConnection()
        sql=f"SELECT * FROM student WHERE hakbun={hakbun}"
        self.cursor.execute(sql)
        data=self.cursor.fetchone()
        self.disConnection()
        return data
dao=StudentDAO()
"""
print("dao객체 생성")
dao.dbCreate()
print("데이터베이스 테이블 생성")
"""
"""
vo=StudentVO()
vo.hakbun=int(input("학번입력:"))
vo.name=input("이름입력:")
vo.kor=int(input("국어입력:"))
vo.math=int(input("수학입력:"))
vo.eng=int(input("영어입력:"))
dao.insert(vo)
print("학생 입력 완료")
"""
hakbun=int(input("상세볼 학번:"))
#dao.delete(hakbun)
data=dao.selectOne(hakbun)
print(data)
#print("삭제 완료!!")
#data=dao.selectList()
#for row in data:
    #print(row)
