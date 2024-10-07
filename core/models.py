from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class AITool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Creation(models.Model):
    CREATION_TYPES = [
        ('APP', 'Application'),
        ('IMG', 'Image'),
        ('VID', 'Video'),
        ('AUD', 'Audio'),
        ('OTH', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_type = models.CharField(max_length=3, choices=CREATION_TYPES)
    content = models.FileField(upload_to='creations/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creations')
    tools_used = models.ManyToManyField(AITool, related_name='creations')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('creation_detail', args=[str(self.id)])

class Comment(models.Model):
    creation = models.ForeignKey(Creation, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.creation.title}"