import os
from dotenv import load_dotenv

load_dotenv()

USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')
print(PASSWORD,type(PASSWORD))