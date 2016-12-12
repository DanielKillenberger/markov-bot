import markovify
import json
import utils
import sys


path = '_chat.txt'

model_name = sys.argv[1]
with open(path) as f:
    content = f.readlines()

text = ""
for line in content:
    temp = line.split(':')
    temp = ':'.join(temp[:4]), ':'.join(temp[4:])
    text += temp[1]

model = markovify.NewlineText(text)

utils.export_model(model, model_name)
