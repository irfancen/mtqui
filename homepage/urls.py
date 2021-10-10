from django.urls import path
from .views import homepage, guidebook, grandopening,grandclosing, grandopeningform, closingform

app_name = "homepage"

urlpatterns = [
    path('', homepage, name='homepage'),
    path('guidebook/', guidebook, name='guidebook'),
    path('GO/', grandopening, name='grandopening'),
    path('CC/', grandclosing, name='grandclosing'),
    path('GO/enroll/', grandopeningform, name='grandopeningform'),
    path('CC/enroll/', closingform, name='closingform')
]