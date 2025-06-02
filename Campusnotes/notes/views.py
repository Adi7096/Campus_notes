from django.shortcuts import render, redirect
from .models import Note, Subject
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponseRedirect


def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.subject = note.subject
            note.uploaded_by = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/upload_note.html', {'form': form})
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    subject = request.GET.get('subject')
    if subject and subject.lower() != "all":
        notes = Note.objects.filter(subject__name__iexact=subject)
    else:
        notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})


def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.download_count += 1
    note.save()
    return HttpResponseRedirect(note.file.url)

