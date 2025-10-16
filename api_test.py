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
- Create a YouTube thumbnail from the images that I have provided.
- Use the outline image to create the thumbnail.
- Make sure my face is clearly used for the character in the scene.
- Make the scene isresistable to clickbait.
- Follow YouTube spec on size and aspect ratio.
"""

outline_image = Image.open("outline.png")
face_image = Image.open("screenshot_of_me.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, outline_image, face_image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
