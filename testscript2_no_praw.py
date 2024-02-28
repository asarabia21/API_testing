import requests
from requests.auth import HTTPBasicAuth
import csv
from pprint import pprint

# Reddit API Credentials
client_id = "Ez0xGK31vry7_EdElEp2dQ"
secret = "dQE-dZcJFQMg8RDNvI6jNyJuMu62KA"

# Reddit user credentials
username = "estabanmagnifico"
password = "Monkey5000"

# Reddit API access token
auth = requests.auth.HTTPBasicAuth(client_id, secret)
data = {"grant_type": "password", "username": username, "password": password}
headers = {"User-Agent": "testscript by u/estabanmagnifico"}
r = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
reddit_token = r.json()["access_token"]

# Set up Reddit API headers
headers = {**headers, **{"Authorization": f"bearer {reddit_token}"}}

# Keyword Search
q_list = ["DoD", "Army", "Military"]


for q in q_list:
	permalink_list = []
	r = requests.get(f"https://oauth.reddit.com/r/all/search.jason?q={q}", headers=headers)
	r_json = r.json()
	pprint(r_json)