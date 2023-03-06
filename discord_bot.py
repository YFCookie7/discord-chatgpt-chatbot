import discord
from dotenv import load_dotenv
import os
from events.onMessage import onMessage
from events.onMessage import erase
from events.onReady import onReady
import json



# uncomfirmed
from discord.ext import commands
from discord import app_commands
from enum import Enum



# load .env
load_dotenv() 
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

# Intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
client = discord.Client(intents=intents, help_command=None)




tree = app_commands.CommandTree(client)


@tree.command(name = "help", description = "Tutorial of the chatbot", guild=discord.Object(id=729915471113224222)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def help_command(interaction):
    await interaction.response.send_message("/ai One-time conversation without memory \n/ask Continuous conversation with memory \n/erase to wipe the restart conversation \n/model to select chat model ")

@tree.command(name = "erase", description = "Erase conversation memory", guild=discord.Object(id=729915471113224222)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def erase_command(interaction):
    await erase()
    await interaction.response.send_message(f'<@{interaction.user.id}>, chatbot memory erased! ')


# ai_models = Enum(value='ai_models', names=["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"])
@tree.command(description='Select the model for the chatbot', guild=discord.Object(729915471113224222))
@discord.app_commands.describe(model='Select the model for the chatbot')
async def model(interaction: discord.Interaction, model: Enum(value='ai_models', names=["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"])):
    user = interaction.user.id
    with open('config.json', "r+") as f:
        data = json.load(f)

        if model.name == 'gpt-3.5-turbo':
            data['default_model'] = 'gpt-3.5-turbo'
            await interaction.response.send_message(f'<@{user}>, Model is switched to gpt-3.5-turbo!')
        elif model.name == 'gpt-3.5-turbo-0301':
            data['default_model'] = 'gpt-3.5-turbo-0301'
            await interaction.response.send_message(f'<@{user}>, Model is switched to gpt-3.5-turbo-0301!')
        elif model.name == 'text-davinci-003':
            data['default_model'] = 'text-davinci-003'
            await interaction.response.send_message(f'<@{user}>, Model is switched to text-davinci-003!')
        elif model.name == 'text-davinci-002':
            data['default_model'] = 'text-davinci-002'
            await interaction.response.send_message(f'<@{user}>, Model is switched to text-davinci-002!')
        
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    


@client.event
async def on_ready():
    await onReady(client, tree)
    

@client.event
async def on_message(message):
    await onMessage(client, message, OPENAI_TOKEN)


client.run(DISCORD_TOKEN)