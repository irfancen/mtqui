from django.shortcuts import render
from django.http import HttpResponse

def gallery(request):
    return HttpResponse("Hello this is gallery page")
