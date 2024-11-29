from openai import OpenAI
from requests import get

client = OpenAI()

query = 'your query to generate an image'


response = client.images.generate(model="dall-e-3", prompt=query, n=1, size="1792x1024")

response_image = get(response.data[0].url)

with open("YouTube-Banner.png", "wb") as file:
    file.write(response_image.content)
