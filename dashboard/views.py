from dashboard.forms import BaseEnrollmentFormSet, EnrollmentForm, EnrollmentListForm
from django.contrib.auth.models import User
from dashboard.models import Kompetisi, Peserta
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
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)

    EnrollmentFormSet = formset_factory(EnrollmentForm, formset=BaseEnrollmentFormSet, max_num=kompetisi.kuota)

    if request.method == "POST":
        enrollment_formset = EnrollmentFormSet(request.POST)

        if enrollment_formset.is_valid():
            peserta_baru = []

            for enrollment_form in enrollment_formset:
                nama = enrollment_form.cleaned_data.get("nama")
                fakultas = request.user.metadata.nama_fakultas
                jurusan = enrollment_form.cleaned_data.get("jurusan")
                angkatan = enrollment_form.cleaned_data.get("angkatan")
                no_hp = enrollment_form.cleaned_data.get("no_hp")
                line_id = enrollment_form.cleaned_data.get("line_id")
                is_ketua = enrollment_form.cleaned_data.get("is_ketua")

                if (nama and fakultas and jurusan and angkatan and no_hp and line_id):
                    peserta_baru.append(Peserta(
                                            nama=nama, 
                                            fakultas=fakultas, 
                                            jurusan=jurusan, 
                                            angkatan=angkatan, 
                                            no_hp=no_hp, 
                                            line_id=line_id, 
                                            is_ketua=is_ketua, 
                                            kompetisi=kompetisi))
            
            Peserta.objects.bulk_create(peserta_baru)

            return redirect(reverse("dashboard:home"))
        
        else:
            context["enrollment_forms"] = enrollment_formset
            context["competition"] = kompetisi
            return render(request, "dashboard/enroll.html", context)

    context["enrollment_forms"] = EnrollmentFormSet()
    context["competition"] = kompetisi
    return render(request, "dashboard/enroll.html", context)

@login_required(redirect_field_name="dashboard:home")
def edit_enrollments(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)

    EnrollmentFormSet = formset_factory(EnrollmentForm, formset=BaseEnrollmentFormSet, max_num=kompetisi.kuota, extra=0)

    if request.method == "POST":
        enrollment_formset = EnrollmentFormSet(request.POST)

        if enrollment_formset.is_valid():
            peserta_baru = []

            for enrollment_form in enrollment_formset:
                nama = enrollment_form.cleaned_data.get("nama")
                fakultas = request.user.metadata.nama_fakultas
                jurusan = enrollment_form.cleaned_data.get("jurusan")
                angkatan = enrollment_form.cleaned_data.get("angkatan")
                no_hp = enrollment_form.cleaned_data.get("no_hp")
                line_id = enrollment_form.cleaned_data.get("line_id")
                is_ketua = enrollment_form.cleaned_data.get("is_ketua")

                if (nama and fakultas and jurusan and angkatan and no_hp and line_id):
                    peserta_baru.append(Peserta(
                                            nama=nama, 
                                            fakultas=fakultas, 
                                            jurusan=jurusan, 
                                            angkatan=angkatan, 
                                            no_hp=no_hp, 
                                            line_id=line_id, 
                                            is_ketua=is_ketua, 
                                            kompetisi=kompetisi))
            
            Peserta.objects.filter(kompetisi=kompetisi).delete()
            Peserta.objects.bulk_create(peserta_baru)

            return redirect(reverse("dashboard:home"))
        
        else:
            context["enrollment_forms"] = enrollment_formset
            context["competition"] = kompetisi
            return render(request, "dashboard/edit_enrollments.html", context)

    current_peserta = Peserta.objects.filter(kompetisi=kompetisi)

    initial_data = [{"nama": peserta.nama,
                    "jurusan": peserta.jurusan,
                    "angkatan": peserta.angkatan,
                    "no_hp": peserta.no_hp,
                    "line_id": peserta.line_id,
                    "is_ketua": peserta.is_ketua} 
                    for peserta in current_peserta]

    context["enrollment_forms"] = EnrollmentFormSet(initial=initial_data)
    context["competition"] = kompetisi
    return render(request, "dashboard/edit_enrollments.html", context)

@login_required(redirect_field_name="dashboard:home")
def view_enrollments(request, id_kompetisi):
    context = {}

    kompetisi = Kompetisi.objects.get(id=id_kompetisi)
    EnrollmentListFormSet = formset_factory(EnrollmentListForm, formset=BaseEnrollmentFormSet, max_num=kompetisi.kuota, extra=0)
    current_peserta = Peserta.objects.filter(kompetisi=kompetisi)

    initial_data = [{"nama": peserta.nama,
                    "fakultas": peserta.fakultas,
                    "jurusan": peserta.jurusan,
                    "angkatan": peserta.angkatan,
                    "no_hp": peserta.no_hp,
                    "line_id": peserta.line_id,
                    "is_ketua": peserta.is_ketua} 
                    for peserta in current_peserta]

    context["enrollments"] = EnrollmentListFormSet(initial=initial_data)
    context["competition"] = kompetisi
    return render(request, "dashboard/view_enrollments.html", context)








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
