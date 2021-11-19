from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from ckeditor.fields import RichTextField
from user_perfil.models import Perfil_Usuario



class Categoria(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.title




class Postagem(models.Model):
    titulo = models.CharField(max_length=400)
    subtitulo = models.CharField(max_length=400,default='subtitulo')
    image_file = models.ImageField( null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    fonte_original = models.CharField(max_length=200,default='não informado', null=True, blank=True)
    user = models.ForeignKey(Perfil_Usuario, on_delete=models.CASCADE)
    content = RichTextField()
    categories = models.ManyToManyField(Categoria)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )



    class Meta:
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo


