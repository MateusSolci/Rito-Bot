import os
from dotenv import load_dotenv
from API_Requests.any_request import make_request
load_dotenv()


# retorna as informações de um determinado champion (por id)
def search_champion(id, champList): 
    for champ in champList["data"]:
        if champList["data"][champ]["key"] == str(id):
            champion = champList["data"][champ]
        else:
            pass

    return champion

# retorna a rotação semanal de campeões


def champ_rotation(origin):
    weekly_rotation = []
    champions_info_url = "http://ddragon.leagueoflegends.com/cdn/" + get_last_patch() + "/data/en_US/champion.json"
    
    ids_list = make_request(origin + "/lol/platform/v3/champion-rotations?api_key=" + os.environ.get('key'))
    champ_list = make_request(champions_info_url)

    for champ_id in ids_list["freeChampionIds"]:
        champ = search_champion(champ_id, champ_list)
        weekly_rotation.append(champ["name"])

    return "\n".join(weekly_rotation)

#retorna o ultimo patch note    
def get_last_patch():
    versions = 'https://ddragon.leagueoflegends.com/api/versions.json'
    
    parsed_versions = make_request(versions)

    return parsed_versions[0]

