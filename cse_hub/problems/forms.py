from django.forms import ModelForm
from .models import problem, testCase, submissions

class SubmitSolutionForm(ModelForm):
	class Meta:
		model = submissions
		fields = ['submission_code']

class ProblemForm(ModelForm):
	class Meta:
		model = problem
		fields = ['quesCode', 'description','tags']

class TestCaseForm(ModelForm):
	class Meta:
		model = testCase
		fields = ['testcase', 'solution', 'question']