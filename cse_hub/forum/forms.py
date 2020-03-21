from django.forms import ModelForm, Textarea
from .models import Post, Comment

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['description']
		widgets = {
			'description': Textarea(attrs={'rows':5, 'cols':8}),
		}