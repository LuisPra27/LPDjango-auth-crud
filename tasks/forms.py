from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':'Escribe un Titulo'}),
            'Descripción': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder':'Escribe una descripción'}),
            'Importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }