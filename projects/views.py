from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .serializers import ProjectSerializer, ProjectTaskSerializer
from .models import Project, ProjectTask
from .permissions import IsOwner, IsStaff, IsTaskOwner


# ================= Project VIEW ================= # 
# `ModelViewSet` a viewset that allows all actions: CRUD
class ProjectView(viewsets.ModelViewSet):
    """
    Returns a list of all **projects** from the database.
    Create **projects** in the database.

    For listing & Creation [see here][ref].

    [ref]: http://localhost:8000/api/projects/

    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner | IsStaff]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    


# ================= ProjectTask List VIEW ================= # 
class ProjectTaskView(generics.ListCreateAPIView):
    """
    Returns a list of all **project tasks list** from the database.
    
    Each project can have mutiple task that have to be completed

    Creatin a model instance.
    Create **project tasks** in the database.

    For creation [see here][ref].

    [ref]: http://localhost:8000/api/projects/`project-slug`/

    Replace `project-slug` by particular project slug since the lookup field is `slug`

    """
    serializer_class = ProjectTaskSerializer
    permission_classes = [IsOwner | IsAdminUser]
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return ProjectTask.objects.filter(project__slug=slug)


# ================= ProjectTask RETRIEVE - UPDATE & DELETE VIEW ================= # 
class ProjectTaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Delete project **tasks**

    """
    queryset = ProjectTask.objects.all()
    serializer_class = ProjectTaskSerializer
    permission_classes = [IsTaskOwner | IsStaff]

