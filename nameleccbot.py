import discord
import asyncio
import chess
import time
import random
client = discord.Client()
players = ["",""]
gameStarted = False
def prepareStart(player, x):
    global players
    players[x] = player
def resetgame():
    global players
    players = ["",""]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    commandList = ".puzzle, .chessgame, .join"
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.casefold() == ".puzzle":
        await message.channel.send("https://lichess.org/training/daily")
    if message.content.casefold() == ".help":
        await message.channel.send("These are the commands I support! %s" % commandList)
    if message.content.casefold() == ".chessgame":
        global gameStarted
        if gameStarted == False:
            prepareStart(message.author.display_name, 0)
            await message.channel.send("Waiting for second player to join!")
            gameStarted = True
        else:
            await message.channel.send("A game has already been started")
    if message.content.casefold() == ".join":
        global players
        if gameStarted == True:
            prepareStart(message.author.display_name, 1)
            await message.channel.send("%s and %s are playing chess! Woop woop!" % (str(players[0]), str(players[1])))
        else:
            await message.channel.send("Start a game first!") 

    

        

client.run('xxxx')
