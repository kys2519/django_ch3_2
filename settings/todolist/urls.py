from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.home),
    path('calender/', views.calender),
]