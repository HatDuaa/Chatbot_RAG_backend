from django.db import models

# Create your models here.
class api_key(models.Model):
    name = models.CharField(max_length=255, unique=True)
    key = models.TextField()
    
    def __str__(self):
        return self.name
    
class Document(models.Model):
    name = models.CharField(max_length=255, unique=True)
    document = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
