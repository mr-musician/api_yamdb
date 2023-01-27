from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, create_token, signup

router = DefaultRouter()

router.register('v1/users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path('v1/auth/signup/', signup),
    path('v1/auth/token/', create_token),
]
