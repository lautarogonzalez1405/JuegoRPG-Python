from personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 150, ataque = 15, defensa = 30)
        self.bloqueo = False
        print('Se ha creado un guerrero, un personaje que aunque no cuenta con un gran nivel de ataque cuenta con una defensa ferrea')

    def alzarEscudo(self):
        #Una habilidad la cual permite al guerrero alzar su escudo en combate y mitigar un porcentaje del daño recibido en el proximo turno
        self.bloqueo = True
        print('El guerrero alza su escudo, preparado para recibir el ataque de lleno')

    def ataquePesado(self, objetivo):
        #Habilidad que permite al guerrero realizar un potente ataque pesado
        danio = self.ataque * 1.8
        objetivo.recibirDanio(danio)

    def recibirDanio(self, danio):
        if self.bloqueo:
            danio = 0
            super().recibirDanio(danio)
            self.bloqueo = False
        super().recibirDanio(danio)