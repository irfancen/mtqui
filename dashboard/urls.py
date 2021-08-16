from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('enroll/<int:id_kompetisi>', enroll, name='enroll'),
    path('add/<int:id_kelompok>', add_anggota, name='add_anggota'),
    path('edit/participant/<int:id_peserta>', edit_peserta, name='edit_peserta'),
    path('edit/team/<int:id_kelompok>', edit_kelompok, name='edit_kelompok'),
    path('edit/member/<int:id_anggota>', edit_anggota, name='edit_anggota'),
    path('delete/participant/<int:id_peserta>', delete_peserta, name='delete_peserta'),
    path('delete/team/<int:id_kelompok>', delete_kelompok, name='delete_kelompok'),
    path('delete/member/<int:id_anggota>', delete_anggota, name='delete_anggota'),
    path('view/<int:id_kompetisi>', view_enrollments, name='view_enrollments'),
    path('view/team/<int:id_kelompok>', view_kelompok, name='view_kelompok'),
    path("debug/", debug, name="debug"),
]
