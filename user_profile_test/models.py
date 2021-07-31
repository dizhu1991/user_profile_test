from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    """My User model, inheriting AbstractUser.

    Username will be removed; email will be used as the 'username' field.
    """
    GENDER_CHOICES = (
        ('F', "Female",),
        ('M', "Male",),
        ('D', "Gender Diverse",),
    )
    """Customized User model, using email to substitute the username field."""
    email = models.EmailField(_("Your Email as Username"), max_length=255,
                              unique=True, blank=False, db_index=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, max_length=25)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """String representation with the email field."""
        return self.email
