import openai

def get_chat_response(conversation, OPENAI_TOKEN, mode):
    openai.api_key = OPENAI_TOKEN

    if (mode==0):
        response = openai.ChatCompletion.create (
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                # {"role": "user", "content": "Who won the world series in 2020?"},
                # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                # {"role": "user", "content": "Where was it played?"}
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
        