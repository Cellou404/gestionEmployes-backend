from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer

class TasksListView(ListCreateAPIView):
    """
    View for Listing or  Creating a model instance.

    Returns a list of all **tasks** from the database.
    Create **tasks** in the database.

    For listing & Creation [see here][ref].

    [ref]: http://localhost:8000/api/tasks/

    """
    queryset = Task.objects.all().order_by('-created')
    permission_classes = (permissions.AllowAny, )
    serializer_class = TaskSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) # Each task has an owner


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update an delete a **task** from the database.

    For more details [see here][ref].

    [ref]: http://localhost:8000/api/tasks/#task_slug/

    Replace #task slug by an existing **task slug**

    """
    queryset = Task.objects.all().order_by('-created')
    permission_classes = (permissions.AllowAny, )
    serializer_class = TaskSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)