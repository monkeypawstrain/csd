'''Rudino Tzunun
Module 9.2
7/7/22
'''

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Pollo1994@",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
    }

try:
    
    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  invalid username or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  Database does not exist")

    else:
        print(err)

finally:

    db.close()