import discord
import os
from keep_alive import keep_alive 

client = discord.Client()



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='OVER LOB Esports'))
      
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
  if message.content.startswith("l&echo"):
    await message.channel.send(message.content[5:].format(message))
    await message.delete()

keep_alive()
client.run(os.getenv('TOKEN'))
