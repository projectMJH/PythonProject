from django.shortcuts import render
from recipeapp import models
# Create your views here.
# 웹관련 모든 서버는 => request,response
def index(request):
  return render(request,"recipe/index.html")
#render => java:forward

def recipeList(request):
  page=request.GET['page']
  # 정수(X) => str
  # request.getParameter("page")
  # request.POST['fd']
  curpage=int(page)
  # 오라클로부터 데이터 받기
  list,totalpage=models.recipeListData(curpage)

  recipe_list=[]
  for r in list:
    rr={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
    recipe_list.append(rr)
    # dict형으로 변경 => tuple 형은 값을 읽을 수 없다
    # list:[], set:{}, tuple:(),
  BLOCK=10
  startPage=((curpage-1)//BLOCK*BLOCK)+1
  endPage=((curpage-1)//BLOCK*BLOCK)+BLOCK
  if endPage>totalpage:
    endPage=totalpage

  return render(request,"recipe/list.html",
                {"rd":recipe_list,"curpage":curpage,"startPage":startPage,
                        "endPage":endPage,"totalpage":totalpage,
                        "range":range(startPage,endPage+1)})

def recipeDetail(request):
  no=request.GET['no']
  # String no=request.getParameter("no")
  rd,rmake,rdata=models.recipeDetail(int(no))

  #print(rd)
  #print(rmake)
  #print(rdata)
  # rd= () = {}:JSON
  recipe_data={
    "no":rd[0],
    "title": rd[1],
    "chef": rd[2],
    "chef_poster": rd[3],
    "chef_profile": rd[4],
    "info1": rd[5],
    "info2": rd[6],
    "info3": rd[7],
    "content": rd[8],
    "poster": rd[9]
  }

  fm=rmake.split("\n")
  #print(fm)
  make=[]
  posters=[]
  #재료 => ,
  data=rdata.split(",")
  for m in fm:
    if m!='':
      temp=m.split("^")
      #print(temp)
      make.append(temp[0])
      posters.append(temp[1])
      #mm={"make":temp[0],"poster":temp[1]}
      #make.append(mm)
  mm=zip(make,posters)
  detail={
    "detail":recipe_data,
    #"posters":posters,
    #"make":zip(make,posters),
    "mm":mm,
    "data":data
  }
  #print(detail)
  return render(request,"recipe/detail.html",{"rd":detail})
