from dashboard.forms import *
from dashboard.models import Anggota, Kelompok, Kompetisi, Peserta
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
@login_required
def home(request):
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin/")

    context = {}

    context["metadata_fakultas"] = request.user.metadata
    context["competitions"] = request.user.kompetisi.all()

    return render(request, "dashboard/dashboard.html", context)


@login_required(redirect_field_name="dashboard:home")
def enroll(request, id_kompetisi):
    kompetisi = Kompetisi.objects.get(id=id_kompetisi)
    tipe_kompetisi = kompetisi.get_tipe()

    if tipe_kompetisi == "Individu":
        return enroll_individu(request, id_kompetisi)

    elif tipe_kompetisi == "Kelompok":
        return enroll_kelompok(request, id_kompetisi)

    elif tipe_kompetisi == "DAQ":
        return enroll_daq(request, id_kompetisi)


def enroll_individu(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)

    if request.method == "POST":
        peserta_form = PesertaForm(request.POST, request.FILES)

        if peserta_form.is_valid():
            nama = peserta_form.cleaned_data.get("nama")
            fakultas = request.user.metadata.nama_fakultas
            jurusan = peserta_form.cleaned_data.get("jurusan")
            angkatan = peserta_form.cleaned_data.get("angkatan")
            no_hp = peserta_form.cleaned_data.get("no_hp")
            line_id = peserta_form.cleaned_data.get("line_id")
            foto_ktm = peserta_form.cleaned_data.get("foto_ktm")
            screenshot_siak = peserta_form.cleaned_data.get("screenshot_siak")

            peserta = Peserta(
                        nama=nama, 
                        fakultas=fakultas, 
                        jurusan=jurusan, 
                        angkatan=angkatan, 
                        no_hp=no_hp, 
                        line_id=line_id, 
                        foto_ktm=foto_ktm, 
                        screenshot_siak=screenshot_siak, 
                        kompetisi=kompetisi
                    )
            peserta.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kompetisi.id}))

        else:
            context["competition"] = kompetisi
            context["peserta_form"] = peserta_form
            return render(request, "dashboard/enroll_individu.html", context)
    
    context["competition"] = kompetisi
    context["peserta_form"] = PesertaForm()
    return render(request, "dashboard/enroll_individu.html", context)


def enroll_kelompok(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)
        anggota_form = AnggotaForm(request.POST, request.FILES)

        if kelompok_form.is_valid() and anggota_form.is_valid():
            nama_kelompok = kelompok_form.cleaned_data.get("nama_kelompok")

            kelompok = Kelompok(nama=nama_kelompok, kompetisi=kompetisi)
            kelompok.save()

            nama = anggota_form.cleaned_data.get("nama")
            fakultas = request.user.metadata.nama_fakultas
            jurusan = anggota_form.cleaned_data.get("jurusan")
            angkatan = anggota_form.cleaned_data.get("angkatan")
            no_hp = anggota_form.cleaned_data.get("no_hp")
            line_id = anggota_form.cleaned_data.get("line_id")
            foto_ktm = anggota_form.cleaned_data.get("foto_ktm")
            screenshot_siak = anggota_form.cleaned_data.get("screenshot_siak")

            anggota = Anggota(
                        nama=nama, 
                        fakultas=fakultas, 
                        jurusan=jurusan, 
                        angkatan=angkatan, 
                        no_hp=no_hp, 
                        line_id=line_id, 
                        foto_ktm=foto_ktm, 
                        screenshot_siak=screenshot_siak, 
                        kelompok=kelompok
                    )
            anggota.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kompetisi.id}))
    
        else:
            context["competition"] = kompetisi
            context["kelompok_form"] = kelompok_form
            context["anggota_form"] = anggota_form
            return render(request, "dashboard/enroll_kelompok.html", context)
    
    context["competition"] = kompetisi
    context["kelompok_form"] = KelompokForm()
    context["anggota_form"] = AnggotaForm()
    return render(request, "dashboard/enroll_kelompok.html", context)


