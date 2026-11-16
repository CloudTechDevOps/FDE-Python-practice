
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="explain aws in two lines",
    model="openai/gpt-oss-20b",
)
print(response.output_text)

## import OS
# os is python built-in module.
# It provides functions to interact with the operating system.
# we can use it to access environment variables.


## from openai import OpenAI
# openai is an external python package.
# OpenAI is a class available inside that package.

# from dotenv import load_dotenv
# dotenv comes from external python-dotenv package.
# load_dotenv is a function.
