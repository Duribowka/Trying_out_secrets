import os
from dotenv import load_dotenv

load_dotenv()

#harmless string for testing
#and another one
#mueheheheheh
string = os.getenv("string")

print("Hello " + string + "!")