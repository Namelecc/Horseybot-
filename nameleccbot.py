import discord
import asyncio
import chess
import time
import random
client = discord.Client()
players = ["",""]
gameStarted = False
turn = random.randint(0,2)
board = chess.Board()
def prepareStart(player, x):
    global players
    players[x] = player
def resetgame():
    global players
    global turn
    global gameStarted
    players = ["",""]
    turn = random.randint(0,2)
    board.reset()
    gameStarted = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global players 
    global gameStarted
    global turn
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
        #global gameStarted
        if gameStarted == False:
            prepareStart(message.author.display_name, 0)
            await message.channel.send("Waiting for second player to join!")
            gameStarted = True
        else:
            await message.channel.send("A game has already been started")
    if message.content.casefold() == ".join":
        #global players
        if gameStarted == True:
            prepareStart(message.author.display_name, 1)
            if turn == 1:
                await message.channel.send("%s (White) and %s (Black) are playing chess! Woop woop!" % (str(players[1]), str(players[0])))
            elif turn == 0:
                await message.channel.send("%s (White) and %s (Black) are playing chess! Woop woop!" % (str(players[0]), str(players[1])))
            await message.channel.send("```\n" + str(board) + "\n```")
        else:
            await message.channel.send("Start a game first!") 
    if message.author.display_name in players:
        if message.content == "draw":
            if board.can_claim_draw == True:
                await message.channel.send("Game is a draw. What a bummer")
                resetgame()
            else:
                pass
        elif message.content in str(board.legal_moves):

            if message.author.display_name == players[0] and turn == 0:
            
                board.push_san(message.content)
                await message.channel.send("```\n" + str(board) + "\n```")
                turn = 1
                if board.is_checkmate == True:
                    await message.channel.send("Congrats! %s won the game!" % str(players[0]))
                    resetgame()

            if message.author.display_name == players[1] and turn == 1:
                board.push_san(message.content)
                await message.channel.send("```\n" + str(board) + "\n```")
                turn = 0
                if board.is_checkmate == True:
                    await message.channel.send("Congrats! %s won the game!" % str(players[1]))
                    resetgame()
                
        else:
            pass
    else:
        pass

    

        

client.run('xxxx')
