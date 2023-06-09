# Create your models here.
from django.db import models

# from django.contrib.auth import get_user_model

# User = get_user_model()

from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model


# user = get_user_model().objects.get(pk=uid)
# queryset = get_user_model().objects.all()


# class User(AbstractUser):
#     class Meta:
#         verbose_name = "user"
#         verbose_name_plural = "users"


class Software(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField(upload_to="software_images/")
    time_created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    information = models.TextField()
    features = models.TextField()
    version = models.CharField(max_length=50)
    supported_systems = models.CharField(max_length=255)
    license = models.CharField(max_length=100)
    subscription = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.name


class Plugin(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField(upload_to="plugin_images/")
    time_created = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    information = models.TextField()
    features = models.TextField()
    version = models.CharField(max_length=50)
    supported_systems = models.CharField(max_length=255)
    license = models.CharField(max_length=100)
    reviews = models.ManyToManyField("Review")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
