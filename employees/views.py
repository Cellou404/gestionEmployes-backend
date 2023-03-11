from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Employee
from .serializers import EmployeeSerializer


# =========== Employee Create & Listing View =========== #
class EmployeeListView(ListCreateAPIView):
    """
    Returns a list of all **employees** in the database.
    Create **employees** in the database.

    For listing [see here][ref].

    [ref]: http://localhost:8000/api/employees/

    For Creation [see here][ref].

    [ref]: http://localhost:8000/api/employees/#slug

    Replace #slug by an employee slug
    """
    permission_classes = (permissions.AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = None
    lookup_field = 'slug' # The lookup field is `slug` instead of `id`


# =========== Employee Actions (CRUD) View =========== #
class EmployeeView(RetrieveUpdateDestroyAPIView):
    """
    Display, Update and Delete a single **employee** from
    database

    For more details please [see here][ref].

    [ref]: http://localhost:8000/api/employees/
    """
    permission_classes = (permissions.AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'slug' # The lookup field is `slug` instead of `id`
