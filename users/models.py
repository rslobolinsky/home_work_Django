from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
            self,
            email: str,
            password: str | None = None,
            **extra_fields,
    ):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
            self,
            email: str,
            password: str | None = None,
            **extra_fields,
    ):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='Страна', blank=True, null=True)
    token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


# class User(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True, verbose_name='Email')
#     phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
#     avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', blank=True, null=True)
#     country = models.CharField(max_length=100, verbose_name='Страна', blank=True, null=True)
#     token = models.CharField(max_length=100, verbose_name='Токен', blank=True, null=True)
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.email
