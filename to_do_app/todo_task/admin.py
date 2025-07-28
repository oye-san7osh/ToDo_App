from django.contrib import admin
from . models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("event_name", "created_by", "event_date")
    prepopulated_fields = {"slug_link": ("event_name",)}
    
    
admin.site.site_header = "To-Do Admin Panel"
admin.site.site_title = "To-Do Admin"
admin.site.index_title = "Welcome to the Task Dashboard"    
    

# Register your models here.
admin.site.register(Task, TaskAdmin)


