from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import ProfileUpdateForm
from django.conf import settings
import os


@login_required
def profile(request, username):
	try:
		requested_user = User.objects.get(username=username)
		image_url = requested_user.profile.profile_pic
		context = {'user': requested_user, 'pic': image_url}

		return render(request, 'users/profile.html', context)
	except ObjectDoesNotExist:
		requested_user = None
		return render(request, 'homepage/404.html')

@login_required
def profile_edit(request, username):
	# logged in user can only his/her profile
	if username != request.user.username:
		return HttpResponseRedirect(reverse('user-profile-edit', kwargs={'username':request.user.username}))
		
	# ===========Implement the followint logic ==================
	# if request.method == 'POST':

	context = {'form': ProfileUpdateForm()}
	return render(request, 'users/profile_edit.html', context)
	# return HttpResponse(f"Editing profile of {request.user.username}")