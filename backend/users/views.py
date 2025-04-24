from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_views(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect("/")
        else: 
            context = {"error": "Invalid"}

    return render(request, "login.html")

def logout_view(request):
    logout(request, user)
    return redirect("/")