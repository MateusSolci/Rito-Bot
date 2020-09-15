import requests
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

# retorna as informações de um determinado champion (por id)
def buscaChampion(id): 
    url = "http://ddragon.leagueoflegends.com/cdn/10.18.1/data/en_US/champion.json"

    response = requests.get(url).json()

    for champ in response["data"]:
        if response["data"][champ]["key"] == str(id):
            champion = response["data"][champ]
        else:
            pass

    return champion


def main():
    id_champion = 82    
    
    champ = buscaChampion(id_champion)

    print(champ)




if __name__ == "__main__":
    main()    