import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

_ = load_dotenv(Path(__file__).parent / ".env")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", ""),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.airforce/v1"),
)
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hi"}],
)
print(resp.choices[0].message.content)
