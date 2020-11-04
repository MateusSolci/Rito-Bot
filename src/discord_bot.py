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
        await ctx.send(summoner.summoner_info(self.riot_api_url, nick))

    @commands.command()
    async def nice(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/753007614736203861/768559876019978310/alienPls.gif')

    @commands.command()
    async def info(self, ctx):
        await ctx.send(internal_services.get_bot_info())
    


def setup(client):
    client.add_cog(Comandos(client))