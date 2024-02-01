from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.models import Todo
from todo.serializers import TodoModeSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModeSerializer
# Create your views here.
