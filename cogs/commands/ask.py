import discord
from discord.ext import commands

from models import gpt3pt5turbo

from dotenv import load_dotenv
import os
load_dotenv() 
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

conversation = []

async def erase():
    global conversation
    conversation=[]

async def update_prompt(prompt):
    global conversation
    conversation=[{"role": "system", "content": prompt}]

class Ask(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ask(self, ctx, *args):
        global conversation
        user_prompt = " ".join(args)

        mode=1
        await self.bot.change_presence(status=discord.Status.dnd)
        await ctx.channel.trigger_typing()
        if (len(conversation) == 0):
            # conversation.append({"role": "system", "content": "You are a helpful assistant."})
            conversation.append({"role": "user", "content": user_prompt})
            response = gpt3pt5turbo.get_chat_response(conversation, OPENAI_TOKEN, mode)
            reply = response.choices[0].message['content']
        else:
            conversation.append({"role": "user", "content": user_prompt})
            response = gpt3pt5turbo.get_chat_response(conversation, OPENAI_TOKEN, mode)
            reply= response.choices[0].message['content']
        
        reply = reply + "\n\n(" + str(response["usage"]["total_tokens"]) + " token used)"
        await ctx.send(reply)
        
        await self.bot.change_presence(status=discord.Status.online)
        return


def setup(bot):
    bot.add_cog(Ask(bot))