# Importamos paquete open cv que hemos descargado e instalado previamente
import cv2
from PIL import Image
import re
from os import listdir
import streamlit as st

# Si no funciona es porque necesitas instalar la app tesseract-OCR que te adjunto en la carpeta
import pytesseract

# Aqui renompbramos la app con la direccion de instalacion
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Esta funcion recibe la ruta donde alojamos las imagenes y devuelve una lista de cada uno de los archivos
ruta = 'C:/Users/cucas/Documents/TRABAJO/App CuentaTickets/tickets'
def ls(ruta='.'):
    return listdir(ruta)

#Creamos un contador de tickets, un contador para el total y una lista con todos los tickets.
contador = 0
total = 0
listado_tickets = []

#Iteramos sobre cada uno de los archivos y extraemos el precio de cada ticket leyendo el texto con OCR y
# encontrando cada precio con una reguex. Una vez extraido lo pasamos a float para poder hacer operaciones.
for ticket in ls(ruta):
    image = cv2.imread(ruta + '/' + ticket)
    text = pytesseract.image_to_string(image, lang='spa')
    try:
        precio = re.findall('[\w]*\,[\w]*\ EUR', text)
        precio = precio[-1].split(' ')
        precio = float(precio[0].replace(',', '.'))
    except:
        print('No se ha podido leer el ticket')
    contador += 1
    total += precio
    listado_tickets.append(precio)

print('',contador, 'tickets','\n','Total:',total,'$','\n','Tickets:',listado_tickets)