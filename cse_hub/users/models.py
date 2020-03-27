from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	problems_tried = models.IntegerField(default=0)

	problems_solved = models.IntegerField(default=0)
	problems_TLE = models.IntegerField(default=0)
	problems_WA = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

	def __repr__(self):
		return 'Profile of {self.user.username}'

admin.site.register(Profile)
