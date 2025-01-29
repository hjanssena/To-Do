from django.contrib import admin
from django.urls import path, include
from users import views as userViews

urlpatterns = [
    path('register/', userViews.register_user),
    path('', userViews.loginView),
    path('logout/', userViews.logoutView, name='logout'),
    path('change_password/', userViews.changePasswordView, name='changePassword'),
]