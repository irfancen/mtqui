from django.shortcuts import render
from django.http import HttpResponse

def lombaPage(request):
    return HttpResponse("Lomba Page")
