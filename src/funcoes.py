import os
import random
import time
import matplotlib
import matplotlib.pyplot as plt
from graph import Graph
from especie import Especie
from dados import *
import plotly
import plotly.graph_objs as go
import numpy as np
import multiprocessing as mp

quant_process = 4

def gerar_grafo_aleatorio(v, e):
    grafo = Graph()
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
    nome = animais[random.randrange(0, len(animais))]
    filo = filos[random.randrange(0, len(filos))]
    classe = classes[random.randrange(0, len(classes))]
    ordem = ordens[random.randrange(0, len(ordens))]

    return Especie(nome, filo, classe, ordem)