import praw
import json
import pickle
import os.path

subreddit_ids_saved_path = 'subreddit_ids/'
models_path = 'models/'
models_suffix = '_model.json'


def parse_subreddit(subreddit_string):
    s = reddit.subreddit(subreddit_string)
    if os.path.isfile(subreddit_ids_saved_path + s.display_name) and \
            os.path.isfile(models_path + 'subreddit_' + s.display_name + models_suffix):

        subreddit_ids = pickle.load(open(subreddit_ids_saved_path + s.display_name, "rb"))

    else:
        subreddit_ids = {'comments': [], 'submissions': []}

    submissions = s.submissions()
    t = ""
    i = 0
    for sub in submissions:
        if sub.id not in subreddit_ids['submissions']:
            print(i)
            i += 1
            subreddit_ids['submissions'].append(sub.id)
            if sub.selftext != '[removed]':
                t += sub.selftext
        for c in sub.comments:
            if c.id not in subreddit_ids['comments']:
                print(i)
                i += 1
                subreddit_ids['comments'].append(c.id)
                if c.body != '[removed]':
                    t += c.body
    return t

# load credentials and create reddit instance
credentials = open('credentials.json').read()
credentials = json.loads(credentials)

reddit = praw.Reddit(user_agent=str(credentials['user_agent']),
                     client_id=str(credentials['client_id']),
                     client_secret=str(credentials['client_secret']))

