from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.contrib import admin
# import jsonfield

class QuestionTag(models.Model):
	'''
		class for storing Problem Tags
	'''
	tag = models.CharField(max_length=15, unique=True)

	def __str__(self):
		return self.tag
	def __repr__(self):
	 return self.__str__()


class Problem(models.Model):
	'''
		Class for storing Problems and its testcase and other data
	'''
	quesCode = models.CharField(max_length=10, unique=True)
	description = models.TextField()
	# description = jsonfield.JSONField()

	total_submissions = models.IntegerField(default=0)
	successful_submissions = models.IntegerField(default=0)

	created_on = models.DateField(default=datetime.date.today)
	# if user is deleted, delete this problem automatically
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	# one question can have many tags, and one tag can belong to many questions
	tags = models.ManyToManyField(QuestionTag)
	# time-limit for the current problem
	time = models.FloatField(choices=[(0.5,0.5),(1.0,1.0)], default=1.0)

	def __str__(self):
		return f'{self.quesCode}'

	def __repr__(self):
		return f'{self.quesCode} by {self.author.username}'


class Submissions(models.Model):
	'''
		For submited code for evaluation
	'''
	submission_code = models.FileField(upload_to='submissions/')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	problem_code = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'by {self.author.username}'

	def __repr__(self):
	 return f'Solution for {self.problem_code} by {self.author.username}'

class TestCase(models.Model):
	'''
	    Class for testcase of problems
	'''
	testcase = models.FileField(upload_to='problem_statements/testcases')
	solution = models.FileField(upload_to='problem_statements/solutions')

	# if problem is deleted, delete this testcase as well
	question = models.ForeignKey(Problem, on_delete=models.CASCADE)

	def __str__(self):
		return self.question.quesCode

	def __repr__(self):
		return f'Testcase for {self.question.quesCode}'

admin.site.register(QuestionTag)
admin.site.register(Problem)
admin.site.register(TestCase)
