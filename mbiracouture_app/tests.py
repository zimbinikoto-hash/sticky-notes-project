
"""Tests for the Sticky Notes application."""

from django.test import TestCase
from django.urls import reverse

from .models import StickyNote
from .forms import StickyNoteForm


class StickyNoteModelTests(TestCase):
    """Test the StickyNote model."""

    def test_create_sticky_note(self):
        """Check that a sticky note is saved correctly."""
        note = StickyNote.objects.create(
            title="My first note",
            content="This is my note content."
        )

        self.assertEqual(note.title, "My first note")
        self.assertEqual(note.content, "This is my note content.")
        self.assertEqual(StickyNote.objects.count(), 1)

    def test_sticky_note_string_representation(self):
        """Check that the note title is returned as its string representation."""
        note = StickyNote.objects.create(
            title="Shopping list",
            content="Buy groceries."
        )

        self.assertEqual(str(note), "Shopping list")


class StickyNoteFormTests(TestCase):
    """Test the StickyNote form."""

    def test_valid_form(self):
        """Check that the form accepts valid information."""
        form = StickyNoteForm(data={
            "title": "Study notes",
            "content": "Complete Django testing."
        })

        self.assertTrue(form.is_valid())

    def test_invalid_form_without_title(self):
        """Check that the form rejects a note without a title."""
        form = StickyNoteForm(data={
            "title": "",
            "content": "Some note content."
        })

        self.assertFalse(form.is_valid())


class StickyNoteViewTests(TestCase):
    """Test the StickyNote views."""

    def setUp(self):
        """Create a note for use in view tests."""
        self.note = StickyNote.objects.create(
            title="Test note",
            content="Original content."
        )

    def test_sticky_note_list(self):
        """Check that the notes page displays saved notes."""
        response = self.client.get(reverse("sticky_note_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test note")

    def test_sticky_note_create(self):
        """Check that a user can create a sticky note."""
        response = self.client.post(
            reverse("sticky_note_create"),
            {
                "title": "New note",
                "content": "New note content."
            }
        )

        self.assertRedirects(
            response,
            reverse("sticky_note_list")
        )
        self.assertTrue(
            StickyNote.objects.filter(title="New note").exists()
        )

    def test_sticky_note_edit(self):
        """Check that a user can update an existing note."""
        response = self.client.post(
            reverse("sticky_note_edit", args=[self.note.pk]),
            {
                "title": "Updated note",
                "content": "Updated content."
            }
        )

        self.assertRedirects(
            response,
            reverse("sticky_note_list")
        )

        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated note")
        self.assertEqual(self.note.content, "Updated content.")

    def test_sticky_note_delete(self):
        """Check that a user can delete a sticky note."""
        response = self.client.post(
            reverse("sticky_note_delete", args=[self.note.pk])
        )

        self.assertRedirects(
            response,
            reverse("sticky_note_list")
        )
        self.assertFalse(
            StickyNote.objects.filter(pk=self.note.pk).exists()
        )
