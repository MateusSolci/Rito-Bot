import discord
from discord.ext.commands import AutoShardedBot

class RitoBot():
    token = 'NzYxMjExNzU1MTk1MjY5MTQw.X3XTsQ.8XGiLBcmfhDRVJiYVAYbogT0yFs'

    bot = AutoShardedBot(command_prefix='-')

    @bot.event
    async def on_ready(self):
        print(bot.user.name + ' TA ONLINE!')
        await bot.change_presence(activity=discord.Game(name="-help"))


    def start(self):
        return self.bot.run('NzYxMjExNzU1MTk1MjY5MTQw.X3XTsQ.8XGiLBcmfhDRVJiYVAYbogT0yFs')

