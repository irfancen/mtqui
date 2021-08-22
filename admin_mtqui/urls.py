from django.urls import path
from admin_mtqui.views import *

app_name = 'admin_mtqui'

urlpatterns = [
    path('create/kompetisi', create_kompetisi, name='create_kompetisi'),
]
