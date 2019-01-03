from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

@login_required
def tasks(request):
    tasks = Task.objects
    if request.method == 'POST':
        if request.POST['taskDescription']:
            task = Task()
            task.task_description = request.POST['taskDescription']
            task.customer = request.user
            task.save()
            return redirect('tasks')
        else:
            return render(request, 'tasks/tasks.html', {'error':'Enter task description.'})
    else:
        return render(request, 'tasks/tasks.html', {'tasks':tasks})

def complete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('tasks')
