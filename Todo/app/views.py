from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoModelForm
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
        'form' : TodoModelForm
    }
    return  render(request,'app/index.html',context)
def completed(request,pk):
    todo=Todo.objects.get(id = pk)
    todo.completed =True
    todo.save()
    return  redirect('/')
def add(request):
    if request.method == "POST":
         form = TodoModelForm(request.POST)
         if form.is_valid():
            form.save()
    return redirect('/')
def delete(request,pk):
    todo=Todo.objects.get(id = pk)
    todo.delete()
    return  redirect('/')
def deleteall(request):
    todo = Todo.objects.all()
    todo.delete()
    return redirect('/')
def notcomplete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.completed=False
    todo.save()
    return redirect('/')

