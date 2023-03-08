import discord
from discord.ext import commands
from cogs.commands.ask import erase
from cogs.commands.ask import update_prompt
import json

class Chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Tutorial for interacting with chatbot")
    async def help(self ,ctx):
        await ctx.defer()
        await ctx.respond("/ai One-time conversation without memory \n/ask Continuous conversation with memory \n/erase to wipe the restart conversation \n/model to select chat model ")


    @discord.slash_command(name="prompt", description="Predefine bot's behavior")
    async def prompt(self,
        ctx,
        prompt: discord.Option(discord.SlashCommandOptionType.string)
    ):
        await update_prompt(prompt)
        await ctx.respond(f"New prompt: `{prompt}`.")


    @discord.slash_command(description="Erase Conversation Memory")
    async def erase(self, ctx):
        await ctx.defer()
        await erase()
        await ctx.respond(f"{ctx.author.mention}, ChatBot memory erased!")


    async def get_ai_model(ctx: discord.AutocompleteContext):
        return ["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "text-davinci-002"]

    @discord.slash_command(name="model", description="Select AI Model")
    async def model_command( self,
    ctx: discord.ApplicationContext,
    ai_model: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(get_ai_model), description="Select AI Model", required = False, default = '')
    ):
        await ctx.defer()
        with open('config.json', "r+") as f:
            data = json.load(f)

            
            if (ai_model!=''):
                data['default_model'] = ai_model
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                await ctx.respond(f'{ctx.author.mention}, Chatbot model is switched to `{ai_model}`!')
                return
            curr_model=data['default_model']
            await ctx.respond(f'{ctx.author.mention}, The current chatbot model is `{curr_model}`!')


    

def setup(bot):
    bot.add_cog(Chat(bot))