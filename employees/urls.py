from django.urls import path
from .views import EmployeeListView, EmployeeView

urlpatterns = [
    path('', EmployeeListView.as_view()), # Path that will display Employees list
    path('<slug:slug>', EmployeeView.as_view()), # This path is used for **rud** actions for
                                                 # a particular employee
]