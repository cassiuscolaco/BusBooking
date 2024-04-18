from django.db import models

# Create your models here.
class MumbaiRoute(models.Model):
	route_no=models.CharField(max_length=10)
	destination=models.CharField(max_length=100)

	def __str__(self):	
		return self.route_no