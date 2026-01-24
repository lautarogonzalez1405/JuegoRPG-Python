from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
import random

def pausar():
    input('\nPresiona ENTER para continuar...')

nombres_enemigos = [
    "Gorath",
    "Malrik",
    "Zharok",
    "Thorgun",
    "Varkun",
    "Drevik",
    "Karnoth",
    "Ulgrim",
    "Rhazak",
    "Mordrek",
    "Skarn",
    "Brakthar",
    "Noktar",
    "Zolmar",
    "Kraven",
    "Drath",
    "Vorgrim",
    "Azgoth",
    "Belrak",
    "Xarnok"
]

print('============================')
print("Bienvenido a mi juego RPG")
print('============================')
print('Este es un juego basico en donde podras crear un personaje en base a una clase')
print('y tener batallas contra enemigos.')
print('Espero que disfrutes este proyecto y te diviertas!')
pausar()
print('Con que tipo de personaje te gustaria comenzar tu aventura?')
print('1. Guerrero')
print('2. Mago')
print('3. Arquero') #TODO: Desarrollar personaje Arquero
eleccion = int(input('Selecciona el numero de personaje: '))
while eleccion not in (1, 2, 3):
    print('Por favor, selecciona una opcion valida para crear un personaje')
    eleccion = int(input('Selecciona el numero de personaje: '))
    continue
if eleccion == 1:
    nombre = input('Genial! Como se llamara tu guerrero?:')
    jugador = Guerrero(nombre)
elif eleccion == 2:
    nombre = input('Genial! Como se llamara tu Mago?:')
    jugador = Mago(nombre)
#TODO: Una vez creado el Arquero implementar un else para crear un Arquero

