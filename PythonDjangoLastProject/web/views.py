from django.shortcuts import render
from django.http import JsonResponse
from web import models
# Create your views here.
def main_page(request):
  food_list,recipe_list=models.mainPageData()
  fd=[]
  for f in food_list:
    fdata={
      "fno":f[0],
      "name": f[1],
      "poster": f[2],
    }
    fd.append(fdata)
  rd=[]
  for r in recipe_list:
    rdata={
      "fno":r[0],
      "name": r[1],
      "poster": r[2],
    }
    rd.append(rdata)
  md={
    "fd":fd,
    "rd":rd
  }
  return JsonResponse(md)

