from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True) # This field will be filled automaticaly by
                                                 # the save method
    class Meta:
        model = Task 
        fields = '__all__'
        lookup_field = 'slug'