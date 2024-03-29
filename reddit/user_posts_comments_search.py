import praw
import os
import urllib.request
import configparser

# Read config file for api and login credentials
config = configparser.ConfigParser()
config.read('config.ini')

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

# Define a function to fetch a user's posts
def fetch_user_posts(username, post_limit=10):
    user = reddit.redditor(username)
    print(f"\nFetching posts from u/{username}:")
    for submission in user.submissions.new(limit=post_limit):
        print(submission.title)

# Define a function to fetch a user's comments
def fetch_user_comments(username, comment_limit=10):
    user = reddit.redditor(username)
    print(f"\nFetching comments from u/{username}:")
    for comment in user.comments.new(limit=comment_limit):
        print(comment.body)

# Define a function to fetch a user's subscribed subreddits
def fetch_user_subscriptions(username):
    user = reddit.redditor(username)
    print(f"\nFetching subscribed subreddits of u/{username}:")
    for subscription in user.subreddits():
        print(subscription.display_name)

# Main function to execute the script
def main():
    username = 'toyotausa'

    # Fetch posts from a user
    fetch_user_posts(username)

    # Fetch comments from a user
    fetch_user_comments(username)

    # Fetch subscribed subreddits of a user
    # fetch_user_subscriptions(username)

# Execute the main function
if __name__ == "__main__":
    main()
