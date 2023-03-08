import discord
from discord.ext import commands
import json
import traceback


from models import gpt3pt5turbo
from models import gpt3pt5turbo0301
from models import davinci003
from models import davinci002

from dotenv import load_dotenv
import os
load_dotenv() 
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')


class Ai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ai(self, ctx, *args):
        global conversation
        user_prompt = " ".join(args)

        with open('config.json', 'r') as f:
            data = json.load(f)
        default_model = data['default_model']

        await self.bot.change_presence(status=discord.Status.dnd)
        await ctx.channel.trigger_typing()
        try:
            if (default_model=="gpt-3.5-turbo"):
                mode = 0
                response = gpt3pt5turbo.get_chat_response(user_prompt, OPENAI_TOKEN, mode)
                reply = response.choices[0].message['content']
            
            elif (default_model=="gpt-3.5-turbo-0301"):
                response = gpt3pt5turbo0301.get_chat_response(user_prompt, OPENAI_TOKEN)
                reply = response.choices[0].message['content']

            elif (default_model=="text-davinci-003"):
                response = davinci003.get_chat_response(user_prompt, OPENAI_TOKEN)
                reply = response["choices"][0]["text"]
            
            elif (default_model=="text-davinci-002"):
                response = davinci002.get_chat_response(user_prompt, OPENAI_TOKEN)
                reply = response["choices"][0]["text"]
        except Exception as e:
            await ctx.channel.send(traceback.format_exc())
            print("\n\n\n\n\n\n")
            print(traceback.format_exc())

        
        reply = reply + "\n\n(" + str(response["usage"]["total_tokens"]) + " token used)"
        await ctx.channel.send(reply)

        await self.bot.change_presence(status=discord.Status.online)
        return



def setup(bot):
    bot.add_cog(Ai(bot))