
from django import forms
from django.core import validators
from .models import Vehiculo
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'año',  'color', 'combustible']
        
        # Aplicar estilos Bootstrap a todos los campos
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Toyota, Ford, Chevrolet'
            })
        }
    

    
    def clean_marca(self):
        """Validación para marca: mínimo 2 caracteres"""
        marca = self.cleaned_data.get('marca')
        if len(marca) < 2:
            raise forms.ValidationError("La marca debe tener al menos 2 caracteres")
        return marca.title()  # Capitalizar primera letra
    
   