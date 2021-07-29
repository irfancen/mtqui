from django.utils import translation
from dashboard.forms import BaseEnrollmentFormSet, EnrollmentForm
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

    EnrollmentFormSet = formset_factory(EnrollmentForm, formset=BaseEnrollmentFormSet)

    if request.method == "POST":
        enrollment_formset = EnrollmentFormSet(request.POST)

        if enrollment_formset.is_valid():
            kompetisi = Kompetisi.objects.get(id=id_kompetisi)

            peserta_baru = []

            for enrollment_form in enrollment_formset:
                nama = enrollment_form.cleaned_data["nama"]
                npm = enrollment_form.cleaned_data["npm"]

                if nama and npm:
                    peserta_baru.append(Peserta(nama=nama, npm=npm, kompetisi=kompetisi))
            
            Peserta.objects.bulk_create(peserta_baru)

            return redirect(reverse("dashboard:home"))
        
        else:
            context["enrollment_forms"] = enrollment_formset
            return render(request, "dashboard/enroll.html", context)

    context["enrollment_forms"] = EnrollmentFormSet()
    return render(request, "dashboard/enroll.html", context)














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
