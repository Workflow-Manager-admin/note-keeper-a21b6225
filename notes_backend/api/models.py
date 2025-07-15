from django.db import models

# PUBLIC_INTERFACE
class Note(models.Model):
    """
    Note model representing a note with a title, content, and timestamps.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # PUBLIC_INTERFACE
    def __str__(self):
        """Return string representation for admin."""
        return self.title
