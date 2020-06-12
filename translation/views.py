from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, UnmtItem
# Create your views here.

def yourName(request):
    all_todo_items = TodoItem.objects.all()
    current_name = "Nikhil Saini"
    return render(request, 'todo.html', {'all_items' : all_todo_items, 'current_name' : current_name})

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

def deleteAll(request):
    # c = request.POST['todo_id']
    TodoItem.objects.all().delete()
    return HttpResponseRedirect('/index/')

def deleteAllUnmt(request):
    # c = request.POST['todo_id']
    UnmtItem.objects.all().delete()
    return HttpResponseRedirect('/index/')

def deleteTodo(request, todo_id):
    # c = request.POST['todo_id']
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/index/')

def deleteUnmt(request, unmt_id):
    # c = request.POST['todo_id']
    item_to_delete = UnmtItem.objects.get(id=unmt_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/index/')

def translate(request):
    c = request.POST['source_sent']
    gen = c + " oh my god"
    new_item = TodoItem(content = c, gen = gen)
    new_item.save()
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items, 'all_unmt_items' : all_unmt_items, 'gen' : gen, 'source' : c})

def translateUnmt(request):
    c = request.POST['source_sent_unmt']
    gen = c + " unmt"
    # generate here
    new_item = UnmtItem(content = c, gen = gen)
    new_item.save()
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items, 'all_unmt_items' : all_unmt_items, 'gen_unmt' : gen, 'source_unmt' : c})

def index(request):
    all_todo_items = TodoItem.objects.all()
    all_unmt_items = UnmtItem.objects.all()
    return render(request, 'index.html', {'all_items' : all_todo_items,'all_unmt_items' : all_unmt_items})
    # return render(request, 'index.html')

def wix(request):
    return render(request, 'wix.html')
