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
    path('logout', views.Logout, name='logout'),
    path('login', views.doLogin, name='Login'),
    path('cnt', ContactUser.as_view(), name='contact_user'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('gurureg', views.guru_register, name='guru_register'),
    path('approve_gurus', ApproveGurusView.as_view(), name='approve_gurus'),
    path('view_users', ViewUsersAndGurus.as_view(), name='view_users'),
    path('selectview/', SelectViews.as_view(), name='selectview'),  
    path('profile', UserProfileView.as_view(), name='profile'),
    path('update_profile', UpdateProfileView.as_view(), name='update_profile'),
    path('guruprofile/', GuruProfileView.as_view(), name='guruprofile'),
    path('updateg_profile/', UpdateProfileView.as_view(), name='updateg_profile'), 
    path('password_change_form', ResetPasswordView.as_view(), name='reset_password'),
    path('guru_detail/<int:pk>/', GuruDetailView.as_view(), name='guru_detail'),
    path('guru_create/<int:pk>/', GuruCreatView.as_view(), name='guru_create'),
    path('bharatanatyam', Bharatanatyamview.as_view(), name='Bharatanatyam'),
]