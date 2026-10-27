
from django import forms
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter your note title",
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Write your sticky note here...",
                "rows": 4,
            }),
        }