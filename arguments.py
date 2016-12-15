import argparse


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser()

parser.add_argument('model_name', type=str,
                    help='Specify model_name to train with specified text sources.\n'
                         'If the specified model already exists, the new model and the existing will be combined.')
parser.add_argument('-s', '--subreddits', type=str,
                    help='String of subreddit names each followed by its weight(optional default = 1)\n'
                         'For example: "ELI5 1 AskReddit 0.5"')
parser.add_argument('-wa', '--whatsapp', type=str,
                    help='String of paths to whatsapp logs each followed by its weight(optional default = 1)\n'
                         'For example: "_chat.txt 1"')
parser.add_argument('-a', '--articles', type=str,
                    help='String of links to articles each followed by its weight(optional default = 1)')
parser.add_argument('-af', '--articlesFromFile', type=str,
                    help='Path to text file with stored links to articles.'
                         'Every link must be on a new line followed by one space and the corresponding weight'
                         '(optional default = 1)')

