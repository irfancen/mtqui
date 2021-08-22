"""mtqui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('gallery/', include('gallery.urls')),
    path('auth/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('seminar/', include('seminar.urls')),
    path('lomba/', include('lomba.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler400 = "homepage.views.bad_request_view"
handler403 = "homepage.views.permission_denied_view"
handler404 = "homepage.views.page_not_found_view"
handler500 = "homepage.views.server_error_view"
