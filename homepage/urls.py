from django.urls import path
from .views import homepage, guidebook, grandopening,grandclosing

app_name = "homepage"

urlpatterns = [
    path('', homepage, name='homepage'),
    path('guidebook/', guidebook, name='guidebook'),
    path('GO/', grandopening, name='grandopening'),
    path('GC/', grandclosing, name='grandclosing')
]