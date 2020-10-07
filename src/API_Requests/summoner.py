import requests
import json
import os
from dotenv import load_dotenv
from API_Requests.any_request import *
load_dotenv()

class Summoner():
# retorna informações do invocador, a partir do nickname
    def summonerInfo(self, origin, nick):
        response = Resquest().makeRequest(origin + "/lol/summoner/v4/summoners/by-name/" + nick + "?api_key=" + os.environ.get('key'))

        return response 