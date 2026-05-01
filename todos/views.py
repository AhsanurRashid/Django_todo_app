from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if not task:
            return redirect('home')
        # save the task to the database
        Task.objects.create(task=task)
        return redirect('home')
    
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')