class Pokemon:
    def __init__(self, nombre, nivel, defensa, fuerza, inteligencia, velocidad):
        self.nombre = nombre
        self.nivel = nivel
        self.defensa = defensa
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.velocidad = velocidad

def asignar_pokemon_leido(campos):
    if len(campos) != 6:
        return None
    else:
        nombre = campos[0]
        nivel = int(campos[1])
        defensa = int(campos[2])
        fuerza = int(campos[3])
        inteligencia = int(campos[4])
        velocidad = int(campos[5])
        pokemon = Pokemon(nombre, nivel, defensa, fuerza, inteligencia, velocidad)
        return pokemon
