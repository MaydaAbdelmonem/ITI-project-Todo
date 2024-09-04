from django import forms
from .models import Task,Category





class TaskForm(forms.ModelForm):
	
	
	class Meta:
		model=Task
		fields=['title','description','deadlin','status','priorty',
	'category']
		widgets = {
    'title':forms.TextInput(attrs={'class': 'form-control form-spacing'}),
    'description':forms.Textarea(attrs={'class': 'form-control form-spacing'}),
    'status':forms.Select(attrs={'class': 'form-control form-spacing'}),
    'priorty':forms.NumberInput(attrs={'class': 'form-control form-spacing'}),
    'deadlin':forms.DateInput(attrs={'class': 'form-control w-100 form-spacing ', 'type': 'date'}),
    'category':forms.Select(attrs={'class': 'form-control form-spacing'}),
}




class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=['name','description']
		widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control form-spacing'}),
            'description':forms.Textarea(attrs={'class': 'form-control form-spacing'})

        }

