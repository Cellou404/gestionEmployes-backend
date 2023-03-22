from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('', ProjectView)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:slug>/project-tasks/', ProjectTaskView.as_view()), # Project tasks list | create url
    path('<slug:slug>/project-tasks/<int:pk>/', ProjectTaskUpdateDeleteView.as_view()), # Project tasks actions url
]