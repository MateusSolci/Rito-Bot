import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import make_request
load_dotenv()


# retorna informações do invocador, a partir do nickname
def summoner_ids(origin, nick):
    response = make_request(origin + "/lol/summoner/v4/summoners/by-name/" + nick + "?api_key=" + os.environ.get('key'))

    return response


def get_elo(origin, id):
    response = make_request(origin + "/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def mastery(origin, id):
    top_mastery = []
    count = 0
    response = make_request(origin + "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    for x in response:
        if(count == 5):
            break
        else:
            count += 1
            # print(x)
            
    return response


def live_game(origin, id):
    response = make_request(origin + "/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def concat_info(origin, nick):
    summonerDict = {}

    IDs = summoner_ids(origin, nick)
    elo = get_elo(origin, IDs['id'])
    mastery(origin, IDs['id'])

    # summonerDict['ID'] = IDs['id']
    # summonerDict['Ícone'] = IDs['profileIconId']
    summonerDict['Nome'] = IDs['name']
    summonerDict['Level'] = IDs['summonerLevel']
    if not elo:
        summonerDict['Rank'] = 'Unranked'
    else:
        summonerDict['Rank'] = elo[0]['tier'] + " " + elo[0]['rank']
        summonerDict['Vitorias'] = elo[0]['wins']
        summonerDict['Derrotas'] = elo[0]['losses']

    return summonerDict

