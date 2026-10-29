

"""Register post-related models with the Django admin site."""

from django.contrib import admin
from .models import Post, Author

admin.site.register(Post)
admin.site.register(Author)

