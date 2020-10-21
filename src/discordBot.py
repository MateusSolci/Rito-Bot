import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from API_Requests.ChampionsService import *
from API_Requests.summoner import *
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
        await ctx.send(Champion().champRotation(self.riot_api_url))

    @commands.command()
    async def invocador(self, ctx, nick):
        await ctx.send(Summoner().summonerInfo(self.riot_api_url, nick))

    @commands.command()
    async def nice(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/753007614736203861/768559876019978310/alienPls.gif')
    


def setup(client):
    client.add_cog(Comandos(client))