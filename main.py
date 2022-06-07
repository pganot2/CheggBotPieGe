import discord 
import chegg
from discord.ext import commands

cogs = [chegg]
command_prefix = '?'
activity = discord.Activity(type=discord.ActivityType.competing, name = "?cheggbotpiege")
client = commands.Bot(command_prefix, intents = discord.Intents.all(), activity = activity)

for i in range(len(cogs)):
    cogs[i].setup(client)

TOKEN = 'ENCRYPTED TOKEN MF'

# WE'RE IN A NEW BRANCH NOW

client.run(TOKEN)
print(TOKEN)
