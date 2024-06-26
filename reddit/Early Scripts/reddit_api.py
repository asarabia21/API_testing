import requests
import configparser
import json

#Read the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Define client credentials
client_id = config.get('config', 'client_id')
client_secret = config.get('config', 'client_secret')

# Define user credentials
username = config.get('config', 'username')
password = config.get('config', 'password')

#Define target username and search parameters
target_username = config.get('config', 'target_user')

#Define the search parameters
sort = config.get('config', 'sort')
t = config.get('config', 'timeframe')
limit = config.get('config', 'limit')

#Define the file path
file_path = config.get('config', 'file_path')

# Define data payload
data = {
    "grant_type": "password",
    "username": username,
    "password": password
}

# Define headers
headers = {
    "User-Agent": "MyAPI/0.1 by YoursTruly"
}

# Encode client ID and secret for basic authentication
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

# Make the request
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)

# Check response
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']

    #defining headers for further requests with token
    headers_with_token = {
        "Authorization": f"bearer {access_token}",
        "User-Agent": "MyAPI/0.1 by YoursTruly"
    }

    # Make certain requests using the access token, just change the url in the following line
    # view requests at https://www.reddit.com/dev/api
    # /api/v1/me - info about your account
    # /user/username/about
    # /user/username/comments
    # /user/username/upvoted
    # /user/username/overview

    response = requests.get(f"https://oauth.reddit.com/user/{target_username}/comments?sort={sort}&t={t}&limit={limit}", headers=headers_with_token)


    # Check response
    if response.status_code == 200:
        user_data = response.json()
        print("User data:", user_data)

        # Write the JSON data to the file
        with open(file_path, "w") as file:
            json.dump(user_data, file)

        print("User data saved successfully.")

    else:
        print("Failed to retrieve user data. Response code:", response.status_code)

else:
    print("Failed to retrieve token. Response code:", response.status_code)
