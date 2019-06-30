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


def pantanal():
    grafo = Grafo()

    # Nodes
    grafo.add_vertex(Especie("Onça-pintada", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Capivara", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Anta", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Jacaré", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Ema", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Coelheiro", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Piranha", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Peixe", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Macaco", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Veado-campeiro", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Tuiuiú", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Gavião", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Sapo", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Roedor", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Coruja", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Periquito", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Sucuri", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    
    # Edges
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Jacaré"))
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Capivara"))
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Anta"))
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Peixe"))
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Macaco"))
    grafo.add_edge(grafo.find_node("Onça-pintada"), grafo.find_node("Veado-campeiro"))
    grafo.add_edge(grafo.find_node("Piranha"), grafo.find_node("Capivara"))
    grafo.add_edge(grafo.find_node("Piranha"), grafo.find_node("Peixe"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Capivara"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Anta"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Peixe"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Sucuri"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Tuiuiú"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Jacaré"), grafo.find_node("Ema"))
    grafo.add_edge(grafo.find_node("Ema"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Ema"), grafo.find_node("Roedor"))
    grafo.add_edge(grafo.find_node("Sucuri"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Sucuri"), grafo.find_node("Coelheiro"))
    grafo.add_edge(grafo.find_node("Sucuri"), grafo.find_node("Periquito"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Sucuri"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Periquito"))
    grafo.add_edge(grafo.find_node("Tuiuiú"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Tuiuiú"), grafo.find_node("Peixe"))
    grafo.add_edge(grafo.find_node("Coruja"), grafo.find_node("Roedor"))
    grafo.add_edge(grafo.find_node("Coruja"), grafo.find_node("Periquito"))
    
    return grafo


def terrestre():
    grafo = Grafo()

    # Nodes
    grafo.add_vertex(Especie("Onça", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Gavião", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Serpente", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Andorinha", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Raposa", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Sapo", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Escorpião", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Coelho", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Caitutu", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Rato", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Gafanhoto", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Besouro Carnívoro", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Tartaruga Terrestre", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    
    # Edges
    grafo.add_edge(grafo.find_node("Onça"), grafo.find_node("Coelho"))
    grafo.add_edge(grafo.find_node("Onça"), grafo.find_node("Tartaruga Terrestre"))
    grafo.add_edge(grafo.find_node("Onça"), grafo.find_node("Caitutu"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Serpente"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Rato"))
    grafo.add_edge(grafo.find_node("Gavião"), grafo.find_node("Andorinha"))
    grafo.add_edge(grafo.find_node("Serpente"), grafo.find_node("Sapo"))
    grafo.add_edge(grafo.find_node("Andorinha"), grafo.find_node("Gafanhoto"))
    grafo.add_edge(grafo.find_node("Andorinha"), grafo.find_node("Besouro Carnívoro"))
    grafo.add_edge(grafo.find_node("Raposa"), grafo.find_node("Coelho"))
    grafo.add_edge(grafo.find_node("Raposa"), grafo.find_node("Caitutu"))
    grafo.add_edge(grafo.find_node("Sapo"), grafo.find_node("Rato"))
    grafo.add_edge(grafo.find_node("Sapo"), grafo.find_node("Gafanhoto"))
    grafo.add_edge(grafo.find_node("Escorpião"), grafo.find_node("Gafanhoto"))
    grafo.add_edge(grafo.find_node("Escorpião"), grafo.find_node("Besouro Carnívoro"))

    return grafo


def aquatico():
    grafo = Grafo()

    # Nodes
    grafo.add_vertex(Especie("Águia-sapeira", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Perna-vermelha", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Garça-real", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Carangueijo-verde", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Robalo", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Caboz-da-areia", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Tainha", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Zooplâncton", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Camarão-mouro", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Lambujinha", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    grafo.add_vertex(Especie("Fitoplâncton", filos[random.randrange(0, len(filos))], classes[random.randrange(0, len(classes))], ordens[random.randrange(0, len(ordens))]))
    
    # Edges
    grafo.add_edge(grafo.find_node("Águia-sapeira"), grafo.find_node("Perna-vermelha"))
    grafo.add_edge(grafo.find_node("Perna-vermelha"), grafo.find_node("Carangueijo-verde"))
    grafo.add_edge(grafo.find_node("Robalo"), grafo.find_node("Carangueijo-verde"))
    grafo.add_edge(grafo.find_node("Carangueijo-verde"), grafo.find_node("Camarão-mouro"))
    grafo.add_edge(grafo.find_node("Robalo"), grafo.find_node("Camarão-mouro"))
    grafo.add_edge(grafo.find_node("Robalo"), grafo.find_node("Caboz-da-areia"))
    grafo.add_edge(grafo.find_node("Caboz-da-areia"), grafo.find_node("Lambujinha"))
    grafo.add_edge(grafo.find_node("Caboz-da-areia"), grafo.find_node("Zooplâncton"))
    grafo.add_edge(grafo.find_node("Garça-real"), grafo.find_node("Tainha"))
    grafo.add_edge(grafo.find_node("Tainha"), grafo.find_node("Fitoplâncton"))
    grafo.add_edge(grafo.find_node("Zooplâncton"), grafo.find_node("Fitoplâncton"))
    grafo.add_edge(grafo.find_node("Lambujinha"), grafo.find_node("Fitoplâncton"))
    grafo.add_edge(grafo.find_node("Camarão-mouro"), grafo.find_node("Zooplâncton"))

    return grafo