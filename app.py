import os
import discord
from dotenv import load_dotenv
import random
import json
import requests
#Aquiring discord token from the .env file
load_dotenv()
#From here down we set up the chatbot
# We are essentially making a POST request to one endpoint and we create a convenience Class to pass in prompts, temperature and model.

groq_api_key = os.getenv("GROQ_API_KEY")
MODEL = "llama-3.3-70b-versatile"
SYSTEM_PROMPT = os.getenv("SYSTEM_MESSAGE")

class MyCustomOpenAI:

    def __init__(self, system_prompt=None, temperature=1.0, model=MODEL):
        self.model_endpoint = "https://api.groq.com/openai/v1/chat/completions"
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        self.api_key = groq_api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
    def generate_text(self, prompt):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": False,  # no streaming or output
            "temperature": self.temperature,
        }
        # Use HTTP POST method from Requests library

        # In future examples we will use OpenAI library instead of requests directly but this is for demo purposes.
        response = requests.post(
            url=self.model_endpoint, headers=self.headers, data=json.dumps(payload)
        ).json()
        return response

client = MyCustomOpenAI(
    model=MODEL,
    system_prompt=SYSTEM_PROMPT,
    temperature=0.0,
)

response = client.generate_text(
    "What is an the difference between Data Science, Data Engineering and Data Analysis?"
)

#From here down is the discord bot




TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True


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
async def counterpick(ctx, champion: str, lane: str):
    response = client.generate_text(champion + lane)
    counterpick = response["choices"][0]["message"]["content"]

    await ctx.send(counterpick)



bot.run(TOKEN)

#client.run(TOKEN)