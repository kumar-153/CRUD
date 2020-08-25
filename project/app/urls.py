from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('display',views.display,name='display'),
    path('delete/<int:id>/',views.delete_view, name='delete_view'),
    path('update/<int:id>/',views.update_view, name='update_view'),
    path('detail_view',views.detail_view, name='detail_view'),
]