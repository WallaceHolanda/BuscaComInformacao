class Cidade:
    def __init__(self, nome, distanciaObjetivo): #Construtor
        self.nome = nome
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.adjacentes = [] #Lista de Cidades Adjacentes
        
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)
        
'''
c = Cidade("Teste")
c.nome
c.visitado
'''