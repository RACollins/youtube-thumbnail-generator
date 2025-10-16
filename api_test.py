from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file from current/parent directories

api_key = os.getenv("API_KEY")  # Retrieve your API key
client = genai.Client(api_key=api_key)

prompt = """
Turn my image into a YouTube thumbnail.
Add silly text saying "Hello, I'm a banana!" to the image.
Make sure the text is in a funny font and the colours are bright and bold.
Make the scene isresistable to clickbait.
"""

image = Image.open("screenshot_of_me.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
