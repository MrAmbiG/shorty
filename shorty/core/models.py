from django.db import models



class shorties(models.Model):
    original = models.URLField(max_length=300)
    alias = models.CharField(max_length=108)
