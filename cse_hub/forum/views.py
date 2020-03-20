from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
from .models import Post

def home(request):
	posts = Post.objects.all()
	return render(request, 'forum/home.html', {'posts':posts})
	# return HttpResponse('<h3> Forum Home Page, returning HttpResponse instead of rendering html page </h3>')

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			messages.success(request, 'Created Post Successfully')
		else:
			messages.error(request, 'Error Creating Post')
	return render(request, 'forum/add_post.html', {'form':PostForm()})

def display_post(request, post_id):
	post = Post.objects.get(id=post_id)
	comments = post.comment_set.all()
	return render(request, 'forum/display_post.html', {'post':post, 'form':CommentForm(), 'comments':comments})

@login_required
def comment(request, post_id):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.post = Post.objects.get(id=post_id)
			form.save()
			messages.success(request, 'comment added Successfully')
		else:
			messages.error(request, 'error adding comment')
	return HttpResponse('Take HttpResponse for now, will return to post page')