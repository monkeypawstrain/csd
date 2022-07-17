# Team Delta
# Rufino Tzunun
# Christopher Clausen
# Moises Herrera
# Module 11 Milestone #3 Wilson Financial


import mysql.connector

config = {
    "user": "root",
    "password": "Pollo1994@",
    "host": "127.0.0.1",
    "database": "willson_finacial",
    "raise_on_warnings": False
    }



db = mysql.connector.connect(**config)
cursor = db.cursor()

# Generate report on clients added in the last 6 months
cursor.execute("""SELECT cl_name AS Client, cl_date_added AS Date_Joined
                    FROM Client 
                    WHERE cl_date_added > '2022-01-12';
                """)
dates = cursor.fetchall()

print("-- DISPLAYING CLIENTS ADDED W/IN LAST 6 MONTHS --")
for date in dates:
    print("Client: {}".format(date[0]))
    print("Date Added: {}".format(date[1]))
    print()

# Generate report on average assets (in currency)
cursor.execute("""SELECT COUNT(cl_id) AS Num_of_Clients,
                         SUM(order_unit_price) AS Client_Total,
                         FORMAT(
                            ((SUM(order_unit_price) / COUNT(order_unit_price))), 'c') 
                                AS Average
                    FROM Transaction
                    ORDER BY Num_of_Clients, Client_Total, Average;
                """)
transactions = cursor.fetchall()

print("-- DISPLAYING AVERAGE of ASSETS --")
for transaction in transactions:
    print("Number of Clients: {}".format(transaction[0]))
    print("Sum of Client Transactions: ${}".format(transaction[1]))
    print("Average Assets: ${}".format(transaction[2]), "rounded")
    print()

# Generate report on transactions >= 10
cursor.execute("""SELECT cl_name AS Client,
                         order_shares_traded AS Num_of_Transactions
                    FROM Client, Transaction
                    WHERE Client.cl_id = Transaction.cl_id
                        AND order_shares_traded >= 10
                    ORDER BY order_shares_traded DESC;
                """)
clients = cursor.fetchall()

print("-- DISPlAYING TRANSACTIONS GREATER THAN 10 --")
for client in clients:
    print("Client: {}".format(client[0]))
    print("Number of Transactions: {}".format(client[1]))
    print()