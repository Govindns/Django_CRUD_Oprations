from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','no','name','sal','addr']
admin.site.register(Employee,EmployeeAdmin)
