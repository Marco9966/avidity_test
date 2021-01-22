from requests import get
from os import system as sys
from random import randrange

ts = '1611107371000'                            # Timestamp used for the creation of the md5 hash
apiKey = '433fdcaccd9941d17e609fe17c3fa262'     # Marvel for Developers API authentication key
hash = 'd48c8e5af3af4132a51a28e482481e65'       # Hash to autenticate to Marvel for Developers API

url = 'http://gateway.marvel.com/v1/public/'    # URL for the Marvel for Developers API

def getHeroInfo(hero_name):     # Gets all the hero info from Marvel for Developers API

    if not hero_name:           # Verify if there's a name, else, it returns None
        return None

    table = 'characters'                                        # Defines the table to get information from
    filter = '?name=' + hero_name                               # Defines a filter for te information, in this case, the name of the hero
    keys = '&ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash  # Concatenates all the authentication information for the Marvel for Developers API

    r = get(url + table + filter + keys)                        # Combines the table, filter and keys to return the information based on the table and filter

    content = r.json()                                          # Gets only the necessary information 
    list = content['data']['results']                           # from the response for the get method

    if len(list) == 0:          # Verify if there's a hero with this name, else, it returns None
            return None

    hero_info = list[0]     # Pass the information from a list to a dict

    return hero_info



def getRandonComic(hero_name):  # Gets a random comic of a specif character from Marvel for Developers API

    hero_info = getHeroInfo(hero_name)  # Gets the hero info

    if hero_info == None:   # Verify if there wasn't any problem getting the hero information, else, it returns None
        return None

    hero_id = str(hero_info['id'])  # Gets the id of the hero

    # This part of the code is to get the total number that this character have and get a random number in this scope to randomize the comic select

    table = 'comics'                                            # Defines the table to get information from
    filter = '?characters=' + hero_id + '&limit=1'              # Defines a filter for te information, in this case, the hero id and the limit of 1
    keys = '&ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash  # Concatenates all the authentication information for the Marvel for Developers API

    r = get(url + table + filter + keys)                        # Combines the table, filter and keys to return the information based on the table and filter

    content = r.json()                                          # Gets only the necessary information 
    comics_n = content['data']['total']                         # from the response for the get method

    offset = randrange(comics_n)                                # Gets a random number in the range of comics of this character and sets this as the offset of the search filter

    filter = '?characters=' + hero_id + '&limit=1&offset=' + str(offset)    # Defines a filter for te information, in this case, the hero id, 
                                                                            # the limit of 1 and the offset as the randon number got on the previous line code

    r = get(url + table + filter + keys)

    content = r.json()                  # Gets only the necessary information 
    list = content['data']['results']   # from the response for the get method
    comic = list[0]                     #

    comic['attributionText'] = content['attributionText']   # Adds the Marvel attribution text to the dictionary

    return comic



def getCharsInfo(char_list):    # Gets information about a list of characters

    keys = '?ts=' + ts + '&apikey=' + apiKey + '&hash=' + hash  # Concatenates all the authentication information for the Marvel for Developers API

    chars_info = []         # Creates a list to store all characters informations
    for char in char_list:
        r = get(char['resourceURI'] + keys) # Gets a character data
        content = r.json()                  # and filter to be only
        list = content['data']['results']   # the necessary information
        
        if len(list) == 0:  # Verifies if the list given got a result, else, returns None
            return None

        chars_info.append(list[0])  # Adds the character information to the list of characters informations
    return chars_info