def enroll_daq(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)
        anggota_daq_form = AnggotaDAQForm(request.POST, request.FILES)

        if kelompok_form.is_valid() and anggota_daq_form.is_valid():
            nama_kelompok = kelompok_form.cleaned_data.get("nama_kelompok")

            kelompok = Kelompok(nama=nama_kelompok, kompetisi=kompetisi)
            kelompok.save()

            nama = anggota_daq_form.cleaned_data.get("nama")
            fakultas = request.user.metadata.nama_fakultas
            jurusan = anggota_daq_form.cleaned_data.get("jurusan")
            angkatan = anggota_daq_form.cleaned_data.get("angkatan")
            no_hp = anggota_daq_form.cleaned_data.get("no_hp")
            line_id = anggota_daq_form.cleaned_data.get("line_id")
            is_ketua = True
            foto_ktm = anggota_daq_form.cleaned_data.get("foto_ktm")
            screenshot_siak = anggota_daq_form.cleaned_data.get("screenshot_siak")
            file_cv = anggota_daq_form.cleaned_data.get("file_cv")

            anggota = Anggota(
                        nama=nama,
                        fakultas=fakultas,
                        jurusan=jurusan,
                        angkatan=angkatan,
                        no_hp=no_hp,
                        line_id=line_id,
                        is_ketua=is_ketua,
                        foto_ktm=foto_ktm,
                        screenshot_siak=screenshot_siak,
                        file_cv=file_cv,
                        kelompok=kelompok
                    )
            anggota.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kompetisi.id}))

        else:
            context["competition"] = kompetisi
            context["kelompok_form"] = kelompok_form
            context["anggota_daq_form"] = anggota_daq_form
            return render(request, "dashboard/enroll_daq.html", context)
    
    context["competition"] = kompetisi
    context["kelompok_form"] = KelompokForm()
    context["anggota_daq_form"] = AnggotaDAQForm()
    return render(request, "dashboard/enroll_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def add_anggota(request, id_kelompok):
    kelompok = Kelompok.objects.get(id=id_kelompok)
    tipe_kompetisi = kelompok.get_tipe()

    if tipe_kompetisi == "Kelompok":
        return add_anggota_kelompok(request, id_kelompok)

    elif tipe_kompetisi == "DAQ":
        return add_anggota_kelompok_daq(request, id_kelompok)


def add_anggota_kelompok(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        anggota_form = AnggotaForm(request.POST, request.FILES)

        if anggota_form.is_valid():
            nama = anggota_form.cleaned_data.get("nama")
            fakultas = request.user.metadata.nama_fakultas
            jurusan = anggota_form.cleaned_data.get("jurusan")
            angkatan = anggota_form.cleaned_data.get("angkatan")
            no_hp = anggota_form.cleaned_data.get("no_hp")
            line_id = anggota_form.cleaned_data.get("line_id")
            foto_ktm = anggota_form.cleaned_data.get("foto_ktm")
            screenshot_siak = anggota_form.cleaned_data.get("screenshot_siak")

            anggota = Anggota(
                        nama=nama, 
                        fakultas=fakultas, 
                        jurusan=jurusan, 
                        angkatan=angkatan, 
                        no_hp=no_hp, 
                        line_id=line_id, 
                        foto_ktm=foto_ktm, 
                        screenshot_siak=screenshot_siak, 
                        kelompok=kelompok
                    )
            anggota.save()

            return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': kelompok.id}))
        
        else:
            context["kelompok"] = kelompok
            context["anggota_form"] = anggota_form
            return render(request, "dashboard/add_anggota_kelompok.html", context)

    context["kelompok"] = kelompok
    context["anggota_form"] = AnggotaForm()
    return render(request, "dashboard/add_anggota_kelompok.html", context)


def add_anggota_kelompok_daq(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        anggota_daq_form = AnggotaDAQForm(request.POST, request.FILES)

        if anggota_daq_form.is_valid():
            nama = anggota_daq_form.cleaned_data.get("nama")
            fakultas = request.user.metadata.nama_fakultas
            jurusan = anggota_daq_form.cleaned_data.get("jurusan")
            angkatan = anggota_daq_form.cleaned_data.get("angkatan")
            no_hp = anggota_daq_form.cleaned_data.get("no_hp")
            line_id = anggota_daq_form.cleaned_data.get("line_id")
            is_ketua = False
            foto_ktm = anggota_daq_form.cleaned_data.get("foto_ktm")
            screenshot_siak = anggota_daq_form.cleaned_data.get("screenshot_siak")
            file_cv = anggota_daq_form.cleaned_data.get("file_cv")

            anggota = Anggota(
                        nama=nama,
                        fakultas=fakultas,
                        jurusan=jurusan,
                        angkatan=angkatan,
                        no_hp=no_hp,
                        line_id=line_id,
                        is_ketua=is_ketua,
                        foto_ktm=foto_ktm,
                        screenshot_siak=screenshot_siak,
                        file_cv=file_cv,
                        kelompok=kelompok
                    )
            anggota.save()

            return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': kelompok.id}))
        
        else:
            context["kelompok"] = kelompok
            context["anggota_daq_form"] = anggota_daq_form
            return render(request, "dashboard/add_anggota_kelompok_daq.html", context)

    context["kelompok"] = kelompok
    context["anggota_daq_form"] = AnggotaDAQForm()
    return render(request, "dashboard/add_anggota_kelompok_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def edit_kelompok(request, id_kelompok):
    kelompok = Kelompok.objects.get(id=id_kelompok)
    tipe_kompetisi = kelompok.get_tipe()

    if tipe_kompetisi == "Kelompok":
        return edit_kelompok_biasa(request, id_kelompok)

    elif tipe_kompetisi == "DAQ":
        return edit_kelompok_daq(request, id_kelompok)


def edit_kelompok_biasa(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)

        if kelompok_form.is_valid():
            kelompok.nama = kelompok_form.cleaned_data.get("nama_kelompok")
            kelompok.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kelompok.kompetisi.id}))
        
        else:
            context["kelompok"] = kelompok
            context["kelompok_form"] = kelompok_form
            return render(request, "dashboard/edit_kelompok_biasa.html", context)

    initial_data = {
        "nama_kelompok" : kelompok.nama,
    }

    context["kelompok"] = kelompok
    context["kelompok_form"] = KelompokForm(initial=initial_data)
    return render(request, "dashboard/edit_kelompok_biasa.html", context)


def edit_kelompok_daq(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        edit_kelompok_daq_form = EditKelompokDAQForm(request.POST, ketua_choices=kelompok.get_ketua_choices())

        if edit_kelompok_daq_form.is_valid():
            kelompok.nama = edit_kelompok_daq_form.cleaned_data.get("nama_kelompok")
            kelompok.save()

            for anggota_kelompok in Anggota.objects.filter(kelompok=kelompok):
                anggota_kelompok.is_ketua = False
                anggota_kelompok.save()

            id_ketua_baru = edit_kelompok_daq_form.cleaned_data.get("ketua")
            ketua_baru = Anggota.objects.get(id=id_ketua_baru)
            ketua_baru.is_ketua = True
            ketua_baru.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kelompok.kompetisi.id}))

        else:
            context["kelompok"] = kelompok
            context["edit_kelompok_daq_form"] = edit_kelompok_daq_form
            return render(request, "dashboard/edit_kelompok_daq.html", context)
    
    initial_data = {
        "nama_kelompok" : kelompok.nama,
        "ketua" : kelompok.get_ketua().id
    }

    context["kelompok"] = kelompok
    context["edit_kelompok_daq_form"] = EditKelompokDAQForm(initial=initial_data, ketua_choices=kelompok.get_ketua_choices())
    return render(request, "dashboard/edit_kelompok_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def delete_kelompok(request, id_kelompok):
    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        kompetisi = kelompok.kompetisi

        kelompok.delete()

        if kompetisi.get_enrollment_count() == 0:
            return redirect(reverse("dashboard:home"))

        return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kompetisi.id}))


