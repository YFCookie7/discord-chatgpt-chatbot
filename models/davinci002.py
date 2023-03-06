import openai

def get_chat_response(user_prompt, OPENAI_TOKEN):
    openai.api_key = OPENAI_TOKEN

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_prompt,
        max_tokens=4000,
        temperature=0.7
    )

    
    return response