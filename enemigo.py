from personaje import Personaje
import random

class Enemigo(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 
                        vida = random.randint(50, 100), 
                        ataque = random.randint(10, 20), 
                        defensa = random.randint(5, 20)
                        )
