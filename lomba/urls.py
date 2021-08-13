from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "lomba"

urlpatterns = [
    path('', views.lomba_list, name='lomba_list'),
    path('<str:alias>/', views.lomba_detail, name='lomba_detail')
]
