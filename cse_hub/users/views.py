from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import ProfileUpdateForm

@login_required
def profile(request, username):
    try:
        requested_user = User.objects.get(username=username)
        context = {'user': requested_user}
        return render(request, 'users/profile.html', context)
    except ObjectDoesNotExist:
        requested_user = None
        return HttpResponse("<h3> 404 User not found<h3> <p> This is returned from HttpResponse, make a template in home app, and render that page and return that before final presentation. </p>")

@login_required
def profile_edit(request, username):
	# logged in user can only his/her profile
	if username != request.user.username:
		return HttpResponseRedirect(reverse('user-profile-edit', kwargs={'username':request.user.username}))
		
	context = {'form': ProfileUpdateForm()}
	return render(request, 'users/profile_edit.html', context)
	# return HttpResponse(f"Editing profile of {request.user.username}")