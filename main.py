from dotenv import load_dotenv
from API_Resquests.champions import *
from API_Resquests.summoner import *
load_dotenv()


def main():
    riot_api_url = "https://br1.api.riotgames.com"

    champRotation = Champion().champRotation(riot_api_url)
    
    print(Summoner().summonerInfo(riot_api_url, "To Voante"))


if __name__ == "__main__":
    main()    


# PROXIMAS FUNÇÕES:
# - TOP 3 CHAMP MASTERY - /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
# - ELO - /lol/league/v4/entries/by-summoner/{encryptedSummonerId}  
# - GAME AO VIVO - /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}
