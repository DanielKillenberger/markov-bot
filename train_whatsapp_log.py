import markovify
import json
import utils
import sys
import re


path = '_chat.txt'

model_name = sys.argv[1]
with open(path) as f:
    content = f.readlines()

text = ""
for line in content:
    temp = line.split(':')
    temp = ':'.join(temp[:4]), ':'.join(temp[4:])
    text += re.sub(r'^https?:\/\/.*[\r\n]*', '', temp[1], flags=re.MULTILINE)

model = markovify.NewlineText(text, state_size=2)

utils.export_model(model, model_name)
