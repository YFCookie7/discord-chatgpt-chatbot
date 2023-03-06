import discord

from discord import app_commands

async def onReady(client, tree):
    print('Logged in as {0.user}'.format(client))
    
    await tree.sync(guild=discord.Object(id=729915471113224222))





    channel = client.get_channel(1072860367526559744)
    await channel.send("Hello! Bot is ready!")

