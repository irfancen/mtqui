from django.urls import path
from . import views

app_name = "lomba"

urlpatterns = [
    path('', views.lomba_list, name='lomba_list'),
    path('<str:alias>/', views.lomba_detail, name='lomba_detail')
]
