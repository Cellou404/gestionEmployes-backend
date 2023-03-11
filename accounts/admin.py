from django.contrib import admin

from .models import UserAccount

# =============== UserAccount Admin ========================= #
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('is_active', 'is_staff')
    list_per_page = 15
