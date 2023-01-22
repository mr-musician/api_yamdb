from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Title, Category, Genre

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
from rest_framework import serializers

from reviews.models import Comment, Review


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