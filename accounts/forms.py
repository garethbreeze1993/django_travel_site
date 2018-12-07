from django.contrib.auth import get_user_model # this returns the user model currently active in this project
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	class Meta():
		fields = ('username','email','password1','password2')
		model = get_user_model()