# Talking with an Image

This project demonstrates an interactive application that allows users to ask questions about uploaded images using Google's Gemini 2.5 Flash model. It includes both a Streamlit web application and a Jupyter Notebook for experimenting with the model.

## Features

*   **Image Upload:** Users can upload `.jpg`, `.jpeg`, `.png`, and `.gif` image files.
*   **Question Answering:** Ask questions about the content of the uploaded image.
*   **Gemini 2.5 Flash Integration:** Utilizes the [`gemini-2.5-flash`](https://ai.google.dev/models/gemini) model for generating answers.
*   **Chat History (Streamlit):** Maintains a history of questions and answers within the Streamlit application.
*   **Jupyter Notebook:** Provides an interactive environment to test the image-to-text functionality.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd py-talk-image
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    The project relies on the packages listed in [requirements.txt](requirements.txt).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Google API Key:**
    Create a `.env` file in the project root directory (as ignored by [.gitignore](.gitignore)) and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    You can obtain a Google API Key from the [Google AI Studio](https://ai.google.dev/gemini/create-api-key).

## Usage

### Streamlit Application

Run the Streamlit application from your terminal:

```bash
streamlit run main.py