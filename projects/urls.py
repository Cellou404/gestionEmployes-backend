from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('', ProjectView)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:slug>/project-task-create/', ProjectTaskCreateView.as_view()), # ProjectTask Create url
    path('<slug:slug>/project-tasks/', ProjectTaskListView.as_view()), # Project tasks list url
    path('<slug:slug>/project-tasks/<int:pk>/', ProjectTaskUpdateDeleteView.as_view()), # Project tasks actions url
]