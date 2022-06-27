'''Rufino Tzunun
Module 6.2

'''
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
students = MongoClient(url)
db = students.pytech
collection = db.students
docs = collection.find({})

print  ("\n -- Displaying Student Documents Find() Query -- ")

##for doc in docs :
    ##print (doc)

print ("-- Displaying Student Documents From find() Query-- ")

for doc in docs:
 for key, value in doc.items():
    print ('{0}: {1}'.format(key, value))

print ("-- Displaying Updated Student Document From find_one () Query-- ")

doc = collection.find_one ({"student_id": "1007"})
print ("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

print("Displaying student documents 1007 from update_one() Query")

doc =  collection.update_one({"student_id": "1007"}, {"$set": {"last_name": "vox"}})
doc = collection.find_one({"student_id": "1007"})
print ("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")








###db.collection.find ({"student_id": "1007"})

'''doc = collection.find_one ({"student_id": "1007"})
print (doc)
rufino = {
    "student_id": "1007",
    "first_name": "Rufino",
    "last_name": "tz",}'''

'''rufino_student_id = collection.insert_one(rufino).inserted_id
print ("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
print (rufino_student_id)

##delete = {""}'''