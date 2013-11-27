from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.user.username
		