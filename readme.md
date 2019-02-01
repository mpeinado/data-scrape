
https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3

. bin/activate
deactivate

# Tutorials 
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

@LEFT Removing Superfluous Data


# Intro Tutorial w/ good explanations
https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3


# Installing two libraries that we need
pip3 install requests
pip3 install beautifulsoup4


# How to setup the environment 
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

# iOS Installation 
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos

# Sql 
https://www.tutorialspoint.com/python/python_database_access.htm
    Thinking of pulling data witht the scraper, adding it to DB
        1. Create an API with Node.js
        2. Play with Django

# How to run
- gameData.py - store the data into an .csv file
I was able to run the progress from Visual Code

cd /Users/marco/Developer/python/environments/dataScrape
. bin/activate

python3 ./gameData.py

I ran the script from VC
deactivate

- storeGameData.py
. bin/activate

// do not need to specify the version of python since the file sets it at the top
python ./storeGameDate.py
# MySql Connection 
pip install mysql-connector-python


mysql -u sports_admin -p
foo_Bar$1

show databases;
use database {database name}

show tables;
select * from bball_games where teamID = 1;
select opponent, score from bball_games where teamID = 1;