@login_required(redirect_field_name="dashboard:home")
def edit_peserta(request, id_peserta):
    context = {}

    peserta = Peserta.objects.get(id=id_peserta)

    if request.method == "POST":
        peserta_form = PesertaForm(request.POST, request.FILES, edit_form=True)

        if peserta_form.is_valid():
            peserta.nama = peserta_form.cleaned_data.get("nama")
            peserta.fakultas = request.user.metadata.nama_fakultas
            peserta.jurusan = peserta_form.cleaned_data.get("jurusan")
            peserta.angkatan = peserta_form.cleaned_data.get("angkatan")
            peserta.no_hp = peserta_form.cleaned_data.get("no_hp")
            peserta.line_id = peserta_form.cleaned_data.get("line_id")
            peserta.foto_ktm = peserta_form.cleaned_data.get("foto_ktm") or peserta.foto_ktm
            peserta.screenshot_siak = peserta_form.cleaned_data.get("screenshot_siak") or peserta.screenshot_siak
            peserta.save()

            return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': peserta.kompetisi.id}))
        
        else:
            context["peserta"] = peserta
            context["peserta_form"] = peserta_form
            return render(request, "dashboard/edit_peserta.html", context)
    
    initial_data = {
        "nama" : peserta.nama,
        "jurusan" : peserta.jurusan,
        "angkatan" : peserta.angkatan,
        "no_hp" : peserta.no_hp,
        "line_id" : peserta.line_id,
        "foto_ktm" : peserta.foto_ktm,
        "screenshot_siak" : peserta.screenshot_siak
    }

    context["peserta"] = peserta
    context["peserta_form"] = PesertaForm(initial=initial_data, edit_form=True)
    return render(request, "dashboard/edit_peserta.html", context)


