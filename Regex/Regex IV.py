"""
Match and Search
Ambas son funciones de busqueda en el modulo regex.
Match solo busca al principio de una string y retorna el objeto si lo encuentra.
Search busca en toda la string incluso si contiene multilineas hasta encontrar o no el objeto deseado
"""
import re

lista_cadenas = ["Estamos aprendiendo regex con python, regex es una herramienta muy util para la busqueda de cadenas, ademas es muy util", "cadenas Estamos aprendiendo regex con python, regex es una herramienta muy util para la busqueda de subcadenas, ademas es muy util" ]

print(".:Match:.")

for elemento in lista_cadenas:
    if re.match("cadena", elemento):
        print(f"{elemento}\n\nSe encuentra en el index: {lista_cadenas.index(elemento)} de la lista")

print("\n.:Search:.")
for elemento in lista_cadenas:
    if re.search("cadena", elemento):
        print(f"\nSe encuentra en el index: {lista_cadenas.index(elemento)} de la lista")
