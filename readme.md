# 📝 Telegram Channel Summarizer

This project is a Telegram bot that parses new posts from specified Telegram channels within the last 24 hours, generates a summary of these posts using Google Gemini, and sends it to a designated chat.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Features

*   **Channel Parsing:** Gathers posts from a list of public Telegram channels.
*   **Time-based Filtering:** Processes only posts published within the last 24 hours.
*   **AI-Powered Summarization:** Uses Google Gemini to create concise and informative summaries of the posts.
*   **Telegram Messaging:** Publishes the final summary to a specified Telegram chat.
*   **HTML Support:** Sends messages using basic HTML formatting for better readability.

## Technologies

This project uses the following technologies and libraries:
*   **Python:** The primary programming language.
*   **Telethon:** An asynchronous library for interacting with the Telegram API.
*   **Aiogram:** An asynchronous framework for building Telegram bots.
*   **Google Generative AI:** Used to generate post summaries.
*   **python-dotenv:** For managing environment variables.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <project-folder-name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the project, you need to set up your environment variables.

1.  **Create a `.env` file** in the root directory of the project.

2.  **Fill the `.env` file** with your credentials. You can get `API_ID` and `API_HASH` from the [Telegram website](https://my.telegram.org). The `BOT_TOKEN` is provided by [BotFather](https://t.me/BotFather) when you create a new bot. `CHAT_ID` is the ID of your chat with the bot. The `GENAI_API_KEY` can be obtained from [Google AI Studio](https://aistudio.google.com/app/apikey).

    ```env
    BOT_TOKEN="YOUR_BOT_TOKEN"
    CHAT_ID="YOUR_CHAT_ID"
    API_ID="YOUR_API_ID"
    API_HASH="YOUR_API_HASH"
    GENAI_API_KEY="YOUR_GENAI_API_KEY"
    ```

3.  **Configure the channels to parse** in the `config.py` file. Please note that the `CHANNELS` variable is duplicated. Ensure you are using the correct list for the Telethon parser.

    ```python
    # --- Telethon Parser Configuration ---
    # ...
    CHANNELS = ['baxxstudio', 'cgplugin', 'nsuniversity'] # List of channels to parse
    ```

## Usage

To run the parser and send the messages, execute the following command in your terminal:

```bash
python run.py
```