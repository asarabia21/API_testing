import praw
import os
import urllib.request
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

# Retreive images from a subreddit based on keyword. Image files are saved to desired location
keyword = 'Tacoma'
subreddit = reddit.subreddit('Toyota')
results = subreddit.search(keyword, limit=75)
save_directory = "# enter path here"
for result in results:
    if result.url.endswith('.jpg') or result.url.endswith('.png'):
        try:
            #create the full path to save the image in the directory
            file_path = os.path.join(save_directory, f"{result.id}.jpg")
            urllib.request.urlretrieve(result.url, file_path)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print('Image not found:', result.url)
            else:
                raise


# Retreives images from a subreddit until limit is reached (no keyword as above); saves to current directory. 
subreddit = reddit.subreddit("Toyota")
count = 0

# Iterate through top submissions
for submission in subreddit.top(limit=None):

    # Get the link of the submission
    url = str(submission.url)

    # Check if the link is an image
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

        # Retrieve the image and save it in current folder
        urllib.request.urlretrieve(url, f"image{count}")
        count += 1

        # Stop once you have 10 images
        if count == 10:
            break