import logging
import traceback

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework.viewsets import GenericViewSet
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

from user_profile_test.models import MyUser
from user_profile_test.api.serializers import MyUserSerializer

logger = logging.getLogger('__name__')


class MyUserViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    """API ViewSet to handle requests about MyUser model."""
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
    permission_classes = []
    pagination_class = PageNumberPagination
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        """Overwrites default get_queryset method."""
        queryset = self.queryset
        email = self.request.query_params.get('email')
        age = self.request.query_params.get('age')
        gender = self.request.query_params.get('gender')
        if email:
            queryset = queryset.filter(email=email)
        if age:
            queryset = queryset.filter(age=int(age))
        if gender:
            queryset = queryset.filter(gender=gender)
        return queryset

    def list(self, request, *args, **kwargs):
        """Overwrite list method."""
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Update a user profile."""
        try:
            return super(MyUserViewSet, self).update(request, *args, **kwargs)
        except ValidationError as err:
            logger.error('update profile failed,'
                         ' error: {}'.format(traceback.format_exc()))
            return Response(
                {'code': 400, 'error': '{}'.format(str(err))},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        validate_password(password)
        instance = MyUser.objects.create(email=email)
        instance.set_password(password)
        # Add permission of generating QR codes to the newly created user.
        instance.save()
        return Response(
            {
                'code': 201,
                'email': email,
                'message': "New user {} created successfully.".format(email)
            },
            status=status.HTTP_201_CREATED
        )
