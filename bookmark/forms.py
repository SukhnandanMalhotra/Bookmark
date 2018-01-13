from django import forms
from .models import Bookmark

class CreateBookmarkForm(forms.ModelForm):
    class Meta:
        model= Bookmark
        fields = ['name','url','tags', 'is_public']
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url' : forms.URLInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
        labels={
            'is_public':'Public'
        }
