'''Rufino Tzunun
Module 5


'''
import certifi
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
db = client.pytech
print("--Pytech Collection List")
print(db.list_collection_names())
input("\n\n End of the program,press any key to exit.. ")