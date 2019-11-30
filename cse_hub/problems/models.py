from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib import admin
# import jsonfield

class questionTag(models.Model):
	tag = models.CharField(max_length=15)

	def __str__(self):
		return self.tag

class problem(models.Model):
	quesCode = models.CharField(max_length=10)
	description = models.TextField()
	# description = jsonfield.JSONField()
	created_on = models.DateField(default=datetime.date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(questionTag)

	def __str__(self):
		return str(self.quesCode)+" by "+str(self.author.username)

admin.site.register(questionTag)
admin.site.register(problem)