from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now you can access the variables
print(f"LLAMA_CLOUD_API_KEY: {os.getenv('LLAMA_CLOUD_API_KEY')}")
print(f"NEO4J_URI: {os.getenv('NEO4J_URI')}")
