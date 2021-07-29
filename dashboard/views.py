from django.contrib.auth.models import User
from dashboard.models import Kompetisi, Peserta
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
@login_required
def home(request):
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin/")

    context = {}

    context["metadata_fakultas"] = request.user.metadata
    context["competitions"] = request.user.kompetisi.all()

    return render(request, "dashboard/dashboard.html", context)

def debug(request):
    print("====================== START ======================")

    print("=== USER ===")
    for user in User.objects.all():
        if user.username == "admin":
            continue

        print(user.username)
        print(user.metadata.nama_fakultas)
        print(user.metadata.singkatan_fakultas)
        print(user.metadata.makara_image_code)
        print(user.kompetisi.all())
        print("-----")

    print("=== KOMPETISI ===")
    for kompetisi in Kompetisi.objects.all():
        print(kompetisi)
        print(kompetisi.peserta.all())
        print("-----")

    print("=== PESERTA ===")
    for peserta in Peserta.objects.all():
        print(peserta)
        print(peserta.kompetisi)
        print("-----")

    print("======================  END  ======================")

    return HttpResponse("DEBUG")
