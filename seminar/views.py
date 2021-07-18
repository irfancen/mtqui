from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def seminarlanding(request):
    return render(request, 'base_seminar.html')
