from django.db import models

class Video(models.Model):
    file_path = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)