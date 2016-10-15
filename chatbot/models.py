from django.db import models

# Create your models here.
class Resume(models.Model):
	greetings = models.CharField(max_length = 250)#model is the variable and the data is stored in the form of char.
	address = models.CharField(max_length = 250)
	contact = models.CharField(max_length = 100)
	name= models.CharField(max_length = 1000)
	fbid= models.CharField(max_length = 1000)


	def __str__(self):
		return self.name