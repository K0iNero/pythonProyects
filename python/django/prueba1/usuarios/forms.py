# clase utilizada para el formulario que se muestra en pantalla

from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=20, label='Nombre')
    correo = forms.EmailField(max_length=30, label='Correo Electrónico')
    SEXO_OPCIONES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    ]
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES, label='Sexo', )
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
