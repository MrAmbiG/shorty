from django.db import models
import uuid
LENGTH = 5

letters = ['a', 'c', 'd', 'e', 'g', 'i', 'k', 'l',
           'm', 'n', 'q', 'r', 's', 't', 'u', 'x', 'y', 'z', '2', '3', '4', '5', '6', '7', '8', '9']


class shorties(models.Model):
    original = models.URLField(max_length=300)
    alias = models.CharField(
        max_length=LENGTH,
        editable=True,
        unique=True,
        # default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    https = models.BooleanField(blank=False, default=False)
