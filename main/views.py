# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    stuff_for_frontend = {
        'todo_items': todo_items,
    }

    return render(request, 'main/index.html', stuff_for_frontend)

def add_todo(request):
    # print(request.POST)
    current_date = timezone.now()
    task = request.POST["task"]
    # print(added_date, task)

    Todo.objects.create(added_date=current_date, text=task)
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    # print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")