import os
from dotenv import load_dotenv
from API_Requests.any_request import *
load_dotenv()


class Champion():
# retorna as informações de um determinado champion (por id)
    def searchChampion(self, id, champList): 
        for champ in champList["data"]:
            if champList["data"][champ]["key"] == str(id):
                champion = champList["data"][champ]
            else:
                pass

        return champion

# retorna a rotação semanal de campeões
    def champRotation(self, origin):
        weekly_rotation = []
        champions_info_url = "http://ddragon.leagueoflegends.com/cdn/" + self.get_last_patch() + "/data/en_US/champion.json"
        
        ids_list = Resquest().makeRequest(origin + "/lol/platform/v3/champion-rotations?api_key=" + os.environ.get('key'))
        champ_list = Resquest().makeRequest(champions_info_url)

        for champ_id in ids_list["freeChampionIds"]:
            champ = self.searchChampion(champ_id, champ_list)
            weekly_rotation.append(champ["name"])

        return weekly_rotation

#retorna o ultimo patch note    
    def get_last_patch(self):
        versions = 'https://ddragon.leagueoflegends.com/api/versions.json'
        
        parsed_versions = Resquest().makeRequest(versions)

        return parsed_versions[0]

