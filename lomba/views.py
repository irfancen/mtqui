from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
import datetime

def cek_timeline(lomba, trainingTL):
    if not lomba.custom_timeline:
        today = datetime.date.today()
        for item in trainingTL:
            if item.start_date == today:
                trainingTL.filter(id=item.id).update(active=True)
            elif item.start_date > today:
                trainingTL.filter(id=item.id).update(active=None)

            if item.finish_date < today:
                trainingTL.filter(id=item.id).update(active=False)

def lomba_list(request):
    lombaList = Lomba.objects.all()
    timeline = TrainingTimeline.objects.all()

    for lomba in lombaList:
        trainingTL = TrainingTimeline.objects.filter(nama_lomba=lomba)
        cek_timeline(lomba, trainingTL)

    res = dict.fromkeys(lombaList)
    for k in res.keys():
        temp = timeline.filter(nama_lomba=k)
        for item in temp:
            if item.active:
                res[k] = item

    args = {
        'lombaList': lombaList,
        'timeline': timeline,
        'active': res
    }

    return render(request, "lomba.html", args)

def lomba_detail(request, alias):
    lomba = get_object_or_404(Lomba, alias=alias)
    rules = LombaRule.objects.filter(nama_lomba=lomba)
    requirement = ParticipantRequirement.objects.filter(nama_lomba=lomba)
    learnt = TrainingLearnt.objects.filter(nama_lomba=lomba)
    trainingTL = TrainingTimeline.objects.filter(nama_lomba=lomba)

    trainingTL = trainingTL.all().order_by('start_date')
    mentors = lomba.nama_mentor.all()
    isLoggedIn = False

    if request.user.is_authenticated:
        isLoggedIn = True

    cek_timeline(lomba, trainingTL)

    isActive = False
    for item in trainingTL:
        if item.active:
            isActive = True

    args = {
        'lomba': lomba,
        'rules': rules,
        'requirement': requirement,
        'mentors': mentors,
        'learnt': learnt,
        'timeline': trainingTL,
        'isActive': isActive,
        'isLoggedIn': isLoggedIn
    }
    return render(request, "lomba_detail.html", args)
