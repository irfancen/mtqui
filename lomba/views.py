from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
import datetime, random

def cek_timeline(lomba, trainingTL):
    if not lomba.custom_timeline:
        today = datetime.date.today()
        for item in trainingTL:
            if item.start_date <= today <= item.finish_date:
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

    alias_list = []
    for lomba in lombaList:
        alias_list.append(lomba.alias)

    if Lomba.objects.count() < 4:
        lomba_random = random.sample(alias_list, Lomba.objects.count())
    else:
        lomba_random = random.sample(alias_list, 4)

    carousel_lomba = []
    for lomba in lombaList:
        for item in lomba_random:
            if lomba.alias == item:
                carousel_lomba.append(lomba)

    tlList = dict.fromkeys(lombaList)
    for k in tlList.keys():
        temp = timeline.filter(nama_lomba=k)
        for item in temp:
            if item.active:
                tlList[k] = item

    today = datetime.date.today()
    active = dict.fromkeys(lombaList)
    for k in active.keys():
        temp = timeline.filter(nama_lomba=k)
        if temp.exists():
            if temp.first().start_date <= today <= temp.latest('finish_date').finish_date:
                active[k] = temp.latest('finish_date')

    args = {
        'carousel_lomba': carousel_lomba,
        'lombaList': lombaList,
        'timeline': timeline,
        'active': active,
        'tlList': tlList
    }

    return render(request, "lomba.html", args)

def lomba_detail(request, alias):
    lomba = get_object_or_404(Lomba, alias=alias)
    rules = LombaRule.objects.filter(nama_lomba=lomba)
    requirement = ParticipantRequirement.objects.filter(nama_lomba=lomba)
    learnt = TrainingLearnt.objects.filter(nama_lomba=lomba)
    trainingTL = TrainingTimeline.objects.filter(nama_lomba=lomba)

    trainingTL = trainingTL.all().order_by('start_date', 'finish_date')
    mentors = lomba.nama_mentor.all()
    isLoggedIn = False

    if request.user.is_authenticated:
        isLoggedIn = True

    cek_timeline(lomba, trainingTL)

    pastTL = []
    for item in trainingTL:
        if (not item.active) and (item.active is not None):
            pastTL.append(item)

    isActive = False

    today = datetime.date.today()
    if trainingTL.first().start_date <= today <= trainingTL.latest('finish_date').finish_date:
        isActive = True

    args = {
        'lomba': lomba,
        'rules': rules,
        'requirement': requirement,
        'mentors': mentors,
        'learnt': learnt,
        'timeline': trainingTL,
        'pastTL': pastTL,
        'isActive': isActive,
        'isLoggedIn': isLoggedIn
    }
    return render(request, "lomba_detail.html", args)
