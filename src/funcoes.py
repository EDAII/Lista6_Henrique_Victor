import random
import time
import matplotlib
import matplotlib.pyplot as plt
from graph import Grafo
from especie import Especie
from dados import *
import plotly
import plotly.graph_objs as go
import numpy as np
import multiprocessing as mp
from graphviz import Digraph


quant_process = 4
visited_dfs = []

def gerar_grafo_aleatorio(v, e):
    grafo = Grafo()
    pool = mp.Pool(processes=quant_process)
    lista = pool.map(gerar_grafo_aleatorio_aux, range(0, v))

    if(e == v*v-v):
        for a in range(v):
            for b in range(v):
                grafo.add_edge(lista[a], lista[b])
    else:
        i = 0
        while (i != e):
            a, b = random.randrange(0, len(lista)), random.randrange(0, len(lista))
            if a == b:
                continue

            if (grafo.add_edge(lista[a], lista[b]) == 0):
                continue

            i += 1
    
    return grafo


def gerar_grafo_aleatorio_aux(i):
    return Especie(animais[random.randrange(0, len(animais))],
                   filos[random.randrange(0, len(filos))],
                   classes[random.randrange(0, len(classes))],
                   ordens[random.randrange(0, len(ordens))])


def BFS(grafo, start):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    while len(queue) != 0:
        prox = queue[0]
        queue.pop(0)

        for v in grafo._Grafo__graph_dict[prox]:
            if v in visited:
                continue
            
            visited.append(v)
            queue.append(v)

def DFS(grafo, u):
    if u in visited_dfs:
        continue
    
    visited_dfs.append(u)
    for v in grafo._Grafo__graph_dict[u]:
        DFS(grafo, v)


def printar_grafo(grafo):
    dot = Digraph(format='png')

    for vertice in grafo._Grafo__graph_dict:
        for v in grafo._Grafo__graph_dict[vertice]:
            if vertice.nome != v.nome:
                dot.edge(vertice.nome, v.nome)
    
    dot.render('grafo.gv', view=True)