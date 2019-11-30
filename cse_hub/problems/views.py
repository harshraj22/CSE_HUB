from django.shortcuts import render
from .forms import ProblemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def problems(request):
	pass

@login_required
def add_problem(request):
	if request.method == 'POST':
		form = ProblemForm(request.POST)
		if form.is_valid():
			form.author = request.user
			form.save()
			messages.success(request, 'Added problem statement')
		else:
			messages.error(request, 'cant upload your problem')

	return render(request, 'problems/add_problem.html', {'form':ProblemForm()})