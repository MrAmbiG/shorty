from django.db import models


class shorties(models.Model):
    original = models.URLField(max_length=300)
    alias = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
