import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    def atacar(self, objetivo):
        numero = random.randint(1, 6)
        ataque = self.ataque
        if numero == 6: #golpe critico
            ataque *= 2 
            print(f'{self.nombre} realiza un golpe critico!')

        objetivo.recibirDanio(ataque)
    
    def recibirDanio(self, danio):
        danioFinal = danio - self.defensa

        if danioFinal < 0:
            danioFinal = 0

        self.vida -= danioFinal
        print(f"{self.nombre} recibe {danioFinal} puntos de daño")
        

    def esta_vivo(self):
        return self.vida > 0
    
    def mostrar_estado(self):
        print(f'Vida del personaje: {self.vida}')
        print(f'Ataque del personaje: {self.ataque}')
        print(f'Defensa del personaje: {self.defensa}')
    
    def subirNivel(self):
        #TODO: Diferenciar por clases y subir mas unas caracteristicas que otras dependiendo del rol
        self.vida += 5
        self.ataque += 5
        self.defensa += 5
