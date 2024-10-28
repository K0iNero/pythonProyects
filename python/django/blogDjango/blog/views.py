from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
import os
import json
from datetime import datetime

# Ruta del archivo JSON
DATA_FILE = os.path.join(settings.BASE_DIR, 'blog_posts.json')

# Función para leer el archivo JSON
def leer_datos():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Función para escribir en el archivo JSON
def escribir_datos(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Vista para añadir una publicación
def agregar_publicacion(request):
    if request.method == 'POST':
        data = leer_datos()
        nueva_publicacion = {
            "id": len(data) + 1,
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
            "author": request.POST.get("author"),
            "date": timezone.now().strftime("%Y-%m-%d %H:%M:%S"),
            "comments": []  # Agregar campo comments como lista vacía
        }
        data.append(nueva_publicacion)
        escribir_datos(data)
        return redirect('/?success=true')
    return render(request, 'addPost.html')

# Vista para listar publicaciones en la página de inicio
def listar_publicaciones(request):
    publicaciones = leer_datos()
    
    # Función para convertir la fecha y ordenar en orden descendente
    def parse_fecha(fecha_str):
        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return datetime.strptime(fecha_str, "%Y-%m-%d")

    # Ordenar las publicaciones por fecha en orden inverso (más reciente primero)
    publicaciones = sorted(publicaciones, key=lambda x: parse_fecha(x["date"]), reverse=True)
    
    return render(request, 'blogInicio.html', {'publicaciones': publicaciones})

# Vista para ver una publicación individual y sus comentarios
def ver_publicacion(request, publicacion_id):
    publicaciones = leer_datos()
    publicacion = next((pub for pub in publicaciones if pub["id"] == publicacion_id), None)
    if publicacion is None:
        return JsonResponse({"error": "Publicación no encontrada"}, status=404)
    return render(request, 'verPublicacion.html', {'publicacion': publicacion})

# Vista para agregar un comentario a una publicación
def agregar_comentario(request, publicacion_id):
    if request.method == 'POST':
        publicaciones = leer_datos()
        publicacion = next((pub for pub in publicaciones if pub["id"] == publicacion_id), None)
        
        if publicacion is None:
            return JsonResponse({"error": "Publicación no encontrada"}, status=404)

        # Crear el nuevo comentario
        nuevo_comentario = {
            "id": len(publicacion["comments"]) + 1,
            "author": request.POST.get("author"),
            "content": request.POST.get("content"),
            "date": timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        publicacion["comments"].append(nuevo_comentario)
        
        # Guardar el archivo JSON actualizado
        escribir_datos(publicaciones)
        return redirect('ver_publicacion', publicacion_id=publicacion_id)
    return JsonResponse({"error": "Método no permitido"}, status=405)

