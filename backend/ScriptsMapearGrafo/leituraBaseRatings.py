import csv 
import pandas as pd
import json
users = {}

with open('ratings.csv', newline = '' ) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        inserir = True
        for x in users.keys():
            if (x != None):
                if x == row['userId']: inserir = False
        if (inserir):
            users.update({row['userId'] : {}})

with open('ratings.csv', newline = '' ) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        for x in users.keys():
            if x == row['userId']:
                users[x].update({row['movieId']: row['rating']})

     
with open ('data.json', 'w') as outfile:
    json.dump(users, outfile)
