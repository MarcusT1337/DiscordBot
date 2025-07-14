import os
import discord
from dotenv import load_dotenv
import random
#Aquiring discord token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents) #Loads the client with default intents
#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord whoohoo!')
#client.run(TOKEN)
#All this does is connect to the discord server and print a message when it is connected.
#Lets try cooking a bit more
test = discord.Client.guilds
print(test)
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, id=int(GUILD))
    print(guild)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

#Cool, its printing Guild name and ID, lets fucking ball with some Messages.
@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.author == client.user:#prevent the bot from responding to its own messages
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
#Cool, that all runs. Make a bot do it instead!
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents = intents, help='Responds with a random quote from Brooklyn 99') #Sets the command for bot activation as !
@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='counterpick', help='Checks U.GG for counterpicks')
async def counterpick(ctx)



    await ctx.send(counterpick)



bot.run(TOKEN)

#client.run(TOKEN)