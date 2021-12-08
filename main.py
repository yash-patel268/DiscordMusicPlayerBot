import os
import discord
from discord import commands

client = commands.Bot(command_prefix="?", intents= discord.Intents.all())

my_secret = os.environ['discordKey']
client.run(my_secret)