from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def sign(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = UserCreationForm()
    return render(request, "account/sign.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog:index")
    else:
        form = AuthenticationForm()
    return render(request, "account/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("blog:index")
