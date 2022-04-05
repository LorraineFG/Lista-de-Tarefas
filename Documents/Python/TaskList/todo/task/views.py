from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def taskList(request):
  tasks = Task.objects.all().order_by('-created_al')
  return render(request, 'task/list.html', {'tasks': tasks})

def taskView(request, id):
  task = get_object_or_404(Task, pk=id)
  return render(request, 'task/task.html', {'task': task})

def newTask(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)

    if form.is_valid():
      task = form.save(commit=False)
      task.done = 'doing'
      task.save()
      return redirect('/')

  else:
    form = TaskForm()
  return render(request, 'task/addtask.html', {'form':form})

def editTask(request, id):
  task = get_object_or_404(Task, pk=id)
  form = TaskForm(instance=task)

  if(request.method == 'POST'):
    
    form = TaskForm(request.POST, instance=task)
   
    if(form.is_valid()):
      task.save()
      return redirect ('/')
    else:
      return render(request, 'task/edittask.html', {'form':form, 'task':task})

  else:
    return render(request, 'task/edittask.html', {'form':form, 'task':task})

def helloWorld(request):
  return HttpResponse(" Hello World! ")

def yourName(request, name):
  return render(request, 'task/yourname.html', {'name': name})