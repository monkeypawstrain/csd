'''Rufino Tzunun
Module 5


'''
import certifi
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ptdopkt.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
ca = certifi.where()
client = MongoClient(url,tlsCAFile=ca)

db = client.pytech
students = db.students

student_list = students.find({})

print('\n  -- Displaying Students Documents From find() QUERY --')

for doc in student_list:
    print(f'Student ID: {doc["student_id"]}\nFirst Name: {doc["first_name"]}\nLast Name: {doc["last_name"]}\n')

brand = students.find_one({"student_id": "1008"})

print('\n-- Displaying Student Document From find_one() QUERY --')
print(f'Student ID: {brand["student_id"]}\nFirst Name: {brand["first_name"]}\nLast Name: {brand["last_name"]}')

input('\n\nEnd of program, press any key to continue... ')