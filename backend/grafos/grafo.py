from .vertice import Vertice
from .aresta import Aresta
from estruturas_de_dados import pilha, fila
import leituraJson
import math


class Grafo:

    def __init__(self, direcionado=False):
        self.__lista_de_Vertices = []
        self.__lista_de_Arestas = []
        self.__lista_de_Adjacentes = {}
        self.__direcionado = direcionado
        self.__regular = False
        self.__completo = False
        self.pilha = None
        self.fila = None

 
    def getAdjacentes(self, vertice):
        """
        Retorna a lista de adjacentes de um determinado vertice.

        Exemplo: grafo.adjacentes('v1') --- retorn [v2,v3].

        """
        return " ".join(map(lambda x: x.__str__(),  self.__lista_de_Adjacentes[vertice]))

    def adicionar_vertice(self, vertices):
        """
        adiciona os vertices no grafo.

        parametros: nome dos vertices --> 'v1','v2','v3' ...

        """
        self.__lista_de_Vertices = [Vertice(nome) for nome in vertices]
        self.__criar_lista_adjacentes()

    def adicionar_arestas(self, arestas, pesosArestas):
        """
        adiciona as arestas no grafo.

        parametros: Tupla com os vertices participantes ---> ('v1','v2'), ('v1','v3'), ('v2','v3').

        após adicionar as arestas ao grafo  chama a função __set_adjacentes()
        """
        self.__lista_de_Arestas = [Aresta(aresta[0], aresta[1], pesosArestas[pos]) for pos, aresta in
                                   enumerate(arestas)]
        self.__set_adjacentes()

    def __criar_lista_adjacentes(self):
        """
        Cria um dicionario onde a chave é um vertice e o valor instancia uma lista ligada.

        """
        for i in self.__lista_de_Vertices:
            self.__lista_de_Adjacentes[i.nome] = []

    def __set_adjacentes(self):
        """
        Seta as adjacencias na lista de adjacencias,  a partir das arestas adicionadas
        Para cada vertice do grafo será inserido, na lista ligada que foi instanciada na função __criar_lista_adjacentes,
        os seus respectivos vertices adjacentes.all

                                    -------- Exemplo --------
        Aresta(v1,v2)

        lista_de_adjacentes = {
            'v1': v2
            'v2': v1
        }

        """
        if not self.__direcionado:
            for aresta in self.__lista_de_Arestas:
                self.__lista_de_Adjacentes[aresta.pontoA].append(self.__select_vertice(aresta.pontoB))
                self.__lista_de_Adjacentes[aresta.pontoB].append(self.__select_vertice(aresta.pontoA))
        else:
            for aresta in self.__lista_de_Arestas:
                self.__lista_de_Adjacentes[aresta.pontoA].append(self.__select_vertice(aresta.pontoB))

    def __select_vertice(self, nome_vertice):
        """
        Seleciona um vertice da lista de vertices a partir do seu nome.

        parametro: Nome do Vertice
        Return: <grafos.vertice.Vertice object at 0x7f18966b2a90>
        """
        for vertice in self.__lista_de_Vertices:
            if vertice.nome == nome_vertice:
                return vertice
        else:
            return None

    def __select_arestas(self, pontoA, pontoB):
        for i in self.__lista_de_Arestas:
            if pontoA == i.pontoA and pontoB == i.pontoB:
                return i
            elif pontoB == i.pontoA and pontoA == i.pontoB:
                return i

    def dijkstraRecomendacao(self, vInicial, vFinal=None):
        filmesDoUsuario = leituraJson.getFilmesByUserId(vInicial)
        s, dist, path = [], {}, {}
        filmesParaRecomendar = []
        atingiuFilmesEsperados = False
        for x in self.__lista_de_Vertices:
            x.visitado = False
            dist.update({x.nome: math.inf})
            path.update({x.nome: None})
        self.fila = fila.Fila()
        s.append(vInicial)
        dist[vInicial], path[vInicial], vertice = 0, vInicial, self.__select_vertice(vInicial)
        vertice.visitado = True
        self.fila.enfilerar(vertice)
        while self.fila.tamanho >= 1:
            v = self.fila.inicio
            for i in (self.__lista_de_Adjacentes[v.nome]):
                aresta = self.__select_arestas(v.nome, i.nome)
                if aresta.peso + dist[v.nome] < dist[i.nome]:
                    dist[i.nome] = aresta.peso + dist[v.nome]
                    path[i.nome] = v
            menor, elemento = math.inf, ""
            for i, j in dist.items():
                adicionar = False
                if i not in s:
                    if j < menor:
                        menor, elemento, adicionar = j, i, True
                if adicionar:
                    s.append(elemento)
                    self.fila.enfilerar(self.__select_vertice(elemento))
                    filmesRelacionados = leituraJson.getFilmesByUserId(elemento)
                    for filme in filmesRelacionados:
                        if filme not in filmesDoUsuario and len(filmesParaRecomendar) < 16:
                            filmesParaRecomendar.append(filme)
                if (len(filmesParaRecomendar) >= 16):
                    atingiuFilmesEsperados = True 
                    break
            self.fila.desenfilerar()
            if atingiuFilmesEsperados:
                break

        return filmesParaRecomendar
 