@login_required(redirect_field_name="dashboard:home")
def edit_anggota(request, id_anggota):
    anggota = Anggota.objects.get(id=id_anggota)
    tipe_kompetisi = anggota.get_tipe()

    if tipe_kompetisi == "Kelompok":
        return edit_anggota_biasa(request, id_anggota)

    elif tipe_kompetisi == "DAQ":
        return edit_anggota_daq(request, id_anggota)


def edit_anggota_biasa(request, id_anggota):
    context = {}

    anggota = Anggota.objects.get(id=id_anggota)

    if request.method == "POST":
        anggota_form = AnggotaForm(request.POST, request.FILES, edit_form=True)

        if anggota_form.is_valid():
            anggota.nama = anggota_form.cleaned_data.get("nama")
            anggota.fakultas = request.user.metadata.nama_fakultas
            anggota.jurusan = anggota_form.cleaned_data.get("jurusan")
            anggota.angkatan = anggota_form.cleaned_data.get("angkatan")
            anggota.no_hp = anggota_form.cleaned_data.get("no_hp")
            anggota.line_id = anggota_form.cleaned_data.get("line_id")
            anggota.foto_ktm = anggota_form.cleaned_data.get("foto_ktm") or anggota.foto_ktm
            anggota.screenshot_siak = anggota_form.cleaned_data.get("screenshot_siak") or anggota.screenshot_siak
            anggota.save()

            return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': anggota.kelompok.id}))
        
        else:
            context["anggota"] = anggota
            context["anggota_form"] = anggota_form
            return render(request, "dashboard/edit_anggota_biasa.html", context)

    initial_data = {
        "nama" : anggota.nama,
        "jurusan" : anggota.jurusan,
        "angkatan" : anggota.angkatan,
        "no_hp" : anggota.no_hp,
        "line_id" : anggota.line_id,
        "foto_ktm" : anggota.foto_ktm,
        "screenshot_siak" : anggota.screenshot_siak
    }

    context["anggota"] = anggota
    context["anggota_form"] = AnggotaForm(initial=initial_data, edit_form=True)
    return render(request, "dashboard/edit_anggota_biasa.html", context)


