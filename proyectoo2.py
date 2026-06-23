from PIL.Image import Image
import numpy as np
import os
import PIL
import matplotlib.pyplot as plt 
from PIL import Image
#_______________________________para seleccionar las imagenes________________
def imageness():
    carpeta = "Objetos"
    
    if not os.path.exists(carpeta):
        print("no se encontro la carpeta, intente denuevo")
        return None
    
    archivos = os.listdir(carpeta)
    imagenes = []
    for archivo in archivos:
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg')): #muestra solo las q son imagenes
            imagenes.append(archivo)
            
    if len(imagenes) == 0:
        print("No se encontraron imágenes válidas en la carpeta.") #si no hay imagenes tira errorr
        return None

    while True:
        print("imagenes disponibles:")
        for i in range(len(imagenes)):
            print(f"numero {i+1} : {imagenes[i]}") #mostrar asi el menu
        try:
            opcion = input("ingrese la opcion que desea: ")
            numerooo = int(opcion)
            
            if 1 <= numerooo <= len(imagenes):
                imagen_seleccionada = imagenes[numerooo - 1] 
                ruta_goti = os.path.join(carpeta, imagen_seleccionada) #si esta en el rango correcto
                print(f"seleccionaste la opcion: {numerooo} : {imagen_seleccionada}") #selecciona la imagen
                return ruta_goti
            else:
                print(f"error, ingrese un numero correcto {len(imagenes)}.")
                
        except ValueError:
            print("ERROR, TIENE QUE INGRESAR UN NUMERO CORRECTO")

seleccionar = imageness()

imagen_lista = Image.open(seleccionar)

tamaño = imagen_lista.size



print(f"el tamaño es: {tamaño}")
Image.open(seleccionar).show()
