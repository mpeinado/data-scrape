#!/usr/bin/python
import sys

# https://stackoverflow.com/questions/25368786/python-print-does-not-work-in-loop
# The link above has the reason why I had to user this function
def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

hostname = 'localhost'
username = 'sports_admin'
password = 'foo_Bar$1'
database = 'sports'


def doQuery(conn) :
    cur = conn.cursor()

    cur.execute("SELECT * from bball_teams")

    for row in cur.fetchall() :
        my_print(row[0])
        my_print("\n")
        my_print(row[1])

def insertIntoGames(conn) :
    cur = conn.cursor()
    
    add_game = ("INSERT INTO sports.bball_games "
                "(teamid, opponent, game_date, game_time, location, score) "
                "values (%s, %s, %s, %s, %s)")

    data_game = (1, 'South', "2018-01-09", '9:00pm', 'Denver South', '98-89')

    cur.execute(add_game, data_game)

    conn.commit()

my_print('Using mysql.connector…')
my_print("\n")
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
insertIntoGames(myConnection)
myConnection.close()