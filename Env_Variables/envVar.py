import os
from dotenv import load_dotenv

load_dotenv()

# Get the value of an environment variable
value_api_key = os.getenv("API_KEY")
value_debug = os.getenv("DEBUG")
print(f"value of api key is: {value_api_key}")
print(f"value of debug is: {value_debug}")