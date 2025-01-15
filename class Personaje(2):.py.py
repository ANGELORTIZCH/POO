class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def dañar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        return max(daño, 0)  # Evita que el daño sea negativo

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
        if enemigo.vida <= 0:
            enemigo.morir()

# Variables del constructor
mi_personaje = Personaje("EstebanDido", 40, 50, 45, 100)
mi_enemigo = Personaje("Ángel", 70, 100, 70, 100)

mi_personaje.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
print(mi_personaje.esta_vivo())
