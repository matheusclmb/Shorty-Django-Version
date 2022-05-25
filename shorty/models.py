from django.db import models
from utils.shorty.factory import create_short_url


# Create your models here.
class Shortener(models.Model):
    startDate = models.DateTimeField(auto_now_add=True)
    lastSeenDate = models.DateTimeField(auto_now=True)
    redirectCount = models.PositiveIntegerField(default=0)
    url = models.URLField()
    shortcode = models.CharField(max_length=6, unique=True, blank=True)

    class Meta:
        ordering = ["-startDate"]

    def __str__(self):
        return f"{self.url} to {self.shortcode}"

    def save(self, *args, **kwargs):

        if not self.shortcode:
            self.shortcode = create_short_url(self)

        super().save(*args, **kwargs)
