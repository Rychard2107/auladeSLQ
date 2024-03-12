from django.urls import path, re_path
from .api import viewsets

urlpatterns = [
    re_path('logar', viewsets.logar),
    re_path('registrar', viewsets.registrar),
    re_path('testar', viewsets.testar),
]
