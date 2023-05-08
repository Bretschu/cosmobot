import discord
from discord.ext import commands

from Token.get_token import get_tok

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('Bot start')

client.run(get_tok())
