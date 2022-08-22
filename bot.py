from http import client
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('>>Bot is online<<')

bot.run('MTAxMTMwNzE4MjcyNzM4MTAyMg.GvBAfc.9aM8KZv_FHK1p6oIogdN3AjDRLE93mJ3C6WigY')