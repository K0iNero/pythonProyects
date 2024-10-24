#Programa CRUD de contactos sobre un json

import json
import os

#Clase contacto
class Contacto:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

#Clase para el acceso a la información
class Acceso:
    # Obtener la ruta absoluta del script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(ruta_actual, 'contactos.json')

    def getListaContactos(self):
        # Leer el archivo JSON
        with open(self.ruta_json, 'r') as archivo:
            datos = json.load(archivo)  # Cargar el contenido del archivo

        # Extraer la lista de contactos
        contactos = datos['contactos']  
        lista_contactos = []

        # Crear objetos Contacto a partir de los datos
        for c in contactos:
            contacto = Contacto(c['nombre'], c['apellido'], c['email'], c['telefono'])
            lista_contactos.append(contacto)

        return lista_contactos
    
    def imprimirContactosLinea(self, lista_contactos):
        for contacto in lista_contactos:
            # Imprimir los datos de cada contacto en una sola línea
            linea = f"{contacto.nombre}, {contacto.apellido}, {contacto.email}, {contacto.telefono}"
            print(linea)


    def getContacto(self, telefono, contactos):
        # Buscar el contacto por teléfono
        for contacto in contactos:
            if contacto.telefono == telefono:
                return contacto  # Retorna el objeto Contacto si se encuentra

        return None  # Retorna None si no se encuentra el contacto
    
    
    def guardarContactos(self, lista_contactos):
        # Convertir objetos Contacto en un formato serializable
        contactos_json = [{
            'nombre': c.nombre,
            'apellido': c.apellido,
            'email': c.email,
            'telefono': c.telefono
        } for c in lista_contactos]

        # Guardar la lista de contactos en el archivo JSON
        with open(self.ruta_json, 'w') as archivo:
            json.dump({'contactos': contactos_json}, archivo, indent=4)
        

    def modificarContacto(self, telefono, nuevos_datos, contactos):
        # Buscar contacto por teléfono y modificar sus datos
        for contacto in contactos:
            if contacto.telefono == telefono:
                contacto.nombre = nuevos_datos.get('nombre', contacto.nombre)
                contacto.apellido = nuevos_datos.get('apellido', contacto.apellido)
                contacto.email = nuevos_datos.get('email', contacto.email)
                contacto.telefono = nuevos_datos.get('telefono', contacto.telefono)

                self.guardarContactos(contactos)  # Guardar la lista actualizada en el archivo JSON
                return True  # Si se encuentra y modifica el contacto
        return False  # Si no se encuentra el contacto
    

    def eliminarContacto(self, telefono, contactos):
        # Buscar y eliminar contacto por teléfono
        for contacto in contactos:
            if contacto.telefono == telefono:
                contactos.remove(contacto)
                self.guardarContactos(contactos)  # Guardar la lista actualizada en el archivo JSON
                return True  # Si se encuentra y elimina el contacto
        return False  # Si no se encuentra el contacto
    

# Función principal
def main():
    acceso = Acceso()
    contactos = acceso.getListaContactos()

    print("Bienvenido al gestor de contactos. Aquí te muestro todos los contactos:", )
    print()
    acceso.imprimirContactosLinea(contactos)
    print()
    print("--- Menú ---", 
                "1- Añadir contacto.",
                "2- Modificar contacto.",
                "3- Eliminar contacto.",
                "4- Consultar contacto.",
                "5- Mostrar todos los contactos.",
                "0- Salir.",
                sep="\n")

    try:
        opcion = int(input("Selecciona una opcion: "))
        print()

        if opcion == 1:
            # Añadir contacto
            print("Has seleccionado añadir contacto.")
            nombre = input("Introduce un nombre: ")
            apellido = input("Introduce un apellido: ")
            email = input("Introduce un email: ")
            telefono = input("Introduce un telefono: ")
            nuevo_contacto = Contacto(nombre, apellido, email, telefono)
            contactos.append(nuevo_contacto)
            acceso.guardarContactos(contactos)
            print("Contacto añadido.")

        elif opcion == 2:
            # Modificar contacto
            telefono = input("Introduce el teléfono del contacto a modificar: ")
            contacto = acceso.getContacto(telefono, contactos)
            if contacto:
                nuevos_datos = {
                    'nombre': input(f"Introduce el nuevo nombre (anterior: {contacto.nombre}): ") or contacto.nombre,
                    'apellido': input(f"Introduce el nuevo apellido (anterior: {contacto.apellido}): ") or contacto.apellido,
                    'email': input(f"Introduce el nuevo email (anterior: {contacto.email}): ") or contacto.email,
                    'telefono': input(f"Introduce el nuevo teléfono (anterior: {contacto.telefono}): ") or contacto.telefono
                }
                acceso.modificarContacto(telefono, nuevos_datos, contactos)
                print("Contacto modificado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == 3:
            # Eliminar contacto
            telefono = input("Introduce el teléfono del contacto a eliminar: ")
            if acceso.eliminarContacto(telefono, contactos):
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")

        elif opcion == 4:
            # Consultar contacto
            telefono = input("Introduce el teléfono del contacto a consultar: ")
            contacto = acceso.getContacto(telefono, contactos)
            if contacto:
                print(f"Nombre: {contacto.nombre}, Apellido: {contacto.apellido}, Email: {contacto.email}, Teléfono: {contacto.telefono}")
            else:
                print("Contacto no encontrado.")

        elif opcion == 5:
            # Mostrar todos los contactos
            if contactos:
                for contacto in contactos:
                    print(f"Nombre: {contacto.nombre}, Apellido: {contacto.apellido}, Email: {contacto.email}, Teléfono: {contacto.telefono}")
            else:
                print("No hay contactos para mostrar.")

        elif opcion == 0:
            # Salir del programa
            print("Saliendo del programa...")

        else:
            print("Opción no válida. Selecciona una de las opciones dadas.")

    except ValueError:
        print("Introduce un valor numérico válido.")


if __name__ == "__main__":
    main()