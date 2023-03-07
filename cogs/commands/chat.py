import discord
from discord.ext import commands
from events.onMessage import erase

class Chat(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
    async def erase(self, ctx): # a slash command will be created with the name "ping"
        await erase()
        await ctx.respond(f"ChatBot memory erased!")


    async def get_ai_model(ctx: discord.AutocompleteContext):
        ai_model = ctx.options['ai_model']
        if ai_model == 'Marine':
            return ['Whale', 'Shark', 'Fish', 'Octopus', 'Turtle']
        else: # is land animal
            return ['Snake', 'Wolf', 'Lizard', 'Lion', 'Bird']

    @discord.slash_command(name="animal")
    async def animal_command(
    ctx: discord.ApplicationContext,
    ai_model: discord.Option(str, choices=['Marine', 'Land']),
    animal: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_ai_model))
    ):
        await ctx.respond(f'You picked an model type of `{ai_model}`!')


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Chat(bot)) # add the cog to the bot