import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import AutoShardedBot
load_dotenv()

class RitoBot():
    bot = AutoShardedBot(command_prefix='-')

    @bot.event
    async def on_ready():
        print(bot.user.name + ' TA ONLINE!')
        await bot.change_presence(activity=discord.Game(name="-help"))


    def start(self):
        return self.bot.run(os.environ.get('token'))

