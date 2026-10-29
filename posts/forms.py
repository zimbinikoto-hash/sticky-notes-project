
"""Forms for creating and updating posts."""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Provide a form for creating and updating Post objects."""

    class Meta:
        """Define the model and fields used by the post form."""

        model = Post
        fields = ["title", "content", "author"]
