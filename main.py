class Player:

    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 1
        self.armadura = 0
        self.escudo = 0
        self.voluntad = 0
        self.nivel = 0
        self.experiencia = 0
        self.inventario = {
            'objeto1': 0,
            'objeto2': 0,
        }    

    def speek(self): #metodo
        print(f"he nacido {self.nombre}")
    
    def chechk_vida(self):
        print(f"vida {self.vida}")

    def chechk_vida(self):
        print(f"nombre {self.nombre}")
    def chechk_vida(self):
        print(f"vida {self.vida}")

    def chechk_vida(self):
        print(f"vida {self.vida}")

    def chechk_vida(self):
        print(f"vida {self.vida}")

    def check_inventario(self):
        #if else
        for objeto, cantidad in self.inventario.item():
            print(f" tengo: {objeto},{cantidad}")

    def check_sobrevive(self):
        if self.vida == 0:
            print("muerto")
        else:
                print("mal herido {self.vida}")

def check_daño(self):
        if self.daño == 0:
            print("daño")
        else:
                print("daño herido {self.vida}")


print("Bienvenidos a SpaceSurvive \n")

nombre = input("Introduzca su nombre:")

jugador = Player(nombre)
jugador.speek("hola")
print(jugador.vida)
print(jugador.check_inventario())
