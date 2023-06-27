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
    # views = models.PositiveIntegerField(default=0)
    views = models.ManyToManyField(User, related_name="viewed_software", blank=True)
    information = models.TextField()
    features = models.TextField()
    version = models.CharField(max_length=50)
    supported_systems = models.CharField(max_length=255)
    license = models.CharField(max_length=100)
    subscription = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")
    reviews = models.ManyToManyField("Review")
    price = models.PositiveIntegerField(default=100)
    release_date = models.DateField(default='2023-02-02')
    developer = models.CharField(max_length=255,default="")
    download_link = models.URLField(default="")
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_new_release = models.BooleanField(default=False)
    demo_available = models.BooleanField(default=False)
    documentation_link = models.URLField(default="")
    video_link = models.URLField(default="")
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
        return str(self.text)
#1.average rating with stars(number stars should be highlighted based upon the average rating).Done
#2.drop down just beside the average rating.Done
#3.Drop down menu should show the 5 progress bars out of 100%.You will show the number of 5 stars,4 stars and all stars here.Done


#Views field per software
#1.when loggged in user try viewing the software,the views should go +1.Done

#Seach_functionality_fix
#1.when there is no input in the search field and if search is requested then the system should show 4 random softwares on the same screen as index.html.Done
#2.when serach is activated,during that pagination should be deactivated.Done



#Payment/Add to cart functionality
#1.the user should be login before clicking on start free trial
#2.When I click on start free trial,it prompts me to new page where it should give me the 3 portions with the pricing information
#3.