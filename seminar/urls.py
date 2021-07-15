from django.urls import path
from .views import seminarlanding

app_name = "seminar"

urlpatterns = [
    path('', seminarlanding, name='seminar_landing')
]