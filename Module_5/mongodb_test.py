import certifi
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.nwh5cip.mongodb.net/retryWrites=true&w=majority",
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)
db = client.pytech
print("--Pytech Collection List")
print(db.list_collection_names())
input("\n\n End of the program,press any key to exit.. ")
#students = client.pytech.get_collection("students")
#student = {"_id":1003,
#"first_name": "Rufino"}
#new_student_id = students.insert_one(student).inserted_id
#print(new_student_id)

#print(db.list_collection_names())W