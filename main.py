# This file holds code to program the player of the game
#
#

class Player:

    def __init__(self, name):
        self.name = name
        self.vida = 1

        self.armadura = 0
        self.escudo = 0
        self.voluntad = 0

        self.inventario = {
            "Objeto_1": 0,
            "Objeto_2": 4
        }

        self.nivel = 0
        self.experiencia = 0
        self.criterio_subida_nivel = 10

    def speak(self):
        print(f"Hola, me llamo {self.name}")

    def check_vida(self):
        print(f"La vida actual es {self.vida}")

    def check_armadura(self):
        print(f"La armadura actual es {self.armadura}")

    def check_escudo(self):
        print(f"El escudo actual es {self.escudo}")

    def check_voluntad(self):
        print(f"La voluntad actual es {self.voluntad}")

    def check_nivel(self):
        print(f"El nivel actual es {self.nivel}")

    def check_xp(self):
        print(f"La experiencia actual es {self.experiencia}")

    def check_inventario(self):
        if self.inventario == {}:
            print("El inventario está vacío :(")

        else:
            for objeto, cantidad in self.inventario.items():
                print(f"Tengo del objeto {objeto}, {cantidad} unidades")

    def check_sobrevive(self):
        if self.vida == 0:
            print(f"Game Over, {self.name} ha sido derrotado")
        else:
            print(f"Aún te quedan {self.vida} puntos de vida, sigue aguantando")

    def daño(self, daño, tipo):
        print(f"{self.name} ha recibido {daño} puntos de daño {tipo}")

        if tipo == "fisico":
            self.vida -= daño - self.armadura
        elif tipo == "energía":
            self.vida -= daño - self.escudo
        elif tipo == "psíquico":
            self.vida -= daño - self.voluntad
        else:
            print("Ese tipo de daño no está contemplado")

    def gain_exp(self, exp):
        self.experiencia += exp
        if self.experiencia >= self.criterio_subida_nivel:
            self.lvl_up()

    def lvl_up(self):
        """
        Esta clase aumenta el nivel de nuestro personaje y además actualiza el criterio para el siguiente nivel
        :return:
        """
        #TODO: Aquí implementamos una escalada de nivel donde el requisito de experiencia escala según la secuencia de fibonacci
        pass

    def check_all(self):
        self.speak()
        self.check_nivel()
        self.check_vida()
        self.check_inventario()
        self.check_sobrevive()
        self.daño(1, "fisico") #BUG:,#FIXME: 
        self.check_sobrevive()


print("Bienvenido a la Alfa de SpaceSurvive!!")
print()

name = input("Introduzca su nombre de jugador: ")

jugador = Player(name)

jugador.check_all()

jugador.daño(2, "fisico") #FIXME: