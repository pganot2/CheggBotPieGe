import discord 
from discord.ext import commands

# Client Code
# ANOTHER CHANGE
class Chegg(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.command()
    async def chegg(self, ctx, *link):
        await ctx.send(link)
        print(link)

def setup(client):
    client.add_cog(Chegg(client))