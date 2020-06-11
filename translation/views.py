from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def myView(request):
    return HttpResponse("Hello!! I'm Translation.")

def pageView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items' : all_todo_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/index/')
    # create a new todo item and save it
    # save it
    # redirect the browser to /page/

def deleteTodo(request, todo_id):
    # c = request.POST['todo_id']
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/index/')

def translate(request):
    c = request.POST['source_sent']
    new_item = TodoItem(content = c)
    new_item.save()
    return HttpResponseRedirect('/index/')

def index(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items})
    # return render(request, 'index.html')

def wix(request):
    return render(request, 'wix.html')
