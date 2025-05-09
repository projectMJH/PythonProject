#pip install pymysql
import pymysql as pm
'''
page=int(input("페이지 입력: "))
start=(12*page)-12
conn=pm.connect(host="127.0.0.1",user="root",
                password="happy",db="mydb",
                charset="utf8")
cur=conn.cursor()
sql=f"""
      SELECT * FROM genie_music ORDER BY mno ASC
      limit {start},12
    """
cur.execute(sql)
music=cur.fetchall()
cur.close()
conn.close()
for m in music:
  mm=list(m)
  for mmm in mm:
    print(mm, end=" ")
  print()
'''
def musicDetail(mno):
  conn=pm.connect(host="127.0.0.1",user="root",
                password="happy",db="mydb",
                charset="utf8")
  cur=conn.cursor()
  sql=f"""
        SELECT * FROM genie_music
        WHERE mno={mno}
      """
  cur.execute(sql)
  music=cur.fetchone()
  cur.close()
  conn.close()
  return music

mno=int(input("뮤직 번호 입력: "))
music=musicDetail(mno)
# 튜플 => 데이터 변경이 안된다 => list 변환
m=list(music)
for s in m:
  print(s)