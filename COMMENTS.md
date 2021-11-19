

# SOBRE O PROJETO
15/11/21 19:40:
<br>
Para este projeto eu decide montar a seguinte estrutura.

Front-end: HTML, CSS E bootstrap v4.6.1. <br>
Back-end: Python com o framework Django.

Estrutura:<br>
--> Django projeto: Portal_Scale_News
    <br>
        -->Apps:
- Home
- Post_noticias,
- Post_Comentarios 
- User_perfil(Ainda falta implementar).

<br><br>Estrutura dos templates base da aplicação - Layout tema: <br>
- Portal_Scale_News/templates/base.html - Inclui navbar.htm e footer.html. Pagina principal para carregamento de recursos vindo do bootstrap.<br>
- Portal_Scale_News/templates/navbar.html - Contém link para rota inicial da aplicação e o link para todas categorias de noticias cadastradas no banco de dados.<br>
- Portal_Scale_News/templates/footer.html - Rodapé da pagina - Contém informações de contato entre outras informações.<br>


16/11/21 07:39:
<br>
Criando teste otimizados e automatizando com pycharm para executar comandos no manage.py.<br>
comandos: runserver, migrate, makemigrations, createsuperuser(criar usuario admin).<br>

Buscando modelos de templates para facilitar o desenvolvimento do front-end:<br>
 - Layout: Bootstrap 4.6.1 link documentação - https://getbootstrap.com/docs/4.6/getting-started/introduction/ <br>
 - Icones: link - https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css <br>
 - Sesão de comentarios: link - https://bbbootstrap.com/snippets/bootstrap-nested-comment-section-reply-72244546 <br>
 - Resposta de envio de comentario: link - https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_ref_js_alert&stacked=h <br>
 
Criando postagem para noticias na aplicação web.<br>
 
 - Inserindo postagens de noticias na tabela 'Postagem' do banco de dados no django-admin.
 - Implementando layout que servirá de tema para aplicação( base.html, navbar.html e footer.html).
 - Implementando layout do envio e listagem de comentarios.
 - Exibindo postagens na pagina principal.



17/11/21 09:12 ATÉ 18/11/21 16:31:<br>

Estudando API do Gravatar no link https://br.gravatar.com/site/implement/ <br>
Baixando e instalando a lib gravatar com pip do python  <br>  comando: pip install libgravatar. 
<br> link - https://pypi.org/project/libgravatar/  <br><br>
Back-end do envio de comentarios:
 - Recebendo dados do front-end pelo formulario do html.
 - Com o email recebido pelo formulario o back-end irá buscar a imagem do perfil do Gravatar. Com lib libgravatar. Se não encontrar uma imagem do perfil do gravatar pelo email fornecido a API retornará uma url da imagem padrão. 
 - Apos gravar os dados na tabela 'Comentario', irá caregar uma mensagem de sucesso ao enviar

# O QUE AINDA SERÁ IMPLEMENTADO:

- Criar cadastro de usuários para realizar postagens ou comentar postagens
- Criar tabela para Resposta_comentarios para que seja possivel responder comentarios
- Desenvolver um layout mais estilizado
- Criar um contador para visualizações nas postagens
- Monitorar comentarios maliciosos ou seja com ofensas e palavrões -  p@#$%
