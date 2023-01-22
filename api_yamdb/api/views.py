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
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from api.serializers import CommentSerializer, ReviewSerializer
from reviews.models import Review, Title


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = ()  # владелец/админ/модер или ридонли

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, review=review)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = ()  # владелец/админ/модер или ридонли

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id'),
        )
        serializer.save(author=self.request.user, title=title)
