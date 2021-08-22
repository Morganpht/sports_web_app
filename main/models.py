from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField
import random






# Create your models here.

class Profile(models.Model):

    def random_pic(array):
        return array[random.randint(0, (len(array)-1))]

    defaultAvatars = ['avatar_01.png', 'avatar_02.png', 'avatar_03.png', 'avatar_04.png']

    genderChoices = (("1", "Male"), ("2", "Female"), ("3", "Other"), ("4", "Prefer not to say"))

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=genderChoices, null=True)
    profile_pic = models.ImageField(default=random_pic(defaultAvatars), null=True)
    nationality = CountryField(blank_label='(select country)',null=True)
    #teams = models.ManyToManyField(Team) #this is an example of adding a team e.g. many teams connecting to many profiles.

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    