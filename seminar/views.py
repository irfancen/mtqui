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
    air_time = []
    for seminar in semua_seminar:
        id_list.append(seminar.id)

    randomized_seminar = random.sample(id_list, 3)

    for i in randomized_seminar:
        temp_seminar = Seminar.objects.get(id=i)
        air_time.append(temp_seminar.d_day - timezone.localtime())

        if temp_seminar.d_day < timezone.localtime():
            temp_seminar.is_past = True

        random_seminar.append(temp_seminar)

    for seminar in semua_seminar:

        if seminar.d_day < timezone.localtime():
            seminar.is_past = True

    argument = {
        'seminar_list': semua_seminar,
        'first_seminar': random_seminar[0],
        'second_seminar': random_seminar[1],
        'third_seminar': random_seminar[2],
        'first_air_time': getairtime(air_time[0]),
        'second_air_time': getairtime(air_time[1]),
        'third_air_time': getairtime(air_time[2]),
    }

    return render(request, 'seminar_landing.html', argument)


def getseminar(request, id_seminar):
    seminar = Seminar.objects.get(id=id_seminar)
    guest_stars = seminar.guest_stars.all()
    all_subjects = [x for x in seminar.subjects.split(';') if x]

    if seminar.d_day < timezone.localtime():
        seminar.is_past = True

    dt = seminar.d_day - timezone.localtime()
    air_time = getairtime(dt)

    argument = {
        'seminar': seminar,
        'guest_stars': guest_stars,
        'all_subjects': all_subjects,
        'air_time': air_time
    }
    return render(request, 'each_seminar.html', argument)


def getseminarform(request):
    return render(request, 'form_template.html')
