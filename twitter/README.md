SETUP:

Visit https://rapidapi.com/twttrapi-twttrapi-default/api/twttrapi and create a free account to be able to subscribe to the API

Under the "code snippets" section on the right column, look for the "X-RapidAPI-Key" and copy it

In TwttrAPI.py 

    paste this in the headers section
    modify path to config.json file

USE:

In twitterconfig.json 

    modify target username with a valid twitter handle or some words to put in the search bar to use the search tools
    toggle desired requests as either "true" or "false"
    modify output file name

Run TwttrAPI.py with the following caveats: 

Free plan only allows for 100 requests a month that are under their "Scraping & Searching" Category. 
Any get request is limited to the first 20 responses in any list and can't be modified with a free account

