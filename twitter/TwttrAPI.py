import requests
import json

def read_config_file(file_path):
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data

#MODIFY PATH TO CONFIG.json file
config = read_config_file('C:\\Users\\adams\\Documents\\GitHub\\API_testing\\twitter\\twitterconfig.json')

# Get the target username
target_username = config.get('target-username')

# Get the methods configuration
methods_config = config.get('endpoints', {})

# Extract individual method configurations
get_user_enabled = methods_config.get('get-user', False)
get_user_followers_enabled = methods_config.get('get-user-followers', False)
get_user_following_enabled = methods_config.get('get-user-following', False)
get_user_likes_enabled = methods_config.get('get-user-likes', False)
get_user_tweets_enabled = methods_config.get('get-user-tweets', False)
get_user_media_enabled = methods_config.get('get-user-media', False)
search_users_enabled = methods_config.get('search-users', False)
search_top_enabled = methods_config.get('search-top', False)
search_latest_enabled = methods_config.get('search-latest', False)
search_images_enabled = methods_config.get('search-images', False)

# Get the output file name
output_file = config.get('output-file', 'output_data.json')

#writes the api response to a json file
def write_response_to_file(api_response, output_file, method_name):
    try:
        # Convert API response to JSON
        response_json = api_response.json()

        # Construct output filename with method name
        output_filename = f"{output_file}_{method_name}.json"

        # Write JSON response to file
        with open(output_filename, 'w') as file:
            json.dump(response_json, file)
        
        print("Response has been written to", output_filename)
    
    except Exception as e:
        print("Error occurred while writing to file:", str(e))


#Global variables for the methods
url = "https://twttrapi.p.rapidapi.com"

querystring = {"username": target_username}

#CHANGE KEY HERE
headers = {
	"X-RapidAPI-Key": "b3e50ce4e9mshf8fdee8d57b9412p190784jsnd95c64fe16bb",
	"X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
}

#Defining methods for pulling information
def get_user(url, username):
    print(f"Getting user data for {username}")
    url += "/get-user"
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "getuser")

def get_followers(url, querystring, username):
    print(f"Getting followers for {username}")
    url += "/user-followers"
    querystring['count'] = '20'
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "getfollowers")

def get_following(url, querystring, username):
    print(f"Getting following for {username}")
    url += "/user-following"
    querystring['count'] = '20'
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "getfollowing")

def get_likes(url, username):
    print(f"Getting likes for {username}")
    url += "/user-likes"
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "getlikes")

def get_tweets(url, username):
    print(f"Getting tweets for {username}")
    url += "/user-tweets"
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "gettweets")

def get_media(url, username):
    print(f"Getting media for {username}")
    url += "/user-media"
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "getmedia")

def search_users(url, querystring, username):
    print(f"Searching for {username}")
    url += "/search-users"
    querystring['query'] = username
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "searchusers")

def search_top(url, querystring, username):
    print(f"Searching for {username}")
    url += "/search-top"
    querystring['query'] = username
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "searchtop")

def search_latest(url, querystring, username):
    print(f"Searching for {username}")
    url += "/search-latest"
    querystring['query'] = username
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "searchlatest")

def search_images(url, querystring, username):
    print(f"Searching for {username}")
    url += "/search-images"
    querystring['query'] = username
    response = requests.get(url, headers=headers, params=querystring)
    write_response_to_file(response, output_file, "searchimages")

# Execute methods based on the configuration
if (get_user_enabled):
    get_user(url, target_username)

if (get_user_followers_enabled):
    get_followers(url, querystring, target_username)

if (get_user_following_enabled):
    get_following(url, querystring, target_username)

if (get_user_likes_enabled):
    get_likes(url, target_username)

if (get_user_tweets_enabled):
    get_tweets(url, target_username)

if (get_user_media_enabled):
    get_media(url, target_username)

if (search_users_enabled):
    search_users(url, querystring, target_username)

if (search_top_enabled):
    search_top(url, querystring, target_username)

if (search_latest_enabled):
    search_latest(url, querystring, target_username)

if (search_images_enabled):
    search_images(url, querystring, target_username)

print("User data saved successfully.")
