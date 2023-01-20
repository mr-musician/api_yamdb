from django.urls import include, path
from rest_framework import routers
from .views import TitleViewSet, CategoryViewSet, GenreViewSet


router = routers.DefaultRouter()
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router.urls)),
]