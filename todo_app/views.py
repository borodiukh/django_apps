from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        form = TaskForm()

        context = {'tasks': tasks, 'form': form}
        return render(request, 'todo_app/main.html', context=context)

    if request.method == 'POST':
        # it creates a TaskForm instance with the POST data
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')


def update_task(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)

        context = {'form': form}
        return render(request, 'todo_app/update_task.html', context=context)

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
        return redirect('/todo/')


def delete_task(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(id=pk)
        context = {'task': task}
        return render(request, 'todo_app/delete_task.html', context=context)

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('/todo/')

