import openai

def get_chat_response(conversation, OPENAI_TOKEN, mode):
    openai.api_key = OPENAI_TOKEN

    if (mode==0):
        response = openai.ChatCompletion.create (
            model="gpt-3.5-turbo",
            messages=[
                { "role": "user", "content": conversation }
            ]
        )
        return response
    elif (mode==1):
        response = openai.ChatCompletion.create (
            model="gpt-3.5-turbo",
            messages=conversation
        )
        conversation.append({"role": "assistant", "content": response.choices[0].message['content']})
        return response
        