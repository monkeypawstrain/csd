from pymongo import MongoClient
import certifi

url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
client = MongoClient(url,tlsCAFile=ca)

ca = certifi.where()
students = client.pytech.get_collection("students")
student = {"_id":1003,
"first_name": "Rufino"}
new_student_id = students.insert_one(student).inserted_id
print(new_student_id)
db = client.pytech
#print(db.list_collection_names())W