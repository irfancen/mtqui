from django.shortcuts import render
from .models import Seminar
from django.utils import timezone
import random


# Create your views here.

def getairtime(dt_data):
    air_time = str(dt_data.days) + "days" + " " + str(dt_data.seconds // 3600) + "hrs" + " " + str(
        (dt_data.seconds // 60) % 60) + "mins"
    return air_time

def seminarlanding(request):
    semua_seminar = Seminar.objects.all()

    id_list = []
    random_seminar = []

    for seminar in semua_seminar:
        id_list.append(seminar.id)

    # randomized_seminar = random.sample(id_list, 3)

    # Get 3 or less random seminar
    if(Seminar.objects.count() < 3):
        randomized_seminar = random.sample(id_list, Seminar.objects.count())
    else:
        randomized_seminar = random.sample(id_list, 3)

    # For each carousel seminar, get its air time and check if past or not
    for i in randomized_seminar:
        temp_seminar = Seminar.objects.get(id=i)
        temp_seminar.air_time = getairtime(temp_seminar.d_day - timezone.localtime())

        if temp_seminar.d_day < timezone.localtime():
            temp_seminar.is_past = True

        random_seminar.append(temp_seminar)

    for seminar in semua_seminar:
        if seminar.d_day < timezone.localtime():
            seminar.is_past = True

    argument = {
        'seminar_list': semua_seminar,
        'carousel_seminar': random_seminar,
    }

    return render(request, 'seminar_landing.html', argument)


def getseminar(request, id_seminar):
    seminar = Seminar.objects.get(id=id_seminar)
    guest_stars = seminar.guest_stars.all()
    all_subjects = [x for x in seminar.subjects.split(';') if x]
    all_biografi = [x for x in guest_stars.first().biografi.split(';') if x]

    if seminar.d_day < timezone.localtime():
        seminar.is_past = True

    seminar.air_time = getairtime(seminar.d_day - timezone.localtime())

    argument = {
        'seminar': seminar,
        'guest_stars': guest_stars,
        'all_subjects': all_subjects,
        'all_biografi': all_biografi
    }
    return render(request, 'each_seminar.html', argument)


def getseminarform(request):
    return render(request, 'form_template.html')
