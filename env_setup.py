# Add this to the first cell of your Jupyter notebook
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Test that variables are loaded
print("Environment variables loaded:")
print(f"LLAMA_CLOUD_API_KEY: {os.getenv('LLAMA_CLOUD_API_KEY', 'Not found')}")
print(f"NEO4J_URI: {os.getenv('NEO4J_URI', 'Not found')}")
