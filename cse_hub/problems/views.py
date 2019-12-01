from django.shortcuts import render
from .forms import ProblemForm, TestCaseForm, SubmitSolutionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import problem, testCase

from evaluation.evaluate import evaluate

# login is required to submit solution
@login_required
def submit(request, id):
	# if this page was tried to access while submitting a form (adding submission to a problem)
	if request.method == 'POST':
		form = SubmitSolutionForm(request.POST, request.FILES)
		if form.is_valid():
			# create and instance of form but don't save it
			form = form.save(commit=False)
			form.author = request.user
			form.problem_code = problem.objects.get(id=id)
			form.save()

			cur_user = request.user
			cur_user.profile.problems_tried += 1
			cur_prob = problem.objects.get(id=id)
			cur_prob.total_submissions += 1

			verdict = evaluate(form.submission_code, id)
			if verdict == 'AC':
				cur_user.profile.problems_solved += 1
				cur_prob.successful_submissions += 1

			cur_prob.save()
			cur_user.profile.save()
			# print(request.user, '=================================================',cur_user.profile.problems_tried)
			# update all fields of question and user submissions
			messages.success(request, 'Added submission')
		else:
			messages.error(request, 'cant add submission')
	return render(request, 'problems/add_submission.html', {'form': SubmitSolutionForm()})

@login_required
def add_testcase(request):
	if request.method == 'POST':
		form = TestCaseForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Added testcase')
		else:
			print(form.errors)
			messages.error(request, 'cant add testcase')
	return render(request, 'problems/add_testcase.html', {'form':TestCaseForm()})

def problems(request):
	problems = problem.objects.all()
	# if request.method == 'GET':
	# 	order = request.GET.get('order_by',False)
	# 	if order:
	# 		problems = problem.objects.all().order_by(str(order))
	return render(request, 'problems/display_problems.html', {'problems':problems})

def display_problem(request, id):
	cur_prob = problem.objects.get(id=id)
	return render(request, 'problems/display_a_problem.html', {'problem':cur_prob})

@login_required
def add_problem(request):
	if request.method == 'POST':
		form = ProblemForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			messages.success(request, 'Added problem statement')
		else:
			messages.error(request, 'cant upload your problem')

	return render(request, 'problems/add_problem.html', {'form':ProblemForm()})