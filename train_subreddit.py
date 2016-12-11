import markovify
import praw
import sys
import json
import utils
credentials = open('credentials.json').read()
credentials = json.loads(credentials)

reddit = praw.Reddit(user_agent=str(credentials['user_agent']),
                     client_id=str(credentials['client_id']),
                     client_secret=str(credentials['client_secret']))


subreddit_string = str(sys.argv[1])
subreddit = reddit.subreddit(subreddit_string)
text = ""

for submission in subreddit.hot():
    text += submission.selftext
    for comment in submission.comments:
        text += comment.body

text_model = markovify.Text(text)
utils.export_model(text_model, subreddit_string)



