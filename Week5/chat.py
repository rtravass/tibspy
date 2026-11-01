import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Ask the model a question
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Your view on Honda CRV"
        }
    ]
)

# Print the model response
print(response.choices[0].message.content)