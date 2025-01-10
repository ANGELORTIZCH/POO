class personaje:
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
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defesa = self.defesa + defensa
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño 
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

#Variable del cosntructor vacío 
mi_personaje = personaje("EsteBandido", 100, 50, 45, 100)
mi_enemigo = personaje("Ángel", 70, 100, 40, 100)
mi_personaje.imprimir_atributos() 
mi_personaje.atacar(mi_enemigo)
print(mi_personaje.esta_vivo())