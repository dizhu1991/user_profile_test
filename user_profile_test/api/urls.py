from django.conf.urls import re_path, include
from rest_framework.routers import SimpleRouter

from user_profile_test.api.views import MyUserViewSet

router = SimpleRouter()

router.register(r'user', MyUserViewSet, basename='user')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]
