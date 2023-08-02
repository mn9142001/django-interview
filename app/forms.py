from .models import Upload
from django import forms

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Upload
        exclude = ('ip', 'slug', 'user')