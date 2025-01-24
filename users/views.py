from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
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