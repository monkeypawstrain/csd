'''Rufino Tzunun
Module 5


'''
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
students = MongoClient(url)
db = students.pytech
collection = db.students


docs = collection.find({})

print('\n  -- Displaying Students Documents From find() QUERY --')

for doc in docs:
    
    print(doc)

doc = collection.find_one({"student_id": "1008"})

print('\n-- Displaying Student Document From find_one() QUERY --')

print(doc["student_id"])

input('\n\nEnd of program, press any key to continue... ')