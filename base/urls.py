from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('dashboard',views.dashboard,name='dashboard'),
    
]