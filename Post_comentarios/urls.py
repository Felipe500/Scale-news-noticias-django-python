from django.urls import path


from .views import *

urlpatterns = [
    path('post/<str:id>/post-comentado/', Enviar_Comentaro, name='enviar_comentario'),


]