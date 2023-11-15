from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    task_form = TaskForm()
    context = {"task_form": task_form}
    return render(request, 'todolist/index.html', context)

def add_task(request):
    if request.method == 'POST':
        task = Task(item=)
               
def outstanding_tasks(request):
    tasks = Task.objects.filter(completion_status=False)
    context = {"tasks": tasks}
    return render(request, 'todolist/outstanding_tasks.html', context)

def completed_tasks(request):
    tasks = Task.objects.all(completion_status=True)
    context = {"tasks": tasks}
    return render(request, 'todolist/outstanding_tasks.html', context)