from django import forms
from .models import Note
import os

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title',  'subject', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            ext = os.path.splitext(file.name)[1]
            valid_extensions = ['.pdf','.docx']
            if not ext.lower() in valid_extensions:
                raise forms.ValidationError('Unsupported file extension. Allowed: PDF, DOCX.')
            return file
        else:
            raise forms.ValidationError("Couldn't read uploaded file")