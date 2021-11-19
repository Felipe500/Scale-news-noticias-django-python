from django.shortcuts import redirect
from .models import Comentario
from django.contrib import messages
from libgravatar import Gravatar
from Post_noticias.models import Postagem


def Enviar_Comentaro(request,id):

    if request.method == 'POST':
        Pos = Postagem.objects.get(id=id)
        nome = request.POST['entrada_nome']
        email = request.POST['entrada_email']
        comentario = request.POST['entrada_comentario']
        imagem_perfil = Gravatar(email)
        print("url img: ",imagem_perfil.get_image())
        print("Comentario enviado com sucesso...")

        Comentario.objects.create(
            nome_user=nome,
            comentario= comentario,
            email = email,
            image_url=imagem_perfil.get_image(),
            postagem_id=Pos
            )
        messages.success(request, 'Comentario enviado')

    return redirect('ver_postagem',id=id)