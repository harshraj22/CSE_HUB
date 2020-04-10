from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# MEDIA_ROOT is set to problems dir, but we don't want profile pics there
# so using static dir here
fs = FileSystemStorage(location=settings.PROFILE_PIC_STATIC_ROOT)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	problems_tried = models.IntegerField(default=0)

	profile_pic = models.ImageField(storage=fs, upload_to='profile_pics', default='default.png')

	problems_solved = models.IntegerField(default=0)
	problems_TLE = models.IntegerField(default=0)
	problems_WA = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

	def __repr__(self):
		return f'Profile of {self.user.username}'

admin.site.register(Profile)
