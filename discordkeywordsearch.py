import os
import csv
from bs4.element import ResultSet

import math

from bs4 import BeautifulSoup
import requests
import re

import discord
from discord.ext.commands.errors import BadArgument, CommandNotFound
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot =  commands.Bot(command_prefix="$")

class errorHandler(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

class someCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.command()
    async def ping(ctx):
        # the test command
        await ctx.channel.send("pong")

    @bot.command()
    async def rule(ctx, arg):
        #look up a rule on legionquickguide, then post the result to discord chat

        url = "http://legionquickguide.com/#a"
        req = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'})
        keyword=arg

        soup = BeautifulSoup(req.text, features="lxml")
        ##print(soup)

        #check for keyword on page
        ruleText = soup.find('div', {'id':keyword}).text.strip()
        ruleText = ruleText.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ')
        #ruleText = re.sub('\\n+', ' ', ruleText)
        #ruleText = re.sub('\\r+', '\n', ruleText)
        #ruleText = re.sub('\\t+', ' ', ruleText)
        ruleText = re.sub(' +', ' ', ruleText)
        #figure out how long
        length = len(ruleText)
        print(ruleText)
        #initialize array to store equal parts
        equalStr = []
        #send the text if < 2000 chars
        if length < 2000:
            await ctx.channel.send("```" + ruleText + "```")
        else:
            n = math.ceil(length / 2000) + 1
            chars = int(length/n)
            print("n= ", n)
            print("chars=", chars)
            for i in range(0, length, chars):
                part = ruleText [i : i+chars]
                await ctx.channel.send("```" + part + "```")
                #print(part)
                    


    @rule.error
    async def info_error(ctx, error):
        print(error)
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send("Error parsing keyword")


def setup(bot: commands.Bot):
    bot.add_cog(errorHandler(bot))
    bot.add_cog(someCommands(bot))

bot.run(TOKEN)