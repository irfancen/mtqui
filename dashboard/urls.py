from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('enroll/<int:id_kompetisi>', enroll, name='enroll'),
    path("debug/", debug, name="debug"),
]
