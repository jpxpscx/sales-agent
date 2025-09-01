# test_groq.py
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Read API key
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

print("GROQ_API_KEY loaded:", groq_key[:8] + "..." )  # Print first few chars only for safety

# Initialize Groq model with your API key
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=groq_key)

# Test the model
response = llm.invoke([{"role": "user", "content": "Say hello"}])

# Print response
print("Response from Groq:", response.content)
