import discord
from discord.ext import commands


class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Tutorial for interacting with chatbot")
    async def help(self, ctx):
        await ctx.defer()
        help_message = """\
        /ai One-time conversation without memory
        /ask Continuous conversation with memory
        /erase to wipe the conversation memory
        /prompt to set the prompt
        """
        await ctx.respond(help_message)


def setup(bot):
    bot.add_cog(Chat(bot))
