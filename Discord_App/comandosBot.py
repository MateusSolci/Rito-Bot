import discord
from discord.ext import commands


class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def alo(self, ctx):
        await ctx.send("OI !")


def setup(client):
    client.add_cog(Comandos(client))