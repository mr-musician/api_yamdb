from reviews.models import Category, Title, Genre
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, TitleSerializer, GenreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = () # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name']

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [] # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name', 'year', 'genre', 'category']

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [] # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name']

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
