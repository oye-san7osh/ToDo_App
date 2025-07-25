from django.contrib import admin
from . models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "event_name", "created_by", "event_date"] # show these fields in the list
    list_filter = ("event_name",) # add sidebar filter
    search_fields = ("title", "created_by", "event_date",) # add search bar
    ordering = ("-event_date",) # ordering the item
    date_hierarchy = 'event_date' # add navigation by date
    list_editable = ("event_name",) # editable fields in list view
    list_display_links = ("id",)
    prepopulated_fields = {"slug_link" : ("event_name",)}
    # auto fill slug from event_name
    readonly_fields = ("event_time", "event_date")

admin.site.site_header = "To-Do Admin Panel"
admin.site.site_title = "To-Do Admin"
admin.site.index_title = "Welcome to the Task Dashboard"    
    

# Register your models here.
admin.site.register(Task, TaskAdmin)


