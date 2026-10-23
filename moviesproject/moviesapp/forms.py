from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image_url']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image_url': 'Image URL',
        }
