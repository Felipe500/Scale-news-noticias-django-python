from django.shortcuts import render,redirect
from .models import Postagem,Categoria
from Post_comentarios.models import Comentario
from django.contrib import messages
from libgravatar import Gravatar
from .models import Postagem
import datetime


def Postagens(request,id):

    categorias = Categoria.objects.all()
    Pos = Postagem.objects.get(id=id)
    Comentarios = Comentario.objects.filter(postagem_id=id)
    print("comentarios ",Comentarios)
    total_categorias = categorias.count()


    context = {
        "Pos": Pos,
        "categorias": categorias,
        "num_categories": total_categorias,
        "title": "Meus foruns",
        "Comentarios":Comentarios
    }
    return render(request,'postagem.html',context)


def save_form(request,id):

    if request.method == 'POST':
        Pos = Postagem.objects.get(id=id)
        nome = request.POST['entrada_nome']
        email = request.POST['entrada_email']
        comentario = request.POST['entrada_comentario']
        imagem_perfil = Gravatar(email)
        print("url img: ",imagem_perfil.get_image())

        Comentario.objects.create(
            nome_user=nome,
            comentario= comentario,
            email = email,
            image_url=imagem_perfil.get_image(),
            postagem_id=Pos
            )
        messages.success(request, 'Comentario enviado')

    return redirect('ver_postagem',id=id)