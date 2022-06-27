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
docs = collection.find({})
for doc in docs:
 for key, value in doc.items():
    print ('{0}: {1}'.format(key, value))


print ("-- Displaying Updated Student Document From find_one () Query-- ")
geo = {
    "student_id": "1010",
    "first_name": "Geo",
    "last_name": "Dur",
}

print ("--Display New Student List Doc-- ")
geo_student_id = collection.insert_one(geo).inserted_id
print("Inserted student record Geo Dur into student collections with document_id " )
print (geo_student_id)
print("Displaying Student new list")
print(geo)
docs = collection.find({})
for doc in docs:
 for key, value in doc.items():
    print ('{0}: {1}'.format(key, value))

print("Deleted student 1010")
delete = {"student_id": "1010"}
deleted =  collection.delete_one(delete)
docs = collection.find({})

for doc in docs:
 for key, value in doc.items():
    print ('{0}: {1}'.format(key, value))