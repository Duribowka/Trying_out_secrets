import os
from dotenv import load_dotenv

load_dotenv()

#harmless string for testing
#and another one
#mueheheheheh
#hahaha
string = os.getenv("string")

print("Hello " + string + "!")
with open("test.txt", "a") as f:
    f.write(string)