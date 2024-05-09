from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.

class TaskListView(TemplateView):
    template_name = 'frontend/list.html'
