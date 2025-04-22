from django.urls import path
from app_login import views

urlpatterns = [
    path('', views.login_usuario, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('autenticar/', views.autenticar_usuario, name='autenticar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),  # Adicionada esta linha
]