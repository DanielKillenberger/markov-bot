import os

import markovify
import utils
import sys
import re

path = '_chat.txt'


def main():
    if sys.argv[1] is None:
        print('Pass model name as program argument')
        return
    model_name = sys.argv[1]
    with open(path, encoding="utf8") as f:
        content = f.readlines()

    text = ""
    for line in content:
        temp = line.split(':')
        temp = ':'.join(temp[:3]), ':'.join(temp[3:])
        text += re.sub(r'^https?:\/\/.*[\r\n]*', '', temp[1], flags=re.MULTILINE)

    model = markovify.NewlineText(text)

    if not os.path.isdir('models/'):
        os.makedirs('models/')
    utils.export_model(model, model_name)


if __name__ == '__main__':
    main()


