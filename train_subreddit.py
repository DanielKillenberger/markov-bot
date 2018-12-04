import markovify
import praw
import sys
import json
import utils
import pickle
import os.path

subreddit_ids_saved_path = 'subreddit_ids/'
models_path = 'models/'
models_suffix = '_model.json'


def initialize_subreddit_training(s):
    if not os.path.isfile(subreddit_ids_saved_path + s.display_name):
        subreddit_ids = {'comments': [], 'submissions': []}
        submissions = s.submissions()
        t = ""
        i = 0
        for sub in submissions:
            print(i)
            i += 1
            subreddit_ids['submissions'].append(sub.id)
            if sub.selftext != '[removed]':
                t += sub.selftext
            for comment in sub.comments:
                print(i)
                i += 1
                subreddit_ids['comments'].append(comment.id)
                if sub.selftext != '[removed]':
                    try:
                        t += comment.body
                    except AttributeError:
                        print('comment has no body')

        pickle.dump(subreddit_ids, open(subreddit_ids_saved_path + s.display_name, "wb"))
        model = markovify.Text(t)
        utils.export_model(model, 'subreddit_' + s.display_name)
    else:
        print('This subreddit has already been trained')
        print('If you want to start over delete the according file in ' + subreddit_ids_saved_path)
        print('Otherwise use update_subreddit_training(s)')


def update_subreddit_training(s):

    if os.path.isfile(subreddit_ids_saved_path + s.display_name) and \
            os.path.isfile(models_path + 'subreddit_' + s.display_name + models_suffix):

        subreddit_ids = pickle.load(open(subreddit_ids_saved_path + s.display_name, "rb"))
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
            for comment in sub.comments:
                if comment.id not in subreddit_ids['comments']:
                    subreddit_ids['comments'].append(comment.id)
                    if comment.body != '[removed]':
                        try:
                            t += comment.body
                        except AttributeError:
                            print('comment has no body')

        if not t == "":
            model = markovify.Text(t)
            with open(models_path + s.display_name + models_suffix) as model_file:
                model_loaded = markovify.Text.from_json(json.load(model_file))
                model = markovify.combine(model, model_loaded)
            utils.export_model(model, 'subreddit_' + s.display_name)

    else:
        print('Subreddit model has not been initialized yet')
        print('Please use initialize_subreddit_training(s) ')


credentials = open('reddit_credentials.json').read()
credentials = json.loads(credentials)

reddit = praw.Reddit(user_agent=str(credentials['user_agent']),
                     client_id=str(credentials['client_id']),
                     client_secret=str(credentials['client_secret']))


subreddit_strings = list(map(lambda x: str(x), sys.argv[1:len(sys.argv)]))
subreddits = []
for subreddit_string in subreddit_strings:
    subreddits.append(reddit.subreddit(subreddit_string))

for subreddit in subreddits:
    initialize_subreddit_training(subreddit)
