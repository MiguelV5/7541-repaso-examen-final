# Utilizando el lenguaje de programación *Python*, escriba una implementación del 
# **TDA Gafo** bajo las siguientes restricciones: 
#   - **No** se pueden utilizar diccionarios (o sea, usen listas) 
#   - Los vértices deben ser entidades separadas y deben poder contener un peso - Las aristas deben poder ser pesadas 
#   - Dados dos vertices, debe poder conocerse el peso entre de la arista que los une (si existe)
#   - Dado un vértice, debe poder conocerse un listado de los vértices vecinos.
# Haga las suposiciones que tenga que hacer si falta información. 
# Explique y justifique su solución.

class Arista:
    def __init__(self, vertice_asociado_1, vertice_asociado_2, peso_arista):
        self.vertices_asociados = [vertice_asociado_1, vertice_asociado_2]
        self.peso_a = peso_arista
        
    def obtener_peso_arista(self):
        return self.peso_a
        
class Vertice:
    def __init__(self, peso_vertice):
        self.peso_v = peso_vertice
        self.vecinos = []
        
    def obtener_peso_vertice(self):
        return self.peso_v
        
    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)
        
    def obtener_vecinos(self):
        return self.vecinos
        
class Grafo:
    def __init__(self):
        self.vertices = []
        self.aristas = []
        
    def insercion_arista(self, vertice_asociado_1, vertice_asociado_2, peso_arista):
        arista = Arista(vertice_asociado_1, vertice_asociado_2, peso_arista)
        vertice_asociado_1.agregar_vecino(vertice_asociado_2)
        vertice_asociado_2.agregar_vecino(vertice_asociado_1)
        self.aristas.append(arista)
    
    def insercion_vertice(self, peso_vertice):
        vertice = Vertice(peso_vertice)
        self.vertices.append(vertice)

    def obtener_vecinos_vertice(self,vertice):
        if vertice not in self.vertices:
            return None
            
        return vertice.obtener_vecinos()

    def obtener_peso_entre_vertices(self, v_1, v_2):
        peso_arista_obtenido = -1
        if v_1 in v_2.vecinos:  #Alcanza con revisar uno solo porque es un grafo no dirigido. Si uno está en la lista del otro se cumple el recíproco tambien.
            lista_auxiliar = [v_1, v_2]
            for arista in self.aristas:
                if arista.vertices_asociados == lista_auxiliar:
                    peso_arista_obtenido = arista.obtener_peso_arista()
        
        return peso_arista_obtenido