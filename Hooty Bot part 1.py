import praw
import os

reddit = praw.Reddit(client_id= 'pn1O_cEZ5eHKGQ', client_secret= 'X8UXFGmveFsLjUjMXMuHDIgzSze0tQ', user_agent= 'Hooty Bot 0.1')
subreddit = reddit.subreddit('KSU')

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------------------\n")





