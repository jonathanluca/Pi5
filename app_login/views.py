from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Usuario

def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado. Tente outro.')
            return render(request, 'usuarios/login.html')

        # Cria o novo usuário
        novo_usuario = Usuario.objects.create_user(email=email, nome=nome, senha=senha)
        return redirect('login_usuario')  # Nome da rota para a tela de login

    return render(request, 'usuarios/cadastro.html')

def login_usuario(request):
    return render(request, 'usuarios/login_existente.html')

def autenticar_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('listagem_usuarios')  # Redireciona após login bem-sucedido
        else:
            return render(request, 'usuarios/login_existente.html', {
                'error': 'E-mail ou senha inválidos!'
            })

def usuarios(request):
    if request.method == 'POST':
        # Cria um novo usuário apenas se os dados forem enviados via POST
        novo_usuario = Usuario()
        novo_usuario.id_usuario = request.POST.get('id_usuario')
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.senha = request.POST.get('senha')
        
        # Valida se os campos obrigatórios foram preenchidos
        if novo_usuario.nome and novo_usuario.email and novo_usuario.senha:
            novo_usuario.save()
        else:
            return render(request, 'usuarios/usuarios.html', {
                'error': 'Preencha todos os campos obrigatórios!',
                'usuarios': Usuario.objects.all()
            })

    # Retorna todos os usuários cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def listagem_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtém todos os usuários cadastrados
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def upload_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Salva no diretório de mídia
        filename = fs.save(video.name, video)
        uploaded_file_url = fs.url(filename)
        return render(request, 'usuarios/upload_success.html', {'uploaded_file_url': uploaded_file_url})
    return redirect('listagem_usuarios')

def dashboard(request):
    # Dados para o gráfico
    vendas = [12, 19, 3, 5, 2]
    cores = [300, 50, 100]
    return render(request, 'usuarios/dashboard.html', {'vendas': vendas, 'cores': cores})
