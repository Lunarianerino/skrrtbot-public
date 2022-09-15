import discord
from discord.ext import commands
from collections import defaultdict
from discord import Spotify
import asyncio

currentsong = defaultdict(str)

class Spotify_Integration(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('4Allain is running :)')

    @commands.command()
    async def spotify(self, ctx, user: discord.Member=None):
        """ :Displays what song your playing on spotify (supposedly)"""
        #if not user:
            #user = message.author.id
        user = ctx.author
        userid = f'<@{ctx.author.id}>'
        for activity in user.activities:
            if isinstance(activity, Spotify):
                await ctx.send(f"{user} is listening to {activity.title} by {activity.artist}")
            #elif isintance(activity, !Spotify):
                #await ctx.send(f"{userid}, your're not listening to anything my dude")
        #sname = discord.Spotify.title
        #sartists = discord.Spotify.artists
        #album = discord.Spotify.album
        #palbum = discord.Spotify.album_cover_url
        #duration = discord.Spotify.duration
        #name = sname.fget()
        #message = ctx.send(name)
        #await message


def setup(client): #allows the cog to communicate with the bot
    client.add_cog(Spotify_Integration(client))
