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
