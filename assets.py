from requests import get
from os import system as sys

ts = '1611107371000'
apiKey = '433fdcaccd9941d17e609fe17c3fa262'
hash = 'd48c8e5af3af4132a51a28e482481e65'

url = 'http://gateway.marvel.com/v1/public/'

def getHeroes(limit, offset):
    table = 'characters?'
    filter = 'orderBy=name&limit=' + limit + '&offset=' + offset
    keys = '&ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash

    r = get(url + table + filter + keys)

    content = r.json()
    content = content['data']
    heroes = content['results']

    return heroes

def GetHeroesTable(height, lenght):
    heroesTable = []

    for i in range(height):

        limit = str(lenght)
        offset = str(lenght * i)

        heroesTable.append(getHeroes(limit, offset))

    return heroesTable
