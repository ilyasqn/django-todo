from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiView, name='apiView'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>', views.taskDetail, name='task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<int:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<int:pk>', views.taskDelete, name='task-delete'),
]