"""
'Expresiones regulares o regex'

¿Que son?
Son una secuencia de caracteres que forman un patron de busqueda

¿Para que sirven?
Para el trabajao y procesamiento de texto

Ejemplos:
Buscar un texto que se ajusta a un formato determinado (Correo electronico)
Buscar si existe o no una cadena de caracteres dentro de un texto
Contar el numero de coincidencias dentro de un texto
Etc.

"""

import re

texto1 = "Vamos a aprender expresiones regulares"
print(".:Metodo search:.")
"""
Nos devuelve un objeto con el indice de inicio y final donde encontro la cadena
"""
print(re.search("aprender", texto1))


texto2 = "Vamos a aprender expresiones regulares, donde vamos a aprender muchas cosas"
buscar = "aprender"
print("\n.:Metodo findall:.")
"""
Devuelve una lista con todas las cadenas encontradas
"""
texto_encontrado = re.findall(buscar,texto2)

print(texto_encontrado)