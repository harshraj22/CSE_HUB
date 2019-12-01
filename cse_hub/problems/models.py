from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib import admin
# import jsonfield

class submissions(models.Model):
	submission_code = models.FileField(upload_to='submissions/')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class questionTag(models.Model):
	tag = models.CharField(max_length=15)

	def __str__(self):
		return self.tag

class problem(models.Model):
	quesCode = models.CharField(max_length=10)
	description = models.TextField()
	# description = jsonfield.JSONField()
	total_submissions = models.IntegerField(default=0)
	successful_submissions = models.IntegerField(default=0)
	created_on = models.DateField(default=datetime.date.today)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(questionTag)

	def __str__(self):
		return str(self.quesCode)+" by "+str(self.author.username)


class testCase(models.Model):
	testcase = models.FileField(upload_to='problem_statements/testcases')
	solution = models.FileField(upload_to='problem_statements/solutions')
	question = models.ForeignKey(problem, on_delete=models.CASCADE)

	def __str__(self):
		return self.question.quesCode


admin.site.register(questionTag)
admin.site.register(problem)
admin.site.register(testCase)