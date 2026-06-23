import numpy as np
import os
import PIL
import matplotlib.pyplot as plt 

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
            opcion_num = int(opcion)
            
            if 1 <= opcion_num <= len(imagenes):
                imagen_seleccionada = imagenes[opcion_num - 1] 
                ruta_completa = os.path.join(carpeta, imagen_seleccionada) #si esta en el rango correcto
                print(f"seleccionaste: {imagen_seleccionada}") #selecciona la imagen
                return ruta_completa
            else:
                print(f"error, ingrese un numero correcto {len(imagenes)}.")
                
        except ValueError:
            print("ERROR, TIENE QUE INGRESAR UN NUMERO CORRECTO")

seleccionar = imageness()
