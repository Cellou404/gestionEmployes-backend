from django.urls import path
from .views import (
    EmployeeListView, 
    EmployeeCreateView, 
    EmployeeUpdateView, 
    EmployeeRetrieveView, 
    EmployeeDeleteView
)

urlpatterns = [
    path('', EmployeeListView.as_view()),  # Employees list
    path('create', EmployeeCreateView.as_view()),  # Create employee url
    path('<slug:slug>/', EmployeeRetrieveView.as_view()),  # Employee details
    path('<slug:slug>/update', EmployeeUpdateView.as_view()),  # Update employee
    path('<slug:slug>/delete', EmployeeDeleteView.as_view()),  # Delete employee
]
