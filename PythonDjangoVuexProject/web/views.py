from django.shortcuts import render
from web import models

# Create your views here.
from django.http import JsonResponse
import numpy as np
import pandas as pd
import oracledb as db
import matplotlib.pyplot as plt

# @RestController

def foodListData(request):
  page=request.GET['page'] # params:{page:1}
  # 문자열
  curpage=int(page)
  # 데이터베이스 연동
  food_list,totalpage=models.foodListData(curpage)
  # Tuple (...) => Dict 로 변경(JSON)

  fd=[]
  for f in food_list:
    ff={"fno":f[0],"name":f[1],"poster":f[2]}
    fd.append(ff)
  BLOCK=10
  startPage=((curpage-1)//BLOCK*BLOCK)+1
  endPage=((curpage-1)//BLOCK*BLOCK)+BLOCK
  if endPage > totalpage:
    endPage=totalpage

  list={
    "fd":fd,
    "curpage":curpage,
    "totalpage":totalpage,
    "startPage":startPage,
    "endPage":endPage
  }
  # food_list:{}
  return JsonResponse(list)

def foodDetailData(request):
  no=request.GET['fno']
  fno=int(no)
  fd,theme,content=models.foodDetailData(fno)
  """
  fno,name,poster,score,address,phone,
                parking,time,type
  """
  f={
    "fno":fd[0],
    "name":fd[1],
    "poster":fd[2],
    "score":fd[3],
    "address":fd[4],
    "phone":fd[5],
    "parking":fd[6],
    "time":fd[7],
    "type":fd[8],
    "theme":theme,
    "content":content
  }

  return JsonResponse(f)

#C:\springDev\springStudy\.metadata\.plugins\org.eclipse.wst.server.core\tmp0\wtpwebapps\SpringLastProject\
def empGraphData(request):
  deptno=request.GET['deptno']
  no=int(deptno)
  conn = db.connect("hr/happy@localhost:1521/XE")
  cur = conn.cursor()
  sql = f"""
        SELECT empno,ename,job,TO_CHAR(hiredate,'YYYY-MM-DD') as dbday,
              sal,deptno
        FROM emp WHERE deptno={no}
        ORDER BY sal DESC
      """
  cur.execute(sql)
  list = cur.fetchall()

  emp = pd.DataFrame(list)

  #print(emp)
  colname=cur.description
  #print(colname)
  cur.close()
  conn.close()


  col=[]
  for i in colname:
    col.append(i[0].lower())
  emp=pd.DataFrame(list,columns=col)
  print(emp)
  emp.plot.scatter(x='ename',y='sal',s=300,c='red')
  #plt.show()
  plt.savefig(f"C:/springDev/springStudy/.metadata/.plugins/org.eclipse.wst.server.core/tmp0/wtpwebapps/SpringLastProject/img/emp{no}.png")

  return JsonResponse({"msg":"yes"})

