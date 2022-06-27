'''Rufino Tzunun
Module 5


'''
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
client = MongoClient(url)
db = client.pytech
students = db.students

docs = students.find({})

print('\n  -- Displaying Students Documents From find() QUERY --')

for doc in docs:
    
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

doc = students.find_one({"student_id": "1008"})

print('\n-- Displaying Student Document From find_one() QUERY --')

print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input('\n\nEnd of program, press any key to continue... ')