from django.forms import ModelForm
from .models import Problem, TestCase, Submissions

class SubmitSolutionForm(ModelForm):
	class Meta:
		model = Submissions
		fields = ['submission_code']

class ProblemForm(ModelForm):
	class Meta:
		model = Problem
		fields = ['quesCode', 'description','tags','time']

class TestCaseForm(ModelForm):
	class Meta:
		model = TestCase
		fields = ['testcase', 'solution', 'question']

	def __init__(self, *args, **kwargs):
		# for current user, display only those problems which he/she has added
		user = kwargs.pop('user')
		# for calling parent class, we need to remove 'user' form kwargs
		super(TestCaseForm, self).__init__(*args, **kwargs)

		# filter the 'question' field to be displayed in the form
		self.fields['question'].queryset = Problem.objects.filter(author=user)
