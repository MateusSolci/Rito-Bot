import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import API_Requests.champions_service as champion_service
import API_Requests.summoner as summoner
import Bot_Services.internal_services as internal_services
load_dotenv()

class Comandos(commands.Cog):
    riot_api_url = "https://br1.api.riotgames.com"
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def alo(self, ctx):
        await ctx.send("OI !")
    
    @commands.command()
    async def rotation(self,ctx):
        await ctx.send(champion_service.champ_rotation(self.riot_api_url))

    @commands.command()
    async def invocador(self, ctx, nick):
        invocador = summoner.concat_info(self.riot_api_url, nick)
        reponse = ""

        if 'Unranked' in invocador.values():
            reponse = ("Olá " + invocador['Nome'] + "!\n"
                        "Sua conta está nível " + str(invocador['Level']) + " sem rank no momento. ")
        else:
            reponse = ("Olá " + invocador['Nome'] + "!\n"
                        "Sua conta está nível " + str(invocador['Level']) + " no rank " + invocador['Rank'] + "\n"
                        "Com " + str(invocador['Vitorias']) + " vitorias e " + str(invocador['Derrotas']) + " derrotas nessa temporada!")

        await ctx.send(reponse)

    @commands.command()
    async def nice(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/753007614736203861/768559876019978310/alienPls.gif')

    @commands.command()
    async def info(self, ctx):
        await ctx.send(internal_services.get_bot_info())

    @commands.command()
    async def versao(self, ctx, version):
        await ctx.send(internal_services.get_version_details(version))
    


def setup(client):
    client.add_cog(Comandos(client))