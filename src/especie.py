class Especie:

    __slots__ = ['nome', 'filo', 'classe', 'ordem']

    def __init__(self, nome, filo, classe, ordem):
        self.nome = nome
        self.filo = filo
        self.classe = classe
        self.ordem = ordem
        