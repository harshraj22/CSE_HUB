from django.forms import ModelForm
from .models import problem

class ProblemForm(ModelForm):
	class Meta:
		model = problem
		fields = ['quesCode', 'description','tags']

