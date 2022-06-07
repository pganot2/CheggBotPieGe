import discord 
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Client Code
# ANOTHER CHANGE
class Chegg(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.command()
    async def chegg(self, ctx, *link):
        chegglink = link[0]
        if chegglink[0:22] == "https://www.chegg.com/":
		
            r = requests.get(link[0],headers={"user-agent":"SET YOUR USER AGENT HERE",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"cookie":"id_token= SET ID TOKEN HERE"})
            source = BeautifulSoup(r.content,"html")
            dmain = source.find("div",attrs={"class":"answer-given-body ugc-base"})
            images = dmain.findAll('img')
            for image in images:
                await ctx.author.send(image['src'])
            await ctx.author.send('-----------------------------------------------------')
            data = source.find("div",attrs={"class":"answer-given-body ugc-base"}).text
            file = open('answer.txt', 'w')   
            file.write(data)  
            file.close()
            my_files = [discord.File('answer.txt')]
            print(link[0])
            await ctx.author.send(files=my_files)
        else:
            print("ERROR")
 

def setup(client):
    client.add_cog(Chegg(client))