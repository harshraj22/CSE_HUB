from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Post(models.Model):
	# one post => one author
	# but one author can have many posts
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{self.title}'

	def __repr__(self):
		return '{self.title} by {self.author.username}'


class Comment(models.Model):
	# one comment => one author
	# but one author can have many comments
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	time_of_comment = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	description = models.TextField()

	def __str__(self):
		return 'on {self.post.id} by {self.author.username}'

	def __repr__(self):
		return self.__str__()

admin.site.register(Post)
admin.site.register(Comment)
