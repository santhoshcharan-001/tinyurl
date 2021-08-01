from django.db import models

# Create your models here.
class all_urls(models.Model):
    normal_url=models.URLField(max_length=1000)
    short_url=models.URLField(max_length=100)