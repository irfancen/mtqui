from django.urls import path
from .views import homepage, guidebook

app_name = "homepage"

urlpatterns = [
    path('', homepage, name='homepage'),
    path('guidebook/', guidebook, name='guidebook')
]