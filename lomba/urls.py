from django.urls import path
from . import views

app_name = "lomba"

urlpatterns = [
    path('', views.lombaPage, name='lombaPage')
]
