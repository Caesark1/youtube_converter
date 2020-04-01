from django.db import models

class Contact(models.Model):
	firstname = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 50)
	youtube = models.URLField(max_length = 255)

	def __str__(self):
		return self.firstname