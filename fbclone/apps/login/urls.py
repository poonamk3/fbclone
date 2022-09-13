# from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('home/',views.index ,name="home"),
    path('', views.HomeView.as_view()),
    path('register', views.RegisterView.as_view(),name="register"),
    path('accounts/profile/',views.ProfileView.as_view(),name="profile"),
]
