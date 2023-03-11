from django.urls import path
from .views import TasksListView, TaskDetailView

urlpatterns = [
    # Enpoints
    path('', TasksListView.as_view()),
    path('<slug:slug>/', TaskDetailView.as_view())
]