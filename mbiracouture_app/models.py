
from django.db import models


class StickyNote(models.Model):
    """Represent a sticky note stored in the database."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the title of the sticky note."""
        return self.title
