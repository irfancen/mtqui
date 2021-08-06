from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('enroll/<int:id_kompetisi>', enroll, name='enroll'),
    path('edit/<int:id_kompetisi>', edit_enrollments, name='edit'),
    path('view/<int:id_kompetisi>', view_enrollments, name='view'),
    path("debug/", debug, name="debug"),
]
