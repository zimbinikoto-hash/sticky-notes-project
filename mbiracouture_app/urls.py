
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sticky_note_list, name="sticky_note_list"),
    path("new/", views.sticky_note_create, name="sticky_note_create"),
    path("<int:pk>/edit/", views.sticky_note_edit, name="sticky_note_edit"),
]
