# Request module to collect a web page
import requests
from bs4 import BeautifulSoup
import csv

# url of page we will scrape
basketballSchools = [
    {
        'school': 'Denver East',
        'url':'http://www.maxpreps.com/high-schools/denver-east-angels-(denver,co)/basketball/schedule.htm'
    },
    {"INSERT INTO `sports`.`bball_teams` (`teamid`, `team_name`) VALUES (1, 'Denver East')"
        'school': 'Broomfield',
        'url':'http://www.maxpreps.com/high-schools/broomfield-eagles-(broomfield,co)/basketball/schedule.htm'
    },
    {
        'school': 'Holy Family',
        'url':'http://www.maxpreps.com/high-schools/holy-family-tigers-(broomfield,co)/basketball/schedule.htm'
    },
    {
        'school': 'George Washington',
        'url':'http://www.maxpreps.com/high-schools/george-washington-patriots-(denver,co)/basketball/schedule.htm'
    },
    {
        'school': 'Rock Canyon',
        'url':'http://www.maxpreps.com/high-schools/rock-canyon-jaguars-(highlands-ranch,co)/basketball/schedule.htm'
    },
    {
        'school': 'Smoky Hill',
        'url':'http://www.maxpreps.com/high-schools/smoky-hill-buffaloes-(aurora,co)/basketball/schedule.htm'
    }
]

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
        extractGameData(game)

    f.writerow([''])