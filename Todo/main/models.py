from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
#one
class Category(models.Model):
	name=models.CharField(max_length=50,unique=True)
	description=models.TextField(null=True,blank=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name}'

#to many
class Task(models.Model):
		#list of set
	STATUS_CHOICES=[
		('PENDING','PENDING'),
		('IN PROGRESS','IN PROGRESS'),
		('COMPELETED','COMPELETED'),
	]

	title=models.CharField(max_length=100)
	description=models.TextField()
	deadlin=models.DateField(null=False,blank=False)
	created_at=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=12,choices=STATUS_CHOICES,default='PENDING')
	priorty=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],default=2)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.title}'
	


#فى حالة ان لكل تاسك كومنت واحد
class comment(models.Model):
    
	content=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	task=models.ForeignKey(Task,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)