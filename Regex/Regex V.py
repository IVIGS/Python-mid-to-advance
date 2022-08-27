""" Grupos de regex y el caracter pipe
"""
import re

"""
Se pueden agrupar caracteres de busqueda como si fueran metodos para facilitar el trabajo.
Se crea una variable y se utiliza el metodo group de regex para poder hacer multiples busquedas
con distintas variables
"""
print(".:Metodo de agrupacion:.")
numero_de_telefono = re.compile(r"\d\d-\d\d-\d\d-\d\d-\d\d")

mi_numero = numero_de_telefono.search("Mi numero de telefono es: 55-22-28-41-63")
print(mi_numero.group())
"""
Cuando se quiere agrupar distintos terminos de busqueda se pueden añadir dentro de un
parentesis ej: (\d\d\d)
"""
print("\n.:Grupos: (\d\d\d):.")
numero_de_telefono = re.compile(r"(\d\d)-(\d\d)-(\d\d)-(\d\d)-(\d\d)")

mi_numero = numero_de_telefono.search("Mi numero de telefono es: 55-22-28-41-63")
print(mi_numero.group())

# Ademas se puede buscar entre los distintos grupos de busqueda como si se tratara de index
print("\n.:Index del grupo: group(1):.")
print(mi_numero.group(1))