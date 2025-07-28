from django.db import models
from django.utils.text import slugify


# Create your models here.
class Task(models.Model):
    event_name = models.CharField(max_length = 250)
    event_detail = models.TextField(max_length = 1000)
    created_by = models.CharField(max_length = 100)
    event_time = models.TimeField(auto_now_add = True)
    event_date = models.DateField(auto_now_add = True)
    slug_link = models.SlugField(null = True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug_link:
            self.slug_link = slugify(self.event_name)
        super().save(*args, **kwargs)
        
    