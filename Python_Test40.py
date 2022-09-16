"""
try to make a discord bot
"""

import discord


client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('hi'):
            await message.channel.send('Hi there!')
        else:
            print("1")

client.run(token)