from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProblemForm, TestCaseForm, SubmitSolutionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Problem, TestCase
from .models import Submissions as submitted_codes
from django.contrib.auth.models import User
import os
from django.conf import settings
from django.http import Http404, HttpResponse
from .evaluate import evaluate

@login_required
def submissions(request, username):
	user = User.objects.get(username = username)
	codes = submitted_codes.objects.filter(author = user)

	return render(request, 'problems/display_submissions.html', {'codes':codes})

def download_submission(request, id):
	solution = submitted_codes.objects.get(id=id)
	file_path = settings.BASE_DIR + solution.submission_code.url

	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404

def display_submission(request, username, id):
	solution = submitted_codes.objects.get(id=id)
	# file_path = os.path.join(settings.BASE_DIR,solution.submission_code.url)
	file_path = settings.BASE_DIR + solution.submission_code.url
	print(f'\nAccessing file: {file_path}\n')

	with open(file_path) as f:
		code = f.read()

	return render(request, 'problems/display_a_submission.html', {'solution':solution, 'code':code})

# login is required to submit solution
@login_required
def submit(request, id):
	# if this page was tried to access while submitting a form (adding submission to a problem)
	if request.method == 'POST':
		# Create a temparory form with data as provided by user on front-end
		form = SubmitSolutionForm(request.POST, request.FILES)

		# get filename of file uploaded by user, we will use different methods to get output from different files
		filename = request.FILES['submission_code'].name

		# If the file is not cpp/python
		if not filename.endswith('.cpp') and not filename.endswith('.py'):
			messages.error(request, 'Wrong file type')

		elif form.is_valid():
			# create and instance of form but don't save it
			form = form.save(commit=False)
			form.author = request.user
			form.problem_code = Problem.objects.get(id=id)
			# form.save()

			cur_user = request.user
			cur_user.profile.problems_tried += 1
			cur_prob = Problem.objects.get(id=id)
			cur_prob.total_submissions += 1

			verdict = evaluate(form.submission_code, id)
			form.verdict = verdict
			form.save()
			
			if verdict == 'AC':
				cur_user.profile.problems_solved += 1
				cur_prob.successful_submissions += 1
			elif verdict == 'TLE':
				cur_user.profile.problems_TLE += 1
			elif verdict == 'WA':
				cur_user.profile.problems_WA += 1

			cur_prob.save()
			cur_user.profile.save()
			# print(request.user, '=======================',cur_user.profile.problems_tried)
			# update all fields of question and user submissions
			messages.success(request, 'Added submission')
		else:
			messages.error(request, 'cant add submission')
	return render(request, 'problems/add_submission.html', {'form': SubmitSolutionForm()})

@login_required
def add_testcase(request):
	if request.method == 'POST':
		form = TestCaseForm(request.POST, request.FILES, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, 'Added testcase')
		else:
			print(form.errors)
			messages.error(request, 'Couldnt add testcase')

	# pass the loggedin user in form, this will be rendered in forms.py and only those problems will
	# be displayed whose author is current loggedin user. Thus current user can't add testcase to problems
	# that someone else has added
	return render(request, 'problems/add_testcase.html', {'form':TestCaseForm(user=request.user)})

def problems(request):
	if 'sortBy' in request.GET.keys() and request.GET['sortBy'] == 'total':
		problems = Problem.objects.all().order_by('-total_submissions')
	else:
		problems = Problem.objects.all()

	# if request.method == 'GET':
	# 	order = request.GET.get('order_by',False)
	# 	if order:
	# 		problems = problem.objects.all().order_by(str(order))
	return render(request, 'problems/display_problems.html', {'problems':problems})

def display_problem(request, id):
	cur_prob = Problem.objects.get(id=id)
	return render(request, 'problems/display_a_problem.html', {'problem':cur_prob})

@login_required
def add_problem(request):
	# if this method was called after user filled a form, there must be a POST data in request
	if request.method == 'POST':
		# create a temporary form with data as filled by user
		form = ProblemForm(request.POST)
		# if form is valid, save the form and send success message
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.save()
			messages.success(request, 'Added problem statement')
			return redirect(reverse('add-testcase'))
		else:
			# print on backend terminal, for debugging purpose
			print(f'\n Error while adding problem:\n{form.errors.as_data()} \n')

			form_error = list(form.errors.as_data().values())[0][0]
			# if user filled form was invalid, send a error message
			messages.error(request, 'cant upload your problem')

			# list unpacking to show the first error as pop-up message
			messages.error(request, *form_error)

	# return the page with a message and a new empty form
	return render(request, 'problems/add_problem.html', {'form':ProblemForm()})
