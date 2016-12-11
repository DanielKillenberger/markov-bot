import markovify
import json
import utils


path = '_chat.txt'

with open(path) as f:
    content = f.readlines()

text = ""
for line in content:
    temp = line.split(':')
    temp = '_'.join(temp[:4]), '_'.join(temp[4:])
    text += temp[1]

model = markovify.NewlineText(text)

utils.export_model(model, 'rümligruppe')
