from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('post/<str:id>/', Postagens, name='ver_postagem'),
    path('comentario-enviado-com-sucesso/<str:id>/', save_form, name='up_comentario'),
    path('', include('Post_comentarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)