from django.contrib import admin

from .models import Employee

# ====================== Employee Admin ================= #
class EmployeeAdmin(admin.ModelAdmin):
    """
        Register the Model in the Django Admin template
    """
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 15 # 15 items will be shown first

admin.site.register(Employee, EmployeeAdmin)