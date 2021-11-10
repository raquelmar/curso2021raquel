# -*- coding: iso-8859-1 -*-
import hashlib
# Se crea una variable con el fichero a ser usado para el hash
nombre = 'catalogo_cf.csv'
# Se convierte el formato a bytes usando 'encode'
# Las funciones hash solamente aceptan esta codificaci�n
nombre_codificado = nombre.encode()
# Se le pasa nombre_codificado a la funci�n sha512
nombre_hash = hashlib.sha512(nombre_codificado)
# Ya creado el hash, se imprime la versi�n hexadecimal del mismo usando el m�todo 'hexdigest()'
print("Object:", nombre_hash)
print("Hexadecimal format:", nombre_hash.hexdigest())