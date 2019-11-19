import json

def lerArquivoUser():
    with open('./users.json') as json_file:
        return json.load(json_file)
    
def lerArquivoMovies():
    with open('./movies.json') as json_file2:
        return json.load(json_file2)

def lerArquivoMoviesPosterPath():
    try:
        with open('./moviesPosterPath.json') as json_file3:
            return json.load(json_file3)
    except FileNotFoundError:
        with open ('moviesPosterPath.json', 'w') as outfile:
            json.dump({}, outfile)
            return {}

def getFilmesByUserId(userId):
    users = lerArquivoUser()
    return users[userId]

def getUsersId(id):
    users = lerArquivoUser()
    return True if id in users.keys() else False

def getFilmeById(filmeId):
    movies = lerArquivoMovies()
    return movies[filmeId]

def getPosterPathById(tmdbId):
    posterPath = lerArquivoMoviesPosterPath()
    return posterPath[tmdbId] if tmdbId in posterPath.keys() else None

def setPosterPathById(tmdbId, path):
    posterPath = lerArquivoMoviesPosterPath()
    posterPath.update({tmdbId: path})
    with open ('moviesPosterPath.json', 'w') as outfile:
        json.dump(posterPath, outfile)


