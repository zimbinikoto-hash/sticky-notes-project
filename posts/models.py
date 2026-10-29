
"""Models for bulletin board posts and their authors."""

from django.db import models


class Post(models.Model):
    """Represent a bulletin board post."""

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        """Return the title of the post."""
        return self.title


class Author(models.Model):
    """Represent the author of a bulletin board post."""

    name = models.CharField(max_length=255)

    def __str__(self):
        """Return the author's name."""
        return self.name
