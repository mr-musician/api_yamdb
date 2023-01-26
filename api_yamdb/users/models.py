from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER_ROLE = [
        (USER, 'user'),
        (ADMIN, 'admin'),
        (MODERATOR, 'moderator')
    ]
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта'
    )
    role = models.CharField(
        max_length=20,
        choices=USER_ROLE,
        default=USER,
        verbose_name='Роль пользователя'
    )

    def save(self, *args, **kwargs):
        if self.role == self.ADMIN:
            self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER

    def __str__(self):
        return self.username
