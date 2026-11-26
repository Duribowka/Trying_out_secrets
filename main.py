import os
from dotenv import load_dotenv

load_dotenv()


string = os.getenv("string")

print("Hello " + string + "!")