import requests
from requests.auth import HTTPBasicAuth
import csv
from pprint import pprint

# Reddit API Credentials
client_id = "Ct-3GfVL4b5POH-Q3fdiSQ"
secret = "X-JF_RAbNYo-S76wYqW0iwbumwzdgQ"

# Reddit user credentials
username = "estabanmagnifico"
password = "Monkey5000"

# Reddit API access token
auth = requests.auth.HTTPBasicAuth(client_id, secret)
data = {"grant_type": "password", "username": username, "password": password}
headers = {"User-Agent": "testscript2_no_praw by u/estabanmagnifico"}
r = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
reddit_token = r.json()["access_token"]

# Set up Reddit API headers
headers = {**headers, **{"Authorization": f"bearer {reddit_token}"}}

# Keyword Search
q_list = ["OSINT"]

for q in q_list:
	permalink_list = []
	r = requests.get(f"https://oauth.reddit.com/r/all/search.json?q={q}", headers=headers)
	r_json = r.json()
	#pprint(r_json)
	for post in r_json["data"]["children"]:
		permalink = f"https://www.reddit.com{post['data']['permalink']}"
		print(permalink)
		permalink_list.append([permalink])
	with open(f"{q.replace(' ', '-')}.csv", "w", newline='') as file:
		writer = csv.writer(file)
		writer.writerows(permalink_list)

	



