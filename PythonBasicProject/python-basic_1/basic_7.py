# 내장 데이터베이스가 존재 sqlite => 4만개
'''
  1. 함수 (사용자 정의)
    = 웹 연결 => URL을 읽어서 해당 함수를 호출
                -----------
 urlpatterns=[
   path('',views.main_page),
   def main_page(request):
         recipe_data=models.mainRecipeData()
         """
           [
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
              (1,"aaa","http")
           ]
         """
         food_data=models.mainFoodData()
         rd=[]
         for r in recipe_data:
             rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
             rd.append(rdata)
         fd=[]
         for f in food_data:
             fdata={"fno":f[0],"name":f[1],"poster":f[2]}
             fd.append(fdata)
         #chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7 => Tuple ()
         cdata=models.chefMainData()
         cd={
              "chef":cdata[0],
              "poster":cdata[1],
              "mc1":cdata[2],
              "mc2": cdata[3],
              "mc3": cdata[4],
              "mc7": cdata[5]
         }
         #(poster,name,jjimcount,hit,theme)
         tdata=models.todayFoodData()
         td={
             "poster":tdata[0],
             "name":tdata[1],
             "jjimcount":tdata[2],
             "hit":tdata[3],
             "theme":tdata[4]
         }
         """
           1. list => []
           2. Tuple => (1,"aaa"...)
           3. Dict  => {키:값} => JSON , Map
         """
         news_data=models.newsData("맛집")
         #print(news_data.encode('utf-8'))
         main_data={
            "rd":rd,
            "fd":fd,
            "cd":cd,
            "td":td,
            "nd":news_data['items']
         }
         """
           list  =>  배열 [] = arraylist
           tuple => () = 데이터베이스 연결
           dict => {} = map
         """
    #return render(request,"main/home.html",main_data)
         return JsonResponse(main_data)
   path('food/list/',food_views.food_list),
   path('food/find/',food_views.food_find),
   path('recipe/list/',recipe_views.recipe_list_view),
   path('recipe/list_vue/',recipe_views.recipe_list),
   path('recipe/find/',recipe_views.recipe_find_view),
   path('recipe/find_vue/',recipe_views.recipe_find),
   path('recipe/chef/',recipe_views.recipe_chef_view),
   path('recipe/chef_vue/',recipe_views.recipe_chef),
   path('food/food_detail/',food_views.food_detail),
   path('recipe/detail/',recipe_views.recipeDetailView),
   path('recipe/detail_vue/',recipe_views.recipeDetail),
   path('goods/list/',goods_views.goods_list),
   path('recipe/chef_detail/',recipe_views.chef_detail)
   => VueJS axios('recipe/chef_detail/')

  현재
                    GateWay => MSA
                        |
    ---------------------------------------
    |                   |                 |
  NodeJS            Spring-Boot       Django
    |                   |                 |
    ---------------------------------------

'''
'''
  함수 형식
  -------
    def 함수명 (매개변수...):
      기능 처리
      return 값,값 => 없는 경우에는 사용하지 않는다 (void)
            ----- return 값이 여러개인 경우도 있다
    *** 파이썬은 기본 => 데이터형 사용하지 않는다
                       --------------------
                        => 가독성 (X)
    *** 수집 / 분석 / 통계 => 시각화
    자바 => 웹
    C   => 하드웨어
    C#  => 웹 MS                            
'''
import pymysql as pm
#연결
def getConnection():
  conn=pm.connect(host="127.0.0.1",user="root",password="happy",db="mydb",charset="utf8")
  return conn

def disConnection(conn,cur):
  cur.close()
  conn.close()

# 전체 목록 읽기
def empListData():
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        SELECT empno,ename,sal,job,date_format(hiredate,'%Y-%m-%d') as hiredate,
              dname,loc
        FROM emp JOIN dept
        ON emp.deptno=dept.deptno      
      """
  cur.execute(sql)
  emp_list=cur.fetchall()
  disConnection(conn,cur)
  return emp_list
# 검색
def empFindData(ename):
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        SELECT * FROM emp
        WHERE ename LIKE concat('%','{ename}','%')
      """
  cur.execute(sql)
  emp_list=cur.fetchall()
  disConnection(conn,cur)

  return emp_list
# 상세보기
def empDetailData(empno):
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        SELECT empno,ename,job,date_format(hiredate,'%Y-%m-%d'),sal
        FROM emp
        WHERE empno={empno}
      """
  cur.execute(sql)
  emp_data=cur.fetchone()
  disConnection(conn,cur)

  return emp_data
# 추가 => dept => () tuple 형태로 전송
def deptInsert(dept):
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        INSERT INTO dept
        VALUES(%s,%s,%s)
      """
  cur.execute(sql,dept)
  conn.commit()
  print("데이터 추가 완료")
  disConnection(conn,cur)

# 수정 => dept => () tuple 형태로 전송
def deptUpdate(dept):
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        UPDATE dept SET
        dname=%s,loc=%s
        WHERE deptno=%s 
      """
  cur.execute(sql,dept)
  conn.commit()
  print("데이터 수정 완료")
  disConnection(conn,cur)

# 삭제 => deptno
def deptDelete(deptno):
  conn=getConnection()
  cur=conn.cursor()
  sql=f"""
        DELETE FROM dept
        WHERE deptno={deptno}
      """
  cur.execute(sql)
  conn.commit()
  print("데이터 삭제 완료")
  disConnection(conn,cur)

# 전체 기능 수행
def main():
  while(True):
    print("1. 사원목록")
    print("2. 사원검색")
    print("3. 상세보기")
    print("4. 데이터추가(영업부)")
    print("5. 데이터삭제(영업부)")
    print("6. 데이터수정(영업부)")
    print("9. 종료")
    menu=int(input("메뉴 선택: "))
    if menu==9:
      print("프로그램 종료")
      break
    elif menu==1:
      emp_list=empListData()
      for emp in emp_list:
        e=list(emp)
        print(e)
    elif menu==2:
      ename=input("이름 입력: ")
      emp_list=empFindData(ename)
      for emp in emp_list:
        e=list(emp)
        print(e)
    elif menu==3:
      empno=int(input("사번 입력: "))
      emp_data=empDetailData(empno)
      print(f"사번: {emp_data[0]}")
      print(f"이름: {emp_data[1]}")
      print(f"직위: {emp_data[2]}")
      print(f"입사일: {emp_data[3]}")
      print(f"급여: {emp_data[4]}")
    elif menu==4:
      dept=(50,'영업부','부산')
      deptInsert(dept)
    elif menu == 5:
      deptDelete(50)
    elif menu==6:
      dept=('영업부수정','서울',50)
      deptUpdate(dept)
'''
  list => 가장 많이 사용 => 일차원 배열
  => a=[1,2,3,4,5...]
      a[0],a[1],a[2],...
  tuple => 데이터베이스 값 => 변경할 수 없다 => list로 변환
  => b=(1,2,3,4,5...)
      b[0],b[1],b[2],...6
      
  set => 중복을 허용하지 않는다 (제거 => 장르)
  => c={1,2,3,4,5...}
      c[0],c[1],c[2],...
  ---------------------------------------    
  dict => Map => JSON과 연결
  => c={"a":1,"b":2,....}
      d["a"],d["b"],....    
  --------------------------------------- 웹으로 전송시에 주로 사용    
'''
main()