from django.forms import ModelForm
from .models import Profile

class ProfileUpdateForm(ModelForm):
	class Meta:
		model = Profile
		# password = forms.CharField(widget=forms.PasswordInput)
		# widgets = {
		# 	'password': forms.PasswordInput(),
		# }
		fields = []