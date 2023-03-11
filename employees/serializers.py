from rest_framework import serializers
from .models import Employee


# ===================== Employee Serializer =================== #
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee # The model that will be serialized
        fields = '__all__' # all fields will be serialized