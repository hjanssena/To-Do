from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = UserCreationForm();
    return render(request, "register.html", {"form":form})

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/main")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", { "form":form })

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")

def changePasswordView(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            u = request.user
            usr = User.objects.get(username=u.username)
            if usr.check_password(request.POST["password"]):
                usr.set_password(request.POST["new_password"])
                usr.save()
            else:
                messages.add_message(request, messages.ERROR, 'Wrong password, please verify.')
                return redirect("/main/")
    logout(request)
    return redirect("/login")