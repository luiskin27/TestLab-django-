from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    author = models.CharField(max_length=100, default='Ivanov Ivan')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title