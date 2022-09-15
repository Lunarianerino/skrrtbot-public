import discord
from discord.ext import commands
import os
import sys

#pip install discord.py
#pip install pynacl
#pip install discord.py[voice]
#pip install NHentai-API

#if youtube_dl doesnt work:
#cd C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\
#python.exe -m pip install youtube_dl
#-m pip install pynacl

#https://www.youtube.com/watch?v=qjtmgCb8NcE << YT Tutorial for ffmpeg
client = commands.Bot(command_prefix = 'x') #for commands :) ex. !play on ry thm

x = 0

xtoken = open("token.txt")
for numbers in xtoken:
    token = numbers

#@client.command()
#async def load (ctx, extension):
#    client.load_extension(f'cogs.{extension}')  #goes into the cogs folder and looks for the cogs
#@client.command()
@client.event #function decorator denoting that function is representing an event
async def on_ready(): #runs when the bot is ready
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the world burn."))
    print(sys.executable)
    #if discord.id(x) == 354180424496447489:
        #await ctx.send('UwU')
    print('Bot is up!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.') #says everytime someone has joined a server


@client.event
async def on_member_remove(member): #when someone leaves or gets kicked from the server
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    """Check bot ping"""
    await ctx.send(f'Pong! {round(client.latency *1000)} ms')




#detects Allain's id and sends a message lmfaooo
#@client.event
#async def on_message (message):
#    channel = message.channel
#    if message.author.id == 354180424496447489:
#        await channel.send('FUCK YOU AND YOUR ELDERWOOD LEB')
#
#    await client.process_commands(message) #bot ignores commands and only executes on_message without this line



for filename in os.listdir('./cogs'): #loops for all the files and checks if its a py file
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') #removes the last 3 charactes (also loads the thingy)

client.run(token) #token (private shit cus other people can control ur shit when they have this)
