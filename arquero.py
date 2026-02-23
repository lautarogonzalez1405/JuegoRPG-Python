from personaje import Personaje

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 90, ataque = 30, defensa = 20)
        self.flechas = 50
        print('Se ha creado un Arquero, aunque sus defensas sean bajas, sus ataques a distancia pueden ser devastadores')

    def dispararFlecha(self, objetivo):
        #Habilidad que permite al Arquero realizar un potente ataque a distancia
        if self.flechas <= 0:
            print('El arquero no tiene flechas para disparar')
            return
        danio = self.ataque * 1.5
        self.flechas -= 1
        print(f'{self.nombre} dispara una flecha!')
        objetivo.recibirDanio(danio)

    def mostrar_estado(self):
        print(f"Flechas restantes: {self.flechas}")
        return super().mostrar_estado()