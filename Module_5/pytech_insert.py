'''Rufino Tzunun
Module 5


'''
import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ptdopkt.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
students = client.pytech.get_collection("students")
students.delete_many({})
def insert_one(student): 
    return students.insert_one(student).inserted_id
print ("-- Insert Statement --")
Antonio = {"student_id": 1007,
    "first_name": "Antonio",
    "last_name": "Bov"}
Antonio_student_id = insert_one(Antonio)
print("Inserted student record {} {} into the students collection with document_id {}".format(Antonio["first_name"], Antonio["last_name"], Antonio_student_id))

ella = {"student_id": 1008,
    "first_name": "Ella",
    "last_name": "Mac"}
ella_student_id = insert_one(ella)
print("Inserted student record {} {} into the students collection with document_id {}".format(ella["first_name"], ella["last_name"], ella_student_id))

Dom = {"student_id": 1009,
    "first_name": "Dom",
    "last_name": "Lom"}
Dom_student_id = insert_one(Dom)
print("Inserted student record {} {} into the students collection with document_id {}".format(Dom["first_name"], Dom["last_name"], Dom_student_id))
input("\n\n  End of program, press any key to exit... ")