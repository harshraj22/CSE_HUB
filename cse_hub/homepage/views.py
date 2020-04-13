from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse
from users.models import Profile
from django.contrib.auth import authenticate, login

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            profile_pic = form.cleaned_data['profile_pic']
            print(f'profile pic {profile_pic} \n\n')
            if profile_pic is None or len(profile_pic) == 0:
                profile_pic = 'profile_pics/default.png'

            user = Profile.objects.create(user=new_user, problems_tried=0 , problems_solved=0 , problems_TLE=0 , problems_WA=0, profile_pic=profile_pic)

            messages.success(request, "Thanks for registering.")
            # return redirect('profile')
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()
    args = {'form':form}
    return render(request, 'homepage/homepage.html', args)

def code_editor(request, code='Your Code Here'):
    return render(request, 'homepage/editor.html', {'code':code})