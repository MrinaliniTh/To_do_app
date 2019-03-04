from django.shortcuts import render,redirect
from . models import Todo

# Create your views here.
def todo(request):
    todo=Todo.objects.all()
    context={
        'todo':todo
    }
    return render(request,'todo/todo.html',context)

def add(request):
    todo=Todo(note=request.POST['note'])
    todo.save()  
    return redirect('/todo/')

def delete(request,todo_id):
    
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todo/')        
