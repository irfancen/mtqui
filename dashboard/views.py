from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("authentication:login"))

    if request.user.is_superuser:
        return HttpResponseRedirect("/admin/")

    context = {}

    context["metadata_fakultas"] = request.user.metadata
    context["competitions"] = [1,2,3,]

    return render(request, "dashboard/dashboard.html", context)
