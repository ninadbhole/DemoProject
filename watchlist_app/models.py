from django.db import models

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title
