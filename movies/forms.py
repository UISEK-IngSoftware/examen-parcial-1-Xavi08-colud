from django import forms 
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'genre', 'duration', 'cost', 'picture']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Pelicula'}),
            'genre' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Gnero de la Pelicula'}),
            'duration' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'cost' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class' : 'form-control', 'id' : 'image_field'}),
        }
    