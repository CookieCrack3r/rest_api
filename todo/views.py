from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializer import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    