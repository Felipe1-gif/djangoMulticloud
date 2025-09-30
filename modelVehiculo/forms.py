from django import forms
from django.core import validators
from modelVehiculo.models import Vehiculo
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'año', 'precio', 'color', 'tipo_combustible']
        
        # Aplicar estilos Bootstrap a todos los campos
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Toyota, Ford, Chevrolet'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Corolla, Mustang, Camaro'
            }),

            'patente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: ABCD12',
                'style': 'text-transform: uppercase;'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 15000000',
                'step': '0.01'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Rojo, Azul, Negro'
            }),
            'tipo_combustible': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
    
