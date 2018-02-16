#!/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector

# https://stackoverflow.com/questions/25368786/python-print-does-not-work-in-loop
# The link above has the reason why I had to user this function
def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

hostname = 'localhost'
username = 'sports_admin'
password = 'foo_Bar$1'
database = 'sports'

my_print('Using mysql.connector…')
my_print("\n")

myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

icur = myConnection.cursor()
icur.execute('TRUNCATE sports.bball_games')
myConnection.commit()

# url of page we will scrape
basketballSchools = [
    {
        'school': 'Denver East',
        'url':'http://www.maxpreps.com/high-schools/denver-east-angels-(denver,co)/basketball/schedule.htm',
        'teamid': 1
    },
    {
        'school': 'Broomfield',
        'url':'http://www.maxpreps.com/high-schools/broomfield-eagles-(broomfield,co)/basketball/schedule.htm',
        'teamid': 2
    },
    {
        'school': 'Holy Family',
        'url':'http://www.maxpreps.com/high-schools/holy-family-tigers-(broomfield,co)/basketball/schedule.htm',
        'teamid': 3
    },
    {
        'school': 'George Washington',
        'url':'http://www.maxpreps.com/high-schools/george-washington-patriots-(denver,co)/basketball/schedule.htm',
        'teamid': 4
    },
    {
        'school': 'Rock Canyon',
        'url':'http://www.maxpreps.com/high-schools/rock-canyon-jaguars-(highlands-ranch,co)/basketball/schedule.htm',
        'teamid': 5
    },
    {
        'school': 'Smoky Hill',
        'url':'http://www.maxpreps.com/high-schools/smoky-hill-buffaloes-(aurora,co)/basketball/schedule.htm',
        'teamid': 6
    }
]

# Create a file to write to, add headers row
f = csv.writer(open('games.csv', 'w'))

def getTagContents(tag) :
    if tag is not None :
        if len(tag) > 0 :
            #print(tag.contents[0])
            return tag.contents[0]

def insertIntoGames(gameObj) :
    cur = myConnection.cursor()
    
    add_game = ("INSERT INTO sports.bball_games "
                "(teamid, opponent, game_date, game_time, location, score) "
                "values (%s, %s, %s, %s, %s, %s)")

    cur.execute(add_game, gameObj)
    myConnection.commit()

def extractGameData(game, teamid):
    #print(game.find(class_='event-date'))

    # Game Date 
    gameDateTag = game.find(class_='event-date')
    gameDate = getTagContents(gameDateTag)

    # game time
    gameTimeTag = game.find(class_='event-time')
    gameTime = getTagContents(gameTimeTag)

    # opponent
    opponentTag = game.find(class_='contest-type-indicator')
    opponent = getTagContents(opponentTag)


    # contest-location
    gameLocation = game.find(class_='contest-location')
    location = getTagContents(gameLocation)

    # score
    gameScore = game.find(class_='score')
    score = getTagContents(gameScore)

    f.writerow([gameDate, gameTime, opponent, location, score])
    # Need to do a sql insert 
    gameObj = (str(teamid), str(opponent), str(gameDate), str(gameTime), str(location), str(score))
    insertIntoGames(gameObj)

    ##print("\n")
   
for school in basketballSchools : 
    f.writerow([school['school']])
    f.writerow(['date', 'time', 'oponent', 'location', 'score'])

    # asssign the result of a request 
    page = requests.get(school['url'])
    print(page.status_code)

    # Create a BeautifulSoup object, or parse tree
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pulling Text from a web page
    sheduleContainer = soup.find("table", {"id": "schedule"})

    gameList = sheduleContainer.find_all(class_='dual-contest')

    for game in gameList :
        extractGameData(game, school['teamid'])

    f.writerow([''])

myConnection.close()
