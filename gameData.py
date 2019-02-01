#!/usr/bin/python3

# Request module to collect a web page
import requests
from bs4 import BeautifulSoup
import csv

from BasketballSchool import BasketballSchool
east = BasketballSchool('Denver East', 'http://www.maxpreps.com/high-schools/denver-east-angels-(denver,co)/basketball/schedule.htm')
broomfield = BasketballSchool('Broomfield', 'http://www.maxpreps.com/high-schools/broomfield-eagles-(broomfield,co)/basketball/schedule.htm')
holyFamily = BasketballSchool('Holy Family', 'http://www.maxpreps.com/high-schools/holy-family-tigers-(broomfield,co)/basketball/schedule.htm')
georgeWashington = BasketballSchool('George Washington', 'http://www.maxpreps.com/high-schools/george-washington-patriots-(denver,co)/basketball/schedule.htm')
lchs = BasketballSchool('Lake County', 'http://www.maxpreps.com/high-schools/lake-county-panthers-(leadville,co)/basketball/schedule.htm')
smokeyHill = BasketballSchool('Smoky Hill', 'http://www.maxpreps.com/high-schools/smoky-hill-buffaloes-(aurora,co)/basketball/schedule.htm')
grandview = BasketballSchool('Grandview', 'http://www.maxpreps.com/high-schools/grandview-wolves-(aurora,co)/basketball/schedule.htm')

schools = []
schools.append(east)
schools.append(broomfield)
schools.append(holyFamily)
schools.append(georgeWashington)
schools.append(lchs)
schools.append(smokeyHill)
schools.append(grandview)

# Create a file to write to, add headers row
f = csv.writer(open('games.csv', 'w'))

def getTagContents(tag) :
    if tag is not None :
        if len(tag) > 0 :
            #print(tag.contents[0])
            return tag.contents[0]


def extractGameData(game):
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
    ##print("\n")
   
for school in schools : 
    f.writerow([school.getSchoolName()])
    f.writerow(['date', 'time', 'oponent', 'location', 'score'])

    # asssign the result of a request 
    page = requests.get(school.getSchoolUrl())
    print(page.status_code)
    print(page.status_code, "for ", school.getSchoolName())

    # Create a BeautifulSoup object, or parse tree
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pulling Text from a web page
    sheduleContainer = soup.find("table", {"id": "schedule"})

    gameList = sheduleContainer.find_all(class_='dual-contest')

    for game in gameList :
        extractGameData(game)

    f.writerow([''])