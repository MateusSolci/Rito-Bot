import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import make_request
from Database_Controller.repository import update_last_search, get_level_by_summoner_id
from datetime import date
load_dotenv()

api_key_parameter = "?api_key=" + os.environ.get('key')


# retorna informações do invocador, a partir do nickname
def summoner_ids(origin, nick):
    response = make_request(origin + "/lol/summoner/v4/summoners/by-name/" + nick + api_key_parameter)

    return response


def get_elo(origin, id):
    response = make_request(origin + "/lol/league/v4/entries/by-summoner/" + id + api_key_parameter)

    return response


def mastery(origin, id):
    top_mastery = []
    count = 0
    response = make_request(origin + "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + api_key_parameter)

    for x in response:
        if(count == 3):
            break
        else:
            count += 1
            top_mastery.append(x)

    return top_mastery


def live_game(origin, id):
    response = make_request(origin + "/lol/spectator/v4/active-games/by-summoner/" + id + api_key_parameter)

    return response


def concat_info(origin, nick, discord_id):
    summonerDict = {}
    indice_elo = 0
    IDs = summoner_ids(origin, nick)

    if 'status' in IDs.keys():
        summonerDict['Nome'] = None
        return summonerDict

    elo = get_elo(origin, IDs['id'])

    summoner_level = IDs['summonerLevel']
    summoner_id = IDs['id']

    level_response = get_level_by_summoner_id(discord_id, summoner_id)

    prepare_query_for_level(discord_id, summoner_id, summoner_level)

    if level_response is not None:
        summonerDict['Level_Consultado'] = level_response[1]
        summonerDict['Data'] = level_response[3]

    summonerDict['ID'] = summoner_id
    summonerDict['Icone'] = IDs['profileIconId']
    summonerDict['Nome'] = IDs['name']
    summonerDict['Level'] = summoner_level
    if not elo:
        summonerDict['Rank'] = 'Unranked'
    else:
        if 'RANKED_SOLO_5x5' in elo[0].values():
            indice_elo = 0
        else:
            indice_elo = 1

        summonerDict['Rank'] = elo[indice_elo]['tier'] + " " + elo[indice_elo]['rank']
        summonerDict['Pontos'] = elo[indice_elo]['leaguePoints']
        summonerDict['Vitorias'] = elo[indice_elo]['wins']
        summonerDict['Derrotas'] = elo[indice_elo]['losses']

    return summonerDict


def prepare_query_for_level(discord_id, summoner_id, summoner_level):
    now = date.today().strftime("%Y-%m-%d")
    update_last_search(discord_id, summoner_id, summoner_level, now)
