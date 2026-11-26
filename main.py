import os
from dotenv import load_dotenv

load_dotenv()

#harmless string for testing
string = os.getenv("string")

print("Hello " + string + "!")