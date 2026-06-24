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
        if archivo.lower().endswith(('.png', '.jpg')): #muestra solo las q son imagenes
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
            opcion_num = int(opcion)
            
            if 1 <= opcion_num <= len(imagenes):
                imagen_seleccionada = imagenes[opcion_num - 1] 
                ruta_directorio = os.path.join(carpeta, imagen_seleccionada) #si esta en el rango correcto
                print(f"seleccionaste la opcion: {opcion_num} : {imagen_seleccionada}") #selecciona la imagen
                return ruta_directorio
            else:
                print(f"error, ingrese un numero correcto {len(imagenes)}.")
                
        except ValueError:
            print("ERROR, TIENE QUE INGRESAR UN NUMERO CORRECTO")

seleccionar = imageness()
imagen_lista = Image.open(seleccionar)

def fondos():
    carpeta_fondos = "Fondos"

    if not os.path.exists(carpeta_fondos):
        print("no se encontro la carpeta para ver los fondos, intentelo denuevo")
        return None
    archivos_fondos = os.listdir(carpeta_fondos)
    fondos = []
    for archivo in archivos_fondos:
        if archivo.lower().endswith(('.png', '.jpg')): #muestra solo las q son imagenes
            fondos.append(archivo)
            
    if len(fondos) == 0:
        print("No se encontraron imágenes válidas en la carpeta.") #si no hay imagenes tira errorr
        return None

    while True:
        print("fondos disponibles:")
        for i in range(len(fondos)):
            print(f"numero {i+1} : {fondos[i]}") #mostrar asi el menu
        try:
            opcion = input("ingrese la opcion que desea: ")
            numero_ingresado = int(opcion)
            
            if 1 <= numero_ingresado <= len(fondos):
                fondo_seleccionado = fondos[numero_ingresado - 1] 
                directorio_fondo = os.path.join(carpeta_fondos, fondo_seleccionado) 
                print(f"seleccionaste la opcion: {numero_ingresado} : {fondo_seleccionado}") 
                return directorio_fondo
            else:
                print(f"error, ingrese un numero correcto")
        except ValueError:
            print("ERROR, TIENE QUE INGRESAR UN NUMERO CORRECTO")

fondos()




tamaño = imagen_lista.size
print(f"el tamaño de tu imagen en pixles es: {tamaño}")
Image.open(seleccionar).show()
