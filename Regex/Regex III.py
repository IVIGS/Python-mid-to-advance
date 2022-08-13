"""
Rangos

Los rangos nos permiten buscar elementos dentro de una lista que contengan por ejemplo un rango de caracteres, de numeros, que comiencen por un rango de caracteres o que terminen por un rango de caracteres
"""
import re

lista_nombres = ["Ana",
                               "Pedro",
                               "Marìa",
                               "Rosa",
                               "Sandra",
                               "Celia"]

print(".:Contiene una letra entre: [o-t]:.")
for elemento in lista_nombres:
    if re.findall("[o-t]", elemento):
        print(elemento)

print("\n.Empieza con una letra entre: ^[O-T]:.")
for elemento in lista_nombres:
    if re.findall("^[O-T]", elemento):
        print(elemento)

print("\n.:Termina con una letra entre: [o-t]$:.")
for elemento in lista_nombres:
    if re.findall("[o-t]$", elemento):
        print(elemento)
        
lista_pedidos = ["Ma1",
                               "Se1",
                               "Ma2",
                               "Ba1",
                               "Ma3",
                               "Va1",
                               "Va2",
                               "Ma4",
                               "MaA",
                               "Ma5",
                               "MaB",
                               "MaC"]

print("\n.:Termina en un rango de numero abc[0-3]:.")

for elemento in lista_pedidos:
    if re.findall("Ma[0-3]", elemento):
        print(elemento)

print("\n.:Negacion de la condicion abc[^0-3]:.")

for elemento in lista_pedidos:
    if re.findall("Ma[^0-3]", elemento):
        print(elemento)

print("\n.:Elementos con letras o numericos abc[A-C0-3]:.")

for elemento in lista_pedidos:
    if re.findall("Ma[A-C0-3]", elemento):
        print(elemento)
 
lista_pedidos = ["Ma.1",
                               "Se1",
                               "Ma.2",
                               "Ba1",
                               "Ma:3",
                               "Va1",
                               "Va2",
                               "Ma.4",
                               "MaA",
                               "Ma5",
                               "Ma.B",
                               "Ma:C"]

print("\n.:Elementos con caracteres especiales abc[.:]   :.")

for elemento in lista_pedidos:
    if re.findall("Ma[.:]", elemento):
        print(elemento)      