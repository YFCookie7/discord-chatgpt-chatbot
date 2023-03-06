import openai

def get_chat_response(user_prompt, OPENAI_TOKEN):
    openai.api_key = OPENAI_TOKEN

    response = openai.ChatCompletion.create (
        model="gpt-3.5-turbo-0301",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            # {"role": "user", "content": "Where was it played?"}
            { "role": "user", "content": user_prompt }
        ]
    )
    return response