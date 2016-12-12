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


subreddit_strings = list(map(lambda x: str(x), sys.argv[1:len(sys.argv)]))
subreddits = []
for subreddit_string in subreddit_strings:
    subreddits.append(reddit.subreddit(subreddit_string))
text = ""

for subreddit in subreddits:
    for submission in subreddit.hot():
        text += submission.selftext
        for comment in submission.comments:
            text += comment.body

text_model = markovify.Text(text)
utils.export_model(text_model, subreddit_strings[0])



