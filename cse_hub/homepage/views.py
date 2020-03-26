from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from homepage.forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse

# def home(request):
# 	return render(request, 'homepage/homepage.html')

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for registering.")
            # return redirect('profile')
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()
    args = {'form':form}
    return render(request, 'homepage/homepage.html', args)
