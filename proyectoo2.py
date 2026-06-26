import numpy as np
import os
import matplotlib.pyplot as plt 
from PIL import Image
from datetime import datetime
from matplotlib.widgets import Button

#_______________________________para seleccionar las imagenes________________
def imageness():
    carpeta = "datos/imagenes"
    
    if not os.path.exists(carpeta):
        return "no se encontro la carpeta, intente denuevo"
    
    archivos = os.listdir(carpeta)
    imagenes = []
    
    for archivo in archivos:
        if archivo.lower().endswith(('.png', '.jpg')): #muestra solo las q son imagenes
            imagenes.append(archivo)
            
    if len(imagenes) == 0: #si no hay imagenes tira errorr
        return "No se encontraron imágenes válidas en la carpeta."

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
                return ruta_directorio
            else:
                print(f"error, ingrese un numero correcto {len(imagenes)}.")
                
        except ValueError:
            print("ERROR, TIENE QUE INGRESAR UN NUMERO CORRECTO")

def fondos():
    carpeta_fondos = "datos/fondos"

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

def guardar_imagen(matriz):
    nombre = "imagen_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".png"
    Image.fromarray(matriz.astype(np.uint8)).save(nombre)
    print(f"Guardada: {nombre}")

def reemplazar_fondo(img, fondo_nuevo, tolerancia=60):
    fondo = np.array(Image.fromarray(fondo_nuevo).resize((img.shape[1], img.shape[0])))

    esquina_superior = img[0, 0].astype(float)
    esquina_inferior = img[-1, 0].astype(float)

    color_fondo = (esquina_superior + esquina_inferior) / 2.0

    mascara = np.linalg.norm(img.astype(float) - color_fondo, axis=2) < tolerancia
    resultado = img.copy()
    resultado[mascara] = fondo[mascara]
    return resultado

img = np.array(Image.open(imageness()).convert("RGB"))
ruta_f1, ruta_f2 = fondos()
fondo1 = np.array(Image.open(ruta_f1).convert("RGB"))
fondo2 = np.array(Image.open(ruta_f2).convert("RGB"))

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
mostrar = ax.imshow(reemplazar_fondo(img, fondo2))
ax.axis("off")

ax_btn1 = plt.axes([0.25, 0.05, 0.2, 0.075])
btn1 = Button(ax_btn1, 'Fondo 1', color='lightblue', hovercolor='skyblue')

ax_btn2 = plt.axes([0.55, 0.05, 0.2, 0.075])
btn2 = Button(ax_btn2, 'Fondo 2', color='lightgreen', hovercolor='green')

def cambiar_a_fondo1(event):
    mostrar.set_data(reemplazar_fondo(img, fondo1))
    fig.canvas.draw_idle()

def cambiar_a_fondo2(event):
    mostrar.set_data(reemplazar_fondo(img, fondo2))
    fig.canvas.draw_idle()

btn1.on_clicked(cambiar_a_fondo1)
btn2.on_clicked(cambiar_a_fondo2)

plt.show()

