from smtplib import SMTPResponseException

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import CustomUser
from .permissions import IsAdmin
from .serializers import (
    RegistrationSerializer, TokenSerializer, UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAdmin,)
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)

        serializer = self.get_serializer(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('role'):
            serializer.validated_data['role'] = request.user.role
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user, created = CustomUser.objects.get_or_create(
        username=username, email=email
    )

    if not created:
        return Response(
            data={
                'error': 'Данный пользователь уже зарегистрирован.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    token = default_token_generator.make_token(user)
    try:
        send_mail(
            'Код для получения токена',
            f'{token}',
            f'{settings.EMAIL_DEBUG}',
            [email],
            fail_silently=False
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except SMTPResponseException:
        user.delete()
        return Response(
            data={
                'error': 'Ошибка отправки кода подтверждения.'
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
def create_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        CustomUser, username=serializer.validated_data['username']
    )
    if default_token_generator.check_token(
            user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(
        {'message': 'Пользователь не обнаружен'},
        status=status.HTTP_400_BAD_REQUEST
    )
