from dashboard.forms import *
from django.contrib.auth.models import User
from dashboard.models import Anggota, Kelompok, Kompetisi, Peserta
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.http.response import HttpResponse, HttpResponseRedirect
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
    tipe_kompetisi = str(kompetisi.tipe)

    if tipe_kompetisi == "Individu":
        enroll_individu(request, id_kompetisi)

    elif tipe_kompetisi == "Kelompok":
        enroll_kelompok(request, id_kompetisi)

    elif tipe_kompetisi == "DAQ":
        enroll_daq(request, id_kompetisi)


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

            return redirect(reverse("dashboard:home"))
        
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
    AnggotaFormSet = formset_factory(AnggotaForm, max_num=kompetisi.kapasitas_kelompok)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)
        anggota_formset = AnggotaFormSet(request.POST, request.FILES)

        if kelompok_form.is_valid() and anggota_formset.is_valid():
            nama_kelompok = kelompok_form.cleaned_data.get("nama")

            kelompok = Kelompok(nama=nama_kelompok, kompetisi=kompetisi)
            kelompok.save()

            anggota_list = []

            for anggota_form in anggota_formset:
                nama = anggota_form.cleaned_data.get("nama")
                fakultas = request.user.metadata.nama_fakultas
                jurusan = anggota_form.cleaned_data.get("jurusan")
                angkatan = anggota_form.cleaned_data.get("angkatan")
                no_hp = anggota_form.cleaned_data.get("no_hp")
                line_id = anggota_form.cleaned_data.get("line_id")
                foto_ktm = anggota_form.cleaned_data.get("foto_ktm")
                screenshot_siak = anggota_form.cleaned_data.get("screenshot_siak")

                anggota_list.append(Anggota(
                            nama=nama, 
                            fakultas=fakultas, 
                            jurusan=jurusan, 
                            angkatan=angkatan, 
                            no_hp=no_hp, 
                            line_id=line_id, 
                            foto_ktm=foto_ktm, 
                            screenshot_siak=screenshot_siak, 
                            kelompok=kelompok
                        ))

            Anggota.objects.bulk_create(anggota_list)

            return redirect(reverse("dashboard:home"))
    
        else:
            context["competition"] = kompetisi
            context["kelompok_form"] = kelompok_form
            context["anggota_formset"] = anggota_formset
            return render(request, "dashboard/enroll_kelompok.html", context)
    
    context["competition"] = kompetisi
    context["kelompok_form"] = KelompokForm()
    context["anggota_formset"] = AnggotaFormSet()
    return render(request, "dashboard/enroll_kelompok.html", context)


