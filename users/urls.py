from django.contrib import admin
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('register/', userViews.register_user),
]