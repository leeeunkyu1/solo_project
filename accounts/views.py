# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
AuthenticationForm,
PasswordChangeForm,
)
from django.views.decorators.http  import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms  import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash



@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "articles:index"
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)




@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index")



@require_http_methods(["GET","POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("articles:index")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        return redirect("articles:index")
    

@require_http_methods(["GET","POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
        
        
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)
    
    


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)    #비밀번호 변경 후 로그인 유지를 위해 세션을 유지해줌.
            return redirect("articles:index") 
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, "accounts/change_password.html", context)