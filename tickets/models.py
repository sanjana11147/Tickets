from django.db import models
from django.core.validators import RegexValidator


class Ticket(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')

class User(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(validators=[[RegexValidator(regex='[a-z]+@[a-z]{2}(.iitr.ac.in)', message='Enter gsuite email address', code='Invalid email')]])
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.name
