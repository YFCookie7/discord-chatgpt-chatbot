import openai

def get_image_response(user_prompt, OPENAI_TOKEN):
    openai.api_key = OPENAI_TOKEN

    response = openai.Image.create(
        prompt=user_prompt,
        n=1,
        size="1024x1024"
        )
    image_url = response['data'][0]['url']
    return image_url