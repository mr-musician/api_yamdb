from rest_framework import serializers
from reviews.models import Title, Category, Genre, Comment, Review

class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='name', queryset=Genre.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre