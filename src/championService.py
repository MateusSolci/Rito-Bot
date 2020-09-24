from src.api import makeRequest
import os

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

    response = makeRequest(url)

    for champ_id in response["freeChampionIds"]:
        champ = searchChampion(champ_id, champ_list)
        weekly_rotation.append(champ["name"])

    return weekly_rotation
