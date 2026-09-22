# TinyLlama Chat — Streamlit App

A simple Streamlit interface for chatting with a Hugging Face-hosted LLM via LangChain.

## Project Structure

```
├── prompt_streamlitapp.py   # Main Streamlit app (self-contained)
├── requirements.txt         # Python dependencies
└── .gitignore
```

## Setup

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   *(On macOS/Linux: `source venv/bin/activate`)*

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   This app requires a Hugging Face API token. Create a `.env` file in the project root (this file is not committed — see `.gitignore`):
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   ```

   Get a token from https://huggingface.co/settings/tokens.

## Running Locally

```
streamlit run prompt_streamlitapp.py
```

The app will open at `http://localhost:8501`.

## Deployment

When deploying (e.g. Streamlit Community Cloud or Hugging Face Spaces), do not upload your `.env` file. Instead, add `HUGGINGFACEHUB_API_TOKEN` through the platform's secrets manager:

- **Streamlit Community Cloud**: App settings → Secrets
- **Hugging Face Spaces**: Space settings → Repository secrets

## Notes

- Not all models on the Hugging Face Hub are available through the hosted Inference API — check a model's page for an active "Inference Providers" section before using it.

## Author

Fawad Ahmad Bilal
