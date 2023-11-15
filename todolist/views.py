from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        
        if task_form.is_valid():
            task = Task(item=task_form.cleaned_data['task'])
            task.save()
            return redirect('home') 
    else:
        task_form = TaskForm()
        context = {"task_form": task_form}
        return render(request, 'todolist/index.html', context)

def outstanding_tasks(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.completion_status = True
        task.save()
    
    tasks = Task.objects.filter(completion_status=False)
    context = {"tasks": tasks}
    return render(request, 'todolist/outstanding_tasks.html', context)



def completed_tasks(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    
    tasks = Task.objects.filter(completion_status=True)
    context = {"tasks": tasks}
    return render(request, 'todolist/completed_tasks.html', context)