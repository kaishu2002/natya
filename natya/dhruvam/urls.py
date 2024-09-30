from django import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from .views import*
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('cnt',views.cnt),
    path('register', views.register, name='register'),
    path('programs', views.programs, name='programs'),
    path('logout/', views.Logout, name='logout'),
    path('login', views.doLogin, name='Login'),
    path('cnt', ContactUser.as_view(), name='contact_user'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('gurureg/', views.guru_register, name='guru_register'),
    path('approve_gurus/', ApproveGurusView.as_view(), name='approve_gurus'),
    path('views_users/<int:ut>', views.view_users_and_gurus, name='views_users'),
    path('selectview/', SelectViews.as_view(), name='selectview'),  
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update_profile', UpdateProfileView.as_view(), name='update_profile'),
    path('guruprofile/', GuruProfileView.as_view(), name='guruprofile'),
    path('updateg_profile/', UpdateProfileView.as_view(), name='updateg_profile'), 
    path('password_change_form', ResetPasswordView.as_view(), name='reset_password'),
    path('guru_detail/<int:pk>/', GuruDetailView.as_view(), name='guru_detail'),
    path('guru_create/<int:pk>/', GuruCreatView.as_view(), name='guru_create'),
    path('bharatanatyam', Bharatanatyamview.as_view(), name='Bharatanatyam'),
    path('mohiniyattam', MohiniyattamView.as_view(), name='mohiniyattamview'),
    path('kuchipudi', kuchipudiView.as_view(), name='kuchipudiview'),
    path('kathak', kathakView.as_view(), name='kathakview'),
    path('odissi', odissiView.as_view(), name='odissiview'),
    path('add_class', AddClassView.as_view(), name='add_class'),
    path('class_details', views.class_detail_view, name='class_details'),
    path('class_detail/<int:value>',views.class_detail,name='class_detail'),
    path('beginners/', beginners_view, name='beginners'),
    path('composition/', composition_view, name='composition'),
    path('performance/', performances_view, name='performances'),
    path('intermediate/', intermediate_view, name='intermediate'),
    path('about', views.about, name='about'),  
    path('tenchiques/', tenchiques_view, name='tenchiques'),
    path('gita/', gita_view, name='gita'),
    path('gurus/', ApprovedGurusView.as_view(), name='gurus'),  
    path('guru/<int:pk>/', GuruDetailView.as_view(), name='guru_detail'),
    path('video_details/', VideoDetailView.as_view(), name='video_details'),
    

]