'''Rufino Tzunun
Module 5


'''
from pymongo import MongoClient
<<<<<<< HEAD
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
students = MongoClient(url)
db = students.pytech
collection = db.students
=======
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")
students.delete_many({})
def insert_one(student): 
    return students.insert_one(student).inserted_id
    
print ("-- Insert Statement --")
bill = {"student_id": 1007,
    "first_name": "Bill",
    "last_name": "Jackson"}
bill_student_id = insert_one(bill)
print("Inserted student record {} {} into the students collection with document_id {}".format(bill["first_name"], bill["last_name"], bill_student_id))
>>>>>>> ea1bd79c61412e56d41ab89ffa079f7b90f2b9b5


<<<<<<< HEAD
rufino = {
    "student_id": "1007",
    "first_name": "Rufino",
    "last_name": "tz",

}

brand = {
    "student_id": "1008",
    "first_name": "Brand",
    "last_name": "Tr",
}

dom = {
    "student_id": "1009",
    "first_name": "Dom",
    "last_name": "Bar",
}


print("\n -- INSERT STATEMENTS --")
rufino_student_id = collection.insert_one(rufino).inserted_id
print(f"  Inserted student record Rufino Tz into students collection with document_id {str(rufino_student_id)}")

brand_student_id = collection.insert_one(brand).inserted_id
print(f"  Inserted student record Brand Tr into students collection with document_id {str(brand_student_id)}")

dom_student_id = collection.insert_one(dom).inserted_id
print(f"  Inserted student record Dom Bar into students collection with document_id {str(dom_student_id)}")

input('\n\n  End of program, press any key to exit... ')
=======
kim = {"student_id": 1009,
    "first_name": "Kim",
    "last_name": "Jackson"}
kim_student_id = insert_one(kim)
print("Inserted student record {} {} into the students collection with document_id {}".format(kim["first_name"], kim["last_name"], kim_student_id))
input("\n\n  End of program, press any key to exit... ")
>>>>>>> ea1bd79c61412e56d41ab89ffa079f7b90f2b9b5
