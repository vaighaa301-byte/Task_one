from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('employee_id', 'name', 'department', 'designation', 'status')
	list_filter = ('status', 'department')
	search_fields = ('employee_id', 'name', 'email', 'department')
	ordering = ('name',)

# Register your models here.
