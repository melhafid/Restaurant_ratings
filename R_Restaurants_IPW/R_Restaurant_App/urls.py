from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('restaurant/', views.rest_list, name='restaurants'),
    path('restaurant/<str:rest_name>', views.rest_detail, name='rest_detail'),
    path('employee/', views.empl_list, name='employee'),
    path('employee/<str:empl_name>', views.empl_detail, name='empl_detail'),
    path('ratings/', views.rat_list, name='ratings'),
    path('<str:rest_pk>/rate', views.rate, name='rate'),
    path('register/', views.register, name='register'),
    path('login_1/', views.login_1, name='login_1'),

]
