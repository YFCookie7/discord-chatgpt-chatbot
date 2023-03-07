import discord
import openai
import json

from models import gpt3pt5turbo
from models import gpt3pt5turbo0301
from models import davinci003
from models import davinci002

conversation = []

async def erase():
    global conversation
    conversation=[]

async def onMessage(client, message, OPENAI_TOKEN):
    global conversation


    if message.author == client.user:
        return

    if message.content.startswith('!testing'):
        await message.channel.send('Hello!')
        return

    words = message.content.split()
    words.pop(0)
    user_prompt = " ".join(words)
    
    if (message.content.split()[0] == "/ai"):
            
        with open('config.json', 'r') as f:
            data = json.load(f)
        default_model = data['default_model']

        # await client.change_presence(status=discord.Status.dnd)
        
        

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

        
        reply = reply + "\n\n(" + str(response["usage"]["total_tokens"]) + " token used)"
        await message.channel.send(reply)

        await client.change_presence(status=discord.Status.online)
        return
    if (message.content.split()[0] == "/ask"):
        print("loading")
        mode=1
        await client.change_presence(status=discord.Status.dnd)
        if (len(conversation) == 0):
            # conversation.append({"role": "system", "content": "You are a helpful assistant."})
            conversation.append({"role": "user", "content": user_prompt})
            response = gpt3pt5turbo.get_chat_response(conversation, OPENAI_TOKEN, mode)
            reply = response.choices[0].message['content']
            print(conversation)
        else:
            conversation.append({"role": "user", "content": user_prompt})
            response = gpt3pt5turbo.get_chat_response(conversation, OPENAI_TOKEN, mode)
            reply= response.choices[0].message['content']
            print(conversation)
        
        reply = reply + "\n\n(" + str(response["usage"]["total_tokens"]) + " token used)"
        await message.channel.send(reply)
        
        # await client.change_presence(status=discord.Status.online)
        return