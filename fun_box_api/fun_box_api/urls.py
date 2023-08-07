from django.contrib import admin
from django.urls import path

from api.views import append_sites, get_sites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/append', append_sites),
    path('api/get_sites', get_sites),
]
