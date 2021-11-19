
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Post_noticias.urls')),
    path('', include('Post_comentarios.urls')),

    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
]

