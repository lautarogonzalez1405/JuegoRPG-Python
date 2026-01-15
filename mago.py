from personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 83, ataque = 36, defensa = 14)
        self.mana = 200
        print('Se ha creado un Mago, aunque sus defensas sean bajas, sus ataques magicos devastaran a los enemigos')

    def bolaDeFuego(self, objetivo):
        #Habilidad que permite al Mago realizar un potente hechizo
        danio = self.ataque * 1.83
        self.mana = self.mana - 40
        print('El mago lanza su potente bola de fuego!')
        objetivo.recibirDanio(danio)