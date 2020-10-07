import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def alo(self, ctx):
        await ctx.send("OI !")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

def setup(client):
    client.add_cog(Comandos(client))