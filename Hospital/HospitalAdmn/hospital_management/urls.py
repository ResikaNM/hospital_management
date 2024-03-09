from django.urls import path
from .import views

urlpatterns=[
    path('',views.signupView,name='signup'),
    path('login/',views.loginView,name='login'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    path('patient/', views.dashboard,name='Patient_Dashboard'),
    path('doctor/', views.dashboard, name='Doctor_Dashboard'),
    path('blog/',views.blog_list,name='blog_list'),
    path('post/<int:pk>/',views.blog_detail,name='blog_detail'),
    path('create/', views.create_blog_post, name='create_blog_post'),



]
