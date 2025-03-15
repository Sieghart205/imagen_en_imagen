from stegano import lsb
import base64

imagen_a_mostrar = input("dame el nombre de la imagen que se verá: ")
imagen_a_ocultar = input("dame el nombre de la imagen a ocultar: ")
imagen_a_guardar = input("dame el nombre con el que se guardara la imagen generada: ")

with open(imagen_a_ocultar,"rb") as f:
  info = base64.b64encode(f.read()).decode("utf-8") 

lsb.hide(imagen_a_mostrar, info).save(imagen_a_guardar)