from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField


User = get_user_model()
class Perfil_Usuario(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=40, blank=True)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True, null=True)
    biografia = RichTextField(blank=True)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True,
                                    blank=True)


    def __str__(self):
        return self.nome_completo

