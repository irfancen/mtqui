from django.shortcuts import render
from django.http import HttpResponse
from .models import Seminar
from django.utils import timezone


# Create your views here.

def seminarlanding(request):

    semua_seminar = Seminar.objects.all()
    for seminar in semua_seminar:

        # Find latest event from a list of events from a seminar
        # latest_event = EventDate.objects.filter(nama_seminar=seminar.id).last()

        if seminar.d_day < timezone.localtime():
            seminar.is_past = True


    argument = {
        'seminar_list': semua_seminar
    }

    return render(request, 'seminar_landing.html', argument)


def getseminar(request, id_seminar):
    seminar = Seminar.objects.get(id = id_seminar)
    guest_stars = seminar.guest_stars.all()
    all_subjects = [x for x in seminar.subjects.split(';') if x]

    if seminar.d_day < timezone.localtime():
        seminar.is_past = True

    dt = seminar.d_day - timezone.localtime()
    air_time = str(dt.days) + "days" + " " + str(dt.seconds//3600) + "hrs" + " " + str((dt.seconds//60)%60) + "mins"

    argument = {
        'seminar': seminar,
        'guest_stars': guest_stars,
        'all_subjects': all_subjects,
        'air_time': air_time
    }
    return render(request, 'each_seminar.html', argument)

def getseminarform(request):
    return render(request, 'form_template.html')

