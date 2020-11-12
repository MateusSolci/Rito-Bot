import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import make_request
from Database_Controller.repository import update_last_search, get_level_by_summoner_id
from datetime import date
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
            top_mastery.append(x)
        
    return top_mastery


def live_game(origin, id):
    response = make_request(origin + "/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

    return response


def concat_info(origin, nick, discord_id):
    summonerDict = {}


    IDs = summoner_ids(origin, nick)
    elo = get_elo(origin, IDs['id'])
    mastery(origin, IDs['id'])

    print(elo)

    sumonner_level = IDs['summonerLevel']
    summoner_id = IDs['id']

    level_response = get_level_by_summoner_id(discord_id, summoner_id)
    prepare_query_for_level(discord_id, summoner_id, sumonner_level)

    if level_response != None:
        summonerDict['Level_Consultado'] = level_response[1]

    summonerDict['ID'] = summoner_id
    summonerDict['Ícone'] = IDs['profileIconId']
    summonerDict['Nome'] = IDs['name']
    summonerDict['Level'] = sumonner_level
    if not elo:
        summonerDict['Rank'] = 'Unranked'
    else:
        summonerDict['Rank'] = elo[0]['tier'] + " " + elo[0]['rank']
        summonerDict['Vitorias'] = elo[0]['wins']
        summonerDict['Derrotas'] = elo[0]['losses']

    return summonerDict


def prepare_query_for_level(discord_id, summoner_id, summoner_level):
    now = date.today().strftime("%d-%m-%Y")
    update_last_search(discord_id, summoner_id, summoner_level, now)