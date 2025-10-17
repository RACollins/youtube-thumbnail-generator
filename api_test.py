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
- Create a YouTube thumbnail from the image that I have provided.
- Convert the screenshot into an impressionistic style, as if Monet himself had painted it.
- Make sure the image is in the correct size and aspect ratio.
- Make sure the image is in the correct format.
- I want captions around the image to be clickbait friendly. Don't hold back on the clickbait titles.
- Text should read "tormenting myself with this YouTube thumbnail generator".
"""

face_image = Image.open("images/input/screenshot_2025-10-17.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, face_image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("images/output/generated_image.png")
