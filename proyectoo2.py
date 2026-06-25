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

imagen_seleccionada = Image.open(imageness()) #abre la imagen elegida
pixeles_imagen = imagen_seleccionada.size #te calcula el tamañp




def fondos():
    carpeta_fondos = "Fondos"
    if not os.path.exists(carpeta_fondos):
        print("no se encontro la carpeta de los fondos, intente denuevo") #se busca la carpeta en el directorio
        return None
        
    fondosss = os.listdir(carpeta_fondos)
    buscar_fondos = []
    for archivo in fondosss:
        if archivo.lower().endswith(('.png', '.jpg')): #busca solo las imagenes en el directoriooo
            directorio = os.path.join(carpeta_fondos, archivo)
            buscar_fondos.append(directorio)
    if len(buscar_fondos) < 2:
        print("no hay fondos suficientes para iniciar el programa")
        return None
    return buscar_fondos[0], buscar_fondos[1] # guardo los fondos en la lista

fondo1, fondo2 = fondos()
imagen_f1 = Image.open(fondo1) # se cargan
imagen_f2 = Image.open(fondo2) # los 2 fondoossss

fondo1_redimensionado = imagen_f1.resize(pixeles_imagen)
fondo2_redimensionado = imagen_f2.resize(pixeles_imagen)



#______________________________________pasarlos a matrizzzzzzzzzzzzz_____________
matriz_imagenn = np.array(imagen_seleccionada) # la imagen q seleccionaron se pasa a matriz
matriz_fondo_uno = np.array(fondo1_redimensionado) # lo mismo con el fondo 1
matriz_fondo_dos = np.array(fondo2_redimensionado) # y con el fondo 2

def procesarrr():
