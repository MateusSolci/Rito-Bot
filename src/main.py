import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import AutoShardedBot
from API_Requests.summoner import *
import Bot_Services.internal_services as services

load_dotenv()

def main():
    modulos = ["discord_bot"]
    bot = AutoShardedBot(command_prefix='-', case_sensitive=True)

    @bot.event
    async def on_ready():
        print(bot.user.name + ' TA ONLINE!')
        await bot.change_presence(activity=discord.Game(name="-help"))

    for modulo in modulos:
        bot.load_extension(modulo)


    bot.run(os.environ.get('token'))


    riot_api_url = "https://br1.api.riotgames.com"
    print(mastery(riot_api_url, 'EUgXFufB1TLYM7dMlfJtCvqp2Kfn_icyR3iGIHfixeI8IkU'))




if __name__ == "__main__":
    main()
    

# PROXIMAS FUNÇÕES:
# - TOP 3 CHAMP MASTERY - /lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
# - ELO - /lol/league/v4/entries/by-summoner/{encryptedSummonerId}  - *CORRIGIR*
# - GAME AO VIVO - /lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}