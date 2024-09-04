from django.shortcuts import render,redirect,get_object_or_404
#return http response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task,Category
from .forms import TaskForm,CategoryForm
# Create your views here.


@login_required
def index(request):
	tasks=Task.objects.filter(user=request.user).order_by('deadlin')
	categories=Category.objects.filter(user=request.user)
	context={
		'tasks':tasks,
		'categories':categories
		}
	return render(request,'main/index.html',context)



@login_required
def detailed_task(request,pk):
	task=Task.objects.get(id=pk)
	context={
		'task':task
	}
	return render(request,'main/detailed.html',context)



@login_required
def todo_by_status(request,st):
	todos=Task.objects.filter(status=st)
	context={
		'todos':todos
	}

	return render(request,'main/todosstatus.html',context)




@login_required
def Createtodo(request):
	if request.method == 'POST':
		form=TaskForm(request.POST)
		if form.is_valid():
			task=form.save(commit=False)
			task.user=request.user
			task.save()
			return redirect('home')
	else:
		form=TaskForm()
	return render(request,'main/create_todo.html',{'form':form})


@login_required
def Createcategory(request):
	if request.method == 'POST':
		form=CategoryForm(request.POST)
		if form.is_valid():
			cat=form.save(commit=False)
			cat.user=request.user
			return redirect('home')
	else:
		form=CategoryForm()
	return render(request,'main/createCategorys.html',{'form':form})



@login_required
def update_task(request , id ):
	task = get_object_or_404(Task , id=id)
	if request.method == 'POST':
		form = TaskForm(request.POST , instance=task)
		if form.is_valid() :
			form.save()
			return redirect('home')
	else:
		form = TaskForm(instance=task)
		
	return render(request, 'main/updatetask.html' , {'form':form})
	
	

@login_required
def delete_task(request , id):
    task = get_object_or_404(Task , id=id)
    task.delete()
    return redirect('home')



