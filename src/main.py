import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from API_Requests.ChampionsService import *
from API_Requests.summoner import *
from Discord_App.discordBot import *

load_dotenv()


def main():
    riot_api_url = "https://br1.api.riotgames.com"
    
    modulos = ["Comandos"]
    bot = AutoShardedBot(command_prefix='-')

    @bot.event
    async def on_ready(self):
        print(bot.user.name + ' TA ONLINE!')
        await bot.change_presence(activity=discord.Game(name="-help"))

    for modulo in modulos:
        bot.load_extension(modulo)

    bot.run(os.environ.get('token'))    


    # champRotation = Champion().champRotation(riot_api_url)
    # print(Summoner().summonerInfo(riot_api_url, "To Voante"))

if __name__ == "__main__":
    main()
    


# PROXIMAS FUNÇÕES:
# - TOP 3 CHAMP MASTERY - /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
# - ELO - /lol/league/v4/entries/by-summoner/{encryptedSummonerId}  
# - GAME AO VIVO - /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}
