import os
import csv

import discord
from discord.ext.commands.errors import BadArgument, CommandNotFound
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot =  commands.Bot(command_prefix="$")

class ErrorHandler(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

class someCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.command()
    async def ping(ctx):
        await ctx.channel.send("pong")

    @bot.command()
    async def rule(ctx, arg):
        from bs4 import BeautifulSoup
        import requests
        import re
        url = "http://legionquickguide.com/#a"
        req = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        keyword=arg

        soup = BeautifulSoup(req.text, features="lxml")
        ##print(soup)

        #check for keyword on page
        ruleText = soup.find('div', {'id':keyword}).text.strip()
        print(ruleText)
        await ctx.channel.send("```" + ruleText + "```")


    @rule.error
    async def info_error(ctx, error):
        print(error)
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("Error parsing keyword")


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
    bot.add_cog(someCommands(bot))

bot.run(TOKEN)