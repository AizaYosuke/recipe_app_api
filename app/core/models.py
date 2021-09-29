from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """cria e salva um novo usuário"""
        if(not email):
            raise ValueError('Usuários precisam ter um endereço de email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Cria e salva um super usuário"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Usuário costumizado model que suporta o
            uso de email ao inves de username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'