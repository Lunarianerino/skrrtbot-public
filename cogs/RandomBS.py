import discord
from discord.ext import commands

class RandomBS(commands.Cog): #important: inherit from commands.Cog

    def __init__(self, client):
        self.client = client #allows access of client within cog

    @commands.Cog.listener() #function decorator for within a cog (just like client.event)
    async def on_ready(self): #has to have self because it is in a class :)
        print('RandomBS is running :)')


#==========================Commands==============================================
    @commands.command() #function decorator for commands
    async def skrrt(self, ctx): #you can name it any name you want, ctx (context) is passed in automatically
        """ :SKRRT SKRRT"""
        await ctx.send('skrrt skrrt')

    @commands.command()
    async def allain(self, ctx):
        """ :Use this command, ALL THE TIME"""
        await ctx.send('UwU')
        print(ctx.author.id)


def setup(client): #allows the cog to communicate with the bot
    client.add_cog(RandomBS(client))
