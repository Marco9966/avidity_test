from requests import get
from os import system as sys

ts = '1611107371000'
apiKey = '433fdcaccd9941d17e609fe17c3fa262'
hash = 'd48c8e5af3af4132a51a28e482481e65'

url = 'http://gateway.marvel.com/v1/public/'

def getHeroInfo(hero_name):

    table = 'characters'
    filter = '?name=' + hero_name
    keys = '&ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash

    r = get(url + table + filter + keys)

    content = r.json()
    content = content['data']
    list = content['results']
    hero_info = list[0]

    return hero_info

def getRandonComic(hero_name):

    hero_info = getHeroInfo(hero_name)
    hero_id = str(hero_info['id'])

    table = 'comics'
    filter = '?characters=' + hero_id + '&limit=1'
    keys = '&ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash

    r = get(url + table + filter + keys)
    content = r.json()
    content = content['data']
    comics_n = content['total']
    
    offset = 0
    comics = []
    while offset < comics_n:

        filter = '?characters=' + hero_id + '&limit=100&offset=' + str(offset)

        r = get(url + table + filter + keys)
        content = r.json()
        comics += content['data']['results']
        offset += 100

    return comics


print(len(getRandonComic('Moon Knight')))



