from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	GENDER = (
		('M', 'Male'),
		('F', 'Female'),
		)
	OCCUPATION = (
		('S', 'Student'),
		('P', 'Professional'),
		('H', 'Hobbyist')
		)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    tagline = models.CharField(max_length=35, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()