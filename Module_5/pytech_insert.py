'''Rufino Tzunun
Module 5


'''
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
client = MongoClient(url)
db = client.pytech
students = db.students

students = client.pytech.get_collection("students")
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


students = db.students

print("\n -- INSERT STATEMENTS --")
rufino_student_id = students.insert_one(rufino).inserted_id
print(f"  Inserted student record Rufino Tz into students collection with document_id {str(rufino_student_id)}")

brand_student_id = students.insert_one(brand).inserted_id
print(f"  Inserted student record Brand Tr into students collection with document_id {str(brand_student_id)}")

dom_student_id = students.insert_one(dom).inserted_id
print(f"  Inserted student record Dom Bar into students collection with document_id {str(dom_student_id)}")

input('\n\n  End of program, press any key to exit... ')