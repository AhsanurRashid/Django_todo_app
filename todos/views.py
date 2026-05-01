from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        # save the task to the database
        Task.objects.create(task=task)
        return redirect('home')