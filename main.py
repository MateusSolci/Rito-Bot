import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

# retorna o resultado de qualquer request em json
def makeRequest(url):
    try:
        response = requests.get(url).json()
    except:
        response = '*Bad Request*'

    return response

# retorna as informações de um determinado champion (por id)
def searchChampion(id, response): 
    for champ in response["data"]:
        if response["data"][champ]["key"] == str(id):
            champion = response["data"][champ]
        else:
            pass

    return champion

# retorna a rotação semanal de campeões
def champRotation(origin, champ_list):
    weekly_rotation = []
    url = origin + "/lol/platform/v3/champion-rotations?api_key=" + os.environ.get('key')

    response = requests.get(url).json()

    for champ_id in response["freeChampionIds"]:
        champ = searchChampion(champ_id, champ_list)
        weekly_rotation.append(champ["name"])

    return weekly_rotation


def main():
    riot_api_url = "https://br1.api.riotgames.com"
    champions_info_url = "http://ddragon.leagueoflegends.com/cdn/10.18.1/data/en_US/champion.json"

    champions_list = makeRequest(champions_info_url)


    print(champRotation(riot_api_url, champions_list))



if __name__ == "__main__":
    main()    