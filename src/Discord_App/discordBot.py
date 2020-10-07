import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import AutoShardedBot
load_dotenv()

class RitoBot():
    def __init__(self, bot):
        self.bot = bot

    bot = AutoShardedBot(command_prefix='-')

    @bot.event
    async def on_ready(self):
        print(bot.user.name + ' TA ONLINE!')
        await bot.change_presence(activity=discord.Game(name="-help"))


    def start(self):
        return self.bot.run(os.environ.get('token'))
    
    @commands.command()
    async def alo(self, ctx):
        await ctx.send("OI !")

