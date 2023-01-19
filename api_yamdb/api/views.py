from django.shortcuts import render
from reviews.models import Category, Titles, Genre
from rest_framework import viewsets
from .serializers import CategorySerializer, TitlesSerializer, GenreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
