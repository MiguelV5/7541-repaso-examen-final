from Pokemon import *
from Entrenador import *

class Salon:
    def __init__(self):
        self.entrenadores = []

    def agregar_entrenador(self, entrenador):
        if entrenador:
            self.entrenadores.append(entrenador)

    def mostrar_salon(self):
        for entrenador in self.entrenadores:
            print("\nEntrenador: {} ,  victorias: {}".format(entrenador.nombre, entrenador.victorias))
            print("Equipo:")
            for pokemon in entrenador.equipo:
                print("\t{}  ,  Nivel: {}  ,  Def: {}  ,  Fuerza: {}  ,  Inteligencia: {}  ,  Vel: {}".format(pokemon.nombre, pokemon.nivel, pokemon.defensa, pokemon.fuerza, pokemon.inteligencia, pokemon.velocidad))

    def mostrar_salon_ordenado_alfabetic(self):
        self.entrenadores.sort(key = lambda entrenador: entrenador.nombre)
        self.mostrar_salon()


def salon_leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    salon = Salon()
    entrenador_actual = None
    pokemon_actual = None
    for linea in archivo:
        campos_divididos = linea.split(";")
        entrenador_aux = asignar_campos_leidos_entrenador(campos_divididos)
        pokemon_actual = asignar_pokemon_leido(campos_divididos)
        if entrenador_aux:
            salon.agregar_entrenador(entrenador_actual)
            entrenador_actual = entrenador_aux
        elif pokemon_actual and entrenador_actual:
            entrenador_actual.agregar_pokemon(pokemon_actual)

    salon.agregar_entrenador(entrenador_actual)

    archivo.close()
    return salon