from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Users(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'

    bio = models.TextField(
        blank=True,
        verbose_name='Биография',
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
    )
    role = models.CharField(
        max_length=20,
        choices=Users.choices,
        default=Users.USER,
        verbose_name='Роль пользователя',
    )

    def save(self, *args, **kwargs):
        if self.role == self.Users.ADMIN:
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.Users.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.Users.MODERATOR

    @property
    def is_user(self):
        return self.role == self.Users.USER

    def __str__(self):
        return self.username
