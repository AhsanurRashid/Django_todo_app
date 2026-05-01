from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.add_task, name='add_task'),
    path('markAsDone/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('markAsUndone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('deleteTask/<int:pk>/', views.delete_task, name='delete_task'),
]