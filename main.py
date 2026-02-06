from personaje import Personaje
from guerrero import Guerrero
from mago import Mago
from enemigo import Enemigo
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

def generarEnemigo():
    enemigo = Enemigo(random.choice(nombres_enemigos))
    return enemigo

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

enemigo = generarEnemigo()

while jugador.esta_vivo() and enemigo.esta_vivo():
    if eleccion == 1:
        print("Que movimiento deseas realizar?")
        print("1. Ataque simple")
        print("2. Ataque pesado")
        print("3. Alzar escudo")
        movimiento = int(input('Elije tu movimiento: '))
        while movimiento not in (1, 2, 3):
            print('Has elejido un movimiento invalido, por favor vuelva a seleccionar un movimiento')
            movimiento = int(input('Elije tu movimiento: '))
            continue
        if movimiento == 1:
            jugador.atacar(enemigo)
            print(f'El enemigo tiene ahora {enemigo.vida} puntos de vida')
            pausar()
            enemigo.atacar(jugador)
            print(f'El jugador tiene ahora {jugador.vida} puntos de vida')
            pausar()
        elif movimiento == 2:
            jugador.ataquePesado(enemigo)
            print(f'El enemigo tiene ahora {enemigo.vida} puntos de vida')
            pausar()
            enemigo.atacar(jugador)
            print(f'El jugador tiene ahora {jugador.vida} puntos de vida')
            pausar()
        else:
            jugador.alzarEscudo()
            pausar()
            enemigo.atacar(jugador)
            print(f'El jugador tiene ahora {jugador.vida} puntos de vida')
            pausar()
    
    if eleccion == 2:
        print("Que movimiento deseas realizar?")
        print("1. Ataque simple")
        print("2. Bola de fuego")
        movimiento = int(input('Elije tu movimiento: '))
        while movimiento not in (1, 2):
            print('Has elejido un movimiento invalido, por favor vuelva a seleccionar un movimiento')
            movimiento = int(input('Elije tu movimiento: '))
            continue
        if movimiento == 1:
            jugador.atacar(enemigo)
            print(f'El enemigo tiene ahora {enemigo.vida} puntos de vida')
            pausar()
            enemigo.atacar(jugador)
            print(f'El jugador tiene ahora {jugador.vida} puntos de vida')
            pausar()
        else:
            jugador.bolaDeFuego(enemigo)
            print(f'El enemigo tiene ahora {enemigo.vida} puntos de vida')
            pausar()
            enemigo.atacar(jugador)
            print(f'El jugador tiene ahora {jugador.vida} puntos de vida')
            pausar()