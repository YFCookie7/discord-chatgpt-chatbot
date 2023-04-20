import discord
from discord.ext import commands
from cogs.commands.ask import erase
from cogs.commands.ask import update_prompt
import openai

from models import imageAI

from dotenv import load_dotenv
import os
load_dotenv() 
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

class Imagine(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="imagine", description="AI generate a picture")
    async def imagine(self,
        ctx,
        user_prompt: discord.Option(discord.SlashCommandOptionType.string)
    ):
        await ctx.respond("Loading...")
        url= imageAI.get_image_response(user_prompt, OPENAI_TOKEN)
        print(url)
        await ctx.edit(content=f'Here is your generated image: {url}')


def setup(bot):
    bot.add_cog(Imagine(bot))