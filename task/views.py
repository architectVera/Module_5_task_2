from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
import json

# Create your views here.
tasks = [
    {"id": 1, "title": "Task #1", "completed": False},
    {"id": 2, "title": "Task #2", "completed": True},
    {"id": 3, "title": "Task #3", "completed": False},
    {"id": 4, "title": "Task #4", "completed": True},
    {"id": 5, "title": "Task #5", "completed": False}
]

task = [
    {
        "id": 1,
        "title": "First task: to learn python",
        "description": "Some long task description...",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": False
    },
    {
        "id": 2,
        "title": "Second task: to learn python",
        "description": "Some long task description...",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": True
    },
    {
        "id": 3,
        "title": "Third task: to learn python",
        "description": "Some long task description...",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": False
    },
    {
        "id": 4,
        "title": "Fourth task: to learn python",
        "description": "Some long task description...",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": True
    },
    {
        "id": 5,
        "title": "Fifth task: to learn python",
        "description": "Some long task description...",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": False
    }

]


def task_view(request: HttpRequest):
    ctx = {'object_list': tasks}
    return render(request, 'task_list.html', ctx)


def task_detail_view(request: HttpRequest, id: int) -> HttpResponse:
    for task_one in task:
        if task_one["id"] == id:
            return render(request, 'task_detail.html', {'object':task_one})
    raise Http404
