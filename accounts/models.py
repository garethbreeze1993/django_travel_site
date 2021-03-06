from django.db import models
from django.contrib import auth # built in django stuff for accounts


class User(auth.models.User,auth.models.PermissionsMixin):
	def __str__(self):
		return self.username # username is an attribute in the auth.models.User class see django docs

# Create your models here.
