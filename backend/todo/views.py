from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import TodoItem
from .serializers import TodoItemSerializer


class ListTodo(ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class RetrieveUpdateDestroyTodo(RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'pk'
