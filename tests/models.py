from django.test import TestCase
from django.contrib.auth import get_user_model


class TestMyUser(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='test@email.com',
            password='ssssssssO0='
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), 'test@email.com')
