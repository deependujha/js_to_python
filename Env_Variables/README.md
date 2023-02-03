# Environment  variables in python ㊙️🤫


### General process:

1. Store the environment variables in a **.env** file.

**Note:**<div style="color:red;"> The .env file should not be checked into <b>version control </b> and should only be stored on the development and production environments.</div>

2. Use a library, such as **python-dotenv**, to load the environment variables from the file into your Python code.

---

### Code:

1. Create a .env file in the root of your project and store the environment variables in it, one per line, in the format VAR_NAME=value. For example:
```sh
API_KEY=abcdefghijklmnopqrstuvwxyz
DEBUG=True
```

2. Install the python-dotenv library using pip:
```sh
pip install python-dotenv
```

3. Load the environment variables in your code by adding the following code at the top of your main Python file:
   
```py
import os
from dotenv import load_dotenv

load_dotenv()

# Get the value of an environment variable
value_api_key = os.getenv("API_KEY")
value_debug = os.getenv("DEBUG")
print(f"value of api key is: {value_api_key}")
print(f"value of debug is: {value_debug}")
```