# Persona Backend (Flask + Gemini)

This backend powers the chat API for the Persona frontend and generates responses in a custom "Jenny Mam" teaching style using Google Gemini.

## Tech Stack

- Python 3.11
- Flask
- Flask-CORS
- Google GenAI SDK (`google-genai`)
- Vercel Python Runtime (`@vercel/python`)

## Project Structure

```text
Backend/
	api/
		index.py        # Vercel entry point
	chtabot.py        # Main Flask app and /api/chat route
	requirements.txt
	vercel.json
	Readme.md
```

## Prerequisites

- Python 3.11+
- A Google Gemini API key

## Environment Variables

Create a `.env` file in the backend root:

```env
gemini_APIKEY=your_gemini_api_key_here
```

The code reads this exact variable name: `gemini_APIKEY`.

## Local Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the backend:

```bash
python chtabot.py
```

Server starts on `http://127.0.0.1:5001`.
