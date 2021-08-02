class Entrenador:
    def __init__(self, nombre, victorias):
        self.equipo = []
        self.victorias = victorias
        self.nombre = nombre

    def agregar_pokemon(self, pokemon):
        self.equipo.append(pokemon)


def asignar_campos_leidos_entrenador(campos):
    if len(campos) != 2:
        return None
    else:
        nombre = campos[0]
        victorias = int(campos[1])
        entrenador = Entrenador(nombre, victorias)
        return entrenador