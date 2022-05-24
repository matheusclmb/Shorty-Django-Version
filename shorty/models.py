from django.db import models


# Create your models here.
class Shortener(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    redirects = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_url
