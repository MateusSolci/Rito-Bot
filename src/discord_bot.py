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
    async def perfil(self, ctx, nick):
        discord_id = ctx.message.author.id
        invocador = summoner.concat_info(self.riot_api_url, nick, discord_id)
        embed = discord.Embed(colour=discord.Colour.gold())

        if invocador['Nome'] is None:
            embed.set_author(name='Nome de invocador não encontrado', icon_url='https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1b/Does_Not_Compute_Emote.png/revision/20171120235503')
            embed.set_footer(text='O nickname deve ser digitado sem espaços')

        else:
            embed.set_author(name='Perfil de: ' + invocador['Nome'], icon_url='https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1b/Does_Not_Compute_Emote.png/revision/20171120235503')
            embed.set_thumbnail(url='http://ddragon.leagueoflegends.com/cdn/'+ champion_service.get_last_patch() +'/img/profileicon/'+ str(invocador['Icone']) +'.png')

            embed.add_field(name='Nível: ',value=str(invocador['Level']),inline=True)
            if 'Unranked' in invocador.values():
                embed.add_field(name='Rankeada :', value='Sem rank no momento',inline=False)
            else:
                embed.add_field(name='Rankeada :', value='**'+ invocador['Rank'] +'**  -  '+ str(invocador['Pontos']) +'LP\n' +
                                str(invocador['Vitorias']) +'V / '+ str(invocador['Derrotas'])+ 'D \n'
                                'Média de vitória: **'+ str(int((invocador['Vitorias'] * 100) / (invocador['Derrotas'] + invocador['Vitorias']))) +'%**', inline=True)

            if 'Level_Consultado' in invocador.keys():
                embed.add_field(name='Última consulta em: ',value=str(invocador['Data'].strftime("%d/%m/%Y")) + '\n'
                                'Seu nível era: **'+ str(invocador['Level_Consultado']) +'**', inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def dance(self,ctx):
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_image(url='https://cdn.discordapp.com/attachments/753007614736203861/768559876019978310/alienPls.gif')

        await ctx.send(embed=embed)


    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/leagueoflegends/images/3/3a/Emote_Dabgu.png/revision/latest?cb=20191005175351&path-prefix=pt-br')
        embed.set_author(name=internal_services.get_bot_info())
        embed.set_footer(text='Para mais detalhes dessa versão use o comando -versao <versao>')

        await ctx.send(embed=embed)


    @commands.command()
    async def versao(self, ctx, version):
        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/leagueoflegends/images/c/c6/Emote_Fino.png/revision/latest/top-crop/width/220/height/220?cb=20191005173555&path-prefix=pt-br')
        embed.set_author(name=internal_services.get_version_details(version))

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(colour = discord.Colour.gold())
        embed.set_author(name='Meus Comandos', icon_url='https://images.emojiterra.com/twitter/512px/1f916.png')
        embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1b/Does_Not_Compute_Emote.png/revision/20171120235503')
        embed.add_field(name='-alo', value='saudações',inline=False)
        embed.add_field(name='-dance', value='Dança',inline=False)
        embed.add_field(name='-info', value='Informações dos desenvolvedores e da versão',inline=False)
        embed.add_field(name='-perfil', value='<nickname>(sem espaços) | Retorna informações do jogador',inline=False)
        embed.add_field(name='-rotation', value='Rotação de campeões gratuítos da semana',inline=False)
        embed.add_field(name='-versao', value='<numero> | Detalhes da versão',inline=False)

        await ctx.send(embed=embed)

#------------------------------------------
def setup(client):
    client.add_cog(Comandos(client))
