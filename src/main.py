from src.api import makeRequest
from src.championService import champRotation
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

def main():
    riot_api_url = "https://br1.api.riotgames.com"
    champions_info_url = "http://ddragon.leagueoflegends.com/cdn/10.18.1/data/en_US/champion.json"

    champions_list = makeRequest(champions_info_url)


    print(champRotation(riot_api_url, champions_list))



if __name__ == "__main__":
    main()    