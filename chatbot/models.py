from django.db import models

import os
import shutil

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
    
    def delete(self, *args, **kwargs):
        # Xóa tệp liên kết
        if self.document:
            self.document.delete(save=False)
        super().delete(*args, **kwargs)

class VectorDB(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vector_db_path = models.CharField(max_length=255, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Xóa các tệp và thư mục trong vector_db_path
        if self.vector_db_path and os.path.exists(self.vector_db_path):
            shutil.rmtree(self.vector_db_path)
            
        super().delete(*args, **kwargs)
    

class ChatSession(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id

class ChatMessage(models.Model):
    SESSION_CHOICES = [
        ('user', 'User'),
        ('bot', 'Bot'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=5, choices=SESSION_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content[:50]}"
