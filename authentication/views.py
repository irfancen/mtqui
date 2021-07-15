from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard:home"))
    
    context = {}

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                django_login(request, user)
                return HttpResponseRedirect(reverse("dashboard:home"))

    context["form"] = AuthenticationForm()
    return render(request, "authentication/login.html", context)

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        
    return HttpResponseRedirect(reverse("authentication:login"))
    
