from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,null=True, on_delete = models.CASCADE,unique=True)
	image = models.ImageField(default="default.jpg", upload_to = 'profile_pic',null=True)

	def __str__(self):
		return '{self.user.username} Profile'