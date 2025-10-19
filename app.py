import streamlit as st
from PIL import Image


class MainPage:
    def __init__(self):
        self.title = "YouTube Thumbnail Generator"
        self.description = "This app generates YouTube thumbnails using AI."

    def check_image_file(self, img_file):
        if img_file is not None:
            img_original = Image.open(img_file)
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

    def render_sidebar(self):
        with st.sidebar:
            st.header("🔑 Configuration")

            # Use session state to manage API key securely
            if "api_key" not in st.session_state:
                st.session_state.api_key = ""

            api_key = st.text_input(
                "Google API Key",
                type="password",
                value=st.session_state.api_key,
                help="Enter your Google API key to enable thumbnail generation",
                key="api_key_input",
            )

            # Update session state when user changes the key
            if api_key != st.session_state.api_key:
                st.session_state.api_key = api_key

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
                st.session_state.api_key = ""
                st.rerun()

    def render_image_modifier(self, img_original):
        # Call the sidebar logic for API key/input configuration
        self.render_sidebar()
        # (Other code for modifying the image would go here)


def main():
    main_page = MainPage()

    img_original = main_page.render_file_uploader()
    if img_original is not None:
        main_page.render_image_modifier(img_original)


if __name__ == "__main__":
    main()
