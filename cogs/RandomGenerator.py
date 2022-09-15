import discord
from discord.ext import commands
from collections import defaultdict
import asyncio
from NHentai import NHentai
import random

class Random_Generator(commands.Cog):
    """Just... Don't ask, please """

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Random Generator is running')

    class nhentai(commands.Cog):
        """Don't ask, please"""
        def __init__(self, client):
            self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('NHentai is running')


        @commands.command()
        async def gimme(self,ctx):
            """It gives random doujin, __**don't ask...**__"""
            nhentai = NHentai()
            random_doujin: Doujin = nhentai.get_random()
            while "english" not in random_doujin.languages:
                random_doujin: Doujin = nhentai.get_random()
            await ctx.send (f"Title: {random_doujin.title}")
            await ctx.send(f"Tags: {random_doujin.tags}")
            await ctx.send(f"Link: https://nhentai.net/g/{random_doujin.id}")

            await ctx.send(f"Image: {random_doujin.images[0]}")



        @commands.command()
        async def findme(self,ctx,* , arg):
            """If you want a specific tag ;)"""
            nhentai = NHentai()
            henlist = list()
            pages = 1
            while pages != 2:
                search_obj: SearchPage = nhentai.search(query=str(arg), sort='recent', page=pages)
                pages += 1
                for doujinthumbnail in search_obj.doujins:
                    henlist.append(doujinthumbnail)

            total = len(henlist) - 1
            number = random.randint(0, total)

            result = henlist[number]
            print(result)


            embed=discord.Embed(
            title= result.title,
                url= f"https://nhentai.net/g/{result.id}",
                description="Nut to this you filthy casual",
                color=discord.Color.blue())
            embed.set_thumbnail(url=result.cover)
            embed.add_field(name="Language", value=f"> {result.lang}", inline=False)
            embed.add_field(name="Link", value=f"> https://nhentai.net/g/{result.id}", inline=False)
            await ctx.send(embed=embed)




def setup(client): #allows the cog to communicate with the bot
    client.add_cog(Random_Generator(client))
def setup(client): #allows the cog to communicate with the bot
    client.add_cog(Random_Generator(client).nhentai(client))
