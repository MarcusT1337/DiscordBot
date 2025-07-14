import os
import discord
from dotenv import load_dotenv

#Aquiring discord token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client() #Loads the client
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord whoohoo!')

client.run(TOKEN)