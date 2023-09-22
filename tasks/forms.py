from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Titulo','Descripcion','Importante']
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':'Escribe un Titulo'}),
            'Description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder':'Escribe una descripcion'}),
            'Importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }