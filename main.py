import discord 
import chegg
from discord.ext import commands

cogs = [chegg]
command_prefix = '?'
activity = discord.Activity(type=discord.ActivityType.competing, name = "?cheggbotpiege")
client = commands.Bot(command_prefix, intents = discord.Intents.all(), activity = activity)

for i in range(len(cogs)):
    cogs[i].setup(client)

TOKEN = 'OTY0MDk2MTE5NTk4NjM3MDU2.GzrRvi.ASFBaF72FuWNTrl6RQmhjMTkzvoIY_jguiOM5w'

# WE'RE IN A NEW BRANCH NOW

client.run(TOKEN)
print(TOKEN)
