import streamlit as st


class MainPage:
    def __init__(self):
        self.title = "YouTube Thumbnail Generator"
        self.description = "This app generates YouTube thumbnails using AI."

    def render(self):
        st.title(self.title)
        st.write(self.description)


def main():
    main_page = MainPage()
    main_page.render()


if __name__ == "__main__":
    main()
