
from pymongo import MongoClient
# from pymongo import MongoClient

uri = "mongodb+srv://<@password>:@ml-python.gbvlrmn.mongodb.net/?retryWrites=true&w=majority&appName=ML-Python"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


    