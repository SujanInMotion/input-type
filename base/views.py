from django.shortcuts import render
from .models import Note, NoteType

# Create your views here.

def home(request):
    note_objs = Note.objects.all()
    data = {"notes":note_objs}
    print(request)
    return render(request, "index.html", context=data)

def note_type(request):
    note_objs = Note.objects.all()
    data = {"notes":note_objs}
    return render(request, "type.html", context=data)