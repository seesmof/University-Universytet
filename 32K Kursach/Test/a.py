
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

user='seesmof'
password='9BnPXNrq40RmohNR'
uri = f"mongodb+srv://{user}:{password}@cluster0.y7yhp7s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    db=client.get_database('sample_mflix')
    users=db.get_collection('users')

    q={'name': {'$regex':'Jon'}}
    user=users.find_one(q)

    print(user)
    print(user['email'])
    client.close()
except Exception as e:
    print(e)