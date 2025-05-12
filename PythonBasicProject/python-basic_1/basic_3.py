import oracledb as db
#import pymysql as pm
'''
  라이브러리 추가 : pip install 라이브러리 추가
    예) pip install bs4 (jsoup과 유사)
      pip install numpy
      pip install pandas
      pip install matplotlib
      pip install seaborn ...
      pip install requests
      
1) 데이터베이스 연동
  1. 연결
    conn=db.connection()
    cur=conn.cursor()
    cur.execute("")
          

# Connection
conn=db.connect("hr/happy@localhost:1521/XE")
# PreparedStatement
cur=conn.cursor()
sql=f"""
      SELECT * FROM emp
    """
cur.execute(sql)
emp_list=cur.fetchall()
print(emp_list)
conn.close()
'''
def getConnection():
    conn=db.connect("hr/happy@localhost:1521/XE")
    return conn
def disConnection(conn):
    conn.close()

def foodListData(page):
    conn=getConnection()
    cur=conn.cursor()
    rowSize=12
    start=(rowSize*page)-(rowSize-1)
    end=(rowSize*page)
    sql=f"""
            SELECT fno,name,poster,num
            FROM (SELECT fno,name,poster,rownum as num
            FROM (SELECT /*+ INDEX_ASC(project_food pf_fno_pk)*/fno,name,poster
            FROM project_food))
            WHERE num BETWEEN {start} AND {end}
        """
    cur.execute(sql)
    food_list=cur.fetchall() # selectList
    cur.close()
    # selectOne => fetchOne()
    cur=conn.cursor()
    sql=f"SELECT CEIL(COUNT(*)/12.0) FROM project_food"
    cur.execute(sql)
    totalpage=cur.fetchone()
    cur.close()
    conn.close()
    return food_list,totalpage[0]
'''
def foodTotalPage():
    conn=getConnection()
    cur=conn.cursor()
    sql=f"SELECT CEIL(COUNT(*)/12.0) FROM project_food"
    cur.execute(sql)
    totalpage=cur.fetchone()
    cur.close()
    conn.close()
    return totalpage[0]
'''
def main():
    curpage=int(input("페이지 입력: "))
    # input => 리턴형 (str)
    food_list,total=foodListData(curpage)
    #total=foodTotalPage()
    for f in food_list:
        print(f)
    print(f"{curpage} page / {total} pages")
main()