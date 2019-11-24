import csv
import json
import requests
def criarJsonFilmes():
    movie = {}

    with open('movies.csv', newline = '', encoding="utf8" ) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mv = {row['movieId']: {"title": row['title'], "genres": row['genres']}}
            movie.update(mv)

    with open('links.csv', newline = '', encoding="utf8" ) as csvfile:
        reader = csv.DictReader(csvfile)
        var = 1
        for row in reader:
            mv = {"imdbId": row['imdbId'], "tmdbId": row['tmdbId']}
            movie[row['movieId']].update(mv)
            var += 1

    with open ('./movies.json', 'w') as outfile:
        json.dump(movie, outfile)

if __name__ =="__main__":
    criarJsonFilmes()