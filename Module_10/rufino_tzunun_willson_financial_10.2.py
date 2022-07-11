'''Rudino Tzunun
Module 9.3
7/7/22
'''

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "willson_finacial_user",
    "password": "Pollo1994@",
    "host": "127.0.0.1",
    "database": "willson_finacial",
    "raise_on_warnings": True
    }

db = mysql.connector.connect(**config)
cursor = db.cursor()
DB_NAME = 'willson_finacial'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

TABLES = {}
TABLES['customer'] = (
    "CREATE TABLE `customer` ("
    "  `customer_id`          int             NOT NULL    AUTO_INCREMENT,"
    "  `customer_lname`       varchar(75)     NOT NULL,"
    "  `customer_fname`       varchar(75)     NOT NULL,"
    "  `start_date`           varchar(75)     NOT NULL,"
    "  PRIMARY KEY (`customer_id`)"
    ") ENGINE=InnoDB")

TABLES['account'] = (
    "CREATE TABLE `account` ("
    "  `account_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `account_number`             int             NOT NULL,"
    "  `sec_id`                     int             NOT NULL,"
    "  `account_name`               varchar(75)     NOT NULL,"
    "  `report_id`                  int     NOT NULL,"

    "  PRIMARY KEY (`account_id`)"
    ") ENGINE=InnoDB")

TABLES['transaction'] = (
    "CREATE TABLE `transaction` ("
    "  `transaction_id`                       int           NOT NULL    AUTO_INCREMENT,"
    "  `account_id`                           int           NOT NULL,"
    "  `sec_id`                               int           NOT NULL,"
    "  `transaction_date`                     int   NOT NULL,"
    "  `amount`                               int   NOT NULL,"
    "  `status`                     varchar(75)   NOT NULL,"
    "  PRIMARY KEY (`transaction_id`)"
    ") ENGINE=InnoDB")


TABLES['sec'] = (
    "  CREATE TABLE `sec` ("
    "  `sec_id`                 int             NOT NULL    AUTO_INCREMENT,"
    "  `transaction_date`       int   NOT NULL,"
    "  PRIMARY KEY (`sec_id`)"
    ") ENGINE=InnoDB")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Create table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
# Insert 6 records
add_customer = """INSERT INTO customer (customer_fname, customer_lname, start_date)
               VALUES (%s, %s, %s)"""
    

customer_data = [('Rudino', 'Tzu', '04/04/2022'),
            ('Andrew', 'To', '04/05/2022'),
            ('Dom', 'Tu', '04/09/2022'),
            ('Mary', 'Ann', '05/04/2022'),
            ('Marc', 'Dos', '04/04/2022'),
            ('Ale', 'Ma', '06/04/2022')]
cursor.executemany(add_customer, customer_data)

customer_id = cursor.lastrowid

print('\n  --Custumer List:---  \n')
for customer in customer_data:
    print("\nFirst Name: {}\n Last Name: {} \n Start Date:  {}\n".format(customer[0], customer[1], customer[2],))  

query = "SELECT customer_fname,customer_lname,start_date FROM customer"
cursor.execute(query)
assetss=cursor.fetchall()
db.commit()


cursor.close()
db.close()