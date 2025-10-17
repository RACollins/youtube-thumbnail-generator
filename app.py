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
            original_file_details = {
                "Filename": img_file.name,
                "FileType": img_file.type,
                "FileSize": img_file.size,
            }
            img_original = Image.open(img_file)
            original_width, original_height = img_original.size
            original_image_details = {
                "Width": "{} px".format(original_width),
                "Height": "{} px".format(original_height),
            }
            render_elements = True
        else:
            st.info("☝️ Upload a .jpg or .png file")

        if render_elements:
            st.header("Original Image")
            st.image(img_original, use_column_width=True)
            st.write(original_file_details)
            st.write(original_image_details)


def main():
    main_page = MainPage()
    main_page.render_page_contents()


if __name__ == "__main__":
    main()
