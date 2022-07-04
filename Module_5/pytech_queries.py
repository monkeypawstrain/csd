<<<<<<< HEAD
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
=======
import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")
>>>>>>> ea1bd79c61412e56d41ab89ffa079f7b90f2b9b5

for doc in docs:
<<<<<<< HEAD
    
    print(doc)

doc = collection.find_one({"student_id": "1008"})

print('\n-- Displaying Student Document From find_one() QUERY --')

print(doc["student_id"])

input('\n\nEnd of program, press any key to continue... ')
=======
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
print()
print ("-- Displaying  Students Documents From find_one() QUERY --") 
doc = students.find_one({"student_id": 1008})
print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])
input("\n\n  End of program, press any key to exit... ")    
>>>>>>> ea1bd79c61412e56d41ab89ffa079f7b90f2b9b5
