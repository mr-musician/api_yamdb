from django.urls import include, path
from rest_framework import routers
from .views import TitleViewSet, CategoryViewSet, GenreViewSet, \
    CommentViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewViewSet,
    basename='Review',
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment',
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
