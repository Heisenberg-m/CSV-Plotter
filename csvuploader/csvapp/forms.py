from django import forms
from .models import UploadedFile

class CSVUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
