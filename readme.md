# TODO
- Get school info from database

# How to run
- gameData.py - store the data into an .csv file
    I was able to run the progress from Visual Code

    cd /Users/marco/Developer/python/environments/dataScrape
    . bin/activate

    python3 ./gameData.py
    deactivate

    I ran the script from VisualCode
    

- storeGameData.py
    cd /Users/marco/Developer/python/environments/dataScrape
    . bin/activate
    
    python ./storeGameData.py
    deactivate

# Tutorials 
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3



# Intro Tutorial w/ good explanations
https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3


# Installing two libraries that we need
pip3 install requests
pip3 install beautifulsoup4

pip install mysql-connector-python


# How to setup the environment 
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

# iOS Installation 
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos

# Sql Information / Sql Connection 

- Thinking of pulling data witht the scraper, adding it to DB
    1. Create an API with Node.js
    2. Play with Django

    https://www.tutorialspoint.com/python/python_database_access.htm

- MySql Commands 
    http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm

    mysql -u sports_admin -p
    foo_Bar$1

    show databases;
    use database {database name}

    show tables;
    select * from bball_games where teamID = 1;
    select opponent, score from bball_games where teamID = 1;
