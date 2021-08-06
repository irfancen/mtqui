from django.urls import path
from . import views

app_name = "lomba"

urlpatterns = [
    path('', views.lomba_list, name='lomba_list'),
    path('<str:nama_lomba>/', views.lomba_detail, name='lomba_detail')
]
