from django.db import models

# Create your models here.
class event(models.Model):
	greetings = models.CharField(max_length = 250)#model is the variable and the data is stored in the form of char.
	name = models.CharField(max_length = 250)
	contact = models.IntegerField(max_length = 100)
	fbid= models.CharField(max_length = 1000)
	dates= models.CharField(max_length = 1000)
	fblink= models.URLField(max_length = 1000)
	description= models.CharField(max_length = 1000)
	emailid= models.EmailField(max_length = 1000)
	logolink= models.URLField(max_length = 1000)
	state= models.IntegerField(max_length = 1000)
	location = models.CharField(max_length = 250)
	


	def __str__(self):
		return self.name