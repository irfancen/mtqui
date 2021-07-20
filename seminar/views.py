from django.shortcuts import render
from django.http import HttpResponse
from .models import Seminar, EventDate
from django.utils import timezone


# Create your views here.

def seminarlanding(request):

    semua_seminar = Seminar.objects.all()
    for seminar in semua_seminar:

        # Find latest event from a list of events from a seminar
        latest_event = EventDate.objects.filter(nama_seminar=seminar.id).last()

        if latest_event.date < timezone.localdate():
            seminar.is_past = True


    argument = {
        'seminar_list': semua_seminar
    }

    return render(request, 'seminar_landing.html', argument)


def getseminar(request, id_seminar):
    seminar = Seminar.objects.get(id = id_seminar)
    guest_stars = seminar.guest_stars.all()
    all_timeline = EventDate.objects.filter(nama_seminar=id_seminar)
    all_received = [x for x in seminar.received.split(';') if x]
    all_reqs = [x for x in seminar.requirement.split(';') if x]
    pendaftaran_date = EventDate.objects.filter(nama_seminar=id_seminar, nama_kegiatan='Pendaftaran').first()

    latest_event = EventDate.objects.filter(nama_seminar=seminar.id).last()
    if latest_event.date < timezone.localdate():
        seminar.is_past = True

    argument = {
        'seminar': seminar,
        'guest_stars': guest_stars,
        'all_timeline': all_timeline,
        'all_received': all_received,
        'all_reqs': all_reqs,
        'pendaftaran_date': pendaftaran_date
    }
    return render(request, 'each_seminar.html', argument)

