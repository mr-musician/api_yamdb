from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import CommentViewSet

router = DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
