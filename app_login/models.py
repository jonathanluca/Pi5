from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de e-mail')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(email, nome, senha, **extra_fields)

class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128, default='default_password')  # Adicionado valor padrão

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    esq_ombro_x = models.FloatField(null=True, blank=True)
    esq_ombro_y = models.FloatField(null=True, blank=True)
    dir_ombro_x = models.FloatField(null=True, blank=True)
    dir_ombro_y = models.FloatField(null=True, blank=True)
    esq_cotovelo_x = models.FloatField(null=True, blank=True)
    esq_cotovelo_y = models.FloatField(null=True, blank=True)
    dir_cotovelo_x = models.FloatField(null=True, blank=True)
    dir_cotovelo_y = models.FloatField(null=True, blank=True)
    esq_pulso_x = models.FloatField(null=True, blank=True)
    esq_pulso_y = models.FloatField(null=True, blank=True)
    dir_pulso_x = models.FloatField(null=True, blank=True)
    dir_pulso_y = models.FloatField(null=True, blank=True)
    esq_quadril_x = models.FloatField(null=True, blank=True)
    esq_quadril_y = models.FloatField(null=True, blank=True)
    dir_quadril_x = models.FloatField(null=True, blank=True)
    dir_quadril_y = models.FloatField(null=True, blank=True)
    esq_joelho_x = models.FloatField(null=True, blank=True)
    esq_joelho_y = models.FloatField(null=True, blank=True)
    dir_joelho_x = models.FloatField(null=True, blank=True)
    dir_joelho_y = models.FloatField(null=True, blank=True)
    esq_tornozelo_x = models.FloatField(null=True, blank=True)
    esq_tornozelo_y = models.FloatField(null=True, blank=True)
    dir_tornozelo_x = models.FloatField(null=True, blank=True)
    dir_tornozelo_y = models.FloatField(null=True, blank=True)
    esq_angulo_perna = models.FloatField(null=True, blank=True)
    dir_angulo_perna = models.FloatField(null=True, blank=True)
    perna_da_frente = models.CharField(max_length=50, null=True, blank=True)
    pulso_da_frente = models.CharField(max_length=50, null=True, blank=True)
    copo_acima = models.BooleanField(default=False)
    stretch_pe_arma = models.BooleanField(default=False)

    def __str__(self):
        return f"Jogador {self.id}"