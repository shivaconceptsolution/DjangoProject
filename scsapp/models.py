from django.db import models

class Register(models.Model):
	emailid= models.CharField(max_length=200)
	password= models.CharField(max_length=200)
	mobile= models.CharField(max_length=200)
	fullname= models.CharField(max_length=200)
	address=models.CharField(max_length=200,default='')
	def __str__(self):
		return self.emailid+" "+self.password +" "+self.mobile+" "+self.fullname +" "+self.address
class Contact(models.Model):
   emailid= models.CharField(max_length=100)
   mobile= models.CharField(max_length=12)
   message= models.CharField(max_length=200)
   def __str__(self):
   	   return self.emailid +" "+self.mobile +" "+self.message
class Feedback(models.Model):
	emailid= models.CharField(max_length=200)
	feeddesc= models.CharField(max_length=200)
	feedto= models.CharField(max_length=200)
	
	def __str__(self):
		return self.emailid+" "+self.feeddesc +" "+self.feedto