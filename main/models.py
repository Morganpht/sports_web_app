from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.

class Profile(models.Model):

    genderChoices = (("1", "Male"), ("2", "Female"), ("3", "Other"), ("4", "Prefer not to say"))

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=genderChoices, blank=True, null=True)
    #teams = models.ManyToManyField(Team) #this is an example of adding a team e.g. many teams connecting to many profiles.

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()