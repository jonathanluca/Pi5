from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_login import views

urlpatterns = [
    path('', views.login_usuario, name='home'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('autenticar/', views.autenticar_usuario, name='autenticar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('upload-video/', views.upload_video, name='upload_video'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

# Adicione esta linha para servir arquivos de mídia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)