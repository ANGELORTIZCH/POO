class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida


    def imprimir_atributos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Fuerza: {self.__fuerza}")
        print(f"Inteligencia: {self.__inteligencia}")
        print(f"Defensa: {self.__defensa}")
        print(f"Vida: {self.__vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.defesa = self.defesa + defensa
    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(f"{self.__nombre} ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        if daño < 0:
            daño = 0
        if enemigo.__vida - daño < 0:
            enemigo.__vida = 0
        else:
         enemigo.__vida = enemigo.__vida - daño 
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)

    def get_vida(self):
        return  self.__vida
    def set_vida(self, vida):
        self.__vida = vida 
        if self.__vida <= 0:
            self.morir()
        
        

#Variable del cosntructor vacío 
mi_personaje = personaje("EsteBandido", 100, 50, 45, 100)
mi_enemigo = personaje("Ángel", 70, 100, 40, 100)
#mi_personaje.vida
print(mi_personaje.get_vida())
#mi_personaje.set_vida(-5)
print(mi_personaje.get_vida())
mi_enemigo.__Personaje_vida = -5
mi_personaje.imprimir_atributos()
#mi_personaje.vida = 0 
#mi_personaje.imprimir_atributos() 
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())