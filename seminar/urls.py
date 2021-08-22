from django.urls import path
from .views import seminarlanding, getseminar, getseminarform

app_name = "seminar"

urlpatterns = [
    path('', seminarlanding, name='seminar_landing'),
    path('more/<str:id_seminar>/', getseminar, name='get_seminar'),
    path('enroll/', getseminarform, name='get_seminar_form'),
]
