
from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm


def sticky_note_list(request):
    notes = StickyNote.objects.all().order_by("-created_at")
    return render(
        request,
        "mbiracouture_app/sticky_notes.html",
        {"notes": notes},
    )


def sticky_note_create(request):
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sticky_note_list")
    else:
        form = StickyNoteForm()

    return render(
        request,
        "mbiracouture_app/sticky_note_form.html",
        {"form": form},
    )


def sticky_note_edit(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("sticky_note_list")
    else:
        form = StickyNoteForm(instance=note)

    return render(
        request,
        "mbiracouture_app/sticky_note_form.html",
        {"form": form, "note": note},
    )


def sticky_note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("sticky_note_list")

    return render(
        request,
        "mbiracouture_app/sticky_note_confirm_delete.html",
        {"note": note},
    )
