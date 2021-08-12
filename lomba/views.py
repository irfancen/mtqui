from django.shortcuts import render
from .models import *
import datetime

def lomba_list(request):
    lombaList = Lomba.objects.all()
    timeline = TrainingTimeline.objects.all()

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
    lomba = Lomba.objects.get(alias=alias)
    rules = LombaRule.objects.filter(nama_lomba=lomba)
    learnt = TrainingLearnt.objects.filter(nama_lomba=lomba)
    trainingTL = TrainingTimeline.objects.filter(nama_lomba=lomba)
    trainingTL = trainingTL.all().order_by('timeline')
    mentors = lomba.nama_mentor.all()
    isLoggedIn = False

    if request.user.is_authenticated:
        isLoggedIn = True

    temp = None
    today = datetime.date.today()
    for item in trainingTL:
        if temp is None:
            if item.timeline > today:
                trainingTL.filter(timeline=item.timeline).update(active=None)
            elif item.timeline == today:
                trainingTL.filter(timeline=item.timeline).update(active=True)
            else:
                trainingTL.filter(timeline=item.timeline).update(active=False)
            temp = item
        else:
            if item.timeline > today:
                trainingTL.filter(timeline=item.timeline).update(active=None)
                if temp.timeline <= today:
                    trainingTL.filter(timeline=temp.timeline).update(active=True)
            elif item.timeline < today:
                trainingTL.filter(timeline=item.timeline).update(active=False)
                trainingTL.filter(timeline=temp.timeline).update(active=False)
            temp = item

    isActive = False
    for item in trainingTL:
        if item.active:
            isActive = True

    args = {
        'lomba': lomba,
        'rules': rules,
        'mentors': mentors,
        'learnt': learnt,
        'timeline': trainingTL,
        'isActive': isActive,
        'isLoggedIn': isLoggedIn
    }
    return render(request, "lomba_detail.html", args)
