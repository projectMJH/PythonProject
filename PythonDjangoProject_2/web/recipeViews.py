from django.shortcuts import render,redirect
from web import recipeModels

def recipe_list(request):
  try:
    page=request.GET['page']
  except Exception as e:
    page="1"
  curpage=int(page)
  recipeList,totalpage=recipeModels.recipeListData(curpage)
  BLOCK=10

  startPage=((curpage-1)//BLOCK*BLOCK) + 1
  endPage=((curpage-1)//BLOCK*BLOCK) + BLOCK

  if endPage>totalpage:
    endPage=totalpage

  rd=[]
  for r in recipeList:
    rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
    rd.append(rdata)
  recipe_data={
    "rd":rd,
    "curpage":curpage,
    "totalpage":totalpage,
    "startPage":startPage,
    "endPage":endPage,
    "range": range(startPage, endPage+1)
  }

  return render(request,
                "recipe/list.html",
                recipe_data)

# 상세보기 => 쿠키 => redirect => detail_before
def recipe_before(request):
  no=request.GET['no']
  response=redirect("/web/recipe/detail/?no="+str(no))
  response.set_cookie(f"recipe{no}",no,60*60*24)

  return response
# 상세보기
def recipe_detail(request):
  no=request.GET['no']
  return render(request,"recipe/detail.html")