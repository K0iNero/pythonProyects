# clase con una definicion para guardar los datos a traves de la request del usuario en la pagina, asi devolviendo los valores introducirlos y guardandolos en un archivo.
# cuando la request se completa con exito se le lleva al usuario a la pagina de exito con opcion de hacer otro formulario.

from django.shortcuts import render
from .forms import ContactoForm
import os

# Create your views here.

def guardar_datos(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            sexo = form.cleaned_data['sexo']
            descripcion = form.cleaned_data['descripcion']

            # Definir la ruta y guardar en el archivo .txt
            archivo_path = os.path.join('formularios_guardados', 'contactos.txt')

            # Asegurarse de que el directorio existe
            if not os.path.exists('formularios_guardados'):
                os.makedirs('formularios_guardados')

            with open(archivo_path, 'a') as archivo:
                archivo.write(f'Nombre: {nombre},\nCorreo: {correo},\nSexo: {sexo},\nDescripcion: {descripcion}\n\t\t------------------------------------------------------\n\n')

            # Redirigir o mostrar un mensaje de éxito
            return render(request, 'usuarios/exito.html')

    else:
        form = ContactoForm()

    return render(request, 'usuarios/formulario.html', {'form': form})

