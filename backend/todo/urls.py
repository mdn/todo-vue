from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.ListTodo.as_view(), name='list_todo'),
    path('<int:pk>', views.RetrieveUpdateDestroyTodo.as_view(), name='todo_action'),
]
