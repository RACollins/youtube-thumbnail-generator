import streamlit as st
from PIL import Image
from io import BytesIO
from google import genai
from prompts.prompt_manager import PromptManager


class MainPage:
    def __init__(self):
        self.title = "YouTube Thumbnail Generator"
        self.description = "This app generates YouTube thumbnails using AI."

    def check_image_file(self, img_file):
        if img_file is not None:
            img_original = Image.open(img_file)
            # Check session state for image file
            if "img_original" not in st.session_state:
                st.session_state["img_original"] = img_original
            else:
                img_original = st.session_state["img_original"]
        else:
            st.info("☝️ Upload a .jpg or .png file")
            return None
        return img_original

    def render_file_uploader(self):
        st.title(self.title)
        st.write(self.description)

        img_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
        img_original = self.check_image_file(img_file)

        if img_original is not None:
            return img_original
        else:
            return None

    def generate_image(self, img_original, user_prompt):
        client = genai.Client(api_key=st.session_state["api_key"])
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[user_prompt, img_original],
        )
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                modified_image = Image.open(BytesIO(part.inline_data.data))
                # Overwrite the session state variable with the new modified image
                st.session_state["modified_image"] = modified_image

    def render_sidebar(self):
        with st.sidebar:
            st.header("🔑 Configuration")

            # Use session state to manage API key securely
            if "api_key" not in st.session_state:
                st.session_state["api_key"] = ""

            api_key = st.text_input(
                "Google API Key",
                type="password",
                value=st.session_state["api_key"],
                help="Enter your Google API key to enable thumbnail generation",
                key="api_key_input",
            )

            # Update session state when user changes the key
            if api_key != st.session_state["api_key"]:
                st.session_state["api_key"] = api_key

            if api_key:
                st.success("✅ API key configured")
                # Show a masked version for verification
                masked_key = (
                    api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
                    if len(api_key) > 8
                    else "*" * len(api_key)
                )
                st.info(f"Using key: {masked_key}")
            else:
                st.warning("⚠️ Please enter your Google API key")

            # Add a clear button for security
            if st.button("🗑️ Clear API Key"):
                st.session_state["api_key"] = ""
                st.rerun()

            st.divider()

            # user prompt input
            st.header("🎨 Image Modifier")

            if "user_prompt" not in st.session_state:
                st.session_state["user_prompt"] = ""

            user_prompt = st.text_area(
                "How do you want to modify the image?",
                value=st.session_state["user_prompt"],
                help="Enter your prompt here",
                key="user_prompt_input",
            )

            if user_prompt != st.session_state["user_prompt"]:
                st.session_state["user_prompt"] = user_prompt

            # Style selector
            style_selector = st.selectbox(
                "Select a style",
                ["Neutral", "Funny", "Serious", "Inspiring"],
                index=0,
                key="style_selector",
            )

            if style_selector != st.session_state["style_selector"]:
                st.session_state["style_selector"] = style_selector

            # Generate full prompt
            full_prompt = PromptManager.get_prompt(
                "main_prompt_template",
                user_prompt=user_prompt,
                style_selector=style_selector,
            )

            if st.button("🔄 Generate Image"):
                self.generate_image(
                    st.session_state["img_original"],
                    full_prompt
                )

    def render_image_modifier(self, img_original):
        # Call the sidebar logic for API key/input configuration
        self.render_sidebar()

        st.header("Original Image")
        st.image(img_original, use_column_width=True)

        st.divider()

        # Check for modified image in session state
        if "modified_image" in st.session_state:
            st.header("Modified Image")
            st.image(st.session_state["modified_image"], use_column_width=True)
            # Convert PIL Image to bytes for download
            img_buffer = BytesIO()
            st.session_state["modified_image"].save(img_buffer, format="PNG")
            img_bytes = img_buffer.getvalue()

            left_button, right_button = st.columns([6, 1])

            with left_button:
                st.download_button(
                    label="💾 Download",
                    data=img_bytes,
                    file_name="modified_image.png",
                    mime="image/png",
                )
            with right_button:
                if st.button("🗑️ Delete"):
                    del st.session_state["modified_image"]
                    st.experimental_rerun()
        else:
            st.info("☝️ No modified image found. Please generate an image first.")


def main():
    main_page = MainPage()

    img_original = main_page.render_file_uploader()
    if img_original is not None:
        main_page.render_image_modifier(img_original)


if __name__ == "__main__":
    main()
