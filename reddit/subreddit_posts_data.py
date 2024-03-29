import praw
import configparser

# Read config file for api and login credentials
config = configparser.ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(
    client_id = config.get('config', 'client_id'),
    client_secret = config.get('config', 'client_secret'),
    user_agent=config.get('config', 'user_agent'),
    username = config.get('config', 'username'),
    password = config.get('config', 'password')
)

subreddit = reddit.subreddit("OSINT")

top_posts = subreddit.top(limit=10)
top_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title - ",post.title)
    print("ID - ", post.id)
    print("Author - ", post.author)
    print("URL -", post.url)
    print("Score - ", post.score)
    print("Comment count - ", post.num_comments)
    print("Created - ", post.created_utc)
    print("\n")