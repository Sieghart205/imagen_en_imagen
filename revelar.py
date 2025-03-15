from stegano import lsb
import base64

imagen_con_secreto = input("dame el nombre de la imagen: ")

secreto_revelado = lsb.reveal(imagen_con_secreto)

secreto_bytes = base64.b64decode(secreto_revelado.encode('utf-8'))

with open("secreta_revelada.png", "wb") as f:
    f.write(secreto_bytes)