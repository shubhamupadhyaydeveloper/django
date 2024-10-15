from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_home,name="product_home"),
    path('<int:product_id>/',views.product_detail,name="product_detail"),
    path('create/',views.create_product,name="create_product"),
]
