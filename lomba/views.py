from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def lomba_list(request):
    lombaList = Lomba.objects.all()
    args = {
        'lombaList': lombaList
    }

    return render(request, "lomba.html", args)

def lomba_detail(request, nama_lomba):
    lomba = Lomba.objects.get(nama_lomba=nama_lomba)
    rules = LombaRule.objects.filter(nama_lomba=lomba)
    learnt = TrainingLearnt.objects.filter(nama_lomba=lomba)
    timeline = TrainingTimeline.objects.filter(nama_lomba=lomba)
    mentors = lomba.nama_mentor.all()
    isLoggedIn = False

    if request.user.is_authenticated:
        isLoggedIn = True

    args = {
        'lomba': lomba,
        'rules': rules,
        'mentors': mentors,
        'learnt': learnt,
        'timeline': timeline,
        'isLoggedIn': isLoggedIn
    }
    return render(request, "lomba_detail.html", args)
