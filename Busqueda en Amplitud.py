# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:06:27 2023

@author: Janeth
"""

from collections import deque

# Definir el grafo
grafo = {
    'Hilandera': ['LittleWhinging', 'MansiónMalfoy'],
    'LittleWhinging': ['Hilandera', 'LaMadriguera', 'Grimmauld'],
    'LaMadriguera': ['LittleWhinging', 'Hangleton'],
    'MansiónMalfoy': ['Hilandera', 'Grimmauld', 'Refugio'],
    'Grimmauld': ['LittleWhinging', 'MansiónMalfoy', 'Hangleton', 'ValledeGodric'],
    'Hangleton': ['LaMadriguera', 'Grimmauld'],
    'Refugio': ['MansiónMalfoy', 'ValledeGodric'],
    'ValledeGodric': ['Grimmauld', 'Refugio'],
    
}

# Definir la función de búsqueda en amplitud
def busqueda_amplitud(grafo, inicio, objetivo):
    # Inicializar la cola con el nodo de inicio
    cola = deque([inicio])
    
    # Inicializar el conjunto de nodos visitados y el diccionario de padres
    visitados = set()
    padres = {inicio: None}
    
    # Iterar hasta que se encuentre el objetivo o se agote la cola
    while cola:
        # Sacar el siguiente nodo de la cola y marcarlo como visitado
        nodo = cola.popleft()
        visitados.add(nodo)
        
        # Si se encontró el objetivo, reconstruir el camino y regresarlo
        if nodo == objetivo:
            camino = [nodo]
            padre = padres[nodo]
            while padre is not None:
                camino.append(padre)
                padre = padres[padre]
            camino.reverse()
            return camino
        
        # Encontrar todos los vecinos no visitados del nodo actual y agregarlos a la cola
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)
                padres[vecino] = nodo
    
    # Si no se encontró el objetivo, regresar None
    return None

# Ejemplo de uso
inicio = 'Grimmauld'
objetivo = 'Hangleton'
camino = busqueda_amplitud(grafo, inicio, objetivo)
print(camino)