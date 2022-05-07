from django.urls import path
from . import views

urlpatterns = [
     path('',views.category,name="home"),
     path('<int:id>',views.category_detail,name="detail"),
     
     
     path('success',views.success,name="success"),
     
     
     path('search',views.search,name="search")
   



]