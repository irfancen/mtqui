from django.urls import path
from .views import seminarlanding, getseminar, getseminarform
from django.conf.urls.static import static
from django.conf import settings

app_name = "seminar"

urlpatterns = [
    path('', seminarlanding, name='seminar_landing'),
    path('more/<str:id_seminar>/', getseminar, name='get_seminar'),
    path('enroll/', getseminarform, name='get_seminar_form')
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)