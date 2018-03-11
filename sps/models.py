from django.db import models
from django.http import JsonResponse

# Create your models here.
class Sps(models.Model):
    song = models.CharField(max_length=40)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s : %s' % (self.song, self.content)