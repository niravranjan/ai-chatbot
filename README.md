# AI Chatbot using Gemini API

A simple command-line AI chatbot built in Python, powered by Google's Gemini API through an OpenAI-compatible interface. This project maintains conversation history so the AI remembers context throughout the chat session.

## Features

- Real-time conversational AI in the terminal
- Maintains full conversation history for context-aware replies
- Secure API key handling using environment variables
- Easy to extend or swap with other LLM providers (Groq, OpenAI, etc.)

## Tech Stack

- Python 3.13
- OpenAI Python SDK (used with Gemini's compatible endpoint)
- python-dotenv for environment variable management

## Setup Instructions

1. Clone this repository
```bash
git clone https://github.com/niravranjan/ai-chatbot.git
cd ai-chatbot
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root folder and add your Gemini API key

Get a free API key from [Google AI Studio](https://aistudio.google.com).

5. Run the chatbot
```bash
python chatbot.py
```

## Usage

Once running, simply type your message and press Enter. Type `exit` or `quit` to end the conversation.

## Project Structure

```
ai-chatbot/
├── chatbot.py
├── requirements.txt
├── .env              (not tracked, contains your API key)
├── .gitignore
└── README.md
```

## Author

Built by Nirav Ranjan  as part of learning AI integration with Python.

## License

This project is open source and available for learning purposes.

