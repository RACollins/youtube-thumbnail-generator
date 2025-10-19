import streamlit as st
from PIL import Image


class MainPage:
    def __init__(self):
        self.title = "YouTube Thumbnail Generator"
        self.description = "This app generates YouTube thumbnails using AI."

    def render_page_contents(self):
        st.title(self.title)
        st.write(self.description)

        img_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])
        render_elements = False
        if img_file is not None:
            img_original = Image.open(img_file)
            render_elements = True
        else:
            st.info("☝️ Upload a .jpg or .png file")

        if render_elements:
            # Sidebar for user input
            with st.sidebar:
                st.subheader("How do you want to modify the image?")
                user_prompt = st.text_area("Enter your prompt here")

            st.header("Original Image")
            st.image(img_original, use_column_width=True)


def main():
    main_page = MainPage()
    main_page.render_page_contents()


if __name__ == "__main__":
    main()