def edit_anggota_daq(request, id_anggota):
    context = {}

    anggota = Anggota.objects.get(id=id_anggota)

    if request.method == "POST":
        anggota_daq_form = AnggotaDAQForm(request.POST, request.FILES, edit_form=True)

        if anggota_daq_form.is_valid():
            anggota.nama = anggota_daq_form.cleaned_data.get("nama")
            anggota.fakultas = request.user.metadata.nama_fakultas
            anggota.jurusan = anggota_daq_form.cleaned_data.get("jurusan")
            anggota.angkatan = anggota_daq_form.cleaned_data.get("angkatan")
            anggota.no_hp = anggota_daq_form.cleaned_data.get("no_hp")
            anggota.line_id = anggota_daq_form.cleaned_data.get("line_id")
            anggota.foto_ktm = anggota_daq_form.cleaned_data.get("foto_ktm") or anggota.foto_ktm
            anggota.screenshot_siak = anggota_daq_form.cleaned_data.get("screenshot_siak") or anggota.screenshot_siak
            anggota.file_cv = anggota_daq_form.cleaned_data.get("file_cv") or anggota.file_cv
            anggota.save()

            return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': anggota.kelompok.id}))
        
        else:
            context["anggota"] = anggota
            context["anggota_daq_form"] = anggota_daq_form
            return render(request, "dashboard/edit_anggota_daq.html", context)

    initial_data = {
        "nama" : anggota.nama,
        "jurusan" : anggota.jurusan,
        "angkatan" : anggota.angkatan,
        "no_hp" : anggota.no_hp,
        "line_id" : anggota.line_id,
        "foto_ktm" : anggota.foto_ktm,
        "screenshot_siak" : anggota.screenshot_siak,
        "file_cv" : anggota.file_cv
    }

    context["anggota"] = anggota
    context["anggota_daq_form"] = AnggotaDAQForm(initial=initial_data, edit_form=True)
    return render(request, "dashboard/edit_anggota_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def delete_peserta(request, id_peserta):
    peserta = Peserta.objects.get(id=id_peserta)

    if request.method == "POST":
        kompetisi = peserta.kompetisi

        peserta.delete()

        if kompetisi.get_enrollment_count() == 0:
            return redirect(reverse("dashboard:home"))

        return redirect(reverse("dashboard:view_enrollments", kwargs={'id_kompetisi': kompetisi.id}))


@login_required(redirect_field_name="dashboard:home")
def delete_anggota(request, id_anggota):
    anggota = Anggota.objects.get(id=id_anggota)
    tipe_kompetisi = anggota.get_tipe()

    if tipe_kompetisi == "Kelompok":
        return delete_anggota_biasa(request, id_anggota)

    elif tipe_kompetisi == "DAQ":
        return delete_anggota_daq(request, id_anggota)


def delete_anggota_biasa(request, id_anggota):
    anggota = Anggota.objects.get(id=id_anggota)

    if request.method == "POST":
        kelompok = anggota.kelompok

        anggota.delete()

        return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': kelompok.id}))


def delete_anggota_daq(request, id_anggota):
    anggota = Anggota.objects.get(id=id_anggota)

    if request.method == "POST":
        is_ketua = anggota.is_ketua
        kelompok = anggota.kelompok

        anggota.delete()

        if is_ketua:
            new_ketua = Anggota.objects.filter(kelompok=kelompok).first()
            new_ketua.is_ketua = True
            new_ketua.save()
        
        return redirect(reverse("dashboard:view_kelompok", kwargs={'id_kelompok': kelompok.id}))


@login_required(redirect_field_name="dashboard:home")
def view_enrollments(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)
    tipe_kompetisi = kompetisi.get_tipe()

    context["competition"] = kompetisi

    if tipe_kompetisi == "Individu":
        return render(request, "dashboard/view_kompetisi_individu.html", context)

    elif tipe_kompetisi == "Kelompok":
        return render(request, "dashboard/view_kompetisi_kelompok.html", context)

    elif tipe_kompetisi == "DAQ":
        return render(request, "dashboard/view_kompetisi_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def view_kelompok(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)
    tipe_kompetisi = kelompok.get_tipe()

    context["kelompok"] = kelompok

    if tipe_kompetisi == "Kelompok":
        return render(request, "dashboard/view_kelompok.html", context)

    elif tipe_kompetisi == "DAQ":
        return render(request, "dashboard/view_kelompok_daq.html", context)
