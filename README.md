# YouTube Thumbnail Generator

An AI-powered Streamlit application that generates eye-catching YouTube thumbnails using Google's Gemini 2.5 Flash Image model.

**🌐 Live App:** TBC

## Features

- 🎨 **AI-Powered Image Generation** - Transform your images into compelling YouTube thumbnails using Google's Gemini API
- 🖼️ **Image Upload** - Support for JPG, PNG, and JPEG formats
- 💬 **Custom Prompts** - Describe how you want to modify your thumbnail
- 🎭 **Style Selection** - Choose from different styles: Neutral, Funny, Serious, or Inspiring
- 📥 **Download Results** - Download your generated thumbnails instantly
- 🔒 **Secure API Key Management** - Safe handling of your Google API key with masked display

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Google API key with access to Gemini API

## Installation

This project uses `uv` for dependency management. If you don't have `uv` installed:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

### Setup Project Environment

Clone the repository and set up the environment:

```bash
# Clone the repository
git clone <repository-url>
cd youtube-thumbnail-generator

# Create virtual environment and install dependencies
uv sync
```

This will create a virtual environment and install all dependencies specified in `pyproject.toml`.

## Usage

### Running the Streamlit App

To launch the web application locally:

```bash
# Activate the virtual environment and run the app
uv run streamlit run app.py
```

The app will open in your default browser (typically at `http://localhost:8501`).

**Using the App:**
1. Enter your Google API key in the sidebar
2. Upload an image (JPG, PNG, or JPEG)
3. Provide instructions on how to modify the image
4. Select a style (Neutral, Funny, Serious, or Inspiring)
5. Click "Generate Image"
6. Download your modified thumbnail

### Running the API Test Script

To test the API directly without the UI:

```bash
# Create a .env file with your API key
echo "API_KEY=your_google_api_key_here" > .env

# Run the test script
uv run python api_test.py
```

The test script will:
- Load your API key from the `.env` file
- Process an image from `images/input/`
- Generate a thumbnail based on the predefined prompt
- Save the result to `images/output/generated_image.png`

## Project Structure

```
youtube-thumbnail-generator/
├── app.py                      # Main Streamlit application
├── api_test.py                 # Standalone API test script
├── main.py                     # Alternative entry point
├── pyproject.toml              # Project dependencies and metadata
├── uv.lock                     # Locked dependency versions
├── images/
│   ├── input/                  # Place your source images here
│   └── output/                 # Generated thumbnails are saved here
├── prompts/
│   ├── prompt_manager.py       # Jinja2 template manager for prompts
│   └── templates/
│       └── main_prompt_template.j2  # Main prompt template
└── README.md
```

## Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini API](https://ai.google.dev/)** - AI image generation (gemini-2.5-flash-image model)
- **[Pillow](https://python-pillow.org/)** - Image processing
- **[Jinja2](https://jinja.palletsprojects.com/)** - Prompt templating
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver

## How It Works

1. The app uses a template-based prompt system (Jinja2) to generate structured prompts
2. Your uploaded image and generated prompt are sent to Google's Gemini 2.5 Flash Image model
3. The AI model modifies the image according to your specifications and style
4. The result is displayed in the app and can be downloaded

## Environment Variables

For the API test script, create a `.env` file in the project root:

```
API_KEY=your_google_api_key_here
```

For the Streamlit app, you can enter your API key directly in the sidebar (it's stored in session state and not persisted).

## License

See [LICENSE](LICENSE) file for details