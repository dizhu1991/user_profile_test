from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """New create_user method for MyUser model."""
        if not email:
            raise ValueError(_('Email is required.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """New create_superuser method for MyUser model."""
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Please set is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Please set is_superuser=True.'))
        return self.create_user(email, password, **kwargs)


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

    objects = MyUserManager()

    def __str__(self):
        """String representation with the email field."""
        return self.email
