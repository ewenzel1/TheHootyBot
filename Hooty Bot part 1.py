import praw
import os
import config


reddit = praw.Reddit(client_id= config.client_id, client_secret= config.client_secret, user_agent= config.user_agent, username= config.username, password= config.password)

subreddit = reddit.subreddit('KSU')

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------------------\n")


# This file runs in addition to a config.py file that includes all of the login information.






