from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


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
