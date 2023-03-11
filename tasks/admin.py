from django.contrib import admin

from .models import Task

# ====================== Task Admin ======================= #
@admin.register(Task)
class TaskAdmmin(admin.ModelAdmin):
    list_display = ('id','title', 'owner', 'complete', 'created')
    list_display_links = ('title', )
    list_filter = ('owner', )
    list_per_page = 15