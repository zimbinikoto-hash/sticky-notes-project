from django.contrib import admin
from .models import StickyNote


@admin.register(StickyNote)
class StickyNoteAdmin(admin.ModelAdmin):
    """Configure how sticky notes appear in the Django admin."""

    list_display = ("title", "created_at")
    search_fields = ("title", "content")
