from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login_page', views.login, name='login_page'),
    path('login', views.login, name='login'),

    path('register_page', views.register,name='register_page'),
    path('register', views.register, name='registration'),

    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),

    path('chatdashboard/', views.chatdashboard, name='chatdashboard'),
]
