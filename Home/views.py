
from django.shortcuts import render
from Post_noticias.models import Postagem,Categoria

def Home(request):
    #postagens = Postagem.objects.all()
    categorias = Categoria.objects.all()
    meus_post = Postagem.objects.prefetch_related('categories').all()

   # num_posts = Postagem.objects.all().count()

   # total_categorias = categorias.count()

    context = {
        "postagens": meus_post,
        "categorias": categorias,
       # "num_posts": num_posts,
        #"num_categories": total_categorias,
        "title": "Meus foruns",

    }
    return render(request, 'Home.html', context)

def Filtro_Categoria(request,id):
    #postagens = Postagem.objects.all()
    #postagens = Postagem.objects.get(id=id)
    #print("id--",id)
    result = Postagem.objects.filter(categories=id)
    postagens = Postagem.objects.filter(categories=id)
    categorias = Categoria.objects.all()


    #num_posts = Postagem.objects.all().count()

    #total_categorias = categorias.count()

    context = {
        "postagens": postagens,
        "categorias": categorias,
       # "num_posts": num_posts,
        #"num_categories": total_categorias,
        "title": "Meus foruns",

    }
    return render(request, 'Home.html', context)