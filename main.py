import os
import discord
from discord import commands
import music

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup()

client = commands.Bot(command_prefix="?", intents= discord.Intents.all())

my_secret = os.environ['discordKey']
client.run(my_secret)