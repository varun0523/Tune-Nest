from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('mainlogin/',mainlogin,name='mainlogin'),
    path('signup/',signup,name='signup'),
    path('userlogin/',userlogin,name='userlogin'),
    path('userlogout/',userlogout,name='userlogout'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('adminsignup/',adminsignup,name='adminsignup'),
    path('passwordreset/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    path('passwordresetsent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('passwordresetconfirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('passwordresetcompleted/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete'),name='password_reset_complete'),
    path('insert/',staff_member_required(insert),name='insert'),
    path('insert2/',staff_member_required(insert2),name='insert2'),
    path('select/',select,name='select'),
    path('search/',search,name='search'),
    path('singerdetail/<int:sid>/<str:sname>/',singerdetail,name='singerdetail'),
    path('detail/<int:sid>/<str:sname>/',detail,name='detail'),
    path('like/<int:sid>/',like,name='like'),
    path('dislike/<int:sid>/',dislike,name='dislike'),
    path('likepage/',likepage,name='likepage'),
    path('trending/',trending,name='trending'),
    path('phonk/',phonk,name='phonk'),
    
    
]