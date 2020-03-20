from django.shortcuts import render
from .forms import ProblemForm, TestCaseForm, SubmitSolutionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Problem, TestCase
from .models import Submissions as submitted_codes

from .evaluate import evaluate

@login_required
def submissions(request, id):
	codes = submitted_codes.objects.filter(author = request.user)

	return render(request, 'problems/display_submissions.html', {'codes':codes})

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
			form.save()

			cur_user = request.user
			cur_user.profile.problems_tried += 1
			cur_prob = Problem.objects.get(id=id)
			cur_prob.total_submissions += 1

			verdict = evaluate(form.submission_code, id)
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
		else:
			# if user filled form was invalid, send a error message
			messages.error(request, 'cant upload your problem')

	# return the page with a message and a new empty form
	return render(request, 'problems/add_problem.html', {'form':ProblemForm()})
