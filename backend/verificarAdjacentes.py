import leituraJson
import math
import json

def euclidianDistance(sample1, sample2, length):
    distance = 0
    for x in range(length):
        distance += pow(sample1[x] - sample2[x], 2)
    return math.sqrt(distance)


users = leituraJson.getUsers()
def verificarAdjacentesForUser(idUser):
    adjacentesUsers = {}
    valor = []
    media = 0
    for userAnalisado in users:
        if userAnalisado != idUser:
            RatingsX, RatingsY = verificarFilmeVotadosPelosDoisUsuarios(idUser, userAnalisado)
            if(len(RatingsX) >= 10):
                calculoEuclidiano = euclidianDistance(RatingsX, RatingsY, len(RatingsX))
                valor.append(calculoEuclidiano)
    if len(valor)> 0:
        media = sum(valor) / len(valor)
        print(media)
    for userAnalisado in users:
        if userAnalisado != idUser:
            RatingsX, RatingsY = verificarFilmeVotadosPelosDoisUsuarios(idUser, userAnalisado)
            if(len(RatingsX) >= 10):
                calculoEuclidiano = euclidianDistance(RatingsX, RatingsY, len(RatingsX))
                if calculoEuclidiano < media:
                    adjacentesUsers.update({userAnalisado: (calculoEuclidiano)})
    return adjacentesUsers

def verificarFilmeVotadosPelosDoisUsuarios(idUser, userAnalisado):
    RatingsX = []
    RatingsY = []
    filmesX = leituraJson.getFilmesByUserId(idUser)
    filmesY = leituraJson.getFilmesByUserId(userAnalisado)
    for idFilmeX in filmesX.keys():
        for idFilmeY in filmesY.keys():
            if idFilmeX == idFilmeY:
                RatingsX.append(float(filmesX[idFilmeX]))
                RatingsY.append(float(filmesY[idFilmeY]))
                break
    return RatingsX, RatingsY

def criarArquivoJsonGrafo():
    grafo = {"direcionado" : False, "vertices": [], "arestas": [], "pesosAresta": []}
    for userId in users:
        grafo['vertices'].append(userId)
        Adjacentes = verificarAdjacentesForUser(userId)
        print(Adjacentes)
        for adjacente, peso in Adjacentes.items():
            grafo['arestas'].append([userId, adjacente])
            grafo['pesosAresta'].append(peso)

    with open ('grafo.json', 'w') as outfile:
        json.dump(grafo, outfile)

if __name__ == "__main__":
    criarArquivoJsonGrafo()

