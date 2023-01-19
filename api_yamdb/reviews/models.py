from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self) -> str:
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self) -> str:
        return self.slug


class Titles(models.Model):
    name = models.CharField(max_length=256) # Название
    description = models.TextField() # Описание
    year = models.DateTimeField() # Год выпуска
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles', blank=True, null=True
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        related_name='titles', blank=True, null=True
    )

    def __str__(self) -> str:
        return self.text