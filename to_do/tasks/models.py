"""DJango models."""
from django.db import models


class Task(models.Model):
    """Task model."""

    task = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """Return string."""
        return self.task

