from django.db import models
from users.models import CustomUser


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


class Title(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    year = models.IntegerField()
    genre = models.ManyToManyField(Genre,)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles', 
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return super().__str__()


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.ForeignKey(Title,on_delete=models.CASCADE)

    def __str__(self):
        return self.slug


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.IntegerField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
