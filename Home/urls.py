from django.urls import path, include

from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('filtro/<str:id>/', Filtro_Categoria, name='Filtro_Categoria'),
]