import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", help_command=None, intents=intents)

for foldername in os.listdir("./cogs"):
    for filename in os.listdir(f"./cogs/{foldername}"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{foldername}.{filename[:-3]}")

bot.run(DISCORD_TOKEN)
