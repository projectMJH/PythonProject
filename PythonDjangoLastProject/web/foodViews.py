from django.http import JsonResponse
from web import foodModels

def foodListData(request):
  try:
    page=request.GET['page']
  except Exception as e:
    page="1"
  curpage=int(page)
  f,totalpage=foodModels.foodListData(curpage)
  fd=[]
  for ff in f:
    fdata={
      "fno":ff[0],
      "name":ff[1],
      "poster":ff[2]
    }
    fd.append(fdata)
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

  return JsonResponse(list)
'''
fno,name,poster,address,phone,
                time,parking,theme,score,price,type
'''
def foodDetailData(request):
  fno=request.GET['fno']
  f,theme=foodModels.foodDetailData(int(fno))
  detail={
    "fno":f[0],
    "name": f[1],
    "poster": f[2],
    "address": f[3],
    "phone": f[4],
    "time": f[5],
    "parking": f[6],
    "theme": theme,
    "score": f[8],
    "price": f[9],
    "type": f[10]
  }
  return JsonResponse(detail)