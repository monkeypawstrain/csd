'''Rufino Tzunun
Module 5


'''
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
client = MongoClient(url)
db = client.pytech
students = db.students

student_list = students.find({})

print('\n  -- Displaying Students Documents From find() QUERY --')

for doc in student_list:
    
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

brand = students.find_one({"student_id": "1008"})

print('\n-- Displaying Student Document From find_one() QUERY --')

print("  Student ID: " + brand["student_id"] + "\n  First Name: " + brand["first_name"] + "\n  Last Name: " + brand["last_name"] + "\n")

input('\n\nEnd of program, press any key to continue... ')