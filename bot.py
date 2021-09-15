import os
import discord
from discord.ext.commands.errors import BadArgument, CommandNotFound
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot =  commands.Bot(command_prefix="$")

bot.load_extension("botcommands")
bot.load_extension("errorhandler")


bot.run(TOKEN)