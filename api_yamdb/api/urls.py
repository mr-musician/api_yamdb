from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, ReviewViewSet

router = DefaultRouter()

router.register(
    'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewViewSet,
    basename='Review',
)

router.register(
    'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),  # заглушка
    path('v1/', include('djoser.urls.jwt')),  # заглушка
]
