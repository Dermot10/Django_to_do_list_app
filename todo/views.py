from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import to_doitem


def todo_view(request):
    all_appitems = to_doitem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_appitems})


# Create To do list items and save it
def addTodo(request):
    new_item = to_doitem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = to_doitem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/todo/')
