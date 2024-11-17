from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic =models.ImageField(upload_to="teams/")
    twitter_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=100)