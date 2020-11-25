import os
import discord
import time
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import API_Requests.champions_service as champion_service
import API_Requests.summoner as summoner
import Bot_Services.internal_services as internal_services
from datetime import datetime
from __main__ import AutoShardedBot
load_dotenv()


class Comandos(commands.Cog):
    riot_api_url = "https://br1.api.riotgames.com"

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def alo(self, ctx):
        embed = discord.Embed(colour = discord.Colour.gold())
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/leagueoflegends/images/d/dc/M%27Pengu_Emote.png/revision/latest?cb=20171121000318')
        embed.set_author(name='Saudações usuário')

        await ctx.send(embed=embed)

    @commands.command()
    async def rotation(self,ctx):
        embed = discord.Embed(colour = discord.Colour.gold())
        champs = champion_service.champ_rotation(self.riot_api_url)
        icons = champion_service.champ_icon(champs)
        for x in range(len(icons)):
            embed.set_author(name=champs[x])
            embed.set_image(url=icons[x])

            await ctx.send(embed=embed)
            time.sleep(0.5)
            

    @commands.command()
    async def invocador(self, ctx, nick):
        discord_id = ctx.message.author.id
        invocador = summoner.concat_info(self.riot_api_url, nick, discord_id)
        reponse = "Olá " + invocador['Nome'] + "!\nSua conta está nível " + str(invocador['Level'])

        if 'Unranked' in invocador.values():
            reponse += " sem rank no momento. "
        else:
            reponse += (" no rank " + invocador['Rank'] + "\n"
                        "Com " + str(invocador['Vitorias']) + " vitorias e " + str(invocador['Derrotas']) +
                        " derrotas nessa temporada!")
        if 'Level_Consultado' in invocador.keys():
            reponse += ("\nAnteriormente era level " + str(invocador['Level_Consultado']) + "!\n.\n.\n.\n" +
                        "Não lembra quando consultou? Eu lembro... foi em " + invocador['Data'].strftime("%d/%m/%Y") +
                        " (¬‿¬)...")
        await ctx.send(reponse)


    @commands.command()
    async def dance(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/753007614736203861/768559876019978310/alienPls.gif')

    @commands.command()
    async def info(self, ctx):
        await ctx.send(internal_services.get_bot_info())

    @commands.command()
    async def versao(self, ctx, version):
        await ctx.send(internal_services.get_version_details(version))

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(colour = discord.Colour.gold())
        embed.set_author(name='Meus Comandos', icon_url='https://images.emojiterra.com/twitter/512px/1f916.png')
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1b/Does_Not_Compute_Emote.png/revision/20171120235503')
        embed.add_field(name='-alo', value='saudações',inline=False)
        embed.add_field(name='-dance', value='Dança',inline=False)
        embed.add_field(name='-invocador', value='<nickname> | Retorna informações do jogador',inline=False)
        embed.add_field(name='-info', value='Informações dos desenvolvedores e da versão',inline=False)
        embed.add_field(name='-rotation', value='Rotação de campeões gratuítos da semana',inline=False)
        embed.add_field(name='-versao', value='<numero> | Detalhes da versão',inline=False)

        await ctx.send(embed=embed)

#------------------------------------------
def setup(client):
    client.add_cog(Comandos(client))
