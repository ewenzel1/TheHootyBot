
# This set of code will search for criteria in a post and reply, as well as keeping a list of posts that have already been replied to.

import praw
import pdb
import re
import os
import config

reddit = praw.Reddit(client_id= config.client_id, client_secret= config.client_secret, user_agent= config.user_agent, username= config.username, password= config.password)

if not os.path.isfile("post_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("KSU")
for submission in subreddit.hot(limit=10):
    print(submission.title)

    if submission.id not in posts_replied_to:
        
        if re.search("Covid", submission.title, re.IGNORECASE):
            submission.reply("Hooty Hoo! Wear your mask!")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)

        elif re.search("Corona", submission.title, re.IGNORECASE):
            submission.reply("Hooty Hoo! Wear your mask!")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

    
    
