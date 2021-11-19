from urllib import request
from django.db import models
from ckeditor.fields import RichTextField
from Post_noticias.models import Postagem
from django.core.files import File
import os


class Comentario(models.Model):
    nome_user = models.CharField(max_length=210, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    postagem_id = models.ForeignKey(Postagem, on_delete=models.CASCADE,null=True, blank=True)
    comentario  = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=210, null=True, blank=True)
    image_file = models.ImageField( null=True, blank=True)
    image_url = models.URLField( null=True, blank=True)


    class Meta:
        verbose_name_plural = "Comentarios"

    def get_remote_image(self):
        if self.image_url and not self.image_file:
            result = request.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
            )
            self.save()

    def __str__(self):
        return self.comentario[:100]
