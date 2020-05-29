from django.urls import path

from . import views

urlpatterns = [
    path('helloWorld/', views.hello_world),
    path('', views.task_list, name= 'task-list'),
    path('task/<int:id>', views.taskView, name='task.view'),
    path('newTask/', views.new_task, name="new-task"),
    path('edit/<int:id>', views.edit_task, name="edit-task"),
    path('delete/<int:id>', views.delete_task, name="delete-task"),
    path('yourName/<str:name>', views.your_name, name='your-name'),    # nome do arquivo/ nome da view/ nome simbólico
]