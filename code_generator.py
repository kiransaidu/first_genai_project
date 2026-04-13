from groq import Groq
from app_config import GROQ_API_KEY
import json

client = Groq(api_key=GROQ_API_KEY)

def generate_code(text):

    prompt = f"""
    Task: {text}

    Rules:
    - return JSON only

    Format:
    {{
      "file": "sample.py",
      "code": "print('hello world')"
    }}
    """

    res = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    content = res.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"file": "sample.py", "code": "print('error')"}