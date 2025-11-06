from django.shortcuts import render, get_object_or_404
from django import forms
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.urls import reverse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

# Index View - Home page showing task list
def index(request):
    # Fetch all tasks from the database to display them
    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {
        "tasks": tasks  # Pass tasks to the template
    })

# In views.py
from django.http import JsonResponse
from .models import Task
def get_tasks(request):
    tasks = Task.objects.all().values()  # Fetch all tasks
    return JsonResponse(list(tasks), safe=False)

[
    {"id": 1, "name": "Complete homework", "completed": False},
    {"id": 2, "name": "Buy groceries", "completed": True}
]