"""
Metacaracteres (Caracteres comodin)
Anclas y clases de caracteres
"""
import re

lista_nombres = ["Ana Gómez",
                 "María Martín",
                 "Sandra López",
                 "Santiago Martín",
                 "Sandra Fernandez",
                 "Sandra Cabrera"]
"""
Esta forma nos regresa todas las cadenas que INICIEN con la cadena a buscar
Se usa el acento circunflejo ^
"""
print(".:Al inicio:.")
print('^')
for elemento in lista_nombres:
    if re.findall("^Sandra",elemento):
        print(elemento)
        
"""
Esta forma nos regresa todas las cadenas que TERMINEN con la cadena a buscar
Se usa el simbolo de dolar $
"""
print("\n.:Al final:.")
print('$')
for elemento in lista_nombres:
    if re.findall("Martín$",elemento):
        print(elemento)
        
lista_dominios = ["http://informaticaespaña.es",
                  "http://pildorasinformaticas.es",
                  "http://pildorasinformaticas.es"]

print("\n.:En algun lugar:.")
for elemento in lista_dominios:
    if re.findall("[ñ]", elemento):
        print(elemento)