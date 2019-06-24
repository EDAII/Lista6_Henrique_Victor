from tkinter import *
from tkinter import filedialog
from funcoes import *

bg_color = "white"
button_color = "cyan"
option_button_font = ("Arial", "15", "bold")
confirmation_button_font = ("Arial", "10", "bold")
error_msg_font = ("Arial", "10", "bold")
text_font = ("Arial", "20", "bold")


class Interface:
    def __init__(self, instancia_Tk):
        self.grafo = Graph()
        self.qtd_nodes = 0
        self.qtd_edges = 0
        
        topo = Frame(instancia_Tk, background=bg_color, pady=50)
        topo.pack()
        frame1 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame1.pack()
        frame2 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame2.pack()
        frame3 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame3.pack()
        frame4 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame4.pack()
        frame5 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame5.pack()
        frame6 = Frame(instancia_Tk, background=bg_color, pady=6)
        frame6.pack()

        self.msgNodes = Label(topo, text = "Quantidade de Nós: {}".format(self.qtd_nodes))
        self.msgNodes.config(background=bg_color, font=text_font, padx=150)
        self.msgNodes.pack(side=LEFT)

        self.msgEdges = Label(topo, text = "Quantidade de Arestas: {}".format(self.qtd_edges))
        self.msgEdges.config(background=bg_color, font=text_font, padx=150)
        self.msgEdges.pack(side=RIGHT)

        B1 = Button(frame1, text="Gerar Grafo Aleatório", width=112, bg=button_color, font=option_button_font, command=self.gerar_grafo_aleat)
        B1.pack(side=LEFT)

        B2 = Button(frame2, text="Cadastrar Espécie Individual", width=55, bg=button_color, font=option_button_font, command=self.cadastro)
        B2.pack(side=LEFT)

        B3 = Button(frame2, text="Cadastrar Relação entre Espécies", width=55, bg=button_color, font=option_button_font, command=self.adicionar_relacao)
        B3.pack(side=RIGHT)

        B4 = Button(frame3, text="Buscar", width=112, bg=button_color, font=option_button_font)
        B4.pack(side=LEFT)

        B5 = Button(frame4, text="BFS - Busca em Largura", width=55, bg=button_color, font=option_button_font)
        B5.pack(side=LEFT)

        B6 = Button(frame4, text="DFS - Busca em Profundidade", width=55, bg=button_color, font=option_button_font)
        B6.pack(side=RIGHT)

        B7 = Button(frame5, text="Comparar Métodos de Busca (Grafo atual)", width=55, bg=button_color, font=option_button_font)
        B7.pack(side=LEFT)

        B8 = Button(frame5, text="Comparar Metodos de Busca (Varios Grafos Aleatorios)", width=55, bg=button_color, font=option_button_font)
        B8.pack(side=RIGHT)

        B9 = Button(frame6, text="Abrir Arquivo", width=55, bg=button_color, font=option_button_font, command=self.abre_arquivo)
        B9.pack(side=LEFT)

        B10 = Button(frame6, text="Salvar", width=55, bg=button_color, font=option_button_font, command=self.salva_arquivo)
        B10.pack(side=RIGHT)
    

    def gerar_grafo_aleat(self):
        tela = Tk()
        tela.title('Gerar Grafo Aleatório')

        texto1 = Frame(tela, pady=10)
        texto1.pack()
        campo1 = Frame(tela, pady=10)
        campo1.pack()
        texto2 = Frame(tela, pady=10)
        texto2.pack()
        campo2 = Frame(tela, pady=10)
        campo2.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()
        msg = Frame(tela, pady=10)
        msg.pack()

        text1 = Label(texto1, text="Digite quantas espécies você quer criar", font=text_font)
        text1.pack()

        nodes = Entry(campo1)
        nodes.pack()

        text2 = Label(texto2, text="Digite quantas relações existirão", font=text_font)
        text2.pack()

        edges = Entry(campo2)
        edges.pack()

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_valor(nodes.get(), edges.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("600x300+700+400")
        tela.mainloop()
    

    def verif_valor(self, nodes, edges, mensagem, tela):
        try:
            nodes = int(nodes)
            edges = int(edges)
            if (nodes > 0) and (edges > 0):
                limite = nodes * nodes - nodes
                if edges <= limite:
                    self.grafo = gerar_grafo_aleatorio(nodes, edges)
                    tela.destroy()
                    self.msgNodes["text"] = "Quantidade de Nós: {}".format(nodes)
                    self.msgEdges["text"] = "Quantidade de Arestas: {}".format(edges)
                    self.qtd_nodes = nodes
                    self.qtd_edges = edges
                else:
                    mensagem["text"] = "Quantidade de Relações deve estar entre 0 e {}".format(limite)
            else:
                mensagem["text"] = "Numero deve ser maior do que 0"
        except ValueError:
            mensagem["text"] = "Deve ser um numero valido"


    def cadastro(self):
        tela = Tk()
        tela.title('Cadastrar Espécie Individual')

        texto = Frame(tela, pady=10)
        texto.pack()
        frame1 = Frame(tela, pady=10)
        frame1.pack()
        frame2 = Frame(tela, pady=10)
        frame2.pack()
        frame3 = Frame(tela, pady=10)
        frame3.pack()
        frame4 = Frame(tela, pady=10)
        frame4.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()        
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite os dados da Espécie", font=text_font, pady=10)
        text.pack()

        nometext = Label(frame1, text="Nome: ", padx=13)
        nometext.pack(side=LEFT)
        nome = Entry(frame1, width=25)
        nome.pack(side=RIGHT)

        filotext = Label(frame2, text="Filo:     ", padx=8)
        filotext.pack(side=LEFT)
        filo = Entry(frame2, width=25)
        filo.pack(side=RIGHT)

        classetext = Label(frame3, text="Classe: ", padx=8)
        classetext.pack(side=LEFT)
        classe = Entry(frame3, width=25)
        classe.pack(side=RIGHT)

        ordemtext = Label(frame4, text="Ordem:     ")
        ordemtext.pack(side=LEFT)
        ordem = Entry(frame4, width=25)
        ordem.pack(side=RIGHT)

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_cadastro(nome.get(), filo.get(), classe.get(), ordem.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("650x300+650+300")
        tela.mainloop()
    

    def verif_cadastro(self, nome, filo, classe, ordem, mensagem, tela):
        if len(nome) == 0:
            mensagem["text"] = "Nome não pode estar em branco"
        elif len(filo) == 0:
            mensagem["text"] = "Filo não pode estar em branco"
        elif len(classe) == 0:
            mensagem["text"] = "Classe não pode estar em branco"
        elif len(ordem) == 0:
            mensagem["text"] = "Ordem não pode estar em branco"
        else:
            self.grafo.add_vertex(Especie(nome, filo, classe, ordem))
            self.qtd_nodes += 1
            self.msgNodes["text"] = "Quantidade de Nós: {}".format(self.qtd_nodes)
            tela.destroy()
    

    def adicionar_relacao(self):
        tela = Tk()
        tela.title('Cadastrar Espécie Individual')

        texto = Frame(tela, pady=10)
        texto.pack()
        frame1 = Frame(tela, pady=10)
        frame1.pack()
        frame2 = Frame(tela, pady=10)
        frame2.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()        
        msg = Frame(tela, pady=10)
        msg.pack()

        text = Label(texto, text="Digite os nomes das Espécies", font=text_font, pady=10)
        text.pack()

        predadortext = Label(frame1, text="Predador: ", padx=13)
        predadortext.pack(side=LEFT)
        predador = Entry(frame1, width=25)
        predador.pack(side=RIGHT)

        presatext = Label(frame2, text="Presa:     ", padx=8)
        presatext.pack(side=LEFT)
        presa = Entry(frame2, width=25)
        presa.pack(side=RIGHT)

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_relacao(predador.get(), presa.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("650x300+650+300")
        tela.mainloop()

    def verif_relacao(self, predador, presa, mensagem, tela):
        if len(predador) == 0:
            mensagem["text"] = "Predador não pode estar em branco"
        elif len(presa) == 0:
            mensagem["text"] = "Presa não pode estar em branco"
        else:
            # if encontrar predador e presa
                #self.grafo.add_edge(predador, presa)
                self.qtd_edges += 1
                self.msgNodes["text"] = "Quantidade de Arestas: {}".format(self.qtd_edges)
                tela.destroy()
            else:
                mensagem["text"] = "As duas espécies devem existir para fazer a relação"

    def abre_arquivo(self):
        self.fila.clear()
        path = filedialog.askopenfilename(initialdir = "/",title = "Selecione o Arquivo",filetypes = [("eda2 files","*.eda2")])

        i = 0
        nome = ""
        sexo = ""
        idade = ""
        gravidade = ""
        ordemChegada = ""
        try:
            with open(path, 'r') as arq:
                for linha in arq:
                    linha = linha.strip()
                    if i == 0:
                        nome = linha
                    elif i == 1:
                        sexo = linha
                    elif i == 2:
                        idade = linha
                    elif i == 3:
                        gravidade = int(linha)
                    else:
                        ordemChegada = int(linha)
                
                    i += 1

                    if i == 5:
                        self.fila.append(Paciente(nome, sexo, idade, gravidade, ordemChegada))
                        i = 0

            arq.close()
            self.msgNodes["text"] = "Quantidade de Pessoas: {}".format(len(self.fila))
            self.msgEdges["text"] = "Tipo de Ordenacao: Nenhuma"
            self.ordenado = False
        except:
            return


    def salva_arquivo(self):
        path = filedialog.asksaveasfilename(initialdir = "/",title = "Selecione o Local para Salvar",filetypes = [("eda2 files","*.eda2")])
        
        try:
            arq = open(path, 'w')

            for i in range(len(self.fila)):
                arq.write('{}\n'.format(self.fila[i].nome))
                arq.write('{}\n'.format(self.fila[i].sexo))
                arq.write('{}\n'.format(self.fila[i].idade))
                arq.write('{}\n'.format(self.fila[i].gravidade))
                arq.write('{}\n'.format(self.fila[i].ordemChegada))
        
            arq.close()
        except:
            return
    
    def aviso(self, mensagem):
        tela = Tk()
        tela.title('Aviso')

        msg = Frame(tela)
        botaoFrame = Frame(tela)
        msg.pack()
        botaoFrame.pack()

        text = Label(msg, text=mensagem, font=text_font, pady=10)
        text.pack()

        botao = Button(botaoFrame, text=" OK ", command=tela.destroy)
        botao.pack()

        tela.geometry("550x100+700+400")
        tela.mainloop()

    def mostrar_fila_ordenada(self):
        if len(self.fila) == 0:
            self.aviso("Nao ha nenhuma pessoa na fila")
        elif self.ordenado == False:
            self.aviso("Primeiro use algum Metodo de Ordenacao")
        else:
            mostrar_fila(self.fila, len(self.fila))


if __name__ == '__main__':
    menu=Tk()
    menu.title('LISTA 3 - ESTRUTURA DE DADOS 2')
    menu.config(background=bg_color)
    menu.geometry("1400x450+300+200")
    Interface(menu)
    menu.mainloop()