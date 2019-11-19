import leituraJson
from flask import Flask, jsonify
from grafos import grafo
import json
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

with open('grafo.json') as f:
    data = json.load(f)

vertices = data['vertices']
arestas = data['arestas']
pesosArestas = data['pesosAresta']
direcionado = data['direcionado']

grafo = grafo.Grafo(direcionado)
grafo.adicionar_vertice(vertices)
grafo.adicionar_arestas(arestas, pesosArestas)

@app.route("/")
def hello():
    return jsonify("Hello Word")

@app.route("/user/<string:id>", methods=["GET"])
def retornarUserExiste(id): 
    return jsonify(leituraJson.getUsersId(id))

@app.route("/users/<string:id>", methods=["GET"])
def retornarFilmesUsers(id):   
    filmesVistos = leituraJson.getFilmesByUserId(id)
    response = []
    for x, avaliacao in filmesVistos.items():
        filme = leituraJson.getFilmeById(x)
        filme.update({"avaliacao": avaliacao})
        filme.update({"movieId":x})
        response.append(filme)
    response.sort(reverse=True, key=lambda x: x['avaliacao'])
    if len(response) > 16:
        response = response[:16]
    for filme in response:
        posterPath = leituraJson.getPosterPathById(filme['movieId'])
        if posterPath != None:
            filme.update({"posterPath": posterPath})
        else:
            tmdbId = filme['tmdbId']
            posterPath = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6e1db1b810b3b674e1a2124938906e02'.format(tmdbId))
            try:
                posterPath = 'https://image.tmdb.org/t/p/w500'+posterPath.json()['poster_path']
                leituraJson.setPosterPathById(filme['movieId'], posterPath)
                filme.update({"posterPath": posterPath})
            except:
                    leituraJson.setPosterPathById(filme['movieId'], 'https://i.imgur.com/6I39vXk.jpg')
                    filme.update({"posterPath": 'https://i.imgur.com/6I39vXk.jpg'})
    return jsonify(response)


@app.route("/recomendacao/<string:id>", methods=["GET"])
def retornarAdjacentes(id):
    filmesRecomendar = grafo.dijkstraRecomendacao(id)
    response = []
    for x in filmesRecomendar:
        filme = leituraJson.getFilmeById(x)
        filme.update({"movieId":x})
        response.append(filme)
    for filme in response:
        posterPath = leituraJson.getPosterPathById(filme['movieId'])
        if posterPath != None:
            filme.update({"posterPath": posterPath})
        else:
            tmdbId = filme['tmdbId']
            posterPath = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6e1db1b810b3b674e1a2124938906e02'.format(tmdbId))
            try:
                posterPath = 'https://image.tmdb.org/t/p/w500'+posterPath.json()['poster_path']
                leituraJson.setPosterPathById(filme['movieId'], posterPath)
                filme.update({"posterPath": posterPath})
            except:
                    leituraJson.setPosterPathById(filme['movieId'], 'https://i.imgur.com/6I39vXk.jpg')
                    filme.update({"posterPath": 'https://i.imgur.com/6I39vXk.jpg'})
    return jsonify(response)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)