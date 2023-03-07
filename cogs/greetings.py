import discord
from discord.ext import commands

class Greetings(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command() # creates a prefixed command
    async def hello(self, ctx): # all methods now must have both self and ctx parameters
        await ctx.send('Hello!')

    @discord.slash_command() # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.slash_command(description="Sends the bot's latency.") # this decorator makes a slash command
    async def ping(self, ctx): # a slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {self.bot.latency}")

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    async def get_animal_types(ctx: discord.AutocompleteContext):
        animal_type = ctx.options['animal_type']
        if animal_type == 'Marine':
            return ['Whale', 'Shark', 'Fish', 'Octopus', 'Turtle']
        else: # is land animal
            return ['Snake', 'Wolf', 'Lizard', 'Lion', 'Bird']

    @discord.slash_command(name="animal")
    async def animal_command( self,
    ctx: discord.ApplicationContext,
    animal_type: discord.Option(str, choices=['Marine', 'Land']),
    animal: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_animal_types))
    ):
        await ctx.respond(f'You picked an animal type of `{animal_type}` that led you to pick `{animal}`!')

    

    @commands.Cog.listener() # we can add event listeners to our cog
    async def on_member_join(self, member): # this is called when a member joins the server
    # you must enable the proper intents
    # to access this event.
    # See the Popular-Topics/Intents page for more info
        await member.send('Welcome to the server!')



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Greetings(bot)) # add the cog to the bot