from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_profile_test.api.views import MyUserViewSet

router = DefaultRouter()

router.register(r'user', MyUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
