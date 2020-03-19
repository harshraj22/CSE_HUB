from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

@login_required
def profile(request, username):
    try:
        requested_user = User.objects.get(username=username)
        context = {'user': requested_user}
        return render(request, 'users/profile.html', context)
    except ObjectDoesNotExist:
        requested_user = None
        return HttpResponse("<h3> 404 User not found<h3> <p> This is returned from HttpResponse, make a template in home app, and render that page and return that before final presentation. </p>")
