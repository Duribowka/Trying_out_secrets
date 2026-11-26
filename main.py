import os
from dotenv import load_dotenv

load_dotenv()

#harmless string for testing
#and another one
file_path = "/home/archuser/Desktop/Gthub-Secret/Server/Trying_out_secrets/test.txt"
#mueheheheheh
#hahaha
string = os.getenv("string")

print("Hello " + string + "!")
with open(file_path, "a") as f:
    f.write(string)