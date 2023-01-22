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
