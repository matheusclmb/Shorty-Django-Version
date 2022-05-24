from django.db import models


# Create your models here.
class Shortener(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=6, unique=True)
    startDate = models.DateTimeField(auto_now_add=True)
    lastSeenDate = models.DateTimeField(auto_now=True)
    redirectCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_url
