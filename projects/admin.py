from django.contrib import admin

from .models import Project, ProjectTask

# ================ Project Admin ====================== #
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'complete', 'created')
    list_display_links = ('id', 'title')
    list_filter = ('complete', 'created', 'owner')
    list_per_page =  15


# ================ ProjectTask Admin ====================== #
@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'project', 'complete', 'created')
    list_display_links = ('id', 'task_name')
    list_filter = ('complete', 'created', 'project')
    list_per_page =  15