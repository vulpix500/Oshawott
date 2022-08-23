import nextcord
import os
import time
import nextcord.ext
from nextcord.utils import get
from nextcord.ext import commands, tasks
from nextcord.ext.commands import has_permissions,  CheckFailure, check
from keep_alive import keep_alive
from nextcord import Interaction, SlashOption
#^ basic imports for other features of nextcord and python ^
#after making your bot on the discord dev portal go from here to the commands tab and then to "secrets" and then put the key as "TOKEN" and the value as your token

ts = 1008170816208388096

client = nextcord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    

@client.slash_command(guild_ids=[1008170816208388096], description="avatar")
async def avatar(interaction: Interaction, user: nextcord.Member = SlashOption(required=True)):
 member = user
 userAvatar = member.avatar.url
 embed = nextcord.Embed(title= f"nice avatar {member} ඞ",color=0x066aff)
 embed.set_image(url=userAvatar)
 await interaction.send(embed=embed)

@client.slash_command(guild_ids=[1008170816208388096],description="shows vulpixiias socials socials")
async def socials(interaction: Interaction):
 embed = nextcord.Embed(title="my socials",description=f"[tiktok](https://tiktok.com/@vulpix500) \n[youtube](https://youtube.com/channel/UCdJgEiYs--SVZbzTqVqEWzA)")
 await interaction.send(embed=embed)

@client.slash_command(guild_ids=[1008170816208388096], description="catch another user")
async def catch(interaction: Interaction, user: nextcord.Member = SlashOption(required=True)):
 embed = nextcord.Embed(title=f"you caught {user}",description=" ")
 embed.set_image(url="https://c.tenor.com/cGMxPS5GxxkAAAAd/pokemon-go.gif")
 await interaction.send(embed=embed)



  
#do not put any code under this # or you will get a error
keep_alive() #when you run the code there will be a 3rd tab called "web" copy the url at the top and put it into uptimerobot.com 
 
client.run(os.getenv("TOKEN"))