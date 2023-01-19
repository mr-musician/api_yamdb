from reviews.models import Category, Titles, Genre
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, TitlesSerializer, GenreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = () # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name']
    lookup_field = ['slug']
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = [] # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name', 'year', 'genre', 'category']
    lookup_field = ['slug']

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [] # Админ или только чтение
    filter_backends = (filters.SearchFilter)
    search_fields = ['name']
    lookup_field = ['slug']

    def perform_create(self, serializer):
        return super().perform_create(serializer)
