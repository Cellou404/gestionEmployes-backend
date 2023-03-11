from rest_framework import serializers

from .models import Project, ProjectTask


# ================= Project Serializer ====================== #
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True) # This field will be filled automaticaly by
                                                 # the save method
    class Meta:
        model = Project
        fields = '__all__'
        lookup_field = 'slug'


# ================ ProjectTaskSerializer =================== #
class ProjectTaskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True) # This field will be filled automaticaly by
                                                 # the save method
    class Meta:
        model = ProjectTask
        fields = '__all__'
