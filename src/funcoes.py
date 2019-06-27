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
tam_max = 100
salto = 2

def gerar_grafo_aleatorio(v, e):
    grafo = Grafo()
    pool = mp.Pool(processes=quant_process)
    lista = pool.map(gerar_grafo_aleatorio_aux, range(0, v))

    for l in lista:
        grafo.add_vertex(l)

    if(e == v*v):
        for a in range(v):
            for b in range(v):
                grafo.add_edge(lista[a], lista[b])
    else:
        i = 0
        while (i != e):
            a, b = random.randrange(0, len(lista)), random.randrange(0, len(lista))

            if (grafo.add_edge(lista[a], lista[b]) != 0):
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
            if v not in visited:            
                visited.append(v)
                queue.append(v)


def DFS(grafo, u, visited):
    if u not in visited:
        visited.append(u)
        for v in grafo._Grafo__graph_dict[u]:
            DFS(grafo, v, visited)


def comparar_tempos(grafo=None):
    if grafo != None:
        lista_tempos = {}
        
        inicio = time.perf_counter()
        for vertice in grafo._Grafo__graph_dict:
            BFS(grafo, vertice)
        fim = time.perf_counter()
        lista_tempos['BFS'] = (fim - inicio)

        inicio = time.perf_counter()
        for vertice in grafo._Grafo__graph_dict:
            DFS(grafo, vertice, [])
        fim = time.perf_counter()
        lista_tempos['DFS'] = (fim - inicio)

        tipos = ['BFS', 'DFS']
        tempos = [lista_tempos['BFS'], lista_tempos['DFS']]

        _, ax = plt.subplots(figsize=(16, 9))
        ax.set(xlabel='Metodo de Busca', ylabel='Tempo (s)')
        plt.figure(1)
        plt.bar(tipos, tempos)

        for i, v in enumerate(tempos):
            plt.text(i-0.1, max(tempos)/100, " "+str(v), color='black',
                    va='center', fontweight='bold', fontsize=12)

        plt.suptitle('Tempo em segundos para percorrer um grafo com {} nós'.format(len(grafo._Grafo__graph_dict)))
        plt.show()
    else:
        tempo_BFS, tempo_DFS = [], []
        for i in range(salto, tam_max+1, salto):
            grafo = gerar_grafo_aleatorio(i, i*i)

            inicio = time.perf_counter()
            for vertice in grafo._Grafo__graph_dict:
                BFS(grafo, vertice)
            fim = time.perf_counter()
            tempo_BFS.append(fim-inicio)

            inicio = time.perf_counter()
            for vertice in grafo._Grafo__graph_dict:
                DFS(grafo, vertice, [])
            fim = time.perf_counter()
            tempo_DFS.append(fim-inicio)
        
        printar_grafico(tempo_BFS, tempo_DFS)


def printar_grafico(BFS, DFS):
    x = np.array([])

    for i in range(salto, tam_max+1, salto):
        x = np.append(x, i)
    
    t = x
    fig, ax = plt.subplots()
    ax.set_title('Comparação entre os Algoritmos')
    ax.set(xlabel='Quantidade de nós', ylabel='Tempo (s)')
    line1, = ax.plot(t, BFS, lw=2, color='red', label='BFS')
    line2, = ax.plot(t, DFS, lw=2, color='blue', label='DFS')
    leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
    leg.get_frame().set_alpha(0.4)

    lines = [line1, line2]
    lined = dict()
    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(2)
        lined[legline] = origline


    def onpick(event):
        legline = event.artist
        origline = lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)

        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()

def printar_grafo(grafo):
    dot = Digraph(format='png')

    for vertice in grafo._Grafo__graph_dict:
        dot.node(vertice.nome)
        for v in grafo._Grafo__graph_dict[vertice]:
            dot.edge(vertice.nome, v.nome)
    
    dot.render('grafo.gv', view=True)