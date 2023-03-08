import openai

def get_chat_response(user_prompt, OPENAI_TOKEN):
    openai.api_key = OPENAI_TOKEN

    response = openai.ChatCompletion.create (
        model="gpt-3.5-turbo-0301",
        messages=[
            { "role": "user", "content": user_prompt }
        ]
    )
    return response