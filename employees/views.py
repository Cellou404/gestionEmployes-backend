from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsStaff


# =========== Employee Create & Listing View =========== #
class EmployeeListView(generics.ListAPIView):
    """
    Returns a list of all **employees** in the database.

    For listing [see here][ref].

    [ref]: http://localhost:8000/api/employees

    """
    permission_classes = [IsAuthenticated | IsStaff]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = None

# =========== Employee Create & Listing View =========== #
class EmployeeCreateView(generics.CreateAPIView):
    """
    Create **employees** in the database.

    For Creation [see here][ref].

    [ref]: http://localhost:8000/api/employees/create

    """
    permission_classes = [IsStaff]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# =========== Employee Retrieve View =========== #
class EmployeeRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve **employee** from
    database

    For more details please [see here][ref].

    [ref]: http://localhost:8000/api/employees/slug

    Replace #slug by an employee slug
    """
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'slug' # The lookup field is `slug` instead of `id`


# =========== Employee Update View =========== #
class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    """
    Display, Update a single **employee** from
    database

    For more details please [see here][ref].

    [ref]: http://localhost:8000/api/employees/slug/update

    Replace #slug by an employee slug
    """
    permission_classes = [IsStaff | IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'slug' # The lookup field is `slug` instead of `id`


# =========== Employee Delete View =========== #
class EmployeeDeleteView(generics.RetrieveDestroyAPIView):
    """
    Delete a single **employee** from
    database

    For more details please [see here][ref].

    [ref]: http://localhost:8000/api/employees/slug/delete

    Replace #slug by an employee slug
    """
    permission_classes = [IsStaff | IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'slug' # The lookup field is `slug` instead of `id`
