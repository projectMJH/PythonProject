from django.urls import path

from web import views
from web import foodViews
from web import recipeViews

urlpatterns=[
  path('',views.main_page),
  path('food/list_vue/',foodViews.foodListData),
  path('food/detail_vue/',foodViews.foodDetailData),
  path('recipe/list_vue/', recipeViews.recipeList),
  path('recipe/detail_vue/', recipeViews.recipeDetail)
]