import os
import csv

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():

 guild = discord.utils.get(client.guilds, name=GUILD)

 print(
  f'{client.user} is connected to the following guild:\n'
  f'{guild.name}(id: {guild.id})'
 )
 
 channel=client.get_channel(833715975274627083)
 # print(channel)
 
 data=[]
 with open("update.csv") as csvfile:
  reader = csv.reader(csvfile, delimiter="\t")
  for line in reader:
   data.append(line)   

 print(data)
 for col in data:
    await channel.send(col)
    
client.run(TOKEN)