def enroll_daq(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)
    AnggotaDAQFormSet = formset_factory(AnggotaDAQForm, max_num=kompetisi.kapasitas_kelompok)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)
        anggota_daq_formset = AnggotaDAQFormSet(request.POST, request.FILES)

        if kelompok_form.is_valid() and anggota_daq_formset.is_valid():
            nama_kelompok = kelompok_form.cleaned_data.get("nama")

            kelompok = Kelompok(nama=nama_kelompok, kompetisi=kompetisi)
            kelompok.save()

            anggota_daq_list = []

            for anggota_daq_form in anggota_daq_formset:
                nama = anggota_daq_form.cleaned_data.get("nama")
                fakultas = request.user.metadata.nama_fakultas
                jurusan = anggota_daq_form.cleaned_data.get("jurusan")
                angkatan = anggota_daq_form.cleaned_data.get("angkatan")
                no_hp = anggota_daq_form.cleaned_data.get("no_hp")
                line_id = anggota_daq_form.cleaned_data.get("line_id")
                is_ketua = anggota_daq_form.cleaned_data.get("is_ketua")
                foto_ktm = anggota_daq_form.cleaned_data.get("foto_ktm")
                screenshot_siak = anggota_daq_form.cleaned_data.get("screenshot_siak")
                file_cv = anggota_daq_form.cleaned_data.get("file_cv")

                anggota_daq_list.append(Anggota(
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
                        ))
            
            Anggota.objects.bulk_create(anggota_daq_list)

            return redirect(reverse("dashboard:home"))

        else:
            context["competition"] = kompetisi
            context["kelompok_form"] = kelompok_form
            context["anggota_daq_formset"] = anggota_daq_formset
            return render(request, "dashboard/enroll_daq.html", context)
    
    context["competition"] = kompetisi
    context["kelompok_form"] = KelompokForm()
    context["anggota_daq_formset"] = AnggotaDAQFormSet()
    return render(request, "dashboard/enroll_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def add_anggota(request, id_kelompok):
    kelompok = Kelompok.objects.get(id=id_kelompok)
    tipe_kompetisi = str(kelompok.kompetisi.tipe)

    if tipe_kompetisi == "Kelompok":
        add_anggota_kelompok(request, id_kelompok)

    elif tipe_kompetisi == "DAQ":
        add_anggota_kelompok_daq(request, id_kelompok)


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

            return redirect(reverse("dashboard:home"))
        
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

            return redirect(reverse("dashboard:home"))
        
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
    tipe_kompetisi = str(kelompok.kompetisi.tipe)

    if tipe_kompetisi == "Kelompok":
        edit_kelompok_biasa(request, id_kelompok)

    elif tipe_kompetisi == "DAQ":
        edit_kelompok_daq(request, id_kelompok)


def edit_kelompok_biasa(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        kelompok_form = KelompokForm(request.POST)

        if kelompok_form.is_valid():
            nama_kelompok = kelompok_form.cleaned_data.get("nama")

            kelompok.nama = nama_kelompok
            kelompok.save()

            return redirect(reverse("dashboard:home"))
        
        else:
            context["kelompok"] = kelompok
            context["kelompok_form"] = kelompok_form
            return render(request, "dashboard/edit_kelompok_biasa.html", context)

    context["kelompok"] = kelompok
    context["kelompok_form"] = KelompokForm()
    return render(request, "dashboard/edit_kelompok_biasa.html", context)


def edit_kelompok_daq(request, id_kelompok):
    context = {}

    kelompok = Kelompok.objects.get(id=id_kelompok)

    if request.method == "POST":
        edit_kelompok_daq_form = EditKelompokDAQForm(request.POST)

        if edit_kelompok_daq_form.is_valid():
            nama_kelompok = edit_kelompok_daq_form.cleaned_data.get("nama")
            id_ketua_baru = edit_kelompok_daq_form.cleaned_data.get("ketua")

            kelompok.nama = nama_kelompok
            kelompok.save()

            for anggota_kelompok in Anggota.objects.filter(kelompok=kelompok):
                anggota_kelompok.is_ketua = False
                anggota_kelompok.save()
            
            ketua_baru = Anggota.objects.get(id=id_ketua_baru)
            ketua_baru.is_ketua = True
            ketua_baru.save()

            return redirect(reverse("dashboard:home"))

        else:
            context["kelompok"] = kelompok
            context["edit_kelompok_daq_form"] = edit_kelompok_daq_form
            return render(request, "dashboard/edit_kelompok_daq.html", context)
    
    context["kelompok"] = kelompok
    context["edit_kelompok_daq_form"] = EditKelompokDAQForm()
    return render(request, "dashboard/edit_kelompok_daq.html", context)


@login_required(redirect_field_name="dashboard:home")
def delete_kelompok(request, id_kelompok):
    Kelompok.objects.get(id=id_kelompok).delete()
    
    return redirect(reverse("dashboard:home"))




@login_required(redirect_field_name="dashboard:home")
def edit_enrollments(request, id_kompetisi):
    return HttpResponse("Hello")

@login_required(redirect_field_name="dashboard:home")
def view_enrollments(request, id_kompetisi):
    return HttpResponse("Hello")


























def debug(request):
    print("====================== START ======================")

    # print("=== USER ===")
    # for user in User.objects.all():
    #     if user.username == "admin":
    #         continue

    #     print(user.username)
    #     print(user.metadata.nama_fakultas)
    #     print(user.metadata.singkatan_fakultas)
    #     print(user.metadata.makara_image_code)
    #     print(user.kompetisi.all())
    #     print("-----")

    # print("=== KOMPETISI ===")
    # for kompetisi in Kompetisi.objects.all():
    #     print(kompetisi)
    #     print(kompetisi.get_enrollment_count())
    #     print("-----")

    # print("=== PESERTA ===")
    # for peserta in Peserta.objects.all():
    #     print(peserta)
    #     print(peserta.foto_ktm.url)
    #     print(peserta.screenshot_siak.url)
    #     print(peserta.file_cv.url)
    #     print("-----")

    print("======================  END  ======================")

    return HttpResponse("DEBUG")
