import uuid
from django.db import models
from django.utils.text import slugify


# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    name = models.CharField(max_length=50,blank=False)
    descripcion = models.TextField(blank=False, null=False)
    imagen = models.URLField(blank=False)
    slug = models.SlugField(unique=True, max_length=255,blank=True)
    is_private = models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    

