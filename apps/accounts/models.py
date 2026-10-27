from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.utils.validators import LETTER_SPACE_DASH_VALIDATOR


# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire!")
        if not email or not email.strip():
            raise ValueError("L'adresse email est obligatoire!")
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        user = self.model(
            username=self.model.normalize_username(username),
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("Superutilisateur doit avoir is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superutilisateur doit avoir is_superuser=True.")
        return self.create_user(username, email, password, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, validators=[LETTER_SPACE_DASH_VALIDATOR], verbose_name="Prénom")
    last_name = models.CharField(max_length=150, validators=[LETTER_SPACE_DASH_VALIDATOR], verbose_name="Nom")
    objects = CustomManager()
