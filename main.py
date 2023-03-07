import discord
from dotenv import load_dotenv
import os

from events.onMessage import onMessage
from events.onMessage import erase
from events.onReady import onReady
import json

from discord.ext import commands

# uncomfirmed
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
# bot = discord.Bot(intents=intents) #main worked, greeting dont, cog error
bot = commands.Bot(command_prefix="!", intents=intents) #@bot.command() doesnt, @bot.slashcommand() worked, 




#typing when loading?

# tree = app_commands.CommandTree(client)


# @tree.command(name = "help", description = "Tutorial of the chatbot", guild=discord.Object(id=729915471113224222)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def help_command(interaction):
#     await interaction.response.send_message("/ai One-time conversation without memory \n/ask Continuous conversation with memory \n/erase to wipe the restart conversation \n/model to select chat model ")

# @tree.command(name = "erase", description = "Erase conversation memory", guild=discord.Object(id=729915471113224222)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
# async def erase_command(interaction):
#     await erase()
#     await interaction.response.send_message(f'<@{interaction.user.id}>, chatbot memory erased! ')


# ai_models = Enum(value='ai_models', names=["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"])
# @tree.command(description='Select the model for the chatbot', guild=discord.Object(729915471113224222))
# @discord.app_commands.describe(model='Select the model for the chatbot')
# async def model(interaction: discord.Interaction, model: Enum(value='ai_models', names=["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"])):
#     user = interaction.user.id
#     with open('config.json', "r+") as f:
#         data = json.load(f)

#         if model.name == 'gpt-3.5-turbo':
#             data['default_model'] = 'gpt-3.5-turbo'
#             await interaction.response.send_message(f'<@{user}>, Model is switched to gpt-3.5-turbo!')
#         elif model.name == 'gpt-3.5-turbo-0301':
#             data['default_model'] = 'gpt-3.5-turbo-0301'
#             await interaction.response.send_message(f'<@{user}>, Model is switched to gpt-3.5-turbo-0301!')
#         elif model.name == 'text-davinci-003':
#             data['default_model'] = 'text-davinci-003'
#             await interaction.response.send_message(f'<@{user}>, Model is switched to text-davinci-003!')
#         elif model.name == 'text-davinci-002':
#             data['default_model'] = 'text-davinci-002'
#             await interaction.response.send_message(f'<@{user}>, Model is switched to text-davinci-002!')
        
#         f.seek(0)
#         json.dump(data, f, indent=4)
#         f.truncate()
    
# @bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
# async def ping(ctx): # a slash command will be created with the name "ping"
#     await ctx.respond(f"Pong! Latency is {bot.latency}")


# @bot.command()
# # pycord will figure out the types for you
# async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
#   # you can use them as they were actual integers
#   sum = first + second
#   await ctx.respond(f"The sum of {first} and {second} is {sum}.")


@bot.event
async def on_ready():
    await onReady(bot)


# async def get_animal_types(ctx: discord.AutocompleteContext):
#   """
#   Here we will check if 'ctx.options['animal_type']' is a marine or land animal and return respective option choices
#   """
#   animal_type = ctx.options['animal_type']
#   if animal_type == 'Marine':
#     return ['Whale', 'Shark', 'Fish', 'Octopus', 'Turtle']
#   else: # is land animal
#     return ['Snake', 'Wolf', 'Lizard', 'Lion', 'Bird']

# @bot.slash_command(name="animal")
# async def animal_command(
#   ctx: discord.ApplicationContext,
#   animal_type: discord.Option(str, choices=['Marine', 'Land']),
#   animal: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_animal_types))
# ):
#   await ctx.respond(f'You picked an animal type of `{animal_type}` that led you to pick `{animal}`!')
    

@bot.event
async def on_message(message):
    await onMessage(bot, message, OPENAI_TOKEN)

for filename in os.listdir('./cogs'): #for every folder in cogs
      if filename.endswith('.py') and not filename in ['util.py', 'error.py']: #if the file is a python file and if the file is a cog
          bot.load_extension(f'cogs.{filename[:-3]}')#load the extension


bot.load_extension('cogs.commands.chat')
bot.run(DISCORD_TOKEN)