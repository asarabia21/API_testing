import praw

reddit = praw.Reddit(
    client_id="Ez0xGK31vry7_EdElEp2dQ",
    client_secret="dQE-dZcJFQMg8RDNvI6jNyJuMu62KA",
    user_agent="myapp by u/estabanmagnifico",
    #username="",
    #password="",
)

subreddit = reddit.subreddit("cscareerquestions")

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