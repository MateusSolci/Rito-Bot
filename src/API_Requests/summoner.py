import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import *
load_dotenv()

class Summoner():
# retorna informações do invocador, a partir do nickname
    def summonerIDs(self, origin, nick):
        response = Request().makeRequest(origin + "/lol/summoner/v4/summoners/by-name/" + nick + "?api_key=" + os.environ.get('key'))

        return response


    def getElo(self, origin, id):
        response = Request().makeRequest(origin + "/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

        return response


    def mastery(self, origin, id):
        response = Request().makeRequest(origin + "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

        return response

    
    def liveGame(self, origin, id):
        response = Request().makeRequest(origin + "/lol/spectator/v4/active-games/by-summoner/" + id + "?api_key=" + os.environ.get('key'))

        return response
    

    def summonerInfo(self, origin, nick):
        IDs = Summoner().summonerIDs(origin, nick)
        elo = Summoner().getElo(origin, IDs['id'])
        mastery = Summoner().mastery(origin, IDs['id'])

        summonerJson = {}

        return summonerJson
