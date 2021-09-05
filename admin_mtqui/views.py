from django.contrib.auth.models import User
from admin_mtqui.forms import KompetisiForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from dashboard.models import Kompetisi, TipeKompetisi

# Create your views here.
@login_required
def create_kompetisi(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    context = {}

    if request.method == "POST":
        kompetisi_form = KompetisiForm(request.POST, tipe_choices=generate_tipe_choices())

        if kompetisi_form.is_valid():
            judul = kompetisi_form.cleaned_data.get("judul")
            kuota = kompetisi_form.cleaned_data.get("kuota")
            tanggal_pendaftaran = kompetisi_form.cleaned_data.get("tanggal_pendaftaran")
            deadline_pendaftaran = kompetisi_form.cleaned_data.get("deadline_pendaftaran")
            tipe = TipeKompetisi.objects.get(id=kompetisi_form.cleaned_data.get("tipe"))
            kapasitas_kelompok = kompetisi_form.cleaned_data.get("kapasitas_kelompok")

            for user in User.objects.all():
                if user.is_superuser:
                    continue

                kompetisi = Kompetisi(judul=judul, kuota=kuota, tanggal_pendaftaran=tanggal_pendaftaran, deadline_pendaftaran=deadline_pendaftaran, tipe=tipe, kapasitas_kelompok=kapasitas_kelompok, fakultas=user)
                kompetisi.save()

            return HttpResponse("DONE")

        else:
            context["kompetisi_form"] = kompetisi_form
            return render(request, "admin_mtqui/create_kompetisi.html", context)

    context["kompetisi_form"] = KompetisiForm(tipe_choices=generate_tipe_choices())
    return render(request, "admin_mtqui/create_kompetisi.html", context)

def generate_tipe_choices():
    return ( (tipe.id, str(tipe)) for tipe in TipeKompetisi.objects.all() )
