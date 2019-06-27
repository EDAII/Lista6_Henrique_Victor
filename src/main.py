from tkinter import *
from funcoes import *

bg_color = "white"
button_color = "cyan"
option_button_font = ("Arial", "15", "bold")
confirmation_button_font = ("Arial", "10", "bold")
error_msg_font = ("Arial", "10", "bold")
text_font = ("Arial", "20", "bold")
estatistica_font = ("Arial", "15", "bold")


class Interface:
    def __init__(self, instancia_Tk):
        self.grafo = Grafo()
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

        self.msgNodes = Label(topo, text = "Quantidade de Espécies: {}".format(self.qtd_nodes))
        self.msgNodes.config(background=bg_color, font=text_font, padx=150)
        self.msgNodes.pack(side=LEFT)

        self.msgEdges = Label(topo, text = "Quantidade de Relações: {}".format(self.qtd_edges))
        self.msgEdges.config(background=bg_color, font=text_font, padx=150)
        self.msgEdges.pack(side=RIGHT)

        B1 = Button(frame1, text="Gerar Grafo Aleatório", width=112, bg=button_color, font=option_button_font, command=self.gerar_grafo_aleat)
        B1.pack(side=LEFT)

        B2 = Button(frame2, text="Cadastrar Espécie Individual", width=55, bg=button_color, font=option_button_font, command=self.cadastro)
        B2.pack(side=LEFT)

        B3 = Button(frame2, text="Cadastrar Relação entre Espécies", width=55, bg=button_color, font=option_button_font, command=self.adicionar_relacao)
        B3.pack(side=RIGHT)

        B4 = Button(frame3, text="Informação sobre Espécie", width=112, bg=button_color, font=option_button_font, command=self.search)
        B4.pack(side=LEFT)

        B5 = Button(frame4, text="Dados sobre o Grafo", width=112, bg=button_color, font=option_button_font, command=self.print_info)
        B5.pack(side=LEFT)

        B6 = Button(frame5, text="Comparar Métodos de Busca (Grafo atual)", width=55, bg=button_color, font=option_button_font, command=lambda: comparar_tempos(self.grafo))
        B6.pack(side=LEFT)

        B7 = Button(frame5, text="Comparar Métodos de Busca (Vários Grafos Aleatórios)", width=55, bg=button_color, font=option_button_font, command=lambda: comparar_tempos())
        B7.pack(side=RIGHT)

        B8 = Button(frame6, text="Gerar Arvore", width=112, bg=button_color, font=option_button_font, command=self.mostrar_grafo)
        B8.pack(side=LEFT)
    

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
            if (nodes > 0) and (edges >= 0):
                if nodes <= len(animais):
                    limite = nodes * nodes
                    if edges <= limite:
                        self.grafo = gerar_grafo_aleatorio(nodes, edges)
                        tela.destroy()
                        self.msgNodes["text"] = "Quantidade de Espécies: {}".format(nodes)
                        self.msgEdges["text"] = "Quantidade de Relações: {}".format(edges)
                        self.qtd_nodes = nodes
                        self.qtd_edges = edges
                    else:
                        mensagem["text"] = "Quantidade de Relações deve estar entre 0 e {}".format(limite)
                else:
                    mensagem["text"] = "Quantidade de Espécies deve estar entre 1 e {}".format(len(animais))
            else:
                mensagem["text"] = "Numero deve ser 0 ou maior"
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

        tela.geometry("650x350+650+300")
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
            node = self.grafo.find_node(nome)
            if node == None:
                self.grafo.add_vertex(Especie(nome, filo, classe, ordem))
                self.qtd_nodes += 1
                self.msgNodes["text"] = "Quantidade de Espécies: {}".format(self.qtd_nodes)
                tela.destroy()
            else:
                mensagem["text"] = "Já existe uma espécie com esse nome"
    

    def adicionar_relacao(self):
        tela = Tk()
        tela.title('Cadastrar Relação entre Espécies')

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

        presatext = Label(frame2, text="Presa:         ", padx=8)
        presatext.pack(side=LEFT)
        presa = Entry(frame2, width=25)
        presa.pack(side=RIGHT)

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_relacao(predador.get(), presa.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("650x250+650+300")
        tela.mainloop()

    def verif_relacao(self, predador, presa, mensagem, tela):
        if len(predador) == 0:
            mensagem["text"] = "Predador não pode estar em branco"
        elif len(presa) == 0:
            mensagem["text"] = "Presa não pode estar em branco"
        else:
            node_pred = self.grafo.find_node(predador)
            node_presa = self.grafo.find_node(presa)
            if node_pred != None and node_presa != None:
                if self.grafo.add_edge(node_pred, node_presa) != -1:
                    self.qtd_edges += 1
                    self.msgEdges["text"] = "Quantidade de Relações: {}".format(self.qtd_edges)
                    tela.destroy()
                else:
                    mensagem["text"] = "Essa relação já existe"
            else:
                mensagem["text"] = "As duas espécies devem existir para fazer a relação"

    def search(self):
        tela = Tk()
        tela.title('Buscar Espécie')

        texto1 = Frame(tela, pady=10)
        texto1.pack()
        campo1 = Frame(tela, pady=10)
        campo1.pack()
        botoes = Frame(tela, pady=10)
        botoes.pack()
        msg = Frame(tela, pady=10)
        msg.pack()

        text1 = Label(texto1, text="Digite o nome da espécie", font=text_font)
        text1.pack()

        nome = Entry(campo1)
        nome.pack()

        mensagem = Label(msg, text=" ", font=error_msg_font)
        mensagem.pack()

        botaoCancel = Button(botoes, text="CANCELAR", font=confirmation_button_font, bg='red2', command=tela.destroy)
        botaoCancel.pack(side=LEFT)

        botaoSend = Button(botoes, text="ENVIAR", font=confirmation_button_font, bg='green2', command=lambda: self.verif_busca(nome.get(), mensagem, tela))
        botaoSend.pack(side=RIGHT)

        tela.geometry("600x200+700+400")
        tela.mainloop()

    def verif_busca(self, nome, mensagem, tela_antiga):
        if len(nome) == 0:
            mensagem["text"] = "Nome não pode estar em branco"
        else:
            node, quant_presas = self.grafo.get_info(nome)
            if node == None:
                mensagem["text"] = "Espécie não encontrada"
            else:
                tela_antiga.destroy()

                tela = Tk()
                tela.title('Espécie')

                msg = Frame(tela)
                f1 = Frame(tela)
                f2 = Frame(tela)
                f3 = Frame(tela)
                f4 = Frame(tela)
                f5 = Frame(tela)
                vazio = Frame(tela)
                botaoFrame = Frame(tela)
                msg.pack()
                f1.pack()
                f2.pack()
                f3.pack()
                f4.pack()
                f5.pack()
                vazio.pack()
                botaoFrame.pack()

                titulo = Label(msg, text='Dados da Espécie', font=text_font, pady=30)
                titulo.pack()

                textNome = Label(f1, text='Nome: ', font=estatistica_font, pady=5)
                textNome.pack(side=LEFT)

                valorNome = Label(f1, text=node.nome, font=estatistica_font, pady=5, fg='red')
                valorNome.pack(side=RIGHT)

                textFilo = Label(f2, text='Filo: ', font=estatistica_font, pady=5)
                textFilo.pack(side=LEFT)

                valorFilo = Label(f2, text=node.filo, font=estatistica_font, pady=5, fg='red')
                valorFilo.pack(side=RIGHT)

                textClasse = Label(f3, text='Classe: ', font=estatistica_font, pady=5)
                textClasse.pack(side=LEFT)

                valorClasse = Label(f3, text=node.classe, font=estatistica_font, pady=5, fg='red')
                valorClasse.pack(side=RIGHT)

                textOrdem = Label(f4, text='Ordem: ', font=estatistica_font, pady=5)
                textOrdem.pack(side=LEFT)

                valorOrdem = Label(f4, text=node.ordem, font=estatistica_font, pady=5, fg='red')
                valorOrdem.pack(side=RIGHT)

                textPresas = Label(f5, text='Quantidade de Presas: ', font=estatistica_font, pady=5)
                textPresas.pack(side=LEFT)

                valorPresas= Label(f5, text=quant_presas, font=estatistica_font, pady=5, fg='red')
                valorPresas.pack(side=RIGHT)

                vaziotext = Label(vazio, text=' ', pady=10)
                vaziotext.pack()
                botao = Button(botaoFrame, text=" OK ", command=tela.destroy)
                botao.pack()
                tela.geometry("550x350+700+400")
                tela.mainloop()


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
    
    def mostrar_grafo(self):
        if self.qtd_nodes == 0:
            self.aviso("Nao ha nenhuma espécie no grafo")
        else:
            printar_grafo(self.grafo)
    

    def print_info(self):
        if self.qtd_nodes == 0:
            self.aviso("Nao ha nenhuma espécie no grafo")
        else:
            tela = Tk()
            tela.title('Dados')

            msg = Frame(tela)
            f1 = Frame(tela)
            f2 = Frame(tela)
            f3 = Frame(tela)
            vazio = Frame(tela)
            botaoFrame = Frame(tela)
            msg.pack()
            f1.pack()
            f2.pack()
            f3.pack()
            vazio.pack()
            botaoFrame.pack()
            titulo = Label(msg, text='Dados do Grafo', font=text_font, pady=30)
            titulo.pack()
            textNome = Label(f1, text='Quantidade de Nós: ', font=estatistica_font, pady=5)
            textNome.pack(side=LEFT)
            valorNome = Label(f1, text=str(self.qtd_nodes), font=estatistica_font, pady=5, fg='red')
            valorNome.pack(side=RIGHT)
            textFilo = Label(f2, text='Quantidade de Arestas: ', font=estatistica_font, pady=5)
            textFilo.pack(side=LEFT)
            valorFilo = Label(f2, text=str(self.qtd_edges), font=estatistica_font, pady=5, fg='red')
            valorFilo.pack(side=RIGHT)
            textClasse = Label(f3, text='Conectado? ', font=estatistica_font, pady=5)
            textClasse.pack(side=LEFT)
            valorClasse = Label(f3, text=self.grafo.connectivity(), font=estatistica_font, pady=5, fg='red')
            valorClasse.pack(side=RIGHT)

            vaziotext = Label(vazio, text=' ', pady=10)
            vaziotext.pack()
            
            botao = Button(botaoFrame, text=" OK ", command=tela.destroy)
            botao.pack()
            tela.geometry("550x280+700+400")
            tela.mainloop()

if __name__ == '__main__':
    menu=Tk()
    menu.title('LISTA 6 - ESTRUTURA DE DADOS 2')
    menu.config(background=bg_color)
    menu.geometry("1400x450+300+200")
    Interface(menu)
    menu.mainloop()