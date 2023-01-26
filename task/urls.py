"""
Task application URL Configuration

"""
from django.urls import path
from task.views import task_view, task_detail_view

urlpatterns = [
    path('', task_view, name='task-list'),
    path('<int:id>/', task_detail_view, name='task-detail')
]