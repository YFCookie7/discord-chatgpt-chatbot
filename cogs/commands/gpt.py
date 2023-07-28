import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
openai.api_key = OPENAI_TOKEN


class GPT(commands.Cog):
    conversation = []
    GPT_MODEL = "gpt-3.5-turbo"

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Predefine bot's behavior")
    async def prompt(
        self, ctx, prompt: discord.Option(discord.SlashCommandOptionType.string)
    ):
        GPT.conversation = [{"role": "system", "content": prompt}]
        await ctx.respond(f"New prompt: `{prompt}`.")

    @discord.slash_command(description="Erase Conversation Memory")
    async def erase(self, ctx):
        await ctx.defer()
        GPT.conversation = []
        await ctx.respond(f"{ctx.author.mention}, ChatBot memory erased!")

    @discord.slash_command(description="ask a one time question")
    async def ai(
        self, ctx, user_message: discord.Option(discord.SlashCommandOptionType.string)
    ):
        await ctx.defer()
        response = openai.ChatCompletion.create(
            model=GPT.GPT_MODEL, messages=[{"role": "user", "content": user_message}]
        )
        await ctx.respond(response["choices"][0]["message"]["content"])

    @discord.slash_command(description="ask questions in a conversation")
    async def ask(
        self, ctx, user_message: discord.Option(discord.SlashCommandOptionType.string)
    ):
        await ctx.defer()
        if len(GPT.conversation) == 0:
            GPT.conversation.append(
                {"role": "system", "content": "You are a helpful assistant."}
            )

        GPT.conversation.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model=GPT.GPT_MODEL, messages=GPT.conversation
        )
        GPT.conversation.append(
            {
                "role": "assistant",
                "content": response["choices"][0]["message"]["content"],
            }
        )
        await ctx.respond(response["choices"][0]["message"]["content"])


def setup(bot):
    bot.add_cog(GPT(bot))
