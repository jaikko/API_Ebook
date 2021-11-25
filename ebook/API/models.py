from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import deletion
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinLengthValidator

# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=100, null=False, unique=True)
    date_created = models.DateTimeField(default=now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def update(self, *args, **kwargs):
        kwargs.update({'date_updated': now, 'is_active' : self.is_active})
        super().update(*args, **kwargs)

        return self

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=64, null=False)
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.CharField(max_length=64, null=False)
    image = models.CharField( max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"

